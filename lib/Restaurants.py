class Restaurant:
    def __init__(self, name):
        if type(name) not in (str,):
            raise ValueError("Wrong Input")            
        self.name = name

    def name(self):
        return(self.name)
    
restaurant_0 = Restaurant("123") # Restaurant case_0
#print(restaurant_0.name)
    
class Customer(Restaurant):
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

    @classmethod
    def all(cls, new_customer_instance):
        cls.all_instances.append(new_customer_instance)
        pass
    @classmethod
    def print_all_customer_instances(cls):
        print([customer.fullName for customer in cls.all_instances])
        pass

customer1 = Customer("Gad", "Ongoro") # Customer case_0
#customer1.print_all_customer_instances()

class Review(Customer):
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
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

    @classmethod
    def all(cls, new_review):
        cls.all_reviews.append(new_review)

    @classmethod
    def print_all_reviews(cls):
        print([review for review in cls.all_reviews])
        pass
my_restaurant_review_0 = Review("Gad", "Nairobi", 7) #case_0
my_restaurant_review_2 = Review("Ongoro", "Kenya", 8) #case_1
#my_restaurant_review.rest_rating
#my_restaurant_review.rating()
#print(Review.all_reviews) #prints the object(s) location
#Review.print_all_reviews() #prints the object(s) location