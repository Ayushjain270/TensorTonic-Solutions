import numpy as np
def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    sum =0
    for i in range(len(y_pred)):
        error = (y_pred[i] - y_true[i])*(y_pred[i] - y_true[i])
        sum = sum + error
    mean = sum/len(y_pred)
    return mean  