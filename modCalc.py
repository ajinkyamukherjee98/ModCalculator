

import math
from tkinter import *
import tkinter as tk

window = tk.Tk() # creating a window
#window.geometry('800X600 + 400 + 300')
window.title("MODULO ARITHMETIC MADE EASY") # title of the windows
window.configure(background="white")


output = Text(window,width=75,height=6,wrap=WORD, background="White")
output.grid(row=9, column=0,columnspan=2, sticky=W)
def HCF(num1,num2):
    if num1<num2:
        return HCF(num2,num1)
    elif num1 % num2 == 0:
        return num2
    else:
        return HCF(num2,num1%num2)

# Function to check if number is coPrime or not
def coprime(num1,num2):
    return HCF(num1,num2)==1

# Function to get a list of number in Z*q
def EulerGroup(x):
    phiGroup=[]
    if x == 1:
        return 1
    else:
        for a in range(1, x):
            if coprime(x, a):
                phiGroup.append(a)
    #print (phiGroup)
    return phiGroup

# Function that returns the length of the current Euler Group
def EulerTot(num):
    print("Th eEuler length is: "+ str(len(EulerGroup(num))))
    return len(EulerGroup(num))

# Function to Calculate Prime Factors of a number and store them in a list
#factorList is the list that stores all its prime factors in the list
def primefactor(n):
    factorlist=[]
    while(n%2)==0:
        factorlist.append(2)
        n=n/2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i==0:
            factorlist.append(i)
            n=n/i
    if n>2:
        factorlist.append(n)

    return factorlist


def multipleOf(a, b):
    #res = 1
    for i in range (1, a):
        tot = b*i
        if a % tot == 0:
            return True
        else:
            return False



# Function to do Modulo arithmetic as per the cryptographic rules
# Modulo Exponnentitaion 
def modExponent(num1,num2,num3): 
    # we know that Eulers Totient is always even
    # we also know the group proeprty using Chinese remainder Theorem that any number raised to the number of objects in the group
    # will give us 1.
    num1 = num1.get()
    num2 = num2.get()
    num3 = num3.get()
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)

    power = primefactor(num2)
    for i in range(0, len(power)):
        # power = primefactor((num2))
        num1 = pow(num1, power[i]) % num3
    print("Else: " + str(num1))


    ## This code can be uncommented when using Chinese remainer theroem to find RSA Values
    ## An important group property: for any finite group G of order n, and g is any object of G, g**n =1
    ##if num2 >= EulerTot(num3):
      ##  tot = multipleOf(num2, EulerTot(num3))
       ## if tot == 1:
         ##   num1 = 1
           ## val = 0

        ##else:
         ##   val = num2 - math.floor(num2 / EulerTot(num2))
           ## for i in range(0, len(primefactor(val))):
             ##   power = primefactor(val)
               ## num1 = pow(num1, power[i]) % num3
            ##print("IF2: " + str(num1))
    ##else:
      ##  power = primefactor(num2)
        ##for i in range(0, len(power)):
          ##  # power = primefactor((num2))
            ##num1 = pow(num1, power[i]) % num3
        ##print("Else: " + str(num1))

    ##



    output.delete(0.0, END)
    output.insert(END, num1)
    return num1

# Function to generate Multiplicative Modulo inverse of a number
# num1 * itr = 1 mod num2
# Return Itr which is multiplicative Inverse of num1 while dividing with num2 resulting in 1 as reminader
def multInverse(num1,num2):
    for itr in range(1,num2):
        if((num1*itr)%num2) == 1:
            return itr
        else:
            continue

def printMod(num1,num2,num3):
    print(" The result is: "+ str(modExponent(num1,num2,num3)))

def main():

    # Photos
    pic1 = PhotoImage(file="xamodp.png")
    Label(window, image=pic1, bg="white").grid(row=0, column=5, sticky=E)

    # Create a label
    Label(window, text="Please Enter x, a and p as shown in the figure", bg="white", fg="Black", font="12").grid(row=1, column=0, sticky=E)

    x = Entry(window, width=20, text="x = ", font="12", fg="Black")
    x.grid(row=2, column=0, sticky=E)

    #x = int(x.get())

    a = Entry(window, width=20, text="a = ", font="12", fg="Black")
    a.grid(row=3, column=0, sticky=E)
    a.get()
    print(a.get())
    #a = int(a.get())
    p = Entry(window, width=20, text="p = ", font="12", fg="Black")
    p.grid(row=4, column=0, sticky=E)
    #p = int(p.get())


    # add a submit buttton
    bt = tk.Button(window, text="Submit", width="10", fg="Black", command=lambda: modExponent(x,a,p)).grid(row=7, column=0, sticky=E)

   # Create a textbox

    window.mainloop()

if __name__ == "__main__":
    main()
