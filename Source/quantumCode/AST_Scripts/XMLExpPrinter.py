#from collections import ChainMap
from types import NoneType
from Source.quantumCode.AST_Scripts.ExpParser import *
from Source.quantumCode.AST_Scripts.XMLExpVisitor import XMLExpVisitor
from Source.quantumCode.AST_Scripts.XMLExpParser import XMLExpParser

class XMLExpPrinter(XMLExpVisitor):

    def __init__(self):
        #self.tenv = tenv
        self.xml_output = ''
        #self.indentation = 0

    def visitRoot(self, ctx: XMLExpParser.RootContext):
        self.xml_output += "<root>"+self.visitChildren(ctx)+"</root>"

    # Visit a parse tree produced by XMLExpParser#nextexp.
    def visitNextexp(self, ctx: XMLExpParser.NextexpContext):
        self.xml_output += "<next>"+self.visitChildren(ctx)+"</next>"

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
        self.xml_output += "<let id = '" + ctx.Identifier().accept(self) + "' >"
        i = 0
        while ctx.idexp(i) is not None:
            #self.xml_output += "("
            ctx.idexp(i).accept(self)
            #self.xml_output += ")"
            i += 1
        #self.xml_output += " in\n  "
        ctx.program().accept(self)
        self.xml_output+= "</let>"

    def visitMatchexp(self, ctx: XMLExpParser.MatchexpContext):
        self.xml_output += "<match id = '"
        ctx.Identifier().accept(self)
        self.xml_output += "'>"
        i = 0
        while ctx.exppair(i) is not None:
            ctx.exppair(i).accept(self)
            i += 1
        #self.xml_output += "\n end \n"

    def visitExppair(self, ctx: XMLExpParser.ExppairContext):
        self.xml_output += "<pair case ='"
        ctx.element().accept(self)
        self.xml_output += "'> "
        ctx.program().accept(self)
        self.xml_output += "</pair>"

    def visitAppexp(self, ctx: XMLExpParser.AppexpContext):
        self.xml_output += "<app id = '"
        ctx.Identifier().accept(self)
        self.xml_output += "' >"
        i = 0
        while ctx.vexp(i) is not None:
            ctx.vexp(i).accept(self)
            self.xml_output += ", "
            #print("var",ctxa.idexp(i+1).Identifier())
            i += 1
        self.xml_output += "</app>"

    def visitIfexp(self, ctx: XMLExpParser.IfexpContext):
        self.xml_output += "<if>"
        ctx.vexp().accept(self)
        self.xml_output += "\n"
        ctx.nextexp(0).accept(self)
        self.xml_output += "\n"
        ctx.nextexp(1).accept(self)
        self.xml_output += "</if>"

    def visitSkipexp(self, ctx: XMLExpParser.SkipexpContext):
        self.xml_output += "<pexp gate = 'SKIP' id ='"
        ctx.Identifier().accpet(self)
        self.xml_output += "' >"
        ctx.vexp().accept(self)
        self.xml_output += "</pexp>"

    # X posi, changed the following for an example
    def visitXexp(self, ctx: XMLExpParser.XexpContext):
        self.xml_output += "<pexp gate = 'X' id ='"
        ctx.Identifier().accpet(self)
        self.xml_output += "' >"
        ctx.vexp().accept(self)
        self.xml_output += "</pexp>"


    # we will first get the position in st and check if the state is 0 or 1,
    # then decide if we go to recucively call ctx.exp
    def visitCUexp(self, ctx: XMLExpParser.CuexpContext):
        self.xml_output += "<pexp gate = 'CU' id ='"
        ctx.Identifier().accpet(self)
        self.xml_output += "' >"
        ctx.vexp().accept(self)
        self.xml_output += "\n"
        ctx.program().accept(self)
        self.xml_output += "</pexp>"


    # SR n x, now variables are all string, are this OK?
    def visitSrexp(self, ctx: XMLExpParser.SrexpContext):
        self.xml_output += "<pexp gate = 'SR' id ='"
        ctx.Identifier().accpet(self)
        self.xml_output += "' >"
        ctx.vexp().accept(self)
        self.xml_output += "</pexp>"

    def visitLshiftexp(self, ctx: XMLExpParser.LshiftexpContext):
        self.xml_output += "<pexp gate = 'Lshift' id ='"
        ctx.Identifier().accpet(self)
        self.xml_output += "' >"
        self.xml_output += "</pexp>"

    def visitRshiftexp(self, ctx: XMLExpParser.RshiftexpContext):
        self.xml_output += "<pexp gate = 'Rshift' id ='"
        ctx.Identifier().accpet(self)
        self.xml_output += "' >"
        self.xml_output += "</pexp>"

    def visitRevexp(self, ctx: XMLExpParser.RevexpContext):
        self.xml_output += "<pexp gate = 'Rev' id ='"
        ctx.Identifier().accpet(self)
        self.xml_output += "' >"
        self.xml_output += "</pexp>"

    # actually, we need to change the QFT function
    # the following QFT is only for full QFT, we did not have the case for AQFT
    def visitQftexp(self, ctx: XMLExpParser.QftexpContext):
        self.xml_output += "<pexp gate = 'QFT' id ='"
        ctx.Identifier().accpet(self)
        self.xml_output += "' >"
        ctx.vexp().accept(self)
        self.xml_output += "</pexp>"

    def visitRqftexp(self, ctx: XMLExpParser.RqftexpContext):
        self.xml_output += "<pexp gate = 'RQFT' id ='"
        ctx.Identifier().accpet(self)
        self.xml_output += "' >"
        self.xml_output += "</pexp>"

    def visitIdexp(self, ctx: XMLExpParser.IdexpContext):
        self.xml_output += "<vexp op = 'id' "
        if ctx.atype() is not None:
            ctx.atype.accept(self)
        self.xml_output += ">"
        ctx.Identifier().accpet(self)
        self.xml_output += "</vexp>"
    def visitAtype(self, ctx:XMLExpParser.AtypeContext):
        self.xml_output += "type = "
        if ctx.Nat() is not None:
            self.xml_output += "'nat' "
        elif ctx.Qt() is not None:
           self.xml_output += "Q("
           ctx.element(0).accept(self)
           self.xml_output += ") "
        elif ctx.Nor() is not None:
           self.xml_output += "Nor("
           ctx.element(0).accept(self)
           self.xml_output += ") "
        elif ctx.Phi() is not None:
           self.xml_output += "Phi("
           ctx.element(0).accept(self)
           self.xml_output += ", "
           ctx.element(1).accept(self)
           self.xml_output += ") "

    def visitElement(self, ctx:XMLExpParser.ElementContext):
        if ctx.numexp() is not None:
            ctx.numexp().accept(self)
        else:
            ctx.Identifier().accept(self)

    def visitVexp(self, ctx: XMLExpParser.VexpContext):
        if ctx.idexp() is not None:
            ctx.idexp().accept(self)
        if ctx.NUM() is not None:
            self.xml_output += "<vexp op = 'num' >"
            ctx.numexp().accept(self)
            self.xml_output += "</vexp>"
        else:
            #print("here")
            #print("op",ctx.op())
            self.xml_output += "<vexp op = '"
            if ctx.op().Plus() is not None:
                self.xml_output += "+"
            elif ctx.op().Minus() is not None:
                self.xml_output += "-"
            elif ctx.op().Times() is not None:
                self.xml_output += "*"
            elif ctx.op().Div() is not None:
                self.xml_output += "/"
            elif ctx.op().Exp() is not None:
                self.xml_output += "^"
            elif ctx.op().Mod() is not None:
                self.xml_output += "%"
            elif ctx.op().GNum() is not None:
                self.xml_output += "$"
            self.xml_output += "' >"
            ctx.vexp(0).accept(self)
            ctx.vexp(1).accept(self)
            self.xml_output += "</vexp>"

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
