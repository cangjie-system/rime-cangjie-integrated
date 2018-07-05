#!/usr/bin/env python3
"""修正編碼表排序
"""

import sys
import os
import argparse
import logging
import re

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
log = logging.getLogger()

def sort(file):
    def key_func(x):
        if len(x) <= 1: # 無編碼者（可能是註解）排最前
            order = -1
        elif 0x4E00 <= ord(x[1]) <= 0x9FFF: # 統一區，不改變順序
            order = 0
        elif 0x3400 <= ord(x[1]) <= 0x4DBF or 0x20000 <= ord(x[1]) <= 0x2EBEF: # Ext-A~F 按 Unicode 排序
            order = ord(x[1])
        else: # 其他非漢字符號，排最後面，按 Unicode 排序
            order = 0x10FFFF + 1 + ord(x[1])

        return (x[0], order)

    with open(file, 'r', encoding='UTF-8', newline=None) as f:
        text0 = text = f.read()
        f.close()

    m = re.match(r'^(.*?\n\.\.\.)?(.*?)(\s*)$', text, flags=re.S)
    header, list, footer = m.group(1) or '', m.group(2), m.group(3)

    list = list.split('\n')
    list = [x.split('\t') for x in list]
    list = sorted(list, key=key_func)
    list = ['\t'.join(x) for x in list]
    list = '\n'.join(list)

    text = header + list + footer

    if text == text0:
        return

    with open(file, 'w', encoding='UTF-8') as f:
        f.write(text)
        f.close()

def main():
    # 解析指令參數
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('path', help="""要處理的檔案""")
    args = parser.parse_args()

    # 開始修改
    log.info("sorting {}".format(args.path))
    sort(args.path)

if __name__ == "__main__":
    main()
