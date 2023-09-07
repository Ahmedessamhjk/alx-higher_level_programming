#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = 0
    for a in range(len(sys.argv) - 1):
        arg += int(sys.argv[a + 1])
    print(arg)
