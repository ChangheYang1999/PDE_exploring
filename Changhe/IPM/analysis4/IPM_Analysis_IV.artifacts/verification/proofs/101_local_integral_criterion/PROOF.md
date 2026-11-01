# Local integral norms detect geometric coefficient growth

Status: PROVED for every positive Lp exponent, including infinity, with the explicit limsup interpretation below. Independent review is recorded in V312.

## Statement

Use the rational canonical setting of topic94: delta=a/b in(0,1), q_0=2b/gcd(a,2), nonzero finite real S1 leading profile with largest frequency L, and stream term

    T_n(t,theta)=exp((2-n delta)t)G_n(t,theta).

The log degree of G_n is at most n/q_0, its angular frequency is at most Dn with D=L+1, and its plain coefficient norm is N_n. Fix Q=[T_0,T_1] times a full angular period, h=T_1-T_0>0 and B=max(|T_0|,|T_1|). Define

    A_Q=exp(delta T_1)(32e)^(2D)
                           [32e(1+B)/h]^(1/q_0),
    C_Q=exp(-delta min(T_0,0))max(1,B)^(1/q_0).

Then for every n>=1,

    N_n <= D exp(2B)/(pi h) n A_Q^n ||T_n||_L1(Q),       (1)
    ||T_n||_L1(Q) <= 2pi h exp(2B) C_Q^n N_n.           (2)

Consequently N_n has a geometric bound if and only if the L1 norms on one such rectangle have a geometric bound, and then those norms have a geometric bound on every such rectangle. In the divergent alternative of topic94 the precise conclusion is

    limsup_(n to infinity) ||T_n||_L1(Q)^(1/n)=infinity   (3)

for every Q. This is not an assertion that the full sequence of nth roots tends to infinity.

## The bounded set may vary with the order

Suppose for one fixed n that |T_n|<=V_n on a measurable set E_n in Q of area at least pi h. Let ell(t) be its angular slice measure. Set eta=pi/2 and S={t:ell(t)>=eta}. The complement contributes at most eta h=pi h/2 to the area, so S contributes at least pi h/2. Since ell(t)<=2pi, S has measure at least h/4.

For t in S, on its angular slice,

    |G_n(t,theta)|<=exp(2B) exp(n delta T_1)V_n.

The angular interpolation estimate of topic94 supplies the factor

    (16pi e/eta)^(2Dn)=(32e)^(2Dn).

Its polynomial interpolation estimate, on a t set of measure at least h/4, supplies the factor

    [8e(1+B)/(h/4)]^(n/q_0)=[32e(1+B)/h]^(n/q_0).

Summing over at most Dn sine amplitudes proves

    N_n<=D exp(2B)n A_Q^n V_n.                    (4)

Both interpolation factors exceed one, so the noninteger degree upper bounds are legitimate. This proof concerns only the current n and therefore does not require a common set E_n for different orders.

## L1 control and the converse

Chebyshev's inequality gives a set of area at least half of Q on which

    |T_n|<=2||T_n||_L1(Q)/|Q|=||T_n||_L1(Q)/(pi h).

Substitute this value of V_n into(4), obtaining(1). If the integral is zero, continuity forces T_n to vanish everywhere on Q, and the polynomial identity then gives N_n=0; the same conclusion follows directly.

Conversely, at every point of Q,

    |G_n(t,theta)|<=max(1,B)^(n/q_0) N_n,
    exp((2-n delta)t)<=exp(2B)exp(-n delta min(T_0,0)).

Integration proves(2). Equations(1)-(2), with the factor n absorbed into any slightly larger base, give the geometric equivalence. A sequence of finite nonnegative numbers has a geometric upper bound precisely when its nth-root limsup is finite, after covering finitely many initial indices with a constant. This proves(3) when no geometric bound exists.

## Why the limsup qualifier matters

The two estimates alone do not imply eventual growth faster than every exponential. For example take G_n=exp(n^2)sin(2theta) for even n and G_n=0 for odd n. These polynomial coefficients meet the linear degree and frequency bounds. Their coefficient and local L1 nth-root limsups are infinite, but their nth-root liminfs are zero. This example is not a generated stationary sequence; it identifies the quantifier which the norm-equivalence argument proves. An eventual lower bound for the actual generated sequence would require another argument.

## Extension to every positive Lp exponent

For any fixed 0<p<infinity, define ||u||_Lp=(integral_Q |u|^p)^(1/p), allowing the usual quasi-norm when p<1. Chebyshev supplies a half-area set with

    |T_n|<=(2/|Q|)^(1/p)||T_n||_Lp.

Thus(4) gives

    N_n<=D exp(2B)(1/(pi h))^(1/p)
                           n A_Q^n ||T_n||_Lp.    (5)

The pointwise upper bound used in(2) gives

    ||T_n||_Lp<=(2pi h)^(1/p)exp(2B)C_Q^n N_n.     (6)

For p=infinity use the essential supremum directly in(4) and omit both area factors. The same geometric equivalence and infinite-limsup alternative therefore hold for every fixed p in(0,infinity]. No triangle inequality for p<1 is needed.

The proof extends to an angular interval of any fixed length ell in(0,2pi] by replacing eta by ell/4, keeping the t measure h/4, and replacing (32e)^(2D) in A_Q by (64pi e/ell)^(2D). The area factors become (2/(h ell))^(1/p) and(h ell)^(1/p). Hence geometric local Lp norms on any nonempty open rectangle suffice. The density has the same conclusion with radial exponent1 and its coefficient norm M_n. Potential and radial-velocity terms are treated with the degree bounds and derivative comparisons of topics94 and99. These statements do not choose between the alternatives for the computed rational sequence.

## Dependencies and audit evidence

Topic94 proves the two measurable-set interpolation estimates in full. The present argument derives every new constant and uses only Chebyshev and Fubini, plus the already established degree bounds. The theory part's source statement is retained in sources/lead_remark4.md. No numerical integration or finite fitting is used.
