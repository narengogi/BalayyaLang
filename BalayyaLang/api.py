from .lexer import Lexer


class BalayyaLang:
    def __init__(self) -> None:
        pass

    def _pyCompiler(self, filename):
        lex = Lexer(filename)

    def run(self, filename):
        pyCompiled = self._pyCompiler(filename)
        hello = 'hello'
        exec(pyCompiled or 'print(hello)')
