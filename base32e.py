#!/usr/bin/env python

import sys
import base64
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='TypePaste - Base32 encoder ')
    parser.add_argument('-l', '--lowercase',
                        help="print lowecased text",
                        action='store_true')
    args = parser.parse_args()

    text = sys.stdin.buffer.read()
    encoded_text = base64.b32encode(text)
    if args.lowercase:
        encoded_text = encoded_text.lower()
    print(encoded_text.decode('utf-8'), end='')
