"""   

  Las tuplas se utilizan para almacenar varios elementos en una sola variable.

   Una tupla es una colección ordenada e inmutable .

   Las tuplas se escriben entre paréntesis.


"""
print("\033c")

paises1=("Mexico","Canada","EUA")
print(paises1)


varios=("Hola",True,33,3.1416)
print(varios)

for i in paises1:
    print(i)

for i in range(0,len(paises1)):
    print(paises1[i])

i=0
while i<len(paises1):
    print(paises1[i])
    i+=1

print(f"El pais que inaugura la copa del mundo 2026 es: {paises1[0]}")

edades=(23,24,18,20,20,23,24,19,24)
cuantos=edades.count(24)
print(cuantos)

#Crear un programa que lea un numero y me diga en que posiciones se encuentra
numero=int(input("Dame el numero a buscar: ").strip())
posiciones=[]
for i in range(0,len(edades)):
    if edades[i]==numero:
     posiciones.append(i)

for i in posiciones:
    print(f"El numero {numero} se encontro en la posicion: {i}")    
