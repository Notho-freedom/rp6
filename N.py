import pymysql
from tkinter import *
import tkinter as tk
from tkinter import ttk
import time
import winsound
from datetime import datetime
import threading
from threading import Thread


def apropos():
    app=tk.Toplevel()
    app.geometry("700x500+0+0")
    app.resizable(0,0)
    app.title("HT-Apropos")
    Label(app,text="APROPOS",fg="white",bg="#4065a4",font=("times new roman",15,"bold"),bd=1).pack(side=TOP,fill=X)
    Label(app,text=" H . A . N . T . A  à été programmer en python 3.9 par #Notho.\n Ses objectifs sont non défini pour le moment, mais il vous surviendrat tres certainement à vos besoins\n Genesis vous remerci!").place(x=50,y=250)
    winsound.PlaySound("E:\\balk\\Balabolka\\sounds\\timer.wav",winsound.SND_ASYNC)
    app.mainloop()





class hanta(tk.Tk):


    def __init__(self, root):

        self.root=root
        self.root.geometry("1360x768+0+0")
        self.root.title("CyberX")
        title = Label(self.root,text="=  = H . A . N . T . A  =  =",bd=9,relief=GROOVE,font=("Roman",40,"bold"),bg="black",fg="red").pack(side=TOP,fill=X)
        label2 = tk.Label(self.root, text="""this is ef_g closing this will not affect root""").place(x=500,y=90)

        #variables
        self.Id = StringVar()
        self.Nomc = StringVar()
        self.heure = StringVar()
        self.heur = IntVar()
        self.min = IntVar()
        self.Addresse = StringVar()
        self.Dett = IntVar()
        Temps_a = IntVar()
        self.DD = StringVar()
        self.tach = IntVar()
        self.tr = IntVar()
        self.nser = StringVar()
        self.vf = StringVar()
        self.vff = StringVar()
        self.Chercher_par = StringVar()
        self.Chercher = StringVar()
        #frame gauche
        f_g= Frame(self.root, width=350,height=700,bg="#4065a4",bd=4,relief=GROOVE).place(x=0,y=80)
        f_g1= Frame(f_g, width=342,height=40,bg="white",bd=4).place(x=3,y=85)
        Label(f_g1,text="= = M.E.N.U = =",fg="black",bg="white",font=("times new roman",15,"bold"),bd=0).place(x=120,y=93)
        f_g2= Frame(f_g, width=345,height=4,bg="red",bd=4).place(x=4,y=390)




        def NETf():
            ax=self.vf.get()
            bx=self.vff.get()
            if ax!="" and bx!="":
                self.vf.set(" ")
                self.vff.set(" ")
            else:
                if ax != '':
                    self.vf.set(" ")
                else:
                    self.vff.set(" ")




        def D_T():
            dt=''
            now = datetime.now()
            heur=now.strftime("%H:%M:%S")
            hr=str(heur[0])+str(heur[1])
            mn=str(heur[3])+str(heur[4])
            self.heur.set(hr)
            self.min.set(mn)
            self.heure.set(heur)
            heur=now.strftime("%d-%m-%Y %H:%M:%S")
            for i in range(10):
                dt=dt+str(heur[i])
            self.DD.set(dt)
            self.tach.set(1)
            heur=now.strftime("%H:%M:%S")
            tk.Label(f_g,text=("Heure("+heur+")"),fg="white",bg="#4065a4",font=("times new roman",10,"bold"),bd=0).place(x=200,y=420)
            heur=now.strftime("%H%M%S")
            cl=str("client")+str(heur)
            self.Nomc.set(cl)
            heur=now.strftime("%d%m%Y%H%M%S")
            self.Id.set(heur)
            self.nser.set("Serveur0")
            NETf()
            winsound.PlaySound("E:\\balk\\Balabolka\\sounds\\clipboard.wav",winsound.SND_ASYNC)


        def convtim():
            heur = self.heur.get()
            min = self.min.get()
            tach = int(self.tach.get())
            e=0
            for i in range(60):
                e = e + heur
            e = e + min
            x=0
            for i in range(60):
                x= x + tach
            e= e + x
            d1=int(e/60)
            d2=float((e/60)-d1)
            t0=d2
            for i in range(60):
                d2=d2+t0
            d2=int(d2)
            s=str(d1)+"h"+str(d2)+"min"
            self.vf.set("")
            D="Fin de session: ("+s+")"
            self.vf.set(D)
            s=str(d1)+"h"+str(d2)+"m "
            return s

        tb_F = Frame(self.root,bd=1,relief=RIDGE,bg="white")

        tb_F.place(x=350,y=85,width=670,height=545) 


        scroll_x = Scrollbar(tb_F,orient=HORIZONTAL)
        scroll_y = Scrollbar(tb_F,orient=VERTICAL)

        self.st = ttk.Treeview(tb_F,column=("ID","Nomc","Temps_Acheter","Temps_restant","DD","Heure","Addresse","Servir_par","Dette"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command= self.st.xview)
        scroll_y.config(command= self.st.yview)

        self.st.heading("ID", text="ID")
        self.st.heading("Nomc", text="Nomc")
        self.st.heading("Temps_Acheter", text="Temps_Acheter")
        self.st.heading("Temps_restant", text="Temps_restant")
        self.st.heading("DD", text="DD")
        self.st.heading("Heure", text="Heure")
        self.st.heading("Addresse", text="Addresse")
        self.st.heading("Servir_par", text="Servir_par")
        self.st.heading("Dette", text="Dette")

        self.st['show']='headings'
        self.st.column("ID", width=100)
        self.st.column("Nomc", width=150)
        self.st.column("Temps_Acheter", width=50)
        self.st.column("Temps_restant", width=50)
        self.st.column("DD", width=100)
        self.st.column("Heure", width=90)
        self.st.column("Addresse", width=100)
        self.st.column("Servir_par", width=150)
        self.st.column("Dette", width=60)
        self.st.pack(fill=BOTH,expand=1)
        
        #bd
        f_gd= Frame(self.root, width=350,height=700,bg="#4065a4",bd=4,relief=GROOVE).place(x=1020,y=80)
        Label(f_gd,text="= = P.R.O.G.R.E.S.S.I.O.N = =",fg="black",bg="white",font=("times new roman",15,"bold"),bd=4).place(x=1025,y=83,width=350,height=40)


        def NETTOYER():
            self.Nomc.set("")
            self.heur.set("")
            self.min.set("")
            self.DD.set("")
            self.tach.set("")
            self.nser.set("")
            self.Id.set("")
            self.Addresse.set("")
            self.vf.set("")
            self.vff.set("")
            self.Chercher.set("")
            self.Chercher_par.set("")
            self.Dett.set("")
            winsound.PlaySound("E:\\balk\\Balabolka\\sounds\\clipboard.wav",winsound.SND_ASYNC)

        def affich_1():
            Chercher = self.Chercher.get()
            Chercher_par = self.Chercher_par.get()

            conn = pymysql.connect(host="localhost", user="root",passwd="",database="hanta_db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM Client WHERE "+Chercher_par+" LIKE '%"+Chercher+"%'")
            rows=cur.fetchall()
            if len(rows)!=0:
                self.st.delete(*self.st.get_children())
                for row in rows:
                    self.st.insert('',END,values=row)
                conn.commit()
            conn.close()
            winsound.PlaySound("E:\\balk\\Balabolka\\sounds\\clipboard.wav",winsound.SND_ASYNC)


        def afficher():
            conn = pymysql.connect(host="localhost", user="root",passwd="",database="hanta_db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM Client")
            rows= cur.fetchall()
            if len(rows)!=0:
                self.st.delete(*self.st.get_children())
                for row in rows:
                    self.st.insert('',END,values=row)
                conn.commit()
            conn.close()
            winsound.PlaySound("E:\\balk\\Balabolka\\sounds\\clipboard.wav",winsound.SND_ASYNC)
            
        afficher()
        self.y = IntVar()
        self.y=100
        self.i = IntVar()
        self.i =1
        dic_pro={}
        self.val ={}
        self.p = {}
        
        def get_cursor(ev):
            cursor_row= self.st.focus()
            contents= self.st.item(cursor_row)
            row = contents['values']
            self.Id.set(row[0])
            self.Nomc.set(row[1])
            self.tach.set(row[2])
            self.tr.set(row[3])
            self.DD.set(row[4])
            self.vf.set(row[5])
            self.Addresse.set(row[6])
            self.nser.set(row[7])
            self.Dett.set(row[8])        
        self.st.bind('<ButtonRelease-1>',get_cursor)

        def addcl():
            T_a=self.tach.get()
            Nomc=self.Nomc.get()
            T_r=self.tr.get()
            heur=self.heur.get()
            min=self.min.get()
            Addresse= self.Addresse.get()
            Servir_par=self.nser.get()
            Dette=self.Dett.get()
            id=self.Id.get()
            DD=self.DD.get()
            Heure=str(heur)+"h"+str(min)+"min"
            if (T_a !=0):
                if len(Servir_par) !=0:
                    conn = pymysql.connect(host="localhost", user="root",passwd="",database="hanta_db")
                    cur = conn.cursor()
                    create = "CREATE TABLE  IF NOT EXISTS Client ( ID VARCHAR(20) PRIMARY KEY,Nomc VARCHAR(20) ,Temps_Acheter INTEGER NOT NULL,Temps_restant INTEGER,DD DATE,Heure INTEGER,Addresse VARCHAR(20),Servir_par VARCHAR(30),Dette INTEGER);"
                    insert = "INSERT INTO Client VALUES (?,?,?,?,?,?,?,?,?)"
                    donnees = [(id,Nomc,T_a,T_r,DD,Heure,Addresse,Servir_par,Dette),]
                    cur.execute(create)
                    for donnee in donnees:
                        cur.execute(insert,donnee)
                    conn.commit()
                    conn.close()
                    convtim()
                    winsound.PlaySound("E:\\balk\\Balabolka\\sounds\\finish.wav",winsound.SND_ASYNC)
                    afficher()
                    
                    def bar():
                            T_a = self.tach.get()
                            dic_pro[self.i] = ttk.Progressbar(f_gd,length=230,mode='determinate')
                            dic_pro[self.i].place(x=1113,y=self.y)

                            label2l=Label(f_gd,font=("times new roman",10,"bold"),bg="#4065a4",fg="white")
                            label2l.place(x=1323,y=self.y,width=35,height=23)

                            label2nl=Label(f_gd,font=("times new roman",10,"bold"),text=self.Nomc.get()+":",bg="#4065a4",fg="white")
                            label2nl.place(x=1024,y=self.y,width=95,height=23)
                            k=self.y - 25
                            kh=" DS: "+str(heur)+"h"+str(min)+"m "
                            khf= convtim()
                            khf = " FS: "+khf
                            Label(f_gd,font=("times new roman",10,"bold"),text=(kh,self.Id.get(),khf),bg="black",fg="red").place(x=1070,y=k,width=280,height=23)

                            T_a*=60

                            if self.i == 1:
                                dic_pro[1]['value']=0
                                dic_pro[1]['maximum']=T_a+1                                      
                                for self.val[1] in range(1,T_a+1,1):
                                    dic_pro[1]['value']=self.val[1]
                                    self.p[1]=self.val[1]
                                    self.p[1]/=T_a
                                    self.p[1]=int(self.p[1]*100)
                                    self.root.update_idletasks()
                                    time.sleep(1)
                                    label2l.config(text=str(self.p[1])+"%")
                                    dic_pro[1]['value']=T_a+1
                                winsound.PlaySound("to.wav",winsound.SND_ASYNC)
                            else:
                                if self.i ==2:
                                    dic_pro[2]['value']=0
                                    dic_pro[2]['maximum']=T_a+1                                                
                                    for self.val[2] in range(1,T_a+1,1):
                                        dic_pro[2]['value']=self.val[2]
                                        self.p[2]=self.val[2]
                                        self.p[2]/=T_a
                                        self.p[2]=int(self.p[2]*100)
                                        self.root.update_idletasks()
                                        time.sleep(1)
                                        label2l.config(text=str(self.p[2])+"%")
                                        dic_pro[2]['value']=T_a+1
                                    winsound.PlaySound("to.wav",winsound.SND_ASYNC)
                                else:
                                    if self.i ==3:
                                        dic_pro[3]['value']=0
                                        dic_pro[3]['maximum']=T_a+1                                                
                                        for self.val[3] in range(1,T_a+1,1):
                                            dic_pro[3]['value']=self.val[3]
                                            self.p[3]=self.val[3]
                                            self.p[3]/=T_a
                                            self.p[3]=int(self.p[3]*100)
                                            self.root.update_idletasks()
                                            time.sleep(1)
                                            label2l.config(text=str(self.p[3])+"%")
                                        dic_pro[3]['value']=T_a+1
                                        winsound.PlaySound("to.wav",winsound.SND_ASYNC)
                                    else:
                                        if self.i ==4:
                                            dic_pro[4]['value']=0
                                            dic_pro[4]['maximum']=T_a+1                                                
                                            for self.val[4] in range(1,T_a+1,1):
                                                dic_pro[4]['value']=self.val[4]
                                                self.p[4]=self.val[4]
                                                self.p[4]/=T_a
                                                self.p[4]=int(self.p[4]*100)
                                                self.root.update_idletasks()
                                                time.sleep(1)
                                                label2l.config(text=str(self.p[4])+"%")
                                            dic_pro[4]['value']=T_a+1
                                            winsound.PlaySound("to.wav",winsound.SND_ASYNC)
                                        else:
                                            if self.i ==5:
                                                dic_pro[5]['value']=0
                                                dic_pro[5]['maximum']=T_a+1                                                
                                                for self.val[5] in range(1,T_a+1,1):
                                                    dic_pro[5]['value']=self.val[5]
                                                    self.p[5]=self.val[5]
                                                    self.p[5]/=T_a
                                                    self.p[5]=int(self.p[5]*100)
                                                    self.root.update_idletasks()
                                                    time.sleep(1)
                                                    label2l.config(text=str(self.p[5])+"%")
                                                dic_pro[5]['value']=T_a+1
                                                winsound.PlaySound("to.wav",winsound.SND_ASYNC)
                                            else:
                                                if self.i ==6:
                                                    dic_pro[6]['value']=0
                                                    dic_pro[6]['maximum']=T_a+1                                                
                                                    for self.val[6] in range(1,T_a+1,1):
                                                        dic_pro[6]['value']=self.val[6]
                                                        self.p[6]=self.val[6]
                                                        self.p[6]/=T_a
                                                        self.p[6]=int(self.p[6]*100)
                                                        self.root.update_idletasks()
                                                        time.sleep(1)
                                                        label2l.config(text=str(self.p[6])+"%")
                                                    dic_pro[6]['value']=T_a+1
                                                    winsound.PlaySound("to.wav",winsound.SND_ASYNC)
                                                else:
                                                    if self.i ==7:
                                                        dic_pro[7]['value']=0
                                                        dic_pro[7]['maximum']=T_a+1                                                
                                                        for self.val[7] in range(1,T_a+1,1):
                                                            dic_pro[7]['value']=self.val[7]
                                                            self.p[7]=self.val[7]
                                                            self.p[7]/=T_a
                                                            self.p[7]=int(self.p[7]*100)
                                                            self.root.update_idletasks()
                                                            time.sleep(1)
                                                            label2l.config(text=str(self.p[7])+"%")
                                                        dic_pro[7]['value']=T_a+1
                                                        winsound.PlaySound("to.wav",winsound.SND_ASYNC)
                                                    else:
                                                        if self.i ==8:
                                                            dic_pro[8]['value']=0
                                                            dic_pro[8]['maximum']=T_a+1                                                
                                                            for self.val[8] in range(1,T_a+1,1):
                                                                dic_pro[8]['value']=self.val[8]
                                                                self.p[8]=self.val[8]
                                                                self.p[8]/=T_a
                                                                self.p[8]=int(self.p[8]*100)
                                                                self.root.update_idletasks()
                                                                time.sleep(1)
                                                                label2l.config(text=str(self.p[8])+"%")
                                                            dic_pro[8]['value']=T_a+1
                                                            winsound.PlaySound("to.wav",winsound.SND_ASYNC)
                                                        else:
                                                            if self.i ==9:
                                                                dic_pro[9]['value']=0
                                                                dic_pro[9]['maximum']=T_a+1              
                                                                for self.val[9] in range(1,T_a+1,1):
                                                                    dic_pro[9]['value']=self.val[9]
                                                                    self.p[9]=self.val[9]
                                                                    self.p[9]/=T_a
                                                                    self.p[9]=int(self.p[9]*100)
                                                                    self.root.update_idletasks()
                                                                    time.sleep(1)
                                                                    label2l.config(text=str(self.p[9])+"%")
                                                                dic_pro[9]['value']=T_a+1
                                                                winsound.PlaySound("to.wav",winsound.SND_ASYNC)
                                                            else:
                                                                if self.i ==10:
                                                                    dic_pro[10]['value']=0
                                                                    dic_pro[10]['maximum']=T_a+1                                                
                                                                    for self.val[10] in range(1,T_a+1,1):
                                                                        dic_pro[10]['value']=self.val[10]
                                                                        self.p[10]=self.val[10]
                                                                        self.p[10]/=T_a
                                                                        self.p[10]=int(self.p[10]*100)
                                                                        self.root.update_idletasks()
                                                                        time.sleep(1)
                                                                        label2l.config(text=str(self.p[10])+"%")
                                                                    dic_pro[10]['value']=T_a+1
                                                                    winsound.PlaySound("to.wav",winsound.SND_ASYNC)
                                                                else:
                                                                    if self.i ==11:
                                                                        dic_pro[11]['value']=0
                                                                        dic_pro[11]['maximum']=T_a+1                                                
                                                                        for self.val[11] in range(1,T_a+1,1):
                                                                            dic_pro[11]['value']=self.val[11]
                                                                            self.p[11]=self.val[11]
                                                                            self.p[11]/=T_a
                                                                            self.p[11]=int(self.p[11]*100)
                                                                            self.root.update_idletasks()
                                                                            time.sleep(1)
                                                                            label2l.config(text=str(self.p[11])+"%")
                                                                        dic_pro[11]['value']=T_a+1
                                                                        winsound.PlaySound("to.wav",winsound.SND_ASYNC)
                                                                    else:                                                                        
                                                                        if self.i ==12:
                                                                            dic_pro[12]['value']=0
                                                                            dic_pro[12]['maximum']=T_a+1              
                                                                            for self.val[12] in range(1,T_a+1,1):
                                                                                dic_pro[12]['value']=self.val[12]
                                                                                self.p[12]=self.val[12]
                                                                                self.p[12]/=T_a
                                                                                self.p[12]=int(self.p[12]*100)
                                                                                self.root.update_idletasks()
                                                                                time.sleep(1)
                                                                                label2l.config(text=str(self.p[12])+"%")
                                                                            dic_pro[12]['value']=T_a+1
                                                                            winsound.PlaySound("to.wav",winsound.SND_ASYNC)
                    th1 = threading.Thread(target=bar)
                    th1.start()
                    self.y=self.y + 50
                    self.i = self.i + 1                               
                else:
                    winsound.PlaySound("Windows Hardware Fail.wav",winsound.SND_ASYNC)
                    NETf()
                    self.vf.set("Veillez inscrire votre nom de service!!")             
            else:
                winsound.PlaySound("Windows Hardware Fail.wav",winsound.SND_ASYNC)
                NETf()
                self.vff.set("Le temps_acheter ne peut pas être null")

        def supp():
            Chercher = self.Chercher.get()
            Chercher_par = self.Chercher_par.get()
            conn = pymysql.connect(host="localhost", user="root",passwd="",database="hanta_db")
            cur = conn.cursor()
            cur.execute("DELETE FROM Client WHERE "+Chercher_par+" LIKE '%"+Chercher+"%'")
            conn.commit()
            conn.close()
            afficher()




        def maj():
            T_a=self.tach.get()
            Nomc=self.Nomc.get()
            T_r=self.tr.get()
            heur=self.heur.get()
            min=self.min.get()
            Addresse= self.Addresse.get()
            Servir_par=self.nser.get()
            Dette=self.Dett.get()
            id=self.Id.get()
            DD=self.DD.get()
            Heure=str(heur)+"h"+str(min)+"min"
            if (T_a !=0):
                if len(Servir_par) !=0:
                    conn = pymysql.connect(host="localhost", user="root",passwd="",database="hanta_db")
                    cur = conn.cursor()
                    cur.execute("UPDATE Client SET Nomc=? ,Temps_Acheter=? ,Temps_restant=? ,DD=? ,Heure=? ,Addresse=? ,Servir_par=? ,Dette=?  WHERE ID=?",(Nomc,T_a,T_r,DD,Heure,Addresse,Servir_par,Dette,id))
                    conn.commit()
                    conn.close()
                    afficher()
  
        #suite_framg
        Label(f_g,text="Date",fg="white",bg="#4065a4",font=("times new roman",11,"bold"),bd=2).place(x=7,y=420)
        Entry(f_g,textvariable=self.DD,font=("times new roman",10),bd=2).place(x=7,y=440)
        mf=Frame(f_g,relief=RIDGE,bg="#4065a4").place(x=200,y=440,width=125,height=17) 
        Entry(mf,textvariable=self.heur,font=("times new roman",10),bd=1,bg="white").place(x=200,y=440,width=30,height=19)
        Label(f_g,text="h",fg="white",bg="#4065a4",font=("times new roman",11,"bold"),bd=2).place(x=220,y=438,width=25)
        Entry(mf,textvariable=self.min,font=("times new roman",10),bd=1,bg="white").place(x=245,y=440,width=20,height=19)
        Label(f_g,text="min",fg="white",bg="#4065a4",font=("times new roman",11,"bold"),bd=2).place(x=264,y=438,width=30)

        Label(f_g,text="Nomc",fg="white",bg="#4065a4",font=("times new roman",11,"bold"),bd=2).place(x=7,y=475)
        Label(f_g,text="Temps_Acheter(h)",fg="white",bg="#4065a4",font=("times new roman",11,"bold"),bd=2).place(x=200,y=475)
        Entry(f_g,textvariable=self.Nomc,font=("times new roman",10),bd=2).place(x=7,y=495)
        Entry(f_g,textvariable=self.tach,font=("times new roman",10),bd=2).place(x=200,y=495)
        Label(f_g,text="Servir_par",fg="white",bg="#4065a4",font=("times new roman",11,"bold"),bd=2).place(x=7,y=530)
        Entry(f_g,textvariable=self.nser,font=("times new roman",10),bd=2).place(x=7,y=550)

        Label(f_g,text="ID",fg="white",bg="#4065a4",font=("times new roman",11,"bold"),bd=2).place(x=200,y=530)
        Entry(f_g,textvariable=self.Id,font=("times new roman",10),bd=2).place(x=200,y=550)
    
        Label(f_g,text="Addresse",fg="white",bg="#4065a4",font=("times new roman",11,"bold"),bd=2).place(x=7,y=575)
        Entry(f_g,textvariable=self.Addresse,font=("times new roman",10),bd=2).place(x=7,y=595)

        Label(f_g,text="Dette",fg="white",bg="#4065a4",font=("times new roman",11,"bold"),bd=2).place(x=200,y=575)
        Entry(f_g,textvariable=self.Dett,font=("times new roman",10),bd=2).place(x=200,y=595)

        #========Fram_down=======
        dt_F = Frame(self.root,bd=0,relief=RIDGE,bg="#4065a4")
        dt_F.place(x=347,y=630,width=675,height=100)

        Label(dt_F,text="Chercher par...",bg="#4065a4",fg="white",font=("times new roman",15)).grid(row=0,column=0,pady=10,padx=20,sticky="W")
        combo_search = ttk.Combobox(dt_F,textvariable=self.Chercher_par,font=("times new roman",10),width=15)
        combo_search['values']=("ID","Nomc","Temps_Acheter","Temps_restant","DD","Heure","Addresse","Servir_par","Dette")
        combo_search.grid(row=0,column=1,pady=10,padx=20,sticky="W")
        Entry(dt_F,textvariable=self.Chercher,font=("times new roman",10),width=15,bd=2,relief=GROOVE).grid(row=0,column=2,pady=10,padx=20,sticky="W")
        Button(dt_F,text="Rechercher",bg="#4065a4",fg="white",width=7,command=affich_1).grid(row=0,column=3,padx=5,pady=10)
        Button(dt_F,text="Afficher" ,bg="#4065a4",fg="white",width=7,command=afficher).grid(row=0,column=4,padx=5,pady=10)
        Button(dt_F, text="Supprimer" , bg="#4065a4",fg="white",command=supp).grid(row=0,column=5,padx=5,pady=10)
        Button(dt_F, text="Mise à jour" , bg="red",fg="white",command=maj).grid(row=1,column=2,padx=5,pady=10)
        Button(dt_F, text="Nouveau" , bg="red",fg="white",command=addcl).grid(row=1,column=3,padx=5,pady=10)
        Button(dt_F, text="Nettoyer" , bg="red",fg="white",command=NETTOYER).grid(row=1,column=4,padx=5,pady=10)
        Button(dt_F, text="Actualiser" , bg="red",fg="white",command=D_T).grid(row=1,column=5,padx=5,pady=10)  
        #frame droite
        Label(f_g,text="Temps restant",fg="white",bg="#4065a4",font=("times new roman",11,"bold"),bd=2).place(x=7,y=620)
        Entry(f_g,textvariable=self.tr,font=("times new roman",10),bd=2).place(x=7,y=640)
        f_g2= Frame(f_g, width=342,height=50,bg="#4065a4",bd=4).place(x=3,y=660)
        Entry(f_g2,textvariable=self.vf,font=("times new roman",10),bd=0,bg="#4065a4",fg="red").place(x=30,y=690,width=290,height=15)
        Entry(f_g2,textvariable=self.vff,font=("times new roman",10),bd=0,bg="#4065a4",fg="red").place(x=30,y=665,width=250,height=15)
        D_T()













class hant(tk.Tk):
    winsound.PlaySound("wc.wav",winsound.SND_ASYNC)
    root=tk.Tk()
    object= hanta(root)
    root.tk.call('wm','iconphoto', root._w,tk.PhotoImage(file='B2.png'))
    menu_bar=Menu(root)
    file_menu=Menu(menu_bar,tearoff=0)
    file_menu.add_command(label="Apropos",command=apropos)
    file_menu.add_command(label="Quitter", command=root.destroy)
    menu_bar.add_cascade(label="Options", menu=file_menu)
    root.config(menu=menu_bar)
    image2=PhotoImage(file='B.png')
    Label1=Label(root,image=image2,border=0,bg="#4065a4").place(x=3,y=140)
    root.mainloop()
