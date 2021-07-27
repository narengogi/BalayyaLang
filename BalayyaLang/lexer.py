from .grammar import Grammar as bp, Tokens as t
from .utils import Thappulu, err as e


class Token:
    def __init__(self, type, value):
        self.type = type    # I've overwritten the default method object here, perhaps I should change it later
        self.value = value

    def __repr__(self):
        return f'type: {self.type}, value: {self.value}'


class Lexer:
    def __init__(self, filename):
        self.inputContent = []
        self.filename = filename
        self.pos = 0
        self.current = ''
        self.currLine = ''
        self.tokens = []

    def makeNumber(self):
        numStr = ''
        dots = 0
        while self.current != None and (self.current.isdigit() or self.current in '.'):
            if self.current == '.':
                if dots == 1:
                    raise Thappulu(e.C101, e.info(self.currLine))
                dots += 1
                numStr += self.current
                self.advance()
            else:
                numStr += self.current
                self.advance()
        return Token(t.NUM, numStr)

    def makeText(self):
        textStr = ''
        while self.current != None and self.current.isalpha():
            textStr += self.current
            self.advance()
        return textStr

    def genTextToken(self, word):
        if bp.PLUS.search(word):
            return Token(t.PLUS, '+')
        elif word == 'teesey':
            return Token(t.MINUS, '-')
        elif word == 'guninchu':
            return Token(t.MULTIPLY, '*')
        elif word == 'baaginchu':
            return Token(t.DIVIDE, '/')
        else:
            raise Thappulu(e.C102, self.currLine)

    def run(self):
        with open(self.filename) as f:
            self.inputContent = list(map(lambda x: x.lower(), f.readlines()))
        for line in self.inputContent:
            self.currLine = line
            self.tokeniser()
        return self.tokens

    def advance(self):
        self.pos += 1
        self.current = self.currLine[self.pos] if self.pos < len(self.currLine) else None

    def tokeniser(self):
        self.pos = 0
        length = len(self.currLine)
        self.current = self.currLine[0]
        while self.current != None and self.pos < length:
            curr = self.current
            if curr.isspace():
                self.advance()
            elif curr.isdigit():
                self.tokens.append(self.makeNumber())
            elif curr.isalpha():
                word = self.makeText()
                if bp.PREPOSITIONS.search(word):
                    self.advance()  # possible error from here
                    word = self.makeText()
                self.tokens.append(self.genTextToken(word))
            else:
                raise Thappulu(e.C101, self.currLine)
