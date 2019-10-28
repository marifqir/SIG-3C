# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:08:40 2019

@author: PandA23
"""

import shapefile #mengimprot shapefile
sf = shapefile.Reader("contohaja") #digunakan untuk membaca file 
 #%%
sf.shapeType #untuk membaca type shape berapakah yang digunakan