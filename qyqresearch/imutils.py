
# Input numpy library and cv2 library (the OpenCV-Python Interface)
import numpy as np
import cv2

# Define the resize function
# 'cv2.INTER_AREA' is the preferable interpolation method for shrinking
def resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized
    # 'image.shape' will return three dimension numpy array (a,b,c)
    # a is total Number of row, b is otal Number of columns, c is color(if image is color)
	dim = None
	(h, w) = image.shape[:2]

    # if both width and height are None, return the origin image
    # the image doesn't need to be resized
	if width is None and height is None:
		return image

    # if the width is None, calculate the ratio = height required / origin image height h
    # the width now = ratio * origin image width w
	if width is None:
		r = height / float(h)
		dim = (int(w * r), height)

    # if the height is None, calculate the ratio = width required / origin image width w
    # the height now = ratio * origin image height h
	else:
		r = width / float(w)
		dim = (width, int(h * r))

    # resize the image and return the resized image
	resized = cv2.resize(image, dim, interpolation = inter)

	return resized





