# A certified-prefix majorant for delta = 2/Q

Status: PROVED. The792 exact scalar coefficient identities and20 exact profile boxes are confirmed in V331. The theory part independently reviewed the h1 extension and incorporated it as PROVED in theory version31, Remark5(b); the review is retained in sources/lead_review_v31.md.

For this exponent the first stream resonance is at2Q. Starting from a certified density prefix through2Q avoids introducing an artificial harmonic atQ. The resulting residue equations have the same form as172, with a different initialization.

## Statement

Fix an integer Q>=3, delta=2/Q, c=Q/(Q-2), and an even integer B>=2. Let f1 be a nonzero real sine polynomial on the odd frequencies below B. Assume its first compatibility obstruction at2Q vanishes. Delete the resonant stream output in each particular inverse, and let sigma_k be the Q-step response to the free harmonic H_(kQ), for k>=2. Assume a certified uniform bound |sigma_k|>=s>0. These are precisely the compatibility and response hypotheses of131.

Choose M>=2 and N=M Q. Suppose rational numbers d_j>0 and e_a>=0 satisfy

    d_j >= j ||f_j||_1,  1<=j<=N,
    e_1=0,  e_a >= aQ |H_(aQ)|,  2<=a<M,

for the actual uniquely tuned prefix. Set

    L=3Q^2/[4(3Q-1)],
    kappa_N=B[2-delta+max(delta,1-delta)](1-delta)/delta * (N+1)/N.

Larger valid constants may replace these. The polynomial system below has a nonnegative strictly triangular affine part at zero. If its transformed map G admits rational w0>0 and a nonnegative vector b with b>=Y0 and G(w0,b)<=b, then the tuned density, stream and a common potential have absolutely uniformly convergent series, together with every appropriately weighted spatial derivative, on every closed exterior

    r>=R>w0^(-1/2).

The common potential includes only the two finite logarithmic corrections at ordersQ and2Q described in132. For amplitude epsilon!=0, multiply the sufficient radius by |epsilon|^(Q/2). The conclusion is an exterior stationary solution and does not assert a global stationary extension or an optimal radius.

## 1. Scalar domination and initialization

By131 the support bounds are Bn-1 for density and Bn for stream. The factored Poisson coefficients at nonzero outputs lie in the lattice with spacing2/Q. The sharp column estimate169 therefore gives ||Pi_n f||_1<=L||f||_1; it requires no condition h>=2. Deleting a resonant output preserves the bound.

Write p_j=1-j delta and P_i=2-i delta. Since |p_j|/j<=max(delta,1-delta) and |P_i|/i<=2-delta, the angular advection norm is at most B[2-delta+max(delta,1-delta)]ij||g_i||_1||f_j||_1. Dividing by lambda_m=(m-1)delta/(1-delta) and multiplying by m yields the common factor kappa_N whenever m>=N+1. This includes every new density and lookahead equation. A free harmonic contributes through ||g_i||_1<=L||f_i||_1+|H_i|.

Set x_j=d_j throughN and eta_(aQ)=e_a for1<=a<M. Set eta_i=0 at all nonresonant indices. At a true resonance n>=N, define in increasing r the nonnegative scalar equalities

    u_(n,r)=kappa_N [L sum_(i+j=n+r, i,j>=r) x_i x_j
                    +sum_(i+j=n+r, j>=Q+1) eta_i x_j
                    +2L sum_(j=1)^(r-1) d_j u_(n,r-j)], r<Q,

    eta_n=(kappa_N/s)[L sum_(i+j=n+Q, i,j>=Q) x_i x_j
                      +sum_(i+j=n+Q, j>=Q+1) eta_i x_j
                      +2L sum_(j=1)^(Q-1) d_j u_(n,Q-j)].

After each base order set

    x_(n+1)=kappa_N sum_(i+j=n+1)(Lx_i+eta_i)x_j.

At nonresonant base orders only the last equation is used. The density indices in each restricted sum are at most n. Earlier harmonics have index at most n-Q, and the extended harmonic sum still uses only indices at most n-1. The remaining lookahead indices are smaller than r. Thus these equalities define the continuation triangularly.

The actual provisional continuation with H_n=0 obeys exactly the inequalities proved in131. The tuning identity H_n=-R/sigma_k and n/(n+Q)<=1 give the harmonic bound. Induction therefore proves x_j>=j||f_j||_1 and eta_n>=n|H_n|. No recurrence inequality is required of the supplied prefix bounds. AtQ there is no positive-frequency harmonic, so e_1=0 is essential; N>=2Q ensures the first unknown harmonic is a true resonance.

## 2. Finite residue system

Let P(z)=sum_(j=1)^N d_j z^j, H(z)=sum_(a=1)^(M-1)e_a z^(aQ), and H_*(w)=sum_a e_a w^a. For a polynomial F define

    K_r F(w)=sum_(k>=0) [z^(N+r+kQ)] F(z) w^k.

Write P_(>=b) for the terms whose indices are at least b. The unknown series are

    X_r=sum_(k>=0) x_(N+r+kQ)w^k, 1<=r<=Q,
    E=sum_(k>=0) eta_(N+kQ)w^k,
    V_r=sum_(k>=0) u_(N+kQ,r)w^k, 1<=r<Q.

In the sums below residue indices lie in1,...,Q. Set

    D_r=sum_(i+j=r)X_i X_j,    C_r=sum_(i+j=Q+r)X_i X_j,
    S_(r,b)=sum_(b<=i<=N, 1<=t<=Q, i+t-r in Q Z_(>=0)) d_i X_t w^((i+t-r)/Q),
    T_(r,b)=sum_(a>=0, b<=aQ+r<=N)d_(aQ+r)w^a,

    A_r=K_r(P_(>=r)^2)+2S_(r,r)+w^M D_r+w^(M+1)C_r,
    B_r=K_r(P^2)+2S_(r,1)+w^M D_r+w^(M+1)C_r,
    Z_(r,b)=K_r(H P_(>=b))+H_*X_r+E T_(r,b)+w^M E X_r.

Projection of the scalar equalities yields

    V_r=kappa_N[L A_r+Z_(r,Q+1)+2L sum_(j=1)^(r-1)d_j V_(r-j)], r<Q,
    E=(kappa_N/s)[L A_Q+Z_(Q,Q+1)+2L sum_(j=1)^(Q-1)d_j V_(Q-j)],
    X_r=kappa_N[L B_r+Z_(r,1)], 1<=r<=Q.                 (1)

To verify every exponent, the density tail is sum_r z^(N+r)X_r(z^Q) and the harmonic tail is z^N E(z^Q). A product of density tails has degree2N+i+j. Subtracting N+r gives w^M or w^(M+1), according to the two possible residue sums. A known density index i and a tail residue t give exponent i+t-r, exactly S. The four harmonic products are known/known, known/tail, tail/known, and tail/tail; these give the four terms in Z in order. The factor2 in S counts both ordered density factors. The lookahead restriction j>=Q+1 produces Z_(r,Q+1), whereas the ordinary density equation uses Z_(r,1). This proves (1) without a heuristic grouping approximation.

## 3. Analytic certificate and potential

Order Y=(V1,...,V_(Q-1),E,X1,...,XQ). At w=0 every tail/tail term vanishes, H_*=0, S_(r,r)=0, and T_(r,Q+1)=0. Thus the V rows depend only on earlier V rows, and E depends only on V. The X_r row depends only on E and X_t for t<r. Consequently Phi(0,Y)=c0+JY with J nonnegative and strictly lower triangular. Let T=(I-J)^(-1)=sum_(j=0)^(2Q-1)J^j, Y0=T c0, and

    G(w,Y)=Y0+T[Phi(w,Y)-Phi(0,Y)].

Every unknown-dependent term in G has positive w degree and every coefficient is nonnegative. Formal iteration from zero is monotone, stabilizes at every fixed degree, and remains below b at w0. Monotone convergence gives finite coefficient sums at w0. Hence the scalar bounds have geometric base A=w0^(-1/Q), with fixed residue-dependent constants. The norm domination above proves geometric bounds for the actual tuned density and stream.

For any R>A^(Q/2), a sufficiently small positive angular strip and every fixed polynomial factor in n are absorbed by the strict ratio A R^(-2/Q)<1. This proves the weighted derivative convergence and justifies termwise differentiation and multiplication in the stationary equation. The common-potential reconstruction132 has the same geometric base, with the two finite exceptional logarithmic terms already stated. Thus the same strict exterior suffices for every derivative of that potential. Amplitude homogeneity gives the radius factor |epsilon|^(Q/2).

## Evidence requirements and scope

The direct scalar implementation is indexed by total order and checks the residue polynomial independently. Exact rational boxes, root enclosures and upward-rounded initial norms must be retained. Proposed numerical boxes may be found approximately, but only complete exact rational inequalities certify them. The root compatibility and all-index response bounds remain the proved inputs119/123,142/143,130/139,154/155 for Q=3,4,5,6. A finite prefix cannot replace those all-index bounds.

## Completed certificates

The768-bit Cartesian calculation encloses every initial density coefficient through2Q at each of20 exact algebraic roots. All first obstructions contain zero and are projected only using their already proved polynomial compatibility. Eight generic initializations and20 actual profiles pass792 direct total-order/residue coefficient identities. Every rational box2Y0 passes and its immediately preceding dyadic point fails.

The sufficient radius exponents q/2, where w0=2^-q, are:

| Q | Radius exponents in increasing root order |
| --- | --- |
| 3 | 35/2,16 |
| 4 | 43/2,24,25,25,24,49/2 |
| 5 | 61/2,73/2,67/2,67/2,67/2,67/2 |
| 6 | 39,43,43,85/2,41,81/2 |

The actual batch took6.437298230826855 seconds. AtQ6 root1 the chosen response bound is173/10, slightly weaker than the already proved434/25; this does not affect validity. The independent analytic review confirms this h1 initialization. Together with the exact certificates, the stated all-order sufficient radii are PROVED.
