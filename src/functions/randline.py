import linecache
import mmap
from random import randint


def mapcount(filename):
    "this returns the number of lines in a file"
    f = open(filename, "r+")
    buf = mmap.mmap(f.fileno(), 0)
    lines = 0
    readline = buf.readline
    while readline():
        lines += 1
    return lines

def random_word(filename):
    "this will return a random word from a file, except the first line"
    line = randint(2,mapcount(filename))
    return linecache.getline(filename, line).replace("\n", "")
