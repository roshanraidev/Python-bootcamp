#Lists are ordered sequences that can hold a variety of object types , supports indexing and slicing
mylist = ['one','two','three']
print(mylist[0])
print(mylist[1:])

#concatenation

another_list = ['four','five','six']
new_list = mylist+another_list
print(new_list)

#mutation
mylist[0]= 'we gege'
print(mylist)

#append
mylist.append('seven')
print(mylist)

#pop
mylist.pop()
print(mylist)
popped_item= mylist.pop(2)
print(mylist, popped_item)

#sort
new_list=['a','b','d','r','f']
new_list.sort()
print(new_list)
rlist = new_list.sort()
print(rlist)  # shows result as none
print(type(rlist))  # type for a none object, its a common return value for function that does not return anything
print(type(new_list))

# reverse
num_list= [1,2,3,4]
num_list.reverse()
print(num_list)