# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:50:06 2019

@author: User
"""

import shapefile #mengimport library
sf = shapefile.Reader("Nomor1") #membaca file shapefile
anu=sf.shapes() #menyimpan hasil kedalam variable
print(anu[0].points) #melihat daftar tupel yang berisi koordinat pada variable anu data yang pertama