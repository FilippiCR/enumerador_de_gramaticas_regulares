def generar_variables_infinitas(n):
    """
    Genera `n` variables no terminales comenzando por 'S', luego 'A'-'Z' (excepto 'S'),
    y luego 'A1'-'Z1', 'A2'-'Z2', etc., si es necesario.
    """
    variables = ['S']
    letras = [chr(i) for i in range(65, 91) if chr(i) != 'S']
    contador = 0
    while len(variables) < n:
        for letra in letras:
            nombre = letra if contador == 0 else f"{letra}{contador}"
            variables.append(nombre)
            if len(variables) == n:
                break
        contador += 1
    return variables


def calcular_total_gramaticas_por_variables(variables_count, terminales_count):
    """
    Calcula cuántas reglas posibles y cuántas gramáticas distintas se pueden formar
    con `variables_count` variables y `terminales_count` símbolos terminales.
    """
    v = variables_count
    t = terminales_count
    total_reglas = v * (t + t * v)  # v*(t reglas tipo v→t + t*v reglas tipo v→tv2)
    total_gramaticas = 2 ** total_reglas
    return total_reglas, total_gramaticas


def encontrar_grupo_variables_para_n(n, terminales_count):
    """
    Dado un número n, encuentra la cantidad mínima de variables necesarias
    para que la gramática número n pertenezca al conjunto con esas variables.
    """
    n_actual = 0
    v = 1
    while True:
        reglas, total = calcular_total_gramaticas_por_variables(v, terminales_count)
        if n < n_actual + total:
            n_local = n - n_actual
            return v, n_local
        n_actual += total
        v += 1


def generar_reglas_posibles(variables, terminales):
    """
    Genera todas las reglas posibles de una gramática regular (sin ε),
    con formato: V → t y V → tV.
    """
    reglas = []
    for v in variables:
        for t in terminales:
            reglas.append(f"{v} → {t}")
            for v2 in variables:
                reglas.append(f"{v} → {t}{v2}")
    return reglas


def n_a_seleccion(n, total_reglas):
    """
    Convierte el número n en binario y devuelve los índices de las reglas activadas (bits en 1).
    """
    binario = bin(n)[2:].zfill(total_reglas)
    return [i for i, bit in enumerate(binario[::-1]) if bit == '1']


def generar_gramatica_enumerada(n, terminales=None):
    """
    Genera la gramática número `n`, ajustando automáticamente la cantidad de variables
    necesarias. El alfabeto terminal puede personalizarse (por defecto: ['a', 'b', 'c']).
    """
    if terminales is None:
        terminales = ['a', 'b', 'c']

    v, n_local = encontrar_grupo_variables_para_n(n, len(terminales))
    variables = generar_variables_infinitas(v)
    reglas_posibles = generar_reglas_posibles(variables, terminales)
    total_reglas = len(reglas_posibles)

    seleccionadas_idx = n_a_seleccion(n_local, total_reglas)
    reglas_seleccionadas = [reglas_posibles[i] for i in seleccionadas_idx]

    return {
        'n': n,
        'VariablesUsadas': v,
        'Variables': variables,
        'Terminales': terminales,
        'Inicial': 'S',
        'Producciones': reglas_seleccionadas,
        'TotalReglas': total_reglas,
        'SeleccionadasIdx': seleccionadas_idx
    }
