# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 22:00:56 2019

@author: User
"""

import shapefile #mengimport libray
sf = shapefile.Reader("Nomor10") #membaca file shpaefile
isidata = sf.records() #membaca isi record dan dimasukkan kedalam variable
print(isidata[0]) #membaca array pertama 
print(isidata[0][0]) #membaca multiarray