import numpy as np


def square(param, add_param):
    output = np.square(param) + add_param
    output = np.round(output, decimals=1)
    return output


def printing(num, phra):
    num = int(str(num)[3])
    aa = phra * num
    return aa
