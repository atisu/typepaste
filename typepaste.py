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
    args = parser.parse_args()
    batch_size = 1
    try:
        batch_size = int(args.batch_size)
    except ValueError:
        sys.exit("Batch size should be an integer. ")
    if batch_size < 1:
        sys.exit("Batch size should be at least 1. ")
    clipboard_text = clipboard.paste()
    if args.base32_encode:
        clipboard_text = base64.b32encode(
            clipboard_text.encode('utf-8')).decode('utf-8')
    if args.lowercase:
        clipboard_text = clipboard_text.lower()
    text = ""
    for i in clipboard_text:
        text += (i)
        if len(text) == batch_size:
            pyautogui.typewrite(text)
            text = ""
    if text:
        pyautogui.typewrite(text)
