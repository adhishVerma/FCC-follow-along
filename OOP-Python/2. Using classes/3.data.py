#we have to store the data, and it's tedious to store them in this file. we could use a database or a csv file for this tutorial

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

  def calculate_total_prie(self):
    return self.price * self.quantity

  def apply_discount(self):
    self.price = self.price * self.pay_rate

  @classmethod
  def  instantiate_from_csv(cls):   #cls is passed as the first argument

    #this cant be used with an instance because it's to make instances
    #hence we used a decorator to make it a class method
    with open('tut/2. Using classes/items.csv', 'r') as f:
      reader = csv.DictReader(f)
      items = list(reader)
    for item in items:
      Item(
        name = item.get('name'),
        price = float(item.get('price')),
        quantity = int(item.get('quantity')),
      )
  
  @staticmethod
  def is_integer(num): 
    #they don't pass in the class or instance as the first argument a simple argument can be passed
    if isinstance(num, float):
      return num.is_integer()
    elif isinstance(num, int):
      return True
    else:
      return False

  def __repr__(self) -> str: #magic method to represent the instance
    return f"Item('{self.name}', {self.price}, {self.quantity})"

 
# Item.instantiate_from_csv()
# print(Item.all)

#using the static method
# print(Item.is_integer(12.9))

