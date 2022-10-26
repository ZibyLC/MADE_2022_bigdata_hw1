#!/usr/bin/env python3
import sys
import csv


def mapper():
    for line in csv.reader(sys.stdin):
        if len(line[9]) > 0 and line[9] != 'price':
            sys.stdout.write(f'{line[9]}\t1\n')


if __name__ == "__main__":
    mapper()
