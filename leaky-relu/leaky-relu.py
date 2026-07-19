import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    out = []
    for i in x: 
        if i >= 0 : 
            out.append(i)
        else : 
            out.append(alpha*i)

    return np.asarray(out)