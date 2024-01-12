temp =[]
principal = []
resp = " "
while True:
    resp = " "
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    principal.append(temp[:])
    #temp.clear()
    while resp not in "SsNn":
        resp = str(input(">>>")).strip()[0]
    if resp in "Nn":
        break
print(f'Os dados foram {principal}')