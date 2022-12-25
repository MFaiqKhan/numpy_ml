import numpy as np;
from matplotlib.image import imread; 

myself = imread('myself.png'); # read the image

#imread function has taken this picture and then find all of its pixel values and stored the color values in the
# output array

print(myself); # print the image
print(type(myself)); # print the type of image
print(myself.size , myself.shape , myself.ndim); # print the size, shape and dimension of image