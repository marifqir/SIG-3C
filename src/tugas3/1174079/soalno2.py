# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 20:00:41 2019

@author: ACER
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 19:07:30 2019

@author: ACER
"""

import shapefile # Meng-import library shapefile
sf = shapefile.Reader("no6.py") # menggunakan fungsi reader yang ada pada shapefile untuk membaca file no6.py
print(sf.shapeType) #mengeluarkan input field dari sf yang berisi no6.py
