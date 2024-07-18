# type checker
import copy
from enum import Enum
from collections import ChainMap
from types import NoneType

from antlr4 import ParserRuleContext

from XMLExpParser import *
from XMLExpVisitor import *

class TypeName:
    pass  # TODO


def types(a:[TypeName]):
    tmp = []
    for i in range(len(a)):
        tmp.append(a[i].type())
    return tmp

class Qty(TypeName):

    def __init__(self, n: int, t: str = None, m:int = None):
        self.n = n
        self.ty = t
        if m is None:
            self.m = 0
        else:
            self.m = m

    def get_num(self):
        return self.n

    def get_anum(self):
        return self.m

    def type(self):
        return (self.ty, self.n)

    def fullty(self):
        return (self.ty, self.n, self.m)

class Nat(TypeName):

    def type(self):
        return ("Nat", 0)

class Fun(TypeName):

    def __init__(self, n: dict, m: dict):
        self.args = n
        self.out = m
        # self.r2 = r2

    def type(self):
        return ("Fun", (self.n,self.m))


class TypeInfer(XMLExpVisitor):

    # x, y, z, env : ChainMap{ x: n, y : m, z : v} , n m v are nat numbers 100, 100, 100, eg {x : 128}
    # st state map, {x : v1, y : v2 , z : v3}, eg {x : v1}: v1,
    # st {x : v1} --> Coq_nval case: v1 is a ChainMap of Coq_nval
    # v1 --> 128 length array v1: {0 : Coq_nval, 1 : Coq_nval, 2 : Coq_nval, ...., 127 : Coq_nval}, 2^128
    # x --> v1 --> cal(v1) --> integer
    # Coq_nval(b,r) b == |0> | |1>, r == e^(2 pi i * 1 / n), r = 0 Coq_nval(b, 0)
    # x -> v1 ----> run simulator -----> v2 ---> calInt(v2,128) == (x + 2^10) % 2^128
    def __init__(self, tenv: dict):
        self.tenv = tenv
        # self.rmax = rmax rmax is M_find(x,env), a map from var to int

    def visitRoot(self, ctx:XMLExpParser.RootContext):
        return ctx.program().accept(self)

    def visitProgram(self, ctx: XMLExpParser.ProgramContext):

        i = 0
        tmp = True
        while ctx.exp(i) is not None:
            tmp = tmp and ctx.exp(i).accept(self)
            i += 1
        return tmp

    def visitNextexp(self, ctx: XMLExpParser.NextexpContext):
        return ctx.program().accept(self)

    def visitExp(self, ctx: XMLExpParser.ExpContext):
        if ctx.letexp() is not None:
            return ctx.letexp().accept(self)
        elif ctx.appexp() is not None:
            return ctx.appexp().accept(self)
        elif ctx.ifexp() is not None:
            return ctx.ifexp().accept(self)
        elif ctx.matchexp() is not None:
            return ctx.matchexp().accept(self)
        elif ctx.cuexp() is not None:
            return self.visitCUexp(ctx.cuexp())
        elif ctx.skipexp() is not None:
            return ctx.skipexp().accept(self)
        elif ctx.xexp() is not None:
            return ctx.xexp().accept(self)
        elif ctx.srexp() is not None:
            return ctx.srexp().accept(self)
        elif ctx.qftexp() is not None:
            return ctx.qftexp().accept(self)
        elif ctx.lshiftexp() is not None:
            return ctx.lshiftexp().accept(self)
        elif ctx.rshiftexp() is not None:
            return ctx.rshiftexp().accept(self)
        elif ctx.revexp() is not None:
            return ctx.revexp().accept(self)
        elif ctx.rqftexp() is not None:
            return ctx.rqftexp().accept(self)
        elif ctx.blockexp() is not None:
            return ctx.blockexp().accept(self)

    def get_type_env(self):
        return self.tenv

    def visitLetexp(self, ctx: XMLExpParser.LetexpContext):
        f = ctx.Identifier().accept(self)
        self.st.update({f: ctx})
        return True
        #print("f", ctx)
        #ctx.exp().accept(self)

    # def visitMatchexp(self, ctx: XMLExpParser.MatchexpContext):
    #     print('1')
    #     return
    #     match_ID = ctx.idexp().accept(self)
    #     print('match_ID:', match_ID)
    #     print(self.st)
    #     match_state_value = self.st.get(match_ID)
    #     i = 0
    #     while ctx.exppair(i) is not None:
    #         vexp_node = ctx.exppair(i).vexp()
    #         if vexp_node.OP() is not None:
    #             va = vexp_node.accept(self)
    #             if match_state_value == va:
    #                 # ctx.exppair(i).exp().accept(self)
    #                 return
    #         else:
    #             # y : list= ctx.exppair(i).vexp().vexp()
    #             y = ctx.exppair(i).vexp().vexp()
    #             print('Y')
    #             print(y)
    #             print(type(y))
    #             #self.st.update({y: match_state_value - 1})
    #            # ctx.exppair(i).exp().accept(self)
    #         i += 1

    def visitMatchexp(self, ctx: XMLExpParser.MatchexpContext):
        x = ctx.Identifier().accept(self)
        #value = self.st.get(x)
        #print("value match", value)
        tmpenv = copy.deepcopy(self.tenv)
        fv = ctx.exppair(0).program().accept(self)
        renv = copy.deepcopy(self.tenv)
        self.tenv = tmpenv
        va = ctx.exppair(1).element().Identifier().accept(self)
        self.tenv.update({va : Nat()})
        sv = ctx.exppair(1).program().accept(self)
        self.tenv.pop(va)
        return fv and sv and renv == self.tenv

    def visitAppexp(self, ctx: XMLExpParser.AppexpContext):
        vx = ctx.Identifier().accept(self)
        ctxa = self.st.get(vx)
        #print("here",ctx.idexp().Identifier())
        #print("herea",ctxa.idexp(0).Identifier())
        #ctxa = self.st.get(f)
        i = 0
        tmpv = dict()
        tmpa = dict()
        while ctxa.idexp(i) is not None:
            x = ctxa.idexp(i).Identifier().accept(self)
            #print("var",ctxa.idexp(i+1).Identifier())
            v = ctx.vexp(i).accept(self)
            #print("val",v)
            tmpv.update({x:self.state.get(x)})
            tmpa.update({x:v})
            i += 1

        while len(tmpa) != 0:
            xv,re = tmpa.popitem()
            self.state.update({xv: re})
            #print("vara",xv,"vala",re)

        ctxa.program().accept(self)
        while len(tmpv) != 0:
            xv,re = tmpv.popitem()
            if re is not None:
                self.state.update({xv:re})
            else:
                self.state.pop(xv, None)

            #print ("var",xv)
            #print("val",re)

    # should do nothing
    def visitSkipexp(self, ctx: XMLExpParser.SkipexpContext):
        return True
        #x = ctx.idexp().accept(self)
        #p = ctx.vexp().accept(self)  # this will pass the visitor to the child of ctx
        #return p < self.env.get(x)

    # X posi, changed the following for an example
    def visitXexp(self, ctx: XMLExpParser.XexpContext):
        x = ctx.idexp().accept(self)
        #p = ctx.vexp().accept(self)  # this will pass the visitor to the child of ctx
        return ctx.vexp().accept(self) and isinstance(self.tenv.get(x), Nor)

        #return p < self.env.get(x) and str(self.tenv.get(x)) == "Nor"
        # print(M_find(x, self.st))

    # we will first get the position in st and check if the state is 0 or 1,
    # then decide if we go to recucively call ctx.exp
    def visitCUexp(self, ctx: XMLExpParser.CuexpContext):
        x = ctx.idexp().accept(self)
        #p = ctx.vexp().accept(self)  # this will pass the visitor to the child of ctx
        return ctx.vexp().accept(self) and isinstance(self.tenv.get(x), Nor) and ctx.program().accept(self)

    # my previous rz parsing is wrong
    # it should be RZ q posi
    def visitRzexp(self, ctx: XMLExpParser.RzexpContext):
        #q = int(ctx.vexp(0).accept(self))  # I guess then you need to define vexp
        # we can first define the var and integer case
        # I guess Identifier and int are all terminal
        # does it means that we do not need to define anything?
        x = ctx.idexp().accept(self)
        #p = ctx.vexp(1).accept(self)  # this will pass the visitor to the child of ctx
        return ctx.vexp(0).accept(self) and ctx.vexp(1).accept(self) and isinstance(self.tenv.get(x), Nor)

            (p < self.env.get(x) and q < self.env.get(x) and str(self.tenv.get(x)) == "Nor")

    # SR n x, now variables are all string, are this OK?
    def visitSrexp(self, ctx: XMLExpParser.SrexpContext):
        n = int(ctx.vexp().accept(self))
        x = ctx.idexp().accept(self)
        return n <= self.env.get(x).get_num() <= self.env.get(x) and str(self.tenv.get(x)) == "Phi"

    def visitLshiftexp(self, ctx: XMLExpParser.LshiftexpContext):
        x = ctx.idexp().accept(self)
        return str(self.tenv.get(x)) == "Nor"

    def visitRshiftexp(self, ctx: XMLExpParser.RshiftexpContext):
        x = ctx.idexp().accept(self)
        return str(self.tenv.get(x)) == "Nor"

    def visitRevexp(self, ctx: XMLExpParser.RevexpContext):
        x = ctx.idexp().accept(self)
        return str(self.tenv.get(x)) == "Nor"

    # actually, we need to change the QFT function
    # the following QFT is only for full QFT, we did not have the case for AQFT
    def visitQftexp(self, ctx: XMLExpParser.QftexpContext):
        x = ctx.idexp().accept(self)
        b = int(ctx.vexp().accept(self))
        rb = b <= self.env.get(x) and str(self.tenv.get(x)) == "Nor"
        self.tenv.update({x: Phi(self.env.get(x)-b)})
        return rb

    def visitRqftexp(self, ctx: XMLExpParser.RqftexpContext):
        x = ctx.idexp().accept(self)
        b = int(ctx.vexp().accept(self))
        rb = b <= self.env.get(x) and str(self.tenv.get(x)) == "Phi"
        self.tenv.update({x: Nor})
        return rb

    def visit(self, ctx: ParserRuleContext):
        if ctx.getChildCount() > 0:
            return self.visitChildren(ctx)
        else:
            return self.visitTerminal(ctx)

    def visitIdexp(self, ctx: XMLExpParser.IdexpContext):
        return ctx.Identifier().accept(self)

    # Visit a parse tree produced by XMLExpParser#vexp.
    def visitVexp(self, ctx: XMLExpParser.VexpContext):
        return ctx.numexp().accept(self)

    # the only thing that matters will be 48 and 47
    def visitTerminal(self, node):
        if node.getSymbol().type == XMLExpParser.Identifier:
            return node.getText()
        if node.getSymbol().type == XMLExpParser.Number:
            return int(node.getText())
        return "None"
