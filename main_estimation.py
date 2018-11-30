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

#input_video = sys.argv[1]
#period_surfline_min = sys.argv[2]
#period_surfline_max = sys.argv[3]

#line detection
vid_line_detection(sys.argv[1])
#edge detection
vid_edge_detection(sys.argv[1])
#immediately create timestack
vid_timestack(sys.argv[1])

#create timestacks of pre-processed videos
vid_timestack(sys.argv[1] + '_line.mp4')
vid_timestack(sys.argv[1] + '_edge.mp4')

#post-processing: edge detection for vid_timestack(input_video)
timestack_edge_detection(sys.argv[1] + '_timestack1.png')
timestack_edge_detection(sys.argv[1] + '_timestack2.png')
timestack_edge_detection(sys.argv[1] + '_timestack3.png')

#9 timestack images to calculate periods of
#post processed
times1 = timestack_periods(sys.argv[1] + '_timestack1.png_canny.png')
times2 = timestack_periods(sys.argv[1] + '_timestack2.png_canny.png')
times3 = timestack_periods(sys.argv[1] + '_timestack3.png_canny.png')
#pre-processed lines
times4 = timestack_periods(sys.argv[1] + '_line.mp4_timestack1.png')
times5 = timestack_periods(sys.argv[1] + '_line.mp4_timestack2.png')
times6 = timestack_periods(sys.argv[1] + '_line.mp4_timestack3.png')
#pre-processed edges
times7 = timestack_periods(sys.argv[1] + '_edge.mp4_timestack1.png')
times8 = timestack_periods(sys.argv[1] + '_edge.mp4_timestack2.png')
times9 = timestack_periods(sys.argv[1] + '_edge.mp4_timestack3.png')

#evaluation / histogram of each time
correct1, percentage1 = evaluation(times1, sys.argv[2], sys.argv[3], sys.argv[1] + '_timestack1.png_canny.png')
correct2, percentage2 = evaluation(times2, sys.argv[2], sys.argv[3], sys.argv[1] + '_timestack2.png_canny.png')
correct3, percentage3 = evaluation(times3, sys.argv[2], sys.argv[3], sys.argv[1] + '_timestack3.png_canny.png')
correct4, percentage4 = evaluation(times4, sys.argv[2], sys.argv[3], sys.argv[1] + '_line.mp4_timestack1.png')
correct5, percentage5 = evaluation(times5, sys.argv[2], sys.argv[3], sys.argv[1] + '_line.mp4_timestack2.png')
correct6, percentage6 = evaluation(times6, sys.argv[2], sys.argv[3], sys.argv[1] + '_line.mp4_timestack3.png')
correct7, percentage7 = evaluation(times7, sys.argv[2], sys.argv[3], sys.argv[1] + '_edge.mp4_timestack1.png')
correct8, percentage8 = evaluation(times8, sys.argv[2], sys.argv[3], sys.argv[1] + '_edge.mp4_timestack2.png')
correct9, percentage9 = evaluation(times9, sys.argv[2], sys.argv[3], sys.argv[1] + '_edge.mp4_timestack3.png')

#write evaluations to text file
f = open(sys.argv[1] + '_evaluation.txt', 'w+')
f.write('Timestack at 1/3 image width and edge detection on timestack image:\nEstimated in correct period range ' + str(correct1) + ' times.\nPercentage estimated correct: ' + str(percentage1) + '\n')
f.write('Timestack at 1/2 image width and edge detection on timestack image:\nEstimated in correct period range ' + str(correct2) + ' times.\nPercentage estimated correct: ' + str(percentage2) + '\n')
f.write('Timestack at 2/3 image width and edge detection on timestack image:\nEstimated in correct period range ' + str(correct3) + ' times.\nPercentage estimated correct: ' + str(percentage3) + '\n')
f.write('Timestack at 1/3 image width and line detection on video:\nEstimated in correct period range ' + str(correct4) + ' times.\nPercentage estimated correct: ' + str(percentage4) + '\n')
f.write('Timestack at 1/2 image width and line detection on video:\nEstimated in correct period range ' + str(correct5) + ' times.\nPercentage estimated correct: ' + str(percentage5) + '\n')
f.write('Timestack at 2/3 image width and line detection on video:\nEstimated in correct period range ' + str(correct6) + ' times.\nPercentage estimated correct: ' + str(percentage6) + '\n')
f.write('Timestack at 1/3 image width and edge detection on video:\nEstimated in correct period range ' + str(correct7) + ' times.\nPercentage estimated correct: ' + str(percentage7) + '\n')
f.write('Timestack at 1/2 image width and edge detection on video:\nEstimated in correct period range ' + str(correct8) + ' times.\nPercentage estimated correct: ' + str(percentage8) + '\n')
f.write('Timestack at 2/3 image width and edge detection on video:\nEstimated in correct period range ' + str(correct9) + ' times.\nPercentage estimated correct: ' + str(percentage9) + '\n')

#create overall histogram
total_times = []
for i in range(0,len(times1)):
	total_times.append(times1[i])
for k in range(0,len(times2)):
	total_times.append(times2[k])
for j in range(0,len(times3)):
	total_times.append(times3[j])
for l in range(0,len(times4)):
	total_times.append(times4[l])
for m in range(0,len(times5)):
	total_times.append(times5[m])
for n in range(0,len(times6)):
	total_times.append(times6[n])
for x in range(0,len(times7)):
	total_times.append(times7[x])
for y in range(0,len(times8)):
	total_times.append(times8[y])
for z in range(0,len(times9)):
	total_times.append(times9[z])

total_correct = correct1 + correct2 + correct3 + correct4 + correct5 + correct6 + correct7 + correct8 + correct9

hist_periods, bin_edges = np.histogram(total_times, bins=15, range=(5, 20))
plt.hist(total_times, bins=15, range=(5, 20), color='b')
plt.title('Histogram of periods')
plt.ylabel('Number of occurences')
plt.xlabel('Wave period (seconds)')
#plt.show()
plt.savefig(sys.argv[1] + '_final_hist.png')

final_correct_percentage = (total_correct / len(total_times)) * 100
f.write('Overall percentage correct: ' + str(final_correct_percentage))
f.close()





