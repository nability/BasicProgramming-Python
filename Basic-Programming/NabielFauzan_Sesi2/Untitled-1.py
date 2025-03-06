name = "NUGRAHA"

for i in range(len(name)):
    for x in range(len(name)):
        if (x <= i) :
            print(name[x], end=" ")
        else :
            print("*"[i], end=" ")
            
            
            