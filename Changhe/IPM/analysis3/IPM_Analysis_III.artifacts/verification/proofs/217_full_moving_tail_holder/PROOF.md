# The full moving-tail linearization on the common Holder target

## Exact setting and statement

Fix 0<alpha<1 and 4k<gamma<2. Let Y=E2 intersect L2(w_gamma) be exactly the physical parity space of proof 213, with its sum norm. Let rho0 be the joined normalized modal trial, k its exact exponent, ell0=1/k, and Theta its exact leading angular factor. Use the smooth radial chart cutoff chi_infinity of topics167 and190, zero on r<=1 and1 outside a fixed disk. Define

 rho_ell=rho0+chi_infinity(r)(r^(1/ell)-r^k)Theta(theta),
 zeta=partial_ell rho_ell at ell0=-k^2 chi_infinity r^k log(r)Theta,
 n(ell)=3ell-1-c[rho_ell], n'_0=3-c[zeta]>=3,
 M0=(X.grad rho0+L_fix zeta)/n'_0,
 H0=chi0 X.grad rho0/3, m0=M0-H0,

where chi0 is smooth radial, compact and1 near0, and

 L_fix h=(ell0 X+U[rho0]).grad h-h+U[h].grad rho0.

All velocities use the same canonical whole-plane convention. The differentiated-tail velocity of zeta is defined by its convergent modal Green formulas. It is not obtained by assuming the growing zeta belongs to Y.

Then m0 belongs to Y for every displayed alpha,gamma. The full chart linearization

 A0 h=L_ren h+c[h]m0
     =V.grad h-h+U[h].grad rho0+c[h]M0,
 V=ell0 X+U[rho0],
 D_Y={h in Y:V.grad h belongs to Y distributionally}

is a closed operator D_Y->Y on exactly its maximal distributional domain. This is a realization theorem, not an inverse theorem. In this Holder target the individual columns H0 and M0 also belong to Y, because this norm permits a cubic jet. Their exclusion from the stronger targets of proof 188 is unaffected.

The full bounded coupling C0=U[.].grad rho0+c[.]M0 has a small output tail: for beta_R=1-chi(X/R), with a fixed smooth radial chi equal1 on B1 and0 outside B2,

 ||beta_R C0||Y->Y<=C R^(2k-gamma/2)(1+log R),       (1)

for sufficiently large R. The exponent is negative precisely under gamma>4k. This is an upper bound; its sharpness is not asserted.

The unit-cubic, exact zero-strain packets of proof 214 lie in D_Y and tend to0 in the full A0 graph. Thus J is not closable on the compact smooth domain even after restriction to c=0. Likewise proof 216's cutoff commutator [A0,chi] is noncompact from D_Y with its graph norm into Y whenever its stated regular flow-box condition holds.

Finally there is an actual-origin extension inverse including this precise moving-tail column. For the coefficient extension V_delta of proof 202 define

 A_delta h=V_delta.grad h-h
       +chi(X/delta){U[h].grad rho0+c[h]M0}.         (2)

For each fixed alpha<1 and sufficiently small delta, (2) is a closed bijection on its maximal E2 transport domain, with a uniformly bounded E2 inverse. Its characteristic factorization error is O(delta^2). On B_(delta/2) it equals the full A0 expression. This extends proof 215's origin result by a smaller rank-one term; it supplies neither a global inverse nor a closed cubic normalization.

## Direct column membership, with both cancellations

Near0, zeta vanishes identically. Its canonical velocity is smooth there and has the parities of the IPM velocity. By the convergent separated kernel and the strain identity,

 U[zeta]=c[zeta](-x,y)+R_zeta,
 R_zeta=O(r^3), D R_zeta=O(r^2).

Every fixed higher derivative on a smaller disk is bounded. The density rho0 is C^(4,1) at0, has both parities, vanishes on x=0, and has Taylor polynomial x^2y through degree4. Thus rho0-x^2y=O(r^5) with the differentiated bounds used in proof 212. Since H0=X.grad rho0/3 near0 and n'_0=3-c[zeta], we have the exact local formula

 m0={U[zeta]+c[zeta]X/3}.grad rho0/n'_0.             (3)

The linear strain annihilates the cubic term, so m0=O(r^5). To check division rather than just pointwise order, write rho0_x=x a1, rho0_y=x^2 a2, with a1=2y+O(r^3), a2=1+O(r^2) and the first derivative bounds of proof 212. The components of R_zeta have the corresponding axis parities, so R_zeta1/x=O(r^2), its first y derivative is O(r), R_zeta2=O(r^3), and its first y derivative is O(r^2). Formula (3) then gives

 |m0/x^2|<=Cr^3, |partial_y(m0/x^2)|<=Cr^2,
 |m0|<=Cr^5, |partial_x m0|<=Cr^4.                  (4)

These bounds include the vertical axis by continuous division. The strain part uses the same exact bracket -(2/3)a1+(4/3)ya2=O(r^3), with derivative O(r^2), as proof 212.

For the far cancellation write, outside a fixed disk,

 rho0=r^k Theta+R,
 D_cyl^j R=O(r^(2k-1))

for each fixed number of cylinder derivatives needed below. These are the exact finite outer formulas of proof 117, with their faster remainders. The separated tail gives

 zeta=-k^2 r^k log(r)Theta,
 U[zeta]=O(r^k(1+log r)), U[rho0]=O(r^k),

including the same fixed cylinder derivatives. The canonical Green integrals converge and their parameter derivative is justified by the integrable far moments r^(q-2)(log r)^j for q<1, as directly proved in proof 167. No Y-valued claim about zeta is used.

In X.grad rho0+L_fix zeta, the leading linear radial terms cancel exactly:

 X.grad(r^k Theta)=k r^k Theta,
 (ell0 r partial_r-1)(-k^2 r^k log(r)Theta)
       =-k r^k Theta.

The remaining linear term is X.grad R=O(r^(2k-1)). Each nonlinear term U[rho0].grad zeta and U[zeta].grad rho0 has size O(r^(2k-1)(1+log r)); products involving R are faster. Consequently, including fixed cylinder derivatives,

 M0=O(r^(2k-1)(1+log r)).                            (5)

There are finitely many smooth angular factors, and the parity and the vertical-axis quadratic vanishing give smooth division by cos^2(theta), with uniform angular derivative bounds. The latter vanishing follows term by term: V1 and U1 vanish to first order in x, rho0_x and zeta_x vanish to first order in x, and rho0_y,zeta_y vanish to second order in x. Oddness in y is preserved as well. Thus (5) yields

 |m0/x^2|<=Cr^(2k-3)(1+log r),
 |partial_y(m0/x^2)|<=Cr^(2k-4)(1+log r),
 |m0|<=Cr^(2k-1)(1+log r),
 |partial_x m0|<=Cr^(2k-2)(1+log r)                 (6)

at infinity, since H0 is compact. On compact punctured annuli the trial is C6 at its radial joins; its first derivatives are C5, the Green velocity is at least as regular, and the smooth tail cutoff creates no additional join. Thus all first derivatives and divisions used in (4),(6) extend continuously and are bounded on the intervening compact region.

Since 2k-1<0, (4),(6) and the compact-region bounds prove globally bounded m0, partial_x m0, m0/x^2 and partial_y(m0/x^2). Splitting one-dimensional differences at1, as in proof 213, proves m0 belongs to E2 for every alpha<1. The weighted L2 integral is bounded at infinity by a constant times

 integral_1^infinity r^(4k-1-gamma)(1+log r)^2 dr,

which is finite for gamma>4k. This proves m0 in Y without a high-to-low norm comparison or an infinite-minus-infinite split. The fixed compact H0 also belongs to Y by the same local division, so M0 belongs to Y as stated.

## Column tail and the closed operator

Apply (6) to beta_R m0. Cutoff derivatives cost C/R and preserve its displayed decay powers. Splitting x and y differences at1 gives

 ||beta_R m0||E2<=C R^(2k-1)(1+log R).

For the weighted L2 part substitute r=Rs in the preceding tail integral. Since gamma-4k>0, the integrals of s^(4k-1-gamma)(1+log s)^j for j=0,1,2 are finite. Therefore

 ||beta_R m0||L2(w_gamma)
       <=C R^(2k-gamma/2)(1+log R).                 (7)

Because gamma<2, the exponent in (7) is larger than 2k-1, so it bounds the E2 part as well for R>=1. The H0 tail vanishes for large R. Proof 214 gives the other coupling tail O(R^(k-1)(1+log R)); here

 (2k-gamma/2)-(k-1)=k+1-gamma/2>0.

Thus (7), ||c||Y*<=4/pi and proof 214 prove (1).

The same strain bound and m0 in Y make c[.]m0 a bounded rank-one operator on Y. Proof 214 proves that L_ren is closed on D_Y and that its bounded coupling does not alter the maximal transport domain. Adding this rank-one term preserves both conclusions and proves the asserted A0 realization. The graph norms of A0 and L_ren are equivalent by this bounded perturbation.

The exact packets k_epsilon of proof 214 have c[k_epsilon]=0, J[k_epsilon]=1 and converge to0 in the L_ren graph. Their A0 images agree exactly, proving the nonclosability statement on the full realized operator. For proof 216's compact flow-box packets h_n, with ||h_n||infinity->0 and exact c=0, the added cutoff commutator is

 c[chi h_n]m0-chi c[h_n]m0=c[chi h_n]m0.

Its norm tends to0 because the input supports are fixed and separated from the origin, so |c[chi h_n]|<=C||h_n||infinity. It cannot cancel that topic's noncompact lower bound. Graph equivalence proves the stated full A0 commutator assertion.

## The exact-column origin extension

Take delta sufficiently small that chi0=1 on B_delta. The operator (2) differs from the normalized origin extension L_delta of proof 215 by the bounded rank-one operator

 D_delta h=c[h]chi(X/delta)m0.

By (4), the cutoff column satisfies

 ||chi(X/delta)m0||E2<=C delta^(3-alpha).             (8)

Indeed its divided vertical cofactor has supremum O(delta^3), y derivative O(delta^2), and support in B_delta; product differences split at delta give y alpha seminorm O(delta^(3-alpha)). The ordinary x seminorm is O(delta^(5-alpha)), and the supremum is O(delta^5), both smaller. The bound is global because pairs with one point outside the larger support box have separation comparable to delta, and the supported-endpoint cutoff difference handles close crossing pairs.

The strain norm gives ||D_delta||E2->E2<=C delta^(3-alpha). Proof 215's factorization becomes

 A_delta=A_delta,coeff{S_delta+E_delta+q_delta D_delta},

where A_delta,coeff is that topic's positive divided transport coefficient, not the operator on the left. The new error obeys

 ||E_delta+q_delta D_delta||<=C delta^2+C delta^(3-alpha)
                            <=C' delta^2

because alpha<1 and delta<=1. Multiplication by the reciprocal coefficient is bounded uniformly by proof 215. The characteristic inverse and the exact maximal domain are unchanged. Its operator-norm Neumann series therefore gives the claimed closed bijection with a uniform bound for sufficiently small delta. This checks the complete column rather than using only its leading cubic coefficient.

Dependencies: topics167,188,190 for the exact chart definitions and finite column identity; proof 117 for the exact outer expansion; topics212-216 for the Holder estimates, maximal realization and counterexamples. All column membership, far cancellation, logarithmic terms, divided derivatives and norm comparisons are derived above. Constants and radii remain qualitative; actual global injectivity and any nonlinear theorem remain OPEN.
