#1. solicitar al usuario que ingrese las medidas (y trasnformarlas a numeros )
convert_cm_pul= float(input("Por favor ingrese las medidas de las piezas del mueble (en cm ): "))
#2. convertir las medidas de cm a pulgadas
inches_measure =  convert_cm_pul / 2.54
#3. mostrar las medidad convertidas
print("Las medidas en pulgadas de la pieza ingresada es: ", inches_measure )