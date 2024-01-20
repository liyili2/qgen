from antlr4 import *
from ExpListener import ExpListener
from ExpLexer import ExpLexer
from ExpParser import ExpParser
import XMLVisitor

def main():
  #giveMeInput = input("(x,0)\n")
  i_stream = InputStream("X (x,0) ; CU (x,0) (CU (x,1) (X (y,1)))\n")
  lexer = ExpLexer(i_stream)
  t_stream = CommonTokenStream(lexer)
  parser = ExpParser(t_stream)
  tree = parser.program()
  print(tree.toStringTree(recog=parser))
#y = XMLVisitor.XMLVisitor()

if __name__ == "__main__":
    main()