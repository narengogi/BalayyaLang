from .grammar import Tokens as t
             
#    #  ####  #####  ######  ####  
##   # #    # #    # #      #      
# #  # #    # #    # #####   ####  
#  # # #    # #    # #           # 
#   ## #    # #    # #      #    # 
#    #  ####  #####  ######  ####  
    
class numNode:
    def __init__(self, token) -> None:
        self.token = token
    def __repr__(self) -> str:
        return f'{self.token}'

class binOpsNode:
    def __init__(self, left, operator, right) -> None:
        self.left = left
        self.right = right
        self.operator = operator
    def __repr__(self) -> str:
        return f'({self.left} {self.operator} {self.right})'
class Parser:
    def __init__(self, lex):
        self.lex = lex
        self.pos = 0
        self.current = lex[0]

    def advance(self):
        self.pos += 1
        self.current = self.lex[self.pos] if self.pos < len(self.lex) else None
    
    def _getNum(self):
        token = self.current
        if token.type == t.NUM:
            self.advance()
            return numNode(token)
    
    def __getBinaryToken(self, func, ops):
        left = func()
        
        while self.current and self.current.type in ops:
            operator = self.current
            self.advance()
            right = func()
            left = binOpsNode(left, operator, right)
        
        return left

    def _getTerm(self):
        return self.__getBinaryToken(self._getNum, [t.MULTIPLY, t.DIVIDE])
    
    def _getExpr(self):
        return self.__getBinaryToken(self._getNum, [t.PLUS, t.MINUS])

    def run(self):
        res = self._getTerm()
        return res
        
