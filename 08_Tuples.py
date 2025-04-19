#tuples are just like lists except that the values are immutable
t=(1,1,2,3)
print(type(t))

print(t[0])
print(t[-1])

# tuples support two functions index and count
print(t.index(1))
print(t.count(1))

# main use of tuple is the pass around objects in the program so that the values dont get accidentally changed
