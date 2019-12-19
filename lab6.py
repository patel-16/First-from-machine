#ex1
'''def function1():
 print("MY FIRST FUNCTION")

function1()'''

#ex2
'''def function2(Fname):
 print(Fname)
 
function2("abcd")
'''

#ex2'

'''def function3(Fname):
 print("Welcome " + Fname)

function3("ABC")
function3("cB")
function3("AcfC")
'''

#ex3(to show that without arguement function takes default value(but found that it does not until the default value is specified ))

'''def function4(COUNTRY):
 print("Welcome to " + COUNTRY )

function4("Canada")
function4("USA") 
function4("Mexico")
function4() 
'''
#ex3'(default arguement specified)

'''def function5(COUNTRY = "India" ):
 print("Welcome to " + COUNTRY)

function5("Malaysia")
function5("Singapore")
function5("China")
function5()
'''
#ex4

'''def function6(x):
 x[1] = "DBAKBJ"

list_1 = [2,3,1,5,8]

function6(list_1)
print(list_1)
'''

#ex4'

'''def function7(food):
 for x in food:
  print(x)

bakery = ["Bread","Toast","Cookies"]

function7(bakery)
'''

#ex5
'''
def function8(x):
 return 5*x

print(function8(5))
print(function8(1))
print(function8(4))
''' 
 
#ex6
'''
def function9(child1,child2,child3):
 print("Hello " + child1)
 print("Hello " + child2)
 print("Hello " + child3)

function9(child2="Doyal",child1="Doyle",child3="Goyal")
'''
#ex7(if number of arguements is unknown)

'''def function10(*x):
 print(x[4])

function10(1,2,3,4,5,6,7,8,9) 
'''
#ex7'(if number of arguements is unknown)
'''def function10(*x):
 print(x + 5)

function10(1,2,3,4,5,6,7,8,9) #in braces is a tupple and tupple can't be mutated so error!
'''

#ex8(using recursion i.e the function calls itself)

"""FINDING FACTORIAL USING RECURSION"""
'''
def function11(number):
 if number==1: 
#BASE CONDITION:Every recursive function must have a base condition that stops the
#recursion or else the
#function calls itself infinitely(HERE if number==1 is the base condition)
  return 1
 else:
  return number*function11(number - 1)

i = int(input("Enter a number whose factorial needs to be found "))

print(function11(i))
'''

#Q1(not in order)
'''def power(x,y):
 if y==0:
  return 1
 else:
  return x*power(x,y-1)
 
print(power(2,4))
'''
#Q2
'''def absolute(x):
 if x>0:
  return x
 elif x<0:
  return -x
 else:
  return 0

print(absolute(0))
print(absolute(-3))
print(absolute(6))
'''
'''
#Q3
def printprime():

 for x in range(2,101):
  a=0
  for k in range(2,x):
    if x%k == 0:
      a=1  
  if a==0:
      print(x)
      
printprime() 
'''    

#Q4(FIBONACCI USING RECURSION)
# 0,1,1,2,3,5,8,13,21
'''def fibonacci(i):

  if i ==2:
   return 0
  
  elif i ==3:
   return 1
  else:
   return fibonacci(i-1) + fibonacci(i-2)
k = int(input("ENTER NO OF TERMS"))   
for i in range(0,k):
 print(fibonacci(i+2))     
'''   
   
#Q5(SWAPPING TWO REAL NO)  
'''def swap(x,y):
 tmp = x
 x = y
 y = tmp
 print(str(x)+","+str(y))
 
swap(5,3)  
'''   

#Q6(ASCII)(NOTE: ORD FUNCTION IS USED TO FIND OUT ASCII OF A GIVEN CHARACTER) 


char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Char = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num = ['0','1','2','3','4','5','6','7','8','9']
print(char)
print(Char)
print(num)


for i in range(0,26):
 char[i]=ord(char[i]) 
for i in range(0,26):
 Char[i]=ord(Char[i])
for i in range(0,10):
 num[i]=ord(num[i])

print(char)
print(Char)
print(num)










 
