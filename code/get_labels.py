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


