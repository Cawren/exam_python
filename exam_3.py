string = input("Entrez une chaîne de caractères : ")
valid = True

correspondances = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

enchainements_acceptes = ["IV", "IX", "XL", "XC", "CD", "CM"]

for char in string :
    if char not in correspondances :
        print(f"Caractère invalide : {char}")
        valid = False
        break

nombre = 0
issu_de_soustraction = False

for i in range(len(string)) :
    try :
        if correspondances[string[i]] < correspondances[string[i+1]] :
            if string[i] + string[i+1] in enchainements_acceptes :
                if issu_de_soustraction == False :
                    nombre -= correspondances[string[i]]
                    issu_de_soustraction = True
                else :
                    print(f"Deux soustractions consécutives effectuées : {string[i-1] + string[i]} et {string[i] + string[i+1]}")
                    valid = False
                    break
            else :
                print(f"Enchaînement de caractères invalide : {string[i] + string[i+1]}")
                valid = False
                break
        else :
            nombre += correspondances[string[i]]
            issu_de_soustraction = False
    except IndexError :
        nombre += correspondances[string[i]]

if valid :
    print(f"Le nombre vaut : {nombre}")