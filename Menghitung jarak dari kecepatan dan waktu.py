# Program Menghitung Jarak
# Spesifikasi : Menghitung nilai jarak (dalam m) dengan input kecepatan dan waktu

# KAMUS
# s = float
# v,t = float

# Algoritma
# Masukan nilai kecepatan (v) dan waktu (t)
v = float(input("Masukan nilai kecepatan :"))   #input
t = float(input("Masukan nilai waktu :"))

# Menghitung jarak dengan rumus s = v*t
s = v*t                                         #proses

#terminasi
print("Maka jaraknya adalah" + str(s))          #output
