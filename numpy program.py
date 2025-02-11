# creating an array

"""arr = np.array([[10, 20, 30, 40], [38, 87, 36, 26]])
# [38, 87, 36, 26], [67, 95, 73, 64]
print(arr)
print(type(arr))
print(arr.dtype)"""

"""a = [[30, 40, 78], [40, 20, 10]]
arr = np.array(a)
print(arr)
print(arr.shape)
print(len(arr))
print(np.size(arr))"""

# sorting,filter and search
"""ar = np.array([[11, 34, 93, 72, 0], [3, 6, 5, 2, 90]])
print(np.sort(ar))

ar = np.array([1, 3, 5, 7])
s = np.where(ar == 3)
print(s)
ss = np.searchsorted(ar, 5)
print(ss)"""

"""ar = np.array([8, 4, 2, 5])
fa = ar % 2 == 1

new = ar[fa]
print(new)"""

"""ar = np.array([30, 87, 18, 34])
fa = [True, False, True, True]
new = ar[fa]

print(new)"""
