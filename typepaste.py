#!/usr/bin/env python

import argparse
import sys
import base64
import pyautogui
import clipboard


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='TypePaste - type clipboard '
                                                 'data into active window')
    parser.add_argument('-B', '--batch-size', metavar='batch_size',
                        help="number of characters to print at once (batch)",
                        required=True)
    parser.add_argument('-3', '--base32-encode',
                        help="print base32 encoded string (for transferring "
                             "scripts)",
                        action='store_true')
    parser.add_argument('-l', '--lowercase',
                        help="print lowecased text",
                        action='store_true')
    parser.add_argument('-f', '--source-file', metavar='source_file',
                        help="Use source file instead of clipboard. "
                        "Assumes binary file.")
    args = parser.parse_args()
    batch_size = 1
    paste_text = ""
    try:
        batch_size = int(args.batch_size)
    except ValueError:
        sys.exit("Batch size should be an integer. ")
    if batch_size < 1:
        sys.exit("Batch size should be at least 1. ")
    if (args.source_file):
        with open(args.source_file, "rb") as f:
            paste_text = f.read()
    else:
        paste_text = clipboard.paste().encode('utf-8')
    if args.base32_encode:
        paste_text = base64.b32encode(paste_text)
    if args.lowercase:
        paste_text = paste_text.lower()
    text = ""
    pyautogui.FAILSAFE = True
    for i in paste_text:
        text += chr(i)
        if len(text) == batch_size:
            pyautogui.typewrite(text, interval=0.0)
            text = ""
    if text:
        print(text, end='')
        pyautogui.typewrite(text, interval=0.0)
