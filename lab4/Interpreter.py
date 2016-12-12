
import AST
import SymbolTable
from Memory import *
from Exceptions import  *
from visit import *
import sys

sys.setrecursionlimit(10000)

class Interpreter(object):


    @on('node')
    def visit(self, node):
        pass

    @when(AST.BinExpr)
    def visit(self, node):
        r1 = node.left.accept(self)
        r2 = node.right.accept(self)
        return eval("a" + node.op + "b", {"a": r1, "b": r2})

        #TODO: ponizszy kutowy komentarz
        # try sth smarter than:
        # if(node.op=='+') return r1+r2
        # elsif(node.op=='-') ...
        # but do not use python eval
    @when(AST.Assignment)
    def visit(self, node):
        pass
    #

    @when(AST.Const)
    def visit(self, node):
        return node.value

    # simplistic while loop interpretation
    @when(AST.WhileInstruction)
    def visit(self, node):
        while node.condition.accept(self):
            try:
                node.instruction.accept(self)
            except BreakException:
                break
            except ContinueException:
                pass
