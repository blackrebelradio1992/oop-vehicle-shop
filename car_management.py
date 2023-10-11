from email.charset import add_charset


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
        self._services = []
        
        
        CarManager.total_cars += 1
        CarManager.all_cars.append(self)


    def __str__(self):
        return f"A {self._year} {self._make} {self._model} with {self._mileage} with these available services:\n {self._services}"

    # @property
    # def get_id(self):
    #     return self._id
    
    # @get_id.setter
    # def set_id(self, new_id):
    #     if 

    @property
    def get_make(self):
        return self._make
    
    @get_make.setter
    def set_make(self, new_make):
        if (type(new_make) == str and new_make != new_make.isspace() and len(new_make) > 2):  #new name must be at least 3 characters
            self._make = new_make
        else:
            print("Make must have at least 3 characters")
    
    @property
    def get_model(self):
        return self._model
    
    @get_model.setter
    def set_model(self, new_model):
        if (type(new_model) == str and new_model != new_model.isspace() and len(new_model) > 2):  #new name must be at least 3 characters
            self._model = new_model
        else:
            print("Model must have at least 3 characters")

    @property
    def get_year(self):
        return self._year
    
    @get_year.setter
    def set_year(self, new_year):
        if (type(new_year) == int and new_year > 1918 and new_year < 2024): #new age must be and intiger & must be greater than 11 and lower than 18
            self._year = new_year
        else:
            print("Invalid year")

    @property
    def get_mileage(self):
        return self._mileage
    
    @get_mileage.setter
    def set_mileage(self, new_mileage):
        if (type(new_mileage) == int and new_mileage >= 0 and new_mileage < 999999): #new age must be and intiger & must be greater than 11 and lower than 18
            self._year = new_mileage
        else:
            print("Invalid mileage")


    def add_service():
        pass



  
        

        

    def add_service():
        pass
        

    def app_main():
            def add_car():
                new_make = input("what is the make?\n ")
                new_model =input("what is the model?\n ")
                new_year = int(input(" what is the year?\n"))
                new_milege = int(input(""))

            def app_menue():
                print("----WELCOME----")
                print("1. Add a car")
                print("2. View all cars")
                print("3. View total number of cars")
                print("4. See a car's details")
                print("5. Service a car")
                print("6. Update mileage")
                print("7. Quit")

            while True:
                app_menue()
                action = int(input("whaT would you like to do?\n"))
                if (action == 1):
                    add_car()
                elif (app_menue() == 2):
                    return CarManager.all_cars
                elif (app_menue() == 3):
                    return CarManager.total_cars
                elif (app_menue() == 4):
                    pass
            

CarManager.app_main()