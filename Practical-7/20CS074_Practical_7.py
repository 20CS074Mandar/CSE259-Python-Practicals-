#ID:20CS074
#Name: Mandar Sanghavi
#Practical-7 :

N = int(input())
str_list =[]
for i in range(N):
    s = input()
    str_list.append(s)

for i in range(N):
    s = str_list[i]
    length = len(s)
    mid = int(length/2)
    if(length%2==0):
        s1 = s[:mid]
        s2 = s[mid:]
    else:
         s1 = s[:mid]
         s2 = s[mid+1:]
    list_1 = list(s1)
    list_2 = list(s2)
    list_1.sort()
    list_2.sort()

    if(list_1 == list_2):
        print("Yes")
    else:
         print("No")



print("\nId : 20CS074 ")
print("Name : Mandar Sanghavi\n")
