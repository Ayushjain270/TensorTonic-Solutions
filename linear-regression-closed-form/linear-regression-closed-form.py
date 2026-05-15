import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    
    rows = len(X)
    cols = len(X[0])
    t = []
    for i in range(cols):
        new = [] 
        for j in range(rows):
            new.append(X[j][i])
        t.append(new)
    
    
    w = np.linalg.inv(np.dot(t,X)).dot(t).dot(y)
    return w
    