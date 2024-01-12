from random import randint

lista = []
jogos = []
cont =0

qtd = int(input('>>>'))
while qtd !=0:
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont ==6:
            cont = 0
            break
    
    jogos.append(lista[:])
    lista.clear()
    qtd -=1
print(f'+{"-"*37}+')
print(f'|{"MEGA SENA":^37}|')    
print(f'+{"-"*37}+')
for i,v in enumerate(jogos):
    print(f'|{i+1}º jogo{f"{v}":^30}|')
print(f'+{"-"*37}+')
       
        