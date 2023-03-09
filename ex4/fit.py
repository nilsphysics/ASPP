import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

data = np.load('I_q_IPA_exp.npy')
model = np.load('I_q_IPA_model.npy')

filt = ~np.isnan(data[:,1])

data_x = data[:,0][filt]
data_y = data[:,1][filt]

data_int = sc.interpolate.interp1d(data_x, data_y)
model_int = sc.interpolate.interp1d(model[:,0], model[:,1])

xnew = np.arange(data_x[0], data_x[-1], 0.01)

def function(scalar):
    return np.sum((data_int(xnew) - model_int(xnew) * scalar)**2)

res = sc.optimize.minimize_scalar(function)

plt.plot(data[:,0], data[:,1], label='data')
plt.plot(xnew, data_int(xnew), label='data interpolation')
plt.plot(model[:,0], model[:,1], label='model')
plt.plot(xnew, model_int(xnew), label='model interpolation')
plt.legend()
plt.xlabel('scattering vector')
plt.ylabel('scattering strength')
plt.tight_layout()
plt.show()

plt.plot(data[:,0], data[:,1], label='data')
plt.plot(model[:,0], model[:,1] * res.x, label='model best fit')
plt.legend(title='model scaling: ' + str(round(res.x, 10)))
plt.xlabel('scattering vector')
plt.ylabel('scattering strength')
plt.tight_layout()
plt.show()

