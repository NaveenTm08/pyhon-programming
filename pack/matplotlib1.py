
import matplotlib.pyplot as plt
import pandas as pd

year = []
profit =  []


x= True
while x:
    choice = input("enter your choice(show=s,adddata=a ,exit=e,display=d):")
    match choice:
        case "a":
            print("add data")
            year.append(int(input("enter the year:")))
            profit.append(int(input("enter your profit")))

        case "s":
            fig, ax = plt.subplots()             # Create a figure containing a single Axes.
            ax.plot(year, profit)                 # Plot some data on the Axes.
            ax.set_xlabel('year')
            ax.set_ylabel('profit')
            plt.show()  
        case "d":
            data = pd.DataFrame({'year':year,'profit':profit})
            print(data)
           
        case "e":
            x = False


        

    






                             # Show the figure.