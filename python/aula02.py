s = 0 
for x in range(0, 999):
    s = s + x
print(s/999)

frase = input(" Digite uma Frase: " )
print(frase)    

palavras = frase.split()
numeroPalavras = len(palavras)
print(numeroPalavras)

palavrasInvertidas = palavras[::-1]
fraseInvertida = ' '.join(palavrasInvertidas)
print(fraseInvertida)



numero = int(input("Digite um numero"))
while(numero != 0):
    if(numero > 0):
        print("Este numero é positivo")      
    else:
        print("Este numero é negativo")

    numero = int(input("Digite um numero"))

print("Voce digitou zero")