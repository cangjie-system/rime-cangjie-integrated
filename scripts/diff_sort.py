#!/usr/bin/env python3
"""比對兩個編碼表的重碼字排序差異
"""

import sys
import os
import argparse
import logging
import re
import json
import yaml

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
log = logging.getLogger()

def load(file):
    """將 yaml 資料檔載入為物件化編碼資料
    """
    with open(file, 'r', encoding='UTF-8', newline=None) as f:
        text = f.read()
        f.close()

    m = re.match(r'^(.*?\n\.\.\.(?:\n|$))?(.*?)(\n\s*)?$', text, flags=re.S)
    header, body, footer = m.group(1) or '', m.group(2) or '', m.group(3) or ''

    if header:
        config = yaml.load(header, Loader=yaml.FullLoader)
        code_idx = config['columns'].index('code')
        char_idx = config['columns'].index('text')
    else:
        code_idx = 0
        char_idx = 1

    data = {}
    for line in body.splitlines():
        if line.startswith('#'): continue

        line = line.split('\t')
        if len(line) <= 1: continue

        data.setdefault(line[code_idx], []).append(line[char_idx])

    return data

def diff(file1, file2, mode):
    """計算差異資料並輸出
    """
    # load file# to dict#
    dict1 = load(file1)
    dict2 = load(file2)

    # diff dict1 and dict2 to delta
    delta = {}
    for code in dict2:
        if not code in dict1: continue
        old = dict1[code]
        new = dict2[code]
        if old != new:
            delta[code] = {
                'old': old,
                'new': new
                }

    # output
    if mode == 'txt':
        for code, item in delta.items():
            print(f"{code}\to:{''.join(item['old'])}\tn:{''.join(item['new'])}")

    else: # default: json
        print(json.dumps(delta, ensure_ascii=False))

def main():
    # 解析指令參數
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file1', help="""要比較的檔案1""")
    parser.add_argument('file2', help="""要比較的檔案2""")
    parser.add_argument('-m', "--mode", default='txt',
        choices=['json', 'txt'],
        help="""輸出模式，預設：%(default)s""")
    args = parser.parse_args()

    # 開始比對
    diff(args.file1, args.file2, mode=args.mode)

if __name__ == "__main__":
    main()
