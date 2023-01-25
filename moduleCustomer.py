customer=[]
def addcustomer():
    confirm='y'
    while confirm=='y':
        customer.append(input("Name of Customer: "))
        customer.append(eval(input("ID of Customer: ")))
        customer.append(eval(input("Age:: ")))
        confirm=(input("Press Y to add more: "))

def viewCustomer():
    print("Name \t\t ID \t\t Age")
    for i in range (0, len(customer),3):
        print(customer[i],"\t\t", customer[i+1],"\t\t", customer[i+2])


def searchC():
    confirm = 'y'
    while confirm=='y':
        searchP = input("Enter name of Customer you want to search: ")
        for i in range(0,len(customer)):
            if searchP == customer[i]:
                print("Name \t ID \t Age")
                print(customer[i],"\t",customer[i+1],"\t",customer[i+2])

        confirm = input("Press Y to Search Again: ")

def updatecustomer():
    print("You can Update Customer ID")
    confirm='y'
    while confirm=='y':
        choicecustomer=input("Enter name of Customer you want to update: ")
        for i in range (0,len(customer)):
            if choicecustomer==customer[i]:
                customer[i+1]=eval(input("Enter ID: "))

        confirm=input("Press Y to Update Again: ")