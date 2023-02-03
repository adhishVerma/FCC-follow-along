import csv

class Item:
  pay_rate = 0.8  #using 20% discount
  all = []

  def __init__(self, name: str, price: int, quantity = 0) -> None:

    # Running validations check
    assert price >= 0
    assert quantity >= 0

    # Assign to self object
    self.__name = name #adding an underscores makes it private and unaccessible outside of class
    self.price = price
    self.quantity = quantity

    # Actions to execcute
    Item.all.append(self)

  @property
  #Property Decorator - Read-Only Attribute
  def name(self):
    return self.__name

  @name.setter
  def name(self, value):
    if len(value) > 10:
      raise Exception('The name is too long!')
    else:
      self.__name = value

  def calculate_total_price(self):
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
    return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
