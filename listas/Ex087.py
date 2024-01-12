matriz = [
    [0,1,0],
    [0,2,0],
    [0,3,0]]
col = lin = par=  0

for i in range(0,3):
    for c in range(0,3):
            print(f'Digite um valor para a posição ({i},{c}): ')
            matriz[i][c] = int(input('>>> '))
for i in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[i][c]:^5}]', end=' ' if c !=2 else '\n')
        if matriz[i][c]%2==0:
            par += matriz[i][c]
        
for i in range (0,3):
    col += matriz[i][2]
    if lin == 0:
        lin = matriz[1][i]
        print(f'{"1", lin}')
        if matriz[1][i] > lin:
            lin = matriz[1][i]
            print(f'{"2",lin}')
        else:
            continue
            
print(f'A soma dos pares {par}')
print(f'A soma da terceira coluna é {col}')
print(f'O maior valor da segunda linha é {lin}')
