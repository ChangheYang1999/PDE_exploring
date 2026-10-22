# Euler inverses and the remaining transverse convergence gap

Prepared 2026-10-22T11:55:03.608937+00:00, before finite controls. This lemma concerns the scalar coefficient operators of P321/P326. It does not establish convergence of the B2 formal hierarchy.

## Exact statement and norm

Fix rho>0. Let A_rho be the complex sequences f=(f_j)_(j>=0) with norm sum_(j>=0)|f_j|rho^j finite, identified with their analytic power series in |z|<rho. Multiplication is bounded with norm at most the product, by the absolutely convergent convolution sum. Let m be a nonnegative integer, P_m remove the coefficient of z^m, and define

S_m f = sum_(j!=m) f_j z^j/(j-m),   E_m=z d/dz-m.

For compatible f with f_m=0, S_m f is the unique analytic solution of E_m g=f whose z^m coefficient is zero. Every other analytic solution is S_m f+c z^m. On A_rho the exact operator norm of S_m is1. Although differentiation D need not preserve A_rho, the coefficientwise composition S_m D extends boundedly from A_rho to itself and has exact norm (m+2)/rho. In contrast S_m D^2 is unbounded on A_rho, even on polynomial inputs for which D^2 f has zero coefficient at the resonance m. For 0<r<rho it obeys

||S_m D^2 f||_r <= 2 ||f||_rho/(rho-r)^2.

The operator E_m itself is interpreted coefficientwise or as an analytic germ; it is not asserted bounded on A_rho.

## Proof of the norm statements

Coefficient comparison gives E_m S_m f=P_m f, S_m E_m g=P_m g whenever the indicated series are interpreted coefficientwise. The kernel of E_m is exactly the multiples of z^m. Each nonzero integer j-m has absolute value at least1, so ||S_m f||_rho<=||f||_rho. Equality occurs for f=z^(m+1).

For an input monomial z^j, D gives j z^(j-1). The resonance j=m+1 is removed, and otherwise the ratio of output to input norms is j/(rho |j-1-m|). For 1<=j<=m this is at most m/rho; for j>=m+2 it is at most (m+2)/rho, attained at j=m+2. The zero monomial contributes zero. Summing absolute coefficients proves the asserted bound and sharpness. The equality witness for m=0 is j=2, so this case is also covered.

Take f^(j)=rho^(-j)z^j, with j>=m+3. Its A_rho norm is1 and D^2 f^(j) has no resonant coefficient. Its image norm is

j(j-1)/(rho^2(j-m-2)),

which tends to infinity with j. This proves unboundedness on the compatible polynomial inputs; it is not a statement about the special nonlinear hierarchy's actual forcings.

For the radius-loss estimate set q=r/rho. For every j>=2 the binomial term binom(j,2)(1-q)^2 q^(j-2) is at most1, since it is one nonnegative term of (q+(1-q))^j=1. Thus j(j-1)r^(j-2)/rho^j <= 2/(rho-r)^2. Sum this inequality times |f_j|rho^j, and then use ||S_m|| on A_r at most1. This proves the final estimate without claiming sharpness of its constant.

## Reduction of the B2 axis operators

Use the hypotheses, notation and normalized analytic germs of P326: B=s+ks^2-(Ck/260)s^13, Ck!=0; t=s^10 exp(tau), Y=s^6 exp(upsilon), tau(0)=upsilon(0)=0, with

B t'=(8+2B')t,   B Y'=(5+B')Y.

Primes in this paragraph mean derivatives in s. Define z=s exp(tau(s)/10). Then z(0)=0,z'(0)=1, so it is an analytic local coordinate after shrinking the disk. Write s=s(z), and define

A(z)=[B(s)z'(s)/z(s)]_(s=s(z))=(8+2B'(s(z)))/10,
eta(z)=Y(s(z))/z^6.

The apparent singularities at0 are removable, and A(0)=eta(0)=1. Shrink the disk again so A and eta are nonzero. For the thermal operator L_n=B d/ds-n(8+2B'), the chain rule gives

L_n[g(z(s))]=A(z)(z D-10n)g.

For the vorticity operator K_j=B d/ds-[(2j+1)(4+B')+1], it gives

K_j[eta(z(s))g(z(s))]=eta(z)A(z)(z D-(10j+6))g.

To verify the second identity, B eta'/eta=(5+B')-6A because Y=eta z^6. Subtract the K_j coefficient and use 10A=8+2B'. The remaining zeroth-order coefficient is -(10j+6)A, as required. These are identities of analytic germs for every n>=1 and j>=0.

For a general one of these equations, write f=eta g and m=10j+6 for the vorticity case, or eta=1 and m=10n for the thermal case. With Rtilde(z)=R(s(z)), its right-hand side after conjugation is h=Rtilde/(A eta). The scalar compatibility condition is h_m=0. It equals the original residue condition because

[R(s)/(B(s) z(s)^m eta(z(s)))] ds = [Rtilde(z)/(A(z)eta(z))] z^(-m-1) dz.

Residues are equal here: substitute the analytic invertible coordinate in the contour integral over a sufficiently small positively oriented simple loop, or compare the coefficient of its primitive's logarithm. Hence a compatible equation has f=eta S_m h plus its homogeneous multiple eta z^m. On a sufficiently small rho disk the multipliers eta and (A eta)^(-1) belong to A_rho. For the choice with g_m=0,

||f||_rho <= ||eta||_rho ||(A eta)^(-1)||_rho ||Rtilde||_rho.

This is a norm in the z coordinate. A comparison with an s-disk norm requires fixed domain choices: choose0<rho<r_z so |s(z)|<r_s for |z|<=r_z. If R belongs to A_(r_s), its supremum there bounds |R(s(z))| on the z-circle of radius r_z. The Taylor coefficient estimate then gives ||Rtilde||_rho <= ||R||_(r_s)/(1-rho/r_z). This radius change and factor depend on the fixed coordinate, not on m. This is an optional comparison, not an assertion that composition preserves the same numerical disk radius. Its particular normalization need not be the zero-constant meromorphic primitive normalization in s used by P321. For compatible equations any difference is a homogeneous solution. Before compatibility a residue-subtracted primitive changes under coordinates by an analytic contribution from log(z/s); no equality of the off-diagonal residue matrix in two such conventions is claimed.

## Consequence and exact scope

There are no arbitrarily small nonzero divisors in the normalized scalar Euler operator. The gain over one derivative has a constant growing linearly with the resonance index, whereas two derivatives cannot be controlled on this fixed normed disk for arbitrary compatible data. A smaller-radius estimate is available. These facts isolate a genuine missing estimate in a naive same-radius bound for the transverse hierarchy, but do not prove that every convergence argument must lose derivatives, that the actual nonlinear forcing attains the bad examples, or that the formal hierarchy diverges. Cancellations or other norms could change that analysis. The coefficients' common axis domain from P326 and this scalar lemma still give no bound in the transverse index. General B2, actual local convergence and a canonical full-plane reconstruction remain OPEN.

Dependencies: the analytic axis factors of P326 and elementary analytic change of coordinates. Finite polynomial/Fraction controls test the formulas and counterexamples; the preceding infinite-index arguments supply the proof. No JavaScript/TypeScript, servers/listeners/tunnels, RLScience cluster, Lean/Lake, commits/pushes/posts or human contact. Write only in verification; one low-priority CPU process at a time.
