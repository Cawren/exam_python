string = input("Entrez une chaîne de caractères : ")

score = 0
for i in range(len(string)-1) :
    score += abs(ord(string[i]) - ord(string[i+1]))

print(f"Score : {score}")