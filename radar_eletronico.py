velocidade = int(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print('multado! Voce excedeu o limite permitido de 80km/h')
    multa = (velocidade - 80) * 7
    print('voce deve pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia! dirija com cuidado!')