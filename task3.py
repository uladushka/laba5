import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

a_st = 3.5
a_end = 25.5
delta_a = 1.5
x = 1.21

a = np.arange(a_st, a_end + delta_a, delta_a)
l = []

for a_val in a:
    l_func = np.arcsin(x/3) + 1.2*a_val
    l.append(l_func)

for a_val, l_func in zip(a, l):
    print(f"a = {a_val:.2f}, l = {l_func:.2f}")

max_l = max(l)
min_l = min(l)
mean_l = np.mean(l)

print("Максимальное значение:", max_l)
print("Минимальное значение: ", min_l)
print("Среднее значение:", mean_l)

l.sort(reverse=True)

plt.figure(figsize=(10, 6))
plt.plot(a, l, label="f(l)", ls='-')
plt.axhline(mean_l, color='orange', ls='-.', lw='2', label="Среднее значение")
plt.title("График функции f(l)")
plt.xlabel("Переменная a")
plt.ylabel("Функция f(l)")
plt.legend()
plt.show()



fig = plt.figure(figsize=(15, 7))

x = np.linspace(0, 4, 100)
y = np.linspace(0, 4, 100)
X, Y = np.meshgrid(x, y)
Z = X**0.25 + Y**0.25
ax1 = fig.add_subplot(231, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='plasma')
ax1.set_title("z = x^0.25+y^0.25")
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 - Y**2
ax2 = fig.add_subplot(232, projection='3d')
ax2.plot_surface(X, Y, Z, cmap='magma')
ax2.set_title('z = x^2 - y^2')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')

x = np.linspace(0, 4, 100)
y = np.linspace(0, 4, 100)
X, Y = np.meshgrid(x, y)
Z = 2*X + 3*Y
ax3 = fig.add_subplot(233, projection='3d')
ax3.plot_surface(X, Y, Z, cmap='inferno')
ax3.set_title('z = 2x + 3y')
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z')

x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2
ax4 = fig.add_subplot(234, projection='3d')
ax4.plot_surface(X, Y, Z, cmap='viridis')
ax4.set_title('z = x^2 + y^2')
ax4.set_xlabel('X')
ax4.set_ylabel('Y')
ax4.set_zlabel('Z')

x = np.linspace(0, 4, 100)
y = np.linspace(0, 4, 100)
X, Y = np.meshgrid(x, y)
Z = 2 + 2*X + 2*Y - X**2 - Y**2
ax5 = fig.add_subplot(236, projection='3d')
ax5.plot_surface(X, Y, Z, cmap='cividis')
ax5.set_title('z = 2 + 2x + 2y - x^2 - y^2')
ax5.set_xlabel('X')
ax5.set_ylabel('Y')
ax5.set_zlabel('Z')
plt.tight_layout()
plt.show()