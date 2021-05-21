import re

calles = {'AC', 'Avenida calle', 'AD', 'Administración', 'ADL', 'Adelante', 'AER', 'Aeropuerto', 'AG', 'Agencia', 'AGP',
          'Agrupación', 'AK', 'Avenida carrera', 'AL', 'Altillo', 'ALD', 'Al lado', 'ALM', 'Almacén', 'AP',
          'Apartamento', 'APTDO',
          'Apartado', 'ATR', 'Atrás', 'AUT', 'Autopista', 'AV', 'Avenida', 'AVIAL', 'Anillo vial', 'BG', 'Bodega', 'BL',
          'Bloque',
          'BLV', 'Boulevard', 'BRR', 'Barrio', 'C', 'Corregimiento', 'CA', 'Casa', 'CAS', 'Caserío', 'CC',
          'Centro comercial', 'CD',
          'Ciudadela', 'CEL', 'Célula', 'CEN', 'Centro', 'CIR', 'Circular', 'CL', 'Calle', 'CLJ', 'Callejón', 'CN',
          'Camino', 'CON',
          'Conjunto residencial', 'CONJ', 'Conjunto', 'CR', 'Carrera', 'CRT', 'Carretera', 'CRV', 'Circunvalar', 'CS',
          'Consultorio', 'DG', 'Diagonal', 'DP', 'Depósito', 'DPTO', 'Departamento', 'DS', 'Depósito sótano', 'ED',
          'Edificio',
          'EN', 'Entrada', 'ES', 'Escalera', 'ESQ', 'Esquina', 'ESTE', 'Este', 'ET', 'Etapa', 'EX', 'Exterior', 'FCA',
          'Finca', 'GJ',
          'Garaje', 'GS', 'Garaje sótano', 'GT', 'Glorieta', 'HC', 'Hacienda', 'HG', 'Hangar', 'IN', 'Interior', 'IP',
          'Inspección de Policía', 'IPD', 'Inspección Departamental', 'IPM', 'Inspección Municipal', 'KM', 'Kilómetro',
          'LC',
          'Local', 'LM', 'Local mezzanine', 'LT', 'Lote', 'MD', 'Módulo', 'MJ', 'Mojón', 'MLL', 'Muelle', 'MN',
          'Mezzanine', 'MZ',
          'Manzana', 'NOMBRE VIA', 'Vías de nombre común', 'NORTE', 'Norte', 'O', 'Oriente', 'OCC', 'Occidente',
          'OESTE', 'Oeste',
          'OF', 'Oficina', 'P', 'Piso', 'PA', 'Parcela', 'PAR', 'Parque', 'PD', 'Predio', 'PH', 'Penthouse', 'PJ',
          'Pasaje', 'PL',
          'Planta', 'PN', 'Puente', 'POR', 'Portería', 'POS', 'Poste', 'PQ', 'Parqueadero', 'PRJ', 'Paraje', 'PS',
          'Paseo', 'PT',
          'Puesto', 'PW', 'Park Way', 'RP', 'Round Point', 'SA', 'Salón', 'SC', 'Salón comunal', 'SD', 'Salida', 'SEC',
          'Sector',
          'SL', 'Solar', 'SM', 'Súper manzana', 'SS', 'Semisótano', 'ST', 'Sótano', 'SUITE', 'Suite', 'SUR', 'Sur',
          'TER', 'Terminal',
          'TERPLN', 'Terraplén', 'TO', 'Torre', 'TV', 'Transversal', 'TZ', 'Terraza', 'UN', 'Unidad', 'UR',
          'Unidad residencial',
          'URB', 'Urbanización', 'VRD', 'Vereda', 'VTE', 'Variante', 'ZF', 'Zona franca', 'ZN', 'Zona'}
postales = {'05', '08', '11', '13', '15', '17', '18', '19', '20', '23', '25', '27', '41', '44', '47', '50',
            '52', '54', '63', '66', '68', '70', '73', '76', '81', '85', '86', '88', '91', '94', '97', '99'}

#dat = 'avenida 17 # 24 - 34'
direcciones = re.compile(r'\s(\d){1,3}([a-g])?(\sbis)?(\s[a-g])?(\s(norte|sur|este|oeste))?\s#\s(\d){1,3}(\s[a-g])?\s'
                         r'-\s(\d){1,3}(\s(norte|sur|este|oeste))?', re.IGNORECASE)


# Compuesto por letras entre 3 y 15 digitos por cada nombre
# La persona puede tener minimo un nombre o dos nombres como maximo
nombres = re.compile(r'^[A-Z][a-z]{2,15}(\s[A-Z][a-z]{2,15})?$')

# Compuesto por letras entre 3 y 15 digitos por cada apellido
# La persona debe tener uno o dos apellidos
apellidos = re.compile(r'^[A-Z][a-z]{2,15}(\s[A-Z][a-z]{2,15})?$')

# Nombre de usuario (compuesto por numeros, letras y punto) de 6 a 30 caracteres
# @ "pertenece a", nombre del dominio
#email = re.compile(r'^\w(\w|.\w){5,29}@\w(\w|(.\w)){2,15}.(\w){2,15}$', re.IGNORECASE)

#Una implementación del Estandard Official: RFC 5322:
#( valida en el 99.99% de los emails existentes )
email = re.compile(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*"
                   r"@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")

# El formato de los numeros telefonicos en colombia esta compuesto por 10 numeros
# En la actualidad todos los numeros asignados inician con 3.
celular = re.compile(r'^3\d{9}$')

# El formato internacional definido por ISO (IS0 8601) para fechas es yyyy/mm/dd
# Tambien se acepta yyyy-mm-dd, yyyy mm dd, dd/mm/yyyy, dd-mm-yyyy, dd mm yyyy, dd de mmm de yyyy.
date = re.compile(
    r'(^((19|20)\d\d)(/|-|\s)(0?[1-9]|1[012])(/|-|\s)(0?[1-9]|[12][0-9]|3[01])$)|'
    r'(^(0?[1-9]|[12][0-9]|3[01])(/|-|\s)(0?[1-9]|1[012])(/|-|\s)((19|20)\d\d)$)|'
    r'(^(0?[1-9]|[12][0-9]|3[01])\s(de\s)?(ene|feb|mar|abr|may|jun|jul|ago|sep|nov|dic)\s(de\s)?((19|20)\d\d)$)'
    , re.IGNORECASE)

# Es un código de 6 dígitos que complementa tu dirección física
# y representa una zona en el mapa de nuestro país.
postal = re.compile(r'\d{4}')

# Los números locales siguen el patrón: NXX-XXXX
# Donde N son números del 2 al 8. Los números donde N es 9 están reservados para teléfonos públicos
# y  X es cualquier número del 0 al 9.
telFijo = re.compile(r'^[2-8](\d){6}$')

def ingresoDireccion(data):
    for d in calles:
        if data.split()[0].lower() == d.lower():
            return re.search(direcciones, data)
    return None


def ingresoPostal(data):
    for d in postales:
        if (data[0] == d[0]) and (data[1] == d[1]):
            return re.search(postal, data)
    return None


while True:
    print("Sistema de ingreso de datos")
    print("-- Bienvenido --")
    while nombres.match(input("Ingrese sus nombres: ")) is None:
        print("- - -Nombres invalidos- - -")
    while apellidos.match(input("Ingrese sus apellidos: ")) is None:
        print("- - -Apellidos invalidos- - -")
    while ingresoDireccion(input("Ingrese la dirección: ")) is None:
        print("- - -Dirección invalida- - -")
    while email.match(input("Ingrese su correo electronico: ")) is None:
        print("- - -Dirección de correo invalida- - -")
    while date.match(input("Ingrese su fecha de nacimiento: ")) is None:
        print("- - -Fecha invalida- - -")
    while celular.match(input("Ingrese su celular: ")) is None:
        print("- - -Celular invalido- - -")
    while telFijo.match(input("Ingrese tel fijo: ")) is None:
        print("- - -Telefono fijo invalido- - -")
    while ingresoPostal(input("Ingrese su codigo postal: ")) is None:
        print("- - -Codigo postal invalido- - -")
    print("----------------------------------------------------------")
    print("--------------------INGRESO CORRECTO----------------------")
    print("----------------------------------------------------------\n")