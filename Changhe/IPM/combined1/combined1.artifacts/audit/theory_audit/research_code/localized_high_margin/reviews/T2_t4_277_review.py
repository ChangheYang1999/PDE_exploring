"""Independent check of T4-277 (c1-t4 research/localized_high_margin/PROOF.md, sha256 f9528c66...b55524): a box whose
low row is ||w J^s h||_2 <= r0 with w >= 1 and whose top margin (1) is the graded one has ||h||_2 < 25/54684
(reviews/REVIEW_T4_277.md).

Run from artifacts/:  python3 -B arith/t4_277_review.py
Needs sympy. Exact arithmetic only; no input data.
"""
import sympy as sp

x1, x2 = sp.symbols("xi1 xi2", real=True)
# (1 + |xi|^2)^2 = 1 + 2|xi|^2 + sum_(i,j) xi_i^2 xi_j^2 (ordered Hessian tensor)
lhs = (1 + x1**2 + x2**2)**2
rhs = 1 + 2 * (x1**2 + x2**2) + sum(a**2 * b**2 for a in (x1, x2) for b in (x1, x2))
assert sp.expand(lhs - rhs) == 0
print("(1) (1 + |xi|^2)^2 = 1 + 2|xi|^2 + sum_ij xi_i^2 xi_j^2: exact")

s, u, n = sp.symbols("s u n", positive=True)
margin = sp.Rational(1, 2) - 4708 * s - (sp.Rational(217, 50) + sp.Rational(1049, 5) * s) * n / sp.sqrt(s)
# margin > 0 with n > 0 forces 1/2 - 4708 s > 0, i.e. s < 1/9416
assert sp.solve(sp.Eq(sp.Rational(1, 2) - 4708 * s, 0), s) == [sp.Rational(1, 9416)]
# solving margin = 0 for n gives the exact cap; dropping 1049 s/5 enlarges it
ncap = sp.solve(sp.Eq(margin, 0), n)[0]
ncap_drop = sp.Rational(50, 217) * sp.sqrt(s) * (sp.Rational(1, 2) - 4708 * s)
assert sp.simplify(ncap - (sp.Rational(1, 2) - 4708 * s) * sp.sqrt(s)
                   / (sp.Rational(217, 50) + sp.Rational(1049, 5) * s)) == 0
assert sp.simplify(ncap_drop / ncap - (1 + sp.Rational(1049 * 50, 5 * 217) * s)) == 0   # ratio > 1 for s > 0
print("(2) margin (1) > 0 forces s < 1/9416 and n < %s; dropping 1049 s/5 multiplies the cap by 1 + (10490/217) s"
      % sp.simplify(ncap))
g = u / 2 - 4708 * u**3
crit = sp.solve(sp.diff(g, u), u)
assert crit == [1 / sp.sqrt(28248)]
gmax = sp.nsimplify(g.subs(u, crit[0]))
assert sp.simplify(gmax - 1 / (3 * sp.sqrt(28248))) == 0
assert sp.diff(g, u, 2).subs(u, crit[0]) < 0 and crit[0]**2 < sp.Rational(1, 9416)
bound = sp.Rational(50, 217) * gmax
assert sp.simplify(bound - 50 / (651 * sp.sqrt(28248))) == 0
print("(3) max over u > 0 of u/2 - 4708 u^3 is 1/(3 sqrt(28248)) at u^2 = 1/28248 < 1/9416; so n < 50/(651 sqrt(28248))"
      " = %s" % sp.N(bound, 12))
assert 651 * 168 == 109368 == 2 * 54684 and 168**2 == 28224 < 28248 and 50000 < 54684
assert bound < sp.Rational(25, 54684) < sp.Rational(1, 2000)
print("(4) 168^2 = 28224 < 28248, 651 * 168 = 109368 = 2 * 54684: 50/(651 sqrt(28248)) < 25/54684 = %s < 1/2000"
      % sp.N(sp.Rational(25, 54684), 10))
for name, d in (("007 (T4-185)", "0.004769166867"), ("013", "0.00199234339"), ("014 (T4-280)", "0.00198301351067"),
                ("annular mass", "0.002")):
    assert sp.Rational(d) > sp.Rational(25, 54684)
    print("(5) %-13s %s > 25/54684 by a factor %s" % (name, d, sp.N(sp.Rational(d) / sp.Rational(25, 54684), 6)))
