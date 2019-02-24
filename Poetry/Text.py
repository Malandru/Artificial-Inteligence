class Text:
    global poem
    def __init__(self, file):
        self.index = 0
        self.poem = open(file)
        self.EOF = False
    def get_word(self):
        word = ''
        while True:
            char = self.poem.read(1)
            self.index += 1
            if self.is_blank(char):
                continue
            if word != '' and (char == ',' or char == '.'):
                self.index -= 1
                self.poem.seek(self.index)
                break
            word += char
            if self.other_word():
                break
        return word

    def is_sign(slef, char):
        return
        {
            '.'
        }

    def read_text(self):
        while self.EOF == False:
            print self.get_word()
        self.poem.close()

    def is_blank(self, char):
        blank = char == ' ' or char == '\n'
        self.EOF = char == ''
        return  blank or self.EOF
    
    def other_word(self):
        char = self.poem.read(1)
        self.poem.seek(self.index)
        return self.is_blank(char)