string = input("Entrez une chaîne de caractères : ")

longest_palindrome = ''
highest_length = 0

# Recherche de palindromes de taille impaire
for i, char in enumerate(string) :
    length = 1
    valid_palindrome = True
    while valid_palindrome :
        try :
            if string[i-length] != string[i+length] :
                valid_palindrome = False
            else :
                length += 1
        except :
            valid_palindrome = False
    if length > highest_length :
        highest_length = length
        longest_palindrome = string[i-length+1:i+length]
highest_length = highest_length*2 - 1

# Recherche de palindromes de taille paire
for i, char in enumerate(string) :
    length = 0
    valid_palindrome = True
    while valid_palindrome :
        try :
            if string[i-length] != string[i+1+length] :
                valid_palindrome = False
            else :
                length += 1
        except :
            valid_palindrome = False
    if length*2 > highest_length :
        highest_length = length*2
        longest_palindrome = string[i-length+1:i+length+1]

print(f"Longest palindrome : {longest_palindrome} (length = {highest_length})")

