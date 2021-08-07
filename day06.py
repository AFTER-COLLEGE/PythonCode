#####     QUESTIONS ON STRINGS     #####
#--1--  How would you confirm that 2 strings have the same identity?
# S1="dance"
# S2=S1
# print(S1==S2)
# print(S2 is S1)
# print(S1 is S2)
# S3="dance"
# print(S1==S3)
# print(S1 is S3)
# print(S2 is S3)

#--2-- How would you check if each word in a string begins with a capital letter?
# string=input()
# if (string.istitle())== True:
#     print("Capital")
# else:
#     print("Small")

#SECOND METHOD

# string=input()
# if string == string.title():
#     print("Capital")
# else:
#     print("Small")

#--3-- Find the index of the first occurrence of a substring in a string
# for i in range(100):
#     string=input("Enter string:")
#     sr=input("Enter sub string:")
#     print("Your substring is at " + str(string.find(sr)))
#     ask=input("You want to check again(y for YES and n for NO):")
#     if ask=="n":
#         break
#     elif ask=="y":
#         continue
#     else:
#         print("Invalid Input")

#--4-- Reverse the string “hello world” with out indexing:
# string=input()
# print(f'the reversed string is {"".join(reversed(string))}')

#--5-- Join a list of strings into a single string
list=[]
n=int(input("enter no of element in list you want to add:"))
for i in range(n):
    ele=input("Enter elements:")
    list.append(ele)
print(f'now your string is : {" ".join(list)}')