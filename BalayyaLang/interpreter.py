from .utils import Thappulu, err as e

class Interpreter:
    def __init__(self):
        self.out = ''

    def visit(self, node):
        methodName = f'visit_{type(node).__name__}'
        method = getattr(self, methodName, self.noMethod)
        method(node)
        return self.out
    
    def noMethod(self, node):
        raise Thappulu(e.C103, e.info(node))
    
    def visit_Token(self, node):
        print('visited Token')
        self.out += node.value
    
    def visit_numNode(self, node):
        print('visited numNode')
        self.out += node.token.value

    def visit_binOpsNode(self, node):
        print('visited binOpsNode')
        self.out += '('
        if node.left:
            self.visit(node.left)
        if node.operator:
            self.visit(node.operator)
        if node.right:
            self.visit(node.right)
        self.out += ')'
        
            