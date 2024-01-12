pilhas = []

expr = str(input('Digite uma expressão'))

for simb in expr:
    if simb == '(':
        pilhas.append('(')
    elif simb == ')':
        if len(pilhas)> 0:
            pilhas.pop()
        else:
            pilhas.append(')')
if len(pilhas) == 0:
    print('Suas expressão está correta')
else:
    print('Sua expressão não está correta')
