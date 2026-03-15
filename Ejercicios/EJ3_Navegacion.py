# establezco las variables globales que representan el estado del vehiculo
estado_vehiculo = {"velocidad": 0, "ruta": "ninguna", "obstaculo_cerca": False}

def leer_sensores_navegacion():
    # obtengo los datos de las camaras y los sensores
    hay_objetos = True
    distancia_metros = 5
    # devuelvo la informacion recolectada para procesarla luego
    return hay_objetos, distancia_metros

def calcular_ruta_optima(destino):
    # procedimiento para definir el mejor camino segun el trafico actual
    # no uso return porque modifico directamente el estado global del sistema
    print("analizando mapas y trafico para llegar a", destino)
    estado_vehiculo["ruta"] = "autopista central"
    print("ruta establecida por la autopista central")

def detectar_y_evitar_obstaculos(hay_objetos, distancia):
    # funcion que decide si el carro debe frenar o esquivar
    maniobra_necesaria = False
    
    # reviso si el objeto esta a menos de diez metros para actuar
    if hay_objetos and distancia < 10:
        print("peligro detectado iniciando maniobra de evasion")
        maniobra_necesaria = True
        
    # devuelvo la decision logica para que el motor reaccione
    return maniobra_necesaria

def ajustar_velocidad_trafico(intensidad_trafico):
    # procedimiento para cambiar la rapidez del carro segun los demas vehiculos
    
    if intensidad_trafico == "alta":
        estado_vehiculo["velocidad"] = 30
    elif intensidad_trafico == "baja":
        estado_vehiculo["velocidad"] = 80
    else:
        estado_vehiculo["velocidad"] = 50
    print("velocidad ajustada a", estado_vehiculo["velocidad"], "kilometros por hora")

def ejecutar_navegacion_autonoma():
    # modulos para simular el viaje del vehiculo
    
    # defino mi destino de prueba
    mi_destino = "centro comercial cci"
    
    # calculo la ruta primero
    calcular_ruta_optima(mi_destino)
    
    # leo los sensores constantemente
    objetos, metros = leer_sensores_navegacion()
    
    # decido si debo esquivar algo o no
    si_esquivo = detectar_y_evitar_obstaculos(objetos, metros)
    
    # ajusto la marcha segun como este la calle
    if si_esquivo:
        ajustar_velocidad_trafico("alta")
    else:
        ajustar_velocidad_trafico("media")

# arranco el sistema de navegacion
ejecutar_navegacion_autonoma()