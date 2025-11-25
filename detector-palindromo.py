# detectar palindromo

frase = input('Digite uma frase: ').upper().strip()

separa = frase.split()
junto = ''.join(separa)
reverso = junto[::-1]

print(reverso)

if reverso == junto:
    print('A frase é um palíndromo')

else:
    print('A frase não é palíndromo')
