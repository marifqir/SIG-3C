# Mengimport modul shapefile
import shapefile

# Inisiasikan variabel w, untuk membuat file shapefile baru
w = shapefile.Writer('soal10')

# Mengecek set variabel w, apakah point, line atau polygon, Kalau koosong berarti tidak di set
w.shapeType=5

# Membuat field tabel atau file dengan format .dbf, C = Tipe data Character
w.field("kolom1","C")
w.field("kolom2","C")

# Membuat row tabel atau isi tabel
w.record("hiji","satu")
w.record("dua","dua")
w.record("tilu","tiga")
w.record("opat","empat")
w.record("lima","lima")
w.record("genep","enam")
w.record("tujuh","tujuh")

# Membuat sebuah jajar genjang
w.poly([[[1,1],[3,5],[7,5],[5,1],[1,1]]])
w.poly([[[-1,-1],[-3,-5],[-7,-5],[-5,-1],[-1,-1]]])
w.poly([[[1,-1],[3,-5],[7,-5],[5,-1],[1,-1]]])
w.poly([[[-1,1],[-3,5],[-7,5],[-5,1],[-1,1]]])
w.poly([[[3,7],[7,7],[5,11],[1,11],[3,7]]])
w.poly([[[-3,7],[-7,7],[-5,11],[-1,11],[-3,7]]])
w.poly([[[9,5],[13,5],[15,1],[11,1],[9,5]]])

w.close
