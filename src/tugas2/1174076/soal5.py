# Mengimport modul shapefile
import shapefile

# Inisiasikan variabel w, untuk membuat file shapefile baru
w = shapefile.Writer('soal5')

# Mengecek set variabel w, apakah point, line atau polygon, Kalau koosong berarti tidak di set
w.shapeType=3

# Membuat field tabel atau file dengan format .dbf, C = Tipe data Character
w.field("kolom1","C")
w.field("kolom2","C")

# Membuat row tabel atau isi tabel
w.record("ngek","satu")

# Menghubungkan titik yang ada pada gambar dengan sebuah garis, menggunakan function line()
w.line([[[1,5],[5,5],[5,1],[3,3],[1,1]]])

# Menutup function writer
w.close()
