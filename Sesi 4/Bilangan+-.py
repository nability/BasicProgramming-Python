bilangan = int(input("Masukan bilangan : "))

if bilangan >=1:
    hasil = "bilangan %i adalah positif"%(bilangan)
elif bilangan <1:
    hasil = "bilangan %i adalah negatif"%(bilangan)
else:
    hasil = "bilangan %i adalah netral"%(bilangan)

print(hasil)