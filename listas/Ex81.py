lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    lista.sort(reverse=True)
    resp = str(input('Quer continuar? [S/N]')).strip()[0]
    if resp in 'Nn':
        break
print('=-'*30)
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O número 5 foi encontrado na lista')
else:
    print('O número 5 não foi encontrado na lista')