#!/usr/bin/env python
import argparse
import sys
import csv
import re

AP = argparse.ArgumentParser("csv2mdtable")
AP.add_argument("--src", default=None)
AP.add_argument("--replace", default=None, type=str)
AP.add_argument("--delimiter", "-d", default=",", type=str)
AP.add_argument("--tsv", action="store_const", const='\t', dest="delimiter")

def process_doc(fin, fout=sys.stdout):
    pat = re.compile('```csv(.*)```')
    cnt = fin.read()
    pattern = re.compile()
    def search(content, start=0):
        content.find()
        pass
    pass

def line_aft_header(headers):
    a = ':--'
    lst =[ a + (len(h) - 2 ) * '-' if len(h) > 2 else a for h in headers]
    return '|%s|\n' % '|'.join(lst)

def process(fin, fout=sys.stdout, has_header=True, delimiter=","):
    csvf = csv.reader(fin, delimiter=delimiter)

    for i, r in enumerate(csvf):
        fout.write('|%s|\n' % '|'.join(r) )
        if i == 0:
            if has_header:
                fout.write(line_aft_header(r))
        fout.flush()

def main(args):
    f = sys.stdin if not args.src else open(args.src, "rb")
    process(f, delimiter=args.delimiter)
    f.close()


if __name__ == '__main__':
    main(AP.parse_args())

