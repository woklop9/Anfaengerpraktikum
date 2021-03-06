import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

t, U = np.genfromtxt('entladung.txt', unpack=True)

def f(x, c, b):
   return c * x + b

x_plot = np.linspace(0, 6)
params, covariance_matrix = curve_fit(f, t, np.log(U))
errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
c = ufloat(params[0], errors[0])
print('c = ', c)
print(-1/c)
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(t ,np.log(U), 'r.', label='Messwerte', Markersize=4)
plt.title('Kondensatorspannung zu dem Zeitpunkt t')
plt.legend()
plt.xlim((0, 5.5))
plt.grid()
plt.xlabel(r'$t/ms$')
plt.ylabel(r'$\ln{\frac{U_C}{U_0}}$')
plt.savefig('build/plot1.pdf')
