#LCS

import numpy as np

'''
X={X1,X2,...Xm}
Z={Z1,Z2,...Zk}
If there is a strictly incremental sequence of X's subscript,for all j=1,2...k,satisfy X[I[j]] = Z[j],then define Z is a subsequence of X.
Given two sequences X,Y, if Z is both a subsequence of X and Y.Then we call it's X and Y's common sequence.

eg.
X='ABCBDAB'
Y='BDCABA'
LCS(X,Y)='BCBA'
'''

def get_lcs(x,y) :
    m = len(x)
    n = len(y)

    c = np.zeros((m + 1,n + 1),int)

    for i in range(1,m+1) :
        for j in range(1,n+1):
            if x[i-1] == y[j-1] :
                 c[i,j] = c[i-1,j-1] + 1
            elif c[i-1,j] >= c[i,j-1] :
                c[i,j] = c[i-1,j]
            else :
                c[i,j] = c[i,j-1]

    return c[m,n]


if __name__ == "__main__":
    x = 'ABCBDAB'
    y = 'BDCABA'

    print(get_lcs(x,y))