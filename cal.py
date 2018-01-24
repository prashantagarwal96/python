def add(a,b):
   return a+b
def subtract(a,b):
   return a-b
def multiply(a,b):
   return a*b
def divide(a,b):
   return a/b
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 
choice = input("Enter choice:")
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
if choice=='1':
   print(n1,"+",n2,"=",add(n1,n2))
elif choice=='2':
   print(n1,"-",n2,"=",subtract(n1,n2))
elif choice=='3':
   print(n1,"*",n2,"=",multiply(n1,n2))
elif choice=='4':
   print(n1,"/",n2,"=",divide(n1,n2))
else:
   print("Invalid input")
