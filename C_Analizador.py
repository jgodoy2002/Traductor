# C_Analizador.py

class TablaSimbolosC:
    def __init__(self):
        self.funciones = {}
        self.variables = {}
        self.errors = []

    def declarar_funcion(self, nombre, tipo, params):
        if nombre in self.funciones:
            self.errors.append(f"Función '{nombre}' ya fue declarada.")
        else:
            self.funciones[nombre] = {
                'tipo': tipo,
                'params': params
            }

    def declarar_variable(self, nombre, tipo):
        if nombre in self.variables:
            self.errors.append(f"Variable '{nombre}' ya fue declarada.")
        else:
            self.variables[nombre] = tipo

    def usar_variable(self, nombre):
        if nombre not in self.variables:
            self.errors.append(f"Variable '{nombre}' usada sin declarar.")

    def reset_variables(self):
        self.variables = {}  # Limpiar variables al iniciar función


class AnalizadorSemanticoC:
    def __init__(self):
        self.tabla = TablaSimbolosC()

    def analizar(self, ast):
        for nodo in ast:
            if nodo[0] == 'function':
                self.analizar_funcion(nodo)

    def analizar_funcion(self, nodo):
        _, tipo, nombre, params, cuerpo = nodo
        self.tabla.declarar_funcion(nombre, tipo, params)
        self.tabla.reset_variables()

        for tipo_param, nombre_param in params:
            self.tabla.declarar_variable(nombre_param, tipo_param)

        for sentencia in cuerpo:
            self.analizar_sentencia(sentencia)

    def analizar_sentencia(self, stmt):
        if stmt[0] == 'var_decl':
            _, tipo, nombre, valor = stmt
            self.tabla.declarar_variable(nombre, tipo)
        elif stmt[0] == 'return':
            _, valor = stmt
            # Puedes extender con validación de tipo de retorno
        else:
            self.tabla.errors.append(f"Sentencia no reconocida: {stmt}")
