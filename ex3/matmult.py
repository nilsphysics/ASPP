# Program to multiply two matrices using nested loops
import random
import time
import numpy as np

#for loops are very inefficient in python, especially the matrix definition cost a lot of time. 
#Using numpy improves this by factor of about 100 as it wraps matrix multiplication in C

st = time.time()

N = 250

X_test = np.random.rand(N,N) * 100
Y_test = np.random.rand(N,N+1) * 100
R_test = np.matmul(X_test, Y_test)

print(R_test)

end = time.time()

print(end -  st)

"""
print(R_test.shape)
print(X_test.shape)

X = []
for i in range(N):
    #this for loop takes too long
    X.append([random.randint(0,100) for r in range(N)])

print(np.array(X).shape)

# Nx(N+1) matrix
Y = []
for i in range(N):
    #this for loop takes too long
    Y.append([random.randint(0,100) for r in range(N+1)])

# result is Nx(N+1)
result = []
for i in range(N):
    result.append([0] * (N+1))

print(np.array(result).shape)

# iterate through rows of X
for i in range(len(X)):
    # iterate through columns of Y
    for j in range(len(Y[0])):
        # iterate through rows of Y
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]
print(np.array(result).shape)
#for r in result:
#    print(r)

"""

