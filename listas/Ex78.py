valores = []
maior = menor = 0
for i in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {i}: ')))
    if i == 0:
        maior = menor = valores[i]
    else:
        if valores[i] > maior:
            maior = valores[i]
        elif valores[i] < menor:
            menor  = valores[i] 

print(f'O mairo valor é {maior} e apareceu nas posições')
for i,v in enumerate(valores):
    if v ==maior:
        print(f'>{i}', end=' ')
print()
print(f"O menor valor é {menor} e apareceu nas posições")
for i, v in enumerate(valores):
    if v == menor:
        print(f'>{i}', end=' ')