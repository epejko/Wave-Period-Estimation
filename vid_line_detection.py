import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt 
import sys

#input: video
#line detection / connected components 
#output: video
def vid_line_detection(video_name):
	cap = cv.VideoCapture(video_name)

	#output video writer
	frames_per_sec = int(cap.get(cv.CAP_PROP_FPS))
	frame_size = (int(cap.get(3)), int(cap.get(4)))
	fourcc = cv.VideoWriter_fourcc('m','p','4','v')
	out = cv.VideoWriter()
	out_open = out.open(video_name + '_inbetween.mp4', fourcc, frames_per_sec, frame_size, False)

	while(1):
		#take each frame
		ret,frame = cap.read()

		if ret == True:
		
			img = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

			img = cv.bitwise_not(img)
			thresh = cv.adaptiveThreshold(img,255, cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,15,-3)

			horizontal = thresh
			rows,cols = horizontal.shape
			horizontalsize = int(cols/30)
			horizontalStructure = cv.getStructuringElement(cv.MORPH_RECT, (horizontalsize,1))
			horizontal = cv.erode(horizontal, horizontalStructure, (-1, -1))
			horizontal = cv.dilate(horizontal, horizontalStructure, (-1, -1))
			structure = cv.getStructuringElement(cv.MORPH_RECT, (horizontalsize, 2))
			horizontal = cv.erode(horizontal, structure, (-1,-1))
			#write frame to output file
			out.write(horizontal)

		else:
			break

		k = cv.waitKey(5) & 0xFF
		if k == 27:
			break

	cap.release()
	out.release()
	cv.destroyAllWindows()


	###################

	cap2 = cv.VideoCapture(video_name + '_inbetween.mp4')

	#create output video file and video writer
	frames_per_sec2 = int(cap2.get(cv.CAP_PROP_FPS))
	frame_size2 = (int(cap2.get(3)), int(cap2.get(4)))
	fourcc = cv.VideoWriter_fourcc('m', 'p', '4', 'v')
	out2 = cv.VideoWriter()
	success = out2.open(video_name + '_line.mp4', fourcc, frames_per_sec2, frame_size2, True)


	while(1):
		_, frame = cap2.read()

		if _ == True:

			img = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
			img = cv.threshold(img, 127, 255, cv.THRESH_BINARY)[1]
			ret, labels = cv.connectedComponents(img)
			#mapping labels to hue values
			label_hue = np.uint8(179*labels/np.max(labels))
			blank_ch = 255*np.ones_like(label_hue)
			labeled_img = cv.merge([label_hue, blank_ch, blank_ch])
			#convert labeled image back to bgr
			labeled_img = cv.cvtColor(labeled_img, cv.COLOR_HSV2BGR)
			#set background label to 0 (black)
			labeled_img[label_hue==0] = 0
			out2.write(labeled_img)

		else:
			break

		k = cv.waitKey(5) & 0xFF
		if k == 27:
			break

	cap2.release()
	out2.release()
	cv.destroyAllWindows()








