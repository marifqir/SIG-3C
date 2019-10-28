# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:52:25 2019

@author: User
"""

import shapefile #mengimport library 
sf = shapefile.Reader("Nomor10") #membaca file shpaefile
namakolom = sf.fields #memasukan nama fields dari file yang dibaca kedalam variable
print(namakolom) #menampilkan isi dari variable "namakolom"