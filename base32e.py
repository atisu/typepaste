#!/usr/bin/env python

from __future__ import print_function
import fileinput
import base64

if __name__ == "__main__":
    text = ""
    for line in fileinput.input():
        text += line
encoded_text = base64.b32encode(text)
print(encoded_text, end='')
