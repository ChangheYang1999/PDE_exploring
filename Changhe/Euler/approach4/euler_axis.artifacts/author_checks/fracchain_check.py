# Lead cross-review of the verifier's fractional-axis-chain statement: for 2 < k < 3 the axial transport
# equations at an order-k saddle do not couple the two source amplitudes in the C^2 (q) / C^1 (eta) class.
import json, time, sympy as sp
t0 = time.time()
z, c, mu = sp.symbols('z c mu', positive=True)
delta = 1 + c
w = z*(z**2 - 1)*(c*z**4 + (4 + 3*c - mu)*z**2 + mu)/(1 + z**2)**3
out = {}
lw = sp.together((sp.diff(w, z) - delta)/w)
out['residue_at_0'] = sp.simplify(sp.limit(z*lw, z, 0))           # expect 1 + delta/mu = k
out['residue_at_1'] = sp.simplify(sp.limit((z - 1)*lw, z, 1))     # expect 0: h analytic at the source
out['wprime_1'] = sp.simplify(sp.diff(w, z).subs(z, 1))           # expect delta
out['wprime_0'] = sp.simplify(sp.diff(w, z).subs(z, 0))           # expect -mu
# glued profile q = Q+ z^k (1 + a z^2) for z > 0, Q- |z|^k (1 + b z^2) for z < 0, k = 5/2
k = sp.Rational(5, 2)
Qp, Qm, a, b, x = sp.symbols('Qp Qm a b x', real=True)
qp = Qp*x**k*(1 + a*x**2)
etap = (2*Qp/mu)*x**(k - 1)
ok = []
for n in range(3):
    ok.append(sp.limit(sp.diff(qp, x, n), x, 0, '+') == 0)
for n in range(2):
    ok.append(sp.limit(sp.diff(etap, x, n), x, 0, '+') == 0)
out['q_C2_eta_C1_vanish_at_saddle_k52'] = all(ok)
# k = 2: q'' = 2 Q on each side, so C^2 forces Q+ = Q-; eta' = 2 K Q/mu forces K+ Q+ = K- Q-
x2 = sp.symbols('x2', positive=True)
out['k2_q2'] = str(sp.diff(Qp*x2**2, x2, 2))
out['ok'] = (sp.simplify(out['residue_at_0'] - (1 + delta/mu)) == 0 and out['residue_at_1'] == 0
             and sp.simplify(out['wprime_1'] - delta) == 0 and sp.simplify(out['wprime_0'] + mu) == 0
             and out['q_C2_eta_C1_vanish_at_saddle_k52'])
out = {kk: (str(v) if not isinstance(v, bool) else v) for kk, v in out.items()}
out['seconds'] = round(time.time() - t0, 1)
json.dump(out, open('checks/fracchain_check_output.json', 'w'), indent=1)
print(json.dumps(out))
