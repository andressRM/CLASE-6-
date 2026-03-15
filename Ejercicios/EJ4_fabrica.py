# creo una estructura para conocer el estado de mi produccion
maquinas = {
    "prensa": {"estado": "operativa", "horas_uso": 120, "piezas_producidas": 1000},
    "soldadora": {"estado": "alerta", "horas_uso": 195, "piezas_producidas": 800}
}

def monitorear_estado_maquina(nombre):
    # reviso si la maquina necesita atencion inmediata segun su estado actual
    estado_critico = maquinas[nombre]["estado"] == "critico"
    
    # devuelvo el valor logico para decidir si detengo la linea
    return estado_critico

def planificar_mantenimiento(nombre):
    # procedimiento para programar revisiones tecnicas segun las horas de uso 
    # modifico el estado sin retornar datos para ahorrar memoria
    if maquinas[nombre]["horas_uso"] > 150:
        maquinas[nombre]["estado"] = "mantenimiento"
        print("maquina", nombre, "enviada a revision preventiva")
    else:
        print("maquina", nombre, "continua operando normalmente")

def analizar_rendimiento(nombre, meta_piezas):
    # calcular la eficiencia d la maquina comparando piezas con la meta
    producido = maquinas[nombre]["piezas_producidas"]
    eficiencia = (producido / meta_piezas) * 100
    
    # devuelvo el porcentaje de rendimiento
    return eficiencia

def ajustar_programacion_demanda(nivel_demanda):
    # procedimiento que cambia el ritmo de trabajo de toda la fabrica
    if nivel_demanda == "alto":
        print("ajustando turnos a veinticuatro horas por alta demanda")
    elif nivel_demanda == "bajo":
        print("reduciendo turnos para evitar sobreproduccion")
    else:
        print("manteniendo ritmo de produccion estandar")

def ejecutar_sistema_fabrica():
    # coordino los modulos para optimizar la produccion diaria
    
    maquina_test = "soldadora"
    demanda_actual = "alto"
    
    # primero ajusto la fabrica segun lo que pide el mercado
    ajustar_programacion_demanda(demanda_actual)
    
    # monitoreo si hay fallos graves
    hay_fallo = monitorear_estado_maquina(maquina_test)
    
    if not hay_fallo:
        # calculo el rendimiento antes de decidir mantenimiento o no
        rendimiento = analizar_rendimiento(maquina_test, 1000)
        print("el rendimiento de", maquina_test, "es de", rendimiento, "por ciento")
        
        # aplico mantenimiento preventivo solo si es necesario
        planificar_mantenimiento(maquina_test)
    else:
        print("parada de emergencia en maquina", maquina_test)

# inicio la ejecucion de mi sistema de la fbrica
ejecutar_sistema_fabrica()