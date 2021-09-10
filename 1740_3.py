import math
import matplotlib.pyplot as plt


def f(x):
    return x + 1 / (x ** 2)

fig, ax = plt.subplots()
a = 1
b = 2
e = 0.02

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

c = round((a + ((3 - math.sqrt(5)) / 2) * (b - a)), 3)
d = round((a + ((math.sqrt(5) - 1) / 2) * (b - a)), 3)
ax.scatter(c, f(c), s=15, c='Black')
ax.scatter(d, f(d), s=15, c='Black')
func = round(f(c), 3)
fund = round(f(d), 3)
while (b - a) > 2 * e:
    if func <= fund:
        b = d
        d = c
        fund = func
        c = round((a + ((3 - math.sqrt(5)) / 2) * (b - a)), 3)
        func = round(f(c), 3)
        ax.scatter(c, func, s=15, c='Black')
    else:
        a = c
        c = d
        func = fund
        d = round((a + ((math.sqrt(5) - 1) / 2) * (b - a)), 3)
        fund = round(f(d), 3)
        ax.scatter(d, fund, s=15, c='Black')
ans = round(((a + b) / 2), 3)
print(ans)
ax.scatter(ans, f(ans), s=15, c='Red')
plt.show()