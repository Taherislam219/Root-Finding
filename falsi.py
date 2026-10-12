def f(x):
    return x**3-x-2

a=1
b=2
n=5



if(f(a)*f(b)>=0):
     print("Invalid Interval")
     
else: 
    for i in range(n):
          c=(a * f(b) - b * f(a)) / (f(b) - f(a))

          print("Iteration", i + 1, "Root =", round(c, 6))

          if(f(a)*f(c)<0):
               b=c

          else:
               a=c
    print("Final root =", round(c, 6))

    