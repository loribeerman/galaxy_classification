import numpy as np
import get_labels

'''module for metrics evaluation'''


def calc_acc(y_pred, y_test):
    '''calculates accuracy between y_pred and y_test
    input: y_pred is a 1D array of length n_image
    input: y_test is a 2D array of shape n_image x 3
    output:  accuracy, float'''
    
    
    y_act = get_labels.get_label_1D(y_test)
    agree = np.where(y_pred == y_act)
    
    return len(agree[0])/float(len(y_pred))



def calc_cm(probas, y_act):
    '''calculates values for confusion matrix from probas and y_act arrays
    input:  probas, an n_image x 3 array of probability values
    ***not prob array here
    input:  y_act, an n_image x 1 array of the actual label values
    outputs:  floats of spiral_acc, ell_acc, spiral_recall, ell_recall, spiral_prec, ell_prec'''
    
    total_pop = float(len(y_act))
    #true positives
    tp_spiral = float(len(np.where((probas[:,0] == 1) & (y_act == 0))[0]))
    tp_ell = float(len(np.where((probas[:,1] == 1) & (y_act == 1))[0]))
    #true negatives
    tn_spiral = float(len(np.where((probas[:,0] == 0) & (y_act != 0))[0]))
    tn_ell = float(len(np.where((probas[:,1] == 0) & (y_act != 1))[0]))
    #false positives
    fp_spiral = float(len(np.where((probas[:,0] == 1) & (y_act != 0))[0]))
    fp_ell = float(len(np.where((probas[:,1] == 1) & (y_act != 1))[0]))
    #false negatives
    fn_spiral = float(len(np.where((probas[:,0] == 0) & (y_act == 0))[0]))
    fn_ell = float(len(np.where((probas[:,1] == 0) & (y_act == 1))[0]))
    
    #accuracy
    spiral_acc = (tp_spiral + tn_spiral) / total_pop
    ell_acc = (tp_ell + tn_ell) / total_pop
    #recall
    spiral_recall = tp_spiral / (tp_spiral + fn_spiral)
    ell_recall = tp_ell / (tp_ell + fn_ell)
    #precision
    spiral_prec = tp_spiral / (tp_spiral + fp_spiral)
    ell_prec = tp_ell / (tp_ell + fp_ell)
    
    return spiral_acc, ell_acc, spiral_recall, ell_recall, spiral_prec, ell_prec



def cm_to_metrics(cm):
    '''calculate metrics from confusion matrix
    input:  cm, a confusion matrix of shape 3 x 3
    outputs:  floats of spiral_acc, ell_acc, spiral_recall, ell_recall, spiral_prec, ell_prec, f1_spiral, f1_ell'''
    
    tp_spiral = cm[0][0]
    tn_spiral = cm[1][1] + cm[1][2] + cm[2][1] + cm[2][2]
    tp_ell = cm[1][1]
    tn_ell = cm[0][0] + cm[0][2] + cm[2][0] + cm[2][2]
    tp_unc = cm[2][2]   # not used
    tn_unc = cm[0][0] + cm[0][1] + cm[1][0] + cm[1][1] #not used
    fn_spiral = cm[0][1] + cm[0][2]
    fn_ell = cm[1][0] + cm[1][2]
    fp_spiral = cm[1][0] + cm[2][0]
    fp_ell = cm[0][1] + cm[2][1]

    
    spiral_acc = (tp_spiral + tn_spiral) / float(np.sum(cm))
    ell_acc = (tp_ell + tn_ell) / float(np.sum(cm))
    spiral_recall = float(tp_spiral) / (tp_spiral + fn_spiral)
    ell_recall = float(tp_ell) / (tp_ell + fn_ell)
    spiral_prec = float(tp_spiral) / (tp_spiral + fp_spiral)
    ell_prec = float(tp_ell) / (tp_ell + fp_ell)
    f1_spiral = 2.*tp_spiral / (2.*tp_spiral + fp_spiral + fn_spiral)
    f1_ell = 2.*tp_ell / (2.*tp_ell + fp_ell + fn_ell)
    
    return spiral_acc, ell_acc, spiral_recall, ell_recall, spiral_prec, ell_prec, f1_spiral, f1_ell




