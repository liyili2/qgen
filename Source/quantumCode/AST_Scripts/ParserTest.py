from antlr4 import *
from ExpListener import ExpListener
from ExpLexer import ExpLexer
from ExpParser import ExpParser
import XMLVisitor

def main():
  giveMeInput = input("QFT (x,0); SR (x,10); RQFT (x, 0)\n")
  i_stream = InputStream(giveMeInput)
  lexer = ExpLexer(i_stream)
  t_stream = CommonTokenStream(lexer)
  parser = ExpParser(t_stream)
  tree = parser.exp()
  print(tree.toStringTree(recog=parser))
#y = XMLVisitor.XMLVisitor()

if __name__ == "__main__":
    main()