from Restaurant import Restaurant

class Customer:
    all_instances = []
    all_names = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.fullName = first_name + " " + last_name
        Customer.all(self)
        Customer.allNamesHandler(self)
        
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

    @classmethod
    def allNamesHandler(cls, new_customer):
        cls.all_names.append(new_customer.fullName)

    @classmethod
    def allNamesPrinter(cls):
        print([fullName for fullName in cls.all_names])


# uncomment to see magic 😄
customer1 = Customer("Gad", "Ongoro") # Customer case_0
customer2 = Customer("Muhammad", "Gaddafi") # Customer case_1
customer3 = Customer("Allahdu", "Jamil") # Customer case_2
customer4 = Customer("Allahdu", "Jamil") # Customer case_3
#customer1.full_name() #returns the customer's full name
#Customer.print_all_instances() #prints a list of all customer names