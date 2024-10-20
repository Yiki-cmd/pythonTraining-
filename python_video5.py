"""
Console Application
# GUI Application

Python functions are callable objets that either supplied by arguments or not

1. built in
2. custom

"""
message="Hello World"
print(message)

"""
any string could be wrapped with the following


'string'
`string`  (bactic)
"string"
''' string '''
\"\"\" string  \"\"\"
``` string ```

"""
full_name = "Yikealo Asgodom Abraha"
print(f"{message},my full name is {full_name}")

"""
datatypes: 
   1. primitives
      1.str
      2.int
      3.bool
      4.float
   4. complex
      1. objects
      2. collections
           1.arrays
               1. lists
               2. sets 
               3. tuples 
           2. hashmaps
           # string keys that refer to values
               1. dictionary
           3.hash table since python 3.12
               1.sets


"""
'LIST'
   
# mutable
# duplication
# number indexed

# num_list=[1,2,5,8]
"""
print(num_list[5])  # --> get out of range

print(num_list{3})  # --> get nicht

"""

#num_list=[1,2,5,8]

"""
print(num_list[5])  --> out of range
print(num_list[1]) --> 2

print(num_list[-1])  -->8
"""

'''
sub_list = num_list[1:]  --> print start from 1st index
print(sub_list)
new_list=num_list[:3]   --> prints start from 0 until 2. index (3rd doesnot print)
print(new_list)


sub_list=num_list[1:3] --> prints from 0. index until 2. index which is 2&5
print(sub_list)
'''

'TUPLE'

# immutable
# duplication
# number indexed
"""
num_tuples = (1,2,5,6,7)
my_num=num_tuples[1]
print(my_num)
print(num_tuples[3])
print(num_tuples[:3])
print(num_tuples[1:])
print(num_tuples[2:3])

# everything that works by list works auch by tuples

"""
'SET'
# mutable
# duplication not allowed
#number indexed
"""
num_set = {1,4,5,9}

num_list=list(num_set)
print(num_list)
print(num_list[3])
print(num_set)
#print(num_set[2]) --> this one doesnot go

"""