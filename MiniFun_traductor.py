def traducir_a_minic(ast, archivo_salida):
    codigo = ""

    for nodo in ast:
        tipo = nodo[0]
        if tipo == 'function_def':
            _, nombre, parametros, cuerpo = nodo
            params_str = ", ".join(f"int {nombre}" for nombre, _ in parametros) 

            if cuerpo[0] == 'if':
                tipo_retorno, cuerpo_str = traducir_if(cuerpo, nombre_funcion=nombre, parametros=parametros)
            elif cuerpo[0] == 'map':
                tipo_retorno = "List"
                cuerpo_str = traducir_map(cuerpo)
            elif cuerpo[0] == 'filter':
                tipo_retorno = "List"
                cuerpo_str = traducir_filter(cuerpo)
            elif cuerpo[0] == 'reduce':
                cuerpo_str = traducir_reduce(cuerpo)
            elif cuerpo[0] == 'call':
                codigo += f"{tipo_retorno} {nombre}({params_str}) {{\n"
                codigo += f"    int resultado = {traducir_expr(cuerpo)};\n"
                codigo += f"    return resultado;\n"
                codigo += "}\n\n"
            else:
                tipo_retorno = "int"
                cuerpo_str = traducir_expr(cuerpo)
            codigo += f"{tipo_retorno} {nombre}({params_str}) {{\n    return {cuerpo_str};\n}}\n\n"
        else:
            raise Exception(f"Traducción no implementada para {tipo}")

    with open(archivo_salida, "w") as f:
        f.write(codigo)

def traducir_expr(expr):
    tipo = expr[0]

    if tipo == 'int':
        return str(expr[1])
    elif tipo == 'float':
        return str(expr[1])
    elif tipo == 'bool':
        return (bool,'true') if expr[1] else (bool,'false')
    elif tipo == 'id':
        return expr[1]
    elif tipo in ('plus', 'minus', 'mul', 'div', 'morethan', 'lessthan', 'eq'):
        op_map = {'plus': '+', 'minus': '-', 'mul': '*', 'div': '/', 'morethan': '>', 'lessthan': '<', 'eq': '=='}
        return f"({traducir_expr(expr[1])} {op_map[tipo]} {traducir_expr(expr[2])})"
    elif tipo == 'call':
        _, funcion, args = expr
        args_str = ", ".join(traducir_expr(arg) for arg in args)
        return f"{traducir_expr(funcion)}({args_str})"
    elif tipo == "list":
        elementos = expr[1]
        valores = ", ".join(traducir_expr(e) for e in elementos)
        return f"int[{valores}]"
    else:
        raise Exception(f"Expresión no reconocida: {tipo}")
    
def traducir_if(expr, nombre_funcion=None, parametros=None):
    _, cond_expr, then_expr, else_expr = expr

    if (
        contiene_nombre_funcion(else_expr, nombre_funcion)
    ):
        var_names = [nombre for nombre, _ in parametros]
        new_args = else_expr[2]



        updates = [
            f"{var_names[i]} = {traducir_expr(new_args)};"
            for i in range(len(var_names))
        ]

        cond_str = traducir_expr(cond_expr)
        then_str = traducir_expr(then_expr)

        ret_var = "resultado"
        init_code = f"int {ret_var} = {then_str};"

        return (
            "int",
            f"""{init_code}
while (!({cond_str})) {{
    {' '.join(updates)}
}}
return {ret_var};"""
        )

    # Caso común (sin recursividad)
    cond_str = traducir_expr(cond_expr)
    then_str = traducir_expr(then_expr)
    else_str = traducir_expr(else_expr)

    tipo = "bool" if all(x[0] == 'bool' for x in [then_expr, else_expr]) else "int"
    return (tipo, f"({cond_str} ? {then_str} : {else_str})")

def traducir_map(expr):
    # expr = ("map", lista_expr, lambda_expr)
    _, lista_expr, lambda_expr = expr
    
    lista_c = traducir_expr(lista_expr)
    func_c = traducir_lambda(lambda_expr, nombre_funcion="map_func")
    
    codigo = f"""
int* map(int* arr, int size) {{
    int* resultado = malloc(size * sizeof(int));
    int i = 0;
    while (i < size) {{
        resultado[i] = map_func(arr[i]);
        i = i + 1;
    }}
    return resultado;
}}

{func_c}
"""
    return codigo

def traducir_filter(expr):
    _, lista_expr, lambda_expr = expr
    
    lista_c = traducir_expr(lista_expr)
    func_c = traducir_lambda(lambda_expr, nombre_funcion="filter_func")
    
    codigo = f"""
int* filter(int* arr, int size, int* result_size) {{
    int* resultado = malloc(size * sizeof(int));
    int i = 0;
    int j = 0;
    while (i < size) {{
        if (filter_func(arr[i])) {{
            resultado[j] = arr[i];
            j = j + 1;
        }}
        i = i + 1;
    }}
    *result_size = j;
    return resultado;
}}

{func_c}
"""
    return codigo

def traducir_reduce(expr):
    _, lista_expr, lambda_expr = expr

    lista_c = traducir_expr(lista_expr)
    func_c = traducir_lambda(lambda_expr, nombre_funcion="reduce_func")

    codigo = f"""
int reduce(int* arr, int size, int initial) {{
    int acumulador = initial;
    int i = 0;
    while (i < size) {{
        acumulador = reduce_func(acumulador, arr[i]);
        i = i + 1;
    }}
    return acumulador;
}}

{func_c}
"""
    return codigo

lambda_counter = 0  # Contador global para nombres únicos
funciones_guardadas = {}

def traducir_lambda(expr, nombre_funcion=None):
    global lambda_counter

    if expr[0] != 'lambda':
        raise Exception("No es una lambda")

    _, parametros, cuerpo = expr

    if nombre_funcion is None:
        nombre_funcion = f"lambda_func_{lambda_counter}"
        lambda_counter += 1

    params_str = ", ".join(f"int {nombre}" for nombre, _ in parametros)
    cuerpo_str = traducir_expr(cuerpo)

    codigo = f"int {nombre_funcion}({params_str}) {{\n    return {cuerpo_str};\n}}\n"

    return codigo
    
def contiene_nombre_funcion(expr, nombre_funcion):
    if isinstance(expr, tuple):
        for item in expr:
            if item == nombre_funcion:
                return True
            if isinstance(item, (tuple, list)) and contiene_nombre_funcion(item, nombre_funcion):
                return True
    elif isinstance(expr, list):
        for item in expr:
            if contiene_nombre_funcion(item, nombre_funcion):
                return True
    return False