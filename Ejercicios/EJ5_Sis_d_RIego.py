# establezco la db de humedad por secciones del campo
estado_campo = {
    "seccion norte": {"humedad": 30, "riego_necesario": 0},
    "seccion sur": {"humedad": 55, "riego_necesario": 0}
}

def leer_humedad_suelo(seccion):
    # obtengo el porcentaje de agua actual en la tierra de la seccion elegida
    valor_humedad = estado_campo[seccion]["humedad"]
    # devuelvo el numero para que el sistema decida si activar el agua
    return valor_humedad

def consultar_prevision_clima():
    # simulo la conexion con un servicio de clima externo
    va_a_llover = False
    probabilidad_lluvia = 20
    # devuelvo los datos del clima para evitar riegos innecesarios
    return va_a_llover, probabilidad_lluvia

def calcular_cantidad_riego(seccion, lluvia_proxima):
    # procedimiento para definir cuantos litros de agua necesita el suelo
    
    humedad_actual = estado_campo[seccion]["humedad"]
    
    if humedad_actual < 40 and not lluvia_proxima:
        # si esta seco y no llovera asigno diez litros por metro cuadrado
        estado_campo[seccion]["riego_necesario"] = 10
        print("calculo finalizado para", seccion, "se requieren diez litros")
    else:
        # si hay humedad o viene lluvia ahorro agua
        estado_campo[seccion]["riego_necesario"] = 0
        print("calculo finalizado para", seccion, "no requiere riego por ahora")

def controlar_valvulas_riego(seccion):
    # funcion que ejecuta la apertura de los aspersores
    litros = estado_campo[seccion]["riego_necesario"]
    exito = False
    
    if litros > 0:
        print("abriendo valvulas de", seccion, "liberando", litros, "litros")
        exito = True
    else:
        print("manteniendo valvulas de", seccion, "cerradas")
        
    # devuelvo verdadero si el riego se ejecuto correctamente
    return exito

def ejecutar_sistema_riego():
    # coordino la lectura de sensores y el clima para iniciar el riego
    seccion_objetivo = "seccion norte"
    
    # primero reviso el cielo
    vendra_lluvia, probabilidad = consultar_prevision_clima()
    
    # luego  calculo cuanto regar segun la humedad y el clima
    calcular_cantidad_riego(seccion_objetivo, vendra_lluvia)
    
    # finalmente intento abrir las valvulas
    riego_activo = controlar_valvulas_riego(seccion_objetivo)
    
    if riego_activo:
        print("proceso de riego en curso satisfactoriamente")

# inicio el programa de automatizacion agricola
ejecutar_sistema_riego()