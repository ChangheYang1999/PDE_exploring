# Smaller explicit constants for the vertical-strip remainder

## Exact theorem and notation

Use the strip space, canonical velocity and extended traces T,T1 of proof 23. In particular the input h is even in x, supported in |x|<R, and

 ||h||_(a,R)^2 = integral_(0<x<R, y in R) |h(x,y)|^2 x^(-2a) dx dy,

with 5/2<a<9/2. Oddness in y is optional. For any v>1 define

 P=256/[6 e^4 (1-1/v)^4], Q=27/[2 e^3 (1-1/v)^3],
 M=1/[e(1-1/v)],

 C_A = P v^(a-9/2)/sqrt(2(9-2a))
       +v^a sqrt((1+v/e)(1+2(v^2-v^(-2))/e^2))
       +M/[sqrt(2(2a+1)) v^(a+1/2)]
       +(4/e^2)/[sqrt(2(2a-3)) v^(a-3/2)],                 (1)

 C_B = 1+Q v^(a-9/2)/[2 sqrt(9-2a)]
       +v^a sqrt(2(1+(v-v^(-1))/e))
       +M/[2 sqrt(2a+1) v^(a+1/2)]
       +(1/e)/[2 sqrt(2a-1) v^(a-1/2)].                  (2)

For j=0,1,2 put

 B_j=((j+1)/e)^(j+1)/sqrt(2a-2j-1),
 D_A=C_A+B_1/sqrt(9-2a), D_B=C_B+B_0/sqrt(9-2a).          (3)

Then the exact bounds are

 ||x(U1[h]-xT1[h])||_(a,R) <=C_A R ||h||_(a,R),
 ||x^2(U2[h]-T[h])||_(a,R) <=C_B R^2 ||h||_(a,R),
 ||x^3 U1[h]||_(a,R) <=D_A R^3 ||h||_(a,R),
 ||x^4 U2[h]||_(a,R) <=D_B R^4 ||h||_(a,R),
 ||partial_y^j T[h]||_L2 <=B_j R^(a-j-1/2)||h||_(a,R).    (4)

All output strip norms are restricted to 0<x<R. At the actual a=17/4, choose v=7/4. Directed arithmetic proves

 C_A<38.436, C_B<24.534, D_A<38.762, D_B<24.724,
 B_0<0.134331, B_1<0.230829, B_2<0.718533.                (5)

Thus both universal constants C_a,D_a in proof 23 may be replaced by39. If the two velocity components are retained separately, use C_A=D_A=39 and C_B=D_B=25. These are safe bounds, not sharp operator norms. The theorem does not estimate the actual background derivatives or any global inverse.

## Frequency kernels

Take the unitary Fourier transform in y and write lambda=|eta|. The derivation and dense core in proof 23 give the following absolute kernel bounds for the operators A=x(U1-xT1) and B=x^2(U2-T). The B kernel also has the local multiplier -x^2.

For x<s the exact nonlocal kernels in absolute value are

 K_A=lambda x e^(-lambda s)(sinh(lambda x)-lambda x),
 K_B=lambda x^2 e^(-lambda s)(cosh(lambda x)-1).

For x>s, bound K_A by the sum of its original Green kernel and trace kernel,

 lambda x e^(-lambda x)cosh(lambda s),
 lambda^2 x^2 e^(-lambda s),

and bound K_B by

 lambda x^2 e^(-lambda x)cosh(lambda s),
 lambda x^2 e^(-lambda s).

Separate the square into s>v x, x>v s, and x/v<=s<=v x. Equalities at the interfaces have measure zero. Every estimate below is uniform in lambda, including its zero limit. This permits Plancherel after the one-dimensional bounds.

## Upper separated region s>v x

The elementary inequalities sinh z-z<=z^3 e^z/6 and cosh z-1<=z^2 e^z/2, together with max_(u>=0) u^m e^(-u)=(m/e)^m, give

 K_A<=P x^4/s^4, K_B<=Q x^4/s^3.                        (6)

Conjugating by x^(-a) changes these kernels to at most P x^(4-a)s^(a-4) and Q x^(4-a)s^(a-3). They are Hilbert-Schmidt on the separated region. Direct integration yields

 integral_0^R integral_0^(s/v) P^2 x^(8-2a)s^(2a-8) dx ds
     =P^2 R^2 v^(2a-9)/[2(9-2a)],

 integral_0^R integral_0^(s/v) Q^2 x^(8-2a)s^(2a-6) dx ds
     =Q^2 R^4 v^(2a-9)/[4(9-2a)].                        (7)

Taking square roots gives the first terms in (1) and the second term in (2), with their required powers of R. This use of the Hilbert-Schmidt norm replaces the much larger separate Schur row and column estimates in proof 23. The condition a<9/2 is exactly what makes the inner x integrals finite.

## Lower separated region x>v s

Here the original Green pieces are bounded by M for A and M x for B, since lambda x e^(-lambda(x-s))<=1/[e(1-1/v)]. The trace pieces are bounded by (4/e^2)x^2/s^2 for A and (1/e)x^2/s for B. Conjugate again by x^(-a) and s^a and integrate first in 0<s<x/v. The four squared Hilbert-Schmidt bounds are respectively

 M^2 R^2/[2(2a+1)v^(2a+1)],
 (4/e^2)^2 R^2/[2(2a-3)v^(2a-3)],
 M^2 R^4/[4(2a+1)v^(2a+1)],
 (1/e)^2 R^4/[4(2a-1)v^(2a-1)].                          (8)

Their square roots are the final two terms of (1) and (2). All integrals converge under the displayed range of a. The original and trace parts are estimated separately here, without invoking a cancellation where the sign is different.

## Comparable region

Put G_lambda(x,s)=e^(-lambda max(x,s))cosh(lambda min(x,s)). It is symmetric and

 integral_0^infinity lambda G_lambda(x,s) ds=1,
 integral_0^infinity lambda G_lambda(x,s) dx=1.

The absolute original Green kernel of either velocity component is bounded by G_lambda. Thus the original A kernel has both unweighted Schur integrals at most R; for B they are at most R^2.

For the A trace kernel, the row integral over the comparable region is at most

 lambda^2 x^2 integral_(x/v)^infinity e^(-lambda s) ds
 <=(v/e)R.

For its column integral use x^2<=Rx and integrate x from s/v to vs. Restricting additionally to x<R only reduces this bound. The result is

 lambda^2 e^(-lambda s) R s^2(v^2-v^(-2))/2
 <=[2(v^2-v^(-2))/e^2] R.

For the B trace the row integral is at most x^2<=R^2. Its column integral uses x^2<=R^2 and an interval of length at most (v-v^(-1))s, giving at most [(v-v^(-1))/e]R^2.

Apply weighted Schur with helper p(x)=x^(-1/2). The row weight ratio is (s/x)^(a-1/2), bounded by v^(a-1/2), and the column ratio is (s/x)^(a+1/2), bounded by v^(a+1/2). The geometric mean therefore contributes v^a. Combining the original and trace row/column bounds proves the middle term in (1) and the third term in (2). The local multiplier -x^2 in B has norm R^2 and contributes the first term1 in C_B. Adding the three regional operator bounds proves the first two inequalities of (4).

## Sharper trace constants and domains

The exact trace formula is

 T_hat(eta)=lambda integral_0^R e^(-lambda s) h_hat(s,eta) ds,
 T1=-partial_y T.

Weighted Cauchy-Schwarz followed by the pointwise maximum formula gives

 |eta|^(2j)|T_hat|^2
 <=lambda^(2j+2) integral_0^R s^(2a)e^(-2lambda s) ds
                  ||h_hat||^2_L2(s^(-2a)ds)
 <=((j+1)/e)^(2j+2) integral_0^R s^(2a-2j-2) ds
                  ||h_hat||^2_L2(s^(-2a)ds).

This is precisely the last inequality in (4). It needs a>j+1/2; all three values j=0,1,2 are covered. Now

 x^3 U1=x^2 A+x^4 T1, x^4 U2=x^2 B+x^4 T,
 ||x^4||_L2((0,R),x^(-2a)dx)=R^(9/2-a)/sqrt(9-2a).

These identities prove D_A,D_B in (3). Plancherel, followed by the same density argument as proof 23, extends all estimates to the full stated strip space. In particular the traces mean their continuous extensions and the velocities agree with the canonical L2 velocities. No unproved pointwise trace theorem is used.

## Consequence for the actual radial weight

With the exact notation and hypotheses of proof 93, its constant Aax can be replaced by

 sqrt(Wmax)[39 M20+(25 s0/2)M21
                    +(39 s0^2/6)M40+(25 s0^3/24)M41].    (9)

The optional factor sqrt(Wmax/Wmin) for radially localized input remains valid. All Taylor factorials, parity conditions, vertical versus radial jet distinctions and output restrictions from proof 93 remain unchanged. This improves a sufficient analytic strip constant only. Four actual coefficient suprema, separated input pieces and the rest of the compact-defect certificate remain necessary.

The accompanying single-thread script evaluates (1)-(3) at256 and384 bits, verifies the outward rational bounds (5), and records exact input rationals and hashes. The integral identities (7)-(8) and the full infinite-dimensional proof above are the mathematical certificate; a finite matrix or frequency sample is not being substituted for it.
