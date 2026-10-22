# Canonical velocity on a fixed transverse jet extension

Topic62. This proves the one-dimensional operators induced by a fixed extension, including their signs, mapping properties and a conditional finite-interval inverse criterion. The result is not an estimate for the full variable-coefficient IPM inverse.

## 1. Setup and exact trace multipliers

Let chi be a real even C2 function onR, compactly supported, equal to1 on[-delta,delta], delta>0. A smooth cutoff is a special case. Let b initially be Schwartz onR, and set

    h(x,y)=Eb(x,y)=y chi(y)b(x).

Use the canonical full-plane velocity U=(-psi_y,psi_x), -Delta psi=h_x, with U=o(r) at infinity. This specifies the velocity uniquely. The x-Fourier convention is bhat(k)=integral exp(-ikx)b(x)dx, inverse factor(2pi)^-1. Put

    I_chi(a)=integral_0^infinity z chi(z)exp(-az)dz, a>=0.

Then the two axis traces have multipliers

    B_chi(k)=-ik I_chi(|k|),
    U1[Eb](x,0)=B_chi b(x),
    U2[Eb]_y(x,0)=-P_chi b(x), P_chi(k)=k² I_chi(|k|).       (1)

At k=0 both displayed multipliers are0 by continuous extension. They are not undefined singular zero-frequency data.

To derive(1), Fourier transformation in x gives

    (-partial_y²+k²)psihat=ik bhat(k)y chi(y).

For a=|k|>0 its decaying Green kernel is exp(-a|y-z|)/(2a), whose derivative at y=0 is sign(z)exp(-a|z|)/2. The right-hand side is odd in z, so psihat_y(k,0)=ik bhat(k)I_chi(a). Taking -psi_y and partial_x psi_y proves(1). This is also consistent with divergence: U2_y=-partial_x U1. The full Fourier multiplier construction for the canonical velocity selects this inverse; no affine harmonic strain is added. Compact support in y and rapid decay in x justify these transforms and the derivatives at the axis. In particular the multipliers in(1) have at most polynomial growth and bhat is rapidly decreasing. The value at a single frequency is irrelevant to L2, and the continuous extensions give the stated value for Schwartz data.

Write ell[h]=psi[h]_xy(0,0) for the strain. The profile scaling functional is ell[h]/3, so

    ell[Eb]=-(P_chi b)(0).                                  (2)

The factor1/3 belongs to scaling, not to the velocity multiplier.

## 2. Explicit convolution kernels and smoothing

Let p_z(x)=z/[pi(x²+z²)] be the one-dimensional Poisson kernel, with Fourier transform exp(-z|k|), z>0. Define

    q(z)=2chi'(z)+z chi''(z),
    S_chi(k)=-integral_0^infinity q(z)exp(-|k|z)dz.

The derivatives of chi vanish on(0,delta), so q is supported away from0. Two integrations by parts give

    integral_0^infinity q(z)exp(-az)dz=-1+a² I_chi(a),
    P_chi=Id-S_chi.                                         (3)

The identity holds also at a=0 by continuity and integral q=-1. In particular S_chi(0)=1.

The operators B_chi and S_chi have integrable convolution kernels

    b_chi(x)=(2x/pi) integral_0^infinity z²chi(z)/(x²+z²)² dz,
    s_chi(x)=-integral_0^infinity q(z)p_z(x)dz.               (4)

For B, use the multiplier -ik exp(-z|k|) of -partial_x p_z and integrate against z chi(z). The kernel is defined almost everywhere; its value at x=0 can be chosen arbitrarily. Since

    integral_R |partial_x p_z(x)|dx=2/(pi z),
    integral_R p_z(x)dx=1,

Tonelli and the triangle inequality prove

    ||b_chi||_1 <= C_B=(2/pi) integral_0^infinity |chi(z)|dz,
    ||s_chi||_1 <= C_S=integral_0^infinity |q(z)|dz.           (5)

These formulas also justify the kernel interchanges. Thus B_chi and S_chi extend boundedly to bounded continuous functions, with those supremum-norm bounds, and

    ||P_chi||_(C_b->C_b)<=1+C_S.                             (6)

The trace formulas for rougher b here mean the continuous extensions of the initially proved trace operators. No unproved bulk C1 regularity of the full velocity for arbitrary bounded b is inferred from that extension.

For every integer N>=0,

    ||S_chi b||_(H^(s+N)) <= C_S C_N(delta)||b||_(H^s),
    C_N(delta)=sum_(j=0)^N binom(N,j)j!delta^-j.              (7)

Indeed |S_chi(k)|<=C_S exp(-delta|k|). Also(1+k²)^(N/2)<=(1+|k|)^N; the bound t^j exp(-delta t)<=j!delta^-j follows from the positive power series for exp(delta t). This proves(7). Every finite ordinary Sobolev derivative gain follows, including real gains by taking a larger integer N.

For B_chi, let M1=integral_0^infinity z|chi(z)|dz and M_infinity=||chi||_infinity. If |k|<=1, |I_chi|<=M1. If |k|>=1, |I_chi|<=M_infinity/|k|². Hence

    ||B_chi b||_(H^(s+1))<=sqrt(2)max(M1,M_infinity)||b||_(H^s). (8)

In high-frequency terminology B_chi has order-1, with leading multiplier -i/k, and P_chi has order0 with leading termId. For example, (3) gives B_chi(k)=(-i/k)(1-S_chi(k)) when k is nonzero. No global smooth-symbol assertion at k=0 is needed, and B_chi is not an order-zero Hilbert transform.

Smoothing is not compactness onR. Choose a nonzero Fourier function supported in a small compact neighborhood of0 where S_chi is nonzero, and let f be its inverse transform, with f in every H^s. Its translations f_n(x)=f(x-nR) have constant H^s norm, while S_chi f_n are translations of the nonzero S_chi f. They converge weakly to0 as n tends to infinity: for each H^(s+N) test function, their inner product is a Fourier integral of an L1 function times exp(-iknR), which tends to0 by the Riemann-Lebesgue lemma. That elementary lemma follows for step functions by direct integration and for L1 functions by approximation. Their norms remain a fixed positive number. Thus no strongly convergent subsequence exists. Consequently S_chi:H^s->H^(s+N) is not compact for any finite s,N for which the displayed maps are defined. Compactness on a bounded interval is a different question requiring a specified extension and restriction.

## 3. The induced jet coupling

Let G1(x)=rho_y(x,0) be a prescribed C1 background trace, and suppose the full linearized axis equation is defined. The canonical normalized coupling at the axis is

    Jh=G1' U1[h](x,0)+G1 U2[h]_y(x,0)
                    +(ell[h]/3)(xG1'+G1).

Substituting(1)-(2) gives the exact one-dimensional operator

    N_chi b=G1' B_chi b-G1 P_chi b
                    -(xG1'+G1)(P_chi b)(0)/3.              (9)

In particular its leading local multiplier is -G1 b. The remaining terms involve the order-1 B_chi, the smoothing S_chi and the strain evaluation. The operator remains nonlocal. This calculation does not justify discarding any of those terms or treating the strain as independent forcing.

## 4. A conditional finite-interval inverse with explicit constants

Let I=[x0,x1], 0<x0<x1, and let e:C(I)->C_b(R) be a specified bounded linear extension that agrees with b on I, with ||e||<=E0. Let G1 be C1 on I and define N b by restricting the right-hand side of(9), with e b in place of b, to I. Then(5)-(6) give

    ||N||_(C(I)->C(I)) <= n,
    n=E0[C_B||G1'||_infinity+(1+C_S)||G1||_infinity
                  +(1+C_S)||xG1'+G1||_infinity/3].          (10)

The scalar(P_chi e b)(0) is bounded by(1+C_S)E0||b||. This bound makes no claim that a particular extension respects all global IPM domain and normalization conditions; those must be checked for an application.

Suppose w,mu are continuous on I, w<0 there, and let Phi>0 solve wPhi'+(mu-1)Phi=0. For

    T b=w b'+(mu-1)b, D(T)={b in C1(I):b(x1)=0},

the Volterra formula gives

    (T^-1 f)(x)=-Phi(x) integral_x^x1 f(t)/[w(t)Phi(t)]dt,
    ||T^-1||_(C->C)<=M,
    M=sup_(x in I) integral_x^x1 Phi(x)/[|w(t)|Phi(t)]dt.    (11)

M is finite because I is compact, w has no zero, and Phi is positive continuous. Differentiation verifies both inverse identities, and the homogeneous identity gives uniqueness. If

    M n<1,

the convergent Neumann series for Id+T^-1 N yields

    ||(T+N)^-1 f||_infinity <= M/(1-Mn)||f||_infinity.       (12)

The fixed point initially lies in C(I), has zero incoming value, and equals T^-1(f-Nb); the right-hand side is C1, so it lies in D(T). This proves existence and uniqueness on the stated domain, not merely an a priori inequality. Nonzero incoming data may be handled by a fixed lift. No values of M,n for the numerical profile are asserted. An origin-weighted interval ending at0 and matching to a source disc require different domain estimates and are not covered by(10)-(12).

## 5. Explicit cutoff for a reproducible constant check

The theorem needs only C2 regularity of chi, not C_infinity. A convenient exact example has delta=1 and support[-2,2]. For z>=0 put

    chi(z)=1, 0<=z<=1;
    chi(z)=1-10u³+15u4-6u5, u=z-1, 1<z<2;
    chi(z)=0, z>=2,

and extend evenly. The first two derivatives match at both joins, so chi is C2. Its derivative in the middle interval is -30u²(1-u)², so0<=chi<=1. Direct polynomial integration gives

    integral chi=3/2, M1=integral z chi=8/7,
    C_B=3/pi, sqrt(2)max(M1,||chi||_infinity)=8sqrt(2)/7.

On0<u<1,

    q=-60u+60u²+180u³-180u4=-60u(1-u)(1-3u²).

It changes sign at u=1/sqrt(3). An antiderivative is -30u²+20u³+45u4-36u5. Splitting at that exact root gives

    C_S=9-16/(3sqrt(3)).                                    (13)

A second evaluation can use midpoint integration of|q|. Its Lipschitz constant is at most200: q'=-60+120u+540u²-720u³ has degree-three Bernstein coefficients(-60,-20,200,-120), whose convex hull contains its range. Absolute value preserves a Lipschitz bound. On N equal subintervals, comparison with each midpoint therefore gives

    |integral_0^1 |q(u)|du - N^-1 sum_(j=0)^(N-1)|q((j+1/2)/N)||
         <=200/(4N).                                      (14)

This bound is elementary: integrate200|u-u_mid| on each subinterval and sum. Exact rational polynomial values avoid sampling assumptions; the Lipschitz remainder covers every point. Arb evaluation of(13) and an independent iv/rational midpoint enclosure using(14) provide two methods for C_S. These are constants of this illustrative extension, not validated constants for a chosen profile inverse.

## 6. Independent positive-series integral enclosure

For the cutoff in section 5 and a>0, let

    M_n = integral_0^2 z chi(z)(2-z)^n dz.

Splitting at z=1 and substituting t=1-z on the first piece gives

    M_n = sum_(j=0)^n binom(n,j)/[(j+1)(j+2)]
          +20/(n+4)-40/(n+5)+27/(n+6)-6/(n+7).              (15)

For the second piece use v=2-z: z chi(z)=20v^3-40v^4+27v^5-6v^6. Both piece integrals are positive, and M_0=8/7. Expanding exp(a(2-z)) with nonnegative terms yields

    L_N = exp(-2a) sum_(n=0)^N a^n M_n/n! <= I_chi(a),
    I_chi(a) <= L_N + (8/7)(2a)^(N+1)/(N+1)!.              (16)

Indeed the exponential Taylor remainder at t>=0 is at most exp(t)t^(N+1)/(N+1)!: writing its series, (N+1+j)! >= (N+1)!j!. Multiplication by exp(-2a), substitution t=a(2-z), and 0<=z<=2 bound the remainder by (2a)^(N+1)/(N+1)! times z chi(z). Integration proves (16). This is a full integral enclosure, not quadrature without a remainder.

The independent Arb method integrates each polynomial times exp(-az) exactly, using the finite antiderivative. The interval method uses rational moments (15), N=160 and (16). Separate validated enclosures need only overlap; the lower-precision one need not be contained in the higher-precision one. A fresh Arb1536 calculation from polynomial derivatives at the endpoints checks that a much narrower third enclosure is contained in both saved enclosures. This is an output consistency audit, not a replacement for either remainder proof.

Dependencies: elementary Fourier Green inversion and the Poisson kernel, derived trace identities, integration by parts, Fourier weighted L2 bounds, the proved midpoint error and a geometric Neumann series. No candidate coefficients or external numerical data enter. OPEN: a domain-compatible longitudinal extension, actual jet inverse constants, all remainder couplings, matching, full inverse and PDE endpoints.
