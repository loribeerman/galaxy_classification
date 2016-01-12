import numpy as numpy
import matplotlib.pyplot as plt

''' module for plotting functions'''


def plot_precision(s_thres, s_prec, e_prec):
    '''plot spiral and elliptical precision as a function of threshold
    input:  arrays of threshold, spiral precision, elliptical precision
    output:  precision_thresh.png'''

    plt.plot(s_thres, s_prec, color="blue", label = "spiral")
    plt.plot(s_thres, e_prec, color="red", label = "elliptical")
    plt.legend(loc="lower right")
    plt.savefig('precision_thresh.png')


def plot_confusion_matrix(cm, title='Confusion Matrix', target_names=['spiral', 'elliptical', 'uncertain'], cmap=plt.cm.Blues, normed=False):
    '''plot confusion matrix -- predicted label vs actual label classifications
    input:  confusion matrix, 3 x 3 array
    output:  confusion_matrix.png'''
    
    np.set_printoptions(precision=2)
    if normed:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(target_names))
    plt.xticks(tick_marks, target_names, rotation=45)
    plt.yticks(tick_marks, target_names)
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.grid('off')
    plt.savefig('confusion_matrix.png')


def plot_ROC_curve(sp_tpr, sp_fpr, ell_tpr, ell_fpr, unc_tpr, unc_fpr):
    '''plot ROC curves for spiral, elliptical, and uncertain classifications on one plot
    inputs:  true positive and false positive arrays for each classification
    output:  ROC_curve.png'''

    plt.plot([0, 1], [0, 1], 'k--')
    plt.plot(sp_fpr, sp_tpr, linewidth=2, label = 'Spiral')
    plt.plot(ell_fpr, ell_tpr, linewidth=2, label = 'Elliptical')
    plt.plot(unc_fpr, unc_tpr, linewidth=2, label = 'Uncertain')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend(loc='lower right')
    plt.savefig('ROC_curve.png')


def plot_thresh(thresh_arr, spiral, ell, tot, label='accuracy'):
    '''plot threshold vs metric (e.g. accuracy) for spiral, elliptical, and total
    inputs:  arrays of threshold, spiral metric, ell metric, total metric
    output:  label_thresh.png'''
    
    plt.plot(thresh_arr, spiral, color='blue', label='Spiral')
    plt.plot(thresh_arr, ell, color='red', label='Elliptical')
    plt.plot(thresh_arr, tot, color='green', label='Total')
    plt.xlabel('Probability Threshold')
    plt.ylabel(label)
    plt.legend(loc='upper left')
    plt.savefig(label + '_thresh.png')



