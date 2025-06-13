from MiniFun_Parser import Parser
from MiniFun_Lexer import lexer  

from SemanticAnalyzer import SemanticAnalyzer

def test_code(code):
    print(f'Código a analizar: {code}')
    tokens = lexer(code)
    parser = Parser(tokens)

    try:
        ast = parser.parse()
        print('Árbol de sintaxis abstracta (AST):')
        print(ast)

        analyzer = SemanticAnalyzer()
        analyzer.analyze(ast)

        print('Tabla de símbolos:')
        print(analyzer.symbol_table.functions)

        print('Errores encontrados:')
        if analyzer.symbol_table.errors:
            for error in analyzer.symbol_table.errors:
                print(f'  - {error}')
        else:
            print('No se encontraron errores semánticos.')
    except Exception as e:
        print(f'Error de análisis: {e}')

if __name__ == "__main__":
    # Pruebas
    code1 = "def suma(x, y) = x + y"
    code2 = "def max(a, b) = if a > b then a else b"
    code3 = "def apply(f, x) = f(x)"
    code4 = "fun(x, y) => x + y"  # función anónima

    test_code(code1)
    test_code(code2)
    test_code(code3)
    test_code(code4)
