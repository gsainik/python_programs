#program to reverse the Order of Words
"""
Input String : Python is both a strongly typed and a dynamically typed language.
Output String : language. typed dynamically a and typed strongly a both is Python

"""

s = input('Enter a String: ')
l=s.split()
print(l)
l1 = []
i= len(l)-1
while i>=0:
    l1.append(l[i])
    i=i-1
output= ' '.join(l1)
print(output)



#Alternative 2

s = input('Enter a String: ')
l=s.split()
print(l)
l1 = []
# i= len(l)-1
for i in l[::-1]:
    l1.append(i)
    print(l1)
output= ' '.join(l1)
print(output)


