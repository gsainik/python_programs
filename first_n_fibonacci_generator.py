#To generate first n fibonacci numbers
def fibonacci_generator():
   a,b=0,1
   while True:
       yield a
       a,b=b,a+b

g = fibonacci_generator()
count=1
n= int(input('enter number of fibonacci number required : '))
while count <= n:
   print(next(g))
   count= count+1
