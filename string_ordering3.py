#Program to remove duplicate characters from a given string

"""
Input String : Pythonpython abc ABCabcddeeFFFdeabcdEF
Output String : Pythonp abcABCdeFE

"""
s = input("Enter a String to remove the duplicates: ")
print(s)
l = []
for i in s:
    if i not in l:
        l.append(i)
output= ''.join(l)
print(output)
