### HACKERRANK PROBLEM on list ###


# n=int(input())
# k=[]
# for i in range(0,n):
#     cho=input().split()
#     if (cho[0]== "insert"):
#         k.insert(int(cho[1]),int(cho[2]))
#     elif (cho[0]== "print"):
#         print(k)
#     elif (cho[0]== "pop"):
#         k.pop(int(cho[1]))
#     elif (cho[0]== "append"):
#         k.append(int(cho[1]))
#     elif (cho[0]== "remove"):
#         k.remove(int(cho[1]))
#     elif (cho[0]== "sort"):
#         k.sort()
#     else:
#         k.reverse()

##   MINI_MAX_SUM PROBLEM   ##
arr=[1,2,3,4,5]
arr.sort()
minsum=0
maxsum=0
for i in range(4):
    minsum+=arr[i]
print(minsum,end=" ")
for i in range(4,0,-1):
    maxsum+=arr[i]
print(maxsum)
