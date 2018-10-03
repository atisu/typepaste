#!/usr/bin/env python

from __future__ import print_function
import fileinput
import base64

if __name__ == "__main__":
    text = ""
    for line in fileinput.input():
        text += line
print(base64.b32decode(text.upper().strip()).decode('ascii'), end='')
