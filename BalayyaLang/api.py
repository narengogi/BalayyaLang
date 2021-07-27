from .lexer import Lexer
from .parser import Parser
from .interpreter import Interpreter

class BalayyaLang:
    def __init__(self) -> None:
        pass

    def _pyCompiler(self, filename):
        lex = Lexer(filename).run()
        parse = Parser(lex).run()
        print(parse)
        code = Interpreter().visit(parse)
        print(code)
        return code
        
    def run(self, filename):
        pyCompiled = self._pyCompiler(filename)
        hello = 'hello'
        exec(pyCompiled)
