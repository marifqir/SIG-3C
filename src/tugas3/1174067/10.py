import shapefile as shp # import library shapfile sebagai shp
r   = shp.Reader("soal10.py") # vairabel dengan yang berisi shapfile reader untuk membaca file soal10.py
isidata = r.records() # implementasi method shapefile record sebagai variabel
print(isidata) # print list dari shapefile record yang dipanggil
