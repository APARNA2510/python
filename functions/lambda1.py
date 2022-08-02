f = lambda x: x+3*5
g = lambda x,y: x**2+y**2
print(f(20))
print(f(30))
print(g(10,20))
print(g(f(2),f(3)))