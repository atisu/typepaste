#!/usr/bin/env python

import sys
import base64

if __name__ == "__main__":
    text = sys.stdin.read()
    sys.stdout.buffer.write(base64.b32decode(text.strip().upper()))
