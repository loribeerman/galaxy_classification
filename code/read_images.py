import numpy as np
from scipy import misc



def get_pix(filename):
    '''get pixels values for RGB from one image file and read in as a 1D numpy array'''

    img = misc.imread(filename)    # read in image from file
    img_arr = img.reshape(img.shape[0] * img.shape[1] * img.shape[2],)    #reshape into a 1D array

    return img_arr


def get_pix_flat(filename):
    '''get pixel values for greyscale from one image file and read in as a 1D numpy array'''

    img = misc.imread(filename, flatten=1)    # read in image from file
    img_arr = img.reshape(img.shape[0] * img.shape[1],)    #reshape into a 1D array

    return img_arr


def get_pix_flat_cen(filename):

    '''get pixel values for greyscale centers from one image file and read in as a 1D numpy array'''

    img = misc.imread(filename, flatten=1)    # read in image from file
    cen = img[50:150, 50:150]                 # only keep center pixels
    cen_arr = cen.reshape(cen.shape[0] * cen.shape[1],)    #reshape into a 1D array

    return cen_arr


def get_pix_3d(filename):
    '''get pixels values for RGB from one image and read in as a 3D numpy array'''

    img = misc.imread(filename)    # read in image from file
    # reshape into 3 X 200 X 200
    image_slice_red =  img[:, :, 0]
    image_slice_blue = img[:, :, 1]
    image_slice_green = img[:, :, 2]
    img_reshape = np.zeros((3, 200, 200))
    img_reshape[0] = image_slice_red
    img_reshape[1] = image_slice_blue
    img_reshape[2] = image_slice_green

    return img_reshape


def make_img_arr(gal_set, n_pix, pix_func=get_pix):
    '''create image array for subset -- will have n_img rows and n_pix columns
    inputs:
    gal_set is an array of galaxy IDs
    n_pix is the number of pixels we want to include from each image'''

    img_arr = np.zeros((len(gal_set), n_pix))
    for ix, gal in enumerate(gal_set):
        filename = "images/img_{0}.png".format(gal)    # get name of file using gal id
        if os.path.exists(filename):    # make sure image exists
            img_arr[ix] = pix_func(filename)    # get pixels for that image

    return img_arr

