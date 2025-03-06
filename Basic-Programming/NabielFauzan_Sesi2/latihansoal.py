nama = "NUGRAHA"
length = len(nama)

for i in range(length):
    output = ""
    for j in range(length):
        if j < length - i:
            output += nama[j]
        else:
            output += '*'
    print(output)