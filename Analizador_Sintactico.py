import ply.yacc as yacc
from Analizador_Lexico.py import tokens 
from Analizador_Lexico.py import analizador 

resultado_gramatica = []

precede = (
    ('right', 'ASSIGNAR'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULT', 'DIV'),
    ('right', 'UMINUS')
)

nombres = {}

def declaracion_asignar(t):
    "declaracion : IDENTIFICADOR"
    nombres[t[1]] = t[3]

def declaracion_expr(t):
    "declaracion : expresion"
    t[0] = t[1]

def operaciones(t):
    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]
    elif t[2] == '%':
        t[0] = t[1] % t[3]
    elif t[2] == '**':
        i = t[3]
        t[0] = t[3]
        while i > 1:
            t[0] *= t[1]
            i -= 1

def unimus(t):
    "expresion : RESTA"
    t[0] = -t[2]

def grupo(t):
    t[0] = t[2]

def expresiones_logicas(t):
    if t[2] == '<':
        t[0] = t[1] < t[3]
    elif t[2] == '>':
        t[0] = t[1] > t[3]
    elif t[2] == '<=':
        t[0] = t[1] <= t[3]
    elif t[2] == '>=':
        t[0] = t[1] >= t[3]
    elif t[2] == '==':
        t[0] = t[1] is t[3]
    elif t[3] == '<':
        t[0] = t[2] < t[4]
    elif t[3] == '>':
        t[0] = t[2] > t[4]
    elif t[3] == '<=':
        t[0] = t[2] <= t[4]
    elif t[3] == '>=':
        t[0] = t[2] >= t[4]
    elif t[3] == '==':
        t[0] = t[2] is t[4]

def expresion_booleana(t):
    if t[2] == '&&':
        t[0] = t[1] and t[3]
    elif t[2] == '||':
        t[0] = t[1] or t[3]
    elif t[2] == '!':
        t[0] =  t[1] is not t[3]
    elif t[3] == '&&':
        t[0] = t[2] and t[4]
    elif t[3] == '||':
        t[0] = t[2] or t[4]
    elif t[3] == '!':
        t[0] = t[2] is not t[4]

def numero(t):
    t[0] = t[1]

def cadena(t):
    t[0] = t[2]

def nombre(t):
    try:
        t[0] = nombres[t[1]]
    except LookupError:
        print("Nombre desconocido", t[1])
        t[0] = 0

def error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico de tipo {} en el valor {}".format(str(t.type), str(t.value))
        print(resultado)
    else:
        resultado = "Error sintactico {}".format(t)
        print(resultado)
    resultado_gramatica.append(resultado)

#Analizador
parser = yacc.yacc()

def prueba_sintactica(data):
    global resultado_gramatica
    resultado_gramatica.clear()

    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
        else:
            print("Data vacia")
    print("Result: ", resultado_gramatica)
    return resultado_gramatica

if __name__ == '__main__':
    while True:
        try:
            s = input('Ingresa dato ')
        except EOFError:
            continue
        if not s: 
            continue

        prueba_sintactica(s)
