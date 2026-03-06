# import pandas as pd
# a=pd.DataFrame({'A': [1, 2, 3]})

# print(a)

import pandas as p

# data = {'name':['kiran','naveen','hari','rahul'],"age":[30,40,10,60],"place":["palakkad","thrissur","malapuram",'eranakulam']}

# b = len(data['name'])
# z= []
# for i in range(1,b+1):
#     z.append(i)


# a = p.DataFrame(data, index=z)

# print(a)


a ={"CARS":["Bmw","Nexon","Lamborgini","Benz","Minicopper","Swift","Mahindra"],"MILAGE":[18,13,7,8,13,24,9],"PRICE":[140000,40000,200000,350000,20000,15000,21000]}
b = len(a["CARS"])
z =[]
for i in range(1,b+1):
    z.append(i)
data =p.DataFrame(a,index=z)
print(data)
