import numpy as np


def bg_subtract(img_arr):
	'''subtract average of background (10 pixels at each corner) from 1D image array'''

	img_arr_bg = np.zeros((img_arr.shape[0], img_arr.shape[1]))
	bg = np.zeros(img_arr.shape[0])
	for i in range(img_arr.shape[0]):
    	bg[i] = np.mean((img_arr[i][0:10], img_arr[i][190:200], img_arr[i][39800:39810], img_arr[i][39990:40000]))
    	img_arr_bg[i] = img_arr[i] - bg[i]

    return img_arr_bg