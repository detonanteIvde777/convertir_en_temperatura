#programa de comvertir en temperatura

#libreria
import math


print("                                   ")
print("convertir grados farenheit y kelvil")
print("                                   ")

#imput
C=int(input("ingrese el valor de grados centigrados: "))

#procedimiento
f= (C*9/5) + 32
k= C + 273.15

#output
print("              ")
print("  resultaods  ")
print("              ")
print("los grados farenheit es : " + str(f))
print("los grados kelvil es: " + str(k))