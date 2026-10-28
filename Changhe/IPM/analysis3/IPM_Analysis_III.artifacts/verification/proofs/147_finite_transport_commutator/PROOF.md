# A finite Taylor proof of the transport commutator

## Statement and notation

Let C=R times S1. Let s and Lambda be real smooth bounded functions with all derivatives bounded and

 41/20<=s(X)<=25/4.

Fix N>=0, A=Op(a), a(X,xi)=e^(N Lambda(X))<xi>^s(X), and let B be a real vector field and c a real scalar coefficient in W^(7,infinity)(C). Use uniform left quantization, or a properly supported version which differs from it by a uniformly smoothing operator. Let P=B.grad+c and w=Av. Put

 kappa=div B/2-c,     ell_B=B.grad s,
 M_B=(kappa+N B.grad Lambda)I-s sym DB,
 R=grad<D>^(-1).

For every 0<epsilon<=1/32 and every eta>0,

 -Re<APv,w>=<M_B Rw,Rw>+Re<ell_B log<D> w,w>+E(v),        (1)

where

 |E(v)|<=eta||v||H^s^2+C_eta||v||H^(s-epsilon)||v||H^s.  (2)

The identity is initially interpreted for compactly supported smooth v. The constants are uniform under translation in t. The small high-norm error arises only from converting a left principal operator to the matrix quadratic form. Before that conversion, the transport commutator remainder has a pure lower-order bound. This proves a sufficient version of Q1; it does not by itself extend (1) to the maximal graph domain.

The theorem also applies at constant order sigma=25/4 to the cofactor transport, with its actual divided scalar coefficient c. That coefficient has W^(7,infinity) regularity by proof 126. On the angular overlap the cutoff forcing is handled separately.

## Kernel Taylor lemma

Set r=13/2. A W^(7,infinity) coefficient q belongs uniformly to C^(6,1/2), with norm controlled by its bounded derivatives up to7. We prove

 [A,M_q]f=sum_(1<=|alpha|<=6) (1/i)^|alpha|/alpha!
               M_(partial^alpha q) Op(partial_xi^alpha a)f+T_q f,
 ||T_q f||_2<=C||q||C^(6,1/2)||f||_2.                  (3)

In a chart write z=X-Y and expand q(Y) at X to degree6. The remainder is bounded by C|z|^(13/2). Away from z=0 the kernel K_A satisfies

 |K_A(X,X-z)|<=C|z|^(-2-25/4),   0<|z|<=1.             (4)

One can verify (4) directly by dyadic decomposition in xi: the frequency-j kernel is bounded by C_M 2^(j(2+s(X)))(1+2^j|z|)^(-M); sum below and above 2^j|z|=1, with M>2+25/4. This bound uses no derivative of s in X. The coefficient e^(N Lambda) is uniformly bounded. Multiplying (4) by the Taylor remainder gives C|z|^(-7/4), which is locally integrable in dimension2. The same bound controls row and column integrals. Outside the unit neighborhood the properly supported kernel is smooth and bounded; the nonproper version has arbitrarily summable decay from frequency integration by parts. Schur's test therefore proves the second line of (3).

Each polynomial Taylor term is exactly the corresponding frequency derivative of the symbol, with the factor (1/i)^|alpha|. This is a distributional identity. To justify it with a finite-regularity q, first mollify q, apply the identity, and pass to the limit in the polynomial terms and in the remainder by their uniform bounds and dominated convergence on test functions. Alternatively the remainder vanishes to order greater than the kernel order, so its kernel product is directly defined by the integrable function just estimated. Possible distributions supported on z=0 are killed by this vanishing. Chart cutoffs add only uniformly smoothing terms, included in T_q.

This argument is why the strict inequality r>max s matters. It does not assume seven or more derivatives of the input f, nor any unverified infinitely smooth actual coefficient.

## The first-order commutator

Apply (3) to q=B_j and f=partial_j v. For |alpha|>=2, the smooth operator Op(partial_xi^alpha a)partial_j has variable order s-|alpha|+1<=s-1. Its map H^(s-epsilon)->L2 is bounded by the smooth variable-order calculus checked in proof 144. The factor partial^alpha B_j is only used as a bounded L2 multiplier. The remainder T_(B_j)partial_j v is bounded by ||v||H^1, which is controlled by ||v||H^(s-epsilon). Thus only |alpha|=1 remains at principal order:

 sum_j[A,B_j]partial_j v
 =sum_(i,j)(partial_i B_j) Op(s a xi_i xi_j/<xi>^2)v+E_0v,
 ||E_0v||_2<=C||v||H^(s-epsilon).                       (5)

The sign in (5) is positive: (1/i) from the Taylor term cancels i from partial_j. The smooth composition formula, now involving only s,Lambda and the smooth frequency multiplier, gives

 Op(s a xi_i xi_j/<xi>^2)v
    =s(X) Op(xi_i xi_j/<xi>^2)w+E_(ij)v,                (6)

with the same lower-order bound. In particular no derivative of B is needed in this composition.

The same Taylor lemma with q=c and f=v shows

 ||[A,c]v||_2<=C||v||H^(s-epsilon),                     (7)

since every polynomial term has order at most s-1 and its remainder is bounded on L2.

## Isolating the variable logarithm exactly

For left quantization,

 [partial_j,A]=Op(partial_j a),
 partial_j a=a(N partial_j Lambda+partial_j s log<xi>).

Let L_j=N partial_j Lambda+partial_j s log<xi>. Smooth composition gives

 Op(a L_j)v=Op(L_j)w+F_jv,
 ||F_jv||_2<=C||v||H^(s-epsilon).                       (8)

Indeed the first nonleading term has relative order -1 with finitely many logarithmic factors. Also Op(L_j)=N partial_j Lambda+(partial_j s)log<D> exactly. Combining (5)-(8) yields

 APv=B.grad w+(c-N B.grad Lambda)w
          -(B.grad s)log<D>w
          +sum_(i,j)s(partial_i B_j)Op(xi_i xi_j/<xi>^2)w+Ev,
 ||Ev||_2<=C||v||H^(s-epsilon).                         (9)

Thus the coefficient of the logarithm is the actual B.grad s. No smoothing of B changes its sign. This is essential when using the monotonicity B.grad s>=0.

## Passing to the matrix form

Integration by parts in B.grad w gives div B/2. The principal scalar and quadratic forms in (9) then have the left symbol

 kappa+N B.grad Lambda-s sum_(i,j)(partial_i B_j)xi_i xi_j/<xi>^2.

All matrix coefficients are uniformly continuous and bounded, in fact C^(5,1/2) or better. We use the following elementary approximation argument to convert them to the displayed R form. For any such matrix coefficient m, approximate it uniformly by smooth bounded m_j with all bounded derivatives. The L2 operator norm of multiplication by m-m_j is its supremum norm. The corresponding left multiplier and the form <m Rw,Rw> therefore differ from their smooth approximations by at most C||m-m_j||_infinity||w||_2^2.

For smooth m_j, composition of R_i^*, multiplication by m_j and R_j has the indicated principal symbol; its difference from left quantization has order -1. Likewise replacing a scalar form <m_j w,w> by sum_i<m_j R_iw,R_iw> has an order -1 remainder (including the inhomogeneous order -2 correction). Consequently these smooth differences are bounded by C_j||w||H^(-epsilon)||w||_2. Choose j to make the first error smaller than eta, and use proof 144 to bound ||w||H^(-epsilon) by ||v||H^(s-epsilon). This proves (1)-(2). The antisymmetric part of DB contributes zero to the symmetric quadratic form, so the matrix is sym DB with the exact sign stated.

The same argument works uniformly on the whole cylinder: convolution gives a global uniform approximation, and all smooth remainders have uniform seminorms. Their constants may grow with j, which is allowed in C_eta. No compact support or compactness claim is used at this step.

## Application to the actual transport

For the bulk coefficient c=beta q-1 and B=W=(q,vartheta), div W=2 c_l-2q, so

 kappa_v=1+c_l-(1+beta)q.

For the uncut cofactor coefficient c=beta q+vartheta p'/p-1,

 kappa_u=1+c_l-(1+beta)q+2 vartheta tan theta-vartheta cot theta.

These are exactly the matrices in proof 142 and the theory author's Hs formula. The divided coefficients extend with the verified W^(7,infinity) regularity. In the cofactor calculation extend them smoothly in angle outside a larger vertical sector, preserving their finite uniform regularity; the support correction of proof 144 handles the resulting off-sector terms. The logarithmic term vanishes there because the cofactor order is constant.

The proof confirms Q1 with the explicit error (2). It does not claim a numerical constant or a full high inverse. A separate argument must pass the energy inequality from test functions to h in the maximal transport domain; smooth density in X_s alone is not enough.
