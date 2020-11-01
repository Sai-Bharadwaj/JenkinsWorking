#a,b,c,d =[int (num) for num in input("ENter 4 numbers for sum, with space:").split(',')]
#print("Sum is", a+b+c+d)


#x,y=[float(num) for num in input("Enter 2 num with space for multiplication").split()]
#print("Product is ", x*y)

# final = eval(input("""ENter Any data, to know its "Type" """))
# result = type(final)
# print("The type of entered data is:", result , "HI")
# print("Good"+"Evening")
# print("Good","Evening")

# for data in final:
#     print(data)
    
s=input("ENter Main String:")
s1=input("ENter SUbstring:")
flag= False
n=len(s)
position=-1
final =0

while True:
    position=s.find(s1,position+1,n)
    if position==-1:
        break
    print("Substring found at index:",position)
    flag=True
    final = s.count(s1)
if flag==False:
    print("Substring not found")
print("Total count is:",final)
k=s.replace("Pisipati","P")
print("Original String is:",s)
print("Replaced or Modifies String is:",k)