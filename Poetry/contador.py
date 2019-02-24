from Text import Text

text = Text('test.txt')

words = []

while text.EOF == False:
    x = text.get_word()
    if x in words:
        continue
    words.append(x)