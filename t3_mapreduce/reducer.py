#!/usr/bin/env python3
import sys


def reduce():
    s = 0
    c = 0
    for line in sys.stdin:
        s += float(line.strip().split("\t")[0])
        c += 1
    sys.stdout.write("{}\n".format(s / c))


if __name__ == "__main__":
    reduce()
