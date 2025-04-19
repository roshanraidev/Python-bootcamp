mylist = [1,2,3,4,5,6,7,8,9,10]
a=10

for num in mylist:
    print(num)

print("\n")
print("\n")
print("\n")
print("\n")



for n in mylist:
    if n%2 == 0: # check if the remainder of n/2 is zero , that makes it even
        print(n)
    else:
        print(f'odd number: {n}')
print("\n")
print("\n")
print("\n")
print("\n")

list_sum =0

for nn in mylist:
    list_sum = list_sum + nn
    print(list_sum)
print("\n")
print("\n")
print("\n")
print("\n")

for letter in "hello world":
    print(letter)

print("\n")
print("\n")
print("\n")
print("\n")


for _ in "we are the world": # _ is used in advanced code when no variable data needs to be printed, used to display repetitive data
    print("cool")
print("\n")
print("\n")

# tuples and for loops

tup =(1,2,3)

for item in tup:
    print(item)

new_tup= [(1,2),(3,4),(5,6)]

for item in new_tup:
    print(item)

# this is called as tuple unpacking where the list items(tuples) are unpacked

for (a,b) in new_tup: # (a,b) is used to unpack the tuple pairs since they have the same syntax
    print(a)          # parenthesis is not required we can use a,b too
    print(b)

#iterating through dictionaries

d = {'k1':1 ,'k2':2, "k3":3}

for item in d: # this only prints the keys
    print(item)

for item in d.items(): # this prints the entire key - value pair
    print(item)

for key,value in d.items(): # similar to tuple unpacking the dictionary can be unpacked too by adjusting the variable format
    print(key)              # so that keys and values can be seperated
    print(value)            # to get values of keys , use d.keys() | to get value of values , use d.values







