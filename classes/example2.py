class Fruit:
    def __init__(self, name, size, color):
        self.name =  name
        self.size = size
        self.color = color

    def __str__(self):
        return f"{self.name} is {self.color}"

# Inheritance
# every property and function is directly accessible from the class

class Mango(Fruit):
    def __init__(self, name, size, color, variety):
        super().__init__(name, color, size)
        self.variety = variety     

if __name__ == "__main__":
    f = Fruit('🍉', 'Green', 'Large')
    print(f)
    m = Mango('🥭', 'Yellow', 'Small', 'Safeda') 
    print(m)
    m2 = Mango('🥭', 'Green', 'Large', 'Langda') 
    print(m2)             