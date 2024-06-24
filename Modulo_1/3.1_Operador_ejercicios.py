#Escribe un programa que solicite 2 números y luego imprima
#1.La suma de los 2 números
#2.La resta del primero por el segundo
#3.El producto de los 2 números
#4.El cubo de la suma de los 2 números
#5.El cociente del primer número entre el segundo

Num1 = float(input("Ingrese el primer número: "))
Num2 = float(input("Ingrese el segundo número: "))

suma = Num1 + Num2
resta = Num1 - Num2
producto = Num1*Num2
cubo = suma**3
cociente = Num1/Num2

print("Suma:", suma)
print("Resta: ", resta)
print("Producto: ", producto)
print("Cubo: ", cubo)
print("Cociente", cociente)


