# Local corner coupling with a smooth factor

Topic 57. This argument is written before its numerical implementation. Its application is conditional on a C8 factor. The current modal trial does not satisfy that hypothesis, as topic 50 proves. No inverse or existence assertion is made here.

## 1. Statement and notation

Write B_d={x²+y²<d²}, Q_d=(-d,d)² and fix d=1/2. Let

    11/2<a<13/2, 5/2<b<7/2, A=a+b,
    w_ab(x,y)=|x|^(-2a)|y|^(-2b).

Initially h is smooth, compactly supported away from the axes, even in x and odd in y. Its velocity U is the canonical full-plane IPM velocity. The Fourier symbol is (xi eta,-xi²)/(xi²+eta²), and the distribution kernel is its principal-value kernel plus the local term -h e2/2. Off zero,

    K2(z)+i K1(z)=(z1+i z2)^(-2)/(2 pi).

In this note c=psi[h]_xy(0)=-partial_x U1(0) denotes the strain, without the factor 1/3. The scaling correction is c/3. Put W=U+(c/3)X. Let alpha be real, even in both coordinates, and C8 on a neighborhood of the closed disk B_d. Define

    rho=x² y alpha, G=W·grad rho,
    H_alpha=max_{p+q<=8} sup_{B_d} |partial_x^p partial_y^q alpha|.

For a smooth function F define R_x^N F=F-sum_{j<N} x^j partial_x^j F(0,y)/j!, with R_x^0=I, and similarly R_y^M. Taylor segments remain in B_d because |(t x,s y)|<=|(x,y)| for t,s in [0,1]. Thus the target expression R_x^6 R_y^3 G is well-defined on B_d without an extension of alpha outside the disk.

There is an explicit constant C_unit(a,b) such that, for h supported in Q_1,

    ||R_x^6 R_y^3 G||_{L2(B_d,w_ab)}
       <= C_unit(a,b) H_alpha ||h||_{L2(w_ab)}.                 (1)

There is also an explicit C_comp(a,b,gamma) such that, when 1<gamma<2 and

    w_comp=w_ab (1+r)^(2(A-gamma)),

arbitrary h in the initial class satisfy

    ||R_x^6 R_y^3 G||_{L2(B_d,w_ab)}
       <= C_comp(a,b,gamma) H_alpha ||h||_{L2(w_comp)}.         (2)

All constants are specified below. Each map extends uniquely from its initial parity class by the corresponding norm. The extension is the coupling remainder as a whole. It does not assert classical traces of the velocity or arbitrary density on the axes, or an independently defined global canonical velocity for every element of the completion.

## 2. Dependency: the complete double-remainder estimate

Topic 55, research/double_remainder/PROOF.md and its accepted evidence/verdict.json, proves the following. For integers N,M>=0 and weights u,v with

    N-1/2<u<N+1/2, M-1/2<v<M+1/2,

both velocity components obey

    ||R_x^N R_y^M U_i[h]||_{L2(w_uv)}
        <= C_NM(u,v) ||h||_{L2(w_uv)},                         (3)
    C_NM(u,v)=2^(|u|+|v|) B_NM L_N(u)L_M(v),
    L_N(u)=sum_{t=-2}^2 2^(-u t)
       +2^(-3(N+1/2-u))/(1-2^(-(N+1/2-u)))
       +2^(-3(u-N+1/2))/(1-2^(-(u-N+1/2))).

For reproducibility, the finite block constants used here are restated. For p,q>=0 set D[p,q]=(p+q+1)!/(2 pi). Define finite vectors

    S_N[p]=1_{p=N} 2^(N+1)(4/3)^(N+1)/N!,
    C_N[p]=1_{p<N} 4*8^p/p!,
    Lg_N[p]=(8/3)1_{p=0}+1_{p<N}2^(p+1)/p!,
    J_N[p]=pi 1_{p=0}+C_N[p].

Let [v,z]=sum_{p,q}v[p]z[q]D[p,q]. The number B_NM is the maximum of

    [S_N,S_M], [S_N,Lg_M], [Lg_N,S_M], [Lg_N,Lg_M],
    [S_N,J_M], [Lg_N,J_M], [J_N,S_M], [J_N,Lg_M],
    1+pi sum_p C_N[p]D[p,0]+pi sum_q C_M[q]D[0,q]+[C_N,C_M].

The proof of (3) treats all nine scale cases and arbitrary aspect ratios. Its local distribution term is covered by the L2 norm of the Fourier multiplier, at most one. In particular N=0 or M=0 is permitted. Only the already proved zeroth remainder theorem is a dependency here; no unproved conormal or trace estimate is invoked.

## 3. An exact Taylor product formula

For integers N,M>=0 and beta in C^(N+M) on B_d there are coefficient functions beta_ij, 0<=i<=N, 0<=j<=M, such that

    beta=sum_{i=0}^N sum_{j=0}^M x^i y^j beta_ij,
    |beta_ij|<=sup_{B_d}|partial_x^i partial_y^j beta|/(i! j!). (4)

If i<N then beta_ij is independent of x, and if j<M it is independent of y. To construct them, in each coordinate use Taylor coefficients up to order N-1 (or M-1) and the integral remainder divided by x^N (or y^M). At positive order N the final coefficient is

    integral_0^1 (1-t)^(N-1) partial_x^N beta(t x,y) dt/(N-1)!,

whose bound is sup|partial_x^N beta|/N!. At order zero the operation is simply beta. Apply the two commuting one-coordinate expansions. Their differentiated integral expressions prove (4), including either zero order.

For any smooth F the following identity holds:

    R_x^N R_y^M(beta F)
      =sum_{i=0}^N sum_{j=0}^M x^i y^j beta_ij
                                  R_x^(N-i) R_y^(M-j) F.     (5)

For i<N the x-independent coefficient commutes with the x Taylor operator and R_x^N(x^i F)=x^i R_x^(N-i)F. For i=N the product has a factor x^N, its Taylor polynomial of degree N-1 vanishes, and R_x^(N-i)=I. The identical argument in y proves (5) term by term. This proof explains why a general, unexpanded variable coefficient cannot simply be moved through the Taylor projections.

## 4. Coupling algebra and the supported-data estimate

Set

    beta1=2 alpha+x alpha_x,
    beta2=alpha+y alpha_y,
    beta0=3 alpha+x alpha_x+y alpha_y.

Then grad rho=(xy beta1,x² beta2), X·grad rho=x² y beta0, and exact monomial extraction gives

    R_x^6 R_y^3 G
       =xy R_x^5 R_y^2(beta1 U1)
        +x² R_x^4 R_y^3(beta2 U2)
        +(c/3)x² y R_x^4 R_y^2 beta0.                        (6)

For i+j<=7, the product rule implies

    |partial_x^i partial_y^j beta1| <= (2+i+d) H_alpha,
    |partial_x^i partial_y^j beta2| <= (1+j+d) H_alpha.         (7)

For example the derivative of x alpha_x is i partial_x^i partial_y^j alpha+x partial_x^(i+1) partial_y^j alpha. The largest derivative of alpha in (7) is order eight. The strain term has the bound

    |R_x^4 R_y^2 beta0|
       <= |x|^4 |y|² (9+2d) H_alpha/(4! 2!).                 (8)

Here partial_x^4 partial_y^2 beta0=9 alpha_42+x alpha_52+y alpha_43. Taylor's integral formula in both coordinates proves (8).

For the first sum in (6), apply (5) with N=5,M=2. The (i,j) term has factor x^(1+i)y^(1+j), hence its target norm is bounded using (3) with

    N=5-i, M=2-j, u=a-1-i, v=b-1-j.

Its two strict weight gaps are exactly a-11/2,13/2-a and b-5/2,7/2-b. For h supported in Q_1,

    ||h||_{L2(w_uv)}<=||h||_{L2(w_ab)}                       (9)

because the ratio of weights is |x|^(2+2i)|y|^(2+2j)<=1. The second sum uses N=4-i,M=3-j,u=a-2-i,v=b-j, and the same argument with the nonnegative shifts 2+i,j. No restriction of the target velocity to the support of h is being used in (3).

Define

    C_vel=sum_{i=0}^5 sum_{j=0}^2
        (2+i+d)/(i! j!) C_(5-i,2-j)(a-1-i,b-1-j)
      +sum_{i=0}^4 sum_{j=0}^3
        (1+j+d)/(i! j!) C_(4-i,3-j)(a-2-i,b-j).              (10)

The bounds just proved give C_vel H_alpha ||h|| for the first two terms in (6). There are 38 terms, each in the strict range of (3).

For the strain, differentiation of the complex kernel gives

    c=(1/pi) integral h(r,theta) sin(3theta) r^(-3) dX.

There is no local term near the origin for the initial data. Dropping sin²(3theta)<=1 in the weighted Cauchy-Schwarz inequality, and enlarging Q_1 to the disk r<sqrt(2), yields

    |c|<=C_str ||h||_{L2(w_ab)},
    C_str=(1/pi) sqrt( B(a+1/2,b+1/2) 2^(A-2)/(A-2) ).       (11)

Indeed the angular integral of |cos theta|^(2a)|sin theta|^(2b) is 2 B(a+1/2,b+1/2), and the radial integral is 2^(A-2)/(2A-4). Both are finite. Define the elementary monomial norm bound

    M_d=sqrt( [2 d^(13-2a)/(13-2a)]
                  [2 d^(7-2b)/(7-2b)] ),
    H0=(9+2d)/(3*4!*2!),
    C_unit=C_vel+H0 C_str M_d.                              (12)

The number M_d is exactly ||x^6 y^3||_{L2(Q_d,w_ab)}, and therefore bounds its disk norm. Equations (6)-(12) prove (1).

## 5. Distant density and the composite weight

Split h=h_near+h_far using the characteristic functions of Q_1 and its complement. For the initial data, any loss of smoothness of h_near at the boundary of Q_1 is away from the target disk. Choose smooth even cutoffs chi_n supported in Q_1, equal to one on Q_0.9 for all large n, bounded between zero and one, and converging almost everywhere to 1_Q1. Then h chi_n converges to h_near in L2(w_ab) by dominated convergence. The difference h(chi_n-1_Q1) is supported at distance at least0.4 from B_d, in the fixed compact support of h and away from the axes. Weighted Cauchy-Schwarz applied to each kernel derivative through order7 therefore gives uniform convergence of its velocity in C7(B_d) to zero; the same applies to the strain at the origin. These estimates use bounded kernel derivatives on that separated support. Consequently the expressions in (6) converge classically on B_d and in their weighted target norm by (1), so the bounded extension agrees with the original expression for h_near. The boundary has measure zero. For h_far, r>=1 while |X|<=d=1/2.

Parity gives integral K_i(-Z) h_far(Z) dZ=0 for compactly supported data. Thus on B_d

    U_i[h_far](X)=integral [K_i(X-Z)-K_i(-Z)] h_far(Z) dZ.    (13)

The local term is zero there. For q>=0 let D_q=(q+1)!/(2pi) and put

    F_0=d D_1 (1-d)^(-3),
    F_q=D_q (1-d)^(-2-q), 1<=q<=7.

Every Cartesian derivative of total order q>=1 of the kernel in (13) has modulus at most F_q r^(-3): differentiate the analytic z^(-2) kernel and use |X-Z|>=(1-d)r and r^(-2-q)<=r^(-3). At order zero integrate the complex directional derivative on the segment from -Z to X-Z, giving F_0 r^(-3). Its directional factor is |X|, so no componentwise sum or missing sqrt(2) is involved.

Since A>gamma and 1+r>=r,

    integral_{r>=1} r^(-6)/w_comp dX
       <= 2 B(a+1/2,b+1/2) integral_1^infinity r^(2gamma-5) dr
       =2 B(a+1/2,b+1/2)/(4-2gamma).

Define

    T_gamma=sqrt(2 B(a+1/2,b+1/2)/(4-2gamma)).

Weighted Cauchy-Schwarz now proves, for every multi-index nu of size q<=7,

    sup_{B_d}|partial^nu U_i[h_far]|
        <= F_q T_gamma ||h_far||_{L2(w_comp)}.               (14)

It also proves |c[h_far]|<=D_1 T_gamma ||h_far|| at the origin, without the distance loss. These bounds permit all differentiations under the integral for q<=7. Formula (13) defines a local smooth velocity for general far data of finite composite norm by the same absolute estimates, consistently with the canonical velocity on the initial class. No global completion claim is needed.

Apply the ordinary two-coordinate Taylor remainder to beta1 U1 in (6), then Leibniz and (7),(14). Define

    S1=(1/(5!2!)) sum_{p=0}^5 sum_{q=0}^2
          binom(5,p)binom(2,q)(2+p+d) F_(7-p-q),
    S2=(1/(4!3!)) sum_{p=0}^4 sum_{q=0}^3
          binom(4,p)binom(3,q)(1+q+d) F_(7-p-q),
    C_far=M_d T_gamma (S1+S2+H0 D_1).                       (15)

All three terms of (6) for h_far are bounded by C_far H_alpha ||h_far|| in the target norm. For example the first is bounded pointwise by |x|^6|y|^3 S1 T_gamma H_alpha ||h_far||. The last follows from (8) and the strain bound.

For the near part, (1) and (1+r)^(2(A-gamma))>=1 give the bound C_unit H_alpha ||h_near||_{L2(w_comp)}. The two source pieces are orthogonal in L2(w_comp). The triangle inequality followed by the scalar Cauchy-Schwarz inequality gives (2) with

    C_comp=sqrt(C_unit²+C_far²).                             (16)

This estimate does not assert that the two target pieces are orthogonal.

## 6. Extension and mathematical scope

The initial compact smooth parity class is dense in the corresponding weighted parity spaces: cut off at infinity and near the axes, then mollify on compact sets separated from the axes and symmetrize. The weights are smooth and locally bounded above and below there. The supported version uses the analogous dense class in Q_1. Inequalities (1),(2) therefore extend the linear map h to its unique bounded remainder. Linearity includes the exact strain normalization c/3. The constants multiply the stated C8 norm of alpha.

This proves a local zeroth-order bound only. It supplies no edge-matching theorem, conormal derivative bound, compactness, smallness, invertibility, nonlinear estimate without loss, or full-plane solution. The target product weight is specified explicitly. Replacing it with the lead's full norm requires the other pieces of that norm. A modal trial whose center factor is not C2 cannot be inserted into this C8-factor theorem.

## 7. Planned executable evidence

Before acceptance, independently check the Taylor product identity on rational polynomial families, the kernel derivative and strain signs, the two product-rule constants, every shifted weight window, and the finite sum coefficients. Compute (10)-(16) at the two exact pairs (129/20,307/100) and (1299/200,3403/1000), with gamma=1129/1000, using separate Arb and mpmath.iv code paths. The iv beta integral is to use positive interval sums and an exact mesh, not the Arb special function. Preserve source, dependency and output hashes, finite-tail bounds, public exact ceilings, actual runtime, and the actual Opus5.5 review. No numerical constant is asserted before those checks finish.
