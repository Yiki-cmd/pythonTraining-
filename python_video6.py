"SET"
# mutable
# duplication not allowed
#number indexed

"""

num_set = {1,4,2,5,3,6}
print(num_set)

num_list=list(num_set)
# it must be changed to list to work
#N.B it sorts also automatically

print(num_list[3])

print(num_list[2])

print(num_list[-2])

print(num_list[1:])

print(num_list[:4])

print(num_list[1:4])

"""
num_list=[1,3,2,7,5,4]
another_list=[8,9,11,0]
new_list=[14,6,10,12,[16,12,3]]
size=len(num_list)
print(f"size of the list is:{size}")
#print(num_list.sort())
num_list.sort()
print(f"the sorted list is :{num_list}")
print(f"the ascending sorted list is{num_list}")
num_list.sort(reverse=True)
print(f"the descending sorted list is{num_list}")
num_list.append(10)
print(num_list)
print(f"after new element is added to the list:{num_list}")
num_list.append(another_list)
print(num_list)
new_list.append(another_list)
print(new_list)
new_list.sort()
# print(new_list) --> it can not be sorted coz different data types


"""
print("num_list.sort()")  -->print num_list.sort()
print({num_list.sort()})  --> print none
#sorted_list=num_list.sort()
#print(f"the sorted list is :{sorted_list}") --> gives none
#print(sort(num_list)) 
"""