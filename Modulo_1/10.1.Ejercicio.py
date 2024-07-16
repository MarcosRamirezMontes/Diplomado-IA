
min_f = None

for x in range(-9,10):
    resultado = x ** 2 - 6*x + 3 

    if min_f is None or resultado < min_f:
        min_f = resultado
        min_x = x

# Imprimir el resultado
print(f'El valor de x que minimiza f(x) es: {min_x}')
print(f'El valor mínimo de f(x) es: {min_f}')
