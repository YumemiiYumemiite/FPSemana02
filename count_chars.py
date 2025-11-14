frase = input()

dicionario = {}
for letra in frase:
    if letra == " ":
        continue 
    if letra not in dicionario:
        dicionario[letra] = frase.count(letra)

print(dicionario)