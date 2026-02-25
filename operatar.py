# # arithametic operator

# a=10
# b=20
# c=a+b
# print(c)

# a=20
# b=10
# c=a-b
# print(a-b)

# a=10
# b=2
# c=a*b
# print(c)


# # floor division
# a=10
# b=3
# c=10//3
# print(c)
# a=10
# b=3
# c=a%b
# print(c)

# # Exponent
# a=5
# b=3
# c=5**3
# print(c)


# b=input("enter your name")
# c=input("enter your date of ")
# d=input("class")
# c=int(c)
# age = 2026 - c
# print("name:",b)
# print("age:",age)
# print("class:",d)

# a=input("enter your name")
# b=input("age")
# c=input("class")
# b=int(b)
# age=2006-b
# print("name:",a)
# print("age:",b)
# print("class:",c)

# rectangle area

# a=input("enter the length")
# b=input("enter the breath")
# a=int(a)
# b=int(b)
# c=a*b

# comparision operator

# equal to 

# a="apple"=="Apple"
# print(a)

# output
# False


# a="101"
# b=input("enter your id")
# c=a==b
# print(c)

# output
# True

# not equal operator

# a=10
# b=11
# c=10
# print(a!=b)
# print(a!=c)

# output
# True
# flase

# greater than operator

# a=input("enter your age:")
# a=int(a)
# c=a>17
# print(c)

# less than operator

# a=input("enter your age")
# a=int(a)
# c=20<a
# print(c)

# a=input("enter your age")
# a=int(a)
# c=a>=18
# print(c)

# logical operatara

# age=20
# a=18<age and 40>age
# print(a)

# age=17
# a=age<18 or 40<age
# print(a)

# output
# True

# a=False
# b=not a
# print(b)

# output
# True


# identity operator

# a=["apple","orange"]
# b=["apple","orange"]
# c=a
# print(a is c)
# print(a is b)

# a=["apple","orange"]
# b=["apple","orange"]
# c=a
# print(a is not c)
# print(a is not b)

# membership operator

# a="hello welcome t the page"
# a1="love"
# b=a1 in a
# # print(b)

# a="hello welcome t the page"
# a1="page"
# b=a1  in a
# print(b)

# a=input("1st number:")
# b=input("2nd number:")
# if(a==b):
#     print("two number is equal")
# else:
#     print("two number is not equal")  


a=input("enter your number:")
a=int(a)
if a>0:
    print("your number is positive")
elif a<0:
    print("your number is negative")
else:
    print("your number is zero")