#Matrix Chain Multiplication

import numpy as np

def maxtrix_multiply(mtx_a, mtx_b) :
    if mtx_a.shape[1] is not mtx_b.shape[0] :
        return None
    
    mtx_row = mtx_a.shape[0]
    mtx_a_col = mtx_a.shape[1]
    mtx_col = mtx_b.shape[1]

    mtx_result = np.zeros([mtx_row,mtx_col], mtx_a.dtype)

    for i in range(mtx_row) :
        for j in range(mtx_col) :
            for k in range(mtx_a_col) :
                mtx_result[i][j] = mtx_result[i][j] + mtx_a[i][k] * mtx_b[k][j]

    return mtx_result



if __name__ == "__main__":
    x = np.array([[1,2,3],[1,2,3]])
    y = np.array([[1,1],[1,1],[1,1]])

    z = maxtrix_multiply(x,y)
    print(z)
