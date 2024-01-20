import unittest
from antlr4 import *
from ExpListener import ExpListener
from ExpLexer import ExpLexer
from ExpParser import ExpParser
from XMLVisitor import XMLVisitor

class MyTestCase(unittest.TestCase):
    def test_something(self):
        i_stream = InputStream("X (x,0) ; CU (x,0) (CU (x,1) (X (y,1)))")
        lexer = ExpLexer(i_stream)
        t_stream = CommonTokenStream(lexer)
        parser = ExpParser(t_stream)
        tree = parser.program()
        xml = XMLVisitor()
        result = tree.accept(xml)
        print(xml.getXML())
        #self.assertEqual(True, False)  # add assertion here
  #walker = ParseTreeWalker()
#y = XMLVisitor.XMLVisitor()

if __name__ == '__main__':
    unittest.main()
