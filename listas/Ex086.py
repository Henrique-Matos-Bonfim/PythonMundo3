matriz = [[[1],[2],[3]],[[4],[5],[6]],[[7],[8],[9]]]

cont = cont2 =0 
# for i in range(0,9):
#     num = int(input(f'Digite o valor para [{cont},{cont2}]'))
#     matriz[cont][cont2].append(num)
#     cont2+=1
#     if cont2 == 3:
#         cont += 1
#         cont2 = 0
for i, v in enumerate(matriz[0]):
    print(v, end=' ')
print(' ')
for i, v in enumerate(matriz[1]):
    print(v, end=' ')
print(' ')
for i, v in enumerate(matriz[2]):
    print(v, end='  ')
