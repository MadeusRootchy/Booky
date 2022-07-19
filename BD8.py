# -*- coding: utf-8 -*-
import sqlite3
def sup(name) :
    try:
        conn = sqlite3.connect('BookyBase.db')
        cur = conn.cursor()
        print("Connexion réussie à SQLite")
        sql = "DELETE FROM contacts WHERE fullname = ?"
        fullname = name
        cur.execute(sql, (fullname, ))
        conn.commit()
        #pull up anglais bate a laaa
        print("Enregistrement supprimé avec succès")
    
        cur.close()
        conn.close()
        print("Connexion SQLite est fermée")

    except sqlite3.Error as error:
        print("Erreur lors du suppression dans la table Contacts", error)