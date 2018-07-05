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

def diff(file1, file2, mode):
    # load file1 to dict1
    with open(file1, 'r', encoding='UTF-8', newline=None) as f:
        text1 = f.read()
        f.close()

    m = re.match(r'^(.*?\n\.\.\.)?(.*?)(\s*)$', text1, flags=re.S)
    header1, list1, footer1 = m.group(1) or '', m.group(2), m.group(3)

    list1 = list1.split('\n')
    list1 = [x.split('\t') for x in list1]

    dict1 = {}
    for _, line in enumerate(list1):
        if len(line) <= 1: continue
        if line[1] not in dict1: dict1[line[1]] = []
        dict1[line[1]].append(line[0])

    # load file2 to dict2
    with open(file2, 'r', encoding='UTF-8', newline=None) as f:
        text2 = f.read()
        f.close()

    m = re.match(r'^(.*?\n\.\.\.)?(.*?)(\s*)$', text2, flags=re.S)
    header2, list2, footer2 = m.group(1) or '', m.group(2), m.group(3)

    list2 = list2.split('\n')
    list2 = [x.split('\t') for x in list2]

    dict2 = {}
    for _, line in enumerate(list2):
        if len(line) <= 1: continue
        if line[1] not in dict2: dict2[line[1]] = []
        dict2[line[1]].append(line[0])

    # diff dict1 and dict2 to delta
    delta = {}
    for char, codes in dict2.items():
        # print(char, codes)
        for _, code in enumerate(codes):
            if char not in dict1 or code not in dict1[char]:
                if not char in delta: delta[char] = {'ins': [], 'del': []}
                delta[char]['ins'].append(code)

    for char, codes in dict1.items():
        # print(char, codes)
        for _, code in enumerate(codes):
            if char not in dict2 or code not in dict2[char]:
                if not char in delta: delta[char] = {'ins': [], 'del': []}
                delta[char]['del'].append(code)

    # output
    if mode == 'ins_del':
        for k, v in delta.items():
            print('{}\t+{}\t-{}'.format(k, ','.join(v['ins']), ','.join(v['del'])))

    elif mode == 'old_new':
        for char in delta:
            print('{}\to:{}\tn:{}'.format(char,
                ','.join(dict1[char]) if char in dict1 else '',
                ','.join(dict2[char]) if char in dict2 else ''
                ))

    else: # default: json
        print(json.dumps(delta))

def main():
    # 解析指令參數
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('file1', help="""要比較的檔案1""")
    parser.add_argument('file2', help="""要比較的檔案2""")
    parser.add_argument('-m', "--mode", default='ins_del',
        choices=['json', 'ins_del', 'old_new'],
        help="""輸出模式，預設：%(default)s""")
    args = parser.parse_args()

    # 開始比對
    diff(args.file1, args.file2, mode=args.mode)

if __name__ == "__main__":
    main()
