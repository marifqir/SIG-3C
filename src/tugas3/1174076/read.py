# Mengimport modul shapefile
import shapefile

# Inisiasikan variabel w, untuk membuat file shapefile baru
w = shapefile.Writer('read')

# Mengecek set variabel w
w.shapeType=1

# Membuat field tabel atau file dengan format .dbf, C = Tipe data Character
w.field("kolom1","C")
w.field("kolom2","C")

# Membuat row tabel atau isi tabel
w.record("ngek","satu")
w.record("ngok","dua")

# Mengisi file berformat .shp dengan point(titik), dengan koordinat x, y
w.point(1,1)
w.point(2,2)

# Menutup function writer
w.close()
