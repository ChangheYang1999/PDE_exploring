"""Frozen point sets for the T2.6 gates and the SPEC v9 development check (exact binary64 coordinates)."""
import math
def _xy(r, th):
    x = r*math.cos(th); y = r*math.sin(th)
    if th == math.pi/2: x = 0.
    if th == 0.: y = 0.
    return x, y
# g2_v3 T2.6b far points (9) and T2.6c finite points (17): bands by r: origin r < 0.02; b1 [0.02,0.1); b2 [0.1,1); b3 [1,10); b4 [10,1e3); b5 [1e3, e^16]
FAR = [('e24', *_xy(math.exp(24), th)) for th in (0., .3, math.pi/2)]+[('e32', *_xy(math.exp(32), th)) for th in (0., .3, math.pi/2)]+[('e44', *_xy(math.exp(44), th)) for th in (0., .3, math.pi/2)]
_BANDS = [('origin', [(.004, .9), (.019, .3)]), ('b1', [(.03, 0.), (.06, .9), (.095, math.pi/2)]), ('b2', [(.2, 0.), (.5, .9), (.9, math.pi/2)]), ('b3', [(1.5, 0.), (3., .9), (8., math.pi/2)]),
          ('b4', [(30., 0.), (300., .9), (900., math.pi/2)]), ('b5', [(3e3, 0.), (1e5, .9), (3e6, math.pi/2)])]
FINITE = [(name, *_xy(r, th)) for name, rows in _BANDS for (r, th) in rows]
# SPEC v9.2: T2.6c needs points on both sides of r = 1 (the R_f switch): added to band b2 / b3
FINITE_V92 = FINITE+[('b2', *_xy(.999, .4)), ('b3', *_xy(1.001, .4))]
# the verifier's 23 diagnostic points (c4-ver evidence/basis860/residual_jacobian/production_manifest.json, read as data), bands 0..6 by r and e24/e32/e44
VERIFIER_23 = [(b, float.fromhex(xh), float.fromhex(yh)) for (b, xh, yh) in [
    ('0', '0x1.0624dd2f1a9fcp-10', '0x0.0p+0'), ('0', '0x1.223ad26d970a3p-6', '0x1.c2471aa0587a7p-8'), ('1', '0x0.0p+0', '0x1.5810624dd2f1bp-6'), ('1', '0x1.538a38837bd04p-4', '0x1.1f1c4040ac557p-5'),
    ('2', '0x1.c28f5c28f5c29p-4', '0x0.0p+0'), ('2', '0x1.9463d9f52572fp-1', '0x1.b9d6acf105225p-2'), ('3', '0x0.0p+0', '0x1.028f5c28f5c29p+0'), ('3', '0x1.b88c91cf39145p+2', '0x1.7311c366edcefp+2'),
    ('4', '0x1.6000000000000p+3', '0x0.0p+0'), ('4', '0x1.dd30c99c0e3bdp+9', '0x1.2739850d2eb27p+8'), ('5', '0x0.0p+0', '0x1.f480000000000p+9'), ('5', '0x1.5c44c7a864d61p+21', '0x1.859d3e6a1c3b9p+20'),
    ('6', '0x1.2d5060448e3b2p+23', '0x0.0p+0'), ('6', '0x1.f61613d9bd3abp+33', '0x1.af8eb95edef98p+33'),
    ('e24', '0x1.8ab7fb5475fb7p+34', '0x0.0p+0'), ('e24', '0x1.7916d2f9e2d1dp+34', '0x1.d296e1be16bbfp+32'), ('e24', '0x0.0p+0', '0x1.8ab7fb5475fb7p+34'),
    ('e32', '0x1.1f43fcc4b662cp+46', '0x0.0p+0'), ('e32', '0x1.126f6ef0123ccp+46', '0x1.53923585960ecp+44'), ('e32', '0x0.0p+0', '0x1.1f43fcc4b662cp+46'),
    ('e44', '0x1.64b41c6d37832p+63', '0x0.0p+0'), ('e44', '0x1.54c59ce885ac7p+63', '0x1.a5a706269150ep+61'), ('e44', '0x0.0p+0', '0x1.64b41c6d37832p+63')]]
GATED_FAR = {'e24'}        # e32, e44 reported as diagnostics
# T2.7H design points: one generic-angle point per band (7 bands) plus r = 0.0199 and 0.0201 on both sides of the origin-series radius
T27H_BANDS = [(0, .02), (.02, .1), (.1, 1), (1, 10), (10, 1e3), (1e3, math.exp(16)), (math.exp(16), 2.6e10)]
def t27h_points():
    pts = [(0, .0199*math.cos(.7), .0199*math.sin(.7)), (1, .0201*math.cos(.7), .0201*math.sin(.7))]
    for b, (lo, hi) in enumerate(T27H_BANDS):
        r = math.sqrt(max(lo, 1e-3)*hi) if b else .011; pts.append((b, r*math.cos(.9), r*math.sin(.9)))
    return pts
T27H_CL = [1.02, 2.0, 3.0, 10.0, 2*(1-2**-20), 2*(1+2**-20), 3*(1-2**-20), 3*(1+2**-20)]
def band_of(r):
    return 'origin' if r < .02 else 'b1' if r < .1 else 'b2' if r < 1 else 'b3' if r < 10 else 'b4' if r < 1e3 else 'b5'
