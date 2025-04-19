
data_file = open('D:\\Self learning\\nf.txt','r+')
print(data_file.read())
data_file.seek(0)
print(data_file.read())

with open('D:\\Self learning\\nf.txt', 'a') as data_file:  # new format
    data_file.write("vivek")

#modes 'r' - read only , 'w'- write only , 'a'- append only ,'r+'-reading and writing , 'w+'-   writing and reading (overwriting an exising file or creating a new file)

g = open('D:\\Self learning\\aa.txt', 'w+')

with open('D:\\Self learning\\aa.txt', 'w') as g:
    g.write('whats up friend.....')

with open('D:\\Self learning\\aa.txt', 'r') as g:
    contents =g.read()
    print(contents)

with open('D:\\Self learning\\aa.txt', 'a') as g:
    g.write('adding more data')

with open('D:\\Self learning\\aa.txt', 'r+') as g:
    newc = g.read()
    print(newc)












