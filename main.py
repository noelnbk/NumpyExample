import numpy as np

a = np.array([1, 2, 3])
print(a)

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

c = np.array([[[2, 3, 4], [5, 6, 7], [8, 9, 0]], [[2, 3, 4], [5, 6, 7], [8, 9, 0]]], dtype='int32')
print(c)

print(a.ndim)
print(b.ndim)
print(c.ndim)

print(a.shape)
print(b.shape)
print(c.shape)

print(c[0, 1, :])

v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])

v3 = np.vstack([v1, v2])
print(v3)