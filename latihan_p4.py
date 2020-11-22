print("membuat list dengan 5 element")
daftar=[11,22,33,44,55]
print(daftar)

print("\nTampilkan elemen ke 3")
print(daftar[2])

print("\nambil nilai elemen ke 2 sampai element ke 4")
print(daftar[1:4])

print("\nambil elemen terakhir")
print(daftar[-1])

print("\nUbah elemen list:")
print("ubah elemen ke 4 dengan nilai lainnya")
daftar[3] = 88
print(daftar)

print("\nubah element ke 4 sampai dengan element terakhir")
daftar[3:5] = [4,110]
print(daftar)

print("\ntambah elemen list:")
print("ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)")
daftar2=daftar[0:2]
print(daftar2)

print("\ntambah list B dengan nilai string")
daftar2.append("Dani")
print(daftar2)

print("\ntambah list B dengan 3 nilai")
daftar2.extend([1,2,3])
print(daftar2)

print("\ngabungkan list B dengan list A")
satukan=daftar2+daftar
print(satukan)