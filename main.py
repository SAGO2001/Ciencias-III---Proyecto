import ply.lex as lex

resul_lexema = []

reservada = (

    'RETURN','INT','IF'
)
tokens = reservada + (
    'IDENTIFICADOR', 'ENTERO','ASIGNAR','SUMA','RESTA','MULT','DIV','POTENCIA','MODULO',

    #Condiciones
    'SI','SINO',
    #Ciclos
    'MIENTRAS','PARA',
    #Lógico
    'AND','OR','NOT','MENORQUE','MENORIGUAL','MAYORQUE','MAYORIGUAL','IGUAL','DISTINTO',
    #Simbolos
    'NUMERAL',

    'PRIZQ','PARDER','CORIZQ','CORDER','LLAIZQ','LLADER',

    #Otros
    'PUNTOCOMA','COMA','COMDOB',
    'MAYORDER', # >>
    'MAYORIZQ', # <<
)
# Reglas de Expresiones Regulares para token
t_SUMA = r'\+'
t_RESTA = r'-'
#t_MINUSMINUS = r'\-\-'
t_MULT = r'\*'
t_DIV = r'/'
t_MODULO = r'\%'
t_POTENCIA = r'(\*{2} | \^)'

t_ASIGNAR = r'='
# Expresiones Lógicas
t_AND = r'\&\&'
t_OR = r'\|{2}'
t_NOT = r'\!'
t_MENORQUE = r'<'
#t_MAYORQUE = r'>'
t_PUNTOCOMA = r';'
t_COMA = r','
#t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAIZQ = r'\{'
t_LLADER = r'\}'
t_COMDOB = r'\"'

def t_RETURN(t):
    r'include'
    return t

def t_INT(t):
    r'int'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_SI(t):
    r'if'
    return t

def t_MIENTRAS(t):
    r'while'
    return t

def t_PARA(t):
    r'for'
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NUMERAL(t):
    r'\#'
    return t

def t_PLUSPLUS(t):
    r'\+\+'
    return t

def t_MENORIGUAL(t):
    r'<='
    return t

def t_MAYORIGUAL(t):
    r'>='
    return t

def t_IGUAL(t):
    r'=='
    return t

def t_comments_ONELine(t):
    r'\/\/(.)*\n'
    t.lexer.lineno += 1
    print("Comentario de una linea")

t_ignore = ' \t'

def t_error(t):
    global resul_lexema
    estado = "** Token no valido en la linea {:4} valor {:16} Posicion {:4}".format(str(t.lineno), str(t.value),
                                                                                    str(t.lexpos))
    resul_lexema.append(estado)
    t.lexer.skip(1)

# Prueba de ingreso
def prueba(data):
    global resul_lexema

    analizador = lex.lex()
    analizador.input(data)

    resul_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break

        estado = "Linea {:4} Tipo {:16} Valor {:4}".format(str(tok.lineno), str(tok.type),
                                                           str(tok.value), str(tok.lexpos))
        resul_lexema.append(estado)
    return resul_lexema

# Instanciamos el analizador lexico
analizador = lex.lex()

if __name__ == '__main__':
    while True:
        data = input("Ingrese: ")
        prueba(data)
        print(resul_lexema)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
