import numpy as np
import os

'''read in categories of classifications and copy images for each classification to a different subdirectory'''


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
