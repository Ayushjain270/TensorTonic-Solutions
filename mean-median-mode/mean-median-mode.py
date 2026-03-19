import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    #mean
    x.sort()
    sum =0
    for i in range(len(x)):
        sum = sum + x[i]
    mean = sum/len(x)

    #median 
    if len(x)%2 ==0:
        y = int(len(x)/2)
        median = (x[y] + x[y-1])/2
    else :
        y = int(len(x)/2)
        median = x[y] 

    #mode 
    count = Counter(x)
    mode = max(count , key = count.get)
    return float(mean) , float(median) , float(mode)
        
        

    
        
    
    