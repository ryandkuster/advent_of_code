import hashlib
import sys


def get_secret_key(f):
    for line in f:
        line = line.rstrip()
        get_hex_hash(line)


def get_hex_hash(line):
    idx = 0
    while True:
        idx += 1
        combo = line + str(idx)
        hex_hash = hashlib.md5(combo.encode())
        if hex_hash.hexdigest().startswith('00000'):
            print(idx)
            break


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        get_secret_key(f)
