import matplotlib.pyplot as plt


def f(x):
    return x + 1 / (x ** 2)


fig, ax = plt.subplots()
a = 1
b = 2
e = 0.02
la = 0.005

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

while (b - a) > 2 * e:
    c = round(((a + b) / 2 - la / 2), 3)
    d = round(((a + b) / 2 + la / 2), 3)
    ax.scatter(c, f(c), s=15, c='Black')
    ax.scatter(d, f(d), s=15, c='Black')
    if f(c) <= f(d):
        b = d
    else:
        a = c
ans = round(((a + b) / 2), 3)
print(ans)
ax.scatter(ans, f(ans), s=15, c='Red')
plt.show()
