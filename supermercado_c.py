#   supermercado_c.py

from productos import ProductoGondola
from productos import Producto


class Gondola:
    def __init__(self, nombre, promocion):
        self._nombre = nombre
        self._productos = []
        self._promocion = promocion

    def agregar_productos(self, producto):
        self._productos.append(producto)

    def quitar_producto(self, producto):
        self._productos.remove(producto)

    def mostrar_tablet(self):
        print(f"=== Góndola {self._nombre} ===")
        for producto in self._productos:
            print(producto.mostrar_info())

    def mostrar_promociones(self):
        print(f"=== Promociones {self._nombre} ===")
        for producto in self._productos:
            # muestro el precio llevando 2 unidades, asi se ve el beneficio de la promo
            precio_final = self._promocion.calcular_precio_final(producto.obtener_precio(), 2)
            print(f"{producto.mostrar_info()} -> Llevando 2: ${precio_final}")

    # getters
    def obtener_productos(self):
        return self._productos

    def obtener_nombre(self):
        return self._nombre


class Promocion:
    def __init__(self, tipo, descuento, gondola_aplicable, aplica_misma_marca):
        self._tipo = tipo
        self._descuento = descuento
        self._gondola_aplicable = gondola_aplicable
        self._aplica_misma_marca = aplica_misma_marca

    def calcular_precio_final(self, precio, cantidad):
        if self._tipo == "2x1":
            # paga la mitad (redondeando para arriba): 2 lleva 1, 3 lleva 2, etc.
            pagadas = cantidad // 2 + cantidad % 2
            return pagadas * precio

        elif self._tipo == "porcentaje_total":
            # descuento sobre TODAS las unidades (ej: perfumeria 50%)
            precio_total = precio * cantidad
            return precio_total - (precio_total * self._descuento)

        elif self._tipo == "porcentaje_segunda":
            # descuento solo en la segunda unidad de cada par (ej: bebidas 30%)
            unidades_con_descuento = cantidad // 2
            precio_total = precio * cantidad
            descuento = precio * unidades_con_descuento * self._descuento
            return precio_total - descuento

        else:
            # sin promo
            return precio * cantidad

    # getters
    def obtener_gondola_aplicable(self):
        return self._gondola_aplicable


class Carrito:
    def __init__(self):
        self._total = 0
        self._productos = []

    def mostrar_pantalla_oled(self):
        print(f"=== Pantalla OLED === Total: ${self._total}")

    def obtener_total(self):
        return self._total

    def obtener_productos(self):
        return self._productos

    def agregar_producto(self, producto, almacen, cantidad):
        for i in range(cantidad):
            self._productos.append(producto)
            almacen.chequear_stock(producto)
        precio = almacen.calcular_promocion(producto, cantidad)
        self._total += precio
        self.mostrar_pantalla_oled()

    def quitar_producto(self, producto, almacen):
        self._productos.remove(producto)
        precio = almacen.calcular_promocion(producto, 1)
        self._total -= precio
        self.mostrar_pantalla_oled()


class Almacen:
    def __init__(self, inventario):
        self._inventario = inventario
        self._gondolas = []
        self._promociones = []
        self._proveedores = []

    def buscar_producto_x_codigo(self, codigo_barras):
        for gondola in self._gondolas:
            for producto in gondola.obtener_productos():
                if producto.obtener_codigo_barras() == codigo_barras:
                    return producto
        return None

    def determinar_precio(self, producto):
        return producto.obtener_precio()

    def calcular_promocion(self, producto, cantidad):
        for promocion in self._promociones:
            for gondola in self._gondolas:
                if gondola.obtener_nombre() == promocion.obtener_gondola_aplicable():
                    if producto in gondola.obtener_productos():
                        return promocion.calcular_precio_final(producto.obtener_precio(), cantidad)
        # si no hay promo aplicable, precio normal por cantidad
        return producto.obtener_precio() * cantidad

    # cada vez que se agrega un producto: decrementa, y si cae por debajo del minimo aplica la prioridad gondola -> deposito -> proveedor.
    def chequear_stock(self, producto):
        self._inventario.decrementar_stock(producto)
        if self._inventario.verificar_stock(producto):  # quedo por debajo del minimo
            repuesto = self._inventario.reponer_desde_deposito(producto)
            if not repuesto:
                # no habia en deposito -> se pide al proveedor externo
                self.solicitar_reposicion(producto)

    def solicitar_reposicion(self, producto):
        pedido = self._inventario.generar_pedido(producto)
        for proveedor in self._proveedores:
            if producto.obtener_nombre() in proveedor.obtener_productos_que_provee():
                proveedor.recibir_pedido(pedido)
                proveedor.despachar_pedido(pedido)
                # tras la reposicion satisfactoria se actualiza el stock
                self._inventario.actualizar_stock(producto, 50)
                return
        print(f"No se encontró proveedor para {producto.obtener_nombre()}")

    def agregar_gondola(self, gondola):
        self._gondolas.append(gondola)

    def agregar_promocion(self, promocion):
        self._promociones.append(promocion)

    def agregar_proveedor(self, proveedor):
        self._proveedores.append(proveedor)


class Pedido:
    def __init__(self, marca, nombre_producto, cantidad):
        self._marca = marca
        self._nombre_producto = nombre_producto
        self._cantidad = cantidad
        self._estado = "Pendiente"

    def marcar_despachado(self):
        self._estado = "Despachado"


class Inventario:
    def __init__(self, deposito):
        self._productos = {}
        self._deposito = deposito

    def registrar_producto(self, producto):
        self._productos[producto] = producto.obtener_stock()

    def verificar_stock(self, producto):
        # True si la cantidad disponible esta por debajo (o igual) del umbral minimo
        if self._productos[producto] <= producto.obtener_stock_minimo():
            return True
        return False

    def decrementar_stock(self, producto):
        self._productos[producto] -= 1
        producto.decrementar_stock()

    def reponer_desde_deposito(self, producto):
        if self._deposito.hay_stock(producto):
            self._deposito.retirar_unidades(producto, 10)
            self._productos[producto] += 10
            # sincronizo tambien el stock propio del producto (la tablet lee de ahi)
            for i in range(10):
                producto.incrementar_stock()
            print(f"Se repusieron 10 unidades de {producto.obtener_nombre()} desde el depósito")
            return True
        else:
            print(f"No hay stock en depósito de {producto.obtener_nombre()} -> se pedirá al proveedor")
            return False

    def generar_pedido(self, producto):
        pedido = Pedido(producto.obtener_marca(), producto.obtener_nombre(), 50)
        print(f"Pedido generado: {producto.obtener_nombre()} x50 unidades")
        return pedido

    # actualizacion de stock tras la reposicion del proveedor (ej 10)
    def actualizar_stock(self, producto, cantidad):
        self._productos[producto] += cantidad
        for i in range(cantidad):
            producto.incrementar_stock()
        print(f"Stock actualizado: {producto.obtener_nombre()} +{cantidad} unidades "
              f"(disponible: {self._productos[producto]})")


class Proveedor:
    def __init__(self, nombre, productos_que_provee):
        self._nombre = nombre
        self._productos_que_provee = productos_que_provee
        self._pedidos = []

    def obtener_productos_que_provee(self):
        return self._productos_que_provee

    def recibir_pedido(self, pedido):
        self._pedidos.append(pedido)
        print(f"Proveedor {self._nombre} recibió un pedido")

    def despachar_pedido(self, pedido):
        pedido.marcar_despachado()
        print(f"Proveedor {self._nombre} despachó el pedido")


class Deposito:
    def __init__(self):
        self._stock_reserva = {}

    def hay_stock(self, producto):
        if producto in self._stock_reserva and self._stock_reserva[producto] > 0:
            return True
        return False

    def retirar_unidades(self, producto, cantidad):
        self._stock_reserva[producto] -= cantidad
        print(f"Se retiraron {cantidad} unidades de {producto.obtener_nombre()} del depósito")

    def agregar_unidades(self, producto, cantidad):
        if producto in self._stock_reserva:
            self._stock_reserva[producto] += cantidad
        else:
            self._stock_reserva[producto] = cantidad
        print(f"Se agregaron {cantidad} unidades de {producto.obtener_nombre()} al depósito")