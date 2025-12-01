taille = int(input("Taille du tableau désirée : "))
nombre = []
i = 0
while i < taille :
    to_append = input(f"Digit {i+1} : ")
    try :
        if int(to_append) < 10 :
            nombre.append(int(to_append))
            i += 1
        else :
            print("Le chiffre doit être inférieur à 10")
    except :
        print("Le caractère ne peut pas être converti en chiffre")

print(f"Nombre entré : {nombre}")

retenue = True
index = 0
while retenue :
    index += 1
    try :
        if nombre[-index] < 9 :
            retenue = False
            nombre[-index] += 1
        else :
            nombre[-index] = 0
    except IndexError :
        new_nombre = [1]
        for chiffre in nombre :
            new_nombre.append(chiffre)
        nombre = new_nombre
        retenue = False

print(f"Nombre incrémenté : {nombre}")

