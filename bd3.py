# -*- coding: utf-8 -*-
import sqlite3

def Insertion(fullname,number,email,address) :
    try:
        conn = sqlite3.connect('BookyBase.db')
        cur = conn.cursor()
        print("Connexion réussie à SQLite")

        cur.execute ("INSERT INTO contacts VALUES (?, ?, ?, ?);",(fullname,number,email,address))

        #conn = cur.execute(sql)
        conn.commit()
        print("Succesfully Enr")
        cur.close()
        conn.close()
        print("Connexion SQLite est fermée")

    except sqlite3.Error as error:
        print("Error", error)