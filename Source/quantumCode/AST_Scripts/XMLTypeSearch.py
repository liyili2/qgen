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


def types(a: [TypeName]):
    tmp = []
    for i in range(len(a)):
        tmp.append(a[i].type())
    return tmp


class Qty(TypeName):

    def __init__(self, n: str, t: str = None, m: str = None):
        self.n = n
        self.ty = t
        if m is None:
            self.m = "0"
        else:
            self.m = m

    def get_num(self):
        return self.n

    def get_anum(self):
        return self.m

    def set_type(self, ty: str):
        self.ty = ty

    def type(self):
        return self.ty

    def fullty(self):
        return (self.ty, self.n, self.m)


class Nat(TypeName):

    def type(self):
        return "Nat"


class Fun(TypeName):

    def __init__(self, la: [str], n: dict, m: dict):
        self.args = la
        self.pre = n
        self.out = m
        # self.r2 = r2

    def type(self):
        return ("Fun", (self.args, self.pre, self.out))

    def args(self):
        return self.args

    def pre(self):
        return self.pre

    def out(self):
        return self.out


def joinType(a: TypeName, b: TypeName):
    if isinstance(a, Qty) and isinstance(b, Qty):
        if a.type() is None or b.type() is None:
            if a.type() is None:
                a.set_type(b.type())
            else:
                b.set_type(a.type())
            return a
        elif a.type() == b.type():
            return a
        else:
            return None
    elif isinstance(a, Nat) and isinstance(b, Nat):
        return a
    elif isinstance(a, Fun) and isinstance(b, Fun):
        return a
    else:
        return None


def joinTypes(a: dict, b: dict):
    for key in a.keys():
        if b.get(key) is not None:
            if isinstance(a.get(key), Qty) and isinstance(b.get(key), Qty):
                if a.get(key).type() is None and b.get(key).type() is not None:
                    a.get(key).set_type(b.get(key).type())
    return a


def equalTypes(a: dict, b: dict):
    tmp = True
    for key in a.keys():
        if a.get(key) != b.get(key):
            tmp = False
    return tmp


class TypeSearch(XMLExpVisitor):

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

    def visitProgram(self, ctx: XMLExpParser.ProgramContext):
        i = 0
        while ctx.exp(i) is not None:
            ctx.exp(i).accept(self)
            i += 1

    def visitNextexp(self, ctx: XMLExpParser.NextexpContext):
        ctx.program().accept(self)

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
        elif ctx.blockexp() is not None:
            ctx.blockexp().accept(self)

    def visitAppexp(self, ctx: XMLExpParser.AppexpContext):
        vx = ctx.Identifier().accept(self)
        qty = self.tenv.get(vx)
        tml = qty.args()
        tmv = qty.pre()
        #rmv = qty.out()
        for i in range(len(tml)):
            ptv = tmv.get(tml[i])
            if isinstance(ptv, Qty) and isinstance(self.tenv.get(x), Qty):
                if self.tenv.get(tml[i]).type() is None and ptv.type() is not None:
                    self.tenv.get(tml[i]).set_type(ptv.type())
        return

    def visitMatchexp(self, ctx: XMLExpParser.MatchexpContext):
        x = ctx.Identifier().accept(self)
        #value = self.st.get(x)
        #print("value match", value)
        fenv = copy.deepcopy(self.tenv)
        ctx.exppair(0).program().accept(self)
        fenv1 = copy.deepcopy(self.tenv)
        va = ctx.exppair(1).element().Identifier().accept(self)
        self.tenv = fenv.update({va : Nat()})
        ctx.exppair(1).program().accept(self)
        if self.tenv is not None:
            return joinTypes(fenv1, self.tenv)

    def visitBlockexp(self, ctx: XMLExpParser.BlockexpContext):
        return

    # should do nothing
    def visitSkipexp(self, ctx: XMLExpParser.SkipexpContext):
        #x = ctx.Identifier().accept(self)
        #ctx.vexp().accept(self)
        return  #isinstance(self.tenv.get(x), Qty)

    # X posi, changed the following for an example
    def visitXexp(self, ctx: XMLExpParser.XexpContext):
        x = ctx.Identifier().accept(self)
        #ctx.vexp().accept(self)
        if isinstance(self.tenv.get(x), Qty):
            if self.tenv.get(x).type() is None:
                self.tenv.get(x).set_type("Nor")
        return
        #return p < self.env.get(x) and str(self.tenv.get(x)) == "Nor"
        # print(M_find(x, self.st))

    # we will first get the position in st and check if the state is 0 or 1,
    # then decide if we go to recucively call ctx.exp
    def visitCUexp(self, ctx: XMLExpParser.CuexpContext):
        x = ctx.Identifier().accept(self)
        #ctx.vexp().accept(self)
        if isinstance(self.tenv.get(x), Qty):
            if self.tenv.get(x).type() is None:
                self.tenv.get(x).set_type("Nor")
            ctx.program().accept(self)
        return

    # SR n x, now variables are all string, are this OK?
    def visitSrexp(self, ctx: XMLExpParser.SrexpContext):
        x = ctx.Identifier().accept(self)
        #ctx.vexp().accept(self)
        if isinstance(self.tenv.get(x), Qty):
            if self.tenv.get(x).type() is None:
                self.tenv.get(x).set_type("Phi")
        return

    def visitLshiftexp(self, ctx: XMLExpParser.LshiftexpContext):
        x = ctx.Identifier().accept(self)
        if isinstance(self.tenv.get(x), Qty):
            if self.tenv.get(x).type() is None:
                self.tenv.get(x).set_type("Nor")
        return

    def visitRshiftexp(self, ctx: XMLExpParser.RshiftexpContext):
        x = ctx.Identifier().accept(self)
        if isinstance(self.tenv.get(x), Qty):
            if self.tenv.get(x).type() is None:
                self.tenv.get(x).set_type("Nor")
        return

    def visitRevexp(self, ctx: XMLExpParser.RevexpContext):
        x = ctx.Identifier().accept(self)
        if isinstance(self.tenv.get(x), Qty):
            if self.tenv.get(x).type() is None:
                self.tenv.get(x).set_type("Nor")
        return

    # actually, we need to change the QFT function
    # the following QFT is only for full QFT, we did not have the case for AQFT
    def visitQftexp(self, ctx: XMLExpParser.QftexpContext):
        x = ctx.Identifier().accept(self)
        #ctx.vexp().accept(self)
        if isinstance(self.tenv.get(x), Qty):
            if self.tenv.get(x).type() is None:
                self.tenv.get(x).set_type("Nor")
        return

    def visitRqftexp(self, ctx: XMLExpParser.RqftexpContext):
        x = ctx.Identifier().accept(self)
        #ctx.vexp().accept(self)
        if isinstance(self.tenv.get(x), Qty):
            if self.tenv.get(x).type() is None:
                self.tenv.get(x).set_type("Phi")
        return
