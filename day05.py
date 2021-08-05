## Question Based ON Functions ##

#__1__ Write a Python function to find the Max of three numbers.
# def max_3(a,b,c):
#     arr=[]
#     arr.append(int(a))
#     arr.append(int(b))
#     arr.append(int(c))
#     maxv=0
#     for i in arr:
#         if i > maxv:
#             maxv=i
#     return maxv

# print(max_3(2,3,4))

#__2__ Get a list as input from user
# def enter_el():
#     ls=[]
#     n=int(input("Enter number of elements :"))
#     for i in range(0,n):
#         ele=int(input("enter element:"))

#         ls.append(ele)
#     return ls


#__3__  Write a Python function to sum all the numbers in a list.
# def sum_list(ls):
#     count=0
#     for i in ls:
#         count+=i

#     return count
# lst=enter_el()
# print(sum_list(lst))

#__4__  Write a Python function to multiply all the numbers in a list.
# ls=[8,2,3,-1,7]

# def multiply(ls):
#     count=1
#     for i in ls:
#         count*=i
#     return count
# print(multiply(ls))

#__5__ Write a Python program to reverse a string.
# s=input()
# for i in s[::-1]:
#     print(i,end="")

#__6__ Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument. 
n=int(input("Enter number : "))
def fact(n):
        if n == 0:
            return 1
        else:
            return n * fact(n-1)

print(fact(n))
