# creo mi base de datos principal de suposicion para el almacen
inventario = {
    "procesadores": {"cantidad": 50, "ventas_mes": 80, "optimo": 0},
    "pantallas": {"cantidad": 200, "ventas_mes": 30, "optimo": 0}
}

def registrar_entrada_producto(articulo, cantidad_ingresada):
    # sumo la mercaderia nueva a la cantidad que ya tenia
    inventario[articulo]["cantidad"] = inventario[articulo]["cantidad"] + cantidad_ingresada
    
    # devuelvo el nuevo total para confirmar que se guardo
    return inventario[articulo]["cantidad"]

def registrar_salida_producto(articulo, cantidad_retirada):
    # resto los productos vendidos de mi db
    inventario[articulo]["cantidad"] = inventario[articulo]["cantidad"] - cantidad_retirada
    
    # devuelvo el total restante en la bodega
    return inventario[articulo]["cantidad"]

def calcular_nivel_optimo(articulo):
    # procedimiento puro que actualiza los datos sin devolver ningun valor
    
    # multiplico las ventas por dos para asegurar tener un buen margen de seguridad
    meta_calculada = inventario[articulo]["ventas_mes"] + inventario[articulo]["ventas_mes"]
    
    # guardo el calculo directamente en la memoria de mi inventario
    inventario[articulo]["optimo"] = meta_calculada

def generar_alerta_reabastecimiento(articulo):
    # comparo si me quedan menos productos de los que deberia tener
    necesita_comprar = inventario[articulo]["cantidad"] < inventario[articulo]["optimo"]
    
    # devuelvo verdadero si hay que comprar o falso si hay suficientes
    return necesita_comprar

def ejecutar_sistema_almacen():
    # agrupo todas mis funciones para simular un dia de trabajo
    
    # defino el producto con el que voy a hacer la prueba
    producto_prueba = "procesadores"
    
    # configuro cual es el nivelk optimo usando mi procedimiento
    calcular_nivel_optimo(producto_prueba)
    
    # simulo que el almacen recibio nuevos productos
    registrar_entrada_producto(producto_prueba, 10)
    
    # simulo que vendimos bastantes productos de golpe
    registrar_salida_producto(producto_prueba, 55)
    
    # reviso si despues de la venta necesito llamar al proveedor
    alerta_compras = generar_alerta_reabastecimiento(producto_prueba)
    
    # imprimo un mensaje en la consola dependiendo del resultado de la alerta
    if alerta_compras:
        print("alerta critica debemos reabastecer", producto_prueba)
    else:
        print("niveles estables para", producto_prueba)

# enciendo mi sistema llamando a mi bloque central
ejecutar_sistema_almacen()