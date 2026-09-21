def f(x):
    return -(x*x-4*x+6)

x=0

while f(x+.1)>f(x):
    x+=.1

print("Best x =",round(x,3))
print("Value =",round(f(x),3))
