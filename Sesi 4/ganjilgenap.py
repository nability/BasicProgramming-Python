bilangan = int(input("Masukan bilangan : "))

if bilangan %2==0 and bilangan >0:
    hasil = "bilangan genap dan positif"
elif bilangan %2==0 and bilangan <0:
    hasil = "bilangan genap dan negatif"
elif bilangan %2!=0 and bilangan <0:
    hasil = "bilangan ganjil dan negatif"
elif bilangan %2!=0 and bilangan >0:
    hasil = "bilangan ganjil dan positif"
else:
    hasil = "0 netral"

print(hasil)
