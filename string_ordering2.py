#program to reverse the internal content of each word

"""
Input String : Python is both a strongly typed and a dynamically typed language.
Output String : nohtyP si htob a ylgnorts depyt dna a yllacimanyd depyt .egaugnal

"""
s = input('Enter a String: ')
l= s.split()
l1=[]
i=0
while i<=len(l)-1:
    l1.append(l[i][::-1])
    i=i+1
output= ' '.join(l1)
print(output)

#Alternative 2

s = input('Enter a String: ')
l=s.split()
print(l)
l1 = []
# i= len(l)-1
for i in l:
    l1.append(i[::-1])
    print(l1)
output= ' '.join(l1)
print(output)