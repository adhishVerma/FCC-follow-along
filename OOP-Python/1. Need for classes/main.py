item1 = 'Phone'
item1_price = 100
item1_quantity = 5
item1_price_total = item1_price*item1_quantity

print(type(item1))
print(type(item1_price))
print(type(item1_quantity))
print(type(item1_price_total))

# each datatype is an object that's instantiated earlier by some class
# we have given different properties for item1, it's name, qty, price etc. but python just considers them as 4 different variables and has no idea that they are related.
# for reusing in future w would have to define variables each time, for example like item2 will have 4 more variables and it will go on like that.
# for our convenience we would like to use them in an instance so that we dont need to define so many variables.
# the instance can take in different attributes like num, price, qty