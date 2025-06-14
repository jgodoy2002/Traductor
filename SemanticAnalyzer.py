class SymbolTable:
    def __init__(self):
        self.functions = {
            'suma': {'params': ['x', 'y'], 'type': 'function'},
            'resta': {'params': ['x', 'y'], 'type': 'function'},
            'multiplicacion': {'params': ['x', 'y'], 'type': 'function'},
            'division': {'params': ['x', 'y'], 'type': 'function'},
            }  # nombre -> {'params': [...], 'type': 'func'}
        self.globals = {}    # variables globales
        self.errors = []

    def declare_function(self, name, params):
        if name in self.functions:
            self.errors.append(f"Redefinición de función '{name}'")
        else:
            self.functions[name] = {
                'params': params,
                'type': 'function'
            }

    def is_function(self, name):
        return name in self.functions

    def get_function_params(self, name):
        return self.functions[name]['params'] if name in self.functions else None

    def declare_variable(self, name, scope):
        if name in scope:
            self.errors.append(f"Variable redeclarada en el mismo ámbito: '{name}'")
        else:
            scope[name] = {'type': 'var'}

    def check_variable(self, name, scope):
        if name not in scope and name not in self.globals:
            self.errors.append(f"Uso de variable no declarada: '{name}'")

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = SymbolTable()

    def analyze(self, ast):
        for node in ast:
            if node[0] == 'function_def':
                self.analyze_function_def(node)
            else:
                self.check_expression(node, self.symbol_table.globals)

    def analyze_function_def(self, node):
        _, name, params, expr = node
        self.symbol_table.declare_function(name, params)
        local_scope = {param: {'type': 'param'} for param in params}
        self.check_expression(expr, local_scope)

    def check_expression(self, expr, scope):
        if expr[0] in ('int', 'bool'):
            return expr[0]

        elif expr[0] == 'id':
            var_name = expr[1]
            self.symbol_table.check_variable(var_name, scope)
            return 'unknown'

        elif expr[0] == 'call':
            func_expr, args = expr[1], expr[2]
            if func_expr[0] != 'id':
                self.symbol_table.errors.append("Llamada a función inválida")
                return
            func_name = func_expr[1]
            if not self.symbol_table.is_function(func_name):
                self.symbol_table.errors.append(f"Función no definida: '{func_name}'")
                return
            expected = self.symbol_table.get_function_params(func_name)
            if len(args) != len(expected):
                self.symbol_table.errors.append(f"Número incorrecto de argumentos en llamada a '{func_name}'")
            for arg in args:
                self.check_expression(arg, scope)
            return 'unknown'

        elif expr[0] == 'if':
            cond = self.check_expression(expr[1], scope)
            then_branch = self.check_expression(expr[2], scope)
            else_branch = self.check_expression(expr[3], scope)
            return 'unknown'

        elif expr[0] == 'lambda':
            params, body = expr[1], expr[2]
            lambda_scope = {param: {'type': 'param'} for param in params}
            self.check_expression(body, lambda_scope)
            return 'func'

        elif expr[0] in ('plus', 'minus', 'mul', 'morethan', 'lessthan', 'eq'):
            left = self.check_expression(expr[1], scope)
            right = self.check_expression(expr[2], scope)
            return 'int'  # asumiendo operaciones enteras

        else:
            self.symbol_table.errors.append(f"Expresión no reconocida: {expr}")

analizador_semantico = SemanticAnalyzer()