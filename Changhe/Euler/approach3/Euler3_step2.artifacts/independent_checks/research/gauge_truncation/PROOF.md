# Central differences of a normalized squared gauge

## Statement

Let a > 0, let N be a real C^5 function on [-a,a], and assume N(0)=1. Let gamma be a real constant and define E(t)=gamma^2 (N(t)-1)^2/2. For 0<h<a, put D_h E=(E(h)-E(-h))/(2h). Then E'(0)=0 and

D_h E = (gamma^2/2) N'(0) N''(0) h^2 + R_h,

where |R_h| <= h^4 sup_{|t|<=h}|E^(5)(t)|/120. In particular a nonzero central difference need not indicate an incorrect value of E'(0).

If t is replaced by a C^5 coordinate map p(t) with p(0)=0, the leading coefficient becomes

gamma^2/2 times [N'(0)p'(0)] times [N''(0)p'(0)^2 + N'(0)p''(0)].

The statement is local. It does not claim that any particular finite-difference tolerance is met.

## Proof

Write n(t)=N(t)-1. Differentiation gives E'=gamma^2 n n', E''=gamma^2[(n')^2+n n''] and E'''=gamma^2[3 n'n''+n n''']. Since n(0)=0, E'(0)=0 and E'''(0)=3 gamma^2 N'(0)N''(0).

Taylor's formula of degree four for E at h and at -h, with its fifth-derivative remainder, gives

E(+-h)=E(0) +- E'(0)h + E''(0)h^2/2 +- E'''(0)h^3/6 + E''''(0)h^4/24 + r_+/-.

Each remainder has absolute value at most h^5 sup_{|t|<=h}|E^(5)(t)|/120. Subtract the two formulas and divide by 2h. The even terms cancel. The bound for R_h and the first formula follow. Apply the first and second chain rules to N composed with p to obtain the coordinate-map formula.

## Application and scope

For the Euler objective's gauge row gamma (||F||-1), take N(t) to be the tail norm on a chosen coefficient-parameter path and gamma=100. The theorem applies wherever that norm and the path are C^5 and the base norm equals one. It predicts a potentially large h^2 contribution to the cost difference even though the gauge contributes zero to the base gradient. Other objective rows contribute their own Taylor terms. Attribution of an observed discrepancy to this gauge requires a separate numerical check; the theorem alone gives no such attribution.

Dependencies: ordinary product, chain and Taylor rules on real intervals. No formal proof is claimed; no Lean or Lake execution is permitted in this side.
