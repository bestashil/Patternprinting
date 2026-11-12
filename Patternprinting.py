#Q1 Square print-------------------->
num = int(input("Enter a number: "))
for i in range(1,num):
    for j in range(1,num):
        print("*",end=" ")
    print("") #By default new line in print()

#Q2 Triangle shape star print------------------>
num = int(input("Enter a number: "))
for i in range(1,num):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

#Q3 Reverse Star Pattern Print:
# *****
# ****
# ***
# **
# *

for i in range(5,0,-1): #Rows
    for j in range(1,i+1): #Cols
        print("*",end=" ")
    print()

#Q4 Q18. Number Pattern Print:---------->
# 1
# 12
# 123
# 1234
# 12345

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()

#Q5 Same Number Pattern print --------------->
# 1
# 22
# 333
# 4444
# 55555

for i in range(1,6):
    for j in range(1,i+1):
      print(i,end="")
    print()

#Q6 Q20. Pyramid Pattern Print:------------------------->
#    *
#   ***
#  *****
# *******
#*********

for i in range(1,6):#Rows
    for k in range(i,5): #Space
        print("",end=" ")
    for j in range(1,i+1):#Cols
        print("* ",end=" ")
    print()

#Q7 . Inverted Pyramid Print:--------------------------------->
# *********
# *******
# *****
# ***
# *

for i in range(1,6):          # Rows
    for k in range(1,i):      # Spaces
        print(" ",end=" ")
    for j in range(1,12-2*i): # Stars
        print("*",end=" ")
    print()

#Q8 Break in Pattern Print a star pattern.Stop printing when the row number reaches 4----------->

for i in range(1,6):
  if i==4 :
      break
  for j in range(1,i+1):
      print("* ",end="")
  print()







