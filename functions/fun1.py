# def function_name():
#     code...

def perimeter(l, b):
    p = 2*(l+b)
    return p

if __name__ == "__main__":
    # use/ call the function
    out = perimeter(10, 20)
    print("perimeter :",out)

    print("perimeter =>",perimeter(20, 20))