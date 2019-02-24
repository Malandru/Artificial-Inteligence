class Word(object):
    def __init__(self, word=str): #constructor
        self.word = word #string
        self.next = [] #(object Word, times) list
        self.times = []
        self.bucle_flag = False
    
    def push_back(self, x):
        for elem in self.next:
            if elem.word == x.word: #Si el elemento ya esta en la lista de siguientes
                index = self.next.index(elem)
                self.times[index] += 1
                break
        else:
            self.next.append(x)
            self.times.append(1)

    def prints(self):
        print '==', self.word, '==', self.bucle_flag
        for index in range(len(self.next)):
            print '-->', self.next[index].word,

def imprimir(x, lista):
    if lista == []:
        for elem in x:
            elem.prints()
        print '\n***************'
    else:
        for elem in lista:
            if elem in x:
                imprimir(x, [])
                continue
            x.append(elem)
            imprimir(x, elem.next)
            x.pop()

def insert(x, wanted):
    wanted.push_back(x)

def find(x, lista, heads):
    for elem in lista:
        if elem.word == x.word:
            return elem
        if elem in heads:
            continue
        if elem.bucle_flag == True:
            heads.append(elem)
        obj = find(x, elem.next, heads)
        if obj != None:
            return obj
    return None