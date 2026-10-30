"""Fixed exact stationary tail with vanishing descendants (lane c1-n1, candidate C design).

For branch j >= 1 and angular block m (m <= 10 j + 9), the leading potential moment must equal the exact stationary C_j(2m) and the
descendant moments q = 1..Q-1 must vanish.  With Q radial functions  R^(p_j - m) H_m t^w P_n(2t-1), n = 0..Q-1 (w = max(5-m, 0)),
the Q x Q moment matrix M[q][n] = sum_h L_n[h] binom(p_j - m - w - h, q) is invertible (generic p_j) and the block is DETERMINED:
coefficients = M^{-1} (C_j(2m), 0, ..., 0).  The sum over all such blocks is one fixed potential chi_tail (exact rational coefficients).
Branch 0 keeps the free 860 functions (its moments are constrained in the optimizer).  Blocks (j <= 3, m <= 9) also keep the free T1
functions; for them the Q moment conditions are imposed as linear constraints on the free coefficients (the fixed tail functions of those
blocks are omitted: their role is played by the constrained free functions).
Inner functions with vanishing moments q <= Q-1 by construction: R^(p_j - m) H_m t^w (1-t)^Q P_n(2t-1) = sum_i C(Q,i)(-1)^i t^(w+i) P_n:
represented as generators with spec ('legq', w, n, Q) expanding to Q+1 'leg' terms.
"""
import math
import flint
from gmpy2 import mpq
import ipm_exact as X

def legendre_monomial(n): return X.legendre_monomial(n)

def block_moment_matrix(c, j, m, Q):
    p = X.p_branch(c, j); w = max(5-m, 0)
    M = [[mpq(0)]*Q for _ in range(Q)]
    for n in range(Q):
        L = legendre_monomial(n)
        for q in range(Q):
            M[q][n] = sum((L[h]*X.binom_q(p-m-w-h, q) for h in range(n+1)), mpq(0))
    return M, w

def solve_block(c, j, m, Q, target):
    """exact coefficients of the Q Legendre functions giving moments (target, 0, ..., 0)"""
    M, w = block_moment_matrix(c, j, m, Q)
    A = flint.fmpq_mat(Q, Q); b = flint.fmpq_mat(Q, 1)
    for q in range(Q):
        for n in range(Q):
            v = M[q][n]; A[q, n] = flint.fmpq(int(v.numerator), int(v.denominator))
    b[0, 0] = flint.fmpq(int(target.numerator), int(target.denominator))
    sol = A.solve(b)
    coefs = [mpq(int(sol[n, 0].p), int(sol[n, 0].q)) for n in range(Q)]
    # verify exactly
    for q in range(Q):
        tot = sum((M[q][n]*coefs[n] for n in range(Q)), mpq(0))
        assert tot == (target if q == 0 else 0), ('block moment check failed', j, m, q)
    return [({'m': m, 'j': j, 'spec': ['leg', w, n]}, coefs[n]) for n in range(Q)]

def fixed_tail(c, stationary_C, jmax, Q, skip_blocks=()):
    """list of (gen dict, exact coef) for all blocks (j = 1..jmax, m <= 10j+9) not in skip_blocks; stationary_C[j] = cos dict (harmonic 2m -> C)"""
    out = []
    for j in range(1, jmax+1):
        Cj = stationary_C[j]
        for m in range(0, 10*j+10):
            if (j, m) in skip_blocks: continue
            target = Cj.get(2*m, mpq(0))
            out.extend(solve_block(c, j, m, Q, target))
    return out

def expand_legq(g):
    """('legq', w, n, Q) -> list of (gen dict with 'leg' spec, integer factor)"""
    spec = g['spec']
    if spec[0] != 'legq': return [(g, 1)]
    w, n, Q = int(spec[1]), int(spec[2]), int(spec[3])
    out = []
    for i in range(Q+1):
        out.append((dict(g, spec=['leg', w+i, n]), (-1)**i*math.comb(Q, i)))
    return out
