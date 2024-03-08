bilangan_A = int(input("Masukan bilangan A : "))
bilangan_B = int(input("Masukan bilangan B : "))
bilangan_C = int(input("Masukan bilangan C : "))

if bilangan_A > bilangan_B and bilangan_A > bilangan_C:
    hasil = "bilangan A : %i paling besar dari B : %i dan C : %i"%(bilangan_A,bilangan_B,bilangan_C)
elif bilangan_B > bilangan_A and bilangan_B > bilangan_C:
    hasil = "bilangan B : %i paling besar dari A : %i dan C : %i"%(bilangan_B,bilangan_A,bilangan_C)
elif bilangan_C > bilangan_A and bilangan_C > bilangan_B:
    hasil = "bilangan %i paling besar dari %i dan %i"%(bilangan_C,bilangan_A,bilangan_C)
elif bilangan_A == bilangan_B and bilangan_A > bilangan_C:
    hasil = "bilangan %i dan %i lebih besar dari %i"%(bilangan_A,bilangan_B,bilangan_C)
elif bilangan_B == bilangan_C and bilangan_B > bilangan_A:
    hasil = "bilangan %i dan %i lebih besar dari %i"%(bilangan_B,bilangan_C,bilangan_A)
elif bilangan_C == bilangan_A and bilangan_C > bilangan_B:
    hasil = "bilangan %i dan %i lebih besar dari %i"%(bilangan_C,bilangan_A,bilangan_B)
else:
    hasil = "bilangan sama"

print(hasil)