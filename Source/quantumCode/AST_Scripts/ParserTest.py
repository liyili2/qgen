import ExpParser
import XMLVisitor

x = ExpParser.ExpParser("QFT x 0; SR x 10; RQFT x 0 ")

print(x)