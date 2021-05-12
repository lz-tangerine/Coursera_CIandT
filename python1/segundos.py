seg_convertido = int(input('Por favor, entre com o número de segundos que deseja converter: '))

horas = seg_convertido // 3600 % 24
dia = seg_convertido // 3600 // 24
seg_restantes = seg_convertido % 3600
minutos = seg_restantes // 60
seg_restantes_final = seg_restantes % 60

print('{} dias, {} horas, {} minutos e {} segundos.'.format(dia, horas, minutos, seg_restantes_final))


