import numpy as np
from PIL import Image

image_filename = "C:\\Users\\gokul\\PycharmProjects\DIP\\tuberculosis.jpg"
save_filename = 'output_image.jpg'

img = Image.open(image_filename)

#convert to grayscale
imagray = img.convert(mode = 'L')

#convert to numpy array
img_array = np.asarray(imagray)
"""
STEP 1: Normalized Cumulative histogram
"""

#flatten image array and calculate histogram via binning
histogram_array = np.bincount(img_array.flatten(), minlength=256)

#normalize
num_pixels = np.sum(histogram_array)
histogram_array = histogram_array/num_pixels

#normalized cumulative histogram

chistogram_array = np.cumsum(histogram_array)

"""
STEP 2: Pixel mapping lookup table
"""
transform_map = np.floor(255 * chistogram_array).astype(np.uint8)
"""
STEP 3: Transformation
"""
# flatten image array into 1D list
img_list = list(img_array.flatten())

# transform pixel values to equalize
eq_img_list = [transform_map[p] for p in img_list]

# reshape and write back into img_array
eq_img_array = np.reshape(np.asarray(eq_img_list), img_array.shape)
eq_img = Image.fromarray(eq_img_array, mode='L')
eq_img.save(save_filename)
