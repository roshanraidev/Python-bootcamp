#sets are unordered collection of unique elements , only one of the same element can exist
myset = set()
print(myset)

#To add a item in set use add method
myset.add(1)
print(myset)
myset.add(2)
print(myset)

#Adding the same element multiple times does not make a difference since multiple copies of an element are not allowed.
myset.add(2)
print(myset)

#Even through the list contains multiple elements of the same type , after conversion to a set , the duplicate elements are removed.
mylist=[1,1,1,1,1,2,2,2,2,2,3,3,3,3,3]
print(set(mylist))

#sets dont have any particular order to them
