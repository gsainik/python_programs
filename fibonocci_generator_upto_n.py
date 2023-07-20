# To generate fibonacci numbers up to n using Generators

def fibonacci_generator():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

g = fibonacci_generator()
n= int(input('enter number up to which the fibonacci number are required : '))
for x in g:
    if x<= n:
        print(x)
    else:
        break
