#  WAP to replace all the multiple spaces into single space 

def spaces(msg):
    new_msg = " ".join(msg.split())
    return new_msg

if __name__ == "__main__":
    print(spaces("My    name    is   Aparna"))    