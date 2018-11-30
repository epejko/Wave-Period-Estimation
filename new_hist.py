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

#9 timestack images to calculate periods of
#post processed
times1 = timestack_periods(sys.argv[1] + '_timestack1.png_canny.png')
times2 = timestack_periods(sys.argv[1] + '_timestack2.png_canny.png')
times3 = timestack_periods(sys.argv[1] + '_timestack3.png_canny.png')
# #pre-processed lines
times4 = timestack_periods(sys.argv[1] + '_line.mp4_timestack1.png')
times5 = timestack_periods(sys.argv[1] + '_line.mp4_timestack2.png')
times6 = timestack_periods(sys.argv[1] + '_line.mp4_timestack3.png')
# #pre-processed edges
times7 = timestack_periods(sys.argv[1] + '_edge.mp4_timestack1.png')
times8 = timestack_periods(sys.argv[1] + '_edge.mp4_timestack2.png')
times9 = timestack_periods(sys.argv[1] + '_edge.mp4_timestack3.png')

#evaluation / histogram of each time
correct1, percentage1, hist1 = evaluation(times1, sys.argv[2], sys.argv[3], sys.argv[1] + '_timestack1.png_canny.png')
correct2, percentage2, hist2 = evaluation(times2, sys.argv[2], sys.argv[3], sys.argv[1] + '_timestack2.png_canny.png')
correct3, percentage3, hist3 = evaluation(times3, sys.argv[2], sys.argv[3], sys.argv[1] + '_timestack3.png_canny.png')
correct4, percentage4, hist4 = evaluation(times4, sys.argv[2], sys.argv[3], sys.argv[1] + '_line.mp4_timestack1.png')
correct5, percentage5, hist5 = evaluation(times5, sys.argv[2], sys.argv[3], sys.argv[1] + '_line.mp4_timestack2.png')
correct6, percentage6, hist6 = evaluation(times6, sys.argv[2], sys.argv[3], sys.argv[1] + '_line.mp4_timestack3.png')
correct7, percentage7, hist7 = evaluation(times7, sys.argv[2], sys.argv[3], sys.argv[1] + '_edge.mp4_timestack1.png')
correct8, percentage8, hist8 = evaluation(times8, sys.argv[2], sys.argv[3], sys.argv[1] + '_edge.mp4_timestack2.png')
correct9, percentage9, hist9 = evaluation(times9, sys.argv[2], sys.argv[3], sys.argv[1] + '_edge.mp4_timestack3.png')
#print(hist1)
#calculate the top 5 bins and see if bins are in correct range
#create dictionary of hist1 and bins1
#bins = [5,7,9,11,13,15,17,19]
dictionary1 = {hist1[0]: 5,
				hist1[1]: 7,
				hist1[2]: 9,
				hist1[3]: 11,
				hist1[4]: 13,
				hist1[5]: 15,
				hist1[6]: 17,
				hist1[7]: 19}
sorted_dict1 = sorted(dictionary1)

dictionary2 = {hist2[0]: 5,
				hist2[1]: 7,
				hist2[2]: 9,
				hist2[3]: 11,
				hist2[4]: 13,
				hist2[5]: 15,
				hist2[6]: 17,
				hist2[7]: 19}
sorted_dict2 = sorted(dictionary2)

dictionary3 = {hist3[0]: 5,
				hist3[1]: 7,
				hist3[2]: 9,
				hist3[3]: 11,
				hist3[4]: 13,
				hist3[5]: 15,
				hist3[6]: 17,
				hist3[7]: 19}
sorted_dict3 = sorted(dictionary3)

dictionary4 = {hist4[0]: 5,
				hist4[1]: 7,
				hist4[2]: 9,
				hist4[3]: 11,
				hist4[4]: 13,
				hist4[5]: 15,
				hist4[6]: 17,
				hist4[7]: 19}
sorted_dict4 = sorted(dictionary4)

dictionary5 = {hist5[0]: 5,
				hist5[1]: 7,
				hist5[2]: 9,
				hist5[3]: 11,
				hist5[4]: 13,
				hist5[5]: 15,
				hist5[6]: 17,
				hist5[7]: 19}
sorted_dict5 = sorted(dictionary5)

dictionary6 = {hist6[0]: 5,
				hist6[1]: 7,
				hist6[2]: 9,
				hist6[3]: 11,
				hist6[4]: 13,
				hist6[5]: 15,
				hist6[6]: 17,
				hist6[7]: 19}
sorted_dict6 = sorted(dictionary6)

dictionary7 = {hist7[0]: 5,
				hist7[1]: 7,
				hist7[2]: 9,
				hist7[3]: 11,
				hist7[4]: 13,
				hist7[5]: 15,
				hist7[6]: 17,
				hist7[7]: 19}
sorted_dict7 = sorted(dictionary7)

dictionary8 = {hist8[0]: 5,
				hist8[1]: 7,
				hist8[2]: 9,
				hist8[3]: 11,
				hist8[4]: 13,
				hist8[5]: 15,
				hist8[6]: 17,
				hist8[7]: 19}
sorted_dict8 = sorted(dictionary8)

dictionary9 = {hist9[0]: 5,
				hist9[1]: 7,
				hist9[2]: 9,
				hist9[3]: 11,
				hist9[4]: 13,
				hist9[5]: 15,
				hist9[6]: 17,
				hist9[7]: 19}
sorted_dict9 = sorted(dictionary9)
# print(sorted_dict)
# bin1 = dictionary1.get(sorted_dict[-1])
# bin2 = dictionary1.get(sorted_dict[-2])
# bin3 = dictionary1.get(sorted_dict[-3])
# bin4 = dictionary1.get(sorted_dict[-4])
# bin5 = dictionary1.get(sorted_dict[-5])

#write evaluations to text file
f = open(sys.argv[1] + '_evaluation2.txt', 'w+')
f.write('Surfline estimation: ' + str(sys.argv[2]) + '-' + str(sys.argv[3]) + ' seconds\n\n')
f.write('TOP 5 ESTIMATED BINS (timestack 1/3 then edge):\n1. ' + str(dictionary1.get(sorted_dict1[-1])) + '-' + str((dictionary1.get(sorted_dict1[-1])+2)) + ' seconds\n2. '+ str(dictionary1.get(sorted_dict1[-2])) + '-' + str((dictionary1.get(sorted_dict1[-2])+2)) + ' seconds\n3. '+ str(dictionary1.get(sorted_dict1[-3])) + '-' + str((dictionary1.get(sorted_dict1[-3])+2)) + ' seconds\n4. '+ str(dictionary1.get(sorted_dict1[-4])) + '-' + str((dictionary1.get(sorted_dict1[-4])+2)) + ' seconds\n5. '+ str(dictionary1.get(sorted_dict1[-5])) + '-' + str((dictionary1.get(sorted_dict1[-5])+2)) + ' seconds\n\n')
f.write('TOP 5 ESTIMATED BINS (timestack 1/2 then edge):\n1. ' + str(dictionary2.get(sorted_dict2[-1])) + '-' + str((dictionary2.get(sorted_dict2[-1])+2)) + ' seconds\n2. '+ str(dictionary2.get(sorted_dict2[-2])) + '-' + str((dictionary2.get(sorted_dict2[-2])+2)) + ' seconds\n3. '+ str(dictionary2.get(sorted_dict2[-3])) + '-' + str((dictionary2.get(sorted_dict2[-3])+2)) + ' seconds\n4. '+ str(dictionary2.get(sorted_dict2[-4])) + '-' + str((dictionary2.get(sorted_dict2[-4])+2)) + ' seconds\n5. '+ str(dictionary2.get(sorted_dict2[-5])) + '-' + str((dictionary2.get(sorted_dict2[-5])+2)) + ' seconds\n\n')
f.write('TOP 5 ESTIMATED BINS (timestack 2/3 then edge):\n1. ' + str(dictionary3.get(sorted_dict3[-1])) + '-' + str((dictionary3.get(sorted_dict3[-1])+2)) + ' seconds\n2. '+ str(dictionary3.get(sorted_dict3[-2])) + '-' + str((dictionary3.get(sorted_dict3[-2])+2)) + ' seconds\n3. '+ str(dictionary3.get(sorted_dict3[-3])) + '-' + str((dictionary3.get(sorted_dict3[-3])+2)) + ' seconds\n4. '+ str(dictionary3.get(sorted_dict3[-4])) + '-' + str((dictionary3.get(sorted_dict3[-4])+2)) + ' seconds\n5. '+ str(dictionary3.get(sorted_dict3[-5])) + '-' + str((dictionary3.get(sorted_dict3[-5])+2)) + ' seconds\n\n')
f.write('TOP 5 ESTIMATED BINS (line then timestack 1/3):\n1. ' + str(dictionary4.get(sorted_dict4[-1])) + '-' + str((dictionary4.get(sorted_dict4[-1])+2)) + ' seconds\n2. '+ str(dictionary4.get(sorted_dict4[-2])) + '-' + str((dictionary4.get(sorted_dict4[-2])+2)) + ' seconds\n3. '+ str(dictionary4.get(sorted_dict4[-3])) + '-' + str((dictionary4.get(sorted_dict4[-3])+2)) + ' seconds\n4. '+ str(dictionary4.get(sorted_dict4[-4])) + '-' + str((dictionary4.get(sorted_dict4[-4])+2)) + ' seconds\n5. '+ str(dictionary4.get(sorted_dict4[-5])) + '-' + str((dictionary4.get(sorted_dict4[-5])+2)) + ' seconds\n\n')
f.write('TOP 5 ESTIMATED BINS (line then timestack 1/2):\n1. ' + str(dictionary5.get(sorted_dict5[-1])) + '-' + str((dictionary5.get(sorted_dict5[-1])+2)) + ' seconds\n2. '+ str(dictionary5.get(sorted_dict5[-2])) + '-' + str((dictionary5.get(sorted_dict5[-2])+2)) + ' seconds\n3. '+ str(dictionary5.get(sorted_dict5[-3])) + '-' + str((dictionary5.get(sorted_dict5[-3])+2)) + ' seconds\n4. '+ str(dictionary5.get(sorted_dict5[-4])) + '-' + str((dictionary5.get(sorted_dict5[-4])+2)) + ' seconds\n5. '+ str(dictionary5.get(sorted_dict5[-5])) + '-' + str((dictionary5.get(sorted_dict5[-5])+2)) + ' seconds\n\n')
f.write('TOP 5 ESTIMATED BINS (line then timestack 2/3):\n1. ' + str(dictionary6.get(sorted_dict6[-1])) + '-' + str((dictionary6.get(sorted_dict6[-1])+2)) + ' seconds\n2. '+ str(dictionary6.get(sorted_dict6[-2])) + '-' + str((dictionary6.get(sorted_dict6[-2])+2)) + ' seconds\n3. '+ str(dictionary6.get(sorted_dict6[-3])) + '-' + str((dictionary6.get(sorted_dict6[-3])+2)) + ' seconds\n4. '+ str(dictionary6.get(sorted_dict6[-4])) + '-' + str((dictionary6.get(sorted_dict6[-4])+2)) + ' seconds\n5. '+ str(dictionary6.get(sorted_dict6[-5])) + '-' + str((dictionary6.get(sorted_dict6[-5])+2)) + ' seconds\n\n')
f.write('TOP 5 ESTIMATED BINS (edge then timestack 1/3):\n1. ' + str(dictionary7.get(sorted_dict7[-1])) + '-' + str((dictionary7.get(sorted_dict7[-1])+2)) + ' seconds\n2. '+ str(dictionary7.get(sorted_dict7[-2])) + '-' + str((dictionary7.get(sorted_dict7[-2])+2)) + ' seconds\n3. '+ str(dictionary7.get(sorted_dict7[-3])) + '-' + str((dictionary7.get(sorted_dict7[-3])+2)) + ' seconds\n4. '+ str(dictionary7.get(sorted_dict7[-4])) + '-' + str((dictionary7.get(sorted_dict7[-4])+2)) + ' seconds\n5. '+ str(dictionary7.get(sorted_dict7[-5])) + '-' + str((dictionary7.get(sorted_dict7[-5])+2)) + ' seconds\n\n')
f.write('TOP 5 ESTIMATED BINS (edge then timestack 1/2):\n1. ' + str(dictionary8.get(sorted_dict8[-1])) + '-' + str((dictionary8.get(sorted_dict8[-1])+2)) + ' seconds\n2. '+ str(dictionary8.get(sorted_dict8[-2])) + '-' + str((dictionary8.get(sorted_dict8[-2])+2)) + ' seconds\n3. '+ str(dictionary8.get(sorted_dict8[-3])) + '-' + str((dictionary8.get(sorted_dict8[-3])+2)) + ' seconds\n4. '+ str(dictionary8.get(sorted_dict8[-4])) + '-' + str((dictionary8.get(sorted_dict8[-4])+2)) + ' seconds\n5. '+ str(dictionary8.get(sorted_dict8[-5])) + '-' + str((dictionary8.get(sorted_dict8[-5])+2)) + ' seconds\n\n')
f.write('TOP 5 ESTIMATED BINS (edge then timestack 2/3):\n1. ' + str(dictionary9.get(sorted_dict9[-1])) + '-' + str((dictionary9.get(sorted_dict9[-1])+2)) + ' seconds\n2. '+ str(dictionary9.get(sorted_dict9[-2])) + '-' + str((dictionary9.get(sorted_dict9[-2])+2)) + ' seconds\n3. '+ str(dictionary9.get(sorted_dict9[-3])) + '-' + str((dictionary9.get(sorted_dict9[-3])+2)) + ' seconds\n4. '+ str(dictionary9.get(sorted_dict9[-4])) + '-' + str((dictionary9.get(sorted_dict9[-4])+2)) + ' seconds\n5. '+ str(dictionary9.get(sorted_dict9[-5])) + '-' + str((dictionary9.get(sorted_dict9[-5])+2)) + ' seconds\n\n')


# #create overall histogram
# total_times = []
# for i in range(0,len(times1)):
# 	total_times.append(times1[i])
# for k in range(0,len(times2)):
# 	total_times.append(times2[k])
# for j in range(0,len(times3)):
# 	total_times.append(times3[j])
# for l in range(0,len(times4)):
# 	total_times.append(times4[l])
# for m in range(0,len(times5)):
# 	total_times.append(times5[m])
# for n in range(0,len(times6)):
# 	total_times.append(times6[n])
# for x in range(0,len(times7)):
# 	total_times.append(times7[x])
# for y in range(0,len(times8)):
# 	total_times.append(times8[y])
# for z in range(0,len(times9)):
# 	total_times.append(times9[z])

# total_correct = correct1 + correct2 + correct3 + correct4 + correct5 + correct6 + correct7 + correct8 + correct9

# hist_periods, bin_edges = np.histogram(total_times, bins=8, range=(5, 21))
# plt.hist(total_times, bins=8, range=(5, 21), color='b')
# plt.title('Histogram of periods')
# plt.ylabel('Number of occurences')
# plt.xlabel('Wave period (seconds)')
# #plt.show()
# plt.savefig(sys.argv[1] + '_final_hist2.png')

# final_correct_percentage = (total_correct / len(total_times)) * 100
# f.write()
f.close()

