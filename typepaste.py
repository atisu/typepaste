#!/usr/bin/env python

import argparse
import sys
import pyautogui
import clipboard


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='TypePaste - type clipboard '
                                                 'data into active window')
    parser.add_argument('-B', '--batch-size', metavar='batch_size',
                        help="print number of characters at once (batch)",
                        required=True)
    args = parser.parse_args()
    batch_size = 1
    try:
        batch_size = int(args.batch_size)
    except ValueError:
        sys.exit("Batch size should be an integer. ")
    if batch_size < 1:
        sys.exit("Batch size should be at least 1. ")
    clipboard_text = clipboard.paste()
    text = ""
    for i in clipboard_text:
        text += i
        if len(text) == batch_size:
            pyautogui.typewrite(text)
            text = ""
    if text:
        pyautogui.typewrite(text)
