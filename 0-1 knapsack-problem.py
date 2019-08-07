'''
product:
a1,a2,a3,...,an

weight:
w1,w2,w3,...,wn

value:
v1,v2,v3,...,vn

##Find the Optimal Substructure Property
Suppose the capacity of the knapsack is Max(w),the set of products tha can achieve maximum value is :
i1,i2,i3,...,in (the i(n)'s value is the subscript of set a. ) 

Using F(n,C) to represent the value of placing the first n items in a knapsack of size C.
If i{1,...,n} is best solution of Max(C)
Proof by cut-paste,then i{1,...,n-1} must be the best solution of Max(C) - w(i(n)),
So it can be proved that 0-1 knapsack has Optimal Substructure Property.

##Suppose a point that is the optimal choice point
if F(i,C) = V
When select the (i+1)th product,we can choose whether to put it in or not,if put it in,then F(i+1,C + w(i)) = V + v(i),on the contrary,if we discard it,then F(i+1,C) = V.

F(n,C)= F(i-1,C) #discard it
      = Max(F(i-1,C),F(i-1,C-w(i)) + v(i)) #put it in
'''
import numpy as np

def max_value(w, v, max_cap) : 
      size = len(w)

      memo = np.zeros((size,max_cap+1))

      for i in range(1,size) :
            for j in range(1,max_cap+1) :
                  if j < w[i] :
                        memo[i,j] = memo[i-1,j] #knapsack doesn't has enough space to put down product[i]
                  else :
                        memo[i,j] = max(memo[i-1,j],memo[i-1,j-w[i]] + v[i]) #knapsack still has enough space to put down product[i]

      return memo


if __name__ == "__main__":
    w=[0,1,2,3,4,5]
    v=[0,3,1,2,6,0]

    max_cap = 3

    ret = max_value(w,v,max_cap)
    print(ret)
