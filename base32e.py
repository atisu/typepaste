#!/usr/bin/env python

from __future__ import print_function
import fileinput
import base64
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='TypePaste - Base32 encoder ')
    parser.add_argument('-l', '--lowercase',
                        help="print lowecased text",
                        action='store_true')
    args = parser.parse_args()

    text = ""
    for line in fileinput.input(files='-'):
        text += line
    encoded_text = base64.b32encode(text.encode('utf-8')).decode('utf-8')
    if args.lowercase:
        encoded_text = encoded_text.lower()
    print(encoded_text, end='')
