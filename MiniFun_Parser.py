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
        if kind == expected_kind:
            self.pos += 1
            return value
        else:
            raise Exception(f"Error de sintaxis: esperaba {expected_kind} pero encontró {kind}")

    def parse(self):
        functions = []
        while self.current_token()[0] != 'EOF':
            if self.current_token()[0] == 'DEF':
                functions.append(self.parse_function_def())
            if self.current_token()[0] == 'FUN':
                functions.append(self.parse_expression())
        return functions
    
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
        if self.current_token()[0] == 'ID':
            parameters.append(self.next_token('ID'))
            while self.current_token()[0] == 'COMMA':
                self.next_token('COMMA')
                parameters.append(self.next_token('ID'))
        return parameters
    
    def parse_expression(self):
        if self.current_token()[0] == 'FUN':
            return self.parse_lambda()

        if self.current_token()[0] == 'IF':
            self.next_token('IF')
            condicion = self.parse_expression()
            self.next_token('THEN')
            entonces = self.parse_expression()
            self.next_token('ELSE')
            sino = self.parse_expression()
            return ('if', condicion, entonces, sino)
        
        left = self.parse_literal()
        if(self.current_token()[0] == 'LPAREN'):
            self.next_token('LPAREN')
            right = self.parse_params()
            self.next_token('RPAREN')
            return ('call', left, right)
        while self.current_token()[0] in ('PLUS', 'MINUS', 'MUL', 'MORETHAN', 'LESSTHAN', 'EQ'):
            op_kind, _ = self.current_token()
            self.next_token(op_kind)
            right = self.parse_literal()
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

        
        
