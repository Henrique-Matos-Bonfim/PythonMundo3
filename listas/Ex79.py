valores = []

while True:
    n = int(input('Digite um valor: '))
    if  n in valores:
        print(f'Valor {n} duplicado. Não adicionar! ')
    else:
        valores.append(n)
    r = str(input('Deseja continuar: [S/N]')).strip()[0]
    if r in "Nn":
        break
valores.sort()
print(f'+{"-"*30}+')
print(f'|{"Os valores adicionados":^30}|')
print(f'+{"-"*30}+')
for i, v in enumerate(valores):
    print(f'|{f"{i+1}  -  {v}":30}|')
print(f'+{"-"*30}+')

