# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:06:43 2019

@author: PandA23
"""

import shapefile #mengimport shapefile
sf = shapefile.Reader("contohaja") #digunakan untuk membaca file tanpa menggunakan ekstensi
anu=sf.shapes() #untuk menyimpan variable sf di dalam anu
#%%
dir(anu) #isi objek anu
#%%
dir(anu[0]) #isi didalam array anu yang pertama