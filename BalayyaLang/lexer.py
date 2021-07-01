from .grammar import Grammar as bp, Tokens as t
from .utils import Thappulu, err as e


class Token:
    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value

    def __repr__(self):
        return f'type: {self.type_}, value: {self.value}'


class Lexer:
    def __init__(self, filename):
        self.inputContent = []
        self.filename = filename
        self.pos = 0
        self.current = ''
        self.currLine = ''

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

    def parse(self):
        with open(self.filename) as f:
            self.inputContent = list(map(lambda x: x.lower(), f.readlines()))
        print(self.inputContent)
        for line in self.inputContent:
            self.currLine = line
            self.tokeniser()

    def advance(self):
        self.pos += 1
        self.current = self.currLine[self.pos] if self.pos < len(
            self.currLine) else None

    def tokeniser(self):
        self.pos = 0
        length = len(self.currLine)
        tokens = []
        self.current = self.currLine[0]
        while self.current != None and self.pos < length:
            curr = self.current
            if curr.isspace():
                self.advance()
            elif curr.isdigit():
                tokens.append(self.makeNumber())
            else:
                raise Thappulu(e.C101, e.info(self.currLine))

        print(tokens)
