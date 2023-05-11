#Mengimport Library Modul numpy,image,matplotlib
import numpy as np#Mengimport library numpy
import imageio#Mengimport library imageio
import matplotlib.pyplot as plt#Mengimport matplotlib

# Membaca gambar dan Mendapatkan resolusi dan type dari gambar
img = imageio.imread("Satoru.jpg")#membaca gambar dengan nama file "Satoru.jpg" menggunakan library imageio dan menyimpannya ke dalam variabel img.
img_height = img.shape[0]#mengambil tinggi gambar dari shape img dan menyimpannya ke dalam variabel img_height.
img_width = img.shape[1]#mengambil lebar gambar dari shape img dan menyimpannya ke dalam variabel img_width.
img_channel = img.shape[2]#mengambil jumlah channel gambar dari shape img dan menyimpannya ke dalam variabel img_channel.

# Inversi
# Membuat variabel img_inversi
img_inversi = np.zeros(img.shape, dtype=np.uint8)#membuat sebuah array dengan ukuran yang sama dengan gambar asli (img) dan bertipe data uint8, lalu menyimpannya ke dalam variabel img_inversi.

#Membuat fungsi untuk inversi grayscale
def inversi_grayscale(nilai):#mendefinisikan sebuah fungsi bernama inversi_grayscale yang menerima satu parameter yaitu nilai.
    for y in range(0, img_height):#melakukan perulangan dari 0 hingga img_height - 1 untuk setiap nilai y.
        for x in range(0, img_width):#melakukan perulangan dari 0 hingga img_width - 1 untuk setiap nilai x.
            red = img[y][x][0]#mengambil nilai warna merah (red) dari pixel pada posisi (y, x) dari gambar asli (img), lalu menyimpannya ke dalam variabel red.
            green = img[y][x][1]#mengambil nilai warna hijau (green) dari pixel pada posisi (y, x) dari gambar asli (img), lalu menyimpannya ke dalam variabel green
            blue = img[y][x][2]# mengambil nilai warna biru (blue) dari pixel pada posisi (y, x) dari gambar asli (img), lalu menyimpannya ke dalam variabel blue.
            gray = (int(red) + int(green) + int(blue)) / 3#menghitung nilai rata-rata dari ketiga nilai warna (red, green, blue) pada pixel tersebut, lalu menyimpannya ke dalam variabel gray.
            gray = nilai - gray#menghitung nilai inversi dari gray dengan menguranginya dari nilai, lalu menyimpannya kembali ke dalam variabel gray.
            img_inversi[y][x] = (gray, gray, gray)#menyimpan nilai gray yang telah di-inversi ke dalam array img_inversi pada posisi (y, x), dengan mengganti nilai 

# Membuat fungsi untuk inversi rgb
def inversi_rgb(nilai):#mendefinisikan fungsi inversi_rgb yang akan digunakan untuk melakukan inversi pada gambar RGB.
    for y in range(0, img_height):#melakukan iterasi pada setiap baris gambar.
        for x in range(0, img_width):# melakukan iterasi pada setiap kolom gambar.
            red = img[y][x][0]#mengambil nilai intensitas warna merah pada piksel (x,y).
            red = nilai - red#melakukan inversi pada nilai intensitas warna merah.
            green = img[y][x][1]#mengambil nilai intensitas warna hijau pada piksel (x,y).
            green = nilai - green#melakukan inversi pada nilai intensitas warna hijau.
            blue = img[y][x][2]#mengambil nilai intensitas warna biru pada piksel (x,y).
            blue = nilai - blue#melakukan inversi pada nilai intensitas warna biru.
            img_inversi[y][x] = (red, green, blue)#engisi nilai pada piksel yang berada pada koordinat (x,y) pada citra img_inversi dengan nilai intensitas warna yang diubah. Nilai intensitas warna tersebut diwakili oleh tiga komponen warna yaitu merah (red), hijau (green), dan biru (blue) yang sudah dihitung sebelumnya.

#Menampilkan hasil inversi Grayscale dan Rgb
inversi_grayscale(255)# Memanggil fungsi inversi_grayscale() dengan argumen 255. Fungsi ini akan melakukan inversi warna pada gambar grayscale, sehingga piksel dengan intensitas warna 0 akan menjadi 255, dan sebaliknya.
plt.imshow(img_inversi)#Menampilkan gambar hasil inversi warna yang disimpan dalam variabel img_inversi menggunakan library Matplotlib.
plt.title("Inversi Grayscale")#Memberikan judul pada gambar yang ditampilkan dengan teks "Inversi Grayscale".
plt.show()#Menampilkan gambar hasil inversi warna pada jendela pop-up.

inversi_rgb(255)# Memanggil fungsi inversi_rgb() dengan argumen 255. Fungsi ini akan melakukan inversi warna pada gambar RGB, sehingga setiap nilai komponen warna (merah, hijau, biru) pada setiap piksel akan diubah menjadi nilai yang sesuai dengan inversinya (255 - nilai asli).
plt.imshow(img_inversi)#Menampilkan gambar hasil inversi warna yang disimpan 
plt.title("Inversi RGB")#Memberikan judul pada gambar yang ditampilkan dengan teks "Inversi RGB".
plt.show()#Menampilkan gambar hasil inversi warna pada jendela pop-up.

#Percoban Logaritmik
#Membuat variabel img_log untuk menampung hasil
img_log = np.zeros(img.shape, dtype=np.uint8)#Membuat sebuah variabel baru dengan nama img_log yang berisi array nol dengan dimensi yang sama dengan gambar awal (img).

#Mendefinisikan fungsi untuk log
def log(c):#Mendefinisikan sebuah fungsi dengan nama log yang menerima satu parameter c. Fungsi ini akan melakukan proses transformasi logaritmik pada setiap piksel gambar.
    for y in range(0, img_height):#Melakukan perulangan for pada setiap baris (y) dalam gambar. Variabel img_height menyimpan jumlah baris pada gambar.
        for x in range(0, img_width):#Melakukan perulangan for pada setiap kolom (x) dalam gambar. Variabel img_width menyimpan jumlah kolom pada gambar.
            red = img[y][x][0]#Mengambil nilai warna merah dari piksel yang sedang diproses pada baris ke-y dan kolom ke-x.
            green = img[y][x][1]# Mengambil nilai warna hijau dari piksel yang sedang diproses pada baris ke-y dan kolom ke-x.
            blue = img[y][x][2]#Mengambil nilai warna biru dari piksel yang sedang diproses pada baris ke-y dan kolom ke-x.
            gray = (int(red) + int(green) + int(blue)) / 3#Menghitung nilai rata-rata dari tiga nilai warna (merah, hijau, biru) yang diambil dari piksel tersebut. Nilai rata-rata tersebut akan digunakan sebagai nilai keabuan (grayscale) dari piksel.
            gray = int(c * np.log(gray + 1))#Menghitung nilai transformasi logaritmik dari nilai keabuan piksel dengan menggunakan rumus c * log(1 + gray), dimana c merupakan nilai konstanta yang diberikan sebagai parameter pada fungsi log
            if gray > 255:#Memeriksa apakah nilai gray yang sudah dihitung melebihi nilai maksimum untuk skala keabuan 8-bit yaitu 255.
                gray = 255#Jika nilai gray melebihi 255, maka nilai gray diubah menjadi 255.
            if gray < 0:#Memeriksa apakah nilai gray yang sudah dihitung kurang dari 0.
                gray = 0#Jika nilai gray kurang dari 0, maka nilai gray diubah menjadi 0.
            img_log[y][x] = (gray, gray, gray)#Menyimpan nilai transformasi logaritmik gray pada setiap nilai warna (merah, hijau, biru) pada piksel yang sedang diproses pada baris ke-y dan kolom ke-x.

#Menampilkan hasil log
log(30)#Memanggil fungsi log() dengan argumen 30. Fungsi ini kemudian akan melakukan transformasi logaritmik pada gambar dengan parameter c=30
plt.imshow(img_log)#Menampilkan gambar hasil transformasi logaritmik yang disimpan dalam variabel img_log menggunakan library Matplotlib.
plt.title("Log")#Memberikan judul pada gambar yang ditampilkan dengan teks "Log".
plt.show()#Menampilkan gambar hasil transformasi logaritmik pada jendela pop-up.

#Inversi & Log
#Membuat variabel img_inlog untuk menampung hasil
img_inlog = np.zeros(img.shape, dtype=np.uint8)#Mendefinisikan sebuah variabel bernama img_inlog yang akan menampung hasil inversi logaritmik pada gambar
#Mendefinisikan fungsi untuk inversi log
def inlog(c):#Mendefinisikan fungsi inlog() dengan satu parameter yaitu c yang akan digunakan sebagai konstanta untuk inversi logaritmik.
    for y in range(0, img_height):#Melakukan perulangan for pada setiap baris (y) dalam gambar. Variabel img_height menyimpan jumlah baris pada gambar.
        for x in range(0, img_width):#Melakukan perulangan for pada setiap kolom (x) dalam gambar. Variabel img_width menyimpan jumlah kolom pada gambar.
            red = img[y][x][0]# Mendapatkan nilai intensitas warna merah pada piksel (x,y) dari gambar asli (img).
            green = img[y][x][1]# Mendapatkan nilai intensitas warna hijau pada piksel (x,y) dari gambar asli (img).
            blue = img[y][x][2]# Mendapatkan nilai intensitas warna biru pada piksel (x,y) dari gambar asli (img).
            gray = (int(red) + int(green) + int(blue)) / 3# Menghitung rata-rata intensitas warna pada piksel (x,y) dari gambar asli (img).
            gray = int(c * np.log(255 - gray + 1))#Menghitung nilai inversi logaritmik dari nilai gray menggunakan konstanta c. Proses ini dilakukan dengan memodifikasi formula transformasi logaritmik pada gambar, yaitu gray = c * log(1 + I). 
            if gray > 255:#Menyaring nilai gray agar tidak melebihi batas maksimum (255) pada tipe data uint8.
                gray = 255
            if gray < 0:#Menyaring nilai gray agar tidak kurang dari batas minimum (0) pada tipe data uint8.
                gray = 0#
            img_inlog[y][x] = (gray, gray, gray)#Menetapkan nilai intensitas warna pada piksel (x,y) dari gambar inversi logaritmik (img_inlog). Karena gambar tersebut berupa grayscale, maka nilai intensitas warna pada ketiga kanal (merah, hijau, biru) sama.
#Menampilkan hasil inversi log
inlog(30)#menghasilkan sebuah gambar yang sudah dikenai transformasi inversi dan transformasi logaritmik.
plt.imshow(img_inlog)#Menampilkan gambar hasil transformasi inversi dan transformasi logaritmik yang disimpan dalam variabel img_inlog menggunakan library Matplotlib.
plt.title("Inversi & Log")# Memberikan judul pada gambar yang ditampilkan dengan teks "Inversi & Log".
plt.show()#Menampilkan gambar hasil transformasi inversi dan transformasi logaritmik pada jendela pop-up.

#Nth Power
#variabel img_nthpower untuk menampung hasil
img_nthpower = np.zeros(img.shape, dtype=np.uint8)#Variabel img_nthpower didefinisikan sebagai array numpy yang memiliki ukuran yang sama dengan gambar awal (img) dan memiliki tipe data uint8.
#fungsi untuk nth power
def nthpower(c, y):#didefinisikan dengan dua parameter yaitu c yang merupakan konstanta dan y yang merupakan nilai eksponen.
    thc = c / 100#Membagi nilai c dengan 100 untuk menormalisasi konstanta.
    thy = y / 100#Membagi nilai y dengan 100 untuk menormalisasi pangkat.
    for y in range(0, img_height):# Looping dari 0 hingga nilai tinggi citra-1 untuk setiap baris citra.
        for x in range(0, img_width):#Looping dari 0 hingga nilai lebar citra-1 untuk setiap piksel di setiap baris citra.
            red = img[y][x][0]# Mendapatkan nilai komponen merah dari piksel yang ditunjuk oleh x dan y.
            green = img[y][x][1]#Mendapatkan nilai komponen hijau dari piksel yang ditunjuk oleh x dan y.
            blue = img[y][x][2]#Mendapatkan nilai komponen biru dari piksel yang ditunjuk oleh x dan y.
            gray = (int(red) + int(green) + int(blue)) / 3# Mendapatkan nilai rata-rata dari ketiga komponen piksel yang ditunjuk oleh x dan y.
            gray = int(thc * pow(gray, thy))#Menghitung nilai hasil transformasi nth power pada nilai gray. Fungsi pow digunakan untuk menghitung pangkat dari nilai gray, yang kemudian dikalikan dengan konstanta yang telah dinormalisasi.
            if gray > 255:#Jika nilai hasil transformasi gray lebih besar dari 255, maka nilai gray diubah menjadi 255.
                gray = 255
            if gray < 0:#Jika nilai hasil transformasi gray kurang dari 0, maka nilai gray diubah menjadi 0.
                gray = 0
            img_nthpower[y][x] = (gray, gray, gray)#Menetapkan nilai hasil transformasi ke piksel yang ditunjuk oleh x dan y pada img_nthpower. 
#Menampilkan hasil
nthpower(50, 100)#menerapkan transformasi Nth power pada citra dengan mengatur nilai parameter c dan y. Kemudian, citra hasil transformasi disimpan dalam variabel img_nthpower
plt.imshow(img_nthpower)#untuk menampilkan citra hasil transformasi 
plt.title("Nth Power")# memberikan judul pada gambar
plt.show()#digunakan untuk menampilkan gambar.

#variabel img_nthrootpower
img_nthrootpower = np.zeros(img.shape, dtype=np.uint8)##Variabel img_nthpower didefinisikan sebagai array numpy yang memiliki ukuran yang sama dengan gambar awal (img) dan memiliki tipe data uint8.
#Membuat fungsi untuk nth root power
def nthrootpower(c, y):#didefinisikan dengan dua parameter yaitu c yang merupakan konstanta dan y yang merupakan nilai eksponen.
    thc = c / 100#Membagi nilai c dengan 100 untuk menormalisasi konstanta.
    thy = y / 100#Membagi nilai y dengan 100 untuk menormalisasi pangkat.
    for y in range(0, img_height):# Looping dari 0 hingga nilai tinggi citra-1 untuk setiap baris citra.
        for x in range(0, img_width):#Looping dari 0 hingga nilai lebar citra-1 untuk setiap piksel di setiap baris citra.
            red = img[y][x][0]# Mendapatkan nilai komponen merah dari piksel yang ditunjuk oleh x dan y.
            green = img[y][x][1]#Mendapatkan nilai komponen hijau dari piksel yang ditunjuk oleh x dan y.
            blue = img[y][x][2]#Mendapatkan nilai komponen biru dari piksel yang ditunjuk oleh x dan y.
            gray = (int(red) + int(green) + int(blue)) / 3## Mendapatkan nilai rata-rata dari ketiga komponen piksel yang ditunjuk oleh x dan y.
            gray = int(thc * pow(gray, thy))#Menghitung nilai hasil transformasi nth power pada nilai gray. Fungsi pow digunakan untuk menghitung pangkat dari nilai gray, yang kemudian dikalikan dengan konstanta yang telah dinormalisasi.
            gray = int(thc * pow(gray, 1./thy))
            if gray > 255:#Jika nilai hasil transformasi gray lebih besar dari 255, maka nilai gray diubah menjadi 255.
                gray = 255
            if gray < 0:#Jika nilai hasil transformasi gray kurang dari 0, maka nilai gray diubah menjadi 0.
                gray = 0
            img_nthpower[y][x] = (gray, gray, gray)#Menetapkan nilai hasil transformasi ke piksel yang ditunjuk oleh x dan y pada img_nthpower. 
#Menampilkan hasil nthrootpower
nthrootpower(50, 100)#menerapkan transformasi Nth power pada citra dengan mengatur nilai parameter c dan y. Kemudian, citra hasil transformasi disimpan dalam variabel img_nthpower
plt.imshow(img_nthrootpower)##untuk menampilkan citra hasil transformasi 
plt.title("Nth Root Power")# memberikan judul pada gambar
plt.show()