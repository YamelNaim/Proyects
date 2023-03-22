

#obtener los datos de las personas
print('----------')
print('Divisor de gastos©\n----------')
cant_personas = int(input('Cuantos son? '))
personas = []
personas_pay = []

print('----------')
#payment logic
total_pagar = float(input('Cuanto es el total a pagar? '))
pagar = total_pagar / cant_personas 

print('----------')
#verificar si alguien puso plata
howmany_pay = str(input('Alguien ya puso plata? '))
print('----------')

#en caso de que alguien puso plata
if howmany_pay == 'si' or howmany_pay == 'Si' or howmany_pay == 'Sí' or howmany_pay == 'sí' or howmany_pay == 's' or howmany_pay == 'y' or howmany_pay == 'yes' or howmany_pay == 'Yes':
    cuantos_pay = int(input('Cuantos pusieron plata: '))
    pagare = []
    print('----------')
    for i in range(cuantos_pay):
        persona = str(input('Como es su nombre? '))
        persona.title
        personas.append(persona)
        print('----------')
        pay = float(input('Cuanto puso '+ personas[i] + '? '))
        personas_pay.append(pay)
        print('----------')
    print('El total a pagar es de',pagar,'cada uno') #cuanto cada uno
    print('----------')
    for a in range(cuantos_pay): #excepto
        #payment logic
        pagare_1 = pagar - personas_pay[a]
        pagare.append(pagare_1)
        print('Excepto',str(personas[a]),': ',str(pagare[a]))
        print('------Divisor de gastos©----')
else: #si nadie puso:
    print('El total a pagar es de',pagar,'cada uno')
    print('------Divisor de gastos©----')












