# n1= int(input("Enter first number"))
# n2= int(input("Enter first number"))

# if n1>n2:
#     print("Bigger number is:", n1)
# else:
#     print("Bigger number is:", n2)

# n=input("Enter some string:")
# index=0
# count=1

# for char in n:
#     print("The Character at", index, "is",char)
#     index= index +1 
#     count=count+1
# print("Total number of characters present in the string",n,"is",count-1)

# x=10
# for n in range(11):
#     x = x -1
#     if x<0:
#         break
#     else:
#         print(x)
    
# n=int(input("Enter any number:"))
# sum=0
# i=1
# while i<=n:
#     sum = sum + i
#     i = i + 1

# print("Sum of first",n,"numbers is",sum)

# for i in range(1,10):
#     print(i)

# s=input("Enter String:")
# s1=input("Enter sub string")

# if s1 in s:
#     print("Substring:{} is present in Main srting:{}".format(s1,s))
# else:
#     print("Substring:{} is NOT present in Main srting:{}".format(s1,s))

s=input("Enter Main String: ")
s1=input("Enter Sub String: ")
flag = False
n=len(s)
position=-1
count =0
while True:
    
    position=s.find(s1,position+1,n)
    
    #print("Substring found at: ", position)
    if position == -1:
        break
    print("Substring found at index: ", position)
    count = count+1
    flag=True
    
print("Total count is", count)
if flag==False:
    print("Substring,",s1, "Not found")
