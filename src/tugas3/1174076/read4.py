
# Mengimport modul shapefile
import shapefile

# Menjalankan function reader yang berada pada modul shapefile yang berguna untuk membuka file
sf = shapefile.Reader("read")

# Mengambil semua record
anu = sf.shapes()

# Menampilkan panjang dari sebuah object
len(anu)