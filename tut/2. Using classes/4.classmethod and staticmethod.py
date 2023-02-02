# When to use class and when to use static methods

class Item:
  @staticmethod
  def is_integer():
    '''
    This should do something that has a realtionship with class, but not something that's unique per instance

    we can put this outside of the class too but it's better to put it inside class if it's related to that class
    '''

  @classmethod
  def instantiate_from_something(cls):
    '''
    This should also do something that has a relationship with the class, but usually these are used to manipulate different structures of data ,to instantiate objects, like we have done with csv
    '''