import numpy as np

X = np.array([[2, 3], [4, 5]])
Y = np.array([[1, 2], [3, 4]])
add_result = X + Y
print("addition of x and y:\n",add_result)
dot_product = np.dot(X,Y)
print("dot product of x and y:\n",dot_product)
transpose = X.T
print("transpose of X:\n",transpose)
determinant = np.linalg.det(transpose)
print("determinant of Y:\n",determinant)
