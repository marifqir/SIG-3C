import shapefile as shp #import library shapfile sebagai shp
w=shp.Writer('soal10', shapeType=5) #membuat file bernama soal9 yang berisi gambar polygon sesuai dengan shaptype 5 yaitu polygon
 
w.field("kolom1","C") #membuat table kolom pertama 
w.field("kolom2","C") #membuat table kolom kedua
 
w.record("record1","record1") #isi untuk kolom pertama dan kedua
w.record("record2","record2") #isi untuk kolom pertama dan kedua
w.record("record3","record3") #isi untuk kolom pertama dan kedua
w.record("record4","record4") #isi untuk kolom pertama dan kedua
w.record("record5","record5") #isi untuk kolom pertama dan kedua
w.record("record6","record6") #isi untuk kolom pertama dan kedua

w.poly([[[-2.7,-3.4],[-3.1,-3],[-5.1,-5],[-4.7,-5.4],[-2.7,-3.4]]])#membuat garis dengan titik yang ada sebagai acuannya
w.poly([[[-0.9,-5.6],[-0.4,-5.1],[-2.7,-2.6],[-3.1,-3],[-0.9,-5.6]]])#membuat garis dengan titik yang ada sebagai acuannya
w.poly([[[-1.7,-5.9],[4.5,0.5],[3.9,1.2],[-2.4,-5.1],[-1.7,-5.9]]])#membuat garis dengan titik yang ada sebagai acuannya
w.poly([[[4,-6],[-3.6,3],[-2.8,3.8],[5,-5],[4,-6]]])#membuat garis dengan titik yang ada sebagai acuannya
w.poly([[[-3.6,1],[-1,3.7],[-1.9,4.6],[-4.5,2],[-3.6,1]]])#membuat garis dengan titik yang ada sebagai acuannya
w.poly([[[3.2,0.5],[3.9,1.2],[1.2,4.2],[0.6,3.6],[3.2,0.5]]])#membuat garis dengan titik yang ada sebagai acuannya
 

w.close() # Menutup penggambar (writer) karena kita sudah beres menggambar yang kita perlukan
