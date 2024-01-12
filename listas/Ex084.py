import os

temp = []
princ = []
maior = menor = 0

def cls():
    return os.system("cls" if os.name == "nt" else "clear")

resp:str = ' '

while True:
    temp.append(str(input('Nome: ')).strip())
    temp.append(float(input('Peso: ')))
    
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] < menor:
            menor = temp[1]    
        if temp[1]> maior:
            maior = temp[1]
    
    
    princ.append(temp[:])
    temp.clear()
# ["nome1", 1]
# ["nome1", 1, "nome2", 2]
    while resp not in "SsNn":
        cls()
        resp = str(input('Quer continuar? [S/N]')).strip()
    
        
    if resp in 'Nn':
        break
    resp = " "

print('-'*30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas')

for p in princ:
    if p[1] == maior:
        print('O maior peso foi de: ')
        print(f'{p[0]}', end=' ')
        print(f'Com {p[1]}Kg')

    else:
        print('O menor peso foi de: ')
        print(f'{p[0]}', end=' ')
        print(f'com {p[1]}kg')
        
print(f'O maior peso foi de {maior}Kg')
print(f'O menor peso foi de {menor}Kg')