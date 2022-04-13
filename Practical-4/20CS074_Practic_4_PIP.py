
#accpting the length of lsit form user
from array import array


n=int(input())
# accepting the values of list from the user
num_list=map(int,input().split())

num_list=sorted(num_list,reverse=True)

for i in range(len(num_list)):
        if(num_list[i]==num_list[0]):
                continue
        else:
                print("Runner-Up in list is:",num_list[i])
                break



print("\nId : 20CS074 ")
print("Name : Mandar Sanghavi\n")
