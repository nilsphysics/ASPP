import numpy as np

n_a = np.zeros(10)
n_a[4] = 1

n_b = np.arange(10, 50, 1)

n_c = np.flip(n_b)

n_d = np.random.rand(3, 3) * 8

n_e1 = np.array([1,2,0,0,4,0])
n_e = np.where(n_e1 != 0)[0]

n_f = np.mean(np.random.rand(30))

n_g = np.zeros((2, 20))
for i in range(len(n_g)):
    n_g[i][0] = 1
    n_g[i][-1] = 1

n_h = np.zeros((8,8))
for i in range(len(n_h)):
    if (i % 2) == 0:
        for j in range(len(n_h[i])):
            if (j % 2) == 0:
                n_h[i][j] = 1
    else:
        for j in range(len(n_h[i])):
            if (j % 2) != 0:
                n_h[i][j] = 1


n_i = np.tile( np.array([[0,1],[1,0]]), (4, 4))

n_j = np.arange(11)
n_j[4:8] *= -1

n_k = np.sort(np.random.random(10))

n_l1 = np.random.randint(0,2,5)
n_l2 = np.random.randint(0,2,5)
equal = np.where(n_l1 == n_l2)[0]

n_m = np.arange(10, dtype=np.int32)
n_m= n_m.astype('float32')

n_n1 = np.arange(9).reshape(3,3)
n_n2 = n_n1 + 1
n_n3 = np.dot(n_n1,n_n2)

print(n_n1)
print(n_n2)
print(n_n3)

n_n4 = np.trace(n_n3)
print(n_n4)



