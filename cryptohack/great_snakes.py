#!/usr/bin/env python3

import sys
# import this

if sys.version_info.major == 2:
    print("Python 2 is no longer supported, please upgrade to Python 3.")

ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]

print("Flag:")
print("".join(chr(o ^ 0x32) for o in ords))
