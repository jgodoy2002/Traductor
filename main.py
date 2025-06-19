from MiniFun_Parser import Parser
from MiniFun_Lexer import lexer  
from Analizador_Semantico import Analizador_Semantico

def separador():
    print('=' * 50)

def imprimir_tabla(symbols):
    print("Tabla de símbolos:")
    for name, info in symbols.items():
        params = ', '.join(info['params']) if 'params' in info else ''
        tipo = info.get('type', 'desconocido')
        print(f"  - {name} ({tipo}) -> params: ({params})")

def imprimir_errores(errores):
    print("Errores encontrados:")
    if errores:
        for error in errores:
            print(f" X {error}")
    else:
        print(":) No se encontraron errores semánticos.")

def test_code(code):
    separador()
    print(f"Código a analizar:\n{code}\n")
    
    tokens = lexer(code)
    parser = Parser(tokens)

    try:
        ast = parser.parse()
        print("Árbol de Sintaxis Abstracta (AST):")
        for node in ast:
            print(f"  {node}")
        print()

        analizador = Analizador_Semantico()
        analizador.analyze(ast)

        imprimir_tabla(analizador.simbolos_tabla.functions)
        print()
        imprimir_errores(analizador.simbolos_tabla.errors)

    except Exception as e:
        print(f"Error de análisis: {e}")
    print()

if __name__ == "__main__":
    # Casos de prueba
    pruebas = [
        "def suma(x, y) = x + y",
        "def max(a, b) = if (a > b) then a else b",
        "def apply(f, x) = f(x)",
        "fun(x, y) => x + y",
    ]

    for code in pruebas:
        test_code(code)