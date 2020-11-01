#a,b,c,d =[int (num) for num in input("ENter 4 numbers for sum, with space:").split(',')]
#print("Sum is", a+b+c+d)


#x,y=[float(num) for num in input("Enter 2 num with space for multiplication").split()]
#print("Product is ", x*y)
####################################################################################################
# final = eval(input("""ENter Any data, to know its "Type" """))
# result = type(final)
# print("The type of entered data is:", result , "HI")
# print("Good"+"Evening")
# print("Good","Evening")

# for data in final:
#     print(data)

####################################################################################################
# n1= int(input("Enter first number"))
# n2= int(input("Enter first number"))

# if n1>n2:
#     print("Bigger number is:", n1)
# else:
#     print("Bigger number is:", n2)
####################################################################################################

# n=input("Enter some string:")
# index=0
# count=1

# for char in n:
#     print("The Character at", index, "is",char)
#     index= index +1 
#     count=count+1
# print("Total number of characters present in the string",n,"is",count-1)
####################################################################################################

# x=10
# for n in range(11):
#     x = x -1
#     if x<0:
#         break
#     else:
#         print(x)
    ####################################################################################################

# n=int(input("Enter any number:"))
# sum=0
# i=1
# while i<=n:
#     sum = sum + i
#     i = i + 1

# print("Sum of first",n,"numbers is",sum)
####################################################################################################

# for i in range(1,10):
#     print(i)

# s=input("Enter String:")
# s1=input("Enter sub string")

# if s1 in s:
#     print("Substring:{} is present in Main srting:{}".format(s1,s))
# else:
#     print("Substring:{} is NOT present in Main srting:{}".format(s1,s))
####################################################################################################
#x=int(input("Enter First Number:"))
#y=int(input("Enter Second Number:"))
#z=int(input("Enter Third Number:"))

#if(x>y):
#    print("First number is greater,",x)
#else:
#    print("Second Number is greater,",12)

#l=  x if x>y and x>z else y if y>z else z
#print("Max values is:",l)
####################################################################################################

#l = "Both Numbers are equaly" if x==y else "First number is greater"  if x>y else "First number is smaller:"
#print(l)
####################################################################################################
# from random import *



# print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9), sep="")

# sai=10
# SAI2SUN=20
# sai=30

# print(sai)
# print(SAI2SUN)

####################################################################################################

# s=input("ENter Main String:")
# s1=input("ENter SUbstring:")
# flag= False
# n=len(s)
# position=-1
# final =0

# while True:
#     position=s.find(s1,position+1,n)
#     if position==-1:
#         break
#     print("Substring found at index:",position)
#     flag=True
#     final = s.count(s1)
# if flag==False:
#     print("Substring not found")
# print("Total count is:",final)
# k=s.replace("Pisipati","P")
# print("Original String is:",s)
# print("Replaced or Modifies String is:",k)

####################################################################################################
# s=input("Enter any string:")
# l=s.split()
# #print(l)
# l1=[]
# i=len(l)-1
# #print(n)
# while i>=0:
#     l1.append(l[i])
#     #print(final)
#     i=i-1
#     print("l1 value", l1)
# output=' '.join(l1)
# print(output)

####################################################################################################
# s=input("Enter any string:")
# l=s.split()
# #print(l)
# i=len(l)-1
# #print(i)
# l1=[]

# while i>0:
#     for char in l:
#         #l1.append(char)
#         l1.append(char[::-1])
#         print("jjjjj",l1)

#         ### k = print(char[::-1])
#         ### l1.append(k)
#         ### print("jjjjj",l1)
#         output=' '.join(l1)
        
#         i=i-1
# #print(l1)
# print(output,sep='')
# #m= (''.join(k))
####################################################################################################
# #Program to reverse order of words


# s=input("Enter any string:")
# l=s.split()

# l1=[]
# i=len(l)-1
# while i>=0:
#     l1.append(l[i])
#     i =i-1
# output=' '.join(l1)
# print(output)
####################################################################################################
##Program to reverse internal content words


# s=input("Enter any string:")
# l=s.split()
# #print(l)
# l1=[]
# i=len(l)-1

# while i>=0:
#     for char in l:
#         #print(char[::-1])
#         l1.append(char[::-1])
#         #l1.append(s[::-1])
#         #print(char)
#         #print(l1)
#         i=i-1
# output=' '.join(l1)
# print("Output in reversed order is:", output)

####################################################################################################

# s=input("Enter a string")
# print("Characters at EVEN position is:", s[0::2])
# print("Characters at ODD position is:", s[1::2])
 ####################################################################################################
        
#Program to merge characters of 2 strings into a single string by taking characters alternatively

# s1=input("Enter First String:")
# s2=input("Enter Second String:")
# output=''
# i,j=0,0


# while i<len(s1) or j<len(s2):
#     if i<len(s1):
#         output=output+s1[i]
#         i=i+1
#     if j<len(s2):
#         output=output+s2[j]
#         j=j+1

# print(output)

 ####################################################################################################
#Write a program to sort the characters of the string and first alphabet symbols followed by numeric values

# s=input("Enter any String with digits:")
# s1=s2=output=''

# for char in s:
#     if char.isalpha():
#         s1=s1+char
#     else:
#         s2=s2+char
# print(s1,s2)
    
# for char in sorted(s1):
#     output=output+char
# for char in sorted(s2):
#     output=output+char
# print("Sorted output:", output)

 ####################################################################################################

# s=input("Enter a String value with digits in formato of AXBXFX:")
# print("Sample Example for Reference, A3D5F7")
# output=''
# for char in s:
#     # if char.isdigit():
#     #     print("Enter Starting value as String not number")
#     #     break
#     if char.isalpha():
#         output=output+char
#         previous = char
#     else:
#         output=output+previous*(int(char)-1)
# print(output)
 ####################################################################################################

# To know how many characters are there in the string

# s=input("Enter Some String:")
# d={}

# for char in s:
#     if char not in d.keys():
#         d[char]=1
#     else:
#         d[char]=d[char]+1
# for keys,values in d.items():
#     print("{} occues {} times".format(keys,values))

 ####################################################################################################


# def newmethod332():
#     def f1(a,b,c):
#         #print("SUb is:", a-b-c)
#         k=a-b-c
#         return k

#     l=f1(10,20,30)
#     print(l)

 ####################################################################################################

# def outer():
#     print("outer func started")
#     def inner():
#         print("inner func started")
#     print("outer func returning inner func")

#     return inner
    
    




# k=outer()

# k()
 ####################################################################################################
# def decor(func):
#     def inner(name):
#         if name=='Sunny':

#             print("Hello", name,"Very very very very Goood Morning")
#         else:

#              func(name)
#     return inner

 ####################################################################################################



# @decor
# def wish(name):
#     print("Hello",name,"Good Monring")


# k = int(input("Enter no of people you want to greet:"))
# i=0
# while i<=k:
#     wish(input("ENter a name: "))
#     #print("Enter a name: ")
#     i=i+1

 ####################################################################################################


class Student:

    def __init__(self,name,rollno,marks):
        self.x=name
        self.y=rollno
        self.z=marks


    def talk(self):
        print("Hello My Name is: ",self.x)
        print("Hello My RollNum is: ",self.y)
        print("Hello MyMarks are: ",self.z)


s1=Student(input("Enter a name"),int(input("ENter Roll no: ")),int(input("Marks : ")))
s1.talk()
