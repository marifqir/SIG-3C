# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:09:06 2019

@author: User
"""

import shapefile #mengimport library shapefile
w=shapefile.Writer('Nomor1') #membuat shapefile dengan nama writer dengan shapetype default yaitu 1
 
w.field("kolom1","C") #membiri nama field dengan nama "kolom1" dengan tipe data "character"
w.field("kolom2","C") #membiri nama field dengan nama "kolom2" dengan tipe data "character"
 
w.record("ngek","satu") #mengisi tabel kolom1 yaitu ngok dan kolom2 yaitu satu
w.record("ngok","dua") #mengisi tabel kolom1 yaitu ngok dan kolom2 yaitu dua
 
w.point(1,1) #menggambarkan point pada koordinat x,y
w.point(2,2) #menggambarkan point pada koordinat x,y
 
w.close()   #menutup wroter