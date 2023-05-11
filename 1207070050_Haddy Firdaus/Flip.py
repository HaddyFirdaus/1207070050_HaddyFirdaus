#Mengimport Library Modul numpy,image,matplotlib
import numpy as np#Mengimport library numpy
import imageio#Mengimport library imageio
import matplotlib.pyplot as plt#Mengimport matplotlib

# Membaca gambar  
img = imageio.imread("Mikasa.jpg")#membaca gambar dengan nama file "Mikasa.jpg" menggunakan library imageio

# Mendapatkan resolusi dan type dari gambar
img_height = img.shape[0]#mengambil tinggi (jumlah baris) dari gambar menggunakan atribut shape dari Numpy dan menyimpannya ke dalam variabel img_height.
img_width = img.shape[1]#mengambil lebar (jumlah kolom) dari gambar menggunakan atribut shape dari Numpy dan menyimpannya ke dalam variabel img_width.
img_channel = img.shape[2]#mengambil jumlah channel (misalnya RGB) dari gambar menggunakan atribut shape dari Numpy dan menyimpannya ke dalam variabel img_channel.
img_type = img.dtype#mengambil tipe data dari gambar menggunakan atribut dtype dari Numpy dan menyimpannya ke dalam variabel img_type.

# Membuat variabel dengan resolusi dan tipe yang sama seperti gambar
img_flip_horizontal = np.zeros(img.shape, img_type)#membuat variabel img_flip_horizontal dengan ukuran dan tipe data yang sama seperti gambar asli. 
img_flip_vertical = np.zeros(img.shape, img_type)#membuat variabel img_flip_vertical dengan ukuran dan tipe data yang sama seperti gambar asli. 

# Membalik gambar secara horizontal
for y in range(0, img_height):# loop untuk tinggi pada gambar.
    for x in range(0, img_width):# loop untuk lebar pada gambar.
        for c in range(0, img_channel):#loop untuk setiap channel pada gambar (misalnya R, G, B).
            img_flip_horizontal[y][x][c] = img[y][img_width-1-x][c]#mengambil nilai piksel dari posisi asli pada gambar dan menempatkannya ke dalam posisi yang sudah dibalik secara horizontal (y tidak berubah, sedangkan x di-reverse dari kanan ke kiri).

# Membalik gambar secara vertical
for y in range(0, img_height):# loop untuk tinggi pada gambar.
    for x in range(0, img_width):# loop untuk lebar pada gambar.
        for c in range(0, img_channel):#loop untuk setiap channel pada gambar (misalnya R, G, B).

            img_flip_vertical[y][x][c] = img[img_height-1-y][x][c]#mengambil nilai piksel dari posisi asli pada gambar dan menempatkannya ke dalam posisi yang sudah dibalik secara vertikal (x tidak berubah, sedangkan y di-reverse dari bawah ke atas).

# Menampilkan hasil balik gambar flip Horinzontal dan Vertical
plt.imshow(img_flip_horizontal)#menampilkan gambar yang sudah di-flip secara horizontal menggunakan matplotlib.
plt.title("Flip Horizontal")##memberi judul pada gambar yang ditampilkan yaitu Flip horizontal
plt.show()#menampilkan gambar yang akan di tampilkan
plt.imshow(img_flip_vertical)#menampilkan gambar yang sudah di-flip secara vertical menggunakan matplotlib.
plt.title("Flip Vertical")#memberi judul pada gambar yang ditampilkan yaitu Flip vertical
plt.show()##menampilkan gambar yang akan di tampilkan

