def exponential_moving_average(values, alpha):
    """
    Compute the exponential moving average of the given values.
    """
    EMA = values[0]
    out= []
    out.append(EMA)
    for i in range(1 , len(values)) : 
        EMA = (1-alpha)*EMA + alpha*values[i]
        out.append(EMA)

    return out