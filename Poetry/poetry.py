from Word import Word, imprimir, find, insert
from Text import Text
from random import randint

grafo = Word(' ')
words = []
text = Text('input.txt')
generated = ''

def read_text():
    global grafo
    word = text.get_word()
    words.append(word)
    grafo = Word(word)
    first = grafo
    while text.EOF == False:
        word = text.get_word()
        secnd = Word(word) #hay que encontrarlo
        obj = find(secnd, [grafo], [])
        if obj == None: #El objeto es nuevo (no se encontro)
            words.append(word)
        else:
            secnd = obj
            secnd.bucle_flag = True
        insert(secnd, first)
        first = secnd

def get_array(next, times):
    x = []
    for index in range(len(next)):
        x += [next[index] for i in range(times[index])]
    return x

def compose(ini, times):
    global generated
    p = get_array(ini.next, ini.times)
    x = randint(0, len(p) - 1)
    word = p[x].word
    if word == ',' or word == '.':
        generated += word
    else:
        generated += ' ' + word
    if times > 0:
        compose(p[x], times - 1)
    else:
        print generated

# maggio1993
read_text()
point = Word('.')
ini = find(point, [grafo], [])
compose(ini, 100)
#imprimir([grafo], grafo.next)