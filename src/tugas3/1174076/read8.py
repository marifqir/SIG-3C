# Mengimport modul shapefile
import shapefile

# Menjalankan function reader yang berada pada modul shapefile yang berguna untuk membuka file
sf = shapefile.Reader("read")

# Mengambil semua record
anu = sf.shapes()

# Menampilkan koordinat (x, y) untuk setiap titik dalam bentuk pada variabel anu index 0
anu[0].points