""" That program just verify the CPF """

regressivo = 10
soma = 0


while True:
    cpf = input('CPF: ').replace('-', '').replace('.', '')
    if len(cpf) != 11:
        print('Informação incorreta')
        continue
    else:
        break

for c in cpf[0:9]:
    c = int(c)
    multiplicação = c * regressivo
    soma += multiplicação
    multiplicação = 0
    regressivo -= 1

multiplicação = soma * 10
resultado_1 = multiplicação % 11
resultado_1 = resultado_1 if resultado_1 <= 9 else 0

regressivo = 11
multiplicação = 0
soma = 0

for c in cpf[0:10]:
    c = int(c)
    multiplicação = c * regressivo
    soma += multiplicação
    multiplicação = 0
    regressivo -= 1    

multiplicação = soma * 10
resultado_2 = multiplicação % 11
resultado_2 = resultado_2 if resultado_2 <= 9 else 0


if resultado_1 == int(cpf[9]) and resultado_2 == int(cpf[10]):
    print('CPF válido')
else:
    print('CPF inválido')

