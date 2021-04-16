#input data
angka_1 = float(input("Masukkan angka pertama: "))
angka_2 = float(input("Masukkan angka kedua: "))
angka_3 = float(input("Masukkan angka ketiga: "))
angka_4 = float(input("Masukkan angka keempat: "))
angka_5 = float(input("Masukkan angka kelima: "))

total_angka = angka_1, angka_2, angka_3, angka_4, angka_5
print(total_angka)

#memilih angka secara random
import random
print(random.choice(total_angka))

#menentukan angka dengan nilai tertinggi
print("Nilai max dari kelima angka tersebut adalah: ", max(total_angka))

#menentukan angka dengan nilai terendah
print("Nulai min dari kelima angka tersebut adalah: ", min(total_angka))
