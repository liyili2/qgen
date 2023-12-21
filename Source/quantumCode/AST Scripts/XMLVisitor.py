from ExpVisitor import ExpVisitor

class XMLVisitor(ExpVisitor):
    def __init__(self):
        self.xml_output = ''
        self.indentation = 0

    def visitProgram(self, ctx):
        self.xml_output += "  " * self.indentation + "<Program>\n"
        self.indentation += 1
        self.visitChildren(ctx)
        self.indentation -= 1
        self.xml_output += "  " * self.indentation + "</Program>\n"

    def visitVexp(self, ctx):
        self.xml_output += "  " * self.indentation + "<Vexp>\n"
        self.indentation += 1
        self.visitChildren(ctx)
        self.indentation -= 1
        self.xml_output += "  " * self.indentation + "</Vexp>\n"

    def visitPosi(self, ctx):
        self.xml_output += "  " * self.indentation + "<Posi>\n"
        self.indentation += 1
        self.visitChildren(ctx)
        self.indentation -= 1
        self.xml_output += "  " * self.indentation + "</Posi>\n"

    def visitExp(self, ctx):
        self.xml_output += "  " * self.indentation + "<Exp>\n"
        self.indentation += 1
        self.visitChildren(ctx)
        self.indentation -= 1
        self.xml_output += "  " * self.indentation + "</Exp>\n"

    def visitSkipexp(self, ctx):
        self.xml_output += "  " * self.indentation + "<Skipexp>\n"
        self.indentation += 1
        self.visitChildren(ctx)
        self.indentation -= 1
        self.xml_output += "  " * self.indentation + "</Skipexp>\n"

    def visitPosiexp(self, ctx):
        self.xml_output += "  " * self.indentation + "<Posiexp>\n"
        self.indentation += 1
        self.visitChildren(ctx)
        self.indentation -= 1
        self.xml_output += "  " * self.indentation + "</Posiexp>\n"

    def visitXgexp(self, ctx):
        self.xml_output += "  " * self.indentation + "<Xgexp>\n"
        self.indentation += 1
        self.visitChildren(ctx)
        self.indentation -= 1
        self.xml_output += "  " * self.indentation + "</Xgexp>\n"

    def visitCuexp(self, ctx):
        self.xml_output += "  " * self.indentation + "<Cuexp>\n"
        self.indentation += 1
        self.visitChildren(ctx)
        self.indentation -= 1
        self.xml_output += "  " * self.indentation + "</Cuexp>\n"
        
    def visitRzexp(self, ctx):
        self.xml_output += "  " * self.indentation + "<Rzexp>\n"
        self.indentation += 1
        self.visitChildren(ctx)
        self.indentation -= 1
        self.xml_output += "  " * self.indentation + "</Rzexp>\n"

    def visitRrzexp(self, ctx):
        self.xml_output += "  " * self.indentation + "<Rrzexp>\n"
        self.indentation += 1
        self.visitChildren(ctx)
        self.indentation -= 1
        self.xml_output += "  " * self.indentation + "</Rrzexp>\n"

    def visitSrexp(self, ctx):
        self.xml_output += "  " * self.indentation + "<Srexp>\n"
        self.indentation += 1
        self.visitChildren(ctx)
        self.indentation -= 1
        self.xml_output += "  " * self.indentation + "</Srexp>\n"

    def visitSrrexp(self, ctx):
        self.xml_output += "  " * self.indentation + "<Srrexp>\n"
        self.indentation += 1
        self.visitChildren(ctx)
        self.indentation -= 1
        self.xml_output += "  " * self.indentation + "</Srrexp>\n"

    def visitLshiftexp(self, ctx):
        self.xml_output += "  " * self.indentation + "<Lshiftexp>\n"
        self.indentation += 1
        self.visitChildren(ctx)
        self.indentation -= 1
        self.xml_output += "  " * self.indentation + "</Lshiftexp>\n"

    def visitRshiftexp(self, ctx):
        self.xml_output += "  " * self.indentation + "<Rshiftexp>\n"
        self.indentation += 1
        self.visitChildren(ctx)
        self.indentation -= 1
        self.xml_output += "  " * self.indentation + "</Rshiftexp>\n"

    def visitRevexp(self, ctx):
        self.xml_output += "  " * self.indentation + "<Revexp>\n"
        self.indentation += 1
        self.visitChildren(ctx)
        self.indentation -= 1
        self.xml_output += "  " * self.indentation + "</Revexp>\n"

    def visitQftexp(self, ctx):
        self.xml_output += "  " * self.indentation + "<Qftexp>\n"
        self.indentation += 1
        self.visitChildren(ctx)
        self.indentation -= 1
        self.xml_output += "  " * self.indentation + "</Qftexp>\n"

    def visitRqftexp(self, ctx):
        self.xml_output += "  " * self.indentation + "<Rqftexp>\n"
        self.indentation += 1
        self.visitChildren(ctx)
        self.indentation -= 1
        self.xml_output += "  " * self.indentation + "</Rqftexp>\n"

    def visitSeqexp(self, ctx):
        self.xml_output += "  " * self.indentation + "<Seqexp>\n"
        self.indentation += 1
        self.visitChildren(ctx)
        self.indentation -= 1
        self.xml_output += "  " * self.indentation + "</Seqexp>\n"
        
    def visitNumexp(self, ctx):
        self.xml_output += "  " * self.indentation + "<Numexp>\n"
        self.indentation += 1
        self.visitChildren(ctx)
        self.indentation -= 1
        self.xml_output += "  " * self.indentation + "</Numexp>\n"

    def visitAddexp(self, ctx):
        self.xml_output += "  " * self.indentation + "<Addexp>\n"
        self.indentation += 1
        self.visitChildren(ctx)
        self.indentation -= 1
        self.xml_output += "  " * self.indentation + "</Addexp>\n"

    def visitSubexp(self, ctx):
        self.xml_output += "  " * self.indentation + "<Subexp>\n"
        self.indentation += 1
        self.visitChildren(ctx)
        self.indentation -= 1
        self.xml_output += "  " * self.indentation + "</Subexp>\n"

    def visitMultexp(self, ctx):
        self.xml_output += "  " * self.indentation + "<Multexp>\n"
        self.indentation += 1
        self.visitChildren(ctx)
        self.indentation -= 1
        self.xml_output += "  " * self.indentation + "</Multexp>\n"

    def visitDivexp(self, ctx):
        self.xml_output += "  " * self.indentation + "<Divexp>\n"
        self.indentation += 1
        self.visitChildren(ctx)
        self.indentation -= 1
        self.xml_output += "  " * self.indentation + "</Divexp>\n"

    def visitTerminal(self, node):
        # For leaf nodes 
        self.xml_output += f'{"  " * self.indentation}<{node.getSymbol().type}>{node.getText()}</{node.getSymbol().type}>\n'

    def get_xml_output(self):
        return self.xml_output
