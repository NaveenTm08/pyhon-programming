try :
    a = int(input("first number"))
    b = int(input("second number"))
    c = a/b
    print(c)
except ValueError:
    print("data must be integar datatype")
except ZeroDivisionError:
    print("cannot be divided to the zero")
else  :
    print("try block executed")
finally:
    print("working")