# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 22:42:58 2019

@author: ADVENT
"""

import shapefile # Meng-import library shapefile
sf = shapefile.Reader("No10") # Berguna untuk membaca file dari nama filenya tanpa ekstensi
sf.bbox # Berguna untuk membaca batas (boundary) dari box atau kotak