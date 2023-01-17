import random
import	sys

while True:
    try:
        criar = str(input('\n\t\033[31m[1] criar um CPF aleatório\033[m\n\t\033[32m[2] validar um autoral\033[m\n' \
            '--> '))
        break
    except:
        print(f'Erro {Exception}')

cpf = 0
soma = 0
multiplicação = 0
regressivo = 10


if criar == '1':
    while True:
        for c in range(0,8):
            cpf += random.randint(0,9)
            cpf *= 10
        if len(str(cpf)) < 9:
            cpf = 0
            continue
        if len(str(cpf)) == 9:
            break
elif criar == '2':
    cpf = input('Digite os 9 primeiros digitos desejados.\n\tCPF: ')
    cpf = cpf[0:9]
else:
    print('Nada foi digitado')
    sys.exit

cpf_1 = str(cpf)

for c in cpf_1[0:9]:
    c = int(c)
    multiplicação = c * regressivo
    soma += multiplicação
    multiplicação = 0
    regressivo -= 1

multiplicação = soma * 10
resultado1 = multiplicação % 11
resultado1 = resultado1 if resultado1 <= 9 else 0


multiplicação = 0
soma = 0

cpf_1 = str(cpf)
num = 0
regressivo = 11

for c in range(0, len(cpf_1)):
    num += int(cpf_1[c])
    multiplicação = num * regressivo
    soma += int(multiplicação)
    multiplicação = 0
    regressivo -= 1
    num = 0
    if c == 8:
        multiplicação = resultado1 * regressivo
        soma += int(multiplicação)
        multiplicação = 0

multiplicação = soma * 10
resultado2 = multiplicação % 11
resultado2 = resultado2 if resultado2 <= 9 else 0

if criar == '1':
    print('=' * 30)
    print('CPF gerado aleatóriamente:')
    print(f'\n{cpf_1[0:3]}.{cpf_1[3:6]}.{cpf_1[6:9]}-{resultado1}{resultado2}')
    print('=' * 30)

if criar == '2':
    print('=' * 30)
    print('Valor colocado: ')
    print(cpf)
    print()
    print('CPF gerado:')
    print(f'{cpf_1[0:3]}.{cpf_1[3:6]}.{cpf_1[6:9]}-{resultado1}{resultado2}')
    print('=' * 30)


