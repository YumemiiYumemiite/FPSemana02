# Solicita as duas frases sem exibir nenhuma mensagem
frase1 = input()
frase2 = input()

palavras1 = set(frase1.split())
palavras2 = set(frase2.split())

intersecao = palavras1 & palavras2

letras = sorted([p for p in intersecao if p.isalpha()])
simbolos = sorted([p for p in intersecao if not p.isalpha()])

resultado = letras + simbolos

print(" ".join(resultado))