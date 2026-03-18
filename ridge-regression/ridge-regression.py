def ridge_regression(X, y, lam):
    """
    Compute ridge regression weights using the closed-form solution.
    """
    # Write code here
  
    rows = len(X)
    cols = len(X[0])

    T =[]
    for  i in range(cols):
        new_row =[]
        for j in range(rows):
            new_row.append(X[j][i])
        T.append(new_row)
    I = np.identity(len(X[0]))
    result = np.linalg.inv(np.dot(T , X ) + lam*I).dot(T).dot(y)  
    return result
        
        

        #for finding the transpose we have to make a list of list with in one list there 