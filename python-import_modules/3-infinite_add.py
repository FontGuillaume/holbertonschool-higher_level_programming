#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv
    total = 0

    for i in range(1, len(args)):
        total += int(args[i])

    print(total)
