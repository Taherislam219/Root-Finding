def f(x):
    return x ** 2 -4

x0 = 0
x1 = 1
tol = 0.000001

while(True) :
    denominator =f(x1) - f(x0)

    if denominator == 0 :
        print("Division By zero")
        break

    x2 =x1 - f(x1) * (x1 - x0) / denominator

    if abs(x2-x1)<tol :
        x1 =x2
        break

    x0 = x1
    x1 = x2

print("Root =", round(x1, 6))