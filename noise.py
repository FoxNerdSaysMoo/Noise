import numpy as np
from utils import static
from scipy.ndimage.filters import gaussian_filter
from random import randint


def static(dims):
    result = np.zeros(dims)
    for x in range(dims[0]):
        for y in range(dims[1]):
            result[x, y] = randint(0, 255)
    return result


def levellednoise(
    dims,
    octaves: int,
    final_scaling_factor=2,
    noise_octaves=6,
    octave_degradation=1.2,
    cap=255,
    fit_end_to_range=True,
    fit_octave_to_range=True,
    smooth=0,
    noise_scale=1
):
    result = None

    for octave in range(1, octaves):
        scale_factor = round(final_scaling_factor * (octaves/octave))
        oct_dims = [int(i / scale_factor)+1 for i in dims]

        if result is None:
            result = noise(dims, noise_octaves)

        adding = np.kron(
            noise(
                oct_dims, noise_octaves, noise_scale
            ),
            np.ones(
                    (scale_factor, scale_factor)
            )
        )[slice(0, dims[0]), slice(0, dims[1])]

        if fit_octave_to_range:
            adding -= adding.min()
            adding *= (cap / adding.max())
        result += adding
        result /= octave_degradation

    if fit_end_to_range:
        result -= result.min()
        result *= (cap / result.max())

    result = gaussian_filter(result, [smooth, smooth], mode='wrap')

    return result


def noise(dims, octaves: int, scale=1):
    final = static(dims)

    for level in range(1, octaves):
        result = np.zeros(dims)

        for x in range(result.shape[0]):
            for y in range(result.shape[1]):
                neighbors = []

                if x > 0:
                    neighbors.append(final[x-scale, y])
                if x < result.shape[0]-scale:
                    neighbors.append(final[x+scale, y])
                if y > 0:
                    neighbors.append(final[x, y-scale])
                if y < result.shape[1]-scale:
                    neighbors.append(final[x, y+scale])

                result[x, y] = sum(neighbors)/len(neighbors)

        final += result/2
        final /= 1.5

    return final
