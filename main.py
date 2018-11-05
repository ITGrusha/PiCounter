from math import *
from scipy.special import factorial
from numpy import float64


def to_fixed(num_obj, digits=0):
    return f"{num_obj:.{digits}f}"


def main(k: int):
    my_pi = float64(1)
    part_sum = float64(0)
    for j in range(k + 1):
        i = float64(j)
        tmp = factorial(float64(4) * i) * \
              (float64(1103) + float64(26390) * i) \
              / (factorial(i) ** float64(4) * float64(396) ** (float64(4) * i))
        part_sum += tmp
    my_pi *= float64(9801) / (float64(2) * float64(2) ** float64(0.5))
    my_pi /= part_sum
    print(to_fixed(my_pi, k * 10))


if __name__ == '__main__':
    main(20)
