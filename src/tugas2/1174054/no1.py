# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:49:41 2019

@author: Aulyardha Anindita
"""

#nomor1

import shapefile #Berfungsi untuk mengimport library shapefile
w=shapefile.Writer("Nomor 1") #membuat writer
w.shapeType=1 #membuat shapetype yaitu 1

w.field("kolom1","C") #Membuat table kolom pertama
w.field("kolom2","C") #Membuat table kolom kedua

w.record("ngek","satu") #Membuat isi table pada kolom pertama
w.record("ngok","dua") #Membuat isi table pada kolom kedua

w.point(1,1) #Menggambarkan point (titik) pada koordinat x,y yaitu 1,1
w.point(2,2) #Menggambarkan point (titik) pada koordinat x,y yaitu 2,2

w.close() #Menutup Writer