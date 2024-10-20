"""
flow control
 when you want to incrementally execute or operate you
 can you flow control

 """
"""
i=0
i+=1
while i<10:
  print(i)
  #i=i+1

  
"""
"""
'while loop'
i=0
while i<10: #condition
 print(i)
 i+=1  #i=i+1

'for loop'
for i in range(10):   # list =[0,.....,9]
     
   print(i)   #prints from 0 until 9 
"""


#print("----------------------------")

#range built in function is to be supplied by three arguments
# 1. starting of the iteration
# 2. end of itration
# 4. step

'''
starting point = 2
ending point = 8
jump value/ increment value = 1
'''

"""
for i in range(2,8,1): # prints until 7. 8 doesnot print with
 print(i)

"""
"""
# N.B on straight goes the giving i and conditon then y get tab by print and decrement
i = 10
while i>1:
 i=i-1
 print(i)

"""

for i in range(10,2,-1):
 print(i)