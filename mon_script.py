import tkinter
import smtplib
import time
from tkinter import *
a=0
def GO () :
    global recepteur,emeteur,sujet,date,corpdutexte,a,serveur
    emeteur=emeteur_.get()
    recepteur=recepteur_.get()
    sujet=sujet_.get()
    date=date_.get()
    corpdutexte="salut"
    serveur_.get()
    root.destroy()
    a=1

root=Tk()
emeteur_=Entry()
emeteur_.grid(row=1,column=2)
Label(text='Entrez l\'email de l\'emeteur').grid(row=1,column=1)
recepteur_=Entry()
recepteur_.grid(row=2,column=2)
Label(text='Entrez l\'email du recepteur').grid(row=2,column=1)
sujet_=Entry()
sujet_.grid(row=3,column=2)
Label(text='Entrez le sujet').grid(row=3,column=1)
date_=Entry()
date_.grid(row=4,column=2)
Label(text='Entrez la date').grid(row=4,column=1)
corpdutexte_=Text()
corpdutexte_.grid(row=6,column=1,columnspan=2)
Label(text='Corp du texte :').grid(row=5,column=1,columnspan=2)
Button(text='      Poster      ',command=GO).grid(row=8,column=1,columnspan=2)
serveur_=Entry()
serveur_.grid(row=7,column=2)
Label(text=' Option : changez le serveur').grid(row=7,column=1)
emeteur_.insert('0','Anonimous@free.fr')
serveur_.insert('0','smtp.wanadoo.fr')
date_.insert('0',time.ctime(time.time()))
root.mainloop()

if a :
    
    from_addr = emeteur
    to_addrs = [recepteur]
    msg = """From: %s
    Subject: %s
    Date: %s
    To: %s
    %s
    """ % (emeteur,sujet,date,recepteur,corpdutexte)
    s = smtplib.SMTP('0','smtp.wanadoo.fr')
    s.set_debuglevel(1)
    s.sendmail(from_addr, to_addrs, msg)
    s.quit()