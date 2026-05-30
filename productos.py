
# productos.py
# Jerarquia de clases de los productos del super (HERENCIA).

#  CLASE PADRE 
class Producto:
    def __init__(self, nombre, marca, precio, peso, stock, codigo_barras, stock_minimo):
        self._nombre = nombre
        self._marca = marca
        self._precio = precio
        self._peso = peso
        self._stock = stock
        self._codigo_barras = codigo_barras
        self._stock_minimo = stock_minimo

    def obtener_precio(self):
        return self._precio

    def obtener_stock(self):
        return self._stock

    def decrementar_stock(self):
        self._stock -= 1

    def incrementar_stock(self):
        self._stock += 1

    # lo que muestra la Tablet de la gondola
    def mostrar_info(self):
        return f"{self._nombre} {self._marca} ${self._precio} (stock: {self._stock})"

    #  getters: metodo cuyo unico trabajo es DEVOLVER el valor de un atributo privado 
    def obtener_nombre(self):
        return self._nombre

    def obtener_codigo_barras(self):
        return self._codigo_barras

    def obtener_marca(self):
        return self._marca

    def obtener_stock_minimo(self):
        return self._stock_minimo


#  RAMA 1: PRODUCTOS DE GONDOLA 
class ProductoGondola(Producto):
    def __init__(self, nombre, marca, precio, peso, stock, codigo_barras, stock_minimo):
        super().__init__(nombre, marca, precio, peso, stock, codigo_barras, stock_minimo)


#  RAMA 2: PRODUCTOS ESPECIALES 
class ProductoEspecial(Producto):
    def __init__(self, nombre, marca, precio, peso, stock, codigo_barras, stock_minimo, precio_por_kg, peso_real):
        super().__init__(nombre, marca, precio, peso, stock, codigo_barras, stock_minimo)
        self._precio_por_kg = precio_por_kg
        self._peso_real = peso_real

    # precio segun el peso real (precio por kg * peso)
    def calcular_precio(self):
        return self._precio_por_kg * self._peso_real

    # POLIMORFISMO: para los productos por peso, el "precio" es el calculado.
    # asi el carrito y el almacen cobran el peso real, no el precio por unidad.
    def obtener_precio(self):
        return self.calcular_precio()


#   SUBCLASES ESPECIFICAS

class Galletita(ProductoGondola):
    def __init__(self, nombre, marca, precio, peso, stock, codigo_barras, stock_minimo):
        super().__init__(nombre, marca, precio, peso, stock, codigo_barras, stock_minimo)


class Perfumeria(ProductoGondola):
    def __init__(self, nombre, marca, precio, peso, stock, codigo_barras, stock_minimo, tipo_producto):
        super().__init__(nombre, marca, precio, peso, stock, codigo_barras, stock_minimo)
        self._tipo_producto = tipo_producto


class Bebida(ProductoGondola):
    def __init__(self, nombre, marca, precio, peso, stock, codigo_barras, stock_minimo, litros):
        super().__init__(nombre, marca, precio, peso, stock, codigo_barras, stock_minimo)
        self._litros = litros

    # tenemos que informar la cantidad de litros en los liquidos
    def mostrar_info(self):
        return f"{self._nombre} {self._marca} {self._litros}L ${self._precio} (stock: {self._stock})"


class Limpieza(ProductoGondola):
    def __init__(self, nombre, marca, precio, peso, stock, codigo_barras, stock_minimo, tipo_producto):
        super().__init__(nombre, marca, precio, peso, stock, codigo_barras, stock_minimo)
        self._tipo_producto = tipo_producto


class Lacteo(ProductoGondola):
    def __init__(self, nombre, marca, precio, peso, stock, codigo_barras, stock_minimo, tipo_producto, refrigerado):
        super().__init__(nombre, marca, precio, peso, stock, codigo_barras, stock_minimo)
        self._tipo_producto = tipo_producto
        self._refrigerado = refrigerado


class Panaderia(ProductoEspecial):
    def __init__(self, nombre, marca, precio, peso, stock, codigo_barras, stock_minimo, precio_por_kg, peso_real, tipo_pan, cant_bols, es_factura, precio_x_unidad):
        super().__init__(nombre, marca, precio, peso, stock, codigo_barras, stock_minimo, precio_por_kg, peso_real)
        self._tipo_pan = tipo_pan
        self._cant_bols = cant_bols
        self._es_factura = es_factura
        self._precio_x_unidad = precio_x_unidad

    # las facturas van por unidad; el pan, por peso
    def obtener_precio(self):
        if self._es_factura:
            return self._precio_x_unidad
        return self.calcular_precio()

    def mostrar_info(self):
        if self._es_factura:
            return f"{self._nombre} {self._marca} ${self._precio_x_unidad}/u (stock: {self._stock})"
        return (f"{self._nombre} ({self._tipo_pan}) {self._peso_real}kg x ${self._precio_por_kg}/kg "
                f"= ${self.calcular_precio()} | {self._cant_bols} bolsones (stock: {self._stock})")


class Fiambreria(ProductoEspecial):
    def __init__(self, nombre, marca, precio, peso, stock, codigo_barras, stock_minimo, precio_por_kg, peso_real, tipo, precio_bandeja):
        super().__init__(nombre, marca, precio, peso, stock, codigo_barras, stock_minimo, precio_por_kg, peso_real)
        self._tipo = tipo
        self._precio_bandeja = precio_bandeja

    def mostrar_info(self):
        return (f"{self._nombre} {self._marca} ({self._tipo}) ${self._precio_por_kg}/kg | "
                f"bandeja {self._peso_real}kg = ${self.calcular_precio()} (stock: {self._stock})")


class Verduleria(ProductoEspecial):
    def __init__(self, nombre, marca, precio, peso, stock, codigo_barras, stock_minimo, precio_por_kg, peso_real, tipo_verdura, es_x_unidad):
        super().__init__(nombre, marca, precio, peso, stock, codigo_barras, stock_minimo, precio_por_kg, peso_real)
        self._tipo_verdura = tipo_verdura
        self._es_x_unidad = es_x_unidad

    # algunas verduras van por unidad y otras por peso
    def obtener_precio(self):
        if self._es_x_unidad:
            return self._precio
        return self.calcular_precio()

    def mostrar_info(self):
        if self._es_x_unidad:
            return f"{self._nombre} ${self._precio}/u (stock: {self._stock})"
        return (f"{self._nombre} {self._peso_real}kg x ${self._precio_por_kg}/kg "
                f"= ${self.calcular_precio()} (stock: {self._stock})")