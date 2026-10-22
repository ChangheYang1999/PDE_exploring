# Independent canonical moment archive validation

2026-10-21. Written before the new computation. Preparation only until every stated finite comparison has completed.

## Exact statement and input

Use the normalized modal_v2 trial and its exact degree7 spline with260 angular input modes. All binary source values are interpreted as exact rationals through data_exact/modal_v2.json. Let a_0<...<a_S, S=1558, be the distinct original knots. The density is rho=r^3 sum_(j=0)^261 H_j(log r) sin((2j+1)theta), with H_261=0. On each knot span H_j is a polynomial of degree at most7. The scalar normalization correction z belongs to the previously accepted exact interval Z from research/modal_repair/evidence/independent_gauss_iv.json. Our calculations retain its affine dependence explicitly.

Define, for1<=n<=261 and m=2n,

 I_n(t)=integral_-infinity^t exp(-(m+4)(t-s)) H_(n-1)(s) ds,
 J_n(t)=integral_t^infinity exp(-(m-4)(s-t)) H_n(s) ds.

The exterior powers specified below make both integrals absolutely convergent. The finite task is to prove that every archive H coefficient and every I_n(a_i), J_n(a_(i+1)) belongs to its exact serialized midpoint/radius interval. There are1558*262*8=3265568 H coefficients and1558*261*2=813276 moment targets. Complete directed containment is required, not mere overlap. A failed sufficient containment test is OPEN, not a refutation of the archive.

## Spline and angular reconstruction

On the open span (a,b) use u=(t-a)/(b-a). Start with the single active degree0 B-spline B_ell,0=1. Repeatedly apply the defining Cox recurrence

 B_i,p(t)=(t-k_i)/(k_(i+p)-k_i) B_i,p-1(t)
          +(k_(i+p+1)-t)/(k_(i+p+1)-k_(i+1)) B_i+1,p-1(t),

omitting a term whose denominator is zero. Each factor is an exact affine polynomial in u, so this constructs the eight degree7 active basis polynomials exactly. Multiply by the original exact S control coefficients. Continuity gives the endpoint values and all one-sided polynomial derivatives used below. The trial definition prescribes matching derivatives through order6.

For the original factor modes T_l, the angular conversion is8H_0=2T_0-T_2,8H_1=2T_0+T_1-T_2-T_3 and, for j>=2,8H_j=T_(j-1)+T_j-T_(j+1)-T_(j+2), where out-of-range modes vanish. It follows by multiplying the cosine factor by the fixed sine factor and collecting positive and negative odd frequencies; equivalently each input mode contributes frequencies1+2l,1-2l,3+2l,3-2l with its sine sign. These two descriptions must agree exactly at source construction. This also proves H_261=0.

If Q(u)=sum Q_k u^k, the archive's coefficient of x^j for x=t-(a+b)/2 is h^(-j) sum_(k>=j) binom(k,j)Q_k/2^(k-j), h=b-a. This is the exact binomial theorem and is checked for every coefficient.

## Complete analytic tail anchors

At the inner boundary a_0 write s=t-a_0<=0 and

 H_j(a_0+s)=C_j+sum_(l=0)^6 D_jl exp((2l+2)s)+exp(b_i s)sum_(l=0)^6 e_jl s^l.

The exact C,D follow the same angular conversion. If j_v is the v-th one-sided spline derivative and p_v is the v-th derivative of the first two terms at s=0, then

 e_jl=sum_(v=0)^l (-b_i)^(l-v)(j_v-p_v)/(v!(l-v)!).

This is coefficient comparison after multiplying the jet discrepancy by exp(-b_i s). Therefore the complete inner integral is

 I_n(a_0)=C_(n-1)/(m+4)+sum_l D_(n-1,l)/(m+6+2l)
          +sum_l e_(n-1,l)(-1)^l l!/(m+4+b_i)^(l+1).

Every denominator is positive. The monomial integral is obtained by s=-v and l integrations by parts, or the elementary gamma integral l!/c^(l+1). It covers the entire infinite inner tail.

At the outer boundary a_S write u=t-a_S>=0. Before the normalization correction,

 H_j(a_S+u)=sum_l A_jl exp(alpha_l u)+exp(-b_o u)sum_(l=0)^6 e^o_jl u^l,
 alpha_l=k-3-j_l(1-k)-2l_l.

The indices(j_l,l_l) and exact A coefficients are input data. With outer spline jets j^o_v and p^o_v=sum_l A_jl alpha_l^v,

 e^o_jl=sum_(v=0)^l b_o^(l-v)(j^o_v-p^o_v)/(v!(l-v)!).

The normalization adds C_j z times exp(alpha_0 u)-exp(-b_o u)sum_(l=0)^6(alpha_0+b_o)^l u^l/l!, whose first seven jets vanish. Hence J_n(a_S)=U_n+V_n z, where

 U_n=sum_l A_nl/(m-4-alpha_l)+sum_(l=0)^6 e^o_nl l!/(m-4+b_o)^(l+1),
 V_n=C_n[1/(m-4-alpha_0)-sum_(l=0)^6(alpha_0+b_o)^l/(m-4+b_o)^(l+1)]
    =C_n(alpha_0+b_o)^7/[(m-4-alpha_0)(m-4+b_o)^7].

The last equality is the finite geometric identity. All m-4-alpha_l and m-4+b_o must be strictly positive. Thus these integrals converge absolutely and the displayed formulas evaluate the complete infinite outer tail, including normalization. Both exact formulas for V must agree.

## Independent propagation formula and proof

For y'(u)=zeta y(u)+P(u) on0<=u<=1 with polynomial P of degree d<=7 and zeta nonzero, set q_(d+1)=0 and compute backwards

 q_k=((k+1)q_(k+1)-P_k)/zeta.

Coefficient comparison gives q'-zeta q=P. Thus y(1)=q(1)+exp(zeta)(y(0)-q(0)). When zeta=0 use y(1)=y(0)+sum_k P_k/(k+1). These are exact identities; outward interval evaluation encloses them despite possible cancellation.

For the forward I step take zeta=-(m+4)h and P(u)=h H_(n-1)(a+hu). For the backward J step use the new increasing coordinate u=(b-t)/h, zeta=(4-m)h and P(u)=h H_n(b-hu). The latter sign follows by differentiating the integral definition: J'=(m-4)J-H_n, then reversing t. The n=2 backward step has zeta=0 and uses the polynomial primitive, never division by a zero interval.

Start I from its exact rational analytic anchor and propagate across all spans. Start J's constant and z coefficients separately from the exact U,V. Propagate its constant part with polynomial forcing and its z coefficient by exp(zeta). Form J=J_constant+J_z*Z only when comparing an archive target. This uses the same normalization parameter throughout the domain, and makes no independence approximation between repeated occurrences of that parameter. Every step uses outward interval arithmetic. Induction from the complete analytic anchors proves membership in the newly computed intervals on every required boundary. If every new interval is contained in its unchanged archive target, the entire original archive is validated relative only to the accepted normalization interval and exact trial definition.

## Verification and scope

The original archive used an Arb exponential-moment recurrence at384bits. The new global propagation will use mpmath.iv at200 decimal digits with the exact finite particular polynomial above. Exact rational spline coefficients, endpoint derivatives and analytic anchors are reconstructed from the source; no archive moment is used as a propagation input. The archive is read only as a target after computing the candidate. Fixed small diagnostics may measure cost and test sufficient containments, but are not a full result. Source pins, complete counts and execution chronology, an independent saved-output scan and actual Opus5.5 review with a separate later verifier disposition are required before any complete verdict.

A complete pass would validate the shared moment archive, including its analytic anchors. It would not validate every residual derivative model, a continuous inverse, distance to X3, a nonlinear closure or an IPM endpoint. No result is claimed in this preparation document.
