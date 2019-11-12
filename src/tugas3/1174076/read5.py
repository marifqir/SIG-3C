# Mengimport modul shapefile
import shapefile

# Menjalankan function reader yang berada pada modul shapefile yang berguna untuk membuka file
sf = shapefile.Reader("read")

# Mengambil semua record
anu = sf.shapes()

# Untuk mengetahui isi object
dir(anu)

# Untuk mengetahui isi object dengan index ke-0
dir(anu[0])