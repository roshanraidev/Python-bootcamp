#Dictionaries are unordered mappings for storing objects , it uses a key value pair to grab objects without knowing the index
my_dict = {'key1':'value1', 'key2':'value2'}
print(my_dict)

# used to lookup prices at a store where the values are predefined.
prices_lookup = {'apple':2.99,'mango':1.99, 'milk': 4.99}
print(prices_lookup)

#dictionaries are very flexible with the data types that they support , they can support lists and even embedded dictionaries
d={'k1':123,'k2':[0,1,2],'k3': {'index': 'one'}}
print(d)
print(d['k1'])
print(d['k2'])
print(d['k3'])
print(d['k3']['index'])
print(d['k3']['index'].upper())   #Multiple steps are not required to perform this action since python is flexible.

# key value pairs can be easily added and overwritten
d['k4']= 567
d['k1']= 456
print(d)

#Certain functions can be used to list all the keys,values and items in a dictionary
print(d.keys())
print(d.values())
print(d.items())






