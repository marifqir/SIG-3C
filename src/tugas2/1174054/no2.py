# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:53:03 2019

@author: Aulyardha Anindita
"""

#Nomor 2

import shapefile #Berfungsi untuk mengimport library shapefile
w=shapefile.Writer("Nomor 2", shapeType=1) #membuat writer dengan shapetype yaitu 1
w.shapeType

w.field("kolom1","C") #Membuat table kolom pertama
w.field("kolom2","C") #Membuat table kolom kedua

w.record("ngek","satu") #Membuat isi table pada kolom pertama
w.record("ngok","dua") #Membuat isi table pada kolom kedua

w.point(1,1) #Menggambarkan point (titik) pada koordinat x,y yaitu 1,1
w.point(2,2) #Menggambarkan point (titik) pada koordinat x,y yaitu 2,2

w.close() #Menutup Writer