class rz_val:
    pass

class coq_val:
    def __init__(self, b, r):
        self.b = b
        self.r = r

def addto(r, n, rmax):
    return ((r + (rmax - n)) % (rmax * rmax))

def addto_n(r, n, rmax):
    return (((r + rmax) - (rmax - n)) % (rmax * rmax))

def get_state(p, f):
    if p in f:
        return f[p]
    else:
        return coq_val(False, 0)

def exchange(v):
    if isinstance(v, coq_val):
        return coq_val(not v.b, v.r)
    else:
        return v

def get_cua(v):
    if isinstance(v, coq_val):
        return v.b
    else:
        return False

def get_cus(n, f, x, i):
    if i < n:
        v = get_state((x, i), f)
        if isinstance(v, coq_val):
            return v.b
        else:
            return False
    else:
        return allfalse(i)

def get_r(v):
    if isinstance(v, coq_val):
        return v.r
    else:
        return v

def rotate(r, q, rmax):
    return addto(r, q, rmax)

def times_rotate(v, q, rmax):
    if isinstance(v, coq_val):
        if v.b:
            return coq_val(v.b, rotate(v.r, q, rmax))
        else:
            return coq_val(v.b, v.r)
    else:
        return v

def r_rotate(r, q, rmax):
    return addto_n(r, q, rmax)

def times_r_rotate(v, q, rmax):
    if isinstance(v, coq_val):
        if v.b:
            return coq_val(v.b, r_rotate(v.r, q, rmax))
        else:
            return coq_val(v.b, v.r)
    else:
        return v

def sr_rotate_prime(st, x, n, size, rmax):
    def fO():
        return st

    def fS(m):
        return sr_rotate_prime(
            M.add((x, m), times_rotate(get_state((x, m), st), max(0, size - m), rmax), st), x, m, size, rmax
        )

    return fO() if n == 0 else fS(max(0, n - 1))

def sr_rotate(st, x, n, rmax):
    return sr_rotate_prime(st, x, n + 1, n + 1, rmax)

def srr_rotate_prime(st, x, n, size, rmax):
    def fO():
        return st

    def fS(m):
        return srr_rotate_prime(
            M.add((x, m), times_r_rotate(get_state((x, m), st), max(0, size - m), rmax), st), x, m, size, rmax
        )

    return fO() if n == 0 else fS(max(0, n - 1))

def srr_rotate(st, x, n, rmax):
    return srr_rotate_prime(st, x, n + 1, n + 1, rmax)

def lshift_prime(n, size, f, x):
    def fO():
        return M.add((x, 0), get_state((x, size), f), f)

    def fS(m):
        return M.add((x, n), get_state((x, m), f), lshift_prime(m, size, f, x))

    return fO() if n == 0 else fS(max(0, n - 1))

def lshift(f, x, n):
    return lshift_prime(n if n > 0 else 0, n + 1 if n > 0 else 1, f, x)

def rshift_prime(n, size, f, x):
    def fO():
        return M.add((x, size), get_state((x, 0), f), f)

    def fS(m):
        return M.add((x, m), get_state((x, n), f), rshift_prime(m, size, f, x))

    return fO() if n == 0 else fS(max(0, n - 1))

def rshift(f, x, n):
    return rshift_prime(n if n > 0 else 0, n + 1 if n > 0 else 1, f, x)

def reverse_prime(f, x, n, i, f_prime):
    def fO():
        return f_prime

    def fS(i_prime):
        return reverse_prime(
            f, x, n, i_prime, M.add((x, i_prime), get_state((x, n - i), f), f_prime)
        )

    return fO() if i == 0 else fS(max(0, i - 1))

def reverse(f, x, n):
    return reverse_prime(f, x, n, n, f)

def up_h(v, rmax):
    if isinstance(v, coq_val):
        if v.b:
            return Coq_qval(v.r, rotate(0, 1, rmax))
        else:
            return Coq_qval(v.r, 0)
    else:
        return Coq_nval((rmax ** 2) <= v.r, v.r)

def assign_h(f, x, n, i, rmax):
    def fO():
        return f

    def fS(m):
        return assign_h(
            M.add((x, n + m), up_h(get_state((x, n + m), f), rmax), f), x, n, m, rmax
        )

    return fO() if i == 0 else fS(max(0, i - 1))

def up_qft(v, f):
    if isinstance(v, Coq_nval):
        return Coq_qval(v.r, f)
    else:
        return v

def a_nat2fb_prime(f, n, acc):
    def fO():
        return acc

    def fS(m):
        return a_nat2fb_prime(f, m, acc + (f(m) * ((succ(succ(0))) ** m)))

    return fO() if n == 0 else fS(max(0, n - 1))

def a_nat2fb(f, n):
    return a_nat2fb_prime(f, n, 0)

def assign_r(f, x, r, n, size, rmax):
    def fO():
        return f

    def fS(m):
        return assign_r(
            M.add((x, max(0, size - n)), up_qft(get_state((x, max(0, size - n)), f), r), f),
            x,
            (r * (succ(succ(0)))) % ((succ(succ(0))) ** rmax),
            m,
            size,
            rmax,
        )

    return fO() if n == 0 else fS(max(0, n - 1))

def turn_qft(f, x, n, rmax):
    return assign_h(
        assign_r(
            f, x,
            ((succ(succ(0))) ** max(0, rmax - n)) * a_nat2fb(fbrev(n, get_cus(n, f, x)), n),
            n, n, rmax
        ),
        x, n, max(0, rmax - n), rmax
    )

def assign_seq(f, x, vals, size, n):
    def fO():
        return f

    def fS(m):
        return assign_seq(
            M.add((x, max(0, size - n)), Coq_nval((vals(size - n)), get_r(get_state((x, max(0, size - n)), f)))), f,
            x, vals, size, m
        )

    return fO() if n == 0 else fS(max(0, n - 1))

def get_r_qft(f, x, n, rmax):
    state_x_0 = get_state((x, 0), f)
    if isinstance(state_x_0, Coq_nval):
        return allfalse()
    else:
        g = state_x_0.r
        return fbrev(n, nat2fb(g // ((succ(succ(0))) ** max(0, rmax - n))))

def turn_rqft(st, x, n, rmax):
    return assign_h(assign_seq(st, x, get_r_qft(st, x, n, rmax), n, rmax), x, n, max(0, rmax - n), rmax)

def exp_sem(env, rmax, e, st):
    if e == 'SKIP':
        return st
    elif e == 'X':
        return M.add(e.p, exchange(get_state(e.p, st)), st)
    elif e == 'CU':
        state_p = get_state(e.p, st)
        if get_cua(state_p):
            return exp_sem(env, rmax, e.e_, st)
        else:
            return st
    elif e == 'RZ':
        return M.add(e.p, times_rotate(get_state(e.p, st), e.q, rmax), st)
    elif e == 'RRZ':
        return M.add(e.p, times_r_rotate(get_state(e.p, st), e.q, rmax), st)
    elif e == 'SR':
        return sr_rotate(st, e.x, e.n, rmax)
    elif e == 'SRR':
        return srr_rotate(st, e.x, e.n, rmax)
    elif e == 'Lshift':
        return lshift(st, e.x, env(e.x))
    elif e == 'Rshift':
        return rshift(st, e.x, env(e.x))
    elif e == 'Rev':
        return reverse(st, e.x, env(e.x))
    elif e == 'QFT':
        return turn_qft(st, e.x, env(e.x), rmax)
    elif e == 'RQFT':
        return turn_rqft(st, e.x, env(e.x), rmax)
    elif e == 'Seq':
        return exp_sem(env, rmax, e.e2, exp_sem(env, rmax, e.e1, st))
