import shapefile as shp # import library shapfile sebagai shp
r   = shp.Reader("soal10.py") # vairabel dengan yang berisi shapfile reader untuk membaca file soal10.py
sf  = r.shapes() # mengembalikan list object shape dari setiap record yang ada
print (sf[0].parts) # print parts dari point yang sudah di kelompokkan menjadi shape
