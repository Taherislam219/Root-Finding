def f(x):
    return x**3 -x -2

a=1
b=2
n=5

if(f(a)*f(b)>=0):
    print("Invalid interVal :")
else:
    for i in range(n):
        c=(a+b)/2
        print("Iteration",i+1,"Root = ",round(c,6))

        if(f(a)*f(c)<0):
            b=c
        else:
            a=c

    print("Final Root : ",round(c,3))


def f(x):
    return x**3 - x - 2

a = 1
b = 2
tol = 0.000001

if f(a) * f(b) >= 0:
    print("Invalid interval")
else:
    while True:
        c = (a + b) / 2

        if abs(f(c)) < tol or abs(b - a) / 2 < tol:
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("Root =", round(c, 6))
