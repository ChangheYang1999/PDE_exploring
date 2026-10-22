Prepared 2026-10-22T09:05:34.960323+00:00 before controls.

# Leading weighted temperature polynomial at the formal endpoint

This is a local formal statement for the tuned beta=2 family of P321. It does not assert convergence, a profile near the material center or a whole-plane solution. Put r=x^2 and let s be the inward axis variable used in P321. Degree below means ordinary total degree in r,s. Multiplying that degree by2 gives the grading with weight2 for s and weight1 for x, so degree11 below corresponds to weighted degree22 in x,s.

## Exact statement
Fix real Ck nonzero. Let B=s+ks^2-(Ck/260)s^13, H=-k^7/231, t=s^10 times an analytic unit with value1 at0, Y=s^6 times an analytic unit, J(0)=0 with J'=t/(B Y). Set theta_1=Ct/2, omega_0=Y(H-CJ), v_0=B and v_1=-(omega_0+B'')/2. Suppose the formal hierarchy of P321 is satisfied, so all theta_l,omega_j,v_j are analytic germs and

Theta(r,s)=sum_(l>=1) theta_l(s) r^l,
V_r=2r[4+B'(s)+sum_(j>=1) v_j'(s) r^j/(2j+1)],
V_s=-B(s)-sum_(j>=1) v_j(s)r^j,
V_r partial_r Theta+V_s partial_s Theta=0.

Then the first nonzero total-degree part of Theta(r,s) has degree11 and is

    Theta_[11](r,s) = (C/2) r (s-(k/11)r)^10.

In particular ord_s theta_l >= 11-l for 1<=l<=11, and

    [s^(11-l)] theta_l = (C/2) binomial(10,l-1) (-k/11)^(l-1).

The notation ord_s at a zero germ can be read as infinity. The lowest ordinary total degree in x,s is12, with unique term(C/2)x^2 s^10. No assertion about the next weighted degree or convergence is made.

## Proof
Because omega_0 vanishes to order at least6 and B''(0)=2k, one has v_1(0)=-k. The displayed formal field consequently has linear part

    L=10r partial_r+(kr-s) partial_s.

All other coefficients of V have total degree at least2. To see this directly, B=s+O(s^2), B'=1+O(s), and every v_j is a power series with nonnegative exponents. Terms r v_1 contribute -k r to B+sum v_j r^j; all j>=2 terms have degree at least2. The r component has a factor r and its bracket has constant5.

Make the invertible linear change q=s-(k/11)r. Then Lr=10r and Lq=-q. Therefore L acts diagonally on r^a q^b with eigenvalue10a-b. A homogeneous polynomial of degree d in the kernel of L is a linear combination of monomials with b=10a and d=11a. Thus there is no nonzero kernel at degrees1 through10, and the degree11 kernel is the one-dimensional span of r q^10.

The series Theta is nonzero, since its r coefficient has leading term(C/2)s^10 with C nonzero, and it has no constant term because it is divisible by r. Let d>=1 be its lowest total degree. The lowest-degree part of V.Theta=0 is L Theta_[d]=0: differentiating lowers degree by1 and every nonlinear part of V has degree at least2. Hence d is a positive multiple of11. The given nonzero coefficient of r s^10 has degree11, so d<=11. It follows that d=11 and Theta_[11]=A r q^10. The coefficient of r s^10 in this polynomial is A, so A=C/2. Expanding the binomial gives the coefficient formula and the lower-order vanishings. For l<=11 the minimum ordinary x,s degree of theta_l(s)x^(2l) is at least11+l, with equality12 only at l=1. For l>=12 it is at least2l>=24. This also proves the ordinary-degree statement. The argument takes place entirely in the formal power-series ring, where each total-degree coefficient depends on finitely many input coefficients.

## Scope
This polynomial explains the large cancellations among the first eleven transverse coefficients. It is not a factorization of the entire temperature and does not establish an actual separatrix of a convergent field. In particular q=0 is the zero line of the leading polynomial in the r,s variables, not a proved zero curve of the full temperature. Finite evaluations and leading coefficients cannot establish convergence or divergence. P321 provides the formal hierarchy; P326 provides a common s disk, but neither provides growth bounds in the transverse index. The full-plane B2 question remains OPEN.

No JavaScript/TypeScript, no servers/listeners, no RLScience cluster or Lean/Lake builds. Write only in verification.
