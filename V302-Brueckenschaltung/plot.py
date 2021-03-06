import matplotlib.pyplot as plt
import numpy as np

f, Ub, Us = np.genfromtxt('Messwerte.txt', unpack=True)

w = np.linspace(0,1)
v = np.linspace(1,100, 200)
plt.plot(f/482.76 , Ub/Us, 'r.', label='Messwerte', Markersize=4)
plt.plot(w , np.sqrt((w**2-1)**2/(9*((1-w**2)**2+9*w**2))), 'k-', label='Theoriekurve', linewidth=0.5)
plt.plot(v , np.sqrt((v**2-1)**2/(9*((1-v**2)**2+9*v**2))), 'k-', linewidth=0.5)
plt.title('Quotient der Spannungsamplituden in Abhängigkeit der Frequenz.')
plt.legend()
plt.grid()
plt.xscale('log')
plt.xlim((0, 100))
plt.xlabel(r'$\frac{f}{f_0}$')
plt.ylabel(r'$\frac{U_{Br}}{U_s}$')
plt.gcf().subplots_adjust(bottom=0.18)
plt.savefig('build/plot.pdf')
