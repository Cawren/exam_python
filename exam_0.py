string = input("Entrez une chaîne de caractères : ")

split_string = string.split(' ')

last_entry_is_word = False
while not last_entry_is_word :
    # On considérera ici comme des mots uniquement les chaînes de caractères composées
    # exclusivement de lettres situées entre deux espaces
    if split_string[-1].isalpha() :
        last_entry_is_word = True
    else :
        split_string.pop(-1)

print(f"Dernier mot : {split_string[-1]}\nLongueur du dernier mot : {len(split_string[-1])}")