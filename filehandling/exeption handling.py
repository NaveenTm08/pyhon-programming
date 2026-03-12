# try :
#     a = int(input("first number"))
#     b = int(input("second number"))
#     c = a/b
#     print(c)
# except ValueError:
#     print("data must be integar datatype")
# except ZeroDivisionError:
#     print("cannot be divided to the zero")
# else  :
#     print("try block executed")
# finally:
#     print("working")

# x =True
# while x:
#     try :
#         a =int(input("enter the first number"))
#         b = int(input("enter the second number"))
#         z =a+b
#         print(z)
#     except ValueError:
#         print("data validate mistake")
#     else:
#         x= False


# creating a error
# ------------------

class name(Exception):
    pass
try :
    name = input("enter your name")
    if name=="naveen":
        raise name
except :
    print("this name not allowed")

        


    
