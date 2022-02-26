#ID:20CS074
#Name: Mandar Sanghavi
#Practical-6 :

from stringprep import c8_set


N=int(input())
str_list=[]
cuntr_dict={}

for i in range (N):
    st=input()
    str_list.append(st)
    
    if s in cuntr_dict:
        cuntr_dict[st]+=1
    else:
        cuntr_dict[st]=1

print(len(cuntr_dict))
print(' '.join([str(cuntr_dict[s]) for s in cuntr_dict]))
