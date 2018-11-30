import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt 
import sys

#input: time periods, period estimate from surfline video
#checks how close estimation is
#output: creates histogram, what fraction of the time did we observe an accurate estimate?
def evaluation(time_periods, period_surfline_min, period_surfline_max, image_name):
	#create histogram
	hist_periods, bin_edges = np.histogram(time_periods, bins=8, range=(5, 21))
	plt.hist(time_periods, bins=8, range=(5, 21), color='b')
	plt.title('Histogram of periods')
	plt.ylabel('Number of occurences')
	plt.xlabel('Wave period (seconds)')
	#plt.show()
	plt.savefig(image_name + '_hist2.png')
	#print(bin_edges)

	#counter for correct estimations of period
	correct_periods = 0
	#go through all periods
	for i in range(0, len(time_periods)):
		if (time_periods[i] >= int(period_surfline_min) and time_periods[i] <= int(period_surfline_max)):
			correct_periods += 1

	#calculate percentage of time correct
	percentage = (correct_periods / len(time_periods)) * 100
	#print('period in estimation range ' + str(percent) + ' percent of the time')
	
	return correct_periods, percentage, hist_periods


