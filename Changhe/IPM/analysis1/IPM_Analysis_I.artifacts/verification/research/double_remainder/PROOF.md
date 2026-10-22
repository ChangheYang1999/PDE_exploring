# Double Taylor remainders on product power weights

Written 2026-10-20T20:24Z before the numerical implementation. Topic 55. Status OPEN until the source, constants and proof have independent review. This note proves a bound for the renormalized velocity remainder. It does not define the separate canonical moments on arbitrary global product-weight data, prove the annular face trace theorem, or bound the variable-coefficient coupling.

## 1. Statement, notation and dependencies

Let H be a finite-dimensional Euclidean space and let T:L2(R2)->L2(R2;H) be a translation-invariant bounded operator of norm at most A0. Off zero its distribution kernel is a smooth H-valued function K satisfying

    |partial_1^p partial_2^q K(z)| <= D[p,q] |z|^(-2-p-q)

for 0<=p<=N and 0<=q<=M in the zeroth-order theorem, and up to p<=N+m, q<=M+n for the derivative theorem of orders (m,n). A distribution supported at zero is allowed provided the stated L2 bound holds. Let D=C_c^infinity(R2 minus {xy=0}), and initially h belongs to D. Define

    Px^N f = sum_{p=0}^{N-1} x^p partial_x^p f(0,y)/p!,
    Py^M f = sum_{q=0}^{M-1} y^q partial_y^q f(x,0)/q!,
    Rx^N=I-Px^N, Ry^M=I-Py^M, R_NM=Rx^N Ry^M T.

Empty sums are zero, so R_x^0=I. The traces exist for h in D: T applied to smooth compact data is smooth, and the data vanish in an open neighborhood of each axis. The assertion of smoothness follows also by moving arbitrary derivatives to h and using the locally integrable Fourier transform with bounded multiplier. No traces on the completion are presumed.

For E_k={2^k<=|t|<2^(k+1)}, Q_kl=E_k x E_l, define

    Phi_N(d) = 2^((N+1/2)d) for d<=-3,
             = 1 for |d|<=2,
             = 2^((N-1/2)d) for d>=3.

The following explicitly defined B_NM gives

    ||1_Qkl R_NM 1_Qpq||_(2->2) <= B_NM Phi_N(k-p) Phi_M(l-q).      (1)

For real a,b in the strict windows N-1/2<a<N+1/2 and M-1/2<b<M+1/2, put w=|x|^(-2a)|y|^(-2b). Then

    ||R_NM h||_L2(w) <= C_NM(a,b) ||h||_L2(w),                    (2)
    C_NM(a,b)=2^(|a|+|b|) B_NM L_N(a)L_M(b),
    L_N(a)=sum_{d=-2}^2 2^(-ad)
        + 2^(-3(N+1/2-a))/(1-2^(-(N+1/2-a)))
        + 2^(-3(a-N+1/2))/(1-2^(-(a-N+1/2))).

Thus the remainder has a unique bounded extension from the dense class D. This statement is valid without parity. It asserts sufficient strict windows; it does not assert endpoint failure in parity-restricted subspaces.

The only analytic dependencies are Taylor's integral formula, Cauchy-Schwarz/Schur's kernel bound, the elementary one-dimensional convolution inequality, and the L2 Fourier multiplier identity (Plancherel). Their uses are given below. No compactness assertion is involved.

## 2. Explicit block constant

Define finite nonnegative vectors indexed by nonnegative integers. Kronecker delta notation is used. For N>=0 put

    S_N[p] = 1_{p=N} 2^(N+1)(4/3)^(N+1)/N!,
    C_N[p] = 1_{0<=p<N} 4*8^p/p!,
    Lg_N[p] = (8/3)1_{p=0} + 1_{0<=p<N} 2^(p+1)/p!,
    J_N[p] = pi*1_{p=0} + C_N[p].

Here Lg is a vector, distinct from the scalar L_N(a) above. For vectors v,u write [v,u]_D=sum_{p,q} v[p]u[q]D[p,q]. All sums are finite. Define nine constants:

    B_SS=[S_N,S_M]_D, B_SL=[S_N,Lg_M]_D,
    B_LS=[Lg_N,S_M]_D, B_LL=[Lg_N,Lg_M]_D,
    B_SC=[S_N,J_M]_D, B_LC=[Lg_N,J_M]_D,
    B_CS=[J_N,S_M]_D, B_CL=[J_N,Lg_M]_D,
    B_CC=A0 + pi sum_p C_N[p]D[p,0]
                + pi sum_q C_M[q]D[0,q] + [C_N,C_M]_D.

Let B_NM be their maximum. Letters S,L,C mean respectively target much smaller, much larger, or comparable to the source in the corresponding coordinate. In particular all nine cases, including arbitrary aspect ratios, are covered.

## 3. One-coordinate bounds and all nine cases

Write X=2^k,S=2^p,Y=2^l,T0=2^q for the four coordinate scales; in this section T0 is a length, not an operator or a transport margin. Each E interval pair has measure 2 times its scale. If k-p<=-3, then |x|<=2X<=S/4 and |s-theta*x|>=3S/4 for 0<=theta<=1. If k-p>=3 then |x-s|>=3X/4. In the comparable case X/S belongs to [1/4,4]. The same statements hold in y.

Two useful elementary kernel bounds are

    |z|^(-2-p-q) <= |z1|^(-1-p)|z2|^(-1-q),
    integral_R |partial_1^p K(s,t)| dt <= pi D[p,0]|s|^(-1-p).     (3)

The first follows by |z1|,|z2|<=|z| and extends in the usual infinite-upper-bound sense when a coordinate vanishes. For the second substitute t=|s|u and bound (1+u^2)^(-(2+p)/2) by (1+u^2)^(-1). Analogous bounds apply with coordinates exchanged.

In a mixed comparable-separated case the convolution majorant must be uniform in all separated variables. If their relevant distance v has |v|>=v0>0, use

    |partial^q K(u,v)| <= D (u^2+v0^2)^(-(2+q)/2),

where u is the comparable coordinate difference and q is the total derivative order present in this identity term. The right side is independent of the separated variables and has L1 norm at most pi D v0^(-1-q). Take v0=3S/4, 3X/4 or S as appropriate. For a Taylor integral remainder apply Minkowski in its segment parameter before this uniform bound. Thus the comparable-variable L1 bound can be combined with the separated-variable block bound; it does not presume convolution in both variables. This also covers order zero.

For an integral kernel bounded by a constant c on E_X x E_S, its L2 block norm is at most 2 sqrt(XS)c, by Cauchy-Schwarz first in the source variable and then integration in the target. For a kernel whose other coordinate acts by convolution, take its L1 norm in that coordinate first. The elementary L2 convolution bound follows from Minkowski and translation invariance: ||g*f||_2 <= integral |g(t)| ||f(. -t)||_2 dt.

Small target coordinate. Taylor's integral remainder of order N gives the factor (2X)^N/N! times the supremum of the Nth derivative between 0 and x. Applying (3) and the block bound in that coordinate gives

    2 sqrt(XS) (2X)^N/N! (3S/4)^(-1-N)
      = S_N[N] (X/S)^(N+1/2).                                  (4)

For N=0 this is the direct kernel bound; no integral remainder is needed. If the other coordinate is separated, (3)'s product inequality gives its derivative factor. If it is comparable, use its integrated-kernel bound plus each Taylor correction. This gives respectively S_N paired with S_M or Lg_M, or with J_M.

Large target coordinate. Expand Rx^N as identity minus its N Taylor terms. The identity part uses |x-s|>=3X/4, so its factor is

    2 sqrt(XS) (3X/4)^(-1) = (8/3)(X/S)^(-1/2)
                            <= (8/3)(X/S)^(N-1/2).              (5)

For the pth Taylor term, p<N, use |s|>=S. Its factor is

    2 sqrt(XS) (2X)^p/(p! S^(p+1))
       = (2^(p+1)/p!)(X/S)^(p+1/2)
       <= (2^(p+1)/p!)(X/S)^(N-1/2).                            (6)

The comparisons hold because X/S>=8 and N>=0, p+1<=N. Thus Lg_N records all the terms. Pairing with the separated or comparable bounds in the second coordinate gives the L row of cases, with no implicit cancellation or change of sign.

Comparable coordinate. Each pth Taylor correction has exactly the first expression in (6), now bounded by

    (2^(p+1)/p!)4^(p+1/2)=4*8^p/p!=C_N[p].                       (7)

For the identity part, the coordinate integration in (3) contributes pi at derivative order zero. This is J_N when the other coordinate has a separation, so that no singularity remains after that integration. It proves the four mixed cases SC,LC,CS,CL.

Both coordinates comparable. Expand Rx^N Ry^M T=T-Px^N T-Py^M T+Px^N Py^M T. The first term has L2 norm <=A0, including any local term. For Px^N T use (7) and integrate the other coordinate as in (3), giving pi sum C_N[p]D[p,0]. The analogous estimate gives the Py term. For Px^N Py^M T the kernel is evaluated at (-s,-t), both nonzero, and (3)'s product inequality with (7) gives [C_N,C_M]_D. Any distribution at zero contributes to none of these projected terms because the source block is away from the axis. This proves B_CC and completes (1). These arguments define the block operators first on smooth block-interior data and then extend them by their bounded kernels and L2 norm, so nonsmooth dyadic cutoffs cause no trace assumption.

## 4. Conjugation, summation, and the scope of the extension

For one coordinate, on target E_k and source E_p,

    (sup_Ek |x|^(-a)) (sup_Ep |s|^a)
        <= 2^|a| 2^(-a(k-p)).                                  (8)

For a>=0 the endpoint factors are 2^(-ak) and 2^(a(p+1)); for a<0 they are 2^(-a(k+1)) and 2^(ap). This proves (8) for all real a. Applying both coordinates to (1), the norm sequence of the output blocks is bounded by the convolution of the source block norms with

    2^(|a|+|b|)B_NM 2^(-ad)Phi_N(d)2^(-be)Phi_M(e).

The two-dimensional l2 norm of a convolution by a nonnegative l1 sequence is at most its l1 norm times the l2 norm of the input, again by Minkowski applied to the sum of shifted sequences. The exact geometric sums are precisely L_N(a), L_M(b); their two tail ratios are less than one in the stated windows. This proves (2) first for finite source sums, including every h in D. Density follows by cutting off near the axes and infinity and then mollifying away from the axes, since w is smooth positive and locally bounded above and below there. It proves the unique bounded extension.

Even if h is even in x and odd in y, its individual global moments can be unbounded on this pure weight, as separately proved in topic 51 (a cited dependency for this scope warning only, not for (1)-(2)). The bounded extension in (2) retains the cancellations defining the double remainder; it is not a decomposition into individually bounded velocity and Taylor maps. The assertion makes no claim about the full coupled linearized equation.

## 5. IPM kernel, and finite conormal derivatives

For the vector IPM operator, the Fourier symbol is (xi*eta,-xi^2)/(xi^2+eta^2), whose Euclidean norm is |xi|/sqrt(xi^2+eta^2)<=1. Off zero,

    K2+i K1 = (1/(2pi))(x+i y)^(-2).

Differentiating gives complex modulus (p+q+1)!/(2pi)|z|^(-2-p-q), so we may use A0=1 and D[p,q]=(p+q+1)!/(2pi), simultaneously for the vector norm. The local term -h e2/2 is included in the Fourier multiplier and the CC base term.

Let Dx=x partial_x and Dy=y partial_y. Direct differentiation of Taylor monomials gives [Dx,Px^N]=0, [Dy,Py^M]=0, and the other pairs commute. Fourier differentiation gives [Dx,T] with symbol -xi partial_xi m and off-zero kernel (1+z1 partial_1)K. Similarly for Dy. Hence on D,

    Dx^m Dy^n R_NM h
       = sum_{p<=m,q<=n} binom(m,p)binom(n,q)
           Rx^N Ry^M T_pq Dx^(m-p)Dy^(n-q)h,                    (9)
    symbol(T_pq)=(-xi partial_xi)^p(-eta partial_eta)^q m.

The two commutator operations commute. Every symbol is smooth on the unit circle and degree zero, so bounded. Explicit constants, without an unspecified continuity argument, are as follows. Let A[p,r] be the Stirling number S(p+1,r+1); equivalently A[0,0]=1 and A[p+1,r]=(r+1)A[p,r]+A[p,r-1], with missing indices zero. Induction gives

    (1+z partial_z)^p=sum_r A[p,r] z^r partial_z^r.

By Leibniz and |z_i|<=|z|, valid derivative bounds for the off-zero kernel of T_pq are

    D_pq[a,b]=sum_{r<=p,s<=q} A[p,r]A[q,s]
       sum_{i<=min(a,r),j<=min(b,s)} binom(a,i)binom(b,j)
          (r)_i (s)_j D[r+a-i,s+b-j],                           (10)

where (r)_i=r!/(r-i)!. To bound the multiplier norm, write a component as P/(xi^2+eta^2)^d with a homogeneous integer polynomial P of degree 2d, initially P=xi eta or -xi^2, d=1. The operation -xi partial_xi replaces P by

    -xi(xi^2+eta^2)partial_xi P+2d xi^2 P,

and replaces d by d+1; exchange xi,eta for the other operation. On the unit circle the sum of the absolute coefficients of P bounds its absolute value. The sum of these two component bounds bounds the vector symbol, and A0=1 is sharper for p=q=0. This gives a finite explicit A0[p,q]. For every T_pq, a kernel term at zero enters only the unprojected CC block and is automatically included by this multiplier bound. It contributes to no separated or projected block, by the same support argument as in section 3. Apply sections 2-4 with (10) and A0[p,q] to each summand of (9).

For clarity, the resulting derivative estimate is asserted on D and on its completion in the norm sum_{i<=m,j<=n}||Dx^i Dy^j h||_L2(w). Derivatives of the extended output are distributional: convergence in the component norms implies convergence in distributions on every compact set off the axes, so (9) passes to the limit there. This does not assert classical axis traces or a larger maximal graph domain.

## 6. Computational checks to accompany the proof

All mathematical parameters are exact rationals. Compute the nine block constants and C_NM(a,b) using Arb512 and independently using mpmath.iv at 160 or more decimal digits. The Arb path uses the finite vectors above. The independent path must enumerate the nine cases directly from (4)-(7), and obtain the geometric sum using a finite sum plus its rigorously bounded tails, not simply call the same vector routine. Both methods use the proved factorial kernel bound. Store exact dyadic endpoints and compare them using exact rationals. Independently recompute the multiplier recurrences and kernel algebra with integer polynomial identities. Record all truncation bounds, library versions, and source hashes. These scalar checks cannot establish omitted analytic hypotheses of the coupled inverse.

Revision 2026-10-20T20:28:47.121673+00:00: actual Opus5.5 first review accepted the analytic argument with the uniform mixed-case majorant made explicit. Numerical and commutator closure remains OPEN.

## 7. Independent exact pi certificate for block constants

A saved-output auditor can additionally bound the nine B values without trusting either interval library. Let A_n(x)=sum_{j=0}^{n-1}(-1)^j x^(2j+1)/(2j+1), with even n=320. Integrating the finite geometric expansion of1/(1+t^2) from0to x proves A_n(x)<atan(x)<A_n(x)+x^(2n+1)/(2n+1) for0<x<1. Machin's identity pi=16atan(1/5)-4atan(1/239) follows by the tangent addition formula: tan(4atan(1/5))=120/119 and tan(4atan(1/5)-atan(1/239))=1. The latter angle lies in(0,1), hence in(0,pi/2), so equals pi/4. Here pi/2>1 follows, for example, from atan(1)>1/2 by integrating1/(1+t^2)>1/2 on(0,1). These facts give exact rational endpoints for pi. Every B case above has the form alpha+beta/pi with nonnegative rational alpha,beta, since the both-comparable base term is treated separately. Substitution reverses the pi endpoints in beta/pi. The auditor uses these exact intervals to check all saved B enclosures; it separately evaluates the weighted scalar expressions at higher Arb precision and checks containment in both saved arithmetic paths. It does not regenerate either original core execution.
