import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt 
import sys
import time
from vid_line_detection import * 
from vid_edge_detection import *
from vid_timestack import *
from timestack_edge_detection import *
from timestack_periods import *
from evaluation import *

def draw_timestacks(image_name, surfline_min, surfline_max):
	img = cv.imread(image_name)
	
	#get height and width
	height, width = img.shape[:2]

	#create image copy to draw on
	img_copy = np.zeros((height,width,3), np.uint8)

	#go through each row
	for x in range (0, height):
		row = x
	#initialize array to keep track of pixels that have color in each row
		white_px = []
		for i in range(0, width):
			#img[y,x]
			if img[row,i].any() != 0:
				white_px.append(i)
				img_copy[row,i] = img[row,i]

		#draw correct estimations of periods onto image copy
		for k in range(1,len(white_px)):
			if (white_px[k]-white_px[k-1])/30 >= int(surfline_min) and (white_px[k]-white_px[k-1])/30 <= int(surfline_max):
				cv.line(img_copy,(white_px[k-1],row),(white_px[k],row), (255,0,0), 2)
		#delete contents of white_px so can be used for next row
		white_px = []


	cv.imwrite(image_name + '_drawn.png', img_copy)



draw_timestacks(sys.argv[1] + '_timestack1.png_canny.png', sys.argv[2], sys.argv[3])
draw_timestacks(sys.argv[1] + '_timestack2.png_canny.png', sys.argv[2], sys.argv[3])
draw_timestacks(sys.argv[1] + '_timestack3.png_canny.png', sys.argv[2], sys.argv[3])
draw_timestacks(sys.argv[1] + '_line.mp4_timestack1.png', sys.argv[2], sys.argv[3])
draw_timestacks(sys.argv[1] + '_line.mp4_timestack2.png', sys.argv[2], sys.argv[3])
draw_timestacks(sys.argv[1] + '_line.mp4_timestack3.png', sys.argv[2], sys.argv[3])
draw_timestacks(sys.argv[1] + '_edge.mp4_timestack1.png', sys.argv[2], sys.argv[3])
draw_timestacks(sys.argv[1] + '_edge.mp4_timestack2.png', sys.argv[2], sys.argv[3])
draw_timestacks(sys.argv[1] + '_edge.mp4_timestack3.png', sys.argv[2], sys.argv[3])


