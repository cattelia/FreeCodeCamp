import numpy as np

def calculate(list):
    n = 3

    '''
    Expected input:
        List consisting of 9 numbers.
        Throw ValueError if not.

    Excepted output:
        Dictionary in this form factor.
            {
            'mean': [axis1, axis2, flattened],
            'variance': [axis1, axis2, flattened],
            'standard deviation': [axis1, axis2, flattened],
            'max': [axis1, axis2, flattened],
            'min': [axis1, axis2, flattened],
            'sum': [axis1, axis2, flattened]
            }
    '''

    # Convert the list into a 3x3 matrix
    # throw Value error if the list is not equal to 9 numbers.

    try:
        n_matrix = np.array(list)
        matrix = n_matrix.reshape(-1, n)
        new_matrix = matrix.tolist()
        print(new_matrix)

    except ValueError:
        raise ValueError("List must contain nine numbers.")

    dict_output = {
        arith: [func(matrix, axis=i).tolist() for i in [0, 1, None]]
        for (arith, func) in zip(["mean", "median", "varience", "standard deviation", "max", "min", "sum"],
                             [np.mean, np.median, np.var, np.std, np.amax, np.amin, np.sum])
    }

    
    output = {

        "mean" : [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(),  np.mean(matrix).tolist()]  ,
        "variance" : [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix).tolist()],
        "standart deviation" : [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix).tolist()],
        "max" : [ np.amax(matrix, axis=0).tolist(), np.amax(matrix, axis=1).tolist(), np.amax(matrix).tolist()],
        "min" : [np.amin(matrix, axis=0).tolist(), np.amin(matrix, axis=1).tolist(), np.amin(matrix).tolist()],
        "sum" : [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix).tolist()]
    }

    print(output)
    
    '''# This. is. ugly.
    men_c = [np.mean(n_matrix[:, i]) for i in range(n)] # columns
    men_r = [np.mean(n_matrix[i, :]) for i in range(n)] # rows
    men_f = np.mean(new_matrix) # flattened

    med_c = [np.median(n_matrix[:, i]) for i in range(n)] # columns
    med_r = [np.median(n_matrix[i, :]) for i in range(n)] # rows
    med_f = np.median(new_matrix) # flattened

    var_c = [np.var(n_matrix[:, i]) for i in range(n)] # columns
    var_r = [np.var(n_matrix[i, :]) for i in range(n)] # rows
    var_f = np.var(new_matrix) # flattened

    std_c = [np.std(n_matrix[:, i]) for i in range(n)] # columns
    std_r = [np.std(n_matrix[i, :]) for i in range(n)] # rows
    std_f = np.std(new_matrix) # flattened

    max_c = [np.max(n_matrix[:, i]) for i in range(n)] # columns
    max_r = [np.max(n_matrix[i, :]) for i in range(n)] # rows
    max_f = np.max(new_matrix) # flattened  

    min_c = [np.min(n_matrix[:, i]) for i in range(n)] # columns
    min_r = [np.min(n_matrix[i, :]) for i in range(n)] # rows
    min_f = np.min(new_matrix) # flattened

    sum_c = [np.sum(n_matrix[:, i]) for i in range(n)] # columns
    sum_r = [np.sum(n_matrix[i, :]) for i in range(n)] # rows
    sum_f = np.sum(new_matrix) # flattened
    '''

    #return calculations

calculate([0,1,2,3,4,5,6,7,8])
