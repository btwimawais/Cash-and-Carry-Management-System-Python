product=[]
def addProcut():
    confirm='y'
    while confirm=='y':
        product.append(input("Enter Manufacturer: "))
        product.append(input("Enter Name of Product: "))
        product.append(eval(input("Enter Price: ")))
        product.append(eval(input("Enter Quantity:")))
        confirm=(input("Press Y to add more: "))

def viewproduct():
    print("Manufacturer \t Name \t Price \t Quantity")
    for i in range (0, len(product),4):
        print(product[i],"\t\t", product[i+1],"\t", product[i+2],"\t",product[i+3])



def searchproduct():
    confirm = 'y'
    while confirm=='y':
        searchP = input("Enter name of product you want to search: ")
        for i in range(0,len(product)):
            if searchP == product[i]:
                print("Manufacturer \t Name \t Price \t Quantity")
                print(product[i-1],"\t",product[i],"\t",product[i+1],"\t",product[i+2])

        confirm = input("Press Y to Search Again: ")

def updateproduct():
    print("You can Only Price")
    confirm='y'
    while confirm=='y':
        choiceproduct=input("Enter name of product you want to update: ")
        for i in range (0,len(product)):
            if choiceproduct==product[i]:
                product[i+1]=eval(input("Enter new price: "))
                confirm=input("Press Y to Update Again: ")