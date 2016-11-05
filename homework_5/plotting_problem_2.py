import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

'''
lorenz = np.recfromtxt('lorenz.txt',names = True)

x = lorenz['x']
y = lorenz['y']
z = lorenz['z']


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x,y,z,color = 'purple')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.legend([r'$x_0 = {0}$ $y_0 = {1}$ $z_0 = {2}$'.format(x[0],y[0],z[0])],bbox_to_anchor=(0.78, 1.13))
ax.set_title(r'$\sigma = 10$ $\beta = 8/3$ $\rho = 28$')
plt.savefig('2_a.png')
plt.show()

'''

lorenz_b = np.recfromtxt('lorenz_b.txt',names = True)

x_b = lorenz_b['x']
y_b = lorenz_b['y']
z_b = lorenz_b['z']


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_b,y_b,z_b, color= 'green')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.legend([r'$x_0 = {0}$ $y_0 = {1}$ $z_0 = {2}$'.format(x_b[0],y_b[0],z_b[0])],bbox_to_anchor=(0.75, 1.13))
ax.set_title(r'$\sigma = 10$ $\beta = 8/3$ $\rho = 28$')
plt.savefig('2_b_try.png')
plt.show()
'''
lorenz_c_short_f = np.recfromtxt('lorenz_c_short_first.txt',names = True)

x_c_short_f = lorenz_c_short_f['x']
y_c_short_f = lorenz_c_short_f['y']
z_c_short_f = lorenz_c_short_f['z']

lorenz_c_short_s = np.recfromtxt('lorenz_c_short_second.txt',names = True)

x_c_short_s = lorenz_c_short_s['x']
y_c_short_s = lorenz_c_short_s['y']
z_c_short_s = lorenz_c_short_s['z']

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_c_short_f,y_c_short_f,z_c_short_f, color= 'green', alpha = 1.0)
ax.plot(x_c_short_s,y_c_short_s,z_c_short_s, color= 'orange', alpha = 1.0)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.legend([r'$x_0 = {0}$ $y_0 = {1}$ $z_0 = {2}$ $T = 5s$'.format(x_c_short_f[0],y_c_short_f[0],z_c_short_f[0]),r'$x_0 = {0}$ $y_0 = {1}$ $z_0 = {2}$ $T = 5s$'.format(x_c_short_s[0],y_c_short_s[0],z_c_short_s[0])],bbox_to_anchor=(0.80, 1.13))
#ax.set_title(r'$\sigma = 10$ $\beta = 8/3$ $\rho = 28$')
plt.savefig('2_c_short_try.png')
plt.show()
#........................................................................................................
lorenz_c_long_f = np.recfromtxt('lorenz_c_long_first.txt',names = True)

x_c_long_f = lorenz_c_long_f['x']
y_c_long_f = lorenz_c_long_f['y']
z_c_long_f = lorenz_c_long_f['z']

lorenz_c_long_s = np.recfromtxt('lorenz_c_long_second.txt',names = True)

x_c_long_s = lorenz_c_long_s['x']
y_c_long_s = lorenz_c_long_s['y']
z_c_long_s = lorenz_c_long_s['z']

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_c_long_f,y_c_long_f,z_c_long_f, color= 'green', alpha = 1.0)
ax.plot(x_c_long_s,y_c_long_s,z_c_long_s, color= 'orange', alpha = 1.0)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.legend([r'$x_0 = {0}$ $y_0 = {1}$ $z_0 = {2}$ $T = 50s$'.format(x_c_long_f[0],y_c_long_f[0],z_c_long_f[0]),r'$x_0 = {0}$ $y_0 = {1}$ $z_0 = {2}$ $T = 50s$'.format(x_c_long_s[0],y_c_long_s[0],z_c_long_s[0])],bbox_to_anchor=(0.80, 1.13))
#ax.set_title(r'$\sigma = 10$ $\beta = 8/3$ $\rho = 28$')
plt.savefig('2_c_long_try.png')
plt.show()

'''