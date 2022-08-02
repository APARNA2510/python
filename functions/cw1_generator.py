# wap to generate a list of even squares using generators

def even(limit):
    for i in range(limit+1):
        if i%2 == 0:
            sq = i**2
            yield sq

# ex call
for e in even(20):
    print(e, end = ' | ')             