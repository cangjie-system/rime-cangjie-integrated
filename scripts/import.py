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

def import_cjsys():
    """匯入倉頡平台（馬來西亞·倉頡之友）
    """

    # 五代
    data = {}
    file = os.path.join(root, 'resources', 'cjsys', 'cj5-70000.txt')
    with open(file, 'r', encoding='UTF-8') as f:
        text = f.read()
        text = re.search(r'^\[DATA\]\s*(.*)$', text, flags=re.S + re.M)[1]

        for line in text.splitlines():
            if not line.strip(): continue

            line = re.split(r' +', line)
            line = '\t'.join(line)
            data.setdefault('base', []).append(line)

        f.close()

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
encoder:
  exclude_patterns:
    - '^z.*$'
...

{}
""".format('\n'.join(data['base']))
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
            line = '\t'.join(line)
            data.setdefault('base', []).append(line)

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
encoder:
  exclude_patterns:
    - '^z.*$'
...

{}
""".format('\n'.join(data['base']))
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
