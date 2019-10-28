# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:45:02 2019

@author: User
"""

import shapefile #import library
sf = shapefile.Reader("Nomor1") #membaca file shapefile
anu=sf.shapes() #melihat bentuk yang yang ada pada "nomor1.py"
print(len(anu)) #menghitung jumlah yang ada dalam "anu"