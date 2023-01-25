from moduleProduct import *
from moduleCustomer import *

p_assign=[]

def productassign():
    pname=input("Enter Product name:")
    if pname in product:
        cid=eval(input("Enter Customer ID:"))
        if cid in customer:
            p_assign.append(pname)
            p_assign.append(cid)
            print("Assigned Sucessfully")


def viewassign():
    for i in range (0, len(p_assign),2):

        print("Product",p_assign[i],"\t", "Customer ID",p_assign[i+1])