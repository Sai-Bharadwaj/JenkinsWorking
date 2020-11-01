x=int(input("Enter First Number:"))
y=int(input("Enter Second Number:"))
#z=int(input("Enter Third Number:"))

#if(x>y):
#    print("First number is greater,",x)
#else:
#    print("Second Number is greater,",12)

#l=  x if x>y and x>z else y if y>z else z
#print("Max values is:",l)

l = "Both Numbers are equaly" if x==y else "First number is greater"  if x>y else "First number is smaller:"
print(l)
