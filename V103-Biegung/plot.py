import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

D, P = np.genfromtxt('daten1.txt', unpack=True)

def f(x, c, b):
   return c * x + b

x_plot = np.linspace(0,80)
params, covariance_matrix = curve_fit(f, P, D)
plt.plot(x_plot, f(x_plot, *params), 'k-', label='Anpassungsfunktion', linewidth=0.5)
print(params)
print(np.sqrt(np.diag(covariance_matrix)))
plt.gcf().subplots_adjust(bottom=0.18)
plt.plot(P ,D, 'r.', label='Biegung an Stelle x', Markersize=4)
plt.title('Verhältnis Auslenkung zu Polynom')
plt.legend()
plt.grid()
plt.xlabel(r'$(Lx^2 -\frac{x^3}{3})$ $\cdot$ $10^{3}/m^3$')
plt.ylabel(r'$D_R(x)$ $\cdot$ $10^{3}/m$')
plt.savefig('build/plot.pdf')
