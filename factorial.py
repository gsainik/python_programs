#Factorial of a Given Number
n= int(input("Enter a number to find its factorial :"))
fact=1
for i in range(1,n+1):
   fact=fact*i
print("Factorial of {} is {}".format(n,fact))
