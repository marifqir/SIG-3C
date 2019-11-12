import shapefile as shp # import library shapfile sebagai shp
r   = shp.Reader("soal10.py") # vairabel dengan yang berisi shapfile reader untuk membaca file soal10.py
isidata = r.records() # implementasi method shapefile record sebagai variabel
print(isidata[0]) # print list dari shapefile record yang dipanggil
print(isidata[0][0]) # print list dari shapefile record yang dipanggil
