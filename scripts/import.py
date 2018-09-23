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
    return code < 0x3400 or 0xFE30 <= code <= 0xFFEF

def is_rad_kanxi(text):
    code = ord(text[0])
    return 0x2F00 <= code <= 0x2FDF

def is_rad_sup(text):
    code = ord(text[0])
    return 0x2E80 <= code <= 0x2EFF

def is_cjk_comp(text):
    code = ord(text[0])
    return 0xF900 <= code <= 0xFAD9 or 0x2F800 <= code <= 0x2FA1D

def is_pua(text):
    code = ord(text[0])
    return 0xE000 <= code <= 0xF8FF or 0xF0000 <= code <= 0x10FFFF

def import_cjsys():
    """匯入倉頡平台（馬來西亞·倉頡之友）
    """
    def sort_key_func(line):
        return line[0]

	# 五代新增字表
    # 五代編碼表有而三代編碼表沒有的字
    map_cj5_extra_chars = {}

    # 五代新增字修正表
    map_cj5_extra_chars_fix = {
        ('tjd', '蘖'): 'thjd',
        }

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

                # 加入五代新增字表
                map_cj5_extra_chars[line[1]] = line

                # 將結尾非「難」的字加入列表
                # 因三代有些重複字沒有標準取碼（結尾不為「難」的碼）
                # 故從五代取得
                if not line[0].endswith('x'):
                    map_non_x.setdefault(line[1], []).append(line[0])

            data.setdefault(dest, []).append(line)

        f.close()

    # 例外處理修正結尾非「難」字表
    for x in map_non_x_excludes:
        map_non_x.pop(x, None)

    data['base'].sort(key=sort_key_func)
    file = os.path.join(root, 'cangjie.5-base.dict.yaml')
    with open(file, 'w', encoding='UTF-8') as f:
        text = """# encoding: utf-8
#
# 官方五代倉頡編碼表
#
# 原始編碼表來自馬來西亞·倉頡之友《倉頡平台2012》內附的編碼表，
# 本專案轉換為 RIME 格式，並參考可取得的官方資訊修訂。
#
# - 符號表 (zx*, yyy*, za*~zg*, etc.) 由此表移除，移至其他編碼表。
# - 倉頡系統有收而 Unicode 未收的字形，加入容錯編碼處理。
#

---
name: "cangjie.5-base"
version: "0.10"
sort: original
use_preset_vocabulary: false
columns:
  - code
  - text
  - notes
...

{}
""".format('\n'.join(['\t'.join(x) for x in data['base']]))
        f.write(text)
        f.close()

    data['base-dups'].sort(key=sort_key_func)
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
  - notes
...

{}
""".format('\n'.join(['\t'.join(x) for x in data['base-dups']]))
        f.write(text)
        f.close()

    # 三代的 zxaf 字元錯誤，故使用五代的
    data['symbols-zx'].sort(key=sort_key_func)
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
""".format('\n'.join(['\t'.join(x) for x in data['symbols-zx']]))
        f.write(text)
        f.close()

    data['symbols-yyy'].sort(key=sort_key_func)
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
""".format('\n'.join(['\t'.join(x) for x in data['symbols-yyy']]))
        f.write(text)
        f.close()

    data['symbols-x'].sort(key=sort_key_func)
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
""".format('\n'.join(['\t'.join(x) for x in data['symbols-x']]))
        f.write(text)
        f.close()

    data['symbols-z'].sort(key=sort_key_func)
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
""".format('\n'.join(['\t'.join(x) for x in data['symbols-z']]))
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

                # 從五代新增字表移除
                map_cj5_extra_chars.pop(line[1], None)

            data.setdefault(dest, []).append(line)

        f.close()

	# 將五代新增字表的字加入三代
    for _, x in map_cj5_extra_chars.items():
        # 修正五代新增字
        if (x[0], x[1]) in map_cj5_extra_chars_fix:
            x[0] = map_cj5_extra_chars_fix[x[0], x[1]]

        data['base'].append(x)

    data['base'].sort(key=sort_key_func)
    file = os.path.join(root, 'cangjie.3-base.dict.yaml')
    with open(file, 'w', encoding='UTF-8') as f:
        text = """# encoding: utf-8
#
# 官方三代倉頡編碼表
#
# 原始編碼表來自馬來西亞·倉頡之友《倉頡平台2012》內附的編碼表，
# 本專案轉換為 RIME 格式，並參考可取得的官方資訊修訂。
#
# - 符號表 (zx*, yyy*, za*~zg*, etc.) 由此表移除，移至其他編碼表。
# - 倉頡系統有收而 Unicode 未收的字形，加入容錯編碼處理。
#

---
name: "cangjie.3-base"
version: "0.10"
sort: original
use_preset_vocabulary: false
columns:
  - code
  - text
  - notes
...

{}
""".format('\n'.join(['\t'.join(x) for x in data['base']]))
        f.write(text)
        f.close()

    data['base-dups'].sort(key=sort_key_func)
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
  - notes
...

{}
""".format('\n'.join(['\t'.join(x) for x in data['base-dups']]))
        f.write(text)
        f.close()

def import_cangjie3_plus():
    """匯入三代倉頡補完計畫
    """
    def sort_key_func(line):
        return line[0]

    data = {}
    file = os.path.join(root, 'resources', 'cangjie3-plus', 'cj3-70000~02.txt')
    with open(file, 'r', encoding='UTF-8') as f:
        text = f.read()
        text = re.search(r'^\[DATA\]\s*(.*)$', text, flags=re.S + re.M)[1]

        for line in text.splitlines():
            if not line.strip(): continue

            line = re.split(r' +', line)

            # 移除相容區字元
            if is_cjk_comp(line[1]): continue

            # 移除造字區字元
            if is_pua(line[1]): continue

            if line[0].startswith('x') and is_punc(line[1]):
                dest = '3-symbols-x'
            elif line[0].startswith('x'):
                dest = '3-base-dups'
            elif line[0].startswith('yyy') and is_punc(line[1]):
                dest = '3-symbols-yyy'
            elif line[0].startswith('zx'):
                dest = '3-symbols-zx'
            elif line[0].startswith('z'):
                dest = '3-symbols-z'
            elif is_punc(line[1]):
                dest = '3-symbols'
            else:
                dest = '3-base'

            line = line[0:2]
            data.setdefault(dest, []).append(line)

        f.close()

    data['3-base'].sort(key=sort_key_func)
    file = os.path.join(root, 'cangjie.3-base.dict.yaml')
    with open(file, 'w', encoding='UTF-8') as f:
        text = """# encoding: utf-8
#
# 官方三代倉頡編碼表
#
# 原始編碼表來自馬來西亞·倉頡之友《倉頡平台2012》內附的編碼表，
# 本專案轉換為 RIME 格式，並參考可取得的官方資訊修訂。
#
# - 符號表 (zx*, yyy*, za*~zg*, etc.) 由此表移除，移至其他編碼表。
# - 倉頡系統有收而 Unicode 未收的字形，加入容錯編碼處理。
#

---
name: "cangjie.3-base"
version: "0.10"
sort: original
use_preset_vocabulary: false
columns:
  - code
  - text
  - notes
...

{}
""".format('\n'.join(['\t'.join(x) for x in data['3-base']]))
        f.write(text)
        f.close()

    data['3-base-dups'].sort(key=sort_key_func)
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
  - notes
...

{}
""".format('\n'.join(['\t'.join(x) for x in data['3-base-dups']]))
        f.write(text)
        f.close()

def import_cangjie5_plus():
    """匯入五代倉頡補完計畫
    """
    def sort_key_func(line):
        return line[0]

    data = {}

    file = os.path.join(root, 'resources', 'cangjie5-plus', 'Cangjie5.txt')
    with open(file, 'r', encoding='UTF-8') as f:
        text = f.read()
        text = re.search(r'^------------------------------\n(.*)$', text, flags=re.S + re.M)[1]

        for line in text.splitlines():
            if not line.strip(): continue

            line = line.split('\t')

            # 移除相容區字元
            if is_cjk_comp(line[0]): continue

            # 移除造字區字元
            if is_pua(line[0]): continue

            if line[1].startswith('x') and is_punc(line[0]):
                dest = '5-symbols-x'
            elif line[1].startswith('x'):
                dest = '5-base-dups'
            elif line[1].startswith('yyy') and is_punc(line[0]):
                dest = '5-symbols-yyy'
            elif line[1].startswith('zx'):
                dest = '5-symbols-zx'
            elif line[1].startswith('z'):
                dest = '5-symbols-z'
            elif is_punc(line[0]):
                dest = '5-symbols'
            else:
                dest = '5-base'

            line = [line[1], line[0]]
            data.setdefault(dest, []).append(line)

    data['5-base'].sort(key=sort_key_func)
    file = os.path.join(root, 'cangjie.5-base.dict.yaml')
    with open(file, 'w', encoding='UTF-8') as f:
        text = """# encoding: utf-8
#
# 官方五代倉頡編碼表
#
# 原始編碼表來自馬來西亞·倉頡之友《倉頡平台2012》內附的編碼表，
# 本專案轉換為 RIME 格式，並參考可取得的官方資訊修訂。
#
# - 符號表 (zx*, yyy*, za*~zg*, etc.) 由此表移除，移至其他編碼表。
# - 倉頡系統有收而 Unicode 未收的字形，加入容錯編碼處理。
#

---
name: "cangjie.5-base"
version: "0.10"
sort: original
use_preset_vocabulary: false
columns:
  - code
  - text
  - notes
...

{}
""".format('\n'.join(['\t'.join(x) for x in data['5-base']]))
        f.write(text)
        f.close()

    data['5-base-dups'].sort(key=sort_key_func)
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
  - notes
...

{}
""".format('\n'.join(['\t'.join(x) for x in data['5-base-dups']]))
        f.write(text)
        f.close()

    file = os.path.join(root, 'resources', 'cangjie5-plus', 'Cangjie5_supplement.txt')
    with open(file, 'r', encoding='UTF-8') as f:
        text = f.read()

        for line in text.splitlines():
            if not line.strip(): continue

            line = line.split('\t')

            if is_cjk_comp(line[0]):
                dest = '5-cjkcomp'
            elif is_rad_kanxi(line[0]):
                dest = '5-rad-kanxi'
            elif is_rad_sup(line[0]):
                dest = '5-rad-sup'
            else:
                continue

            line = line[0:2]
            data.setdefault(dest, []).append(line)

        f.close()

    data['5-cjkcomp'].sort()
    file = os.path.join(root, 'cangjie.5-cjkcomp.dict.yaml')
    with open(file, 'w', encoding='UTF-8') as f:
        text = """# encoding: utf-8
#
# Unicode 中日韓兼容表意文字（補充） (CJK Compatibility Ideographs (Supplement))
#
# - 按 Unicode 排序
#

---
name: "cangjie.5-cjkcomp"
version: "0.10"
sort: original
use_preset_vocabulary: false
columns:
  - text
  - code
...

{}
""".format('\n'.join(['\t'.join(x) for x in data['5-cjkcomp']]))
        f.write(text)
        f.close()

    data['5-rad-kanxi'].sort()
    file = os.path.join(root, 'cangjie.5-rad-kanxi.dict.yaml')
    with open(file, 'w', encoding='UTF-8') as f:
        text = """# encoding: utf-8
#
# Unicode 康熙部首 (Kangxi Radicals)
#
# - 按康熙部首順序（亦即 Unicode 順序）排序
#

---
name: "cangjie.5-rad-kanxi"
version: "0.10"
sort: original
use_preset_vocabulary: false
columns:
  - text
  - code
...

{}
""".format('\n'.join(['\t'.join(x) for x in data['5-rad-kanxi']]))
        f.write(text)
        f.close()

    data['5-rad-sup'].sort()
    file = os.path.join(root, 'cangjie.5-rad-sup.dict.yaml')
    with open(file, 'w', encoding='UTF-8') as f:
        text = """# encoding: utf-8
#
# Unicode 中日韓部首補充 (CJK Radicals Supplement)
#
# - 按 Unicode 排序
#

---
name: "cangjie.5-rad-sup"
version: "0.10"
sort: original
use_preset_vocabulary: false
columns:
  - text
  - code
...

{}
""".format('\n'.join(['\t'.join(x) for x in data['5-rad-sup']]))
        f.write(text)
        f.close()

    # 五代轉三代
    map_conv = {
        ('曆', 'mhda'): 'mda',
        ('歷', 'mhdm'): 'mdylm',
        ('遲', 'yseq'): 'ysyq',

        ('⾮', 'lmsy'): 'lmyyy',
        ('⾯', 'mwsl'): 'mwyl',
        ('⾲', 'lsmm'): 'lmmm',
        ('⿁', 'hui'): 'hi',

        ('⻤', 'hui'): 'hi',
        ('⻫', 'yksl'): 'yklml',
        }
    
    data['3-cjkcomp'] = list(data['5-cjkcomp'])
    for i, x in enumerate(data['3-cjkcomp']):
        if (x[0], x[1]) in map_conv:
            x = x[0], map_conv[x[0], x[1]]
        data['3-cjkcomp'][i] = '\t'.join(x)
    file = os.path.join(root, 'cangjie.3-cjkcomp.dict.yaml')
    with open(file, 'w', encoding='UTF-8') as f:
        text = """# encoding: utf-8
#
# Unicode 中日韓兼容表意文字（補充） (CJK Compatibility Ideographs (Supplement))
#
# - 按 Unicode 排序
#

---
name: "cangjie.3-cjkcomp"
version: "0.10"
sort: original
use_preset_vocabulary: false
columns:
  - text
  - code
...

{}
""".format('\n'.join(data['3-cjkcomp']))
        f.write(text)
        f.close()
    
    data['3-rad-kanxi'] = list(data['5-rad-kanxi'])
    for i, x in enumerate(data['3-rad-kanxi']):
        if (x[0], x[1]) in map_conv:
            x = x[0], map_conv[x[0], x[1]]
        data['3-rad-kanxi'][i] = '\t'.join(x)
    file = os.path.join(root, 'cangjie.3-rad-kanxi.dict.yaml')
    with open(file, 'w', encoding='UTF-8') as f:
        text = """# encoding: utf-8
#
# Unicode 康熙部首 (Kangxi Radicals)
#
# - 按康熙部首順序（亦即 Unicode 順序）排序
#

---
name: "cangjie.3-rad-kanxi"
version: "0.10"
sort: original
use_preset_vocabulary: false
columns:
  - text
  - code
...

{}
""".format('\n'.join(data['3-rad-kanxi']))
        f.write(text)
        f.close()
    
    data['3-rad-sup'] = list(data['5-rad-sup'])
    for i, x in enumerate(data['3-rad-sup']):
        if (x[0], x[1]) in map_conv:
            x = x[0], map_conv[x[0], x[1]]
        data['3-rad-sup'][i] = '\t'.join(x)
    file = os.path.join(root, 'cangjie.3-rad-sup.dict.yaml')
    with open(file, 'w', encoding='UTF-8') as f:
        text = """# encoding: utf-8
#
# Unicode 中日韓部首補充 (CJK Radicals Supplement)
#
# - 按 Unicode 排序
#

---
name: "cangjie.3-rad-sup"
version: "0.10"
sort: original
use_preset_vocabulary: false
columns:
  - text
  - code
...

{}
""".format('\n'.join(data['3-rad-sup']))
        f.write(text)
        f.close()

def import_resources():
    """匯入資料檔
    """
    import_cjsys()
    import_cangjie3_plus()
    import_cangjie5_plus()

def main():
    parser = argparse.ArgumentParser(
            description=__doc__,
            formatter_class=argparse.RawTextHelpFormatter)
    args = parser.parse_args()

    import_resources()

if __name__ == "__main__":
    main()
