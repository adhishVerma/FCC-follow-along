from item import Item

item1 = Item("MyItem",750)
# item1.name = "OtherItem"


#in case if we want some argument to be only instantiated once, and not be modified ever then we can use setter and getter

print(item1.name) #we dont need an under-score here

# we cannot set the attribute without a setter if we use the double underscore before the property name

# we can put restrictions using setters
# we can disallow someone to change the property value directly if we want to do that, by making a setter function it can be achieved
