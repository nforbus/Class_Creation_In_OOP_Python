
class Car:
    def __init__(self, make="unknown", model="unknown", color="unknown", year=-1, price=-1):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.price = price

car = Car("buick","lesabre","red",2013,10000)        
print("Model = " + car.model)