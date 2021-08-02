# ls=["name",True,66.7]
# print(ls)
# ls.append(99)
# print(ls)
# ls=["ashish","rahul","vijay","raghav","sonu","raj","gaurav","suraj"]
# del(ls[2])
# print(ls)

##########---------Questions Based on Python Lists----------###########
#--1--Check if the list contains element?

# ls=[1,2,3,"ashish"]
# if len(ls) == 0:
#     print("empty")
# else:
#     print("List is not empty")


#--2--differnce btw append and extend

# l=[1,2,3,"ashish"]
# l.append("Sharma")
# print(l)
# l.append([5,6])
# print(l)
# l.extend([7,8])#extend() adds each value from a 2nd list as its own elements.
# print(l)

#--3-- Remove all elements from the list 

# l=["ashish","sam","rajiv","sonu",1,2,3]
# print(l)
# l.clear()
# print(l)

# l=["ashish","sam","rajiv","sonu",1,2,3]
# print(l)
# del(l[:])
# print(l)

#--4-- How to manipulate every element in a list with list comprehension

# l=[0,1,2,3,4]
# for i in l:
#     i=i+5
#     print(i,end=" ")
#     i+=1

#--5-- Count the occurrence of a specific object in a list
# fruit=["Mango","Apple","banana","Mango","Apple"]
# print(fruit.count("Mango"))

#--6-- Return the length of a list
# li=["a","b","c","ashish",1,2,3]
# print(len(li))

#--7-- How to check if an element is not in a list
# ls=[1,2,3,4,5,"a","b","c"]
# print(5 in ls)
# print("RAJIV" in ls)
# print(1 in ls)

#--8-- Multiply every element in a list by 5 with the map function
# lis=(1,2,3,4,5,6,7,8,9,10)
# def multiply_5(num):
#     a=num*5
#     return a
# ls=list(map(multiply_5,lis))
# print(ls)

#--9-- Insert value at a specific index in an existing list
# ls=["a","b","c","D","e"]
# ls.insert(3,10)
# print(ls)

#--10-- to convert list to dictionary

# def convert(ls):
#     new={ls[i]: ls[i+1] for i in range (0,len(ls),2)}
#     return new
# ls=["a",1,"b",2,"c",3]
# print(convert(ls))
# print(type(convert(ls)))

#--11-- Modify an existing list with a lambda func
# ls=[10,20,30,40,50]
# fun=list(map(lambda ls:ls*5,ls))
# print(fun)

#--12-- sorting a list in ascending order 
# l=[10,4,2,1,6,8,9,3,5,7]
# l.sort()
# print(l)

#--13-- sorting a list in descending order 
# l=[10,4,2,1,6,8,9,3,5,7]
# l.sort(reverse=True)
# print(l)

#--14-- Filter even value from list

# l=[1,2,3,4,5,6,7,8,9,10]
# for i in l:
#     if i % 2==0:
#         print(i,end="")
#         i+=1

#--15-- Get the first element from each nested list in a list
# ls=[[1,2,3],[4,5,6],[7,8,9]]
# print([i[0] for i in ls])

#--16-- Reverse the order of list using slicing
ls=[1,2,3,4,5]
ls2=ls[::-1]
print(ls,ls2)