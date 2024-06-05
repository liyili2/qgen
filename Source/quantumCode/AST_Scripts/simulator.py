import traceback
from collections import ChainMap
# from types import NoneType

from antlr4 import ParserRuleContext

from Source.quantumCode.AST_Scripts.XMLExpParser import *
from Source.quantumCode.AST_Scripts.XMLExpVisitor import *

NoneType = type(None)


class CoqVal:
    pass  # TODO


class CoqNVal(CoqVal):

    def __init__(self, boolean_binary_array: [bool], phase: int):
        self.boolean_binary = boolean_binary_array
        self.phase = phase

    def getBits(self):
        return self.boolean_binary

    def getPhase(self):
        return self.phase


class CoqQVal(CoqVal):

    def __init__(self, r1: int, r2: int, b: [bool], n: int):
        self.r1 = r1
        self.r2 = r2
        self.n = n
        self.b = b

    def getPhase(self):
        return self.r1

    def getLocal(self):
        return self.r2

    def getRest(self):
        return self.b

    def getNum(self):
        return self.n


"""
Helper Functions
"""


def exchange(coq_val: CoqVal, n: int):
    if isinstance(coq_val, CoqNVal):
        coq_val.getBits()[n] = not coq_val.getBits()[n]


def times_rotate(v, q, rmax):
    if isinstance(v, CoqNVal):
        if v.boolean_binary:
            return CoqNVal(v.getBits(), rotate(v.getPhase(), q, rmax))
        else:
            return CoqNVal(v.getBits(), v.getPhase())
    else:
        return CoqQVal(v.r1, rotate(v.r2, q, rmax))


def addto(r, n, rmax):
    return (r + 2 ** max_helper(rmax, n)) % 2 ** rmax


def max_helper(x, y):
    return max(x - y, 0)


def rotate(r, n, rmax):
    return addto(r, n, rmax)


def addto_n(r, n, rmax):
    return max_helper(r + 2 ** rmax, 2 ** max_helper(rmax, n)) % 2 ** rmax


def r_rotate(r, n, rmax):
    return addto_n(r, n, rmax)


def times_r_rotate(v, q, rmax):
    if isinstance(v, CoqNVal):
        if v.boolean_binary:
            return CoqNVal(v.getBits(), r_rotate(v.getPhase(), q, rmax))
        else:
            return CoqNVal(v.getBits(), v.getPhase())
    else:
        return CoqQVal(v.r1, r_rotate(v.r2, q, rmax))


def up_h(v, rmax):
    if isinstance(v, CoqNVal):
        b = v.boolean_binary
        r = v.phase
        if b:
            return CoqQVal(
                r,
                rotate(0, 1, rmax)
            )
        else:
            return CoqQVal(r, 0)
    else:
        r = v.r1
        f = v.r2
        return CoqNVal(
            2 ** max_helper(rmax, 1) <= f,
            r
        )


def natminusmod(x, v, a):
    if x - v < 0:
        return x - v + a
    else:
        return x - v


def bit_array_to_int(bit_array, num_qubits):
    val = 0
    for i in range(num_qubits):
        val += pow(2, i) * int(bit_array[i])
    return val


def to_binary_arr(value, array_length):
    binary_arr = [False] * array_length
    for i in range(array_length):
        b = value % 2
        value = value // 2
        binary_arr[i] = bool(b)
    return binary_arr

def calBin(val, num):
    return to_binary_arr(val, num)


def calBinNoLength(v):
    val = []
    while v != 0:
        b = v % 2
        v = v // 2
        val.append(b)
    return val


class Simulator(XMLExpVisitor):
    # x, y, z, env : ChainMap{ x: n, y : m, z : v} , n m v are nat numbers 100, 100, 100, eg {x : 128}
    # st state map, {x : v1, y : v2 , z : v3}, eg {x : v1}: v1,
    # st {x : v1} --> Coq_nval case: v1 is a ChainMap of Coq_nval
    # v1 --> 128 length array v1: {0 : Coq_nval, 1 : Coq_nval, 2 : Coq_nval, ...., 127 : Coq_nval}, 2^128
    # x --> v1 --> cal(v1) --> integer
    # Coq_nval(b,r) b == |0> | |1>, r == e^(2 pi i * 1 / n), r = 0 Coq_nval(b, 0)
    # x -> v1 ----> run simulator -----> v2 ---> calInt(v2,128) == (x + 2^10) % 2^128
    def __init__(self, state: dict, env: dict):
        self.st = state
        self.env = env
        # self.rmax = rmax rmax is M_find(x,env), a map from var to int

    def visitProgram(self, ctx):

        i = 0
        while ctx.exp(i) is not None:
            ctx.exp(i).accept(self)
            i += 1

    def visitExp(self, ctx):
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
        f = ctx.idexp(0).Identifier().accept(self)
        self.st.update({f: ctx})
        #print("f", ctx)
        # ctx.exp().accept(self)

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
        x = ctx.idexp().Identifier().accept(self)
        value = self.st.get(x)
        #print("value match", value)
        i = 0
        while ctx.exppair(i) is not None:
            if ctx.exppair(i).vexp().OP() is None:
                va = ctx.exppair(i).vexp().accept(self)
                if value == va:
                    ctx.exppair(i).program().accept(self)
                    return
            else:
                y = ctx.exppair(i).vexp().vexp(0).idexp().Identifier().accept(self)
                tmpv = self.st.get(y)
                self.st.update({y: int(value) - 1})
                ctx.exppair(i).program().accept(self)
                if tmpv is not None:
                    self.st.update({y:tmpv})
            i += 1

    def visitAppexp(self, ctx: XMLExpParser.AppexpContext):
        ctxa = ctx.idexp().accept(self)
        #print("here",ctx.idexp().Identifier())
        #print("herea",ctxa.idexp(0).Identifier())
        #ctxa = self.st.get(f)
        i = 0
        tmpv = dict()
        tmpa = dict()
        while ctxa.idexp(i+1) is not None:
            x = ctxa.idexp(i+1).Identifier().accept(self)
            #print("var",ctxa.idexp(i+1).Identifier())
            v = ctx.vexp(i).accept(self)
            #print("val",v)
            tmpv.update({x:self.st.get(x)})
            tmpa.update({x:v})
            i += 1

        while len(tmpa) != 0:
            xv,re = tmpa.popitem()
            self.st.update({xv: re})
            #print("vara",xv,"vala",re)

        ctxa.program().accept(self)
        while len(tmpv) != 0:
            xv,re = tmpv.popitem()
            if re is not None:
                self.st.update({xv:re})
            else:
                self.st.pop(xv, None)

            #print ("var",xv)
            #print("val",re)

    def visitIfexp(self, ctx: XMLExpParser.IfexpContext):
        v = ctx.vexp().accept(self)
        if v == 1:
            ctx.exp(0).accept(self)
        else:
            ctx.exp(1).accept(self)

    def get_state(self):
        return self.st

    def sr_rotate(self, x, n):
        val = self.st.get(x)[0]
        if isinstance(val, CoqQVal):
            self.st.get(x)[0] = CoqQVal(val.r1, (val.r2 + pow(2, val.getNum() - n - 1)) % pow(2, val.getNum()), val.getRest(), val.getNum())

    def srr_rotate(self, x, n):
        val = self.st.get(x)
        if isinstance(val, CoqQVal):
            self.st.get(x)[0] = CoqQVal(val.r1, natminusmod(val.r2, pow(2, val.getNum() - n - 1),
                                                           pow(2, val.getNum())), val.getRest(), val.getNum())

    # should do nothing
    def visitSkipexp(self, ctx: XMLExpParser.SkipexpContext):
        return

    # X posi, changed the following for an example
    def visitXexp(self, ctx: XMLExpParser.XexpContext):
        x = ctx.idexp().accept(self)[0]
        p = ctx.vexp().accept(self)  # this will pass the visitor to the child of ctx
        exchange(x, p)

    # we will first get the position in st and check if the state is 0 or 1,
    # then decide if we go to recursively call ctx.exp
    def visitCUexp(self, ctx: XMLExpParser.CuexpContext):
        x = ctx.idexp().accept(self)[0]
        p = ctx.vexp().accept(self)  # this will pass the visitor to the child of ctx
        if x.getBits()[p]:
            ctx.program().accept(self)
        else:
            return  # do nothing

    # my previous rz parsing is wrong
    # it should be RZ q posi
    # def visitRzexp(self, ctx: XMLExpParser.RzexpContext):
    #     q = int(ctx.vexp(0).accept(self))  # I guess then you need to define vexp
    #     # we can first define the var and integer case
    # I guess Identifier and int are all terminal
    # does it means that we do not need to define anything?
    #     x = ctx.idexp().accept(self)
    #    p = ctx.vexp(1).accept(self)  # this will pass the visitor to the child of ctx
    #   if q >= 0:
    #      self.st.update({x: times_rotate(self.st.get(x), q, self.env.get(x))})
    #  else:
    #     self.st.update({x: times_r_rotate(self.st.get(x), abs(q), self.env.get(x))})

    # SR n x, now variables are all string, are this OK?
    def visitSrexp(self, ctx: XMLExpParser.SrexpContext):
        n = int(ctx.vexp().accept(self))
        x = ctx.idexp().Identifier().accept(self)
        if n >= 0:
            self.sr_rotate(x, n)
        else:
            self.srr_rotate(x, abs(n))

    def lshift(self, x, n):
        if n == 0:
            return

        tmp = self.st.get(x)[0].getBits()
        tmpv = tmp[0]
        for i in range(n - 1):
            tmp[i] = tmp[i + 1]
        tmp[n - 1] = tmpv
        self.st.get(x)[0] = CoqNVal(tmp, self.st.get(x)[0].getPhase())

    def visitLshiftexp(self, ctx: XMLExpParser.LshiftexpContext):
        x = ctx.idexp().Identifier().accept(self)
        self.lshift(x, self.env.get(x))

    def rshift(self, x, n):
        if n == 0:
            return

        tmp = self.st.get(x)[0].getBits()
        tmpv = tmp[n - 1]
        for i in range(n - 1, -1, -1):
            tmp[i] = tmp[i - 1]

        tmp[0] = tmpv
        self.st.get(x)[0] = CoqNVal(tmp, self.st.get(x)[0].getPhase())

    def visitRshiftexp(self, ctx: XMLExpParser.RshiftexpContext):
        x = ctx.idexp().Identifier().accept(self)
        self.rshift(x, self.env.get(x))

    def reverse(self, x, n):
        if n == 0:
            return

        size = n
        tmp = self.st.get(x)[0].getBits()
        tmpa = []
        for i in range(n):
            tmpa.append(tmp[size - i])
        self.st.get(x)[0] = CoqNVal(tmp, self.st.get(x)[0].getPhase())

    def visitRevexp(self, ctx: XMLExpParser.RevexpContext):
        x = ctx.idexp().Identifier().accept(self)
        self.reverse(x, self.env.get(x))

    def turn_qft(self, x, n):
        val = self.st.get(x)[0]
        r1 = val.getPhase()
        r2 = 0
        if isinstance(val, CoqNVal):
            for i in range(n):
                r2 = (r2 + pow(2, i) * int(val.getBits()[i])) % pow(2, n)
        result = val.getBits()[n:]
        #print("val", result)
        self.st.get(x)[0] = CoqQVal(r1, r2, result, n)

        # actually, we need to change the QFT function
        # the following QFT is only for full QFT, we did not have the case for AQFT

    def visitQftexp(self, ctx: XMLExpParser.QftexpContext):
        x = ctx.idexp().Identifier().accept(self)
        b = int(ctx.vexp().accept(self))
        self.turn_qft(x, self.env.get(x) - b)
        #print("qft_exp val",self.env.get(x)-b)
        #print("qft_exp x",self.st.get(x))
        # TODO implement

    def turn_rqft(self, x):
        val = self.st.get(x)[0]
        n = val.getNum()
        if isinstance(val, CoqQVal):
            tmp = val.getLocal()
            tov = [False] * n
            for i in range(n):
                b = tmp % 2
                tmp = tmp // 2
                tov[i] = bool(b)
            result = tov + val.getRest()
            self.st.get(x)[0] = CoqNVal(result, val.getPhase())

    def visitRqftexp(self, ctx: XMLExpParser.RqftexpContext):
        x = ctx.idexp().Identifier().accept(self)
        self.turn_rqft(x)
        #print("rqftexp end")

    def visit(self, ctx: ParserRuleContext):
        if ctx.getChildCount() > 0:
            return self.visitChildren(ctx)
        else:
            return self.visitTerminal(ctx)

    def visitIdexp(self, ctx: XMLExpParser.IdexpContext):
        # print("idexp var",ctx.Identifier().accept(self))
        # print("idexp val",self.get_state().get(ctx.Identifier().accept(self)))
        return self.get_state().get(ctx.Identifier().accept(self))

        # Visit a parse tree produced by XMLExpParser#vexp.

    def visitVexp(self, ctx: XMLExpParser.VexpContext):
        if ctx.op() is None:
            #print("vexp none op")
            if ctx.numexp() is not None:
                return ctx.numexp().accept(self)
            elif ctx.idexp() is not None:
                x = ctx.idexp().accept(self)
                return x
            elif ctx.boolexp() is not None:
                if ctx.boolexp().TrueLiteral() is not None:
                    return 1
                else:
                    return 0
        else:
            #print("here")
            #print("op",ctx.op())
            x = ctx.vexp(0).accept(self)
            y = ctx.vexp(1).accept(self)
            #print("val",y)
            if ctx.op().Plus() is not None:
                return x + y
            elif ctx.op().Minus() is not None:
                return x - y
            elif ctx.op().Times() is not None:
                return x * y
            elif ctx.op().Div() is not None:
                return x // y
            elif ctx.op().GNum() is not None:
                #print("here1")
                tmp = (calBinNoLength(x))
                #print("val",tmp)
                #print("val",tmp)
                #print("vala", y)
                if y < len(tmp):
                    #print("val",tmp[y])
                    return int(tmp[y])
        return 0

    #def visitIda(self, ctx: XMLExpParser.IdaContext):
    #    return ctx.Identifier().getText()

        # the only thing that matters will be 48 and 47

    def visitTerminal(self, node):
        # print("terminal")
        if node.getSymbol().type == XMLExpParser.Identifier:
            return node.getText()
        if node.getSymbol().type == XMLExpParser.Number:
            return int(node.getText())
        return "None"
