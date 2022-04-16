def maxArea(A, Len) :
    area = 0
    for  i in range(Len) :
        for j in range(i + 1, Len) :
            area = max(area, min(A[j], A[i]) * (j - i))
    return area

a = [int(n) for n in input("Enter heights: ").split()]
len1 = len(a)
print("Max are :- ",maxArea(a, len1))
print("\nId : 20CS074")
print("Name : Mandar Sanghavi")