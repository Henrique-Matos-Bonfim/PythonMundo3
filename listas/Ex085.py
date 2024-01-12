princ = [[],[]]

def lista():
    for i in range(1,8):
        num = int(input(f'Digite o {i}o. valor: '))
        if num % 2 == 0:
            princ[0].append(num)
            princ[0].sort()
        else:
            princ[1].append(num)
            princ[1].sort()


lista()
print(f'Números pares: {princ[0]}\nNúmeros impares: {princ[1]}')