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


"""
3 ways 
sorting
append 
extend 
add
insert
count-->how much is the number
index
copy and = difference
max
min
sum--> adds all numbers on the list


"""
"""
empty_list=[]
print(empty_list)
empty_list.append(1)
empty_list.append(5)
print(empty_list)
empty_list.extend([20,11,14])
print(empty_list)
another_list=[8,9,11,0]
new_list=[14,6,10,12,[16,12,3]]
another_list.extend(new_list)
empty_list.extend(another_list)
print(empty_list)
print(another_list)
neu_list = empty_list+another_list
print(neu_list)

print("num_list.sort()")  -->print num_list.sort()
print({num_list.sort()})  --> print none
#sorted_list=num_list.sort()
#print(f"the sorted list is :{sorted_list}") --> gives none
#print(sort(num_list)) 

"""
"""
another_list=[8,9,11,0]

another_list.insert(2,100)--> shows where 100 add in 2. index
print(another_list)
#another_list.remove(100)--> shows which number removed must be
#print(another_list)
another_list.pop(2)--> shows where removed must be in 2. index
print(another_list)
"""

another_list=[1,8,9,11,0,3,1]
print(another_list.count(8))
print(another_list.count(1))
#print(another_list.index(11)) --> shows in which index is 11 number
new_list=another_list.copy()
print(new_list)
new_list=another_list
print(new_list)
max_value=max(new_list)
print(max_value)
print(min(new_list))
print(sum(new_list))
