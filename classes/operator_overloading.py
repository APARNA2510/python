class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

# raw reprentation of object for list
    def __repr__(self):
        return self.__str__()    

# special function to overloading > symbol when used for object
    def __gt__(self, other):
        return self.age > other.age    

if __name__ == "__main__":

    p = Person('Raju', 39)
    p2 = Person('Suneel', 45)
    p3 = Person('Vijay', 30)  

    if p > p3:
        print(f'{p.name} is elder') 

person_list = [p, p2, p3]
person_list.sort()
print(person_list)        