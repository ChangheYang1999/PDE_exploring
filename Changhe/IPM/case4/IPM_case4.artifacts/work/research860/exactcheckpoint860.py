"""Exact rational checkpoint (lead ruling D3 (f), 2026-10-24T09:44Z): the far-field engine and the canonical export take the EXACT rationals of a checkpoint
(P, high, c_l binary64), not a rounded array. a_000 = (1 - c_l - sum_{k>=1} s_k a_k)/s_0 with the strains s_k rational in c_l (basis860.strain_values on a Fraction c_l);
the T1 map uses the frozen N_n as exact Fractions of their binary64 values and the integer Legendre factors (basis860.legendre_monomial). Records the sha256 of a canonical
'numerator/denominator' serialization of the 860 coefficients."""
import hashlib
from fractions import Fraction
import numpy as np
import basis860 as B

def exact_canonical(P, high):
    """P: 60 binary64 raw chart coordinates [c_l, a_1..a_59]; high: 800 binary64 internal high coordinates. Returns (a: list of 860 Fractions in canonical order, record)."""
    P = np.asarray(P, float); high = np.asarray(high, float)
    if P.shape != (B.NLOW,) or high.shape != (B.NHIGH,): raise ValueError('expected 60 raw chart coordinates and 800 high coordinates')
    c = Fraction(float(P[0])); s, _ = B.strain_values(c)
    low = [Fraction(float(v)) for v in P]
    low[0] = (1-c-sum((s[k]*low[k] for k in range(1, B.NLOW)), Fraction(0)))/s[0]
    a = [Fraction(0)]*B.NRAW
    for value, (m, k, j) in zip(low, B.LOW): a[B.canonical_index(j, m, k)] += value
    for value, (m, n, j) in zip(high, B.HIGH):
        v = Fraction(float(value))
        if v:
            v *= Fraction(float(B.NN[n])); vm = max(5, m)
            for h, L in enumerate(B.legendre_monomial(n)): a[B.canonical_index(j, m, vm+h)] += v*int(L)
    ser = ('cl %d/%d\n' % (c.numerator, c.denominator)+'\n'.join('%d/%d' % (x.numerator, x.denominator) for x in a)).encode()          # SPEC v9.17: the serialization binds c_l
    raw = np.asarray(P, '<f8').tobytes()+np.asarray(high, '<f8').tobytes()
    rec = {'input_exact_for_checkpoint': True, 'input_exact_for_checkpoint_method': 'Fraction(c_l) and Fraction of every binary64 P and high coordinate; a_000 = (1 - c_l - sum_k s_k a_k)/s_0 in Fractions (strains rational in c_l); N_n as exact Fractions of the frozen binary64 constants; integer Legendre factors; T1 map exact (SPEC v9.17)',
           'cl_exact': '%d/%d' % (c.numerator, c.denominator), 'a000_exact': '%d/%d' % (low[0].numerator, low[0].denominator), 'a000_float': float(low[0]),
           'canonical_serialization_sha256': hashlib.sha256(ser).hexdigest(), 'serialization': "first line 'cl num/den' (binary64 c_l as an exact rational), then the newline-joined numerator/denominator of the 860 canonical coefficients in canonical order I(j,m,k)",
           'binary64_inputs_sha256': hashlib.sha256(raw).hexdigest(), 'binary64_inputs_serialization': 'little-endian float64 bytes of P (60, c_l first) followed by high (800)'}
    return a, rec
