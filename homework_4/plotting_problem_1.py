import sys
import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

rk45_data = np.recfromtxt('rk45.txt', names = True)

x = rk45_data['x']
y = rk45_data['y']
y_analytic = rk45_data['y_analytic']
y_RK4 = rk45_data['yRK4']
y_RK5 = rk45_data['yRK5']
h = rk45_data['h']

h_min = np.min(h)
print 'h min'
print h_min

plt.plot(x,y,color = 'black', alpha = 0.5)
plt.plot(x, y_analytic, linestyle = '--',color= 'green', alpha = 1.0)
plt.legend(['RK45', 'y = -sin(pi*cos(x))'], loc = 'lower left')
plt.title('Part (a): y(x) = -sin(pi*cos(x))')
plt.xlabel('x')
plt.ylabel('y')

plt.xlim(-0.1, 10.1)
#plt.savefig('problem_1_a.png')
plt.show()
plt.close()

plt.plot(x, y_RK4, color = 'green',alpha = 0.7)
plt.plot(x, y_RK5, color = 'purple', linestyle = '--',alpha = 1.0)
plt.legend(['RK4', 'RK5'], loc = 'lower left')
plt.title('Part (b): RK4 vs RK5\nh=0.01')
plt.xlabel('x')
plt.ylabel('y')
#plt.savefig('problem_1_b.png')
plt.show()
plt.close()


plt.plot(x, h)
plt.title('Part (c): x vs step size q*h')
plt.xlabel('x')
plt.ylabel('h')
plt.savefig('problem_1_c.png')
plt.show()
plt.close()


'''
real    0m0.199s
user    0m0.046s
sys     0m0.046s
'''




