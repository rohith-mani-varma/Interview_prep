class Car:
    total_cars = 0

    def __init__ (self,brand, model):
        self.__brand = brand
        self.model = model
        Car.total_cars += 1
    def print_info(self):
        print(self.__brand,self.model)
    def get_brand(self):
        return self.__brand
    def fuel_type(self):
        return "Petrol or Diesel"



class Elec_car(Car):
    def __init__(self,brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Battery"



my_car = Car("toyota", "corolla")
print(my_car.model)
my_car.print_info()
my_new_car = Car("Tata","Safari")

print(my_car.get_brand())


my_tesla = Elec_car("tesla", "model s", "85Kwh")
# print(my_tesla.print_info())
print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,Elec_car))
