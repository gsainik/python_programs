#To check the given number is prime or not

def prime(n):
    if n < 2 :
        print("{} is not a prime number".format(n))
    else:
        count=0
        for i in range(1,n+1):
            if n%i==0:
                count+=1
            else:
                continue
        return count
n= int(input("Enter a number : "))
count = prime(n)
if count == 2:
    print("{} is prime number".format(n))
else:
    print("{} is not a prime number".format(n))



# Alternative 2
def is_prime(num):
    if num <= 1:
        return False
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
    return True

num= int(input("Enter a number to check it is Prime or Not: "))
if is_prime(num):
    print("{} is prime number".format(num))
else:
    print("{} is not a prime number".format(num))
