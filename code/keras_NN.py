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

''' Main pipeline script for creating neural net with keras and fitting it to image data
output predictions for input data'''


if __name__ == '__main__':
    data = np.loadtxt('gal_pos_label.txt', delimiter=',')  	# columns are:  dr7objid,ra,dec,spiral,elliptical,uncertain 
    gal_id = np.genfromtxt('gal_pos_label.txt', delimiter=',', dtype=int, usecols=[0])   
    spiral = data[:,3]
    elliptical = data[:,4]
    uncertain = data[:,5]

    # Take subset of data
    num_images = 20000
    gal_arr = gal_id[0:num_images]
    # Only take center 10000 pixels of each image
    num_pix_cen = 10000
    # Get array of image pixels
    img_arr = read_images.make_img_arr(gal_arr, num_pix_cen, pix_func=read_images.get_pix_flat_cen)
    label_arr = get_labels.get_labels(gal_arr, spiral, elliptical, uncertain, img_arr)
    # Remove images with no data
    img_arr = img_arr[~np.all(img_arr == 0, axis=1)]
    gal_arr = gal_arr[~np.all(img_arr == 0, axis=1)]
    
    # Split data into train and test set
    X_train, X_test, y_train, y_test, idx_train, idx_test = train_test_split(img_arr, label_arr, indices)
    # Normalize
    X_train_norm = X_train/np.max(X_train)
    X_test_norm = X_test/np.max(X_test)
    
    # Build the NN model one piece at a time
    model = Sequential()            
    # Define hidden layer: 10000 pixels in input, output dimension will have 512 nodes, initialize weights using uniform dist
    model.add(Dense(512, input_dim=num_pix_cen, init='uniform'))    
    # Sigmoid activation
    model.add(Activation('sigmoid'))
    # Use 35% dropout on this layer for regularization to avoid overfitting
    model.add(Dropout(0.35))
    # Define another layer with 512 nodes (input and output)
    model.add(Dense(512, init='uniform'))
    # Sigmoid activation
    model.add(Activation('sigmoid'))
    # Use 35% dropout on this layer for regularization to avoid overfitting
    model.add(Dropout(0.35))
    # Last layer (output) has 3 outputs with 512 inputs
    model.add(Dense(y_train20.shape[1], init='uniform'))
    # Activation function is softmax b/c it is the output layer
    model.add(Activation('softmax'))

    # Fit model
    # SGD does go through all data points but only uses a batch at a time, data gets shuffled after each epoch
    sgd = Adam()
    # Choose categorical_crossentropy as loss function b/c softmax was the activation function
    model.compile(loss='categorical_crossentropy', optimizer=Adam())
    # An epoch is one pass through the whole training data set, batch size is number of data points used for each iteration of gradient descent
    NN_fit = model.fit(X_train_norm, y_train, 
          nb_epoch=20, 
          batch_size=150, 
          validation_data = (X_test_norm, y_test),
          show_accuracy = True, verbose=2)

    # Calculate metrics
    y_pred_train = model.predict_classes(X_train_norm)    # Predicted y_train classification
    print "Train Acc:"
    metrics.calc_acc(y_pred_train, y_train)
    y_pred_test = model.predict_classes(X_test_norm)      # Predicted y_test classification
    print "Train Acc:"
    calc_acc(y_pred_test, y_test)
    # Classification report
    y_act = get_labels.get_label_1D(y_test)
    print(classification_report(y_act, y_pred_test, target_names=['spiral', 'elliptical', 'uncertain']))
    # Plot confusion matrix
    cm = confusion_matrix(y_act, y_pred_test)
    plots.plot_confusion_matrix(cm, normed=True)
    # Get probabilities for each classification
    probas = model.predict_proba(X_test_norm)
    # Calculate true positive and false positive rates treating each classifier as binary
    sp_fpr, sp_tpr, _ = roc_curve(y_test20[:,0], probas[:,0])
    ell_fpr, ell_tpr, _ = roc_curve(y_test20[:,1], probas[:,1])
    unc_fpr, unc_tpr, _ = roc_curve(y_test20[:,2], probas[:,2])
    # Plot ROC curves
    plots.plot_ROC_curve(sp_tpr, sp_fpr, ell_tpr, ell_fpr, unc_tpr, unc_fpr)
    # Print AUC scores
    print "AUC for spirals:"
    roc_auc_score(y_test[:,0], probas[:,0])  
    print "AUC for ellipticals:"
    roc_auc_score(y_test[:,0], probas[:,1])    
    print "AUC for uncertain:"
    roc_auc_score(y_test[:,0], probas[:,2])

    # Save predicted probabilities
    np.savetxt('gal_probas.txt', probas, fmt='%1.3f')
    # Make categories of predictions and save these gal IDs
    create_category.create_category_arr(y_act, y_pred_test, gal_arr, idx_test)
    # Save files to appropriate subdirectories
    create_category.main()


 
