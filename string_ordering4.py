#Program to to find the number of occurences of each character in a given string


s = input("Enter a String: ")
d={}
for i in s:
    d[i] = d.get(i,0)+1

print(d)
for k,v in d.items():
    print("{} is {} Times".format(k,v))



# Alternative 2

s = input("Enter a String: ")
d={}
for i in s:
    if i in d.keys():
        d[i] = d.get[i]+1 # type: ignore
    else:
        d[i] = 1

print(d)
for k,v in d.items():
    print("{} is {} Times".format(k,v))