from ExpParser import *


class simulator:
    def rec(self, exp_sem, env, rmax, e ,st):
        if isinstance(e, SkipexpContext):
            return st
        elif isinstance(e, xgexp):
