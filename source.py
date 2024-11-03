# Modules
import csv
import os
from datetime import date
import pprint

# Functions
# add expense to the .csv file
def addexp():
    exp={
        'Date':'',
        'Category':'',
        'Description':'',
        'Amount':''
    }
    # exp['Date']= input("Enter the date: ")
    exp['Date']= date.today()
    exp['Category']= input("Enter the category: ")
    exp['Description']= input("Enter the description(Name-Quantity): ")
    exp['Amount']= int(input("Enter the amount: "))

    exp_list=[exp]

    file_exists=os.path.isfile('ExpenseTrack/exp_source.csv')
    with open('ExpenseTrack/exp_source.csv','a',newline='') as file:
        writer=csv.DictWriter(file,fieldnames=["Date", "Category", "Description", "Amount"])
        
        if not file_exists or os.stat('ExpenseTrack/exp_source.csv').st_size == 0:
            writer.writeheader()
        
        writer.writerows(exp_list)
        print("Expense Added Successfully!")

# sort expense based on fieldname
def sort(fieldname):
    with open('ExpenseTrack/exp_source.csv','r', newline='') as file:
        reader = csv.DictReader(file)
        data = list(reader)

        data.sort(key=lambda row: row[fieldname])

        for row in data:
            print(row)

# view expense based on date
def viewexp():
    with open('ExpenseTrack/exp_source.csv','r', newline='') as file:
        reader = csv.DictReader(file)
        choice=int(input("1. View all expenses\n2. View expenses based on date\nEnter your choice: "))
        if choice==1:
            data=list(reader)
            pprint.pprint(data)
        elif choice==2:
            date=input("Enter the date to view the expense(YYYY-MM-DD): ")
            count=0
            for row in reader :
                if row['Date']==date:
                    o_data=list(row.values())
                    print(f'{count+1}. {o_data[1]}\t{o_data[2]}\t{o_data[3]}\n')
                    count+=1
            if count==0:
                print("No Record Found!")

# delete an expense
# need to add an option to delete expense based on date
def delexp():
    with open('ExpenseTrack/exp_source.csv','r', newline='') as file:
        reader = csv.DictReader(file)
        choice=int(input("1. Delete all expenses\n2. Delete expense based on row number\nEnter your choice: "))
        if choice==1:
            with open('ExpenseTrack/exp_source.csv','w', newline='') as file:
                writer = csv.DictWriter(file,fieldnames=["Date", "Category", "Description", "Amount"])
                writer.writeheader()
            print("All Expenses Deleted Successfully!")
        elif choice==2:
            data=list(reader)
            pprint.pprint(data)
            print("Enter the row number to delete the expense: ")
            row=int(input())
            data.pop(row-1)
            print(data)
            with open('ExpenseTrack/exp_source.csv','w', newline='') as file:
                writer = csv.DictWriter(file,fieldnames=["Date", "Category", "Description", "Amount"])
                writer.writeheader()
                writer.writerows(data)
            print("Expense Deleted Successfully!")

    
            

# Execution part
# addexp()
# viewexp()
# delexp()