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

  def __repr__(self) -> str: #magic method to represent the instance
    return f"Item('{self.name}', {self.price}, {self.quantity})"


item1 = Item('Phone', 100, 1)
item2 = Item("Laptop",1000,3)
item3 = Item("Cable",10,5)
item4 = Item("Mouse", 50 ,5)
item5 = Item("Keyboard", 75, 5)
item6 = Item("Monitor", 175)

# we have no way to get a list of all the instances made till this point, hence we created a class attribute with a list to contain all the instances of Item class

print(Item.all) #now with this we can access all the instances of the class 