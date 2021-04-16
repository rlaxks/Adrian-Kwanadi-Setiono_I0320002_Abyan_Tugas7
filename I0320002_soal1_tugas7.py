#kata sambutan
teks = "Selamat Datang di Restoran Ayam Gepuk"
a = teks.center(50, "=")
print(a)

#input data
nama = input("Atas nama siapa orderannya ?")
b = nama.capitalize()

#memesan makanan
pesanan = input("Menu apa yang ingin Anda pesan: ")

#pesanan tambahan
tambahan = input("Apakah ada tambahan menu yang lain? (Y/N)")
if tambahan == "Y" or "y":
    tambahan_menu = input("Menu tambahan apa yang ingin dipesan?")
elif tambahan == "N" or "n":
    print("Baik, pesanan Anda sedang di proses")

print("Baik saya ulangi pesanannya ya")
print(pesanan)
print(tambahan_menu)
print("Dengan orderan atas nama", b)

teks = "terima kasih atas pesanannya. mohon ditunggu"
print(teks.upper())