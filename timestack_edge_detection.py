import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt 
import sys


#input: timestack image
#canny edge detection for image
#output: image
def timestack_edge_detection(image_name):
	src = cv.imread(image_name)

	if len(src.shape) == 3: 
		src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
	else:
		src_gray = src 

	ratio = 3
	kernel_size = 3
	low_threshold = 100
	img_blur = cv.blur(src_gray, (3,3))
	detected_edges = cv.Canny(img_blur, low_threshold, low_threshold*ratio, kernel_size)
	mask = detected_edges != 0
	dst = src * (mask[:,:,None])

	cv.imwrite(image_name + '_canny.png', dst)