import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def f(x1, x2):
    return 100 * np.sqrt(abs(x2 - 0.01 * x1**2)) + 0.01 * abs(x1 + 10)

x1_min, x1_max = -15.0, -5.0
x2_min, x2_max = -3.0, 3.0
test_point = (-10.0, 1.0) 

x1 = np.linspace(x1_min, x1_max, 100)
x2 = np.linspace(x2_min, x2_max, 100)
X1, X2 = np.meshgrid(x1, x2)
Z = f(X1, X2)

test_value = f(test_point[0], test_point[1])

fig = plt.figure(figsize=(16, 12))
fig.suptitle(f'Графики функции f(x1, x2) = 100√(x2 - 0.01x1²) + 0.01x2 + 10\n'
             f'Тестовая точка: ({test_point[0]}, {test_point[1]}), f(x1, x2) = {test_value:.2f}',
             fontsize=14)

ax1 = fig.add_subplot(221, projection='3d')
surf1 = ax1.plot_surface(X1, X2, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax1.set_xlabel('x1')
ax1.set_ylabel('x2')
ax1.set_zlabel('f(x1, x2)')
ax1.set_title('3D поверхность (изометрический вид)')
fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=5)

ax2 = fig.add_subplot(222, projection='3d')
surf2 = ax2.plot_surface(X1, X2, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax2.view_init(elev=90, azim=0)
ax2.set_xlabel('x1')
ax2.set_ylabel('x2')
ax2.set_zlabel('f(x1, x2)')
ax2.set_title('3D поверхность (вид сверху)')
fig.colorbar(surf2, ax=ax2, shrink=0.5, aspect=5)

ax3 = fig.add_subplot(223)
x20 = test_point[1]
y_x1 = f(x1, x20)
ax3.plot(x1, y_x1, 'b-', linewidth=2)
ax3.set_xlabel('x1')
ax3.set_ylabel(f'f(x1, {x20})')
ax3.set_title(f'График f(x1) при x2 = {x20}')
ax3.grid(True)

ax4 = fig.add_subplot(224)
x10 = test_point[0]
y_x2 = f(x10, x2)
ax4.plot(x2, y_x2, 'r-', linewidth=2)
ax4.set_xlabel('x2')
ax4.set_ylabel(f'f({x10}, x2)')
ax4.set_title(f'График f(x2) при x1 = {x10}')
ax4.grid(True)

plt.tight_layout()
plt.subplots_adjust(top=0.9)

plt.savefig('function_plots_v2.png')
plt.show()
