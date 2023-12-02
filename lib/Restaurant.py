class Restaurant:
    def __init__(self, restaurant_name):
        if type(restaurant_name) not in (str,):
            raise ValueError("Wrong Input")            
        self._name = restaurant_name

    def name(self): #getter
        return(self._name)
    
    def restaurant_name_setter(self, new_rest_name): #setter
        raise AttributeError("Name cannot be changed after initialization")
        pass    

    def reviews(self):
        pass

    def customers(self):
        # Returns a **unique** list of all customers who have reviewed a particular restaurant
        pass

    restaurant_name = property(name, restaurant_name_setter)
    
restaurant_0 = Restaurant("12345") # Restaurant case_0
# print(restaurant_0.name()) #calling the name() method

# restaurant_0.restaurant_name = "678910" #raises an Error on attempt to change the name 
