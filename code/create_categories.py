import numpy as np
import os

'''read in categories of classifications and copy images for each classification to a different subdirectory'''


def create_category_arr(y_act, y_pred, gal_arr, idx):
    ''' Create and save arrays of gal_IDs that are part of that category
    '''

    # true spirals predicted correctly
    true_spiral = np.where((y_act == 0) & (y_pred == 0))
    np.savetxt('true_spiral.txt', gal_arr[idx[true_spiral]], fmt='%18d')
    # true ellipticals predicted correctly
    true_ell = np.where((y_act == 1) & (y_pred == 1))
    np.savetxt('true_ell.txt', gal_arr[idx[true_ell]], fmt='%18d')
    # true uncertain predicted correctly
    true_unc = np.where((y_act == 2) & (y_pred ==2))
    np.savetxt('true_unc.txt', gal_arr[idx[true_unc]], fmt='%18d')
    # true spirals predicted as ellipticals
    spiral_pred_ell = np.where((y_act == 0) & (y_pred == 1))
    np.savetxt('spiral_pred_ell.txt', gal_arr[idx[spiral_pred_ell]], fmt='%18d')
    # true spirals predicted as uncertain
    spiral_pred_unc = np.where((y_act == 0) & (y_pred == 2))
    np.savetxt('spiral_pred_unc.txt', gal_arr[idx[spiral_pred_unc]], fmt='%18d')
    # true elliptical predicted as spiral
    ell_pred_spiral = np.where((y_act == 1) & (y_pred == 0))
    np.savetxt('ell_pred_spiral.txt', gal_arr[idx[ell_pred_spiral]], fmt='%18d')
    # true elliptical predicted as uncertain
    ell_pred_unc = np.where((y_act == 1) & (y_pred == 2))
    np.savetxt('ell_pred_unc.txt', gal_arr[idx[ell_pred_unc]], fmt='%18d')
    # true uncertain predicted as spiral
    unc_pred_spiral = np.where((y_act == 2) & (y_pred == 0))
    np.savetxt('unc_pred_spiral.txt', gal_arr[idx[unc_pred_spiral]], fmt='%18d')
    # true uncertain predicted as elliptical
    unc_pred_ell = np.where((y_act == 2) & (y_pred == 1))
    np.savetxt('unc_pred_ell.txt', gal_arr[idx[unc_pred_ell]], fmt='%18d')


def get_ID(filename):
    '''read galaxy IDs from filename and store as array of strings'''

    gal_ID_arr = np.loadtxt(filename, dtype=str)
    return gal_ID_arr


def copy_images(gal_ID_arr, dir_name):
    '''copy images for galaxies in gal_ID_arr from image subdirectory to category subdirectory'''

    for gal_ID in gal_ID_arr:
        img_file = "images/img_{0}.png".format(gal_ID)
        os.system("cp {0} {1}".format(img_file, dir_name))



if __name__ == '__main__':
    file_list = ["true_spiral.txt", "spiral_pred_ell.txt", "spiral_pred_unc.txt",
				 "true_ell.txt", "ell_pred_spiral.txt", "ell_pred_unc.txt", 
				 "true_unc.txt", "unc_pred_spiral.txt", "unc_pred_ell.txt"]
    for file in file_list:
        dir_name = file.split(".")[0]
        print file, dir_name
        copy_images(get_ID(file), dir_name)
