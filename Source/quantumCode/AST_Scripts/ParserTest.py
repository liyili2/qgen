from antlr4 import *
from ExpListener import ExpListener
from ExpLexer import ExpLexer
from ExpParser import ExpParser
import XMLVisitor

def main():
  #giveMeInput = input("(x,0)\n")
  i_stream = InputStream("QFT x 0; SR 10 x; RQFT x 0 //We first turn x array to QFT type, and we apply SR gate to rotate the phase of x for 2 pi i * (1/2^10). It will make sense if 10 < rmax, RQFT is the inverse of QFT.")
  lexer = ExpLexer(i_stream)
  t_stream = CommonTokenStream(lexer)
  parser = ExpParser(t_stream)
  tree = parser.program()
  print(tree.toStringTree(recog=parser))
#y = XMLVisitor.XMLVisitor()

if __name__ == "__main__":
    main()