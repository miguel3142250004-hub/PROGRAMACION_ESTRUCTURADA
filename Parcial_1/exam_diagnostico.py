def borrarPantalla():
 print("\033c")

def ventaAutos():
    borrarPantalla()
    opc="S"
    autos=0
    acum_pv=0

    while opc=="S":

     marca=input("Marca: ").strip().upper()
     origen=input("Origen: ").strip().upper()
     costo=float(input("Costo: "))

    #Proceso
     if origen=="ALEMANIA":
      impuesto=0.20
     elif origen=="JAPON":
      impuesto=0.30
     elif origen=="ITALIA":
      impuesto=0.15
     elif origen=="USA":
      impuesto=0.08
     else :
      impuesto=0
    
     impuesto_pesos=costo*impuesto
     pv=impuesto_pesos+costo

     print(f"El impuesto a pagar es: ${impuesto_pesos}")
     print(f"El precio de venta es: ${pv}")
     autos+=1
     acum_pv+=pv

     opc=input("Deseas realizar otra vrz el proceso (S/N)?").upper().strip()

    print(f"El total de los vehiculos es : {autos} \n Y el monto total de los precios de venta es: ${acum_pv}")
ventaAutos()