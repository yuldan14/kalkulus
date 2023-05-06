a = float(input("Masukkan nilai suku pertama (a): "))
b = float(input("Masukkan nilai suku terakhir (b): "))
n = int(input("Masukkan jumlah suku (n): "))

total = (n * (a + b)) / 2

# Menampilkan bilangan deret
deret = [a]
selisih = (b - a) / (n - 1)
for i in range(1, n):
    deret.append(a + (i * selisih))

print("Hasil dari deret aritmatika adalah:", total)
print("Bilangan deret:", deret)
