# creating an object or ccreating an instance mean the same thing and are used interchangeably..
class Item:
  pay_rate = 0.8 # class attribute, after 20% discount
  def __init__(self,name: str,price: int ,quantity = 0) -> None: #magic methods
    #Run validations to the received arguments
    assert price >= 0, f"Price {price} is not greater than or equal to zero" #to check that the values are valid
    assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

    #Assign to self object
    self.name = name
    self.price = price
    self.quantity = quantity
     
  def calculate_total_price(self):
    return self.price * self.quantity 

  def apply_discount(self):
    self.price = self.price * self.pay_rate  # we cannot directly use the class attribute

# creating instances of this class
item1 = Item("Phone",100,5)
item2 = Item("Laptop",1000,3)

# item2.has_numpad = False  #not every item will have a numpad or some other property, this is where we can add additional properties to them

# print(type(item1)) #__main__.Item
# print(type(item1.name)) #str
# print(type(item1.price))  #int
# print(type(item1.quantity))  #int
# print(item1.calculate_total_price()) #calling method 
# print(item2.calculate_total_price()) #calling method 

# isolated definitions are called functions while thse inside classes are called methods
# in every method defined inside a class, python always passes the instance or self as the first argument, it's called self by convention and could be named something else
# every method must recieve atleast one parameter, if you don't recieve self then it'll throw an error

# this is tough to maintain, every instance has to be given parameters manually, it could've been better if these were done when while creating the instance

# whenever instance is created, the init method is executed automatically
# it's important to pass the correct data types

# attribute values that are to be shared among all the instances of that class are called class attributes
# attributes in reference to a particular object or instance are called instance attributes

# print(Item.pay_rate) #can be acceseed via class
# print(item1.pay_rate) # can be accessed via instance also, because it looks outside of instance also and brings it back from class level

# print(Item.__dict__) #magic attribute, gives all the attributes at class level
# print(item1.__dict__) #magic attribute, gives all the attributes at instance level

item1.apply_discount()
print(item1.price)

item2.pay_rate = 0.7 # 30% discount on the laptop

item2.apply_discount()
print(item2.price)


# it's always better to access class attributes from instance level because we can over write them again at instance level in case an instance requires them to be different