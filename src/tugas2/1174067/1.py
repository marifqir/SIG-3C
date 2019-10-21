import shapefile as shp #import library shapfile sebagai shp
w=shp.Writer('soal1',shapeType=1) #membuat file bernama soal1 yang berisi gambar titik atau point sesuai dengan shaptype 1 yaitu point
 
w.field("kolom1","C") #membuat table kolom pertama 
w.field("kolom2","C") #membuat table kolom kedua
 
w.record("ngek","satu") #isi untuk kolom pertama dan kedua
w.record("ngok","dua") #isi untuk kolom pertama dan kedua
 
w.point(1,1) #membuat poin pada koordinat x=1 dan y=1
w.point(2,2) #membuat poin pada koordinat x=2 dan y=2
 
w.close() #menutup writer
