#!/usr/bin/env python3
import sys


def reduce():
    k, ex, ex2, n = 0.0, 0.0, 0.0, 0

    for line in sys.stdin:
        value = float(line.strip().split("\t")[0])

        if n == 0:
            k = value

        n += 1
        ex += value - k
        ex2 += (value - k) ** 2

    sys.stdout.write(f'{((ex2 - ex**2 / n) / (n - 1)) ** (1/2)}\n')
            
            
if __name__ == "__main__":
    reduce()
