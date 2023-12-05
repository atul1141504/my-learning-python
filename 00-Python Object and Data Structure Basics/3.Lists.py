# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#
#    1. Lists
#        Lists can be thought of the most general version of a sequence in Python. 
#        Unlike strings, they are mutable, meaning the elements inside a list can be changed!
#        
#        Facts:
#            -> Lists are constructed with brackets [] and commas separating every element in the list.
#            -> Lists can actually hold different object types
#            -> Just like strings, the len() function will tell you how many items are in the sequence of the list.
#
#        a.) Creating lists
#        b.) Indexing and Slicing Lists
#            Facts:
#            -> We can also use + to concatenate lists, just like strings.
#               Note: This doesn't actually change the original list!
#               We must reassign the list to make the change permanent.
#            -> We can also use the * for a duplication method similar to strings:
#               Again doubling not permanent
#        c.) Basic List Methods
#            -> Append - Use the append method to permanently add an item to the end of a list:
#            -> Pop - Use pop to "pop off" an item from the list. By default pop takes off the last index, 
#                     but you can also specify which index to pop off, remember default popped index is -1
#            -> Sort & Reverse - We can use the sort method and the reverse methods to also effect your lists.
#                ** reverse order is permanent.
#        d.) Nesting Lists
#            -> This means we can have data structures within data structures. 
#               For example: A list inside a list.
#            -> It allows Multi Level Indexing
#        e.) Introduction to List Comprehensions
#            -> Python has an advanced feature called list comprehensions. 
#               They allow for quick construction of lists. 
#               To fully understand list comprehensions we need to understand for loops.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# 1. Lists
print("\n1. Lists")
_my_list1 = [1,2,12.52136, 'Hello']
_my_list2 = [3,4,'The Added String']
print(_my_list1)
print(len(_my_list1))

print(_my_list1[0])
print(_my_list1[2:])
print(_my_list1[:3])

_my_list1 = _my_list1 + _my_list2
print(_my_list1)
print(len(_my_list1))

print(_my_list2*3)
print(_my_list2)

# Use the append method to permanently add an item to the end of a list:
_my_list2.append('The Appended String')
#print(_my_list2.append('The Appended String'))
print(_my_list2)

# Use pop to "pop off" an item from the list. By default pop takes off the last index, 
# but you can also specify which index to pop off.
_my_list2.pop(2)
print(_my_list2)

# Use reverse to reverse order (this is permanent!)
_my_list1.reverse()
print(_my_list1)

_my_list_sort_number = [128, 12, 88, 15]
_my_list_sort_string = ['d','a','c','b']
_my_list_sort_number.sort()
_my_list_sort_string.sort()
print(_my_list_sort_number)
print(_my_list_sort_string)

# Nesting Lists
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]
matrix = [lst_1,lst_2,lst_3]
print(matrix)
print(matrix[0])
print(matrix[0][2])
print(matrix[1])
print(matrix[1][0])

# List Comprehensions
# Build a list comprehension by deconstructing a for loop within a []
first_col = [row[0] for row in matrix]
print(first_col)