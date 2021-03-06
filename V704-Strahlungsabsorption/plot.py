import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import mu_0
from scipy.optimize import curve_fit
from uncertainties import ufloat

D, A = np.genfromtxt('gammazahlen.txt', unpack=True)
F =[1.7, 1.4, 1.3, 1.1, 1.0, 0.9, 0.8, 0.7, 0.7, 0.7]

def f(x, a, b):
   return a * x + b


x_plot = np.linspace(1, 21)
params, covariance_matrix = curve_fit(f, D, np.log(A))
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.errorbar(D, np.log(A), yerr=[np.log(A+F)-np.log(A), np.log(A)-np.log(A-F)], fmt = 'o',color='r', markersize=2, capsize=2, ecolor='b', elinewidth=0.5, markeredgewidth=0.5)
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(D, np.log(A), 'r.', label='Messwerte', Markersize=4)
plt.legend()
plt.grid()
plt.xlim((1, 21))
#plt.ylim((2, 20))
plt.ylabel(r'$\ln(A/A_0)$')
plt.xlabel(r'$D/$mm')
plt.savefig('build/plot.pdf')
