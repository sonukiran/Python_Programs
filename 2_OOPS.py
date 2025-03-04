#OOPS concept
from abc import ABC, abstractmethod
#Inheritance
class Car:
    def __init__(self):
        self.a = 10
        self.b = 20
    
class Volvo(Car):
    def __init__(self):
        self.y = 10
        super().__init__()

p = Volvo()
print(p.a) #10

#polimorphism
#same name different form
class Car:
    def __init__(self):
        self.a = 10
        self.b = 20
    def model(self):
        return "Basic Car"
    
class Volvo(Car):
    def __init__(self):
        self.y = 10
        super().__init__()
    
    def model(self):
        return "Volvo car"

q = Volvo()
r = Car()
print(f"when called with volvo object: {q.model()}, when called with Car object: {r.model()}")

#Encapsulation
#restriciting direct access to the varibale
class Car:
    
    def __init__(self):
        self.__a__ = 10
        self.b = 20
    def model(self):
        self.__price = 100
        return "Basic Car"
    
class Volvo(Car):
    def __init__(self):
        self.y = 10
        super().__init__()
    
    def model(self):
        return "Volvo car"
x = Car()
# print(x.__price)
print(x.model())

#Abstraction
class Car(ABC):
    
    def __init__(self):
        self.__a__ = 10
        self.b = 20
    @abstractmethod
    def model(self):
        self.__price = 100
        return "Basic Car"
    def absclass(self):
        pass
    
class Volvo(Car):
    def __init__(self):
        self.y = 10
        super().__init__()
    def model(self):
        return "Volvo car"
    def absclass(self):
        return "volvo"
x = Volvo()
# print(x.__price)
print(x.absclass())