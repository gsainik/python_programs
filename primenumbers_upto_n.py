num= int(input("Enter the N value up to which the prime numbers to be displayed :"))
n=2
while n<=num:
    count = 0
    for i in range(2,n):
        if n%i== 0:
            count = 1
        else:
            continue
    if count==0:  
        #if count == 0 then it prints all prime number
        #if count == 1 then it prints all Non prime number
        print("{}".format(n))
    n+=1