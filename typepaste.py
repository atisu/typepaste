#!/usr/bin/env python

import pyautogui
import clipboard


if __name__ == "__main__":
    clipboard_text = clipboard.paste()
    text = ""
    for i in clipboard_text:
        text += i
        if len(text) == 10:
            pyautogui.typewrite(text)
            text = ""
    if len(text) > 0:
        pyautogui.typewrite(text)
