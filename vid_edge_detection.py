import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt 
import sys

#input: video
#canny edge detection
#output: video
def vid_edge_detection(video_name):
	cap = cv.VideoCapture(video_name)

	#output video writer
	frames_per_sec = int(cap.get(cv.CAP_PROP_FPS))
	frame_size = (int(cap.get(3)), int(cap.get(4)))
	fourcc = cv.VideoWriter_fourcc('m','p','4','v')
	out = cv.VideoWriter()
	out_open = out.open(video_name + '_edge.mp4', fourcc, frames_per_sec, frame_size, True)

	while(1):
		#take each frame
		ret,frame = cap.read()

		if ret == True:
		
			src_gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
			ratio = 3
			kernel_size = 3
			low_threshold = 100
			img_blur = cv.blur(src_gray, (3,3))
			detected_edges = cv.Canny(img_blur, low_threshold, low_threshold*ratio, kernel_size)
			mask = detected_edges != 0
			dst = frame * (mask[:,:,None])

			out.write(dst)

		else:
			break

		k = cv.waitKey(5) & 0xFF
		if k == 27:
			break

	cap.release()
	out.release()
	cv.destroyAllWindows()	