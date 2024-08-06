#from collections import ChainMap
from types import NoneType
from quantumCode.AST_Scripts.XMLExpVisitor import XMLExpVisitor
from quantumCode.AST_Scripts.XMLExpParser import XMLExpParser

class XMLPrinter(XMLExpVisitor):

    def __init__(self):
        #self.type_environment = type_environment
        self.xml_output = ''
        #self.indentation = 0

    def visitRoot(self, ctx: XMLExpParser.RootContext):
        self.xml_output += self.visitChildren(ctx)

    # Visit a parse tree produced by XMLExpParser#nextexp.
    def visitNextexp(self, ctx: XMLExpParser.NextexpContext):
        self.xml_output += self.visitChildren(ctx)

    # Visit a parse tree produced by XMLExpParser#program.
    def visitProgram(self, ctx: XMLExpParser.ProgramContext):
        i = 0
        while ctx.exp(i) is not None:
            ctx.exp(i).accept(self)
            self.xml_output += "\n"
            i += 1

    # should do nothing
    def visitExp(self, ctx: XMLExpParser.ExpContext):
        if ctx.letexp() is not None:
            ctx.letexp().accept(self)
        elif ctx.appexp() is not None:
            ctx.appexp().accept(self)
        elif ctx.ifexp() is not None:
            ctx.ifexp().accept(self)
        elif ctx.matchexp() is not None:
            ctx.matchexp().accept(self)
        elif ctx.cuexp() is not None:
            self.visitCUexp(ctx.cuexp())
        elif ctx.skipexp() is not None:
            ctx.skipexp().accept(self)
        elif ctx.xexp() is not None:
            ctx.xexp().accept(self)
        elif ctx.srexp() is not None:
            ctx.srexp().accept(self)
        elif ctx.qftexp() is not None:
            ctx.qftexp().accept(self)
        elif ctx.lshiftexp() is not None:
            ctx.lshiftexp().accept(self)
        elif ctx.rshiftexp() is not None:
            ctx.rshiftexp().accept(self)
        elif ctx.revexp() is not None:
            ctx.revexp().accept(self)
        elif ctx.rqftexp() is not None:
            ctx.rqftexp().accept(self)

    def visitLetexp(self, ctx: XMLExpParser.LetexpContext):
        self.xml_output += "let " + ctx.Identifier().accept(self) + " = "
        i = 0
        while ctx.idexp(i) is not None:
            self.xml_output += "("
            ctx.idexp(i).accept(self)
            self.xml_output += ")"
            i += 1
        self.xml_output += " in\n  "
        ctx.program().accept(self)

    def visitMatchexp(self, ctx: XMLExpParser.MatchexpContext):
        self.xml_output += "match "
        ctx.Identifier().accept(self)
        self.xml_output += " with "
        i = 0
        while ctx.exppair(i) is not None:
            ctx.exppair(i).accept(self)
            i += 1
        self.xml_output += "\n end \n"

    def visitExppair(self, ctx: XMLExpParser.ExppairContext):
        ctx.element().accept(self)
        self.xml_output += " => "
        ctx.program().accept(self)

    def visitAppexp(self, ctx: XMLExpParser.AppexpContext):
        self.xml_output += " "
        ctx.Identifier().accept(self)
        self.xml_output += "("
        i = 0
        while ctx.vexp(i) is not None:
            ctx.vexp(i).accept(self)
            self.xml_output += ", "
            #print("var",ctxa.idexp(i+1).Identifier())
            i += 1
        self.xml_output += ")"

    def visitIfexp(self, ctx: XMLExpParser.IfexpContext):
        self.xml_output += "if "
        ctx.vexp().accept(self)
        self.xml_output += " then {"
        ctx.nextexp(0).accept(self)
        self.xml_output += "} else {"
        ctx.nextexp(1).accept(self)
        self.xml_output += "}"

    def visitSkipexp(self, ctx: XMLExpParser.SkipexpContext):
        self.xml_output += "  SKIP ("
        ctx.Identifier().accpet(self)
        self.xml_output += ", "
        ctx.vexp().accept(self)
        self.xml_output += ")"

    # X posi, changed the following for an example
    def visitXexp(self, ctx: XMLExpParser.XexpContext):
        self.xml_output += "  X ("
        ctx.Identifier().accpet(self)
        self.xml_output += ", "
        ctx.vexp().accept(self)
        self.xml_output += ")"


    # we will first get the position in st and check if the state is 0 or 1,
    # then decide if we go to recucively call ctx.exp
    def visitCUexp(self, ctx: XMLExpParser.CuexpContext):
        self.xml_output += "  CU ("
        ctx.Identifier().accpet(self)
        self.xml_output += ", "
        ctx.vexp().accept(self)
        self.xml_output += ")"
        ctx.program().accept(self)

    # SR n x, now variables are all string, are this OK?
    def visitSrexp(self, ctx: XMLExpParser.SrexpContext):
        self.xml_output += "  SR ("
        ctx.Identifier().accpet(self)
        self.xml_output += ", "
        ctx.vexp().accept(self)
        self.xml_output += ")"

    def visitLshiftexp(self, ctx: XMLExpParser.LshiftexpContext):
        self.xml_output += "  Lshift "
        ctx.Identifier().accpet(self)

    def visitRshiftexp(self, ctx: XMLExpParser.RshiftexpContext):
        self.xml_output += "  Rshift "
        ctx.Identifier().accpet(self)

    def visitRevexp(self, ctx: XMLExpParser.RevexpContext):
        self.xml_output += "  Rev "
        ctx.Identifier().accpet(self)

    # actually, we need to change the QFT function
    # the following QFT is only for full QFT, we did not have the case for AQFT
    def visitQftexp(self, ctx: XMLExpParser.QftexpContext):
        self.xml_output += "  QFT ("
        ctx.Identifier().accpet(self)
        self.xml_output += ", "
        ctx.vexp().accept(self)
        self.xml_output += ")"

    def visitRqftexp(self, ctx: XMLExpParser.RqftexpContext):
        self.xml_output += "  RQFT "
        ctx.Identifier().accpet(self)

    def visitIdexp(self, ctx: XMLExpParser.IdexpContext):
        ctx.Identifier().accpet(self)
        if ctx.atype() is not None:
            self.xml_output += " : "
            ctx.atype().accept(self)

    def visitAtype(self, ctx:XMLExpParser.AtypeContext):
        if ctx.Nat() is not None:
            self.xml_output += "nat"
        elif ctx.Qt() is not None:
           self.xml_output += "Q("
           ctx.element(0).accept(self)
           self.xml_output += ")"
        elif ctx.Nor() is not None:
           self.xml_output += "Nor("
           ctx.element(0).accept(self)
           self.xml_output += ")"
        elif ctx.Phi() is not None:
           self.xml_output += "Phi("
           ctx.element(0).accept(self)
           self.xml_output += ", "
           ctx.element(1).accept(self)
           self.xml_output += ")"



    def visitElement(self, ctx:XMLExpParser.ElementContext):
        if ctx.numexp() is not None:
            ctx.numexp().accept(self)
        else:
            ctx.Identifier().accept(self)

    def visitVexp(self, ctx: XMLExpParser.VexpContext):
        if ctx.idexp() is not None:
            ctx.idexp().accept(self)
        if ctx.NUM() is not None:
            ctx.numexp().accept(self)
        else:
            #print("here")
            #print("op",ctx.op())
            ctx.vexp(0).accept(self)
            if ctx.op().Plus() is not None:
                self.xml_output += " + "
            elif ctx.op().Minus() is not None:
                self.xml_output += " - "
            elif ctx.op().Times() is not None:
                self.xml_output += " * "
            elif ctx.op().Div() is not None:
                self.xml_output += " / "
            elif ctx.op().Exp() is not None:
                self.xml_output += " ^ "
            elif ctx.op().Mod() is not None:
                self.xml_output += " % "
            elif ctx.op().GNum() is not None:
                self.xml_output += " @ "
            ctx.vexp(1).accept(self)

    def visitTerminal(self, node):
        # For leaf nodes
        if node.getSymbol().type == XMLExpParser.Identifier:
            self.xml_output += ""f'{node.getText()}\n'""
        if node.getSymbol().type == XMLExpParser.Number:
            self.xml_output += ""f'{node.getText()}\n'""
        self.xml_output += ""

    # def visit(self, ctx):
    #    if ctx.getChildCount() > 0:
    #        self.visitChildren(ctx)
    #    else:
    #        self.visitTerminal(ctx)

    def getXML(self):
        return self.xml_output
