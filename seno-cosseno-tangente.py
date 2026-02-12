import math
angulo=float(input('Digite o angulo que deseja: '))
seno=math.sin(math.radians(angulo))
print('o angulo de {} tem seno de {:.2f}'.format(angulo,seno))
cosseno=math.cos(math.radians(angulo))
print('o angulo de {} tem cosseno de {:.2f}'.format(angulo,cosseno))
tangente=math.tan(math.radians(angulo))
print('o angulo de {} tem tangente de {:.2f}'.format(angulo,tangente))