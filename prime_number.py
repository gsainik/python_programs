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
