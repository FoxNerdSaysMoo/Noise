from PIL import Image
import numpy as np
from noise import levellednoise
import matplotlib.pyplot as plt


elemap = levellednoise(
    dims=(756, 756),
    octaves=7,
    noise_octaves=12,
    octave_degradation=1.5,
    final_scaling_factor=20,
    fit_end_to_range=True,
    fit_octave_to_range=False,
    cap=255,
    smooth=12,
    noise_scale=1
)

img = Image.fromarray(elemap.astype(np.uint8))
print("** DONE **")
img.save('elemap.png')

plt.imshow(elemap, cmap='terrain')
plt.show()
