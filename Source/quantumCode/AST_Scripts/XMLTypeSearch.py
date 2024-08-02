# type checker
import copy
from enum import Enum
from collections import ChainMap
from types import NoneType

from antlr4 import ParserRuleContext

from quantumCode.AST_Scripts.XMLExpParser import *
from quantumCode.AST_Scripts.XMLExpVisitor import *
from quantumCode.AST_Scripts.XMLProgrammer import *

class TypeSearch(ProgramVisitor):

    # x, y, z, env : ChainMap{ x: n, y : m, z : v} , n m v are nat numbers 100, 100, 100, eg {x : 128}
    # st state map, {x : v1, y : v2 , z : v3}, eg {x : v1}: v1,
    # st {x : v1} --> Coq_nval case: v1 is a ChainMap of Coq_nval
    # v1 --> 128 length array v1: {0 : Coq_nval, 1 : Coq_nval, 2 : Coq_nval, ...., 127 : Coq_nval}, 2^128
    # x --> v1 --> cal(v1) --> integer
    # Coq_nval(b,r) b == |0> | |1>, r == e^(2 pi i * 1 / n), r = 0 Coq_nval(b, 0)
    # x -> v1 ----> run simulator -----> v2 ---> calInt(v2,128) == (x + 2^10) % 2^128
    def __init__(self, type_environment: dict):
        self.type_environment = type_environment
        # self.rmax = rmax rmax is M_find(x,env), a map from var to int

    def visitApp(self, ctx:XMLProgramer.QXApp):
        vx = ctx.ID()
        qty = self.type_environment.get(vx)
        tml = qty.args()
        tmv = qty.pre()
        #rmv = qty.out()
        for i in range(len(tml)):
            ptv = tmv.get(tml[i])
            if isinstance(ptv, Qty) and isinstance(self.type_environment.get(x), Qty):
                if self.type_environment.get(tml[i]).type() is None and ptv.type() is not None:
                    self.type_environment.get(tml[i]).set_type(ptv.type())
        return

    def visitMatch(self, ctx:XMLProgramer.QXMatch):
        x = ctx.ID()
        #value = self.st.get(x)
        #print("value match", value)
        fenv = copy.deepcopy(self.type_environment)
        ctx.zero().accept(self)
        fenv1 = copy.deepcopy(self.type_environment)
        va = ctx.multi().elem().ID()
        self.type_environment = fenv.update({va: Nat()})
        ctx.multi().accept(self)
        if self.type_environment is not None:
            return joinTypes(fenv1, self.type_environment)

    # should do nothing
    def visitSKIP(self, ctx:XMLProgramer.QXSKIP):
        #x = ctx.Identifier().accept(self)
        #ctx.vexp().accept(self)
        return  #isinstance(self.type_environment.get(x), Qty)

    # X posi, changed the following for an example
    def visitX(self, ctx:XMLProgramer.QXX):
        x = ctx.ID()
        #ctx.vexp().accept(self)
        if isinstance(self.type_environment.get(x), Qty):
            if self.type_environment.get(x).type() is None:
                self.type_environment.get(x).set_type("Nor")
        return
        #return p < self.env.get(x) and str(self.type_environment.get(x)) == "Nor"
        # print(M_find(x, self.st))

    # we will first get the position in st and check if the state is 0 or 1,
    # then decide if we go to recucively call ctx.exp
    def visitCU(self, ctx:XMLProgramer.QXCU):
        x = ctx.ID()
        #ctx.vexp().accept(self)
        if isinstance(self.type_environment.get(x), Qty):
            if self.type_environment.get(x).type() is None:
                self.type_environment.get(x).set_type("Nor")
            ctx.program().accept(self)
        return

    # SR n x, now variables are all string, are this OK?
    def visitSR(self, ctx:XMLProgramer.QXSR):
        x = ctx.ID()
        #ctx.vexp().accept(self)
        if isinstance(self.type_environment.get(x), Qty):
            if self.type_environment.get(x).type() is None:
                self.type_environment.get(x).set_type("Phi")
        return

    def visitLshift(self, ctx:XMLProgramer.QXLshift):
        x = ctx.ID()
        if isinstance(self.type_environment.get(x), Qty):
            if self.type_environment.get(x).type() is None:
                self.type_environment.get(x).set_type("Nor")
        return

    def visitRshift(self, ctx:XMLProgramer.QXRshift):
        x = ctx.ID()
        if isinstance(self.type_environment.get(x), Qty):
            if self.type_environment.get(x).type() is None:
                self.type_environment.get(x).set_type("Nor")
        return

    def visitRev(self, ctx:XMLProgramer.QXRev):
        x = ctx.ID()
        if isinstance(self.type_environment.get(x), Qty):
            if self.type_environment.get(x).type() is None:
                self.type_environment.get(x).set_type("Nor")
        return

    # actually, we need to change the QFT function
    # the following QFT is only for full QFT, we did not have the case for AQFT
    def visitQFT(self, ctx:XMLProgramer.QXQFT):
        x = ctx.ID()
        #ctx.vexp().accept(self)
        if isinstance(self.type_environment.get(x), Qty):
            if self.type_environment.get(x).type() is None:
                self.type_environment.get(x).set_type("Nor")
        return

    def visitRQFT(self, ctx:XMLProgramer.QXRQFT):
        x = ctx.ID()
        #ctx.vexp().accept(self)
        if isinstance(self.type_environment.get(x), Qty):
            if self.type_environment.get(x).type() is None:
                self.type_environment.get(x).set_type("Phi")
        return
