import sys
import numpy as np
import matplotlib.pyplot as plt


data_inner_a = np.recfromtxt('henon_inner_a.txt', names = True)

x_a_inner = data_inner_a['x']
y_a_inner = data_inner_a['y']

fig = plt.figure()
ax = fig.add_subplot(111)
#plt.scatter(x_a, y_a, marker = 'o', edgecolor='blue', facecolor='none')
ax.scatter(x_a_inner, y_a_inner, marker = 'o', edgecolor='purple',facecolor='none',alpha=0.15)
plt.title(r'$\alpha = 0.2$ $\beta = 0.9991$')
plt.legend(['$x_0 =  0.0$\n$y_0 = -3.0$'],loc = 'upper right')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.savefig('part_a_left.png')
plt.show()
plt.close()


data_right = np.recfromtxt('henon_right.txt', names = True)

x_right = data_right['x']
y_right = data_right['y']

plt.scatter(x_right, y_right, marker = 'o', edgecolor='gray', facecolor='blue',alpha = 0.15)
plt.title(r'$\alpha = 0.2$ $\beta = -0.9999$')
plt.legend(['$x_0 = {0}$\n$y_0 = {1}$'.format(x_right[0],y_right[0])],loc = 'upper right')
plt.xlabel('x')
plt.ylabel('y')
#plt.xlim(-0.3,1.3)
#plt.ylim(-1.3,0.3)
plt.savefig('part_a_right.png')
plt.show()
plt.close()


data_b = np.recfromtxt('henon_b.txt', names = True)

x_b = data_b['x']
y_b = data_b['y']

plt.scatter(x_b, y_b, marker = 'o', edgecolor='purple', facecolor='none',alpha = 1.0)
plt.title(r'$\alpha = 1.4$ $\beta = 0.3$')
plt.legend(['$x_0 = {0}$\n$y_0 = {1}$'.format(x_b[0],y_b[0])],loc = 'upper right')
plt.xlabel('x')
plt.ylabel('y')
#plt.xlim(-0.3,1.3)
#plt.ylim(-1.3,0.3)
plt.savefig('part_b.png')
plt.show()
plt.close()