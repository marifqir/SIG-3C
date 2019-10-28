# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:47:58 2019

@author: User
"""

import shapefile #mengimport library
sf = shapefile.Reader("Nomor1") #membaca file shapefile
anu=sf.shapes() #menyimpan hasil kedalam variable 
print(anu[0].parts) #membaca data yang pertama didalam "anu", parts menjadikan satu dari beberapa records