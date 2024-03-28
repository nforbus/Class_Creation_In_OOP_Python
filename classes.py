
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
        print("Setter for year called, value is: " + str(self._year))
        self._year = year_to_add

    def __str__(self):
        return 'Car(make = ' + str(self.make) + ', model = ' + str(self.model) +\
            ', color = ' + str(self.color) + ', year = ' + str(self.year) +\
            ', price = ' + str(self.price) + ')'
    

file_handler = open("cars.csv", "r")
cars_data = file_handler.readlines()
cars_data.pop(0) #removes the first entry, which in this case is the column headers we don't want.

cars_list = []

for raw_string in cars_data:
    make, model, color, year, price = raw_string.split(',')
    cars_list.append(Car(make, model, color, int(year), float(price)))

cars_list.sort(key=lambda car: car.price)

print(*cars_list, sep="\n")