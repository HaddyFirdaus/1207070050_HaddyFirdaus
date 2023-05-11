import numpy as np#Mengimport library numpy
import imageio#Mengimport library imageio
import matplotlib.pyplot as plt#Mengimport matplotlib

img = imageio.imread("Mikasa.jpg")#menggunakan imageio untuk membaca gambar mikasa

# Mendapatkan resolusi dan type dari gambar
img_height = img.shape[0]#Untuk mendapatkan nilai tinggi dari gambar
img_width = img.shape[1]#Untuk mendapatkan nilai lebar dari gambar,
img_channel = img.shape[2]#Untuk mendapatkan nilai jumlah channel dari gambar

# Membuat variabel img_grayscale
img_grayscale = np.zeros(img.shape, dtype=np.uint8)
#Merubah gambar menjadi Grayscale
for y in range(0, img_height):# for untuk mengakses setiap baris (tinggi) dari gambar.
    for x in range(0, img_width):# for untuk mengakses setiap baris (lebar) dari gambar.
        red = img[y][x][0]#menentukan nilai dari channel (merah) pada setiap pixel gambar
        green = img[y][x][1]#menentukan nilai dari channel (hijau) pada setiap pixel gambar
        blue = img[y][x][2]#menentukan nilai dari channel (biru) pada setiap pixel gambar
        gray = (int(red) + int(green) + int(blue)) / 3#menghitung nilai rata-rata dari 3 channel (dalam satuan 0-255) untuk mendapatkan nilai keabuan (grayscale) pada setiap pixel gambar.
        img_grayscale[y][x] = (gray, gray, gray)#membuat tuple baru yang merepresentasikan warna keabuan dari pixel dan menyimpan nilai tuple tersebut pada posisi yang sama dengan pixel asli menggunakan koordinat (y,x) yang sama.

#Menampilkan Gambar dari img_grayscale        
plt.imshow(img_grayscale)#menampilkan gambar yang telah dihasilkan pada variabel img_grayscale
plt.title("Grayscale")#memberikan judul pada gambar yang ditampilkan
plt.show()#Menampilkan gambar grayscale

# Menampilkan Histogram Gambar Grayscale
# Membuat variabel untuk menyimpan data gambar
hg = np.zeros((256))# untuk membuat array numpy kosong (berisi nol) dengan ukuran (256).
# Mengisi setiap nilai dalam array hg dengan 0
for x in range(0, 256):#menggunakan loop untuk mengakses setiap elemen pada array numpy "hg"dan akan diulang sebanyak 256 kali
    hg[x] = 0#array numpy "hg" memiliki nilai awal yang sama (nol), 
# Menghitung nilai dari gambar
for y in range(0, img_height):# loop "for" untuk mengakses setiap baris pada gambar grayscale. 
    for x in range(0, img_width):# menggunakan loop "for" untuk mengakses setiap kolom pada gambar grayscale dan akan diulang sebanyak "img_width"
        gray = img_grayscale[y][x][0]#nilai piksel abu-abu pada baris dan kolom yang sedang diakses, dengan mengakses elemen pertama dari array numpy "img_grayscale" 
        hg[gray] += 1#menggunakan nilai piksel abu-abu tersebut sebagai indeks array numpy dan menambahkan nilai satu
#Menampilkan Histogram
# plt.figure(figsize=(20, 6))
# plt.plot(hg, color="black", linewidth=2.0)
# plt.show()

bins = np.linspace(0, 256, 100)#menggunakan numpy.linspace untuk membuat 100 interval dengan panjang yang sama dalam rentang 0-256, dan menyimpannya dalam array numpy "bins". 
plt.hist(hg, bins, color="black", alpha=0.5)#menggunakan matplotlib.pyplot.hist untuk menghitung dan menampilkan histogram dari array numpy "hg".
plt.title("Histogram")#memberikan judul gambar "Histogram"
plt.show()#Menampilkan gambar grayscale

#Menampilkan Histogram Gambar RGB
#variabel untuk menyimpan data gambar
hgr = np.zeros((256))#digunakan untuk menyimpan nilai frekuensi kemunculan setiap nilai piksel abu-abu pada komponen warna merah (R) pada gambar asli dengan ukuran 256
hgg = np.zeros((256))#digunakan untuk menyimpan nilai frekuensi kemunculan setiap nilai piksel abu-abu pada komponen warna hijau (G) pada gambar asli dengan ukuran 256
hgb = np.zeros((256))#yang digunakan untuk menyimpan nilai frekuensi kemunculan setiap nilai piksel abu-abu pada komponen warna biru (B) pada gambar asli dengan ukuran 256
hgrgb = np.zeros((768))#digunakan untuk menyimpan nilai frekuensi kemunculan setiap kombinasi nilai piksel pada ketiga komponen warna (R, G, B) pada gambar asli dengan ukuran 768
# Mengisi setiap nilai dalam array hg dengan 0
# Melakukan Perulangan sebanyak 256x dan memulai dengan 3 aray hgr,hgg,hgb
for x in range(0, 256):#melakukan looping sebanyak 256 kali, dengan mengiterasi variabel x dari 0 hingga 255.
    hgr[x] = 0#menginisialisasi nilai awal dari setiap elemen pada array hgr
    hgg[x] = 0#menginisialisasi nilai awal dari setiap elemen pada array hgg
    hgb[x] = 0#menginisialisasi nilai awal dari setiap elemen pada array hgb
# Melakukan Perulangan sebanyak 768x dan memulai dengan aray Rgb
for x in range(0, 768):#melakukan looping sebanyak 768 kali, dengan mengiterasi variabel x dari 0 hingga 768.
    hgrgb[x] = 0#menginisialisasi nilai awal dari setiap elemen pada array hgrgb

# Menghitung nilai dari gambar
for x in range(0, 256):#melakukan looping sebanyak 256 kali, dengan mengiterasi variabel x dari 0 hingga 255.
    hgr[x] = 0#menginisialisasi nilai awal dari setiap elemen pada array hgr
    hgg[x] = 0#menginisialisasi nilai awal dari setiap elemen pada array hgg
    hgb[x] = 0#menginisialisasi nilai awal dari setiap elemen pada array hgb
# Melakukan Perulangan sebanyak 768x dan memulai dengan aray Rgb    
for x in range(0, 768):#melakukan looping sebanyak 768 kali, dengan mengiterasi variabel x dari 0 hingga 768.
    hgrgb[x] = 0#menginisialisasi nilai awal dari setiap elemen pada array hgrgb

# th = int(256/64)
# Mengakses Setiap piksel citra digital dan memiliki nilai intensitas saluran warna RGB
temp = [0]#menginisialisasi dengan sebuah list kosong yang berisi satu elemen 0.
for y in range(0, img.shape[0]):
    for x in range(0, img.shape[1]):#perulangan nested (bersarang) yang akan melakukan iterasi pada setiap piksel gambar dan mengembalikan tuple berisi dimensi dari gambar
        red = int(img[y][x][0])#untuk mengambil nilai merah (red) dari sebuah gambar pada posisi tertentu (x, y) dengan indeks 0
        green = int(img[y][x][1])#untuk mengambil nilai hijau(green) dari sebuah gambar pada posisi tertentu (y, x)dengan indeks 1
        blue = int(img[y][x][2])#untuk mengambil nilai biru (blue) dari sebuah gambar pada posisi tertentu (y, x) dengan indeks 2
        green = green + 256#menambahkan nilai pada variabel hijau (green) dengan nilai 256 .
        blue = blue + 512#menambahkan nilai pada variabel biru (blue) dengan nilai 512 .
# temp.append(green)
# Menghitung distribusi frekuensi intensitas mengunakan array (R,G,B)
        hgrgb[red] += 1#mengambil nilai merah (red) dari sebuah gambar pada posisi tertentu dan menambahkan nilai frekuensi 1 pada histogram 
        hgrgb[green] += 1#mengambil nilai  hijau(green) dari sebuah gambar pada posisi tertentu dan menambahkan nilai frekuensi 1 pada histogram 
        hgrgb[blue] += 1#mengambil nilai  biru (blue) dari sebuah gambar pada posisi tertentu dan menambahkan nilai frekuensi 1 pada histogram 

#Memvisualisasikan distribusi frekuensi intensitas pada warna (R,G,B)
binsrgb = np.linspace(0, 768, 100)#menggunakan fungsi linspace() dari library numpy untuk membuat array binsrgb yang merepresentasikan batas-batas bin yang terbentuk secara merata pada skala nilai RGB 0-768 dan dibuat 100 batas bin secara merata pada rentang nilai intensitas 0-256.
plt.hist(hgrgb, binsrgb, color="black", alpha=0.5)#hist() dari library matplotlib digunakan untuk memvisualisasikan histogram. Fungsi ini menerima 3 parameter: list frekuensi, batas-batas bin, dan warna (color). 
# plt.plot(hgrgb)
plt.title("Histogram Red Green Blue")#Memberikan judul gambar "Histogram Red Green Blue"
plt.show()# menampilkan grafik tampilan histogram tersebut diberi judul "Histogram Red Green Blue". 

#Menampilkan Histogram
#Menghitung frekuensi kemunculan intensitas pada warna (R, G, B)
for y in range(0, img_height):#untuk mengakses masing-masing piksel pada gambar (dalam representasi array) pada posisi yang sesuai. 
    for x in range(0, img_width):#untuk mengakses masing-masing piksel pada gambar (dalam representasi array) pada posisi yang sesuai. 
        red = img[y][x][0]#untuk mengambil nilai merah (red) dari sebuah gambar pada posisi tertentu (y, x) dengan indeks 0
        green = img[y][x][1]#untuk mengambil nilai hijau(green) dari sebuah gambar pada posisi tertentu (y, x)dengan indeks 1
        blue = img[y][x][2]##untuk mengambil nilai biru (blue) dari sebuah gambar pada posisi tertentu (y, x) dengan indeks 2
        hgr[red] += 1#intensitas pada channel warna (merah) pada setiap piksel diambil dan frekuensi kemunculan intensitas tersebut ditambahkan 1 
        hgg[green] += 1#intensitas pada channel warna (hijau) pada setiap piksel diambil dan frekuensi kemunculan intensitas tersebut ditambahkan 1 
        hgb[blue] += 1#intensitas pada channel warna (biru) pada setiap piksel diambil dan frekuensi kemunculan intensitas tersebut ditambahkan 1 

# menampilkan histogram dari frekuensi kemunculan intensitas Channel (R, G, B)
bins = np.linspace(0, 256, 100)#merepresentasikan batas-batas bin yang terbentuk secara merata pada skala nilai intensitas 0-256 dan dibuat 100 batas bin secara merata pada rentang nilai intensitas 0-256.
plt.hist(hgr, bins, color="red", alpha=0.5)#menerima tiga parameter, yaitu variabel yang berisi nilai frekuensi, array bins yang merupakan batas-batas bin,array hgr serta warna (merah) dan transparansi (alpha) dari histogram yang akan dihasilkan.
plt.title("Histogram Red")#Memberikan judul "Histogram Red"
plt.show()#menampilkan grafik tampilan histogram tersebut diberi judul "Histogram Red". 

plt.hist(hgg, bins, color="green", alpha=0.5)#menerima tiga parameter, yaitu variabel yang berisi nilai frekuensi, array bins yang merupakan batas-batas bin,array hgg serta warna (hijau) dan transparansi (alpha) dari histogram yang akan dihasilkan.
plt.title("Histogram Green")#Memberikan judul "Histogram green"
plt.show()#menampilkan grafik tampilan histogram tersebut diberi judul "Histogram Green ". 

plt.hist(hgb, bins, color="blue", alpha=0.5)#menerima tiga parameter, yaitu variabel yang berisi nilai frekuensi, array bins yang merupakan batas-batas bin,array hgb serta warna (biru) dan transparansi (alpha) dari histogram yang akan dihasilkan.
plt.title("Histogram Blue")#Memberikan judul "Histogram blue"
plt.show()#menampilkan grafik tampilan histogram tersebut diberi judul "Histogram Blue". 

#Menampilkan Histogram Kumulatif
#Menginisialisasi dua array NumPy hgk bernilai 256 dan c dengan nol
hgk = np.zeros((256))#menginilisasi array hgk dengan ukuran 256 dan menyimpan frekuensi kemunculan dari nilai piksel pada gambar 
c = np.zeros((256))#menginilisasi array c dengan ukuran 256 dan menyimpan kumulatif frekuensi kemunculan.
#Mengeksekusi setiap iterasi pada nilai x yang berada dalam range 0 hingga 255 dengan menggunakan dua array numpy
for x in range(0, 256):#menggunakan for-loop pada setiap nilai x yang berada dalam range 0 hingga 255
    hgk[x] = 0#melakukan inisialisasi nilai 0 pada array hgk
    c[x] = 0#melakukan inisialisasi nilai 0 pada array hgk
#untuk menghitung histogram kumulatif dari citra grayscale dan dilakukan dengan dua kali iterasi pada setiap piksel dalam citra grayscale
for y in range(0, img_height):#untuk mengakses masing-masing piksel pada gambar (dalam representasi array) pada posisi yang sesuai
    for x in range(0, img_width):#untuk mengakses masing-masing piksel pada gambar (dalam representasi array) pada posisi yang sesuai
        gray = img_grayscale[y][x][0]#nilai grayscale dari sebuah pixel pada posisi (y,x) pada gambar grayscale yang sedang diproses
        hgk[gray] += 1# operasi yang menambahkan nilai satu ke dalam array 
#Menghitung nilai kumulatif dari histogram kumulatif yang telah dihitung sebelumnya                
c[0] = hgk[0]# inisialisasi nilai c[0] dengan nilai frekuensi kemunculan intensitas pixel pada gambar grayscale yang memiliki nilai intensitas 0.
for x in range(1, 256):#perulangan for yang mengulang rentang angka dari 1 hingga 255.
     c[x] = c[x-1] + hgk[x]#menjumlahkan nilai variabel c[x-1] dengan nilai frekuensi kemunculan intensitas pixel pada intensitas x yang dihitung dari variabel hgk[x].
#nilai maksimum yang dicapai untuk histogram kumulatif
hmaxk = c[255]# menghasilkan nilai histogram kumulatif maksimum

for x in range(0, 256):#Perulangan for mengulangi setiap nilai histogram kumulatif
    c[x] = 190 * c[x] / hmaxk#setiap nilai histogram kumulatif dihitung dan dikalikan dengan 190 kemudian dibagi dengan nilai maksimum histogram kumulatif

plt.hist(c, bins, color="black", alpha=0.5)#dengan parameter c sebagai data histogram, bins sebagai batasan interval histogram, color untuk warna histogram, alpha sebagai tingkat transparansi histogram, 
plt.title("Histogram Grayscale Kumulatif")#Memberikan judul gambar "Histogram Grayscale Kumulatif"
plt.show()#Menampilkan grafik tampilan histogram tersebut yang diberi judul "Histogram Grayscale Kumulatif". 

#Menampilkan Histogram Hequalisasi
hgh = np.zeros((256)) #membuat array hgh dengan nilai awal 0 sebanyak 256 elemen
h = np.zeros((256)) #membuat array h dengan nilai awal 0 sebanyak 256 elemen
c = np.zeros((256)) #membuat array c dengan nilai awal 0 sebanyak 256 elemen

for x in range(0, 256): #iterasi sebanyak 256 kali
    hgh[x] = 0 #set nilai awal elemen array hgh dengan 0
    h[x] = 0 #set nilai awal elemen array h dengan 0
    c[x] = 0 #set nilai awal elemen array c dengan 0

for y in range(0, img_height): #iterasi sebanyak img_height
    for x in range(0, img_width): #iterasi sebanyak img_width
        gray = img_grayscale[y][x][0] #mendapatkan nilai grayscale dari citra pada posisi x,y
        hgh[gray] += 1 #menambah nilai elemen array hgh pada posisi gray

h[0] = hgh[0] #set nilai awal elemen array h dengan nilai awal elemen array hgh
for x in range(1, 256): #iterasi sebanyak 255 kali
     h[x] = h[x-1] + hgh[x] #menjumlahkan elemen array hgh pada posisi x dengan elemen array h pada posisi x-1

for x in range(0, 256): #iterasi sebanyak 256 kali
     h[x] = h[x] / img_height / img_width #membagi setiap elemen array h dengan hasil perkalian img_height dan img_width

for x in range(0, 256): #iterasi sebanyak 256 kali
    hgh[x] = 0 #set nilai awal elemen array hgh dengan 0

for y in range(0, img_height): #iterasi sebanyak img_height
    for x in range(0, img_width): #iterasi sebanyak img_width
        gray = img_grayscale[y][x][0] #mendapatkan nilai grayscale dari citra pada posisi x,y
        gray = h[gray] * 255 #mengalikan nilai elemen array h pada posisi gray dengan 255
        hgh[int(gray)] += 1 #menambah nilai elemen array hgh pada posisi integer dari gray

c[0] = hgh[0] #set nilai awal elemen array c dengan nilai awal elemen array hgh
for x in range(1, 256): #iterasi sebanyak 255 kali
     c[x] = c[x-1] + hgh[x] #menjumlahkan elemen array hgh pada posisi x dengan elemen array c pada posisi x-1

hmaxk = c[255] #mendapatkan nilai elemen array c pada posisi 255

for x in range(0, 256): #iterasi sebanyak 256 kali
    c[x] = 190 * c[x] / hmaxk #mengalikan elemen array c pada posisi x dengan 190 dan membaginya dengan hmaxk

plt.hist(c, bins, color="black", alpha=0.5)#membuat histogram dari data c dengan jumlah bins sebanyak bins. Argumen color menentukan warna(Hitam) dari bar pada histogram, sedangkan alpha menentukan transparansi bar pada histogram.
plt.title("Histogram Grayscale Hequalisasi")#Menambahkan judul pada gambar "Histogram Grayscale Hequalisasi"
plt.show()#Menampilkan tampilan Histogram Grayscale Hequlisasi