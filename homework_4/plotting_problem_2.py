import sys
import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

rk45_data = np.recfromtxt('rk45_problem_2.txt', names = True)

x = rk45_data['x']
y = rk45_data['y']
#y_analytic = rk45_data['y_analytic']
y_RK4 = rk45_data['yRK4']
y_RK5 = rk45_data['yRK5']
h = rk45_data['h']

h_min = np.min(h)
print 'h min'
print h_min

rk45_data_c = np.recfromtxt('rk45_problem_2_c.txt', names = True)

x_c = rk45_data_c['x']
y_c = rk45_data_c['y']
#y_analytic = rk45_data['y_analytic']
y_RK4_c = rk45_data_c['yRK4']
y_RK5_c = rk45_data_c['yRK5']
h_c = rk45_data_c['h']

h_min_c = np.min(h_c)
print 'h min c'
print h_min_c

rk45_data_d = np.recfromtxt('rk45_problem_2_d.txt', names = True)

x_d = rk45_data_d['x']
y_d = rk45_data_d['y']
#y_analytic = rk45_data['y_analytic']
y_RK4_d = rk45_data_d['yRK4']
y_RK5_d = rk45_data_d['yRK5']
h_d = rk45_data_d['h']

h_min_d = np.min(h_d)
print 'h min d'
print h_min_d

plt.plot(x,y,color = 'black', alpha = 1.0)
plt.legend(['part (a)\ne_tol = 0.001\nvariable h'],loc='lower left')
plt.title("y(t) for Pliny the Elder's Intermittent Fountain")
plt.xlabel('t')
plt.ylabel('y')
plt.xlim(-0.1, 100.1)
plt.savefig('problem_2_a.png')
plt.show()
plt.close()

plt.plot(x_c,y_c,color = 'blue', alpha = 1.0)
plt.legend(['part (c)\nq<2\ne_tol=0.5'], loc = 'upper right')
plt.title("y(t) for Pliny the Elder's Intermittent Fountain")
plt.xlabel('t')
plt.ylabel('y')
plt.xlim(-0.1, 100.1)
plt.savefig('problem_2_c.png')
plt.show()
plt.close()

plt.plot(x_d,y_d,color = 'green', alpha = 1.0)
plt.legend(['part (d)\nfixed dt=0.1'], loc = 'upper right')
plt.title("y(t) for Pliny the Elder's Intermittent Fountain")
plt.xlabel('t')
plt.ylabel('y')
plt.xlim(-0.1, 100.1)
plt.savefig('problem_2_d.png')
plt.show()
plt.close()
'''
plt.plot(x, y_RK4, color = 'green',alpha = 0.7)
plt.plot(x, y_RK5, color = 'purple', linestyle = '--',alpha = 1.0)
plt.legend(['RK4', 'RK5'], loc = 'lower left')
plt.title('Part (b): RK4 vs RK5\nh=0.1')
plt.xlabel('t')
plt.ylabel('y')
plt.savefig('problem_2_b.png')
plt.show()
plt.close()
'''
'''
plt.plot(x, h)
plt.title('Part (c): x vs step size q*h')
plt.xlabel('x')
plt.ylabel('h')
plt.savefig('problem_1_c.png')
plt.show()
plt.close()

'''




