
def f(x):
    return x**2 - 4

def df(x):
    return 2*x

x = 3
n = 5

for i in range(n):
    if df(x) == 0:
        print("Derivative is zero")
        break

    x_new = x - f(x) / df(x)
    print("Iteration", i + 1, "=", round(x_new, 6))
    x = x_new

print("Root =", round(x, 6))
 


'''def f(x):
    return x**2 - 4

def df(x):
    return 2*x

x = 2.00
ite = 0
tol = 0.000001

while True:
    if df(x) == 0:
        print("Derivative is zero!")
        break

    x_new = x - f(x) / df(x)
    ite += 1

    if abs(x_new - x) < tol:
        x = x_new
        break

    x = x_new

print("Root =", round(x, 6))
print("Iterations =", ite)'''
