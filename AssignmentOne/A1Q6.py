from collections import Counter
StringList1 = list()
num_of_strings = int(input("Enter The Number Of Strings: "))
for x in range(1,num_of_strings + 1):
    string = input("Enter string %s:"%(x))
    StringList1.append(string)
print("Original StringList1:")
print(StringList1)

MStringList1 =  [i for i in set(StringList1) if StringList1.count(i) > 1]
freq = dict(Counter(StringList1))
for x in MStringList1:
    if freq.get(x) % 2 == 0:
        print(x,"occurs even no. of times in StringList1.")
    else:
        print(x,"occurs odd no. of times in StringList1.")

def del_last(lst,x) -> list:
    lst.reverse()
    lst.remove(x)
    lst.reverse()
    return lst 
  

for x in range(len(StringList1)):
    for y in range(len(StringList1)-1,x,-1):
        if StringList1[x] == StringList1[y]:
            StringList1 = del_last(StringList1,StringList1[x])
            break

print("After Removing i >= 2 occurence StringList1:")
print(StringList1)