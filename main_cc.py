from productos import *
from supermercado_c import *

#  SETUP DE PRODUCTOS

# Góndola Galletas
g1 = Galletita("Pepitos", "Arcor", 500, 200, 50, 1001, 10)
g2 = Galletita("Oreo", "Mondelez", 600, 150, 80, 1002, 10)
g3 = Galletita("Chocolinas", "Bagley", 450, 250, 30, 1003, 10)

# Góndola Bebidas
b1 = Bebida("Coca-Cola", "Coca-Cola", 2500, 1500, 100, 2001, 10, 1.5)
b2 = Bebida("Sprite", "Coca-Cola", 2500, 1500, 200, 2002, 10, 1.5)
b3 = Bebida("Naranja", "Manaos", 800, 1500, 50, 2003, 10, 1.5)

# Góndola Perfumería
p1 = Perfumeria("Lavandina", "Ayudin", 900, 1500, 100, 3001, 10, "limpieza")
p2 = Perfumeria("Jabón en polvo", "Zorro", 900, 400, 50, 3002, 10, "limpieza")
p3 = Perfumeria("Jabón Tocador", "Nivea", 200, 100, 30, 3003, 10, "cuidado personal")

# Góndola Limpieza
l1 = Limpieza("Desodorante piso", "Poett", 700, 900, 60, 4001, 10, "pisos")
l2 = Limpieza("Esponja", "Scotch-Brite", 300, 50, 100, 4002, 10, "cocina")
l3 = Limpieza("Detergente", "Magistral", 500, 750, 40, 4003, 10, "cocina")

# Góndola Lácteos
la1 = Lacteo("Leche entera", "La Serenísima", 800, 1000, 150, 5001, 10, "leche", True)
la2 = Lacteo("Yogur frutilla", "Danone", 600, 200, 80, 5002, 10, "yogur", True)
la3 = Lacteo("Queso crema", "Casancrem", 500, 300, 40, 5003, 10, "queso", True)

# Panadería
pan1 = Panaderia("Pan francés", "Panadería", 0, 1000, 30, 6001, 5, 800, 0.5, "francés", 10, False, 0)
pan2 = Panaderia("Pan lactal", "Bimbo", 0, 500, 20, 6002, 5, 1200, 0.5, "lactal", 5, False, 0)
pan3 = Panaderia("Facturas", "Panadería", 0, 100, 50, 6003, 5, 0, 0, "factura", 0, True, 150)

# Fiambrería  (segundo sector elegido entre panaderia/carniceria/fiambreria)
f1 = Fiambreria("Jamón cocido", "La Paulina", 0, 0, 30, 8001, 5, 8000, 0.25, "jamón", 2000)
f2 = Fiambreria("Queso de máquina", "Sancor", 0, 0, 25, 8002, 5, 6000, 0.30, "queso", 1800)
f3 = Fiambreria("Salame", "Cagnoli", 0, 0, 20, 8003, 5, 9000, 0.20, "salame", 1800)

# Verdulería
v1 = Verduleria("Tomate", "Sin marca", 500, 1000, 40, 7001, 5, 1200, 0.8, "tomate", False)
v2 = Verduleria("Lechuga", "Sin marca", 300, 500, 25, 7002, 5, 800, 0.3, "lechuga", True)
v3 = Verduleria("Papa", "Sin marca", 200, 2000, 60, 7003, 5, 600, 1.5, "papa", False)

#  PROMOCIONES
promo_galletas = Promocion("2x1", 0, "Galletas", False)
promo_bebidas = Promocion("porcentaje_segunda", 0.30, "Bebidas", True)   # 30% en la 2da unidad
promo_perfumeria = Promocion("porcentaje_total", 0.50, "Perfumería", False)  # 50% a todo

#  DEPÓSITO
deposito = Deposito()
deposito.agregar_unidades(g1, 100)
deposito.agregar_unidades(g2, 100)
deposito.agregar_unidades(g3, 100)
deposito.agregar_unidades(b1, 50)
deposito.agregar_unidades(b2, 50)
deposito.agregar_unidades(b3, 50)
deposito.agregar_unidades(p1, 30)
deposito.agregar_unidades(p2, 30)
deposito.agregar_unidades(p3, 30)

#  INVENTARIO
inventario = Inventario(deposito)
for prod in [g1, g2, g3, b1, b2, b3, p1, p2, p3, l1, l2, l3,
             la1, la2, la3, pan1, pan2, pan3, f1, f2, f3, v1, v2, v3]:
    inventario.registrar_producto(prod)

#  GÓNDOLAS
gondola_galletas = Gondola("Galletas", promo_galletas)
gondola_galletas.agregar_productos(g1)
gondola_galletas.agregar_productos(g2)
gondola_galletas.agregar_productos(g3)

gondola_bebidas = Gondola("Bebidas", promo_bebidas)
gondola_bebidas.agregar_productos(b1)
gondola_bebidas.agregar_productos(b2)
gondola_bebidas.agregar_productos(b3)

gondola_perfumeria = Gondola("Perfumería", promo_perfumeria)
gondola_perfumeria.agregar_productos(p1)
gondola_perfumeria.agregar_productos(p2)
gondola_perfumeria.agregar_productos(p3)

gondola_limpieza = Gondola("Limpieza", Promocion("ninguna", 0, "Limpieza", False))
gondola_limpieza.agregar_productos(l1)
gondola_limpieza.agregar_productos(l2)
gondola_limpieza.agregar_productos(l3)

gondola_lacteos = Gondola("Lácteos", Promocion("ninguna", 0, "Lácteos", False))
gondola_lacteos.agregar_productos(la1)
gondola_lacteos.agregar_productos(la2)
gondola_lacteos.agregar_productos(la3)

#  PROVEEDORES
proveedor1 = Proveedor("Arcor", ["Pepitos", "Chocolinas"])
proveedor2 = Proveedor("Coca-Cola", ["Coca-Cola", "Sprite"])
proveedor3 = Proveedor("Manaos", ["Naranja"])
proveedor4 = Proveedor("Distribuidora Láctea", ["Leche entera", "Yogur frutilla", "Queso crema"])
proveedor5 = Proveedor("Distribuidora Limpieza", ["Desodorante piso", "Esponja", "Detergente"])
proveedor6 = Proveedor("Fiambres del Sur", ["Jamón cocido", "Queso de máquina", "Salame"])
proveedor7 = Proveedor("Verdulería Central", ["Tomate", "Lechuga", "Papa"])
proveedor8 = Proveedor("Panificados", ["Pan francés", "Pan lactal", "Facturas"])

#  ALMACÉN
almacen = Almacen(inventario)
almacen.agregar_gondola(gondola_galletas)
almacen.agregar_gondola(gondola_bebidas)
almacen.agregar_gondola(gondola_perfumeria)
almacen.agregar_gondola(gondola_limpieza)
almacen.agregar_gondola(gondola_lacteos)
almacen.agregar_promocion(promo_galletas)
almacen.agregar_promocion(promo_bebidas)
almacen.agregar_promocion(promo_perfumeria)
for prov in [proveedor1, proveedor2, proveedor3, proveedor4,
             proveedor5, proveedor6, proveedor7, proveedor8]:
    almacen.agregar_proveedor(prov)

"""
usamos "codigos de escape ANSI": secuencias especiales que la terminal interpreta como una instruccion de color en vez de imprimirlas como texto.
El "\033" es el caracter de escape (avisa que viene una instruccion) y el numero (ej: 32) indica el color: 31 rojo, 32 verde, 33 amarillo, 34 azul, etc.
cada variable guarda un color para no tener que escribir el codigo cada vez.
RESET vuelve la terminal al color normal; se pone al final de cada texto coloreado, sino TODO lo que se imprima despues queda con ese color como "pegado"
"""
#  COLORES
VERDE = "\033[1;32m"
AZUL = "\033[1;34m"
AMARILLO = "\033[1;33m"
ROJO = "\033[1;31m"
CYAN = "\033[1;36m"
MAGENTA = "\033[1;35m"
BLANCO = "\033[1;37m"
RESET = "\033[0m"

#  DATOS PARA EL MENÚ
gondolas_dict = {
    "1": ("Galletas", gondola_galletas),
    "2": ("Bebidas", gondola_bebidas),
    "3": ("Perfumería", gondola_perfumeria),
    "4": ("Limpieza", gondola_limpieza),
    "5": ("Lácteos", gondola_lacteos),
}

productos_especiales = {
    "6": ("Panadería", [pan1, pan2, pan3]),
    "7": ("Fiambrería", [f1, f2, f3]),
    "8": ("Verdulería", [v1, v2, v3]),
}

# diccionario codigo => producto (simula el lector) y codigo => sector
todos_los_productos = {}
codigo_a_sector = {}
for nombre, gondola_obj in gondolas_dict.values():
    for prod in gondola_obj.obtener_productos():
        todos_los_productos[prod.obtener_codigo_barras()] = prod
        codigo_a_sector[prod.obtener_codigo_barras()] = nombre
for nombre, productos_lista in productos_especiales.values():
    for prod in productos_lista:
        todos_los_productos[prod.obtener_codigo_barras()] = prod
        codigo_a_sector[prod.obtener_codigo_barras()] = nombre

# todos los sectores que el cliente tiene que recorrer (ej 6)
TODOS_LOS_SECTORES = set()
for nombre, _ in gondolas_dict.values():
    TODOS_LOS_SECTORES.add(nombre)
for nombre, _ in productos_especiales.values():
    TODOS_LOS_SECTORES.add(nombre)

sectores_comprados = set()  # se va llenando a medida que el cliente compra

#  FUNCIONES DE INTERFAZ

def mostrar_bienvenida():
    print(f"""
{CYAN}╔═══════════════════════════════════════════════════╗
║                                                   ║
║   {AMARILLO}███████╗█████╗ ██╗   ██╗ █████╗{CYAN}                 ║
║   {AMARILLO}██╔════╝██╔══██╗██║   ██║██╔══██╗{CYAN}               ║
║   {AMARILLO}█████╗  ███████║██║   ██║███████║{CYAN}               ║
║   {AMARILLO}██╔══╝  ██╔══██║╚██╗ ██╔╝██╔══██║{CYAN}               ║
║   {AMARILLO}██║     ██║  ██║ ╚████╔╝ ██║  ██║{CYAN}               ║
║   {AMARILLO}╚═╝     ╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝{CYAN}               ║
║                                                   ║
║   {VERDE}███╗   ███╗ █████╗ ██████╗ ██╗  ██╗███████╗████████╗{CYAN}║
║   {VERDE}████╗ ████║██╔══██╗██╔══██╗██║ ██╔╝██╔════╝╚══██╔══╝{CYAN}║
║   {VERDE}██╔████╔╝███████║██████╔╝█████╔╝ █████╗     ██║{CYAN}   ║
║   {VERDE}██║╚██╔╝██╔══██║██╔══██╗██╔═██╗ ██╔══╝     ██║{CYAN}   ║
║   {VERDE}██║ ╚═╝ ██║  ██║██║  ██║██║  ██╗███████╗   ██║{CYAN}   ║
║   {VERDE}╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝{CYAN}   ║
║                                                   ║
║     {BLANCO}Tu supermercado inteligente del futuro{CYAN}         ║
║          {BLANCO}Universidad Favaloro{CYAN}                      ║
║                                                   ║
╚═══════════════════════════════════════════════════╝{RESET}
""")

def mostrar_menu():
    print(f"""
{CYAN}╔══════════════════════════════════════╗
║     {AMARILLO}MENU PRINCIPAL - FavaMarket{CYAN}      ║
╠══════════════════════════════════════╣
║                                      ║
║   {VERDE}1.{BLANCO} Ver góndolas y sectores         {CYAN}║
║   {VERDE}2.{BLANCO} Ver promociones                 {CYAN}║
║   {VERDE}3.{BLANCO} Escanear producto (código)      {CYAN}║
║   {VERDE}4.{BLANCO} Ver carrito                     {CYAN}║
║   {VERDE}5.{BLANCO} Ir a la caja                    {CYAN}║
║                                      ║
╚══════════════════════════════════════╝{RESET}""")

def ver_gondolas():
    print(f"\n{CYAN}══════════ SECTORES DISPONIBLES ══════════{RESET}\n")
    for num, (nombre, _) in gondolas_dict.items():
        print(f"  {VERDE}{num}.{RESET} Góndola {nombre}")
    for num, (nombre, _) in productos_especiales.items():
        print(f"  {VERDE}{num}.{RESET} Sector {nombre}")
    print(f"  {VERDE}0.{RESET} Volver al menú")

    opcion = input(f"\n{AMARILLO}Seleccione un sector: {RESET}")

    if opcion in gondolas_dict:
        nombre, gondola_obj = gondolas_dict[opcion]
        print(f"\n{CYAN}══════ Tablet - Góndola {nombre} ══════{RESET}")
        for prod in gondola_obj.obtener_productos():
            print(f"  {BLANCO}Código: {AMARILLO}{prod.obtener_codigo_barras()}{RESET} | {prod.mostrar_info()}")
    elif opcion in productos_especiales:
        nombre, productos_lista = productos_especiales[opcion]
        print(f"\n{CYAN}══════ Sector {nombre} ══════{RESET}")
        for prod in productos_lista:
            print(f"  {BLANCO}Código: {AMARILLO}{prod.obtener_codigo_barras()}{RESET} | {prod.mostrar_info()}")
    elif opcion == "0":
        return
    else:
        print(f"{ROJO}Opción no válida.{RESET}")

def ver_promociones():
    print(f"\n{MAGENTA}╔══════════════════════════════════════╗")
    print(f"║     {AMARILLO}PROMOCIONES FAVAMARKET{MAGENTA}           ║")
    print(f"╚══════════════════════════════════════╝{RESET}\n")

    print(f"  {VERDE}Galletas:{RESET} 2x1 en cualquier marca")
    print(f"  {VERDE}Bebidas:{RESET} 30% en la segunda unidad (misma marca)")
    print(f"  {VERDE}Perfumería:{RESET} 50% en cualquier producto\n")

    print(f"{CYAN}--- Precios con promoción ---{RESET}")
    gondola_galletas.mostrar_promociones()
    print()
    gondola_bebidas.mostrar_promociones()
    print()
    gondola_perfumeria.mostrar_promociones()

def escanear_producto(carrito, almacen):
    codigo = input(f"\n{AMARILLO}Ingrese el código de barras: {RESET}")

    try:
        codigo = int(codigo)
    except ValueError:
        print(f"{ROJO}Código inválido. Debe ser un número.{RESET}")
        return

    if codigo in todos_los_productos:
        producto = todos_los_productos[codigo]
        print(f"\n  {VERDE}Producto encontrado:{RESET} {producto.mostrar_info()}")
        confirmar = input(f"  {AMARILLO}¿Agregar al carrito? (s/n): {RESET}")

        if confirmar.lower() == "s":
            cantidad = input(f"  {AMARILLO}¿Cuántas unidades? {RESET}")
            try:
                cantidad = int(cantidad)
            except ValueError:
                print(f"{ROJO}Cantidad inválida.{RESET}")
                return
            carrito.agregar_producto(producto, almacen, cantidad)
            # Registro el sector como comprado (consigna 6)
            sectores_comprados.add(codigo_a_sector[codigo])
            print(f"  {VERDE}{cantidad} unidad(es) agregada(s) al carrito{RESET}")
    else:
        print(f"{ROJO}Producto no encontrado.{RESET}")

def ver_carrito(carrito):
    print(f"\n{CYAN}╔══════════════════════════════════════╗")
    print(f"║     {AMARILLO}PANTALLA OLED - CARRITO{CYAN}          ║")
    print(f"╚══════════════════════════════════════╝{RESET}")
    productos = carrito.obtener_productos()
    if len(productos) == 0:
        print(f"  {BLANCO}El carrito está vacío.{RESET}")
    else:
        # Cuento cuantas unidades de cada producto hay
        conteo = {}
        for prod in productos:
            conteo[prod] = conteo.get(prod, 0) + 1
        for prod, cant in conteo.items():
            print(f"  {BLANCO}{cant}x {prod.obtener_nombre()} {prod.obtener_marca()}{RESET}")
    carrito.mostrar_pantalla_oled()

def ir_a_la_caja(carrito):
    # ej 6: el cliente tiene que haber comprado en TODOS los sectores
    faltan = TODOS_LOS_SECTORES - sectores_comprados
    if faltan:
        print(f"\n{ROJO}No podés ir a la caja todavía.{RESET}")
        print(f"  {AMARILLO}Te falta comprar en: {', '.join(sorted(faltan))}{RESET}")
        return False

    print(f"""
{VERDE}╔══════════════════════════════════════════╗
║                                          ║
║   {AMARILLO}GRACIAS POR COMPRAR EN FAVAMARKET!{VERDE}
║                                          ║
║   {BLANCO}Su compra total es: {CYAN}${carrito.obtener_total()}{VERDE}
║                                          ║
║   {BLANCO}Vuelva pronto!{VERDE}          ║
║   {BLANCO}Universidad Favaloro - LP1{VERDE}                           
║                                          ║
╚══════════════════════════════════════════╝{RESET}
""")
    return True

# ========== PROGRAMA PRINCIPAL 
mostrar_bienvenida()

carrito = Carrito()
ejecutando = True

while ejecutando:
    mostrar_menu()
    opcion = input(f"{AMARILLO}Seleccione una opción: {RESET}")

    if opcion == "1":
        ver_gondolas()
    elif opcion == "2":
        ver_promociones()
    elif opcion == "3":
        escanear_producto(carrito, almacen)
    elif opcion == "4":
        ver_carrito(carrito)
    elif opcion == "5":
        if ir_a_la_caja(carrito):
            ejecutando = False
    else:
        print(f"{ROJO}Opción no válida. Intente de nuevo.{RESET}")