class Tabla_Simbolos:
    def __init__(self):
        self.functions = {
            'suma': {'params': [('x', 'int'), ('y', 'int')], 'type': 'function'},
            'resta': {'params': [('x', 'int'), ('y', 'int')], 'type': 'function'},
            'multiplicacion': {'params': [('x', 'int'), ('y', 'int')], 'type': 'function'},
            'division': {'params': [('x', 'int'), ('y', 'int')], 'type': 'function'},
            } 
        self.globals = {} 
        self.errors = []

    def declare_function(self, name, params):
        if name in self.functions:
            self.errors.append(f"Redefinición de función '{name}'")
        else:
            self.functions[name] = {'params': params, 'type': 'function'}

#    def declare_variable(self, name, tipo, scope):
#        if name in scope:
 #           self.errors.append(f"Variable '{name}' ya declarada en este ámbito")
 #       else:
  #          scope[name] = {'type': tipo}


    def is_function(self, name):
        return name in self.functions

    def get_function_params(self, name):
        return self.functions.get(name, {}).get('params', [])

    def check_variable(self, name, scope):
        if name in self.functions:
            return

        if name not in scope and name not in self.globals:
            self.errors.append(f"Uso de variable no declarada: '{name}'")

class Analizador_Semantico:
    def __init__(self):
        self.simbolos_tabla = Tabla_Simbolos()

    def analyze(self, ast):
        for node in ast:
            if node[0] == 'function_def':
                self.analizar_funcion(node)
            elif node[0] == 'variable':
                self.analizar_variable(node, self.simbolos_tabla.globals)
            else:
                self.analizar_expr(node, self.simbolos_tabla.globals)

    def analizar_funcion(self, node):
        _, nombre, parametros, cuerpo = node
        self.simbolos_tabla.declare_function(nombre, parametros)

        ambito_local = {nombre: {'type': tipo} for nombre, tipo in parametros}
        self.analizar_expr(cuerpo, ambito_local)

#    def analizar_variable(self, node, scope):
#        # Nodo variable: ('variable', nombre, tipo, expr)
#       _, nombre, tipo, expr = node
#
#        self.simbolos_tabla.declare_variable(nombre, tipo, scope)
#
#        self.analizar_expr(expr, scope)

    def analizar_expr(self, expr, scope):
        tipo = expr[0]

        if tipo in ('int', 'bool'):
            return tipo
        
        elif expr[0] == 'list':
            elementos = expr[1]
            tipos = []
            for e in elementos:
                tipo_elem = self.analizar_expr(e, scope)
                tipos.append(tipo_elem)
            
            tipos_unicos = set(tipos)
            if len(tipos_unicos) > 1:
                self.simbolos_tabla.errors.append("Lista heterogénea: todos los elementos deben ser del mismo tipo")
            
            return f"list<{tipos_unicos.pop()}>" if tipos_unicos else "list<empty>"

        elif tipo == 'id':
            nombre = expr[1]
            self.simbolos_tabla.check_variable(nombre, scope)
            return 'unknown'
        
#        elif tipo == 'variable':
#            self.analizar_variable(expr, scope)
#            return 'unknown'

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
            ambito_lambda = {nombre: {'type': tipo} for nombre, tipo in parametros}
            self.analizar_expr(cuerpo, ambito_lambda)
            return 'func'

        elif tipo in ('plus', 'minus', 'mul', 'div', 'morethan', 'lessthan', 'eq'):
            self.analizar_expr(expr[1], scope)
            self.analizar_expr(expr[2], scope)

        elif expr[0] in ('plus', 'minus', 'mul', 'div', 'morethan', 'lessthan', 'eq'):
            left = self.analizar_expr(expr[1], scope)
            right = self.analizar_expr(expr[2], scope)
            return 'int' 
        
        elif expr[0] == 'map':
            _, lista_expr, lambda_expr = expr
            tipo_lista = self.analizar_expr(lista_expr, scope)
            lambda_type = self.analizar_expr(lambda_expr, scope)

            if not tipo_lista.startswith('list'):
                self.simbolos_tabla.errors.append("Primer argumento de 'map' debe ser una lista")
            if not self.es_funcion_valida(lambda_expr):
                self.simbolos_tabla.errors.append("Segundo argumento de 'map' debe ser una función lambda o función válida")
            return tipo_lista  # map devuelve una lista

        elif expr[0] == 'filter':
            _, lista_expr, lambda_expr = expr
            tipo_lista = self.analizar_expr(lista_expr, scope)
            lambda_type = self.analizar_expr(lambda_expr, scope)

            if not tipo_lista.startswith('list'):
                self.simbolos_tabla.errors.append("Primer argumento de 'filter' debe ser una lista")
            if not self.es_funcion_valida(lambda_expr):
                self.simbolos_tabla.errors.append("Segundo argumento de 'filter' debe ser una función lambda o función válida")
            return tipo_lista  # filter devuelve una lista del mismo tipo

        elif expr[0] == 'reduce':
            _, lista_expr, lambda_expr = expr
            tipo_lista = self.analizar_expr(lista_expr, scope)
            lambda_type = self.analizar_expr(lambda_expr, scope)

            if not tipo_lista.startswith('list'):
                self.simbolos_tabla.errors.append("Primer argumento de 'reduce' debe ser una lista")
            if not self.es_funcion_valida(lambda_expr):
                self.simbolos_tabla.errors.append("Segundo argumento de 'reduce' debe ser una función lambda o función válida")
            return 'int'  # Suponemos que reduce devuelve un int (puedes ajustar esto)

        else:
            self.simbolos_tabla.errors.append(f"Expresión no reconocida: {expr}")

    def es_funcion_valida(self, expr):
        if expr[0] == 'lambda':
            return True
        elif expr[0] == 'id' and self.simbolos_tabla.is_function(expr[1]):
            return True
        return False

analizador_semantico = Analizador_Semantico