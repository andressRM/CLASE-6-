# defino mis parametros base para simular el comportamiento del sis
temperatura_base = 22
temperatura_nocturna = 18

def leer_sensores_temperatura(zona):
    # simulo la lectura de la temperatura actual de la zona especificada
    temperatura_actual = temperatura_base
    return temperatura_actual

def calcular_temperatura_optima(hora, hay_gente, clima_exterior):
    # calculo cual deberia ser la temperatura ideal dependiendo de las variables
    temperatura_ideal = temperatura_base
    
    # reviso si es de noche para bajar la temperatura y ahorrar
    if hora < 6 or hora > 22:
        temperatura_ideal = temperatura_nocturna
        
    # reviso si la habitacion esta vacia para no gastar eergia
    if not hay_gente:
        temperatura_ideal = temperatura_nocturna
        
    # compenso si hace mucho frio afuera subiendo un gradp
    if clima_exterior < 10:
        temperatura_ideal = temperatura_ideal + 1
        
    # devuelvo la temperatura que el sistema deberia alcanzar
    return temperatura_ideal

def ajustar_climatizacion(zona, temperatura_actual, temperatura_ideal):
    # procedimiento que ejecuta la accion fisica sin devolver ningun valor
    
    # verifico si hace falta encender la calefaccion
    if temperatura_actual < temperatura_ideal:
        print(zona, "activando calefaccion para alcanzar temperatura ideal")
        
    # verifico si hac falta encender el aire acondicionado
    elif temperatura_actual > temperatura_ideal:
        print(zona, "activando aire acondicionado para alcanzar temperatura ideal")
        
    # si las temperaturas son iguales no hago nada
    else:
        print(zona, "temperatura perfecta no se requiere accion")

def registrar_consumo(zona, accion_tomada):
    # guardo el registro de la energia gastada para futuros analisis
    
    # simulo un gasto de energia base
    gasto_energia = 0
    
    # sumo gasto si el sistema tuvo que encenderse
    if accion_tomada != "ninguna":
        gasto_energia = 5
        
    # devuelvo el valor del gasto calculado
    return gasto_energia

def ejecutar_sistema_edificio():
    # funcion principal 
    
    # defino mis variables simuladas para probar el sistema
    hora_actual = 23
    zona_actual = "oficina principal"
    ocupacion = False
    clima_afuera = 8
    
    # llamo a la funcion para leer mi sensor
    temp_actual = leer_sensores_temperatura(zona_actual)
    
    # llamo a la funcion para calcular la meta
    temp_ideal = calcular_temperatura_optima(hora_actual, ocupacion, clima_afuera)
    
    # llamo a mi procedimiento para ejecutar la accion
    ajustar_climatizacion(zona_actual, temp_actual, temp_ideal)
    
    # defino que accion se tomo para calcular el gasto
    accion = "calefaccion" if temp_actual < temp_ideal else "ninguna"
    
    # llamo a mi funcion de registro para ver cuanto gaste
    consumo = registrar_consumo(zona_actual, accion)
    
    # imprimo un reporte final del sistema
    print("reporte de consumo finalizado energia gastada", consumo)

# ejecuto mi programa principal para iniciar el ciclo
ejecutar_sistema_edificio()