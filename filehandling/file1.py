# f =open("demo.txt","w")
# f.write("python djang")
# f.close()


# f =open("demo.txt","a")
# f.write("python djang\n")
# f.close()


# f =open("demo.txt","r")
# a = f.read()
# print(a)
# f.close()

# import csv

# data = [['kiran','palakad'],['thrissur','ajay'],['malapuram','vijay']]
# f = open('demo1.csv','w',newline='')
# w =csv.writer(f)
# w.writerows(data)
# f.close()


# file = open("demo1.csv","r",newline="")
# w = csv.reader(file)
# for i in w:
#     print("name:",i[0])
#     print("place:",i[1])

# output

# name: kiran
# place: palakad
# name: thrissur
# place: ajay
# name: malapuram
# place: vijay


# json
# data = {"name":"naveen","age":"20","place":"thrissur"}
import json
# file = open("data.json","w")
# json.dump(data,file)
# file.close()

f = open ("data.json","r")
a = json.load(f)
print(a)

# output

# {'name': 'naveen', 'age': '20', 'place': 'thrissur'}


