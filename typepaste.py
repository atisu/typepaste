#!/usr/bin/env python

import argparse
import sys
import pyautogui
import clipboard


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='TypePaste - type clipboard '
                                                 'data into active window')
    parser.add_argument('-B', '--batch-size', metavar='batch_size',
                        help="print number of characters at once (batch)")
    args = parser.parse_args()
    batch_size = 0
    if not args.batch_size:
        sys.exit("ERROR: Batch size (-B or --batch-size) missing.")
    try:
        batch_size = int(args.batch_size)
    except ValueError:
        sys.exit("Batch size (-B or --batch-size) should be an integer "
                 "at least 1.")
    clipboard_text = clipboard.paste()
    text = ""
    for i in clipboard_text:
        text += i
        if len(text) == 10:
            pyautogui.typewrite(text)
            text = ""
    if text:
        pyautogui.typewrite(text)
