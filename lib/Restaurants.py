""""""
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
        pass

    def customers(self):
        # Returns a **unique** list of all customers who have reviewed a particular restaurant
        pass

    @classmethod
    def add_all_instances(cls, new_restaurant):
        cls.all_restaurants.append(new_restaurant)

    restaurant_name = property(name, restaurant_name_setter)

# uncomment to see magic :)
restaurant_0 = Restaurant("12345") # Restaurant case_0
# print(restaurant_0.name()) #calling the name() method to display the restaurant name

# restaurant_0.restaurant_name = "678910" #raises an Error on attempt to change the name
""""""
   
#Customer
""""""
class Customer:
    all_instances = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.fullName = first_name + " " + last_name
        Customer.all(self)
        
    def given_name(self):
        return(self.first_name)
    
    def family_name(self):
        return(self.last_name)
    
    def full_name(self):
        return(f"{self.first_name} {self.last_name}")
        pass

    def restaurants(self):
        # Returns a **unique** list of all restaurants a customer has reviewed
        pass

    def add_review(restaurant, rating):
        pass

    @classmethod
    def all(cls, new_customer_instance):
        # cls.all_instances.append(new_customer_instance.fullName)
        cls.all_instances.append(new_customer_instance)
        pass

    @classmethod
    def print_all_instances(cls):
        print([fullname.fullName for fullname in cls.all_instances])

# uncomment to see magic :)
customer1 = Customer("Gad", "Ongoro") # Customer case_0
customer2 = Customer("Muhammad", "Gaddafi") # Customer case_1
customer3 = Customer("Allahdu", "Jamil") # Customer case_2
#customer1.full_name() #returns the customer's full name
#Customer.print_all_instances() #prints a list of all customer names
""""""

#Review
""""""
class Review(Customer):
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.rest_customer = customer
        self.rest_restaurant = restaurant
        self._rating = rating
        Review.all(self)
        if type(rating) in (int,):
            self._rating = rating
        else:
            self._rating = None
            print("Rating should be an Integer")

    def rating(self):
        print(self._rating)
    
    def rating_setter(self, rating):
        if type(rating) in (int,):
            self._rating = rating
        else:
            print("Rating should be an Integer")

    rest_rating = property(rating, rating_setter)

    def customer(self):
        # returns the customer object for that review
        return(Customer.all_instances)
        pass

    def restaurant(self):
        return(Restaurant.all_restaurants)
        pass

    @classmethod
    def all(cls, new_review):
        cls.all_reviews.append(new_review)

    @classmethod
    def print_all_reviews(cls):
        print([review for review in cls.all_reviews])
        pass

# uncomment to see magic :)
my_restaurant_review_0 = Review("Gad", "Spicy", 7) #case_0
my_restaurant_review_1 = Review("Abdi", "Five_Star", 10) #case_1
my_restaurant_review_2 = Review("Allahdu", "Big_Square", 8) #case_2

#my_restaurant_review_2.rest_rating #calling rating() returns a rating of an instance
#my_restaurant_review_0.rating() #calling rating() returns a rating of an instance
#print(Review.all_reviews) #prints the object(s) location
#Review.print_all_reviews() #prints the object(s) location
# print(my_restaurant_review_0.customer()) # returns the customer object for a review and doesn't change the customer
# print(my_restaurant_review_0.restaurant()) # returns the restaurant object for that given review

""""""