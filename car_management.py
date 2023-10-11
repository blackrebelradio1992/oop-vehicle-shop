class CarManager:
    # `all_cars` (class attribute): A list/dictionary that will store all the car instances created.
    all_cars = []
    # - `total_cars` (class attribute): An integer that will keep track of the total number of cars.
    total_cars = 0

    def __init__(self, id, make, model, year, mileage, services):
        # `_id` (instance attribute): An integer that should never be repeated and only rise with each car instance
        self._id = CarManager.total_cars
        # - `_make` (instance attribute): A string representing the make of the car.
        self._make = make
        # - `_model` (instance attribute): A string representing the model of the car.
        self._model = model 
        # - `_year` (instance attribute): An integer representing the manufacturing year of the car.
        self._year = year
        # - `_mileage` (instance attribute): An integer representing the vehicles total mileage
        self._mileage =  mileage
        #- `_services` (instance attribute): A list that will store the services done to the car.
        self._services = services
        
        
        CarManager.total_cars += 1
        CarManager.all_cars.append(self)


    def __str__(self):
        return f"A {self._year} {self._make} {self._model} with {self._mileage} with these available services:\n "

    @property
    def get_id(self):
        return self._id
    
    @get_id.setter
    def set_id(self, new_id):
        pass

    @property
    def get_make(self):
        return self._make
    
    @get_make.setter
    def set_make(self, new_make):
        pass



while true:
    print("----WELCOME----")
    print("\n1. Add a car\")
          print('n2. View all cars")
                print("\n3. View total number of cars")
                print("\n4. See a car's details")
                print("\n5. Service a car\n6. Update mileage\n7. Quit")

