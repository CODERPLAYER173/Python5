import time as t
customer_name = input("Enter the Customer Name: ")
Date = t.strftime("%d/%m/%Y")
medicine_amount = int(input("Enter the number of medicine : "))

for medicine in range(medicine_amount):
    medicine_name = input("Enter medicine name")
    medicine_cost = int(input("Enter medicine cost"))
    
