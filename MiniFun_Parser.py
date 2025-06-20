class Parser:
    def __init__(self, tokens):
       self.tokens = tokens
       self.pos = 0

    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return ('EOF', '')
        
    def next_token(self, expected_kind):
        kind, value = self.current_token()
        print(kind, value)
        if kind == expected_kind:
            self.pos += 1
            return value
        else:
            raise Exception(f"Error de sintaxis: esperaba {expected_kind} pero encontró {kind}")

    def parse(self):
        result = []
        while self.current_token()[0] != 'EOF':
            if self.current_token()[0] == 'ENDLINE':
                self.next_token('ENDLINE')
                continue
            elif self.current_token()[0] == 'DEF':
                result.append(self.parse_function_def())
            elif self.current_token()[0] in ('FUN', 'MAP', 'FILTER', 'REDUCE', 'ID'):
                result.append(self.parse_expression())
            else:
                raise Exception(f"Token inesperado: {self.current_token()}")
            if self.current_token()[0] == 'ENDLINE':
                self.next_token(self.current_token()[0])
        return result

    
    def parse_function_def(self):
        self.next_token('DEF')
        function_name = self.next_token('ID')
        self.next_token('LPAREN')
        parameters = self.parse_params()
        self.next_token('RPAREN')
        self.next_token('ASSIGN')
        expression = self.parse_expression()
        return ('function_def', function_name, parameters, expression)

    def parse_params(self):
        parameters = []

        if self.current_token()[0] in ('VARINT', 'VARBOOL', 'VARFLOAT', 'ID'):
            parameters.append(self.parse_param())
            while self.current_token()[0] == 'COMMA':
                self.next_token('COMMA')
                parameters.append(self.parse_param())

        return parameters
    
    def parse_param(self):
        valid_types = ('VARINT', 'VARBOOL', 'VARFLOAT', 'ID') 

        kind_type, type_value = self.current_token()
        if kind_type not in valid_types:
            raise SyntaxError(f"Se esperaba un tipo (int, bool, float), se encontró: {type_value}")
        self.next_token(kind_type)

        if(kind_type == 'ID'):
            return (type_value, 'function')

        kind_id, param_name = self.current_token()
        if kind_id != 'ID':
            raise SyntaxError(f"Se esperaba un identificador después del tipo, se encontró: {param_name}")
        self.next_token('ID')

        return (param_name, type_value)
    
    def parse_expression(self):
        if self.current_token()[0] == 'FUN':
            return self.parse_lambda()
        if self.current_token()[0] == 'IF':
            return self.parse_if()
        
        if self.current_token()[0] == 'MAP':
            self.next_token('MAP')
            self.next_token("LPAREN")
            lista_expr = self.parse_expression()
            self.next_token("COMMA")
            lambda_expr = self.parse_expression()
            self.next_token("RPAREN")
            return ("map", lista_expr, lambda_expr) 
        
        if self.current_token()[0] == 'FILTER':
            self.next_token('FILTER')
            self.next_token("LPAREN")
            lista_expr = self.parse_expression()
            self.next_token("COMMA")
            lambda_expr = self.parse_expression()
            self.next_token("RPAREN")
            return ("filter", lista_expr, lambda_expr) 
        
        if self.current_token()[0] == 'REDUCE':
            self.next_token('REDUCE')
            self.next_token("LPAREN")
            lista_expr = self.parse_expression()
            self.next_token("COMMA")
            lambda_expr = self.parse_expression()
            self.next_token("RPAREN")
            return ("map", lista_expr, lambda_expr) 
        
        left = self.parse_literal()
        if(self.current_token()[0] == 'LPAREN'):
            self.next_token('LPAREN')
            right = self.parse_arguments()
            self.next_token('RPAREN')
            return ('call', left, right)
        while self.current_token()[0] in ('PLUS', 'MINUS', 'MUL', 'DIV', 'MORETHAN', 'LESSTHAN', 'EQ'):
            op_kind, _ = self.current_token()
            self.next_token(op_kind)
            right = self.parse_expression()
            left = (op_kind.lower(), left, right)
        return left
        
    def parse_literal(self):
        kind, value = self.current_token()
        if kind == 'INT':
            self.next_token('INT')
            return ('int', int(value))
        elif kind == 'ID':
            self.next_token('ID')
            return ('id', value)
        elif kind == 'FLOAT':
            self.next_token('FLOAT')
            return ('float', value)
        elif kind == 'TRUE':
            self.next_token('TRUE')
            return ('bool', True)
        elif kind == 'FALSE':
            self.next_token('FALSE')
            return ('bool', False)
        elif kind == 'LPAREN' :
            self.next_token('LPAREN')
            expr = self.parse_expression()
            self.next_token('RPAREN')
            return expr
        elif kind == 'LBRACK':
            self.next_token('LBRACK')
            elements = []
            if self.current_token()[0] != 'RBRACK':  
                elements.append(self.parse_expression())
                while self.current_token()[0] == 'COMMA':
                    self.next_token('COMMA')
                    elements.append(self.parse_expression())
            self.next_token('RBRACK') 
            return ('list', elements)
        else:
            raise Exception(f"Error de sintaxis: expresión inesperada {kind}")
        
        
    def parse_lambda(self):
        if self.current_token()[0] == 'FUN':
            self.next_token('FUN')
            self.next_token('LPAREN')
            parameters = self.parse_params()
            self.next_token('RPAREN')
            self.next_token('ARROW')
            expression = self.parse_expression()
            return ('lambda', parameters, expression)
        
    def parse_arguments(self):
        args = []
        if self.current_token()[0] != 'RPAREN':
            args.append(self.parse_expression())
            while self.current_token()[0] == 'COMMA':
                self.next_token('COMMA')
                args.append(self.parse_expression())
        return args
    
    def parse_if(self):
        self.next_token('IF')
        condicion = self.parse_expression()
        self.next_token('THEN')
        entonces = self.parse_expression()
        self.next_token('ELSE')
        sino = self.parse_expression()
        return ('if', condicion, entonces, sino)

        
    #def parse_variables(self):
    #    if self.current_token()[0] in ('VARINT', 'VARBOOL', 'VARFLOAT'):
    #        tipo = self.next_token(self.current_token()[0])
    #        var_name = self.next_token('ID')
    #        self.next_token('ASSIGN')
    #        expression = self.parse_expression()
    #        return ('variable', var_name, tipo, expression)
        

