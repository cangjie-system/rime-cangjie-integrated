#!/usr/bin/env python3
"""將 resources/ 下的資料轉換為 .yaml
"""

import os
import argparse
import logging
import re

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
log = logging.getLogger()

root = os.path.normpath(os.path.join(__file__, '..', '..'))

def is_punc(text):
    code = ord(text[0])
    return code < 0x3400 or 0xFF00 <= code <= 0xFFEF

def is_cjk_comp(text):
    code = ord(text[0])
    return 0xF900 <= code <= 0xFAD9 or 0x2F800 <= code <= 0x2FA1D

def is_pua(text):
    code = ord(text[0])
    return 0xE000 <= code <= 0xF8FF or 0xF0000 <= code <= 0x10FFFF

def import_cjsys():
    """匯入倉頡平台（馬來西亞·倉頡之友）
    """
    # 結尾非「難」字表
    # 用於確認三代結尾為「難」的字不是重複字
    map_non_x = {}

    # 結尾非「難」字排除表
    # 這些字應視為倉頡碼以「難」結尾，
    # 但它們在五代編碼結尾不是「難」，
    # 故設此例外表排除
    map_non_x_excludes = [
        '𦥑',
        '揷',
        '𠦶',
        '𦁴',
        ]

    # 造字修正表
    # 將造字字元修正為適當的 Unicode 字元
    map_pua_fix = {
        '': '︙',
        }

    # 五代
    data = {}
    file = os.path.join(root, 'resources', 'cjsys', 'cj5-70000.txt')
    with open(file, 'r', encoding='UTF-8') as f:
        text = f.read()
        text = re.search(r'^\[DATA\]\s*(.*)$', text, flags=re.S + re.M)[1]

        for line in text.splitlines():
            if not line.strip(): continue

            line = re.split(r' +', line)

            # 移除相容區字元
            if is_cjk_comp(line[1]): continue

            # 修正或移除造字區字元
            if is_pua(line[1]):
                if line[1] in map_pua_fix:
                    line[1] = map_pua_fix[line[1]]
                else:
                    continue

            if line[0].startswith('x') and is_punc(line[1]):
                dest = 'symbols-x'
            elif line[0].startswith('x'):
                dest = 'base-dups'
            elif line[0].startswith('yyy') and is_punc(line[1]):
                dest = 'symbols-yyy'
            elif line[0].startswith('zx'):
                dest = 'symbols-zx'
            elif line[0].startswith('z'):
                dest = 'symbols-z'
            else:
                dest = 'base'

                # 將結尾非「難」的字加入列表
                # 因三代有些重複字沒有標準取碼（結尾不為「難」的碼）
                # 故從五代取得
                if not line[0].endswith('x'):
                    map_non_x.setdefault(line[1], []).append(line[0])

            line = '\t'.join(line)
            data.setdefault(dest, []).append(line)

        f.close()

    # 例外處理修正結尾非「難」字表
    for x in map_non_x_excludes:
        map_non_x.pop(x, None)

    file = os.path.join(root, 'cangjie.5-base.dict.yaml')
    with open(file, 'w', encoding='UTF-8') as f:
        text = """# encoding: utf-8
#
# 官方五代倉頡編碼表
#

---
name: "cangjie.5-base"
version: "0.10"
sort: original
use_preset_vocabulary: false
columns:
  - code
  - text
...

{}
""".format('\n'.join(data['base']))
        f.write(text)
        f.close()

    file = os.path.join(root, 'cangjie.5-base-dups.dict.yaml')
    with open(file, 'w', encoding='UTF-8') as f:
        text = """# encoding: utf-8
#
# 官方五代倉頡編碼表的重碼字表
#

---
name: "cangjie.5-base-dups"
version: "0.10"
sort: original
use_preset_vocabulary: false
columns:
  - code
  - text
...

{}
""".format('\n'.join(data['base-dups']))
        f.write(text)
        f.close()

    # 三代的 zxaf 字元錯誤，故使用五代的
    file = os.path.join(root, 'cangjie.3-symbols-zx.dict.yaml')
    with open(file, 'w', encoding='UTF-8') as f:
        text = """# encoding: utf-8
#
# 官方三代倉頡編碼表的符號表（ZXAA~ZXCY 區段）
#

---
name: "cangjie.3-symbols-zx"
version: "1.00"
sort: original
use_preset_vocabulary: false
columns:
  - code
  - text
encoder:
  exclude_patterns:
    - '^zx.*$'
...

{}
""".format('\n'.join(data['symbols-zx']))
        f.write(text)
        f.close()

    file = os.path.join(root, 'cangjie.5-symbols-yyy.dict.yaml')
    with open(file, 'w', encoding='UTF-8') as f:
        text = """# encoding: utf-8
#
# 官方五代倉頡編碼表的符號表（YYYAA~YYYYO 區段）
#

---
name: "cangjie.5-symbols-yyy"
version: "1.00"
sort: original
use_preset_vocabulary: false
columns:
  - code
  - text
encoder:
  exclude_patterns:
    - '^yyy.*$'
...

{}
""".format('\n'.join(data['symbols-yyy']))
        f.write(text)
        f.close()

    file = os.path.join(root, 'cangjie.symbols-x.dict.yaml')
    with open(file, 'w', encoding='UTF-8') as f:
        text = """# encoding: utf-8
#
# 官方三代、五代倉頡編碼表的符號表（X* 區段）
#

---
name: "cangjie.symbols-x"
version: "1.00"
sort: original
use_preset_vocabulary: false
columns:
  - code
  - text
encoder:
  exclude_patterns:
    - '^x.*$'
...

{}
""".format('\n'.join(data['symbols-x']))
        f.write(text)
        f.close()

    file = os.path.join(root, 'cangjie.symbols-z.dict.yaml')
    with open(file, 'w', encoding='UTF-8') as f:
        text = """# encoding: utf-8
#
# 《倉頡平台2012》的擴充符號表（ZA*~ZG* 區段）
#

---
name: "cangjie.symbols-z"
version: "0.10"
sort: original
use_preset_vocabulary: false
columns:
  - code
  - text
encoder:
  exclude_patterns:
    - '^z.*$'
...

{}
""".format('\n'.join(data['symbols-z']))
        f.write(text)
        f.close()

    # 三代
    data = {}
    file = os.path.join(root, 'resources', 'cjsys', 'cj3-70000.txt')
    with open(file, 'r', encoding='UTF-8') as f:
        text = f.read()
        text = re.search(r'^\[DATA\]\s*(.*)$', text, flags=re.S + re.M)[1]

        for line in text.splitlines():
            if not line.strip(): continue

            line = re.split(r' +', line)

            # 移除相容區字元
            if is_cjk_comp(line[1]): continue

            # 修正或移除造字區字元
            if is_pua(line[1]):
                if line[1] in map_pua_fix:
                    line[1] = map_pua_fix[line[1]]
                else:
                    continue

            if line[0].startswith('x') and is_punc(line[1]):
                dest = 'symbols-x'
            elif line[0].endswith('x') and line[1] in map_non_x:
                dest = 'base-dups'
            elif line[0].startswith('yyy') and is_punc(line[1]):
                dest = 'symbols-yyy'
            elif line[0].startswith('zx'):
                dest = 'symbols-zx'
            elif line[0].startswith('z'):
                dest = 'symbols-z'
            else:
                dest = 'base'

            line = '\t'.join(line)
            data.setdefault(dest, []).append(line)

        f.close()

    file = os.path.join(root, 'cangjie.3-base.dict.yaml')
    with open(file, 'w', encoding='UTF-8') as f:
        text = """# encoding: utf-8
#
# 官方三代倉頡編碼表
#

---
name: "cangjie.3-base"
version: "0.10"
sort: original
use_preset_vocabulary: false
columns:
  - code
  - text
...

{}
""".format('\n'.join(data['base']))
        f.write(text)
        f.close()

    file = os.path.join(root, 'cangjie.3-base-dups.dict.yaml')
    with open(file, 'w', encoding='UTF-8') as f:
        text = """# encoding: utf-8
#
# 官方三代倉頡編碼表的重碼字表
#

---
name: "cangjie.3-base-dups"
version: "0.10"
sort: original
use_preset_vocabulary: false
columns:
  - code
  - text
...

{}
""".format('\n'.join(data['base-dups']))
        f.write(text)
        f.close()

def import_resources():
    """匯入資料檔
    """
    import_cjsys()

def main():
    parser = argparse.ArgumentParser(
            description=__doc__,
            formatter_class=argparse.RawTextHelpFormatter)
    args = parser.parse_args()

    import_resources()

if __name__ == "__main__":
    main()
