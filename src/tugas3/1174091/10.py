# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 22:00:09 2019

@author: User
"""

import shapefile #mengimport library
sf = shapefile.Reader("Nomor10") #membaca file shapefile
isidata = sf.records() #membaca isi record dari variable sf dan memasukkan kedalam variable isidata
print(isidata) #menampilkan isi variable