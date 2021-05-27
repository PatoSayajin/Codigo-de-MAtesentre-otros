import math
from tabulate import tabulate
from fractions import Fraction


print("Teorema de bayes:")

matrix = []
contador = 0
filas = int(input("Cuantas filas incluyendo le quieres agregar: "))
columnas = int(input("Cuantas columnas incluyendo le quieres agregar: "))

for fil in range(filas):
    lista = []
    for colum in range(columnas):
        x = input(f"Ingresa los datos - fila={fil}, columna={colum}: ")
        lista.append(x)
    matrix.append(lista)

print("\n",tabulate(matrix, headers="firstrow", tablefmt="grid"))

print("La probsbilidad de P(N|B) = P(B|N)P(A)\n                            ----------\n                               P(B)\n")

print("Probabilidad de P(B|N): ")
p_n_b_f = int(input("Ingresa la fila: ")) #Probabilidad de lugar
p_n_b_c = int(input("Ingresa la columna: "))
d_p_n_b = float(matrix[p_n_b_f][p_n_b_c])
print(d_p_n_b)

print("\n","Probabilidad de P(A): ")
p_a_f = int(input("Ingresa la fila: ")) #Probabilidad de objeto
p_a_c = int(input("Ingresa la columna: "))
d_a = float(matrix[p_a_f][p_a_c])
print(d_a)

#resultado de arriba de la division
pnbda = float(d_p_n_b * d_a)

print("Probabilidad de P(B):")
long = len(matrix)
contador = 1
listadef = 0
while contador != long:
    p_b_i = float(matrix[contador][0])
    p_b_f = float(matrix[contador][1])
    contador += 1
    mult = p_b_i * p_b_f
    listadef += mult
redondeador = int(input(f"P(B) es: {listadef}, desde cuantas decimaels quieres redondear?: "))
listadef_redon = round(listadef,redondeador)

resultado = float((d_p_n_b*d_a)/listadef_redon)
resultado_frac = Fraction.from_float(resultado)

print(f"La probsbilidad de P(N|B) =  {d_p_n_b}*{d_a}\n                            ----------\n                               {listadef_redon}")
print(f"El resultado de la probabilidad de P(N|B) es: {resultado} = {resultado_frac}")