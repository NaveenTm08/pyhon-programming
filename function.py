# def hello():
#     print("helloworld")
# 
# hello()

# output
# helloworld


# def add(a,b):------parameter
#     print(a+b)
# add(25,25)---------argument

# output
# 50

# with argument and with return value
# -----------------------------------
# def multi(a,b):
#     return a*b
# a=multi(10,5)
# print(a)

# without argument and with return value
# ----------------------------------------
# def data():
#     return "rayees"
# a=data()
# print(a)

# output
# rayees

# default argument

# def add(a,b=0):
#     print(a+b)
# add(10)

# output
# 10

# def add():
#     a = int(input("enter the first number:"))
#     b = int(input("enter the second number:"))
#     return a+b
# z=add()
# print(z)

# def add():
#     a = int(input("enter the first number:"))
#     b = int(input("enter the second number:"))
#     return a+b
# v=add()
# print(v)
# def sub():
#     c = int(input("enter the firstnumber:"))
#     e = int(input("enter the second number"))


# def add(a,b):
 
#     return(a+b)

# def sub(a,b):
    
#     return(a-b)

# def multi(a,b):
#     return(a*b)

# def div(a,b):
#     return(a/b)

# choice = input("enter the choice")
# a = int(input("enter the first number"))
# b = int(input("enter the second number"))
# match choice:
#     case "+":
#         print(add(a,b))
#     case "-":
#         print(sub(a,b))
#     case "*":
#         print(multi(a,b))
#     case "/":
#         print(div(a,b))


# n=3
# a=1
# for i in range(1,n+1):
#     a=a*i
# print(a)

# output
# 6

# recursive function
# --------------------
# def fact1(n):
#     if n==1:
#         return 1
#     else:
#         return n * fact1(n-1)
# a=fact1(6)
# print(a)

# def cout(a):
#     print(a)
#     if a==1:
#         return 1
#     else:
#         return cout(a-1)
# cout(10)

# lambda
# without argument & without return

# hello = lambda :print("hello world")
# hello()

#hello world

# hello = lambda x,y :print(x+y)
# hello(100,200)

# output
# 30

# hello  = lambda x,y:x+y
# a = hello(100,200)
# print(a)

# sq = 5
# def multi (sq):
#     return sq*sq
# a = multi(sq)
# print(a)

# sq = lambda x,y=2:x**y
# a = sq(5,2)
# print(a)

# ouput
# 25

#  lambda using map function
# a=[1,2,3,4,5]
# b=list(map(lambda x:x**3 , a))
# print(b)

# filter------------
# reduce-----------


# object orient programming
# -----------------------------
# class Hello():
#     def hi(self):
#         self.name="naveen"
# obj1 = Hello()
# obj1.hi()
# obj1.name = "kiran"
# print(obj1.name)
# obj2 = Hello()
# obj2.hi()
# print(obj2.name)

# class employe():
#     def add(self,name,salary):
#         self.name = name
#         self.salary = salary
# obj = employe()
# obj.add('naveen',1000)
# print("name:",obj.name,"|salary:",obj.salary)

# class employe():
#     def add(self,name,salary):
#         self.name = name
#         self.salaray = salary
#     def show(self):
#         print("name:",self.name)
#         print("slary:",self.salaray)
# a=employe()
# a.add("naveen",10000)
# a.show()

# person2 = employe()
# person2.add("kiran",5000)
# person2.show()

# output
# name: naveen
# slary: 10000
# name: kiran
# slary: 5000

# class car():
#     def add(self,name,speed,price):
#         self.name = name
#         self.speed = speed
#         self.price = price
#     def show(self):
#         print("name:",self.name)
#         print("speed:",self.speed)
#         print("name:",self.price)
# bmw= car()
# bmw.add("bmw m5",400,4000000)
# bmw.show()

# alto = car()
# alto.add("alto 800",137,350000)
# alto.show()

class Employee():
    def add(self,name,salary,joindate):
        self.name = name
        self.salary = salary
        self.joindate = joindate
    def show(self):
        print("name",self.name)
        print("salary:",self.salary)
        print("experience:",2026-self.joindate)





person1 = Employee()
person1.add("sooraj",5000,2020)
person1.salary=8000
person1.show()
print()

