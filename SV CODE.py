#==========importation des modules=======================================================================================
import tkinter
from tkinter import *
import sqlite3
from typing import DefaultDict
import winsound
from tkinter import ttk
import time
from datetime import date, datetime
from sqlite3.dbapi2 import Date
import threading
from threading import Thread
from tkinter.constants import BOTH, TRUE, YES
from tkinter.filedialog import *
import tkinter as tk


class Code(tk.Tk):


    def __init__(self, root):
        #==========variables==================================================================================
        self.Chercher_par = StringVar()
        self.Chercher = StringVar()
        self.Nom = StringVar()
        self.Date = StringVar()
        self.Code = StringVar()
        self.ext = StringVar()
        self.ttx = IntVar()
        self.ttx = 15

        #==========fenêtre==================================================================================
        self.root=root
        self.root.geometry("1366x768")
        self.root.title("<<GS CODE>>")
        self.root.config(bg="black")
        #==========canvas==================================================================================
        can = Canvas(self.root,bg="black",bd='5')
        #==========label==================================================================================
        title = Label(can,text=" < <  G  .  S  .  C  .  O  .  D  .  E  > > ",bd=9,relief=RIDGE,font=("Roman",50,"bold"),bg="black",fg="red")
        title.pack(side=TOP,fill=X)
        #==========frame==================================================================================
        T=Frame(can,width=1000,height=560,bg="white",bd='2')
        T.place(x=3,y=106)
        self.entry = Text(T,wrap=WORD,bg="#F9DDA4",font=("popping",self.ttx))
        self.entry.pack(fill=BOTH,expand=TRUE)
        #==========frame2==================================================================================
        T2=Frame(can,relief=RIDGE,bg="black",bd='2')
        T2.place(x=900,y=106,width=462,height=560)
        #==========headings==================================================================================
        scroll_x2 = Scrollbar(T2,orient=HORIZONTAL)
        scroll_y2 = Scrollbar(T2,orient=VERTICAL)
        pg = ttk.Treeview(T2,column=("DATE","NOM","CODE","EXTANSION"),xscrollcommand=scroll_x2.set,yscrollcommand=scroll_y2.set)
        scroll_x2.pack(side=BOTTOM,fill=X)
        scroll_y2.pack(side=RIGHT,fill=Y)
        scroll_x2.config(command= pg.xview)
        scroll_y2.config(command= pg.yview)

        pg.heading("DATE", text="DATE")
        pg.heading("NOM", text="NOM")
        pg.heading("CODE", text="CODE")
        pg.heading("EXTANSION", text="EXTANSION")
        pg['show']='headings'

        pg.column("DATE", width=90)
        pg.column("NOM", width=90)
        pg.column("CODE", width=450)
        pg.column("EXTANSION", width=20)
        pg.pack(fill=BOTH,expand=1)
        #==========frame3==================================================================================
        en=Frame(can,width='300',height='90',bg="black")
        en.place(x=3,y=680)
        #==========fonctions================================================================================
        def D_T():
            now = datetime.now()
            heur=now.strftime("%d-%m-%Y %H:%M:%S")
            self.Date.set(heur)


        def get_cursor(ev):
            cursor_row=pg.focus()
            contents=pg.item(cursor_row)
            row = contents['values']
            self.Date.set(row[0])
            self.Nom.set(row[1])
            self.entry.delete("1.0",END)
            self.entry.insert(END,row[2])
            self.ext.set(row[3])      
        pg.bind('<ButtonRelease-1>',get_cursor)

        def SFile():
            nf= asksaveasfile(mode='w',filetype=[('text files(*.txt)','*.txt'),('Python(*.py*)','*.py*'),('All File(*.*)','*.*')])
            if nf is None:
                return
            text = str(self.entry.get('1.0', END))
            nf.write(text)
            nf.close()
        content=""
        def OFile():
            CFile()
            D_T()
            file= askopenfile(mode='r',filetype=[('text files(*.txt)','*.txt'),('Python(*.py*)','*.py*'),('All(*.*)','*.*')])
            if file is not None:
                content = file.read()
            self.entry.insert(INSERT,content)

        def CFile():
            self.entry.delete('1.0',END)
            D_T()
            self.Chercher_par.set("")
            self.Chercher.set("")
            self.Nom.set("")
            self.Date.set("")
            self.Code.set("")
            self.ext.set("")
            self.ttx = 15           

        def afficher():
            conn = sqlite3.connect("CD.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM codesave")
            rows= cur.fetchall()
            if len(rows)!=0:
                pg.delete(*pg.get_children())
                for row in rows:
                    pg.insert('',END,values=row)
                conn.commit()
            conn.close()

        def afficher_1():
            Cherche = self.Chercher.get()
            Chercher_pa = self.Chercher_par.get()
            conn = sqlite3.connect("CD.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM codesave WHERE "+Chercher_pa+" LIKE '%"+Cherche+"%'")
            rows= cur.fetchall()
            if len(rows)!=0:
                pg.delete(*pg.get_children())
                for row in rows:
                    pg.insert('',END,values=row)
                conn.commit()
            conn.close()

        def supp():
            nom = self.Nom.get()
            conn = sqlite3.connect("CD.db")
            cur = conn.cursor()
            cur.execute("DELETE FROM codesave WHERE NOM=?",(nom))
            conn.commit()
            conn.close()
            afficher()


        def maj():
            DD=self.Date.get()
            nom = self.Nom.get()
            ex =self.ext.get()
            code = str(self.entry.get('1.0', END))
            conn = sqlite3.connect("CD.db")
            cur = conn.cursor()
            cur.execute("UPDATE codesave SET DATE=? ,CODE=? ,EX=? WHERE NOM=?",(DD,code,ex,nom))                 
            conn.commit()
            conn.close()
            afficher()


        def addcd():
            text = str(self.entry.get('1.0', END))
            if text is not None:
                DD=self.Date.get()
                nom = self.Nom.get()
                code = str(self.entry.get('1.0', END))
                ex = self.ext.get()
                conn = sqlite3.connect("CD.db")
                cur = conn.cursor()
                create = "CREATE TABLE  IF NOT EXISTS codesave ( DATE VARCHAR(20) PRIMARY KEY,NOM VARCHAR(20) ,CODE VARCHAR(100000000),EX VARCHAR(20));"
                insert = "INSERT INTO codesave VALUES (?,?,?,?)"
                donnees = [(DD,nom,code,ex),]
                cur.execute(create)
                for donnee in donnees:
                    cur.execute(insert,donnee)               
                conn.commit()
                conn.close()
                afficher()
                CFile()
                D_T()
        afficher()
        #==========boutons==================================================================================
        Label(en,text="DATE",bg="black",fg="white",font=("times new roman",10)).grid(row=0,column=0,pady=5,padx=10,sticky="W")
        Entry(en,textvariable=self.Date,font=("times new roman",10),width=10,bd=2,relief=GROOVE).grid(row=0,column=1,pady=5,padx=10,sticky="W")
        Label(en,text="NOM",bg="black",fg="white",font=("times new roman",10)).grid(row=0,column=2,pady=5,padx=10,sticky="W")
        Entry(en,textvariable=self.Nom,font=("times new roman",10),width=10,bd=2,relief=GROOVE).grid(row=0,column=3,pady=5,padx=10,sticky="W")
        Label(en,text="EXT.",bg="black",fg="white",font=("times new roman",10)).grid(row=0,column=4,pady=5,padx=10,sticky="W")
        Entry(en,textvariable=self.ext,font=("times new roman",10),width=5).grid(row=0,column=5,pady=5,padx=10,sticky="W")
        Button(en, text="Nouveau" , bg="red",fg="white",command=addcd).grid(row=0,column=6,padx=5,pady=10)
        Button(en,text="Afficher" ,bg="red",fg="white",width=7,command=afficher).grid(row=0,column=7,padx=5,pady=10)
        Button(en, text="Mise à jour" , bg="red",fg="white",command=maj).grid(row=0,column=8,padx=5,pady=10)
        Label(en,text="Rechercher par ...",bg="black",fg="white",font=("times new roman",10),relief=GROOVE).grid(row=0,column=9,padx=5,pady=10)
        combo_search = ttk.Combobox(en,textvariable=self.Chercher_par,font=("times new roman",10),width=15)
        combo_search['values']=("DATE","NOM","INDICE","EX")
        combo_search.grid(row=0,column=10,pady=5,padx=10,sticky="W")
        Entry(en,textvariable=self.Chercher,font=("times new roman",10),width=10,bd=2,relief=GROOVE).grid(row=0,column=11,pady=10,padx=20,sticky="W")
        Button(en,text="Rechercher",bg="red",fg="white",width=7,command=afficher_1).grid(row=0,column=12,padx=5,pady=10)
        Button(en, text="Supprimer" , bg="red",fg="white",command=supp).grid(row=0,column=13,padx=5,pady=10)
        Button(en, text="Nettoyer" , bg="red",fg="white",command=CFile).grid(row=0,column=14,padx=5,pady=10)
        Label(en,text="Taille",bg="black",fg="white",font=("times new roman",10),relief=GROOVE).grid(row=0,column=15,padx=5,pady=10)
        combo_search = ttk.Combobox(en,textvariable=self.ttx,font=("times new roman",10),width=15)
        combo_search['values']=(9,10,11,12,13,14,15,16,17,18,19,20)
        combo_search.grid(row=0,column=16,pady=5,padx=10,sticky="W")
        D_T()
        menu_bar=Menu(self.root)
        file_menu=Menu(menu_bar,tearoff=0)
        file_menu.add_command(label="importer",command=OFile)
        file_menu.add_command(label="exporter",command=SFile)
        file_menu.add_command(label="Quitter", command=root.destroy)
        menu_bar.add_cascade(label="Options", menu=file_menu)
        self.root.config(menu=menu_bar)
        th1 = threading.Thread(target=D_T)
        th1.start()
        can.pack(expand=TRUE,fill=BOTH)



#==========fenêtre==================================================================================
root=tk.Tk()
object= Code(root)
root.call('wm', 'iconphoto', root,PhotoImage(file='D.png'))
root.mainloop()
