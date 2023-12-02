from Restaurants import Review
from Restaurants import Customer

class Restaurant:
    all_restaurants = []
    def __init__(self, restaurant_name):
        if type(restaurant_name) not in (str,):
            raise ValueError("Wrong Input")            
        self._name = restaurant_name
        Restaurant.add_all_instances(self)

    def name(self): #getter
        return(self._name)
    
    def restaurant_name_setter(self, new_rest_name): #setter
        raise AttributeError("Name cannot be changed after initialization")
        pass    

    def reviews(self):
        return(Review.all_reviews)
        pass

    def customers(self):
        # Returns a **unique** list of all customers who have reviewed a particular restaurant
        count = len(Customer.all_instances)
        # sorted_customers = Customer.all_instances.sort()     
        # while count >= 0:                   
        #     pass
        print(Customer.all_instances)
        pass

    @classmethod
    def add_all_instances(cls, new_restaurant):
        cls.all_restaurants.append(new_restaurant)

    restaurant_name = property(name, restaurant_name_setter)

# uncomment to see magic :)
restaurant_0 = Restaurant("Spicy") # Restaurant case_0
restaurant_1 = Restaurant("Five_Star") # Restaurant case_1
restaurant_2 = Restaurant("Big_Square") # Restaurant case_1
# print(restaurant_0.name()) #calling the name() method to display the restaurant name
# restaurant_0.restaurant_name = "678910" #raises an Error on attempt to change the name
#print(restaurant_0.reviews()) #returns a list of all reviews for that restaurant
# restaurant_2.customers()