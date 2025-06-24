from MiniFun_Parser import Parser
from MiniFun_Lexer import lexer  
from Analizador_Semantico import Analizador_Semantico
from MiniFun_traductor import traducir_a_minic

def separador():
    print('=' * 50)

def imprimir_tabla(symbols):
    print("Tabla de símbolos:")
    for name, info in symbols.items():
        params = ', '.join(f"{n}: {t}" for n, t in info['params']) if 'params' in info else ''
        tipo = info.get('type', 'desconocido')
        print(f"  - {name} ({tipo}) -> params: ({params})")

def imprimir_errores(errores):
    print("Errores encontrados:")
    if errores:
        for error in errores:
            print(f" X {error}")
    else:
        print(":) No se encontraron errores semánticos.")

def test_code(code, filename):
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
        astdebug = (
            'function_def',
            'mayorA2',
            [('x', 'int')],
            (
                'if',
                ('morethan', ('id', 'x'), ('int', 2)),
                ('bool', True),
                ('bool', False)
            )
        )
        traducir_a_minic(ast, filename)

    except Exception as e:
        print(f"Error de análisis: {e}")
    print()

if __name__ == "__main__":
    # Casos de prueba
    pruebas = """
    def f(float x) = x / 2
    
    def max(int a, int b) = if (a > b) then a else b
    def apply(f, float x) = f(x)
    def mayor_3(int x) = x > 3

    def make_list(int x, int y, int z) = [x, y, z]
    def empty_list() = []

    def prueba_map() = map([1, 2, 3], fun(int x) => x * 2)


    def factorial(int n) = if (n == 0) then 1 else n * factorial(n - 1)
    """
    """
        def prueba_filter() = filter([1, 2, 3, 4, 5], mayor_3)
    def prueba_reduce() = reduce([1, 2, 3, 4], suma)"""

    #    fun(int x, int y) => x + y
        
    test_code(pruebas, "Prueba.mc")