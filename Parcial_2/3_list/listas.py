print("\033c")

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
numeros=[23,33,45,8,24,0,100]
lista="["
for i in numeros:
  
    lista+=f"{i},"
print(lista+"]")

lista="["
for i in range(0,len(numeros)):
    lista+=f"{numeros[i]},"
print(lista+"]")
  
lista="["
i=0
while i<len(numeros):
    lista+=f"{numeros[i]},"
    i+=1
print(lista+"]")
#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
#1er forma
palabras=["UTD","tercer","cuatrimestre","TI"]
palabras=input("Dame la palabra buscar: ").strip()
if palabras in palabras:
    print(f"Encontre la palabra {palabras} en la lista")
else:
    print(f"No se encontro la palabra {palabras} en la lista")
#2DA FORMA
palabras=["UTD","tercer","cuatrimestre","TI"]
palabras=input("Dame la palabra buscar: ").strip()

encontro=False
for i in palabras:
    if i==palabras:
       encontro=True
       if encontro:
        print(f"Encontre la palabra {palabras} en la lista")
    else:
        print(f"No se encontro la palabra {palabras} en la lista")     
# 3ra FORMA con len
palabras= ['utd','tercer','cuatrimestre','ti']
palabra=input("Ingresa la palabra a buscar: ").strip()
find=False
for o in range(0,len(palabras)):
    if palabra==palabras[o]:
        find=True
if find:
    print("Palabra encontrada")
else:
    print("palabra no encontrada")

#4ta FORMA con while 

palabras= ['utd','tercer','cuatrimestre','ti']
palabra=input("Ingresa la palabra a buscar: ").strip()
encontrar=True
while encontrar: 
    if palabra in palabras:
        print("Palabra encontrada")
    encontrar=False
if palabra not in palabras:
    print("Palabra no encontrada")




#Ejemplo 3 Añadir elementos a la lista
lista=[]
true=True
while true:
  lista.append(input("Dame un valor: ").strip())
  true=input("Ingresa True/False para continuar: ").strip()
  if true=="False":
     true=False
 
true="true"
while true=="true":
   lista.append(input("Dame un valor: ").strip())
   true=input("Ingresa True/False para continuar: ").strip().lower()
   


print(lista)

#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda

agenda=[
         ["Carlos","6181234567"],
         ["Adrian","6182332456"],
         ["Luis","6182223444"]
       ]
print(agenda)


for i in agenda:
   print(i)
lista=""
for r in range(0,3):
   for c in range(0,2):
      lista+=f"{agenda[r][c]}, "
   lista+="\n"
print(lista)