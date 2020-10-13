import os
import numpy as np
import cv2 
import pandas as pd
from matplotlib import pyplot as plt
from tkinter import *
import PIL.Image 
import PIL.ImageTk
from sklearn.decomposition import PCA
human_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
human_cascade1=cv2.CascadeClassifier('haarcascade_eye.xml')
class log_in:
    def __init__(self,window):
        self.window = window
        self.window.title("TÜBİTAK 2242")
        self.window.geometry('1350x690+0+0')
        self.window.tk_setPalette("grey")
        self.lbl = Label(self.window,text="STRABİSMUS TERAPİ",fg='red',bg='black', font="Times 30 bold").place(relx=0.0,rely=0.0,relwidth=1,relheight=0.15)
        self.btn1 = Button(self.window, text="ŞAŞILIK\n DÜZEY TESPİTİ\n \niçin tıklayınız", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.ekran_teşhis).place(relx = 0.2, rely = 0.4, relwidth=0.2,relheight=0.3) 
        self.btn2 = Button(self.window, text="TEDAVİ\n \niçin tıklayınız ", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.ekran_tedavi1).place(relx = 0.6, rely = 0.4, relwidth=0.2,relheight=0.3)               
    def initt(self):
        for widget in self.window.winfo_children(): # pencerede bulunan herşeyi kaldırdık
            widget.destroy()               
        self.window = window
        self.window.title("TÜBİTAK 2242")
        self.window.geometry('1350x690+0+0')
        self.window.tk_setPalette("grey")
        self.lbl = Label(self.window, text="STRABİSMUS TERAPİ", fg='red',bg='black', font="Times 30 bold").place(relx = 0.0, rely = 0.0, relwidth=1,relheight=0.15)
        self.btn = Button(self.window, text="ŞAŞILIK\n DÜZEY TESPİTİ\n \niçin tıklayınız", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.ekran_teşhis).place(relx = 0.2, rely = 0.4, relwidth=0.2,relheight=0.3)
        self.btn = Button(self.window, text="TEDAVİ\n \niçin tıklayınız ", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.ekran_tedavi1).place(relx = 0.6, rely = 0.4, relwidth=0.2,relheight=0.3)                     
    def ekran_teşhis(self):
        for widget in self.window.winfo_children(): # pencerede bulunan herşeyi kaldırdık
            widget.destroy()        
        self.giris = Label(text = "Teşhis aşamasında gözünüzün 3 adet fotoğrafı çekilerek\n farklı açılardan mercek konum verisi oluşturulacaktır.\nBu veriler gözdeki kayma miktarını \nhesaplamak için kullanılacaktır.",font="Times 30 bold", fg='red',bg='grey').place(relx = 0.0, rely = 0.05, relwidth=1,relheight=0.4)
        self.btn = Button(text="BAŞLA", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.ekran_teşhis1).place(relx = 0.4, rely = 0.5, relwidth=0.2,relheight=0.2)
        self.btn = Button(text="<--Geri", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.initt).place(relx = 0.9, rely = 0.9, relwidth=0.1,relheight=0.1)
        self.giris.pack() 
    def ekran_teşhis1(self): 
        for widget in self.window.winfo_children(): 
            widget.destroy()                     
        self.giris = Label(text = "1. Görüntü", fg='red',bg='green',font="Times 20 bold").place(relx = 0.0, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "2. Görüntü", fg='red',bg='yellow',font="Times 20 bold").place(relx = 0.2, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "3. Görüntü", fg='red',bg='yellow',font="Times 20 bold").place(relx = 0.4, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "ONAY", fg='red',bg='yellow',font="Times 20 bold").place(relx = 0.6, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "SONUÇLAR", fg='red',bg='yellow',font="Times 20 bold").place(relx = 0.8, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Button(text = " 1. GÖRÜNTÜ\n( SAĞ )\n\nKamerayı aktif\netmek için\ntıklayınız", fg='red',bg='black',font="Times 30 bold", cursor="bottom_side",command=self.foto1).place(relx = 0, rely = 0.05, relwidth=0.5,relheight=0.77)
        self.btn = Button(text="<--Geri", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.ekran_teşhis).place(relx = 0.9, rely = 0.9, relwidth=0.1,relheight=0.1)
        self.giris = Label(text = "Yüzünüz\nkameraya dönük bir şekilde\ntam sağa bakınız.\nUygun açıyı yakalayınca \nenter'a basarak \n1.Görüntüyü \nkaydedebilirsiniz\n\nSAĞ --->", fg='red',bg='grey',font="Times 30 bold").place(relx = 0.53, rely = 0.1, relwidth=0.45,relheight=0.65) 
        self.giris.pack()       
    def foto1(self):
        self.cap = cv2.VideoCapture(0)
        while True:            
            _,frame=self.cap.read()
            self.gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)   
            self.göz=human_cascade1.detectMultiScale(self.gri,1.1,7)
            self.yuz=human_cascade.detectMultiScale(self.gri,1.1,7)
            for (x,y,x1,y1) in self.yuz:
                cv2.rectangle(frame,(x,y),(x+x1,y+y1),(0,255,0),7)
                cv2.putText(frame,("SAG'a bakiniz"),(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 0, 255),3)
            a=1
            for (x,y,x1,y1) in self.göz:
                cv2.rectangle(frame,(x,y),(x+x1,y+y1),(255,2,5),4)                
                if a==1:
                    m1=frame[y:y+y1,x:x+x1]
                    a=2
                if a==2:
                    m2=frame[y:y+y1,x:x+x1]
           
            cv2.imshow('VERI OLUSTURMA',frame)           
            if cv2.waitKey(10) & 0xFF==ord('a'):
                frame=cv2.resize(frame,(640,480))
                m1=cv2.resize(m1,(100,100))
                m2=cv2.resize(m2,(100,100))
                cv2.imwrite('yuzA'+'.png',frame)
                cv2.imwrite('gozA'+str(1)+'.png',m1)
                cv2.imwrite('gozA'+str(2)+'.png',m2)
                self.cap.release()
                cv2.destroyAllWindows()
                self.onay1()                            
    def onay1(self):       
        for widget in self.window.winfo_children():
            widget.destroy()
        self.giris = Label(text = "1. Görüntü", fg='red',bg='green',font="Times 20 bold").place(relx = 0.0, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "2. Görüntü", fg='red',bg='yellow',font="Times 20 bold").place(relx = 0.2, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "3. Görüntü", fg='red',bg='yellow',font="Times 20 bold").place(relx = 0.4, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "ONAY", fg='red',bg='yellow',font="Times 20 bold").place(relx = 0.6, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "SONUÇLAR", fg='red',bg='yellow',font="Times 20 bold").place(relx = 0.8, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(bg='green').place(relx = 0, rely = 0.05, relwidth=0.49,relheight=0.72)
        self.btn = Button(text="<--Geri", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.ekran_teşhis1).place(relx = 0.9, rely = 0.9, relwidth=0.1,relheight=0.1)
        self.giris = Label(text = "Yüz ve göz konumları tespit edildi ise \nDEVAM butonuna tıklayarak resmi kaydedebilirsiniz", fg='red',bg='grey',font="Times 30 bold").place(relx = 0.53, rely = 0.1, relwidth=0.45,relheight=0.65) 
        self.giris = Label(text = "1. Görüntü\n Yüz ve göz konumları \ntespit edildi ise \n\nDEVAM\n\n butonuna tıklayarak \ngörüntüyü kaydedebilirsiniz.\nGörüntüyü tekrar çekmek için\n geriye tıklayınız.", fg='red',bg='grey',font="Times 30 bold").place(relx = 0.53, rely = 0.07, relwidth=0.45,relheight=0.65) 
        self.btn = Button(text="DEVAM", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.ekran_teşhis2).place(relx = 0.66, rely = 0.3, relwidth=0.18,relheight=0.14)        
        ım1= PIL.Image.open("yuzA.png")
        ım2= PIL.Image.open("gozA1.png")
        ım3= PIL.Image.open("gozA2.png")
        photo1 = PIL.ImageTk.PhotoImage(ım1)
        photo2 = PIL.ImageTk.PhotoImage(ım2)
        photo3 = PIL.ImageTk.PhotoImage(ım3)
        self.label=Label(window,image=photo1).place(relx = 0.0, rely = 0.06, relwidth=0.48,relheight=0.7)
        self.label=Label(window,image=photo2,bg='black').place(relx = 0.0, rely = 0.83, relwidth=0.08,relheight=0.15)
        self.label=Label(window,image=photo3,bg='black').place(relx = 0.08, rely = 0.83, relwidth=0.08,relheight=0.15)
        self.label.image=photo1
        self.label.image=photo2
        self.label.image=photo3
        self.label.pack()        
    def ekran_teşhis2(self): 
        for widget in self.window.winfo_children(): 
            widget.destroy()                     
        self.giris = Label(text = "1. Görüntü +", fg='red',bg='black',font="Times 20 bold").place(relx = 0.0, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "2. Görüntü", fg='red',bg='green',font="Times 20 bold").place(relx = 0.2, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "3. Görüntü", fg='red',bg='yellow',font="Times 20 bold").place(relx = 0.4, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "ONAY", fg='red',bg='yellow',font="Times 20 bold").place(relx = 0.6, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "SONUÇLAR", fg='red',bg='yellow',font="Times 20 bold").place(relx = 0.8, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Button(text = " 2. GÖRÜNTÜ\n( SOL )\n\nKamerayı aktif\netmek için\ntıklayınız", fg='red',bg='black',font="Times 30 bold", cursor="bottom_side",command=self.foto2).place(relx = 0, rely = 0.05, relwidth=0.5,relheight=0.77)
        self.btn = Button(text="<--Geri", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.onay1).place(relx = 0.9, rely = 0.9, relwidth=0.1,relheight=0.1)
        self.giris = Label(text = "Yüzünüz\nkameraya dönük bir şekilde\ntam sol'a bakınız.\nUygun açıyı yakalayınca \nenter'a basarak \n2. Görüntüyü \nkaydedebilirsiniz\n\n<--SOL", fg='red',bg='grey',font="Times 30 bold").place(relx = 0.53, rely = 0.1, relwidth=0.45,relheight=0.65) 
        ım2= PIL.Image.open("gozA1.png")
        ım3= PIL.Image.open("gozA2.png")
        photo2 = PIL.ImageTk.PhotoImage(ım2)
        photo3 = PIL.ImageTk.PhotoImage(ım3)
        self.label=Label(window,image=photo2,bg='black').place(relx = 0.0, rely = 0.83, relwidth=0.08,relheight=0.15)
        self.label=Label(window,image=photo3,bg='black').place(relx = 0.08, rely = 0.83, relwidth=0.08,relheight=0.15)
        self.label.image=photo2
        self.label.image=photo3
        self.giris.pack()       
    def foto2(self):
        self.cap = cv2.VideoCapture(0)
        while True:            
            _,frame=self.cap.read()
            self.gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)   
            self.göz=human_cascade1.detectMultiScale(self.gri,1.1,7)
            self.yuz=human_cascade.detectMultiScale(self.gri,1.1,7)
            for (x,y,x1,y1) in self.yuz:
                cv2.rectangle(frame,(x,y),(x+x1,y+y1),(0,255,0),7)
                cv2.putText(frame,("SOL'a bakiniz"),(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 0, 255),3)
            a=1
            for (x,y,x1,y1) in self.göz:
                cv2.rectangle(frame,(x,y),(x+x1,y+y1),(255,2,5),4)                
                if a==1:
                    m1=frame[y:y+y1,x:x+x1]
                    a=2
                if a==2:
                    m2=frame[y:y+y1,x:x+x1]            
            cv2.imshow('VERİ OLUŞTURMA',frame)            
            if cv2.waitKey(10) & 0xFF==ord('a'):
                frame=cv2.resize(frame,(640,480))
                m1=cv2.resize(m1,(100,100))
                m2=cv2.resize(m2,(100,100))
                cv2.imwrite('yuzB'+'.png',frame)
                cv2.imwrite('gozB'+str(1)+'.png',m1)
                cv2.imwrite('gozB'+str(2)+'.png',m2)
                self.cap.release()
                cv2.destroyAllWindows()
                self.onay2()                    
    def onay2(self):       
        for widget in self.window.winfo_children():
            widget.destroy()
        self.giris = Label(text = "1. Görüntü +", fg='red',bg='black',font="Times 20 bold").place(relx = 0.0, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "2. Görüntü", fg='red',bg='green',font="Times 20 bold").place(relx = 0.2, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "3. Görüntü", fg='red',bg='yellow',font="Times 20 bold").place(relx = 0.4, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "ONAY", fg='red',bg='yellow',font="Times 20 bold").place(relx = 0.6, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "SONUÇLAR", fg='red',bg='yellow',font="Times 20 bold").place(relx = 0.8, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(bg='green').place(relx = 0, rely = 0.05, relwidth=0.49,relheight=0.72)
        self.btn = Button(text="<--Geri", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.ekran_teşhis2).place(relx = 0.9, rely = 0.9, relwidth=0.1,relheight=0.1)
        self.giris = Label(text = "2. Görüntü\n Yüz ve göz konumları \ntespit edildi ise \n\nDEVAM\n\n butonuna tıklayarak \ngörüntüyü kaydedebilirsiniz.\nGörüntüyü tekrar çekmek için\n geriye tıklayınız.", fg='red',bg='grey',font="Times 30 bold").place(relx = 0.53, rely = 0.07, relwidth=0.45,relheight=0.65) 
        self.btn = Button(text="DEVAM", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.ekran_teşhis3).place(relx = 0.66, rely = 0.3, relwidth=0.18,relheight=0.14)           
        ım2= PIL.Image.open("gozA1.png")
        ım3= PIL.Image.open("gozA2.png")
        ım4= PIL.Image.open("yuzB.png")
        ım5= PIL.Image.open("gozB2.png")
        ım6= PIL.Image.open("gozB1.png")        
        photo2 = PIL.ImageTk.PhotoImage(ım2)
        photo3 = PIL.ImageTk.PhotoImage(ım3)
        photo4 = PIL.ImageTk.PhotoImage(ım4)
        photo5 = PIL.ImageTk.PhotoImage(ım5)
        photo6 = PIL.ImageTk.PhotoImage(ım6)
        self.label=Label(window,image=photo4).place(relx = 0.0, rely = 0.06, relwidth=0.48,relheight=0.7)
        self.label=Label(window,image=photo2,bg='black').place(relx = 0.0, rely = 0.83, relwidth=0.08,relheight=0.15)
        self.label=Label(window,image=photo3,bg='black').place(relx = 0.08, rely = 0.83, relwidth=0.08,relheight=0.15)
        self.label=Label(window,image=photo5,bg='black').place(relx = 0.2, rely = 0.83, relwidth=0.08,relheight=0.15)
        self.label=Label(window,image=photo6,bg='black').place(relx = 0.28, rely = 0.83, relwidth=0.08,relheight=0.15)        
        self.label.image=photo4
        self.label.image=photo2
        self.label.image=photo3
        self.label.image=photo5
        self.label.image=photo6
        self.label.pack()     
    def ekran_teşhis3(self): 
        for widget in self.window.winfo_children(): 
            widget.destroy()                     
        self.giris = Label(text = "1. Görüntü +", fg='red',bg='black',font="Times 20 bold").place(relx = 0.0, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "2. Görüntü +", fg='red',bg='black',font="Times 20 bold").place(relx = 0.2, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "3. Görüntü", fg='red',bg='green',font="Times 20 bold").place(relx = 0.4, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "ONAY", fg='red',bg='yellow',font="Times 20 bold").place(relx = 0.6, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "SONUÇLAR", fg='red',bg='yellow',font="Times 20 bold").place(relx = 0.8, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Button(text = " 3. GÖRÜNTÜ\n( YUKARI )\n\nKamerayı aktif\netmek için\ntıklayınız", fg='red',bg='black',font="Times 30 bold", cursor="bottom_side",command=self.foto3).place(relx = 0, rely = 0.05, relwidth=0.5,relheight=0.77)
        self.btn = Button(text="<--Geri", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.onay2).place(relx = 0.9, rely = 0.9, relwidth=0.1,relheight=0.1)
        self.giris = Label(text = "Yüzünüz\nkameraya dönük bir şekilde\ntam yukarıya bakınız.\nUygun açıyı yakalayınca \nenter'a basarak \n3. Görüntüyü \nkaydedebilirsiniz\n\nYUKARI ^", fg='red',bg='grey',font="Times 30 bold").place(relx = 0.53, rely = 0.1, relwidth=0.45,relheight=0.65) 
        ım2= PIL.Image.open("gozA1.png")
        ım3= PIL.Image.open("gozA2.png")
        ım5= PIL.Image.open("gozB2.png")
        ım6= PIL.Image.open("gozB1.png")
        photo2 = PIL.ImageTk.PhotoImage(ım2)
        photo3 = PIL.ImageTk.PhotoImage(ım3)
        photo5 = PIL.ImageTk.PhotoImage(ım5)
        photo6 = PIL.ImageTk.PhotoImage(ım6)
        self.label=Label(window,image=photo2,bg='black').place(relx = 0.0, rely = 0.83, relwidth=0.08,relheight=0.15)
        self.label=Label(window,image=photo3,bg='black').place(relx = 0.08, rely = 0.83, relwidth=0.08,relheight=0.15)
        self.label=Label(window,image=photo5,bg='black').place(relx = 0.2, rely = 0.83, relwidth=0.08,relheight=0.15)
        self.label=Label(window,image=photo6,bg='black').place(relx = 0.28, rely = 0.83, relwidth=0.08,relheight=0.15)                
        self.label.image=photo2
        self.label.image=photo3
        self.label.image=photo5
        self.label.image=photo6
        self.giris.pack()       
    def foto3(self):
        self.cap = cv2.VideoCapture(0)
        while True:            
            _,frame=self.cap.read()
            self.gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)   
            self.göz=human_cascade1.detectMultiScale(self.gri,1.1,7)
            self.yuz=human_cascade.detectMultiScale(self.gri,1.1,7)
            for (x,y,x1,y1) in self.yuz:
                cv2.rectangle(frame,(x,y),(x+x1,y+y1),(0,255,0),7)
                cv2.putText(frame,("YUKARI bakiniz"),(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 0, 255),3)
            a=1
            for (x,y,x1,y1) in self.göz:
                cv2.rectangle(frame,(x,y),(x+x1,y+y1),(255,2,5),4)                
                if a==1:
                    m1=frame[y:y+y1,x:x+x1]
                    a=2
                if a==2:
                    m2=frame[y:y+y1,x:x+x1]
            
            cv2.imshow('VERİ OLUŞTURMA',frame)            
            if cv2.waitKey(10) & 0xFF==ord('a'):
                frame=cv2.resize(frame,(640,480))
                m1=cv2.resize(m1,(100,100))
                m2=cv2.resize(m2,(100,100))
                cv2.imwrite('yuzC'+'.png',frame)
                cv2.imwrite('gozC'+str(1)+'.png',m1)
                cv2.imwrite('gozC'+str(2)+'.png',m2)
                self.cap.release()
                cv2.destroyAllWindows()
                self.onay3()                            
    def onay3(self):       
        for widget in self.window.winfo_children():
            widget.destroy()
        self.giris = Label(text = "1. Görüntü +", fg='red',bg='black',font="Times 20 bold").place(relx = 0.0, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "2. Görüntü +", fg='red',bg='black',font="Times 20 bold").place(relx = 0.2, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "3. Görüntü", fg='red',bg='green',font="Times 20 bold").place(relx = 0.4, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "ONAY", fg='red',bg='yellow',font="Times 20 bold").place(relx = 0.6, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "SONUÇLAR", fg='red',bg='yellow',font="Times 20 bold").place(relx = 0.8, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(bg='green').place(relx = 0, rely = 0.05, relwidth=0.49,relheight=0.72)
        self.btn = Button(text="<--Geri", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.ekran_teşhis3).place(relx = 0.9, rely = 0.9, relwidth=0.1,relheight=0.1)
        self.giris = Label(text = "3. Görüntü\n Yüz ve göz konumları \ntespit edildi ise \n\nDEVAM\n\n butonuna tıklayarak \ngörüntüyü kaydedebilirsiniz.\nGörüntüyü tekrar çekmek için\n geriye tıklayınız.", fg='red',bg='grey',font="Times 30 bold").place(relx = 0.53, rely = 0.07, relwidth=0.45,relheight=0.65) 
        self.btn = Button(text="DEVAM", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.onay4).place(relx = 0.66, rely = 0.3, relwidth=0.18,relheight=0.14)           
        ım7= PIL.Image.open("yuzC.png")
        ım2= PIL.Image.open("gozA1.png")
        ım3= PIL.Image.open("gozA2.png")        
        ım5= PIL.Image.open("gozB2.png")
        ım6= PIL.Image.open("gozB1.png")
        ım8= PIL.Image.open("gozC2.png")
        ım9= PIL.Image.open("gozC1.png")   
        photo7 = PIL.ImageTk.PhotoImage(ım7)
        photo2 = PIL.ImageTk.PhotoImage(ım2)
        photo3 = PIL.ImageTk.PhotoImage(ım3)        
        photo5 = PIL.ImageTk.PhotoImage(ım5)
        photo6 = PIL.ImageTk.PhotoImage(ım6)
        photo8 = PIL.ImageTk.PhotoImage(ım8)
        photo9 = PIL.ImageTk.PhotoImage(ım9)
        self.label=Label(window,image=photo7).place(relx = 0.0, rely = 0.06, relwidth=0.48,relheight=0.7)
        self.label=Label(window,image=photo2,bg='black').place(relx = 0.0, rely = 0.83, relwidth=0.08,relheight=0.15)
        self.label=Label(window,image=photo3,bg='black').place(relx = 0.08, rely = 0.83, relwidth=0.08,relheight=0.15)
        self.label=Label(window,image=photo5,bg='black').place(relx = 0.2, rely = 0.83, relwidth=0.08,relheight=0.15)
        self.label=Label(window,image=photo6,bg='black').place(relx = 0.28, rely = 0.83, relwidth=0.08,relheight=0.15)        
        self.label=Label(window,image=photo8,bg='black').place(relx = 0.4, rely = 0.83, relwidth=0.08,relheight=0.15)
        self.label=Label(window,image=photo9,bg='black').place(relx = 0.48, rely = 0.83, relwidth=0.08,relheight=0.15)                
        self.label.image=photo7
        self.label.image=photo2
        self.label.image=photo3
        self.label.image=photo5
        self.label.image=photo6
        self.label.image=photo8
        self.label.image=photo9
        self.label.pack()                     
        
    def onay4(self):
        for widget in self.window.winfo_children():
            widget.destroy()       
        self.giris = Label(text = "1. Görüntü +", fg='red',bg='black',font="Times 20 bold").place(relx = 0.0, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "2. Görüntü +", fg='red',bg='black',font="Times 20 bold").place(relx = 0.2, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "3. Görüntü +", fg='red',bg='black',font="Times 20 bold").place(relx = 0.4, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "ONAY", fg='red',bg='green',font="Times 20 bold").place(relx = 0.6, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "SONUÇLAR", fg='red',bg='yellow',font="Times 20 bold").place(relx = 0.8, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.btn = Button(text="<--Geri", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.onay3).place(relx = 0.9, rely = 0.9, relwidth=0.1,relheight=0.1)
        self.giris = Label(bg='blue').place(relx = 0.05, rely = 0.08, relwidth=0.28,relheight=0.8)
        self.giris = Label(text = "1.Çift (sağ)",bg='green', fg='red',font="Times 15 bold").place(relx = 0.05, rely = 0.12, relwidth=0.07,relheight=0.05)
        self.giris = Label(text = "2.Çift (sol)",bg='green', fg='red',font="Times 15 bold").place(relx = 0.05, rely = 0.41, relwidth=0.07,relheight=0.05)
        self.giris = Label(text = "3.Çift (yukarı)",bg='green', fg='red',font="Times 15 bold").place(relx = 0.05, rely = 0.69, relwidth=0.09,relheight=0.05)        
        self.giris = Label(text = "A1",bg='red', fg='yellow',font="Times 20 bold").place(relx = 0.15, rely = 0.26, relwidth=0.08,relheight=0.05)        
        self.giris = Label(text = "A2",bg='red', fg='yellow',font="Times 20 bold").place(relx = 0.23, rely = 0.26, relwidth=0.08,relheight=0.05)        
        self.giris = Label(text = "B1",bg='red', fg='yellow',font="Times 20 bold").place(relx = 0.15, rely = 0.54, relwidth=0.08,relheight=0.05)        
        self.giris = Label(text = "B2",bg='red', fg='yellow',font="Times 20 bold").place(relx = 0.23, rely = 0.54, relwidth=0.08,relheight=0.05)        
        self.giris = Label(text = "C1",bg='red', fg='yellow',font="Times 20 bold").place(relx = 0.15, rely = 0.82, relwidth=0.08,relheight=0.05)        
        self.giris = Label(text = "C2",bg='red', fg='yellow',font="Times 20 bold").place(relx = 0.23, rely = 0.82, relwidth=0.08,relheight=0.05)        
        self.giris = Label(text = "Gözler arasındaki benzerlik\noranını\n\n",bg='red', fg='yellow',font="Times 20 bold").place(relx = 0.4, rely = 0.25, relwidth=0.25,relheight=0.4)        
        self.btn = Button(text="HESAPLA", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.sonuc).place(relx = 0.475, rely = 0.5, relwidth=0.1,relheight=0.1)
        self.giris = Label(bg='blue').place(relx = 0.7, rely = 0.08, relwidth=0.25,relheight=0.8)
        self.giris = Label(text = "A1-A2 =  ?",bg='red', fg='yellow',font="Times 20 bold").place(relx = 0.73, rely = 0.12, relwidth=0.2,relheight=0.05)        
        self.giris = Label(text = "A1-B2 =  ?",bg='red', fg='yellow',font="Times 20 bold").place(relx = 0.73, rely = 0.19, relwidth=0.2,relheight=0.05)        
        self.giris = Label(text = "A1-C2 =  ?",bg='red', fg='yellow',font="Times 20 bold").place(relx = 0.73, rely = 0.26, relwidth=0.2,relheight=0.05)        
        self.giris = Label(text = "B1-A2 =  ?",bg='red', fg='yellow',font="Times 20 bold").place(relx = 0.73, rely = 0.37, relwidth=0.2,relheight=0.05)        
        self.giris = Label(text = "B1-B2 =  ?",bg='red', fg='yellow',font="Times 20 bold").place(relx = 0.73, rely = 0.44, relwidth=0.2,relheight=0.05)        
        self.giris = Label(text = "B1-C2 =  ?",bg='red', fg='yellow',font="Times 20 bold").place(relx = 0.73, rely = 0.51, relwidth=0.2,relheight=0.05)        
        self.giris = Label(text = "C1-A2 =  ?",bg='red', fg='yellow',font="Times 20 bold").place(relx = 0.73, rely = 0.62, relwidth=0.2,relheight=0.05)        
        self.giris = Label(text = "C1-B2 =  ?",bg='red', fg='yellow',font="Times 20 bold").place(relx = 0.73, rely = 0.69, relwidth=0.2,relheight=0.05)        
        self.giris = Label(text = "C1-C2 =  ?",bg='red', fg='yellow',font="Times 20 bold").place(relx = 0.73, rely = 0.76, relwidth=0.2,relheight=0.05)                
        ım2= PIL.Image.open("gozA1.png")
        ım3= PIL.Image.open("gozA2.png")        
        ım5= PIL.Image.open("gozB2.png")
        ım6= PIL.Image.open("gozB1.png")
        ım8= PIL.Image.open("gozC2.png")
        ım9= PIL.Image.open("gozC1.png")        
        photo2 = PIL.ImageTk.PhotoImage(ım2)
        photo3 = PIL.ImageTk.PhotoImage(ım3)        
        photo5 = PIL.ImageTk.PhotoImage(ım5)
        photo6 = PIL.ImageTk.PhotoImage(ım6)
        photo8 = PIL.ImageTk.PhotoImage(ım8)
        photo9 = PIL.ImageTk.PhotoImage(ım9)             
        self.label=Label(window,image=photo2,bg='black').place(relx = 0.15, rely = 0.1, relwidth=0.08,relheight=0.15)
        self.label=Label(window,image=photo3,bg='black').place(relx = 0.23, rely = 0.1, relwidth=0.08,relheight=0.15)
        self.label=Label(window,image=photo5,bg='black').place(relx = 0.15, rely = 0.38, relwidth=0.08,relheight=0.15)
        self.label=Label(window,image=photo6,bg='black').place(relx = 0.23, rely = 0.38, relwidth=0.08,relheight=0.15)        
        self.label=Label(window,image=photo8,bg='black').place(relx = 0.15, rely = 0.66, relwidth=0.08,relheight=0.15)
        self.label=Label(window,image=photo9,bg='black').place(relx = 0.23, rely = 0.66, relwidth=0.08,relheight=0.15)                
        self.label.image=photo2
        self.label.image=photo3
        self.label.image=photo5
        self.label.image=photo6
        self.label.image=photo8
        self.label.image=photo9
        self.label.pack()
    def sonuc(self):                 
        res1=cv2.imread("gozA1.png",0)
        res2=cv2.imread("gozA2.png",0)
        res3=cv2.imread("gozB1.png",0)
        res4=cv2.imread("gozB2.png",0)   
        res5=cv2.imread("gozC1.png",0)
        res6=cv2.imread("gozC2.png",0)           
        r1=np.zeros((50,80))
        r2=np.zeros((50,80))
        r3=np.zeros((50,80))
        r4=np.zeros((50,80))
        r5=np.zeros((50,80))
        r6=np.zeros((50,80))      
        r1=np.uint8(r1)
        r2=np.uint8(r2)
        r3=np.uint8(r3)
        r4=np.uint8(r4)
        r5=np.uint8(r5)
        r6=np.uint8(r6)
########### A1.               
        for m in range(30,80,1):
            for n in range(10,90,1):
                r1[m-30,n-10]=res1[m,n]
                r2[m-30,n-10]=res2[m,n]
        r1 = cv2.equalizeHist(r1)
        r2 = cv2.equalizeHist(r2)
        for i in range(0,50,1):
            for j in range(0,80,1):
                if r1[i,j]>=50 and r2[i,j]>=50 :
                   r1[i,j]=255
                   r2[i,j]=255          
                if r1[i,j]<20 and r2[i,j]<20:
                   r1[i,j]=0
                   r2[i,j]=0 
                if r1[i,j]<10:
                   r1[i,j]=0
                if r2[i,j]<10:
                   r2[i,j]=0 
                if r1[i,j]>200:
                   r1[i,j]=200
                if r2[i,j]>200:
                   r2[i,j]=200    
        a=r1-r2
        toplam=np.array(a)
        toplam=np.sqrt(toplam**2)
        A1=sum(sum(toplam))
        cv2.imwrite('A1'+'.png',r1)
        cv2.imwrite('A2'+'.png',r2)
###########  A2.        
        for m in range(30,80,1):
            for n in range(10,90,1):
                r1[m-30,n-10]=res1[m,n]
                r4[m-30,n-10]=res4[m,n]

        r1 = cv2.equalizeHist(r1)
        r4 = cv2.equalizeHist(r4)
        for i in range(0,50,1):
            for j in range(0,80,1):
                if r1[i,j]>=50 and r4[i,j]>=50 :
                   r1[i,j]=255
                   r4[i,j]=255          
                if r1[i,j]<20 and r4[i,j]<20:
                   r1[i,j]=0
                   r4[i,j]=0
                if r1[i,j]<10:
                   r1[i,j]=0
                if r4[i,j]<10:
                   r4[i,j]=0 
                if r1[i,j]>200:
                   r1[i,j]=200
                if r4[i,j]>200:
                   r4[i,j]=200
        a=r1-r4
        toplam=np.array(a)
        toplam=np.sqrt(toplam**2)
        A2=sum(sum(toplam))

#######   A3
        for m in range(30,80,1):
            for n in range(10,90,1):
                r1[m-30,n-10]=res1[m,n]
                r6[m-30,n-10]=res6[m,n]
        r1 = cv2.equalizeHist(r1)
        r6 = cv2.equalizeHist(r6) 
        for i in range(0,50,1):
            for j in range(0,80,1):
                if r1[i,j]>=50 and r6[i,j]>=50 :
                   r1[i,j]=255
                   r6[i,j]=255              
                if r1[i,j]<20 and r6[i,j]<20:
                   r1[i,j]=0
                   r6[i,j]=0
                if r1[i,j]<10:
                   r1[i,j]=0
                if r6[i,j]<10:
                   r6[i,j]=0 
                if r1[i,j]>200:
                   r1[i,j]=200
                if r6[i,j]>200:
                   r6[i,j]=200 
        a=r1-r6
        toplam=np.array(a)
        toplam=np.sqrt(toplam**2)
        A3=sum(sum(toplam))        
# # B1.       
        for m in range(30,80,1):
            for n in range(10,90,1):        
                r2[m-30,n-10]=res2[m,n]
                r3[m-30,n-10]=res3[m,n]
        r3 = cv2.equalizeHist(r3)
        r2 = cv2.equalizeHist(r2)        
        for i in range(0,50,1):
            for j in range(0,80,1):
                if r3[i,j]>=50 and r2[i,j]>=50 :
                    r3[i,j]=255
                    r2[i,j]=255          
                if r3[i,j]<20 and r2[i,j]<20:
                    r3[i,j]=0
                    r2[i,j]=0 
                if r3[i,j]<10:
                    r3[i,j]=0
                if r2[i,j]<10:
                    r2[i,j]=0 
                if r3[i,j]>200:
                    r3[i,j]=200
                if r2[i,j]>200:
                    r2[i,j]=200
        a=r3-r2
        toplam=np.array(a)        
        toplam=np.sqrt(toplam**2)        
        B1=sum(sum(toplam))        
# # B2.
        for m in range(30,80,1):
            for n in range(10,90,1):
                r3[m-30,n-10]=res3[m,n]
                r4[m-30,n-10]=res4[m,n]
        r3 = cv2.equalizeHist(r3)
        r4 = cv2.equalizeHist(r4)
        for i in range(0,50,1):
            for j in range(0,80,1):
                if r3[i,j]>=50 and r4[i,j]>=50 :
                    r3[i,j]=255
                    r4[i,j]=255          
                if r3[i,j]<20 and r4[i,j]<20:
                    r3[i,j]=0
                    r4[i,j]=0
                if r3[i,j]<10:
                    r3[i,j]=0
                if r4[i,j]<10:
                    r4[i,j]=0 
                if r3[i,j]>200:
                    r3[i,j]=200
                if r4[i,j]>200:
                    r4[i,j]=200
        a=r3-r4
        toplam=np.array(a)
        toplam=np.sqrt(toplam**2)
        B2=sum(sum(toplam))  
        cv2.imwrite('B1'+'.png',r3)
        cv2.imwrite('B2'+'.png',r4)        
# #B3.       
        for m in range(30,80,1):
            for n in range(10,90,1):
                r3[m-30,n-10]=res3[m,n]
                r6[m-30,n-10]=res6[m,n]
        r3 = cv2.equalizeHist(r3)
        r6 = cv2.equalizeHist(r6)
        for i in range(0,50,1):
            for j in range(0,80,1):
                if r3[i,j]>=50 and r6[i,j]>=50 :
                    r3[i,j]=255
                    r6[i,j]=255          
                if r3[i,j]<20 and r6[i,j]<20:
                    r3[i,j]=0
                    r6[i,j]=0
                if r3[i,j]<10:
                    r3[i,j]=0
                if r6[i,j]<10:
                    r6[i,j]=0 
                if r3[i,j]>200:
                    r3[i,j]=200
                if r6[i,j]>200:
                    r6[i,j]=200
        a=r3-r6
        toplam=np.array(a)
        toplam=np.sqrt(toplam**2)
        B3=sum(sum(toplam))        
# #C1.      
        for m in range(30,80,1):
            for n in range(10,90,1):
                r2[m-30,n-10]=res2[m,n]
                r5[m-30,n-10]=res5[m,n]
        r5 = cv2.equalizeHist(r5)
        r2 = cv2.equalizeHist(r2)
        for i in range(0,50,1):
            for j in range(0,80,1):
                if r5[i,j]>=50 and r2[i,j]>=50 :
                    r5[i,j]=255
                    r2[i,j]=255          
                if r5[i,j]<20 and r2[i,j]<20:
                    r5[i,j]=0
                    r2[i,j]=0 
                if r5[i,j]<10:
                    r5[i,j]=0
                if r2[i,j]<10:
                    r2[i,j]=0 
                if r5[i,j]>200:
                    r5[i,j]=200
                if r2[i,j]>200:
                    r2[i,j]=200
        a=r5-r2
        toplam=np.array(a)
        toplam=np.sqrt(toplam**2)
        C1=sum(sum(toplam))        
# # C2.     
        for m in range(30,80,1):
            for n in range(10,90,1):
                r4[m-30,n-10]=res4[m,n]
                r5[m-30,n-10]=res5[m,n]
        r5 = cv2.equalizeHist(r5)
        r4 = cv2.equalizeHist(r4)
        for i in range(0,50,1):
            for j in range(0,80,1):
                if r5[i,j]>=50 and r4[i,j]>=50 :
                    r5[i,j]=255
                    r4[i,j]=255          
                if r5[i,j]<20 and r4[i,j]<20:
                    r5[i,j]=0
                    r4[i,j]=0
                if r5[i,j]>30 and r4[i,j]>30 and r5[i,j]<=60 and r4[i,j]<=60:
                    r5[i,j]=100
                    r4[i,j]=100
                if r5[i,j]<10:
                    r5[i,j]=0
                if r4[i,j]<10:
                    r4[i,j]=0 
                if r5[i,j]>200:
                    r5[i,j]=200
                if r4[i,j]>200:
                    r4[i,j]=200    
        a=r5-r4
        toplam=np.array(a)
        toplam=np.sqrt(toplam**2)
        C2=sum(sum(toplam))       
# #C3.        
        for m in range(30,80,1):
            for n in range(10,90,1):
                r5[m-30,n-10]=res5[m,n]
                r6[m-30,n-10]=res6[m,n]
        r5 = cv2.equalizeHist(r5)
        r6 = cv2.equalizeHist(r6)
        for i in range(0,50,1):
            for j in range(0,80,1):
                if r5[i,j]>=50 and r6[i,j]>=50 :
                    r5[i,j]=255
                    r6[i,j]=255          
                if r5[i,j]<20 and r6[i,j]<20:
                    r5[i,j]=0
                    r6[i,j]=0
        
                if r5[i,j]<10:
                    r5[i,j]=0
                if r6[i,j]<10:
                    r6[i,j]=0 
                if r5[i,j]>200:
                    r5[i,j]=200
                if r6[i,j]>200:
                    r6[i,j]=200 
        a=r5-r6
        toplam=np.array(a)
        toplam=np.sqrt(toplam**2)
        C3=sum(sum(toplam))
        cv2.imwrite('C1'+'.png',r5)
        cv2.imwrite('C2'+'.png',r6)

        print("A1="+str(A1)) 
        print(str(A2)) 
        print(str(A3))
        print("B2="+str(B2))
        print(str(B1))
        print(str(B3))
        print("C3="+str(C3))
        print(str(C1))
        print(str(C2))
# #
        for widget in self.window.winfo_children():
            widget.destroy()
        self.giris = Label(bg='blue').place(relx = 0.37, rely = 0.08, relwidth=0.25,relheight=0.8)  
        self.giris = Label(text = "1. Görüntü +", fg='red',bg='black',font="Times 20 bold").place(relx = 0.0, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "2. Görüntü +", fg='red',bg='black',font="Times 20 bold").place(relx = 0.2, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "3. Görüntü +", fg='red',bg='black',font="Times 20 bold").place(relx = 0.4, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "ONAY +", fg='red',bg='black',font="Times 20 bold").place(relx = 0.6, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.giris = Label(text = "SONUÇLAR", fg='red',bg='green',font="Times 20 bold").place(relx = 0.8, rely = 0.0, relwidth=0.2,relheight=0.05)
        self.btn = Button(text="<--Geri", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.onay4).place(relx = 0.9, rely = 0.9, relwidth=0.1,relheight=0.1)
        self.btn = Button(text="Ana Menü", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.initt).place(relx = 0.0, rely = 0.9, relwidth=0.15,relheight=0.1)        
        self.giris = Label(bg='blue').place(relx = 0.05, rely = 0.08, relwidth=0.28,relheight=0.8)
        self.giris = Label(text = "1.Çift (sağ)",bg='green', fg='red',font="Times 15 bold").place(relx = 0.05, rely = 0.12, relwidth=0.07,relheight=0.05)
        self.giris = Label(text = "2.Çift (sol)",bg='green', fg='red',font="Times 15 bold").place(relx = 0.05, rely = 0.41, relwidth=0.07,relheight=0.05)
        self.giris = Label(text = "3.Çift (yukarı)",bg='green', fg='red',font="Times 15 bold").place(relx = 0.05, rely = 0.69, relwidth=0.09,relheight=0.05)        
        self.giris = Label(text = "A1",bg='red', fg='yellow',font="Times 20 bold").place(relx = 0.15, rely = 0.26, relwidth=0.08,relheight=0.05)        
        self.giris = Label(text = "A2",bg='red', fg='yellow',font="Times 20 bold").place(relx = 0.23, rely = 0.26, relwidth=0.08,relheight=0.05)        
        self.giris = Label(text = "B1",bg='red', fg='yellow',font="Times 20 bold").place(relx = 0.15, rely = 0.54, relwidth=0.08,relheight=0.05)        
        self.giris = Label(text = "B2",bg='red', fg='yellow',font="Times 20 bold").place(relx = 0.23, rely = 0.54, relwidth=0.08,relheight=0.05)        
        self.giris = Label(text = "C1",bg='red', fg='yellow',font="Times 20 bold").place(relx = 0.15, rely = 0.82, relwidth=0.08,relheight=0.05)        
        self.giris = Label(text = "C2",bg='red', fg='yellow',font="Times 20 bold").place(relx = 0.23, rely = 0.82, relwidth=0.08,relheight=0.05)        
        self.giris = Label(bg='blue').place(relx = 0.7, rely = 0.08, relwidth=0.25,relheight=0.8)
        self.giris = Label(text = "A1-A2 = "+str(round(A1)),bg='red', fg='black',font="Times 20 bold").place(relx = 0.73, rely = 0.12, relwidth=0.2,relheight=0.05)        
        self.giris = Label(text = "A1-B2 = "+str(round(A2)),bg='red', fg='yellow',font="Times 20 bold").place(relx = 0.73, rely = 0.19, relwidth=0.2,relheight=0.05)        
        self.giris = Label(text = "A1-C2 = "+str(round(A3)),bg='red', fg='yellow',font="Times 20 bold").place(relx = 0.73, rely = 0.26, relwidth=0.2,relheight=0.05)        
        self.giris = Label(text = "B1-A2 = "+str(round(B1)),bg='red', fg='yellow',font="Times 20 bold").place(relx = 0.73, rely = 0.37, relwidth=0.2,relheight=0.05)        
        self.giris = Label(text = "B1-B2 = "+str(round(B2)),bg='red', fg='black',font="Times 20 bold").place(relx = 0.73, rely = 0.44, relwidth=0.2,relheight=0.05)        
        self.giris = Label(text = "B1-C2 = "+str(round(B3)),bg='red', fg='yellow',font="Times 20 bold").place(relx = 0.73, rely = 0.51, relwidth=0.2,relheight=0.05)        
        self.giris = Label(text = "C1-A2 = "+str(round(C1)),bg='red', fg='yellow',font="Times 20 bold").place(relx = 0.73, rely = 0.62, relwidth=0.2,relheight=0.05)        
        self.giris = Label(text = "C1-B2 = "+str(round(C2)),bg='red', fg='yellow',font="Times 20 bold").place(relx = 0.73, rely = 0.69, relwidth=0.2,relheight=0.05)        
        self.giris = Label(text = "C1-C2 = "+str(round(C3)),bg='red', fg='black',font="Times 20 bold").place(relx = 0.73, rely = 0.76, relwidth=0.2,relheight=0.05)                
        ım2= PIL.Image.open("gozA1.png")
        ım3= PIL.Image.open("gozA2.png")        
        ım5= PIL.Image.open("gozB2.png")
        ım6= PIL.Image.open("gozB1.png")
        ım8= PIL.Image.open("gozC2.png")
        ım9= PIL.Image.open("gozC1.png") 
        K1= PIL.Image.open("A1.png")
        K2= PIL.Image.open("A2.png")        
        L1= PIL.Image.open("B1.png")
        L2= PIL.Image.open("B2.png")
        M1= PIL.Image.open("C1.png")
        M2= PIL.Image.open("C2.png") 
        photo2 = PIL.ImageTk.PhotoImage(ım2)
        photo3 = PIL.ImageTk.PhotoImage(ım3)        
        photo5 = PIL.ImageTk.PhotoImage(ım5)
        photo6 = PIL.ImageTk.PhotoImage(ım6)
        photo8 = PIL.ImageTk.PhotoImage(ım8)
        photo9 = PIL.ImageTk.PhotoImage(ım9)
        K1 = PIL.ImageTk.PhotoImage(K1)
        K2 = PIL.ImageTk.PhotoImage(K2)        
        L1 = PIL.ImageTk.PhotoImage(L1)
        L2 = PIL.ImageTk.PhotoImage(L2)
        M1 = PIL.ImageTk.PhotoImage(M1)
        M2 = PIL.ImageTk.PhotoImage(M2)      
        self.label=Label(window,image=photo2,bg='black').place(relx = 0.15, rely = 0.1, relwidth=0.08,relheight=0.15)
        self.label=Label(window,image=photo3,bg='black').place(relx = 0.23, rely = 0.1, relwidth=0.08,relheight=0.15)
        self.label=Label(window,image=photo5,bg='black').place(relx = 0.15, rely = 0.38, relwidth=0.08,relheight=0.15)
        self.label=Label(window,image=photo6,bg='black').place(relx = 0.23, rely = 0.38, relwidth=0.08,relheight=0.15)        
        self.label=Label(window,image=photo8,bg='black').place(relx = 0.15, rely = 0.66, relwidth=0.08,relheight=0.15)
        self.label=Label(window,image=photo9,bg='black').place(relx = 0.23, rely = 0.66, relwidth=0.08,relheight=0.15)                
        self.label=Label(window,image=K1,bg='black').place(relx = 0.40, rely = 0.10, relwidth=0.08,relheight=0.15)
        self.label=Label(window,image=K2,bg='black').place(relx = 0.48, rely = 0.10, relwidth=0.08,relheight=0.15)
        self.label=Label(window,image=L1,bg='black').place(relx = 0.40, rely = 0.38, relwidth=0.08,relheight=0.15)
        self.label=Label(window,image=L2,bg='black').place(relx = 0.48, rely = 0.38, relwidth=0.08,relheight=0.15)        
        self.label=Label(window,image=M1,bg='black').place(relx = 0.40, rely = 0.66, relwidth=0.08,relheight=0.15)
        self.label=Label(window,image=M2,bg='black').place(relx = 0.48, rely = 0.66, relwidth=0.08,relheight=0.15)                
        self.label.image=photo2
        self.label.image=photo3
        self.label.image=photo5
        self.label.image=photo6
        self.label.image=photo8
        self.label.image=photo9 
        self.label.image=K1
        self.label.image=K2
        self.label.image=L1
        self.label.image=L2
        self.label.image=M1
        self.label.image=M2
        self.giris = Label(bg='blue').place(relx = 0.4, rely = 0.08, relwidth=0.2,relheight=0.2)         
        self.giris.pack()              
    def ekran_tedavi1(self):
        for widget in self.window.winfo_children(): 
            widget.destroy()       
        self.giris = Label(text = "Tedavi aşamasında\nkas gücü yetersiz olan göz çevresine\nelektrotlar bağlanıp labirentteki karakter \nçıkışa ulaştırılarak \nkaslar güçlendirilmeye \nçalışılacaktır.",font="Times 35 bold",fg='red').place(relx = 0.05, rely = 0.0, relwidth=0.9,relheight=0.5)
        self.btnc = Button(text="<--Geri", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.initt).place(relx = 0.9, rely = 0.9, relwidth=0.1,relheight=0.1)
        self.btn = Button(text="BAŞLA", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.ekran_tedavi2).place(relx = 0.55, rely = 0.53, relwidth=0.2,relheight=0.2)  
        
        ımg= PIL.Image.open("img.png")
        ımg = PIL.ImageTk.PhotoImage(ımg)
        self.label=Label(window,image=ımg,bg='black').place(relx = 0.2, rely = 0.5, relwidth=0.24,relheight=0.28)
        self.label.image=ımg  
        self.btn.pack()

    def ekran_tedavi2(self):
        for widget in self.window.winfo_children(): 
            widget.destroy() 
        self.giris = Label(text = "OYUN KATEGORİLERİ",bg='red', fg='yellow',font="Times 30 bold").place(relx = 0.0, rely = 0.0, relwidth=1,relheight=0.1)                
        self.btnc = Button(text="<--Geri", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.ekran_tedavi1).place(relx = 0.9, rely = 0.9, relwidth=0.1,relheight=0.1)
        
        self.btnc = Button(text="Sağ Üst\nRektus Kası\nGüçlendirme", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.boş).place(relx = 0.015, rely = 0.2, relwidth=0.12,relheight=0.2)
        self.btnc = Button(text="Sağ Alt\nRektus Kası\nGüçlendirme", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.boş).place(relx = 0.185, rely = 0.2, relwidth=0.12,relheight=0.2)
        self.btnc = Button(text="Sağ İç\nRektus Kası\nGüçlendirme", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.boş).place(relx = 0.355, rely = 0.2, relwidth=0.12,relheight=0.2)
        self.btnc = Button(text="Sağ Dış\nRektus Kası\nGüçlendirme", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.boş).place(relx = 0.525, rely = 0.2, relwidth=0.12,relheight=0.2)
        self.btnc = Button(text="Sağ Üst\nOblik Kası\nGüçlendirme", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.boş).place(relx = 0.695, rely = 0.2, relwidth=0.12,relheight=0.2)
        self.btnc = Button(text="Sağ Alt\nOblik Kası\nGüçlendirme", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.boş).place(relx = 0.865, rely = 0.2, relwidth=0.12,relheight=0.2)
        
        self.btnc = Button(text="Sol Üst\nRektus Kası\nGüçlendirme", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.boş).place(relx = 0.015, rely = 0.45, relwidth=0.12,relheight=0.2)
        self.btnc = Button(text="Sol Alt\nRektus Kası\nGüçlendirme", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.boş).place(relx = 0.185, rely = 0.45, relwidth=0.12,relheight=0.2)
        self.btnc = Button(text="Sol İç\nRektus Kası\nGüçlendirme", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.boş).place(relx = 0.355, rely = 0.45, relwidth=0.12,relheight=0.2)
        self.btnc = Button(text="Sol Dış\nRektus Kası\nGüçlendirme", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.boş).place(relx = 0.525, rely = 0.45, relwidth=0.12,relheight=0.2)
        self.btnc = Button(text="Sol Üst\nOblik Kası\nGüçlendirme", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.boş).place(relx = 0.695, rely = 0.45, relwidth=0.12,relheight=0.2)
        self.btnc = Button(text="Sol Alt\nOblik Kası\nGüçlendirme", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.boş).place(relx = 0.865, rely = 0.45, relwidth=0.12,relheight=0.2)
        self.btnc = Button(text="Genel\n(Tüm Kaslar)", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.ekran_tedavi3).place(relx = 0.44, rely = 0.7, relwidth=0.12,relheight=0.2)
        
    def boş(self):
        for widget in self.window.winfo_children(): 
            widget.destroy()    
        self.btnc = Button(text="<--Geri", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.ekran_tedavi2).place(relx = 0.9, rely = 0.9, relwidth=0.1,relheight=0.1)
        self.giris = Label(text = " Bu aşamalar henüz tamamlanmadı...",bg='grey', fg='red',font="Times 30 bold").place(relx = 0.0, rely = 0.3, relwidth=1,relheight=0.1)                
#################################################        
    def ekran_tedavi3(self):
        for widget in self.window.winfo_children(): 
            widget.destroy()    
        self.giris = Label( bg='yellow').place(relx = 0.0, rely = 0.0, relwidth=1,relheight=0.03)       
        self.giris = Label( bg='yellow').place(relx = 0.0, rely = 0.0, relwidth=0.02,relheight=1)       
        self.giris = Label( bg='yellow').place(relx = 0.98, rely = 0.0, relwidth=0.02,relheight=0.9)          
        self.btnc = Button(text="<--Geri", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.ekran_tedavi2).place(relx = 0.9, rely = 0.9, relwidth=0.1,relheight=0.1)
        self.giris = Label( bg='red').place(relx = 0.2, rely = 0.2, relwidth=0.6,relheight=0.44)       
        self.giris = Label( bg='black').place(relx = 0.2, rely = 0.22, relwidth=0.02,relheight=0.43)
        self.giris = Label( bg='black').place(relx = 0.78, rely = 0.2, relwidth=0.02,relheight=0.45)       
        self.giris = Label( bg='white').place(relx = 0.35, rely = 0.22, relwidth=0.01,relheight=0.42)
        self.giris = Label( bg='white').place(relx = 0.5, rely = 0.22, relwidth=0.01,relheight=0.42)
        self.giris = Label( bg='white').place(relx = 0.65, rely = 0.22, relwidth=0.01,relheight=0.42)   
        self.giris = Label( bg='black').place(relx = 0.2, rely = 0.2, relwidth=0.46,relheight=0.02)
        self.giris = Label( bg='black').place(relx = 0.35, rely = 0.34, relwidth=0.45,relheight=0.02)
        self.giris = Label( bg='black').place(relx = 0.2, rely = 0.48, relwidth=0.46,relheight=0.02)
        self.giris = Label( bg='black').place(relx = 0.35, rely = 0.62, relwidth=0.45,relheight=0.02)        
        ımg1= PIL.Image.open("img11.png")
        ımg2= PIL.Image.open("img2.png")
        ımg1 = PIL.ImageTk.PhotoImage(ımg1)
        ımg2 = PIL.ImageTk.PhotoImage(ımg2)
        self.label=Label(window,image=ımg1,bg='blue').place(relx = 0.23, rely = 0.51, relwidth=0.1,relheight=0.1)
        self.label=Label(window,image=ımg2,bg='blue').place(relx = 0.68, rely = 0.14, relwidth=0.08,relheight=0.12)
        self.label.image=ımg1
        self.label.image=ımg2
        self.giris.pack()
        
    def ekran_tedavi4(self):
        for widget in self.window.winfo_children(): 
            widget.destroy()    
        self.giris = Label( bg='yellow').place(relx = 0.0, rely = 0.0, relwidth=1,relheight=0.03)       
        self.giris = Label( bg='yellow').place(relx = 0.0, rely = 0.0, relwidth=0.02,relheight=1)       
        self.giris = Label( bg='yellow').place(relx = 0.98, rely = 0.0, relwidth=0.02,relheight=0.9)          
        self.btnc = Button(text="<--Geri", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.ekran_tedavi3).place(relx = 0.9, rely = 0.9, relwidth=0.1,relheight=0.1)
        self.giris = Label( bg='red').place(relx = 0.2, rely = 0.2, relwidth=0.6,relheight=0.44)       
        self.giris = Label( bg='black').place(relx = 0.2, rely = 0.22, relwidth=0.02,relheight=0.43)
        self.giris = Label( bg='black').place(relx = 0.78, rely = 0.2, relwidth=0.02,relheight=0.45)       
        self.giris = Label( bg='white').place(relx = 0.35, rely = 0.22, relwidth=0.01,relheight=0.42)
        self.giris = Label( bg='white').place(relx = 0.5, rely = 0.22, relwidth=0.01,relheight=0.42)
        self.giris = Label( bg='white').place(relx = 0.65, rely = 0.22, relwidth=0.01,relheight=0.42)   
        self.giris = Label( bg='black').place(relx = 0.2, rely = 0.2, relwidth=0.46,relheight=0.02)
        self.giris = Label( bg='black').place(relx = 0.35, rely = 0.34, relwidth=0.45,relheight=0.02)
        self.giris = Label( bg='black').place(relx = 0.2, rely = 0.48, relwidth=0.46,relheight=0.02)
        self.giris = Label( bg='black').place(relx = 0.35, rely = 0.62, relwidth=0.45,relheight=0.02)        
        ımg1= PIL.Image.open("img11.png")
        ımg2= PIL.Image.open("img2.png")
        ımg1 = PIL.ImageTk.PhotoImage(ımg1)
        ımg2 = PIL.ImageTk.PhotoImage(ımg2)
        self.label=Label(window,image=ımg1,bg='blue').place(relx = 0.23, rely = 0.51, relwidth=0.1,relheight=0.1)
        self.label=Label(window,image=ımg2,bg='blue').place(relx = 0.68, rely = 0.14, relwidth=0.08,relheight=0.12)
        self.label.image=ımg1
        self.label.image=ımg2
        self.giris.pack()
        
    def ekran_tedavi5(self):
        for widget in self.window.winfo_children(): 
            widget.destroy()    
        self.giris = Label( bg='yellow').place(relx = 0.0, rely = 0.0, relwidth=1,relheight=0.03)       
        self.giris = Label( bg='yellow').place(relx = 0.0, rely = 0.0, relwidth=0.02,relheight=1)       
        self.giris = Label( bg='yellow').place(relx = 0.98, rely = 0.0, relwidth=0.02,relheight=0.9)          
        self.btnc = Button(text="<--Geri", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.ekran_tedavi4).place(relx = 0.9, rely = 0.9, relwidth=0.1,relheight=0.1)
        self.giris = Label( bg='red').place(relx = 0.2, rely = 0.2, relwidth=0.6,relheight=0.44)       
        self.giris = Label( bg='black').place(relx = 0.2, rely = 0.22, relwidth=0.02,relheight=0.43)
        self.giris = Label( bg='black').place(relx = 0.78, rely = 0.2, relwidth=0.02,relheight=0.45)       
        self.giris = Label( bg='white').place(relx = 0.35, rely = 0.22, relwidth=0.01,relheight=0.42)
        self.giris = Label( bg='white').place(relx = 0.5, rely = 0.22, relwidth=0.01,relheight=0.42)
        self.giris = Label( bg='white').place(relx = 0.65, rely = 0.22, relwidth=0.01,relheight=0.42)   
        self.giris = Label( bg='black').place(relx = 0.2, rely = 0.2, relwidth=0.46,relheight=0.02)
        self.giris = Label( bg='black').place(relx = 0.35, rely = 0.34, relwidth=0.45,relheight=0.02)
        self.giris = Label( bg='black').place(relx = 0.2, rely = 0.48, relwidth=0.46,relheight=0.02)
        self.giris = Label( bg='black').place(relx = 0.35, rely = 0.62, relwidth=0.45,relheight=0.02)        
        ımg1= PIL.Image.open("img11.png")
        ımg2= PIL.Image.open("img2.png")
        ımg1 = PIL.ImageTk.PhotoImage(ımg1)
        ımg2 = PIL.ImageTk.PhotoImage(ımg2)
        self.label=Label(window,image=ımg1,bg='blue').place(relx = 0.23, rely = 0.51, relwidth=0.1,relheight=0.1)
        self.label=Label(window,image=ımg2,bg='blue').place(relx = 0.68, rely = 0.14, relwidth=0.08,relheight=0.12)
        self.label.image=ımg1
        self.label.image=ımg2
        self.giris.pack()    
        
    def ekran_tedavi6(self):
        for widget in self.window.winfo_children(): 
            widget.destroy()    
        self.giris = Label( bg='yellow').place(relx = 0.0, rely = 0.0, relwidth=1,relheight=0.03)       
        self.giris = Label( bg='yellow').place(relx = 0.0, rely = 0.0, relwidth=0.02,relheight=1)       
        self.giris = Label( bg='yellow').place(relx = 0.98, rely = 0.0, relwidth=0.02,relheight=0.9)          
        self.btnc = Button(text="<--Geri", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.ekran_tedavi5).place(relx = 0.9, rely = 0.9, relwidth=0.1,relheight=0.1)
        self.giris = Label( bg='red').place(relx = 0.2, rely = 0.2, relwidth=0.6,relheight=0.44)       
        self.giris = Label( bg='black').place(relx = 0.2, rely = 0.22, relwidth=0.02,relheight=0.43)
        self.giris = Label( bg='black').place(relx = 0.78, rely = 0.2, relwidth=0.02,relheight=0.45)       
        self.giris = Label( bg='white').place(relx = 0.35, rely = 0.22, relwidth=0.01,relheight=0.42)
        self.giris = Label( bg='white').place(relx = 0.5, rely = 0.22, relwidth=0.01,relheight=0.42)
        self.giris = Label( bg='white').place(relx = 0.65, rely = 0.22, relwidth=0.01,relheight=0.42)   
        self.giris = Label( bg='black').place(relx = 0.2, rely = 0.2, relwidth=0.46,relheight=0.02)
        self.giris = Label( bg='black').place(relx = 0.35, rely = 0.34, relwidth=0.45,relheight=0.02)
        self.giris = Label( bg='black').place(relx = 0.2, rely = 0.48, relwidth=0.46,relheight=0.02)
        self.giris = Label( bg='black').place(relx = 0.35, rely = 0.62, relwidth=0.45,relheight=0.02)        
        ımg1= PIL.Image.open("img11.png")
        ımg2= PIL.Image.open("img2.png")
        ımg1 = PIL.ImageTk.PhotoImage(ımg1)
        ımg2 = PIL.ImageTk.PhotoImage(ımg2)
        self.label=Label(window,image=ımg1,bg='blue').place(relx = 0.23, rely = 0.51, relwidth=0.1,relheight=0.1)
        self.label=Label(window,image=ımg2,bg='blue').place(relx = 0.68, rely = 0.14, relwidth=0.08,relheight=0.12)
        self.label.image=ımg1
        self.label.image=ımg2
        self.giris.pack()
        
    def ekran_tedavi7(self):
        for widget in self.window.winfo_children(): 
            widget.destroy()    
        self.giris = Label( bg='yellow').place(relx = 0.0, rely = 0.0, relwidth=1,relheight=0.03)       
        self.giris = Label( bg='yellow').place(relx = 0.0, rely = 0.0, relwidth=0.02,relheight=1)       
        self.giris = Label( bg='yellow').place(relx = 0.98, rely = 0.0, relwidth=0.02,relheight=0.9)          
        self.btnc = Button(text="<--Geri", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.ekran_tedavi6).place(relx = 0.9, rely = 0.9, relwidth=0.1,relheight=0.1)
        self.giris = Label( bg='red').place(relx = 0.2, rely = 0.2, relwidth=0.6,relheight=0.44)       
        self.giris = Label( bg='black').place(relx = 0.2, rely = 0.22, relwidth=0.02,relheight=0.43)
        self.giris = Label( bg='black').place(relx = 0.78, rely = 0.2, relwidth=0.02,relheight=0.45)       
        self.giris = Label( bg='white').place(relx = 0.35, rely = 0.22, relwidth=0.01,relheight=0.42)
        self.giris = Label( bg='white').place(relx = 0.5, rely = 0.22, relwidth=0.01,relheight=0.42)
        self.giris = Label( bg='white').place(relx = 0.65, rely = 0.22, relwidth=0.01,relheight=0.42)   
        self.giris = Label( bg='black').place(relx = 0.2, rely = 0.2, relwidth=0.46,relheight=0.02)
        self.giris = Label( bg='black').place(relx = 0.35, rely = 0.34, relwidth=0.45,relheight=0.02)
        self.giris = Label( bg='black').place(relx = 0.2, rely = 0.48, relwidth=0.46,relheight=0.02)
        self.giris = Label( bg='black').place(relx = 0.35, rely = 0.62, relwidth=0.45,relheight=0.02)        
        ımg1= PIL.Image.open("img11.png")
        ımg2= PIL.Image.open("img2.png")
        ımg1 = PIL.ImageTk.PhotoImage(ımg1)
        ımg2 = PIL.ImageTk.PhotoImage(ımg2)
        self.label=Label(window,image=ımg1,bg='blue').place(relx = 0.23, rely = 0.51, relwidth=0.1,relheight=0.1)
        self.label=Label(window,image=ımg2,bg='blue').place(relx = 0.68, rely = 0.14, relwidth=0.08,relheight=0.12)
        self.label.image=ımg1
        self.label.image=ımg2
        self.giris.pack()
        
    def ekran_tedavi8(self):
        for widget in self.window.winfo_children(): 
            widget.destroy()    
        self.giris = Label( bg='yellow').place(relx = 0.0, rely = 0.0, relwidth=1,relheight=0.03)       
        self.giris = Label( bg='yellow').place(relx = 0.0, rely = 0.0, relwidth=0.02,relheight=1)       
        self.giris = Label( bg='yellow').place(relx = 0.98, rely = 0.0, relwidth=0.02,relheight=0.9)          
        self.btnc = Button(text="<--Geri", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.ekran_tedavi7).place(relx = 0.9, rely = 0.9, relwidth=0.1,relheight=0.1)
        self.giris = Label( bg='red').place(relx = 0.2, rely = 0.2, relwidth=0.6,relheight=0.44)       
        self.giris = Label( bg='black').place(relx = 0.2, rely = 0.22, relwidth=0.02,relheight=0.43)
        self.giris = Label( bg='black').place(relx = 0.78, rely = 0.2, relwidth=0.02,relheight=0.45)       
        self.giris = Label( bg='white').place(relx = 0.35, rely = 0.22, relwidth=0.01,relheight=0.42)
        self.giris = Label( bg='white').place(relx = 0.5, rely = 0.22, relwidth=0.01,relheight=0.42)
        self.giris = Label( bg='white').place(relx = 0.65, rely = 0.22, relwidth=0.01,relheight=0.42)   
        self.giris = Label( bg='black').place(relx = 0.2, rely = 0.2, relwidth=0.46,relheight=0.02)
        self.giris = Label( bg='black').place(relx = 0.35, rely = 0.34, relwidth=0.45,relheight=0.02)
        self.giris = Label( bg='black').place(relx = 0.2, rely = 0.48, relwidth=0.46,relheight=0.02)
        self.giris = Label( bg='black').place(relx = 0.35, rely = 0.62, relwidth=0.45,relheight=0.02)        
        ımg1= PIL.Image.open("img11.png")
        ımg2= PIL.Image.open("img2.png")
        ımg1 = PIL.ImageTk.PhotoImage(ımg1)
        ımg2 = PIL.ImageTk.PhotoImage(ımg2)
        self.label=Label(window,image=ımg1,bg='blue').place(relx = 0.23, rely = 0.51, relwidth=0.1,relheight=0.1)
        self.label=Label(window,image=ımg2,bg='blue').place(relx = 0.68, rely = 0.14, relwidth=0.08,relheight=0.12)
        self.label.image=ımg1
        self.label.image=ımg2
        self.giris.pack()
        
    def ekran_tedavi9(self):
        for widget in self.window.winfo_children(): 
            widget.destroy()    
        self.giris = Label( bg='yellow').place(relx = 0.0, rely = 0.0, relwidth=1,relheight=0.03)       
        self.giris = Label( bg='yellow').place(relx = 0.0, rely = 0.0, relwidth=0.02,relheight=1)       
        self.giris = Label( bg='yellow').place(relx = 0.98, rely = 0.0, relwidth=0.02,relheight=0.9)          
        self.btnc = Button(text="<--Geri", fg='red',bg='black',font="Times 20 bold", cursor="bottom_side",command=self.ekran_tedavi8).place(relx = 0.9, rely = 0.9, relwidth=0.1,relheight=0.1)
        self.giris = Label( bg='red').place(relx = 0.2, rely = 0.2, relwidth=0.6,relheight=0.44)       
        self.giris = Label( bg='black').place(relx = 0.2, rely = 0.22, relwidth=0.02,relheight=0.43)
        self.giris = Label( bg='black').place(relx = 0.78, rely = 0.2, relwidth=0.02,relheight=0.45)       
        self.giris = Label( bg='white').place(relx = 0.35, rely = 0.22, relwidth=0.01,relheight=0.42)
        self.giris = Label( bg='white').place(relx = 0.5, rely = 0.22, relwidth=0.01,relheight=0.42)
        self.giris = Label( bg='white').place(relx = 0.65, rely = 0.22, relwidth=0.01,relheight=0.42)   
        self.giris = Label( bg='black').place(relx = 0.2, rely = 0.2, relwidth=0.46,relheight=0.02)
        self.giris = Label( bg='black').place(relx = 0.35, rely = 0.34, relwidth=0.45,relheight=0.02)
        self.giris = Label( bg='black').place(relx = 0.2, rely = 0.48, relwidth=0.46,relheight=0.02)
        self.giris = Label( bg='black').place(relx = 0.35, rely = 0.62, relwidth=0.45,relheight=0.02)        
        ımg1= PIL.Image.open("img11.png")
        ımg2= PIL.Image.open("img2.png")
        ımg1 = PIL.ImageTk.PhotoImage(ımg1)
        ımg2 = PIL.ImageTk.PhotoImage(ımg2)
        self.label=Label(window,image=ımg1,bg='blue').place(relx = 0.23, rely = 0.51, relwidth=0.1,relheight=0.1)
        self.label=Label(window,image=ımg2,bg='blue').place(relx = 0.68, rely = 0.14, relwidth=0.08,relheight=0.12)
        self.label.image=ımg1
        self.label.image=ımg2
        self.giris.pack()
    
window = Tk()
uygulama=log_in(window)
window.mainloop()

