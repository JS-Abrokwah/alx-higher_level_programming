#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = int(len(sys.argv)) - 1
    results = 0
    for i in range(count):
        results += int(sys.argv[i + 1])
    print("{}".format(results))
