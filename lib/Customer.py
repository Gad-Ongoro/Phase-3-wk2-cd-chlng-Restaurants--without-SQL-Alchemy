from Restaurant import Restaurant

class Customer:
    all_instances = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
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
        cls.all_instances.append(new_customer_instance)
        pass

customer1 = Customer("Gad", "Ongoro")
#customer1.full_name()
print(Customer.all_instances[0].full_name())