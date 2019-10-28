# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:46:08 2019

@author: User
"""

import shapefile #mengimport library
sf = shapefile.Reader("Nomor1") #membaca file shapefile
anu=sf.shapes() #menyimpan kedalam variable
dir(anu) #melihat isi objek
print(dir(anu[0])) #melihan isi objek dalam array