import math

def g(x) :
    return math.exp(-x) + 1

x = 0
n = 5

for i in range(n) :
    x_new = g(x)
    print("Iteration",i+1,"x = ",round(x_new,6))

    x = x_new

print("Final root = ",round(x,6))


import math

def g(x):
    return math.exp(-x)

x = 0
tol = 0.000001
max_iter = 100

for i in range(max_iter):
    x_new = g(x)

    if abs(x_new - x) < tol:
        x = x_new
        break

    x = x_new

print("Root =", round(x, 6))
print("Iterations =", i + 1)
