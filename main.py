# main.py

from utils import get_float
from utils import get_int

if __name__ == '__main__':
    x = get_float("x: ")
    i = get_int("i: ")
    z = x*i

    print(z)