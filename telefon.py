# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 21:00:15 2019

@author: enki06
"""

isim=input("aradığınız kişinin adını soyadını giriniz")
from tkinter import messagebox
while True:
    
        
    if isim=="Funda Tamdoğan":
        messagebox.showinfo(isim,"dahili 2712 Cep 0553 353 7882")
        yeniisim=input("aradığınız yeni kişinin adı ve soyadı")
    if isim=="Nazan Tamdoğan":
        messagebox.showinfo(isim,"Dahili 2648 Cep 0542 456 7886")
        yeniisim=input("aradığınız yeni kişinin adı ve soyadı")
    if yeniisim=="quit":
        break
