import csv

class Item:
  pay_rate = 0.8  #using 20% discount
  all = []

  def __init__(self, name: str, price: int, quantity = 0) -> None:

    # Running validations check
    assert price >= 0
    assert quantity >= 0

    # Assign to self object
    self.name = name
    self.price = price
    self.quantity = quantity

    # Actions to execcute
    Item.all.append(self)

  def calculate_total_price(self):
    return self.price * self.quantity

  def apply_discount(self):
    self.price = self.price * self.pay_rate


# Phone is child class of Item
# Item is parent class of Phone

class Phone(Item): #Phone class inherits from the Item class 
  
  def __init__(self, name: str, price: int, quantity = 0, broken_phones = 0) -> None:
    #call to super function to have access to all attributes/methods
    super().__init__(
      name,price,quantity
    )

    # Running validations check
    assert broken_phones >= 0

    # Assign to self object
    self.broken_phones = broken_phones


phone1 = Phone('jsPhonev10',500,5,1)
print(phone1.calculate_total_price())
phone2 = Phone('jsPhonev20',600,5,1)

print(Item.all)
print(Phone.all)

# Problem:  we dont want duplication of code, hence there's another way to inherit init arguments from the parent class, in case if we want to add more args to the instance, we can't do that without redefining the init/constructor if we follow old approach.

#soln : for each child class we use a separated constructor,we used super function, in order to inherit all the attributes and methods from the parent class.
# we also get access to class attributes inside the child class when we use super().__init__