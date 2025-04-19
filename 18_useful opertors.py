# range function is a generator which is used to generate data where there is none
# range(initial value, final value, step size)
# instead of declaring a variable and assigning values , this can be used to simplify the work
for n in range(4,10,2):
    print(n)


print(list(range(1,10,2)))  # range itself cannot be displayed , it must be cast into a list to generate values





