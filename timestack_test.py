import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt 
import sys
import time
from timestack_periods import *
from evaluation import * 
from draw_timestacks import * 

times1 = timestack_periods('timestack_tester.png')

c1, p1, hist1 = evaluation(times1, 7, 9, 'timestack_tester.png')

dictionary1 = {hist1[0]: 5,
				hist1[1]: 7,
				hist1[2]: 9,
				hist1[3]: 11,
				hist1[4]: 13,
				hist1[5]: 15,
				hist1[6]: 17,
				hist1[7]: 19}
sorted_dict1 = sorted(dictionary1)

f = open('model_eval.txt', 'w+')
print('TOP 2 ESTIMATED BINS:\n1. ' + str(dictionary1.get(sorted_dict1[-1])) + '-' + str((dictionary1.get(sorted_dict1[-1])+2)) + ' seconds\n2. '+ str(dictionary1.get(sorted_dict1[-2])) + '-' + str((dictionary1.get(sorted_dict1[-2])+2)) + ' seconds\n')
f.close()

draw_timestacks('timestack_tester.png', 7, 9)




