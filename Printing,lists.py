print('This is a string {}'.format('Inserted'))
print('The {2}{1}{0}'.format('fox ', 'brown ', 'quick '))
print('The {0}{1}{0}'.format('fox ', 'brown ', 'quick '))
print('The {f}{b}{q}'.format(f='fox ', b='brown ', q='quick '))

result = 100 / 777
print('Result was {}'.format(result))
print('Result was {r:10.6f}'.format(r=result))
print(result)

name = "Jose"
print("my name is {}".format(name))
print(f"my name is {name}")

name = "Sam"
age = "3"
print(f"{name} is {age} years old")
my_list = [1, 2, 3]
my_list = ["string", 100, 20.1]
print(len(my_list))
mylist = ["one", "two", 'three']
print(mylist[2])
print(mylist[1:])
anotherlist = ['four', 'five']
print(mylist + anotherlist)
nextlist = mylist + anotherlist
nextlist [0] = "jeden",
nextlist.append('six')
print(nextlist)
nextlist.pop()
print(nextlist)
remove_item = nextlist.pop()
print(remove_item)
nextlist.pop(2)
print(nextlist)
list_letters = ['a','c','e','d','b']
list_numbers = [2,4,1,3,6,5]
list_letters.sort()
print(list_letters)
list_numbers.sort()
print(list_numbers)
print(type(list_letters))
print(type(list_numbers))
list_letters.reverse()
list_numbers.reverse()
print(list_letters)
print(list_numbers)

def arr(n):

    n = [0,n - 1]
    return n


arr(6)
print(arr(3))

#print(list(range(0, 10))