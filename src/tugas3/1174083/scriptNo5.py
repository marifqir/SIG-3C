# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:25:25 2019

@author: bakti
"""
import shapefile #mengimport shapefile

sf = shapefile.Reader("contohFile") #untuk membaca file tanpa menggunakan ekstensi
anu=sf.shapes() #untuk menyimpan variable sf di dalam anu
dir(anu) #isi dari objek anu
dir(anu[0]) #isi didalam array anu yang pertama

# In[]