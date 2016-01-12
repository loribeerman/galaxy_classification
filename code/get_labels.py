import numpy as np


def get_labels(gal_set, spiral, elliptical, uncertain, img_arr):

	'''code to get label array for subset of data
	label array will have n_rows and 1 columns for each label:  spiral, elliptical, uncertain
	gal_set is subset of array of gal IDs, img_arr is array of image pixels having length = number of images in gal_set
	spiral, elliptical, and uncertain are arrays containing 1 or 0'''

	label_arr = np.zeros((img_arr.shape[0], 3))
	for ix, gal in enumerate(gal_set):    
    	pos = np.where(gal_set == gal)
    	label_arr[ix, 0] = spiral[pos[0][0]]
    	label_arr[ix, 1] = elliptical[pos[0][0]]
    	label_arr[ix, 2] = uncertain[pos[0][0]]

    return label_arr


def get_label_1D(label_arr):
    '''creates classification label from column information in 3D label array
    goes from n x 3 array to n x 1
    1, 0, 0 becomes 0
    0, 1, 0 becomes 1
    0, 0, 1 becomes 2'''
    
    y_act = np.zeros(len(label_arr))
    for i in range(len(label_arr)):
        if label_arr[i][0] == 1:
            y_act[i] = 0
        elif label_arr[i][1] == 1:
            y_act[i] = 1
        elif label_arr[i][2] == 1:
            y_act[i] = 2
                
    return y_act