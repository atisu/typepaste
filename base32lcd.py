#!/usr/bin/env python

from __future__ import print_function
import sys
import base64

if __name__ == "__main__":
    text = sys.stdin.read()
    print(base64.b32decode(text.strip().upper()), end='')
