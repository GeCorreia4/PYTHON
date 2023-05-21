import math
ang = int(input('Digite o ângulo: '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print('Ângulo: {}º\nSeno: {:.3f}\nCosseno: {:.3f}\nTangente: {:.3f}'.format(ang, seno, cos, tg))
