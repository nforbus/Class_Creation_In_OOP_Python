
class Car:
    def __init__(self, make="unknown", model="unknown", color="unknown", _year=-1, _price=-1):
        self.make = make
        self.model = model
        self.color = color
        self._year = _year
        self._price = _price


    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price_to_add):
        if(price_to_add <= 0):
            raise ValueError("Price is zero or less.")
        print("Setter for price called, value is: " + str(price_to_add))
        self._price = price_to_add

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, year_to_add):
        if(year_to_add <= 1799):
            raise ValueError("Cars didn't exist back then.")
        print("Setter for year called, value is: " + self._year)
        self._year = year_to_add


car = Car()
print("Model = " + car.model)
car.price = 10000
print("price is: " + str(car.price))

car.year = 1750
print("year is: " + str(car.year))