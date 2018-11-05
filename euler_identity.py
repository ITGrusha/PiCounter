from math import pow
from scipy import power
from numpy import float64


def to_fixed(num_obj, digits=0):
    return f"{num_obj:.{digits}f}"


def main(k: int):
    my_pi = float64(0)
    for i in range(k):
        j = float64(i)
        my_pi += float64(1) / power(i, float64(2))
    my_pi = power(my_pi * float64(6), float64(0.5))
    print(to_fixed(my_pi, k * 10))


if __name__ == '__main__':
    main(20)
