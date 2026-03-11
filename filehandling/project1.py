
import json
import pandas as p
file = open("data1.json","r")
data = json.load(file)
file.close()
x = True
while x:
    choice = input("enter your choice(a,r,e)")
    match choice:
        
        case "a":  
            data["name"].append(input("enter your name:"))
            data["email"].append (input("enter your emali:"))
            data["mobile"].append(input("enter your moblie:"))
            file = open("data1.json","w")
            json.dump(data,file)
            file.close()
        case "r":
            n = p.DataFrame(data)
            print(n)
            file1=open("details.txt","w")
            file1.write(str(n))
            file1.close()

        case "e":
            x = False


