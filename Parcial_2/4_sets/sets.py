"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""

print("\033c")
set1={"hola","123","123","Mexico","Holanda",123,3.1416}
print(set1)
set1.add("Ganador")
print(set1)
set1.pop()
print(set1)
#ejemplo Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados

#Solucion 1
lista_emails_1 = []
cantidad_1 = int(input("¿Cuántos emails ingresarás (Solución 1)?: "))
for i in range(cantidad_1):
    lista_emails_1.append(input(f"Ingresa el email {i+1}: "))

emails_sin_duplicados = set(lista_emails_1)
print("Emails sin duplicados:", emails_sin_duplicados)


#Solucion 2
lista_emails_2 = []
cantidad_2 = int(input("\n¿Cuántos emails ingresarás (Solución 2)?: "))
for i in range(cantidad_2):
    lista_emails_2.append(input(f"Ingresa el email {i+1}: "))

emails_unicos = []
for email in lista_emails_2:
    if email not in emails_unicos:
        emails_unicos.append(email)

print("Emails sin duplicados:", emails_unicos)
