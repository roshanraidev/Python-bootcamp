#.format method
print("this is a string {}".format('Inserted'))
print("the {0} {0} {0}".format('fox','brown','quick'))
print("the {2} {1} {0}".format('fox','brown','quick')) # index for the format inputs can be created and called multiple times
print("the {q} {b} {f}".format(f='fox',b='brown',q='quick'))

#float formatting
print(100/77)
result = 100/77
print("the result was {q}".format(q=result))
print("the result was {q:1.3f}".format(q=result)) # float formatting follows "{value:width.precision f}"
print("the result was {q:10.5f}".format(q=result))# width is used to set the total number of characters to display

#formatted string literals
name ='Jose'
print(f"the name is {name}") #add a f at the start of the string and inject varaibles into the string itself

name='sam'
age =3
print(f'the name is {name} and age is {age}')

