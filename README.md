# FCC-follow-along

**1. Encapsulation**
- Mechanism of restricting the direct access to some of the attributes in our program
- Restricting the overwriting of values is what encapsulation is about, the attribute can't be changed from outside of class making it private. 
(@property, double underscore, @[property].setter)
- we create methods to modify the values rather than directly modifying them.

**2. Abstraction**
 - Hiding the unnecessary information/details from the instances, and only exposing the required details.
 - hiding sensetive tasks, private methods.
 - private methods is done by preceeding it with double underscore, they can't be accessed outside class. 
 - If a public method is called and it contains the private method,  it can be accessed.
 - doing complex tasks, without knowing it all.

**3. Inheritance**
- to avoid writing code everytime , we can inherit methods and attributes from the parent class.
- passing all the methods to a child class avoids code duplication.
- like Item class might have child class as Phone, Keyboard, Laptop, Camera etc.
- Vehicle might have child classes such as that of Scooter, Car etc.
- parent class = base class, child class = derived class

**4. Polymorphism**
- Many forms, ability to have different scenarios when the exact same entity is utilized(example a method)
- len(str) or len([array]) will give the length. is a good example of polymorphism.
- Single entity that can be used via multiple classes after inheriting, hence people often listen about inheritance and polymorphism together.
- if we provide different pay_rate(discount) to different classes that inherit from Item class, the apply_discount() method will work everywhere with different values pertaining to each class.