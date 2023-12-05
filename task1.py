import numpy as np

b = 0.371
a = 1.21
z = np.tan((a + b) ** 2) - (a + 1.5) ** (1/3) + a * b ** 5 - b / (np.log(a ** 2))
print(z)

a = np.ones((12, 1))
b = np.random.randint(17, 29, (12, 1))
c = np.random.randint(60, 82, (12, 1))
temp = np.hstack((a, b))
X = np.hstack((temp, c))
print("X:", X)
Y = np.array([
        13.5,
        13.7,
        13.9,
        14.1,
        14.5,
        15.2,
        15.6,
        16.3,
        17.4,
        17.7,
        18.1,
        18.6])
print("Y:", Y)
X_t = X.T
X_t_X = X_t.dot(X)
X_t_X_inv = np.linalg.inv(X_t_X)
X_t_Y = X_t.dot(Y)
A = X_t_X_inv.dot(X_t_Y)
print("Вектор оценок А:", A)
Y_A = X.dot(A)
print("Проверка вектора А:", Y_A)
