from Customer import Customer
from Restaurant import Restaurant

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
        return(Restaurant.all)
        pass

    @classmethod
    def all(cls, new_review):
        cls.all_reviews.append(new_review)

    @classmethod
    def print_all_reviews(cls):
        print([review for review in cls.all_reviews])
        pass

# uncomment to see magic :)
my_restaurant_review_0 = Review("Gad", "Nairobi", 7) #case_0
my_restaurant_review_2 = Review("Ongoro", "Kenya", 8) #case_1

#my_restaurant_review_2.rest_rating #calling rating() returns a rating of an instance
#my_restaurant_review_0.rating() #calling rating() returns a rating of an instance
#print(Review.all_reviews) #prints the object(s) location
#Review.print_all_reviews() #prints the object(s) location
# print(my_restaurant_review_0.customer()) # returns the customer object for a review and doesn't change the customer
print(my_restaurant_review_0.restaurant()) # returns the restaurant object for that given review