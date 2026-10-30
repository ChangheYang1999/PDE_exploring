# Independent audit of the first theory contract

## Statement, hypotheses and scope

This note audits the frozen theory_v01 in source/. In its notation, let the reference satisfy all hypotheses (A) to (D) of the independently reviewed T4-019 theorem in ../l2_closure/PROOF.md. In particular the signed L2 decay rate is at least beta_L=2, the first and second differentiated energy margins are 9/10 and 1/2, and the component-sum caps are (2,6,24,160,22,32,80,2048). The parity is S1, even in x and odd in y, the exponent c is fixed, and c+c[rho]=1 exactly. All spaces and maximal distributional domains are those of T4-019, with omega=(1+4r²)^(2/5) and J=(1-Delta)^(1/2).

Write e(h)=(P,a,b)=(||omega D²J^s h||_2,||DJ^s h||_2,||J^s h||_2). For positive radii r=(r2,r1,r0), set n=(r2²+2r1²+r0²)^(1/2), nu=n/sqrt(s), 0<s<=1/1024, and

m0=beta_L-3882s-(3/10)nu,
m1=9/10-4290s-(13/10)nu,
m2=1/2-4708s-(A_s+B_s)nu,
A_s=127/50+(653/5)s, B_s=(9/5)(1+44s),
alpha=347/5+5440s+B_s nu, beta=10+34816s, c1=6+1360s.

If m0,m1,m2>0, define

Gamma0=phi0/m0,
Gamma1=(phi1+c1 Gamma0)/m1,
Gamma2=(phi2+alpha Gamma1+beta Gamma0)/m2+sqrt(40/m2)Gamma1.

If e(F)<=phi, Gamma<=r componentwise and d/beta_L<1, where d=n/[2sqrt(pi s(1+s))], then exactly one h in the box e(h)<=r, c[h]=0 solves the stationary equation at the fixed c. Its slope is positive if d<a0. The fixed leading profile is preserved under the tail hypotheses of T4-019.

This is the conditional FW-T-TB-gradedL2-v1 assertion. No candidate has been shown to satisfy all its hypotheses. Section 4 below audits independent norm and finite-rank lemmas. Section 5 confines the scope of the contract's numerical interpretations.

## 1. Transfer of the bottom energy and rough costs

The low L2 energy for A_k=L+U[k].D is bounded by -beta_L||h||_2² independently of k: the rough transport is skew on L2 because U[k] is divergence free. After conjugation by J^s the smooth commutator contributes at most 3882s b², by the third row of the audited commutator table. The rough commutator contributes at most (3/10)nu b². These bounds do not use an Hdot^-1 norm. Hence

m0 b² <= phi0 b.

This is the asserted (L0), including at b=0. The top two rows of T4-013 do not use its fourth component; the inequality ||k||_(H^(2+s))<=n uses only P,a,b. Its weighted velocity bound uses P alone. Their transfer therefore gives

m1 a² <= phi1 a+c1 ab,
m2 P² <= (phi2+alpha a+beta b)P+40a².

The three Gamma bounds follow successively, using the elementary positive-root bound for the last quadratic. No feedback from the deleted H component remains.

## 2. Qualitative inverse and domain

It would be incorrect to invoke the scalar T4-019 high decay rate at this box: that particular scalar aggregation need not be positive. Instead construct an equivalent positive energy directly. Put

M=(41+alpha²/m2)/m1,
L=(1+beta²/m2+(M c1)²/2)/m0,
E_aux²=P²+M a²+L b².

For the homogeneous estimates, bound alpha aP and beta bP by m2 P²/4 plus respectively alpha² a²/m2 and beta² b²/m2. Bound M c1 ab by a²/2+(M c1)²b²/2. The resulting dissipation is at least

(m2/2)P²+(1/2)a²+b² >= min(m2/2,1/(2M),1/L) E_aux².

This rate is positive and uniform for k in the box. The strict inequalities also hold in a small enlarged box. The smooth-approximation and generator construction of T4-019 applies in this equivalent norm. Its L2 Duhamel consistency argument, made explicit in that topic's ADDENDUM.md, identifies this semigroup with the maximal L2 realization restricted to the high space. Integration of the decaying semigroup gives the inverse; approximating k and f and taking weak component limits proves the three Gamma inequalities for that inverse. Thus the argument does not presume undefined separate energy pairings on a rough maximal-domain element.

## 3. Nonlinear, normalization and exact box checks

Let T(k)=-A_k^-1F. Gamma<=r makes the box invariant. The identity (A_k h)_y(0)=c[k]h_y(0)+a0 c[h], together with F_y(0)=0 and c[k]=0, proves c[T(k)]=0. The trace exists because the box bounds H^(2+s). For two inputs, the common low realization gives

||T(k)-T(l)||_2 <= beta_L^-1 ||U[k-l].DT(l)||_2
<= (d/beta_L)||k-l||_2.

The box is complete in L2: any L2 Cauchy sequence has a weakly convergent high-space subsequence, the limits agree distributionally, all component bounds pass by weak lower semicontinuity, and the continuous strain functional passes to the limit. The contraction theorem now proves existence and uniqueness within this box. Positivity and leading-tail preservation follow as in T4-019.

The independent Arb512 script checks the exact decimal box from theory_v01,

s=5/262144,
r=(2023/10000000,83/250000000,23/1250000000),
phi=(89021/5000000000,17387/125000000000,347739/10000000000000).

The same script checks the four-component graded instance (i), using its exact printed decimals and the independently audited T4-013 Gamma map. These are sufficient boxes, not optimized global thresholds.

## 4. Other conditional lemmas

For 0<=s<=1, concavity gives (1+|xi|²)^(s/2)<=1+s((1+|xi|²)^(1/2)-1)<=1+s|xi|. Multiplication by the Fourier amplitude, |xi| times that amplitude, or |xi|^-1 times it, followed by the triangle inequality in L2, proves respectively

G0<=gamma0<=G0+sG1,
G1<=gamma1<=G1+s||D²f||_2<=G1+sP2,
H<=gammaH<=H+sG0.

These hold when the displayed right sides are finite, with the Fourier convention and Plancherel factor fixed in the contract. Thus (G-a) to (G-c) are confirmed. No pointwise Fourier comparison is asserted for the weighted top norm.

For lemma L4, take a Banach space X, a bijection L0:D(L0)->X with bounded inverse of norm at most kappa0, bounded functionals p_i in X*, vectors a_i in X, and K=sum a_i p_i. Let L=L0+K on D(L0). Suppose g_i in D(L0), r_i=L g_i-a_i, and theta=kappa0 sum ||p_i||||r_i||<1. Define S=(I-sum g_i p_i)L0^-1. Direct multiplication gives

LS=I-E, E=sum r_i p_i L0^-1, ||E||<=theta.

The geometric series gives a right inverse S(I-E)^-1. Injectivity follows because L0^-1L=I+L0^-1K is identity plus finite rank: on the finite-dimensional range of L0^-1K, surjectivity implies injectivity, and every vector in its kernel belongs to that range. Hence L is bijective and

||L^-1|| <= kappa0(1+sum ||p_i||||g_i||)/(1-theta).

This confirms L4 under the explicit domain and boundedness hypotheses just stated. It gives no decomposition of the IPM coupling into finite rank and a controlled remainder. In particular, it does not contradict the full-coupling noncompactness obstruction.

## 5. Scope corrections to theory_v01

The tables of pure exterior powers have the conditional meaning stated in section 5 of the contract. They are not lower bounds for a full residual on the basis of its leading coefficient alone. The finite-family bounds, rather than those tables, give the stated family exclusions.

The assertion that H binds for every residual away from the origin is too broad as a norm statement. A smooth S1 function supported in a fixed annulus, multiplied by cos(Nx), has Hdot^-1 norm tending to zero as N grows, whereas its derivative norms grow. A low-frequency annular scaling model cannot be applied uniformly to these functions. For the particular d2 candidate the reported component dominance is a separate numerical observation.

The assertion that a decaying residual can never benefit from the weighted framework is not an established theorem about potential-generated residuals. The source itself gives a smooth S1 function with the prescribed fixed tail and finite power structure below the weighted threshold (A2 P29), while explicitly leaving realizability as a nonlinear residual open. The blanket statement should be restricted to the presently measured candidates, or labelled heuristic. Likewise 'the missing factor cannot come from inverse constants' is a planning judgment about the explored estimates, not an impossibility theorem for every inverse construction.

Some displayed necessary bounds on the components of J^s F are rounded down. At s=2^-17 the exact limits are 1/163840, 1/20971520 and 1/83886080. Safe decimal upper roundings are 6.103516e-6, 4.768372e-8 and 1.192093e-8. Existing raw-F upper roundings in the contract are safe.

## 6. Six-branch finite-family cutoffs

Here the hypotheses are precisely the A2 P33 family: c=4076476460239181/2251799813685248, gamma=1/c, delta=1-gamma, potential branches 0<=j<=5, angular indices 0<=m<=59, radial indices m<=k<=K with K>=59, the six fixed stationary leading moments, and zero first descendants of branches 0 and 1. The unchanged A2 theorem supplies

||F||_H >= D_K sqrt((pi/2) sum_m e_m²/(m²+Q_n)),
D_K=(2a_*+1)^(-1/2) product_(a in A_K,a>a_*) (a-a_*)/(a+a_*+1),
a_*=7delta/2-2,
A_K={ell delta/2+k-2:1<=ell<=12,0<=k<=2K+4, ell delta/2+k-2>=a_*},
n=12(2K+5)-8, Q_n=4(n-1/2+log(2n-1)/8)²+4/3.

The fixed coefficients e_m come from the exact sixth stationary forcing vector, stored in source/stationary_principal.json. This application does not reprove the A2 power-space and cylinder theorem, whose statement and proof are frozen in source/A2_P33.txt. It independently reproduces the new numerical cutoffs.

If delta=N/D in lowest terms, each distance ratio is the positive exact integer ratio

((ell-7)N+2Dk)/((ell+7)N+2D(k-3)).

All admitted ratios except the omitted leading one lie strictly between zero and one. There are no coincident exponents, since D>12. Raising K appends powers, decreases D_K, raises n and decreases the angular factor. Thus the lower bound decreases strictly with K. Certifying its value above the appropriate required H bound at K_* and below at K_*+1 proves the stated cutoff for this sufficient criterion. It makes no feasibility claim at larger K.

The independent script uses direct integer-ratio products in Arb512, rather than T1's logarithmic sum. Requirements are eta/[(1-34s)512sqrt(20/21)] for scalar Ns balls and the exact printed phi_H for graded boxes, because gamma_H>=H. The comparisons to check are K_*=3675,1315,1021,1063,511 for the baseline, rebalanced, T1 graded, T4 graded and sharp balls respectively. The immutable JSON records both sides of each crossing and source hashes.
