import numpy as np
from random import randint


def static(dims):
    result = np.zeros(dims)
    for x in range(dims[0]):
        for y in range(dims[1]):
            result[x, y] = randint(0, 255)
    return result
