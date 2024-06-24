edad = float(input('Ingrese una edad: '))
if edad < 13:
    print('Niño')
elif edad < 18:
        print('Adolescente')
elif edad <65:
    print('Adulto')
else:
    print('Adulto Mayor')