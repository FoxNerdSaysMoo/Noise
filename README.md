# Noise
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FFoxNerdSaysMoo%2FNoise.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FFoxNerdSaysMoo%2FNoise?ref=badge_shield)

## Basic usage
```python
levellednoise(
    dims=(756, 756),  # Dimensions of array (only 2D supported so far)
    octaves=7,  # Number of octaves for noise to be compunded (how much detail)
    noise_octaves=12,  # Number of octaves for static to be smoothened
    octave_degradation=1.5,  # How much to divide noise by (mess around with it to get a feel) (default: 1.2)
    final_scaling_factor=20,  # How much the final layer will be scaled up relative to first (default: 2)
    fit_end_to_range=True,  # Set the max and min of the final array to a range of 0-cap (default True)
    fit_octave_to_range=False,  # Set max and min of every noise level to a ranfe of 0-cap (default: True)
    cap=255,  # cap value for fitting to range (default: 255)
    smooth=12,  # How many pixels to smooth the result by
    noise_scale=1  # Not recommened to change, but cool if you do
)
```
`output.png` is not important.
`elemap.png` is the image output of `test.py`.


## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FFoxNerdSaysMoo%2FNoise.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FFoxNerdSaysMoo%2FNoise?ref=badge_large)