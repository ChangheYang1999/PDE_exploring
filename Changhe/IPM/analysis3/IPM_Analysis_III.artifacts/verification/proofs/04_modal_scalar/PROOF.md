# Independent recomputation of the exactly joined modal strain

Status: CONFIRMED for the scalar quantities and exact object stated below. The method was written before computation. Own-code recomputation and output audit passed; see evidence/recomputed.json and evidence/output_audit.json.

## Exact object

The input is the copied `research_copy/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz`. All binary64 numbers are interpreted as exact dyadic rationals. The modal density is

    rho(r,theta)=r^3 cos^2(theta)sin(theta) sum_{m=0}^{259} a_m(log r)cos(2m theta).

There are degree-seven clamped splines with simple interior knots. The first and last mathematical logarithmic endpoints t_- and t_+ are taken from the knot vector, not from separately rounded `rmin` or `R0` fields. On t<=t_-, the mode factor is delta_{m0}+sum_{j=1}^7 D_mj exp(2j tau)+exp(bi tau)sum_{i=0}^6 Ei_mi tau^i, tau=t-t_-. On t>=t_+, it is sum_q A_mq exp(alpha_q tau)+exp(-bo tau)sum_{i=0}^6 Eo_mi tau^i, tau=t-t_+. The pairs (j_q,l_q) are

    (0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(0,1),(1,1),(2,1),(0,2),

and alpha_q=k-3-j_q(1-k)-2l_q. The Ei and Eo in this mathematical definition are recomputed by exact C^6 matching; their stored rounded fields are not used.

## Reduction to four modes

The sin(3theta) coefficient of cos^2(theta)sin(theta)cos(2m theta) is 1/4 for m=0, 1/8 for m=1, -1/8 for m=2 or 3, and zero otherwise. This follows by expanding (sin theta+sin 3theta)cos(2m theta)/4. Consequently, if a(t)=a_0(t)/4+a_1(t)/8-a_2(t)/8-a_3(t)/8, then

    c0=integral_{-infinity}^{infinity} exp(2t)a(t)dt.       (1)

The coefficient combination commutes with the exact matching equations because those equations are linear and use the same exponents. It is therefore sufficient to exactify the projected scalar spline rather than all 260 modes to compute (1). This scalar calculation does not by itself certify every individual mode's join.

## Exact joins and exterior normalization

Let J_n be the projected spline endpoint jet, P_n the endpoint jet of its non-correction terms, and b be bi at the inner endpoint or -bo at the outer endpoint. The unique coefficients of exp(b tau)sum E_i tau^i that match orders zero through six are

    E_i=sum_{j=0}^i (-b)^{i-j}(J_j-P_j)/((i-j)!j!).        (2)

Multiplying the Taylor jet difference by exp(-b tau) proves the formula and its uniqueness. Exact rational de Boor polynomial reconstruction supplies the J_n. A separate derivative-coefficient recurrence checks both endpoint jets exactly.

The complete inner contribution is

    exp(2t_-) [1/8 + sum_{j=1}^7 d_j/(2j+2)
               +sum_{i=0}^6 Ei_i (-1)^i i!/(bi+2)^{i+1}],

where d_j is the four-mode projection of D_mj. The base factor is 1/4, so its inner integral is 1/8. The outer contribution is

    exp(2t_+) [sum_q a_q/(-alpha_q-2)
               +sum_{i=0}^6 Eo_i i!/(bo-2)^{i+1}].       (3)

These formulas are ordinary exponential monomial integrals. The calculation checks bi+2>0, bo>2 and every alpha_q<-2 as exact rational inequalities.

Changing only the unprojected coefficient A_00 by z while recomputing its outer jet correction changes the central strain by s z, where

    s=exp(2t_+)/[4(-alpha_0-2)] ((alpha_0+bo)/(bo-2))^7.  (4)

To see this, its factor change on tau>=0 is exp(alpha_0 tau)-exp(-bo tau)sum_{i=0}^6((alpha_0+bo)tau)^i/i!, multiplied by z. Integrate it with exp(2tau)/4. Summing the finite geometric series gives (4). If alpha_0+bo>0, then s>0. The exact scalar normalization is therefore defined by

    z=(3/k-1-c0)/s.                                      (5)

It gives c=3/k-1 exactly. An interval for z encloses this exact real definition and must not be substituted as a rounded exact coefficient.

## Independent interval integration of the spline region

On every exact nonzero span [a,b], set t=a+width u, width=b-a, 0<=u<=1. Exact rational de Boor recursion constructs the unique degree-seven polynomial P(u)=sum_i p_i u^i representing the scalar spline there. Then its strain contribution is

    exp(2a)width sum_i p_i M_i(2width),
    M_i(z)=integral_0^1 u^i exp(zu)du.

For z>=0, use the first N=64 terms of

    M_i(z)=sum_{n>=0} z^n/[n!(n+i+1)].

Taylor's theorem for exp gives the rigorous remainder

    0 <= remainder <= exp(z) z^N/[N!(N+i+1)].             (6)

Indeed the pointwise omitted exponential series at zu is at most exp(z)(zu)^N/N!, and integrating u^{N+i} yields (6). No numerical quadrature tolerance or sampled derivative bound enters this proof. Arb balls enclose every dyadic conversion, exponential, moment sum, signed polynomial sum and final scalar operation. The signed p_i cause no problem because each M_i is individually enclosed.

The de Boor construction uses affine factors (a-t_i)/den+(width/den)u, with exact rational nonzero denominators, so its polynomial is exact. The derivative-coefficient check separately uses d_i=p(c_{i+1}-c_i)/(t_{i+p+1}-t_{i+1}), removes the first and last knots, and repeats. Clamping identifies endpoint values with the first and last coefficients. This checks the critical endpoint jets by a different algebraic route.

## Scope

The computation certifies the complete scalar c0 of this precisely defined exact-join modal trial, its normalization slope, and its scalar correction. It does not certify X3's strain, the modal residual, a distance to X3, source coefficients, all-mode continuity, or a linear inverse. Input hashes, precision, explicit remainder sums and outward enclosures will be recorded in evidence. Python integer/Fraction arithmetic and python-flint/Arb are trusted arithmetic dependencies.
