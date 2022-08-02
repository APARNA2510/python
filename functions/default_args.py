# function can have default parameters if you want
# default parameters are added after required parameter

def add(a,b,c=0,d=0):
    return a+b+c+d





if __name__ == "__main__":
    out = add(20,20)
    print(odd)
    out = add(20,20,10)
    print(out)  
    out = add(20,20,10,20)
    print(out)  
    out = add(20,20,c=10)
    print(out)  
    out = add(20,20,d=10)
    print(out)  
    out = add(20,20,d=10,c=10)
    print(out)  
    out = add(20,d=20,c=10,b=20)
    