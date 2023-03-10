import scipy as sc
import numpy as np
import matplotlib.pyplot as plt

# scipy.linalg

matA = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

vec = np.array([[1], [2], [3]])

x_c = sc.linalg.solve(matA, vec)
b_solve = np.matmul(matA, x_c)

matB = np.random.rand(3, 3) * 10 -5

#det(matA) = 0, thats why there are issues with this
x_e = sc.linalg.solve(matA, matB)
x_e2 = np.matmul(np.linalg.inv(matA), matB)

eigA = sc.linalg.eig(matA, left=True, right=True)
for i in eigA:
    print(i)

#det(matA) = 0, thats why there are issues with this
#inv_det = 1 / sc.linalg.det(matA)
det_inv = sc.linalg.det(np.linalg.inv(matA))

norm0 = sc.linalg.norm(matA, 'nuc')
norm1 = sc.linalg.norm(matA, 'fro')
norm2 = sc.linalg.norm(matA, np.inf)
norm3 = sc.linalg.norm(matA, -np.inf)

# scipy.stats
x = np.linspace(0,20,100)
pos = sc.stats.poisson(10)

fig1 = plt.figure(figsize=(7, 2), dpi=200)

ax  = fig1.add_subplot(131)
ax.plot(x, pos.pmf(x), 'ro', ms=8, mec='r')
ax.vlines(x, 0, pos.pmf(x), colors='r', linestyles='-', lw=2)
plt.title('PMF')
plt.ylabel('Probability')

ax  = fig1.add_subplot(132)
ax.plot(x, pos.cdf(x), 'ro', ms=8, mec='r')
plt.title('CDF')
plt.ylabel('cumulative probability')

ax  = fig1.add_subplot(133)
ax.hist(np.random.poisson(7, 1000), density=True)
plt.title('HIST')
plt.ylabel('counts')
plt.tight_layout()


#normal
x = np.linspace(0,20,100)
norm = sc.stats.norm(10, 2)

fig2 = plt.figure(figsize=(7, 2), dpi=200)

ax  = fig2.add_subplot(131)
ax.plot(x, norm.pdf(x), 'ro', ms=8, mec='r')
#ax.vlines(x, 0, norm.pdf(x), colors='r', linestyles='-', lw=2)
plt.title('PDF')
plt.ylabel('Probability')

ax  = fig2.add_subplot(132)
ax.plot(x, norm.cdf(x), 'ro', ms=8, mec='r')
plt.title('CDF')
plt.ylabel('cumulative probability')

ax  = fig2.add_subplot(133)
ax.hist(np.random.normal(10, 2, 1000), density=True)
plt.title('HIST')
plt.ylabel('counts')
plt.tight_layout()
#plt.show()

rvs1 = sc.stats.poisson.rvs(loc=5, mu = 7, size=500)
rvs2 = sc.stats.norm.rvs(loc=5, scale=10, size=500)

test = sc.stats.ttest_ind(rvs1, rvs2)
print(test)
