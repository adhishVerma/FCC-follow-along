from item import Item

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
