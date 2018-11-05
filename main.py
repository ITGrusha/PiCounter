from math import *
# from numpy import float64 as float256
from scipy.special import gamma
from numpy import dtype
import scipy


def to_fixed(num_obj, digits=0):
    return f"{num_obj:.{digits}f}"


def main(k: int):
    float256 = scipy.dtype('f')
    my_pi = float256(1)
    part_sum = float256(0)
    for j in range(k + 1):
        i = float256(j)
        tmp = gamma(float256(4) * i) * (float256(1103) + float256(26390) * i) / (gamma(i) ** float256(4) * float256(396) ** (float256(4) * i))
        part_sum += tmp
    my_pi *= float256(9801) / (float256(2) * float256(2) ** float256(0.5))
    my_pi /= part_sum
    print(to_fixed(my_pi, k * 10))


if __name__ == '__main__':
    main(20)
