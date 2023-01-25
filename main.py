from moduleCustomer import *
from moduleProduct import *
from AssignmentModule import *


flagproduct=0
flagcustomer=0
flagassign=0
while True:
    choice=input("1. Product Mamagememt \n2. Customer Management \n3. Product Assigned \n4.Exit: ")
    if choice=='1':
        print("Welcome to Product Management")
        menu=input("1.Add Record \t2.View \t3.Update \t4.Search \t5.Exit: ")
        if menu=='1':
            addProcut()
            flagproduct+=1

        elif menu=='2':
            if flagproduct>0:
                viewproduct()
            else:
                print("No Record Found")

        elif menu=='3':
            if flagproduct>0:
                updateproduct()
            else:
                print("NO Record Found")

        elif menu=='4':
            if flagproduct>0:
                searchproduct()
            else:
                print("No record Found!")

        elif menu=='5':
            print("Thanks For Using")
            break

        else:
            print("Invalid Input!")


    elif choice=='2':
        print("Welcome to Customer Management")
        menu = input("1.Add Customer \t2.View \t3.Update \t4.Search \t5.Exit")
        if menu == '1':
            addcustomer()
            flagcustomer += 1

        elif menu == '2':
            if flagcustomer > 0:
                viewCustomer()
            else:
                print("No Record Found")

        elif menu=='3':
            if flagcustomer > 0:
                updatecustomer()
            else:
                print("NO Record Found")

        elif menu=='4':
            if flagcustomer>0:
                searchC()
            else:
                print("No record Found")

        elif menu=='5':
            print("Thanks For Using")
            break

        else:
            print("Invalid Input!")

    elif choice=='3':
        print("Welcome to Product Assigning")
        choice1=input("1. Assign Product 2. View Assigned")
        if choice1=='1':
            if flagproduct>0 and flagcustomer>0:
                productassign()
                flagassign+=1
            else:
                print("No Record Found!")

        elif choice1=='2':
            if flagassign>0:
                viewassign()
            else:
                print("no Record Found!")



    elif choice=='4':
        break

    else:
        print("wrong input!")