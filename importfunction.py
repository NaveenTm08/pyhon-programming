def add(a,b):
    print(a+b)
def userdata():
    a=input("enter your name")
    b=input("enter your place")
    print("hi,\n i am "+a,"i am come from "+b)

def calc(a):
    b = int(input("enter your first number"))
    c = int(input("enter your second number"))
    match a:
        case "+":
            print(c+b)
        case "-":
            print(b-c)
        case "*":
            print(b*c)
        case "/":
            print(b/c)
        case _:
            print("inavlid input (+,-,*,/)")




# count(10,100)
# 1 - 10  
def count(a,b=0,c=1):
    if b==0:
        for i in range(1,a+1):
            print(i)

    else:
        if c<0:
            for i in range(a,b-1,c):
                print(i)
        else:
            count(10,1,-1)
