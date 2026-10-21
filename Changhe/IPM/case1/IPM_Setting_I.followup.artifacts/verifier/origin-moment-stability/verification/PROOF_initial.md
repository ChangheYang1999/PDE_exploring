# A quantitative origin moment and a sufficient Dini control

Date: 2026-10-20. Status: complete informal proof, written before checks; independent review pending. This concerns compatible scalar axis data only.

## Statement and conventions

Fix A>2, beta=2/A in (0,1), and L>0. Let the smooth pair (w_0,g_0) on [0,L] satisfy

    w_0(0)=w_0(L)=0, w_0'(0)=-A, w_0'(L)=A,
    w_0<0 on (0,L), g_0>0 on (0,L],
    w_0 g_0'=(w_0'-A)g_0, g_0(x)/x^2 ->1 at zero.

Assume w_0 is odd analytic near zero. Fix r_0>0 smaller than min(1,L)/4 and small enough that this analytic description holds on [0,r_0]. For a trace w sufficiently close in the sense below, rebuild its normalized g_w by the same first equation. Define

    Q_w=(g_w'-w'')/(2g_w^3), m_w=-w/g_w,
    W_w=m_w^(beta-2)/g_w,
    B[w]=(beta-1)A^(1-beta)/3
           * FP integral_0^L (Q_w-Q_w(L)) W_w dx.             (1)

The finite part is in the physical coordinate x, removing divergent powers at zero with no added constant. Every perturbation used below vanishes on some neighborhood of zero. Consequently the singular powers there are the same as those of the base. The subtraction at L makes the integral ordinary and convergent at that endpoint.

For v in C_c^infinity((0,r_0)), extended by zero to [0,L], put

    e(v)=max_(0<=i<=2) sup_(0<x<=r_0)
                              x^(i-7-beta)|v^(i)(x)|,
    M(v)=integral_0^r_0 v(x)x^(-8-beta) dx,
    kappa_A=(1-beta)(6+beta)(7+beta)/(6A)>0.

There are e_*>0 and C<infinity, depending only on the fixed base, A and r_0, such that whenever e(v)<=e_*, w_0+v is negative in (0,L), its rebuilt density is smooth and compatible, and

    |B[w_0+v]-B[w_0]-kappa_A M(v)| <= C e(v).                (2)

In particular the constants do not depend on the smallest positive point of the support of v or on its length in log x.

The estimate also holds while fixing the entire source germ. Fix one smooth nonnegative nonzero f with compact support in an interval (b,c), where r_0<b<c<L. Then, after decreasing e_* if necessary, there is a unique small t=t(v) such that the pair corresponding to

    w=w_0+v+t(v)f

agrees with (w_0,g_0) on [c,L]. One has |t(v)|<=C e(v), and

    |B[w]-B[w_0]-kappa_A M(v)| <= C e(v).                    (3)

Both pairs agree with the base near zero as well.

Here is a sufficient borderline continuity criterion. Define the nondecreasing modulus and its Dini quantity by

    omega_v(x)=sup_(0<s<=x) |v^(7)(s)|/s^beta,
    D_beta(v)=omega_v(r_0)+integral_0^r_0 omega_v(x) dx/x.     (4)

For these compactly supported smooth v, D_beta(v) is finite. When e(v)<=e_*, both the uncorrected trace and the source-corrected trace obey

    |B[w]-B[w_0]| <= C D_beta(v).                            (5)

Thus D_beta(v_n)->0 suffices for convergence of B in either construction. More explicitly, for any beta<gamma<1, the ordinary C^(7,gamma) seminorm gives

    D_beta(v) <= [v^(7)]_(C^gamma) r_0^(gamma-beta)
                                         (1+1/(gamma-beta)), (6)

so small C^(7,gamma) perturbations supported in (0,r_0) make B small. The theorem is a local sufficient estimate for this specified perturbation class. It makes no claim that (4) is necessary, nor any claim about a general nonlinear neighborhood of coupled IPM solutions.

## Normalized density and endpoint bounds

The normalized equation integrates to

    eta(x):=log(g_(w_0+v)(x)/g_0(x))
       =log(1+v(x)/w_0(x))
          -A integral_0^x [1/(w_0+v)-1/w_0] ds.             (7)

Odd analyticity and the normalization give g_0=x^2(1+O(x^2)) and w_0=-Ax(1+O(x^2)). To verify the density assertion, subtract 2/x from (w_0'-A)/w_0. The result is an odd analytic function O(x), so its integral is an even analytic function vanishing at zero. Exponentiation proves the stated g_0 form. It follows that

    m_0=(A/x)(1+O(x^2)), W_0=A^(beta-2)x^(-beta)(1+O(x^2)),
    Q_0=O(x^(-5)).                                         (8)

All O constants below depend on the fixed base and r_0, never on the inner support radius of v. For e=e(v) sufficiently small, |v/w_0|<=C e x^(6+beta)<=1/2. Thus negativity holds. Derivatives of the first term in (7) up to order two are bounded by C e x^(6+beta-i). The reciprocal difference in (7) is O(e x^(5+beta)); its first derivative is O(e x^(4+beta)). Integrating, or differentiating the integral at most twice, proves

    |eta^(i)(x)|<=C e x^(6+beta-i),  i=0,1,2,
    |g_(w_0+v)-g_0|<=C e x^(8+beta),
    |g_(w_0+v)'-g_0'|<=C e x^(7+beta)                      (9)

on (0,r_0]. These estimates require only the three quantities defining e(v).

On [r_0,L], the perturbed trace equals w_0 and its density equals lambda g_0, with lambda=exp(-A I) and

    I=integral_0^r_0 [1/(w_0+v)-1/w_0] dx, |I|<=C e,
    |lambda-1|<=C e.                                       (10)

Consequently the rebuilt pair is smooth and positive up to L. Near zero it agrees exactly with the base. All endpoint compatibility conditions persist, even though the uncorrected density at L can change.

At L, write s=L-x. Smoothness and w_0'(L)=A give -w_0=A s+O(s^2), with g_0(L)>0. Therefore W_0=O(s^(beta-2)), and Q_0-Q_0(L)=O(s). The product in (1) is O(s^(beta-1)), which is integrable because beta>0.

## A remainder uniform in the logarithmic support length

Use a hat for the pair associated with w_0+v. Equations (8)-(9) and the definitions give, on (0,r_0],

    W_hat-W_0=O(e x^6),
    Q_hat-Q_0=-v''/(2g_0^3)+O(e x^(1+beta)),
    Q_hat(L)-Q_0(L)=O(e).                                  (11)

For the second line, the changes in g' and in the denominator of Q multiply quantities of sizes x^(7+beta) and x^(-5), respectively, giving O(e x^(1+beta)). Replacing the denominator of the v'' term by g_0^3 costs at most C e^2 x^(5+2beta). Since e is bounded and r_0<1, that is covered by the displayed remainder. The first line follows by differentiating the smooth scalar powers of the relative changes v/w_0 and (g_hat-g_0)/g_0, both O(e x^(6+beta)).

Subtract the two integrands, with the endpoint constants included. The leading contribution is -v'' g_0^(-3) W_0/2. By (8),

    g_0^(-3) W_0=A^(beta-2)x^(-6-beta)(1+O(x^2)).

Its O(x^2) correction is O(e x). The remaining products in (11) are bounded as follows: the Q remainder times W_0 is O(e x); the base Q times the W change is O(e x); the endpoint constant change times W_0 is O(e x^(-beta)); and the product of perturbations is O(e^2 x^(5+beta)), covered by O(e x). Thus

    (Q_hat-Q_hat(L))W_hat-(Q_0-Q_0(L))W_0
        =-A^(beta-2)v'' x^(-6-beta)/2 + E(x),
    |E(x)|<=C e (x+x^(-beta)).                              (12)

This is integrable uniformly at zero. Below the support of v only the endpoint constant subtraction differs, also covered by (12).

For x>=r_0 write

    G=g_0'/(2g_0^3), V=-w_0''/(2g_0^3).

There the exact formulas are

    Q_hat=lambda^(-2)G+lambda^(-3)V,
    W_hat=lambda^(1-beta)W_0.                              (13)

Subtract endpoint values of G and V before estimating. They vanish to first order at L, so (10) and (13) bound the integrand difference by C e (L-x)^(beta-1) near L and by C e on the rest of [r_0,L]. The resulting integral is bounded by C e independently of the origin support radius. Since the singular finite-part terms agree at zero, the difference of finite parts equals the ordinary integral of their integrand difference.

Multiplying (12) by the prefactor in (1), and including this tail, gives

    B[w_0+v]-B[w_0]
        =(1-beta)/(6A) integral_0^r_0 v'' x^(-6-beta) dx
                                                        +O(e).

The two integrations by parts have zero boundary terms, since v is compactly supported in (0,r_0). They give

    integral v'' x^(-6-beta) dx
       =(6+beta)(7+beta) integral v x^(-8-beta) dx.

This proves (2). In particular no estimate has replaced M(v) by e times a constant depending on the logarithmic support length.

## Fixing the source germ

Define the scalar function

    J(t)=integral_0^L [1/(w_0+t f)-1/w_0] dx.

On the fixed support of f the denominators are bounded away from zero. Hence J is smooth near zero, J(0)=0, and

    J'(0)=-integral_0^L f/w_0^2 dx<0.

By the inverse function theorem and (10), t(v)=J^(-1)(-I) exists for small e, with |t(v)|<=C e. The two perturbation supports are disjoint. Their reciprocal differences therefore add exactly, and their total integral is zero. Equation (7), with v+t f substituted, then gives equality with the base on [c,L]. Both perturbations vanish near zero and the same equation gives equality there. Negativity follows from the small size of t on its fixed support and from the previous origin estimate.

For completeness, the correction changes B by at most C e without assuming any unproved critical-norm continuity. Before b, the corrected and uncorrected pairs coincide; only their subtracted Q(L) constants differ, by O(e). The common W is uniformly integrable at zero by (9), so this contributes O(e). On [b,c], the uncorrected pair is (w_0,lambda g_0). Ordinary differentiation of (7) on this fixed interval bounds changes of g,g',Q and W by C e, giving O(e) contribution. After c, the corrected pair is the base pair and the uncorrected pair is (w_0,lambda g_0). The exact formula (13), after subtraction at L, again gives the integrable bound C e (L-x)^(beta-1). The pairs agree near zero, so this ordinary integral equals their finite-part difference. Combining with (2) proves (3).

## The Dini bound and stronger Holder exponents

All derivatives of v vanish near zero. Taylor's integral formula, applied to v^(i) for i=0,1,2, is therefore

    v^(i)(x)=1/(6-i)! integral_0^x (x-s)^(6-i) v^(7)(s) ds.

By definition |v^(7)(s)|<=omega_v(x)s^beta for s<=x. Thus

    |v^(i)(x)|<=c_(i,beta) omega_v(x)x^(7+beta-i),
    c_(i,beta)=1/(6-i)! integral_0^1 (1-s)^(6-i)s^beta ds.

The constants are finite and positive. It follows that

    e(v)<=max_i c_(i,beta) omega_v(r_0),
    |M(v)|<=c_(0,beta) integral_0^r_0 omega_v(x) dx/x.

Equations (2)-(3) prove (5). Finiteness of (4) holds for each v because omega_v vanishes below a positive support radius and is bounded on the remaining interval.

Finally v^(7)(0)=0. The C^gamma seminorm therefore gives |v^(7)(s)|<=[v^(7)]_(C^gamma)s^gamma, so omega_v(x)<=[v^(7)]_(C^gamma)x^(gamma-beta). Integrating this bound gives (6). In particular if that seminorm tends to zero, the smallness hypothesis e(v)<=e_* eventually holds and the corresponding B values converge to B[w_0].

## Dependencies, interpretation and limits

This argument uses the normalized scalar axis ODE, the explicit finite part (1), ordinary differentiation, two compact-support integrations by parts, Taylor's integral formula and a scalar inverse function theorem. Its origin and source-correction ledger generalizes ../origin-fixed-source/PROOF.md, but all bounds needed here were derived above. The estimate distinguishes the signed moment M, which can have cancellations, from the sufficient absolute Dini control D_beta. It neither asserts a Dini necessity theorem nor controls perturbations placed near the source endpoint.

The logarithmic cutoff sequence in ../critical-holder-origin/PROOF.md can have a nonzero limiting M while its critical Holder norm tends to zero. This is compatible with (5): critical Holder control bounds omega_v, but alone does not make its logarithmic integral small. Conversely, an exponent gamma>beta supplies that integrability through x^(gamma-beta).

No coupled profile is constructed or excluded. These scalar trace estimates do not settle the candidate's continuum kernel, the existence of a profile family, B_5 or B_7, or either strong-setting endpoint. The separate team's source-endpoint regularity and a posteriori estimates are outside the statement proved here.
