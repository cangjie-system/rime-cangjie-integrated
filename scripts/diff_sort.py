#!/usr/bin/env python3
"""比對兩個編碼表的重碼字排序差異
"""

import sys
import os
import argparse
import logging
import re
import json

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
log = logging.getLogger()

def diff(file1, file2, mode):
    """修改指定的檔案或目錄
    """

    # load file1 to dict1
    with open(file1, 'r', encoding='UTF-8', newline=None) as f:
        text1 = f.read()
        f.close()

    m = re.match(r'^(.*?\n\.\.\.)(.*?)$', text1, flags=re.S)
    if m:
        header1, list1 = m.group(1), m.group(2)
    else:
        header1, list1 = "", text1

    list1 = [x.split('\t') for x in list1.split('\n')]

    dict1 = {}
    for _, line in enumerate(list1):
        if len(line) <= 1: continue
        if line[0] not in dict1: dict1[line[0]] = []
        dict1[line[0]].append(line[1])

    # load file2 to dict2
    with open(file2, 'r', encoding='UTF-8', newline=None) as f:
        text2 = f.read()
        f.close()

    m = re.match(r'^(.*?\n\.\.\.)(.*?)$', text2, flags=re.S)
    if m:
        header2, list2 = m.group(1), m.group(2)
    else:
        header2, list2 = "", text2

    list2 = [x.split('\t') for x in list2.split('\n')]

    dict2 = {}
    for _, line in enumerate(list2):
        if len(line) <= 1: continue
        if line[0] not in dict2: dict2[line[0]] = []
        dict2[line[0]].append(line[1])

    # diff dict1 and dict2, output to delta
    delta = {}
    for code, chars in dict2.items():
        if not code in dict1: continue
        old = ''.join(chars)
        new = ''.join(dict1[code])
        if old != new:
            delta[code] = {
                'old': old,
                'new': new
                }

    # output
    if mode == 'txt':
        for code, item in delta.items():
            print(f"{code}\to:{item['old']}\tn:{item['new']}")

    else: # default: json
        print(json.dumps(delta))

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
