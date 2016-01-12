import numpy as numpy
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import os
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.optimizers import SGD, RMSprop, Adagrad, Adam, Adadelta
from keras.utils import np_utils
from sklearn.cross_validation import train_test_split
from scipy import misc
from sklearn.metrics import roc_auc_score, roc_curve, classification_report, confusion_matrix
import read_images
import get_labels
import Metrics
import Plots

'''create neural net with keras and fit it to data (use final model)
output predictions for input data'''


if __name__ == '__main__':
    data = np.loadtxt('gal_pos_label.txt', delimiter=',')  	# columns are:  dr7objid,ra,dec,spiral,elliptical,uncertain 
    gal_id = np.genfromtxt('gal_pos_label.txt', delimiter=',', dtype=int, usecols=[0])   
    spiral = data[:,3]
    elliptical = data[:,4]
    uncertain = data[:,5]

    # take subset
    num_images = 20000
    gal_set20 = gal_id[0:num_images]
    # only take center 10000 pixels
    num_pix_cen = 10000
    make_img_arr(gal_set20, num_pix_cen, pix_func=read_images.get_pix_flat_cen)


    # script to run whole NN




# calc_y_act became get_label_1D in get_labels.py
get_label_1D(y_test20)


#calc thresholds starting with # loop over high prob values
max_prob = np.max(probas, axis=1)
thresh_arr = np.arange(0.1, 0.9, 0.05)
spiral_acc = np.zeros(len(thresh_arr))
