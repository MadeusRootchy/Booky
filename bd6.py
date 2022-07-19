# -*- coding: utf-8 -*-
import sqlite3
def MAJ(fullname,number,email,address):
    try:
        conn = sqlite3.connect('my.db')
        cur = conn.cursor()
        print("Connexion réussie à SQLite")

        sql = "UPDATE contacts SET address = ? WHERE fullname = ?"
        value = (address,fullname )
        cur.execute(sql, value)
        #sql = "UPDATE contacts SET address = ? WHERE fullname = ?"

        cur.execute(sql)
        conn.commit()
        print("Enregistrement mis à jour avec succès")
    
        cur.close()
        conn.close()
        print("Connexion SQLite est fermée")

    except sqlite3.Error as error:
        print("Erreur lors du mis à jour dans la table person", error)