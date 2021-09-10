import math
import matplotlib.pyplot as plt


def f(x):
    return x + 1 / (x ** 2)


fig, ax = plt.subplots()
a = 1
b = 2
e = 0.02
n = math.ceil((b - a) / e)
t = (b - a) / n
x = a
minfun = f(a)
minx = 0
for i in range(1, n + 1):
    x += t
    if f(x) <= minfun:
        minfun = f(x)
        minx = x
    ax.scatter(x, f(x), s=15, c='Black')
ax.scatter(minx, minfun, s=15, c='Red')

x = a
i = 1
l = [x]
k = [f(x)]
while x < b:
    i += 0.001
    x *= i
    l.append(x)
    k.append(f(x))
ax.plot(l, k, c='Black')

print(round(minx, 3))
plt.show()
