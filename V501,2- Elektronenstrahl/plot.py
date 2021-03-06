import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import mu_0
from scipy.optimize import curve_fit
from uncertainties import ufloat

I, D = np.genfromtxt('daten_bfeld_250.txt', unpack=True)
L = 0.175
N = 20*10**4
R = 0.282

def f(x, a, b):
   return a * x + b

x_plot = np.linspace(-0.1, 1.8)
params, covariance_matrix = curve_fit(f, mu_0*8/np.sqrt(125)*N*I/R, D/(L**2+D**2))
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(mu_0*8/np.sqrt(125)*N*I/R, D/(L**2+D**2), 'r.', label='Messwerte', Markersize=4)
plt.legend()
plt.grid()
plt.xlim((-0.1, 1.8))
plt.xlabel(r'$B = \mu_0\cdot\frac{8}{\sqrt{125}}\cdot\frac{NI}{R}\: / (10^{-4} \cdot T)$')
plt.ylabel(r'$\frac{D}{L^2 + D^2}\: / \frac{1}{m}$')
plt.savefig('build/plot.pdf')

plt.clf()

I, D = np.genfromtxt('daten_bfeld_400.txt', unpack=True)

x_plot = np.linspace(-0.1, 1.8)
params, covariance_matrix = curve_fit(f, mu_0*8/np.sqrt(125)*N*I/R, D/(L**2+D**2))
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(mu_0*8/np.sqrt(125)*N*I/R, D/(L**2+D**2), 'r.', label='Messwerte', Markersize=4)
plt.legend()
plt.grid()
plt.xlim((-0.1, 1.8))
plt.xlabel(r'$B = \mu_0\cdot\frac{8}{\sqrt{125}}\cdot\frac{NI}{R}\: / (10^{-4} \cdot T) $')
plt.ylabel(r'$\frac{D}{L^2 + D^2}\: / \frac{1}{m}$')
plt.savefig('build/plot2.pdf')
