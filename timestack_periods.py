import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt 
import sys

#input: timestack image
#calculates all periods found
#output: time periods
def timestack_periods(image_name):
	img = cv.imread(image_name, 0)

	#get height and width
	height, width = img.shape[:2]
	#print(height)
	#print(width)

	#initialize pixel period array and time period array
	pixel_periods = []
	time_periods = []

	#go through each row
	for x in range (0, height):
		row = x
	#initialize array to keep track of pixels that have color in each row
		white_px = []
		for i in range(0, width):
			if img[row, i] != 0:
				white_px.append(i)

		#add acceptable pixel periods to pixel periods array
		for k in range(1,len(white_px)):
			if white_px[k]-white_px[k-1] > 30:
				pixel_periods.append((white_px[k]-white_px[k-1]))

		#delete contents of white_px so can be used for next row
		white_px = []


	#once gone through each row and have all pixel periods, change to time
	for j in range(0,len(pixel_periods)):
			time = pixel_periods[j]/30
			if time >= 5 and time <= 20:
				time_periods.append(time)


	return time_periods