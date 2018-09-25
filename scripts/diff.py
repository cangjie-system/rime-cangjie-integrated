#!/usr/bin/env python3
"""比對兩個編碼表的差異
"""

import sys
import os
import argparse
import logging
import re
import json

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
log = logging.getLogger()

def load(file):
    """將 yaml 資料檔載入為物件化編碼資料
    """
    with open(file, 'r', encoding='UTF-8', newline=None) as f:
        text = f.read()
        f.close()

    m = re.match(r'^(.*?\n\.\.\.)?(.*?)(\n\s*)?$', text, flags=re.S)
    header, body, footer = m.group(1), m.group(2), m.group(3)

    data = {}
    for row in body.splitlines():
        if row.startswith('#'): continue

        row = row.split('\t')
        if len(row) <= 1: continue

        code = row[0]
        char = row[1]
        data.setdefault(char, []).append(code)

    return data

def diff(file1, file2, mode='json'):
    """計算差異資料並輸出
    """
    # load file# to dict#
        dict1 = load(file1)
        dict2 = load(file2)

    # diff dict1 and dict2 to delta
    delta = {}
    for char, codes in dict2.items():
        for _, code in enumerate(codes):
            if char not in dict1 or code not in dict1[char]:
                delta.setdefault(char, {'ins': [], 'del': []})['ins'].append(code)

    for char, codes in dict1.items():
        for _, code in enumerate(codes):
            if char not in dict2 or code not in dict2[char]:
                delta.setdefault(char, {'ins': [], 'del': []})['del'].append(code)

    # 將差異資料轉為文字輸出
    if mode == 'ins_del':
        for k, v in delta.items():
            print('{}\t{}\t{}'.format(k, ','.join(v['ins']), ','.join(v['del'])))

    elif mode == 'ins_del_m':
        for k, v in delta.items():
            print('{}\t+{}\t-{}'.format(k, ','.join(v['ins']), ','.join(v['del'])))

    elif mode == 'old_new':
        for char in delta:
            print('{}\t{}\t{}'.format(char,
                ','.join(dict1.get(char, [])),
                ','.join(dict2.get(char, []))
                ))

    elif mode == 'old_new_m':
        for char in delta:
            print('{}\to:{}\tn:{}'.format(char,
                ','.join(dict1.get(char, [])),
                ','.join(dict2.get(char, []))
                ))

    else: # default: json
        print(json.dumps(delta))

def main():
    # 解析指令參數
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('file1',
        help="""要比較的檔案1""")
    parser.add_argument('file2',
        help="""要比較的檔案2""")
    parser.add_argument('-m', "--mode", default='ins_del_m',
        choices=['json', 'ins_del', 'ins_del_m', 'old_new', 'old_new_m'],
        help="""輸出模式，預設：%(default)s""")
    args = parser.parse_args()

    # 開始比對
    diff(args.file1, args.file2, mode=args.mode)

if __name__ == "__main__":
    main()
