# Modules
import csv
import os
from datetime import date

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
    exp['Description']= input("Enter the description(Name,Quantity): ")
    exp['Amount']= int(input("Enter the amount: "))

    exp_list=[exp]

    file_exists=os.path.isfile('ExpenseTrack/exp_source.csv')
    with open('ExpenseTrack/exp_source.csv','a',newline='') as file:
        writer=csv.DictWriter(file,fieldnames=["Date", "Category", "Description", "Amount"])
        
        if not file_exists or os.stat('ExpenseTrack/exp_source.csv').st_size == 0:
            writer.writeheader()
        
        writer.writerows(exp_list)

# sort expense based on filedname
def sort(fieldname):
    with open('ExpenseTrack/exp_source.csv','r', newline='') as file:
        reader = csv.DictReader(file)
        data = list(reader)

        data.sort(key=lambda row: row[fieldname])

        for row in data:
            print(row)


# Execution part
addexp()
sort('Category')