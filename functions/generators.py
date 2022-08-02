def cube(limit):
    for i in range(1, limit+1):
        yield i**3

def fib(limit):
    a, b = 0, 1
    for i in range(limit):
        yield a
        a, b = b, a+b

def even(limit):
    for i in range(limit):
        if i%2 == 0:
            yield i

# ex call
for c in cube(10):
    print(c) 

for f in fib(15):
    print(f, end = ' | ')

for e in even(10):
    print(e, end = ' | ')              


# generators are special function in python
# that can be used to generate a sequence of values
# instead of returning the value from a function once
# we put the value into a memory space using the yield 
# and then we can  use the next() function to get the next value
# generators are fast compared to lists    


# wap to generate a list of even squares using generators
# wap to generate a list of acronyms from a list of words using generators and *args

          