#Factorial of a Given Number using recursion
def factorial(n):
    if n==1 or n==0 :
        return 1
    else:
        return n*factorial(n-1)

n=int(input("Enter a number to get factorial :"))
print("factorial of {} is {}".format(n,factorial(n)))
