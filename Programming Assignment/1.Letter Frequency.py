


def sort_dict_by_value(d, reverse = False):
  return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))

str = input("Enter String :- ")
dicto={}

for  i in str:
    keys=dicto.keys()
    if i in keys:
        dicto[i]+=1
    else:
        dicto[i]=1

print(sort_dict_by_value(dicto, True))
