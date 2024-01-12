lista = []
pares = []
impares = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n%2==0:
        pares.append(n)
    else:
        impares.append(n)
#for i,v in enumerate(lista):
#   if v%2 ==0:
#       pares.append(v)
#   else:
#       impares.append(v)
    resp = str(input('Deseja continuar? [S/N]')).strip()[0]
    if resp in 'Nn':
        break

print(f'A lista completa {lista}')
print(f'A lista de pares {pares}')
print(f'A lista de impares {impares}') 
