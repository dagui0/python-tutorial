#!/usr/bin/env python3
# fibonacci.py - print Fibonacci series

import sys

a, b = 0, 1
n = int(sys.argv[1]) if len(sys.argv) > 1 else 10

while a < n:
    print(a, end=' ')
    a, b = b, a + b
