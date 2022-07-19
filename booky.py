# -*- coding: utf-8 -*-
import sqlite3
from bd import connexion
from bd2 import Create
from bd3 import Insertion
from bd4 import Lister
from BD8 import sup
contact={}
lischwa=[1,2,3,4,5,6]


while True :
    print("   ----------Booky----------")
    choix=input("\t1.Add contact\n\t2.Edit contact\n\t3.Delete contact\n\t4.Search contact\n\t5.Contact lists\n\t6.Exit\n\n\tMake a choice:\n\t ")
    choix=int(choix)
    if not  isinstance(choix,int):
            print("choice can't be a letter :")
            choix=input("1.Add contact\n2.Edit contact\n3.Delete contact\n4.Search contact\n5.Contact lists\n6.Exit\n\nMake a choice:\n ")
        
    while int(choix) not in lischwa:
        print("choice must be a number between 1 and 6  :")
        choix=input("1.Add contact\n2.Edit contact\n3.Delete contact\n4.Search contact\n5.Contact lists\n6.Exit\n\nMake a choice:\n ")
    
    if int(choix)==1:
        lischwa2 = [1,2]
        chwa=input("1.Add a new contact\n2.import a contact from google contact\n\nMake a choice :  ")
        chwa=int(chwa)
        if not isinstance (chwa,int):
            print("choice can be a letter")
            chwa=input("1.Add a new contact\n2.import a contact from google contact")
        while int(chwa) not in lischwa2:
            print("choice must be a number between 1 and 2  :")
            chwa=input("1.Add a new contact\n2.import a contact from google contact")
            
        if int (chwa)==1:
            fullname=input("Enter the fullname : ")
            number=input("Enter the phone number : ")
            email=input("Enter the mail : ")
            address=input("Enter the adress : ")
            connexion()
            Create()
            Insertion(fullname,number,email,address)
        if int(chwa)==2:
            pass
    if int(choix)==2  :
        pass
    if int(choix)==3  :
        name = input("Enter the fullname to delete :")
        sup(name)
    if int(choix)==4  :
        pass
    if int(choix)==5 :
        Lister()
        


    if int(choix)==6:
        break

    
        

