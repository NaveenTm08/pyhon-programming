# a=int(input("enter the number"))
# for i in range(a):
#     print(" *"* i)
    
# output

#  *
#  * *
#  * * *
#  * * * *
#  * * * * *
    

# a=int(input("enter the number"))
# for i in range(a):
#     print(" "*a+"* " *i)
#     a-=1

# output

#     *
#    * *
#   * * *
#  * * * *

# a=int(input("enter the number"))
# for i in range(1,a+1):
#     print()
#     for b in range(1,i+1):
#         print(b,end=" ")

# 
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# a=int(input("enter the number"))
# for i in range(1,a+1):
#     print()
#     print(" "*a,end="")
#     a-=1
#     for j in range(1,i+1):
#         print(j,end=" ")

# a=int(input("enter the rows:"))
# b=a
# d=1
# for i in range(1,a+1):
#     print()
#     print(" "*b,end="")
#     for j in range(1,i+1):
#         print(d,end=" ")
#         d+=1
#     b=b-1

# limit=int(input("enter the number"))
# a=1
# b=1

# for i in range(limit):
#     print(a)
#     c = a+b
#     a = b
#     b = c










#fibonacci series

# limit=int(input("enter the number"))
# a=1
# b=1
# c=1

# for i in range(limit):
#     a=b
#     b=c
#     c=a+b
#     print(a)

# a=int(input("enter the number"))
# count =0
# for i in range (1,a+1):
#     if a%i==0:
#         count +=1
    
# print(count)
# if count == 2:
#     print("prime number")
# else :
#     print("not prime number")


# a=int(input("enter the number"))
# for i in range(a):
#     print(" "*a+"* "*i)
#     a-=1
    
# a=int(input("enter the row"))
# s=a
# for i in range(1,a+1):
#     print(" "*s,end="")
#     for j in range(i):
#         print("* ",end="")
#     print()
#     s=s-1

# a=int(input("enter the number"))
# s=a
# for i in range(1,a+1):
#     print()
#     print(" "*s,end="")
#     for j in range(i):
#         if j==0 or j==(i-1) or a==i:
#             print("*",end=" ")
#         else:
#             print("  ",end="")
#     s-=1


# a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# b=int(input("enter the row"))
# for i in range(b):
#     print((a[i]+" ")*(i+1))





# b=int(input("enter the number"))
# c =1
# for i in range(-1,-(b+1),-1):
#     print((a[i]+" ")*c)
#     c=c+1 










