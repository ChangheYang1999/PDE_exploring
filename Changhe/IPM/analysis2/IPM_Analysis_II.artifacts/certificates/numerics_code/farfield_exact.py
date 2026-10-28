"""Exact far-field (r > 1) expansion of an 860-generator case-4 state, in rational arithmetic.

For r > 1:  r^{2k} (1+r^2)^{p_j-k} = r^{2 p_j} (1 + r^{-2})^{p_j-k} = sum_{q>=0} C(p_j-k, q) r^{2 p_j - 2q}.
Potential sector (j,q): r^{s} sum_m C_{m,j,q} cos(2m theta), s = 2 p_j - 2 q = 3 + alpha_{j,q}, alpha_{j,q} = gamma - j lambda - 2q,
C_{m,j,q} = sum_k a_{mkj} C(p_j - k, q).
Rules (own derivation, polar coordinates), for a potential term C r^s cos(n theta):
  rho = -d_y Lap:  -C (s^2-n^2)(s-2-n)/2 sin((n+1)theta) + C (s^2-n^2)(s-2+n)/2 sin((n-1)theta), exponent s-3;
  psi = d_x d_y:   +C (s-n)(s-n-2)/4 sin((n+2)theta) - C (s+n)(s+n-2)/4 sin((n-2)theta), exponent s-2.
Residual F = (cl X + U).grad rho - rho with U = (-psi_y, psi_x):  X.grad = r d_r;  U.grad rho = (psi_r rho_theta - psi_theta rho_r)/r.
For psi-term r^sigma Phi(theta), rho-term r^alpha G(theta): U.grad rho = r^{sigma+alpha-2} [sigma Phi G' - alpha Phi' G].
Density sectors: rho_{j,q} = r^{alpha_{j,q}} G_{j,q}(theta); stream sectors psi_{j,q} = r^{alpha_{j,q}+1} Phi_{j,q}(theta).
Residual sector E_{h,q} at exponent gamma - h lambda - 2q: (cl alpha_{h,q} - 1) G_{h,q} [h<=3] + sum_{i+jj+1=h, u+v=q} [(alpha_{i,u}+1) Phi_{i,u} G'_{jj,v} - alpha_{jj,v} Phi'_{i,u} G_{jj,v}].
Sine series are dicts {k: coefficient} over positive k (sin(-k) = -sin(k) folded).
"""
import json, math, sys
from fractions import Fraction as Fr

def canon(j, m, k): return 215*j + 26*m - m*(m-1)//2 + (k-m)

def binom_fr(p, q):
    out = Fr(1)
    for i in range(q): out = out*(p-i)/(i+1)
    return out

def sadd(S, k, v):
    if v == 0: return
    if k < 0: k, v = -k, -v
    if k == 0: return
    S[k] = S.get(k, 0) + v
    if S[k] == 0: del S[k]

def ssum(*Ss):
    out = {}
    for S in Ss:
        for k, v in S.items(): sadd(out, k, v)
    return out

def sscale(S, f): return {k: f*v for k, v in S.items()} if f != 0 else {}

def dtheta_sin(S):
    """d/dtheta of sum s_k sin(k theta) = sum k s_k cos(k theta): cosine dict."""
    return {k: k*v for k, v in S.items()}

def sin_times_cos(S, C):
    """(sum s_a sin a)(sum c_b cos b) = sum s_a c_b [sin(a+b) + sin(a-b)]/2."""
    out = {}
    for a, sa in S.items():
        for b, cb in C.items():
            sadd(out, a+b, sa*cb/2); sadd(out, a-b, sa*cb/2)
    return out

def density_rule(C, s):
    G = {}
    for n, c in C.items():
        sadd(G, n+1, -c*(s*s-n*n)*(s-2-n)/2); sadd(G, n-1, c*(s*s-n*n)*(s-2+n)/2)
    return G

def stream_rule(C, s):
    P = {}
    for n, c in C.items():
        sadd(P, n+2, c*(s-n)*(s-n-2)/4); sadd(P, n-2, -c*(s+n)*(s+n-2)/4)
    return P

def norm2_quarter(S):
    """||sum s_k sin k theta||^2_{L2(0,pi/2)} for odd k = (pi/4) sum s_k^2 -> returns sum s_k^2 /4 (times pi)."""
    return sum((v*v for v in S.values()), Fr(0))/4

def expand(cl, a, qmax=3, hmax=7):
    g = Fr(1)/cl; lam = 1-g
    p = [(3+g-j*lam)/2 for j in range(4)]
    def alpha(h, q): return g - h*lam - 2*q
    C = {}; G = {}; Phi = {}
    for j in range(4):
        for q in range(qmax+1):
            Cj = {}
            for m in range(10):
                v = sum((a[canon(j, m, k)]*binom_fr(p[j]-k, q) for k in range(m, 26)), Fr(0))
                if v != 0: Cj[2*m] = v
            s = 2*p[j]-2*q
            C[(j, q)] = Cj; G[(j, q)] = density_rule(Cj, s); Phi[(j, q)] = stream_rule(Cj, s)
    E = {}
    for h in range(hmax+1):
        for q in range(qmax+1):
            terms = []
            if h <= 3: terms.append(sscale(G[(h, q)], cl*alpha(h, q)-1))
            for i in range(4):
                jj = h-1-i
                if not (0 <= jj <= 3): continue
                for u in range(q+1):
                    v = q-u
                    ai = alpha(i, u); aj = alpha(jj, v)
                    # (ai+1) Phi G' - aj Phi' G ; Phi, G sine series; G' and Phi' cosine series
                    terms.append(sscale(sin_times_cos(Phi[(i, u)], dtheta_sin(G[(jj, v)])), ai+1))
                    terms.append(sscale(sin_times_cos(G[(jj, v)], dtheta_sin(Phi[(i, u)])), -aj))
            E[(h, q)] = ssum(*terms)
    return {'gamma': g, 'lambda': lam, 'p': p, 'alpha': alpha, 'C': C, 'G': G, 'Phi': Phi, 'E': E}

def fr_str(v): return '%d/%d' % (v.numerator, v.denominator)
def sdict_out(S): return {str(k): {'exact': fr_str(v), 'float': float(v)} for k, v in sorted(S.items())}

if __name__ == '__main__':
    d = json.load(open(sys.argv[1]))
    cl = Fr(d['cl']); a = [Fr(s) for s in d['a_canonical']]
    qmax = 3
    X = expand(cl, a, qmax=qmax)
    g, lam, alpha = X['gamma'], X['lambda'], X['alpha']
    print('cl =', float(cl), ' gamma =', float(g), ' lambda =', float(lam), ' 2gamma-1 =', float(2*g-1), fr_str(2*g-1))
    # leading density profile Theta_0 = G_{0,0} (r^gamma), stream Phi_{0,0}
    G00 = X['G'][(0, 0)]
    print('Theta_0 = G_{0,0} (sine coefficients, odd k):')
    for k, v in sorted(G00.items()): print('   k=%2d  %.17g' % (k, float(v)))
    print('||Theta_0||_{L2(0,pi/2)}^2/pi =', float(norm2_quarter(G00)), ' ||Theta_0||_{L2(0,2pi)} =', math.sqrt(float(norm2_quarter(G00))*4*math.pi))
    # exponent groups
    groups = {}
    for (h, q), S in X['E'].items():
        ex = alpha(h, q); groups.setdefault(ex, []).append((h, q))
    print('Residual sectors by exponent (nonzero):')
    omitted = alpha(0, qmax+1)
    for ex in sorted(groups, reverse=True):
        S = ssum(*[X['E'][hq] for hq in groups[ex]])
        if not S: 
            print('  exp %+.6f  members %s  EXACT ZERO' % (float(ex), groups[ex])); continue
        n2 = norm2_quarter(S)
        print('  exp %+.6f  members %s  ||E||_{L2(0,pi/2)} = %.10g  max harmonic %d' % (float(ex), groups[ex], math.sqrt(float(n2)*math.pi), max(S)))
    print('largest omitted exponent gamma - 2(qmax+1) =', float(omitted))
    for N in (1, 2, 3):
        S = X['E'][(N, 0)]
        n2 = norm2_quarter(S); rep = sum((v*v for k, v in S.items() if k <= 19), Fr(0))/4; unr = sum((v*v for k, v in S.items() if k > 19), Fr(0))/4
        print('E_%d: ||E||=%.10g  exponent %.7f  fraction above harmonic 19 = %.4f %%  max harmonic %d' % (N, math.sqrt(float(n2)*math.pi), float(alpha(N, 0)), 100*math.sqrt(float(unr/(rep+unr))), max(S)))
    out = {'cl': d['cl'], 'gamma': fr_str(g), 'lambda': fr_str(lam), 'p': [fr_str(v) for v in X['p']], 'qmax': qmax,
           'density_sectors_G': {'%d,%d' % k: {'exponent': fr_str(alpha(*k)), 'series': sdict_out(S)} for k, S in X['G'].items()},
           'stream_sectors_Phi': {'%d,%d' % k: {'exponent': fr_str(alpha(*k)+1), 'series': sdict_out(S)} for k, S in X['Phi'].items()},
           'potential_sectors_C': {'%d,%d' % k: {'exponent': fr_str(alpha(*k)+3), 'series_cos': sdict_out(S)} for k, S in X['C'].items()},
           'residual_sectors_E': {'%d,%d' % k: {'exponent': fr_str(alpha(*k)), 'series': sdict_out(S)} for k, S in X['E'].items()},
           'notes': 'sine series in theta (odd harmonics for density and residual; even for stream, cosine for potential); valid for r > 1; omitted terms have exponent <= gamma - 2(qmax+1)'}
    json.dump(out, open(sys.argv[2], 'w'))
