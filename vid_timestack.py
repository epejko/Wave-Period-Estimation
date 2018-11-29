import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt 
import sys
import time

#input:video
#creates timestacks
#output: 3 timestacks
def vid_timestack(video_name):
	cap = cv.VideoCapture(video_name)

	#initialize image for timestack
	fps = int(cap.get(cv.CAP_PROP_FPS))
	length = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
	height = int(cap.get(4)) #height is same as height of input video
	width = length
	timestack_img1 = np.zeros((height, width, 3), dtype="uint8")
	timestack_img2 = np.zeros((height, width, 3), dtype="uint8")
	timestack_img3 = np.zeros((height, width, 3), dtype="uint8")


	#choose a column to look at
	k1 = int((cap.get(3))/3) #1/3
	k2 = int((cap.get(3))/2) #1/2
	k3 = 2*(int((cap.get(3))/3)) #2/3
	#counter for timestack x-axis
	x_axis = 0
	#take each frame and select one column of pixels and write to timestack image
	while(1):
		#take each frame
		ret,frame = cap.read()

		#print(frame.shape)

		if ret == True:
			if x_axis < width:
				#select kth column
				#add to timestack image
				timestack_img1[:,x_axis] = frame[:,k1]
				timestack_img2[:,x_axis] = frame[:,k2]
				timestack_img3[:,x_axis] = frame[:,k3]

				#increment counter
				x_axis += 1

		else:
			break


		k = cv.waitKey(5) & 0xFF
		if k == 27:
			break

	#write imgage to png file
	output_file1 = video_name + '_timestack1.png'
	cv.imwrite(output_file1, timestack_img1)

	output_file2 = video_name + '_timestack2.png'
	cv.imwrite(output_file2, timestack_img2)

	output_file3 = video_name + '_timestack3.png'
	cv.imwrite(output_file3, timestack_img3)

	cap.release()
	cv.destroyAllWindows()

