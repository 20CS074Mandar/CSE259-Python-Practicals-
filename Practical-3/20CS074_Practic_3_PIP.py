
#inputing value of k from user 
k=int(input())
#inputing the elements from user
room_nos=(int (x) for x in input().split(' '))
flags={}

#storing the frequency of all elements of room_nos in flags sets
for i in room_nos:
        if i in flags:
                flags[i]+=1  #if ith element of room_no is present in flags then increment the ith index of flags by 1.
        else:
                flags[i]=1 #if it is not present then store 1 in ith index of flag

#finding the unique value in flags set.
for caproom,frequency in flags.items():
        if frequency !=k:          #if the frequency is not same as the k value then print the captians room
                print("\nCaptian's room :- ",caproom)



print("\nId : 20CS074 ")
print("Name : Mandar Sanghavi\n")