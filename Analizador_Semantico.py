class Tabla_Simbolos:
    def __init__(self):
        self.functions = {
            'suma': {'params': ['x', 'y'], 'type': 'function'},
            'resta': {'params': ['x', 'y'], 'type': 'function'},
            'multiplicacion': {'params': ['x', 'y'], 'type': 'function'},
            'division': {'params': ['x', 'y'], 'type': 'function'},
            } 
        self.globals = {} 
        self.errors = []

    def declare_function(self, name, params):
        if name in self.functions:
            self.errors.append(f"Redefinición de función '{name}'")
        else:
            self.functions[name] = {'params': params, 'type': 'function'}

    def is_function(self, name):
        return name in self.functions

    def get_function_params(self, name):
        return self.functions.get(name, {}).get('params', [])

    def check_variable(self, name, scope):
        if name not in scope and name not in self.globals:
            self.errors.append(f"Uso de variable no declarada: '{name}'")

class Analizador_Semantico:
    def __init__(self):
        self.simbolos_tabla = Tabla_Simbolos()

    def analyze(self, ast):
        for node in ast:
            if node[0] == 'function_def':
                self.analizar_funcion(node)
            else:
                self.analizar_expr(node, self.simbolos_tabla.globals)

    def analizar_funcion(self, node):
        _, nombre, parametros, cuerpo = node
        self.simbolos_tabla.declare_function(nombre, parametros)

        ambito_local = {param: {'type': 'param'} for param in parametros}
        self.analizar_expr(cuerpo, ambito_local)

    def analizar_expr(self, expr, scope):
        tipo = expr[0]

        if tipo in ('int', 'bool'):
            return tipo

        elif tipo == 'id':
            nombre = expr[1]
            self.simbolos_tabla.check_variable(nombre, scope)
            return 'unknown'

        elif tipo == 'call':
            funcion = expr[1]
            argumentos = expr[2]

            if funcion[0] != 'id':
                self.simbolos_tabla.errors.append("Llamada a función inválida")
                return

            nombre_func = funcion[1]
            if not self.simbolos_tabla.is_function(nombre_func):
                self.simbolos_tabla.errors.append(f"Función no definida: '{nombre_func}'")
                return

            esperados = self.simbolos_tabla.get_function_params(nombre_func)
            if len(argumentos) != len(esperados):
                self.simbolos_tabla.errors.append(f"Argumentos incorrectos en llamada a '{nombre_func}'")

            for arg in argumentos:
                self.analizar_expr(arg, scope)
            return 'unknown'

        elif tipo == 'if':
            _, condicion, caso_si, caso_no = expr
            self.analizar_expr(condicion, scope)
            self.analizar_expr(caso_si, scope)
            self.analizar_expr(caso_no, scope)
            return 'unknown'

        elif tipo == 'lambda':
            _, parametros, cuerpo = expr
            ambito_lambda = {p: {'type': 'param'} for p in parametros}
            self.analizar_expr(cuerpo, ambito_lambda)
            return 'func'

        elif tipo in ('plus', 'minus', 'mul', 'morethan', 'lessthan', 'eq'):
            self.analizar_expr(expr[1], scope)
            self.analizar_expr(expr[2], scope)

        elif expr[0] in ('plus', 'minus', 'mul', 'morethan', 'lessthan', 'eq'):
            left = self.check_expression(expr[1], scope)
            right = self.check_expression(expr[2], scope)
            return 'int' 
        
        elif expr[0] == 'map':
            _, lista_expr, lambda_expr = expr
            self.check_expression(lista_expr, scope)
            lambda_type = self.check_expression(lambda_expr, scope)
            if lambda_type != 'func':
                self.simbolos_tabla.errors.append("Segundo argumento de 'map' debe ser una función lambda")
            return 'list'

        elif expr[0] == 'filter':
            _, lista_expr, lambda_expr = expr
            self.check_expression(lista_expr, scope)
            lambda_type = self.check_expression(lambda_expr, scope)
            if lambda_type != 'func':
                self.simbolos_tabla.errors.append("Segundo argumento de 'filter' debe ser una función lambda")
            return 'list'

        elif expr[0] == 'reduce':
            _, lista_expr, lambda_expr = expr
            self.check_expression(lista_expr, scope)
            lambda_type = self.check_expression(lambda_expr, scope)
            if lambda_type != 'func':
                self.simbolos_tabla.errors.append("Segundo argumento de 'reduce' debe ser una función lambda")
            return 'int'

        else:
            self.simbolos_tabla.errors.append(f"Expresión no reconocida: {expr}")

analizador_semantico = Analizador_Semantico