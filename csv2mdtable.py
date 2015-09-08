#!/usr/bin/env python
import argparse
import sys
import csv

AP = argparse.ArgumentParser("csv2mdtable")
AP.add_argument("--src", default=None)

def process(csvf, out=sys.stdout):
    csvout = csv.writer(out, delimiter='|')
    for i in csvf:
        csvout.write(i)

def main(args):
    f = sys.stdin if not args.src:
    process(f)


if name == '__main__':
    main(AP.parse_args())
