"""Positive real roots a0 of the degree-(2j+1) jet resonance determinants (from runs/jet_res_hi.log) at given A."""
import sympy as sp, re
A, a0 = sp.symbols('A a0')
dets = {}
for line in open('runs/jet_res_hi.log'):
    m = re.match(r'j=(\d+) \(degree (\d+)\): det = (.*)', line.strip())
    if m: dets[int(m.group(2))] = sp.sympify(m.group(3))
for Av in [1.2, 1.5, 2.0, 3.0, 4.94, 5.0, 7.0, 15.0]:
    out = []
    for n, d in sorted(dets.items()):
        p = sp.Poly(d.subs(A, Av), a0)
        rts = sorted([float(sp.re(r)) for r in p.nroots() if abs(sp.im(r)) < 1e-9 and sp.re(r) > 0])
        out.append(f"deg{n}: " + ", ".join(f"{r:.3f}" for r in rts))
    print(f"A={Av}: " + " | ".join(out))
