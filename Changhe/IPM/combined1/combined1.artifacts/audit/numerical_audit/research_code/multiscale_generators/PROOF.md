# Exact audit of scaled radial generators

## Statement, hypotheses and notation

Let m,w,n,Q be nonnegative integers, R>0 and p rational. Let H_m(x,y)=Re(x+iy)^(2m), s=x²+y² and P_n be the ordinary Legendre polynomial normalized by P_n(1)=1. Define

    T_R=s/(R²+s), U_R=R²/(R²+s),
    chi=H_m (1+s)^(p-m) T_R^w U_R^Q P_n(2T_R-1).        (1)

Finite real rational linear combinations of (1) are permitted. In the campaign p=p_j=(3+gamma-j delta)/2, gamma=1/c and delta=1-gamma, with the exact fixed c supplied by the candidate. R and all coefficients are rational. The older mono, leg and legq generators are the special cases R=1, with respectively (n,Q)=(0,0), Q=0, or unrestricted Q.

The following are exact statements about a single generator and extend by finite linearity.

1. chi is smooth on the real plane. Its first nonzero homogeneous Taylor term at the origin is

       (-1)^n R^(-2w) H_m s^w,

   of degree2(m+w). Thus if m+w>=5, every derivative of chi of order at most9 vanishes at the origin. In particular its contributions to the density slope and strain are zero.
2. Writing the radial factor as G(r), so chi=G(r)cos(2m theta), it has a convergent far-field expansion G(r)=r^(2p) sum_(q>=0) M_q r^(-2q) for r>max(1,R). The coefficients through any finite order are exactly computable rational numbers. They satisfy

       M_q=0 for q<Q,
       M_Q=R^(2Q),
       M_(Q+1)=R^(2Q)[p-m-R²(w+Q+n(n+1))].              (2)

3. A finite Taylor calculation in the scalar variable s, followed by exact composition with s=(x+h)²+(y+k)², gives every Cartesian derivative through any prescribed finite order. Outward interval evaluation at a rational point certifies those derivatives without numerical differentiation or radial quadrature.

These claims do not assert that a complete candidate satisfies all residual-sector cancellations, any norm threshold, or any background matrix inequality.

## Origin regularity and normalization

Both denominators in (1) are strictly positive for real s>=0. The real power of1+s is therefore smooth. Near zero,

    T_R=s/R²+O(s²), U_R=1+O(s), P_n(2T_R-1)=(-1)^n+O(s).

Multiplying gives the displayed leading homogeneous term. H_m s^w is a nonzero homogeneous polynomial, so its degree is exactly2(m+w). This proves statement1, including the vanishing of all lower derivatives. The campaign fields are

    rho=-chi_xxy-chi_yyy,
    U1=-chi_xyy, U2=chi_xxy,
    rho_y(0)=-chi_xxyy(0)-chi_yyyy(0),
    strain=partial_y U2(0)=chi_xxyy(0).

Both normalization quantities involve only fourth derivatives. The stronger implementation restriction m+w>=5 also preserves Taylor information through degree8. This is a property of these extra generators, not a proof that the unchanged coefficients already satisfy normalization.

## Independent far-field formula

Put z=r^-2. Write P_n(v)=sum_(k=0)^n c_k v^k, and define the polynomial

    A_n(v)=sum_(k=0)^n c_k (1-v)^k (1+v)^(n-k).

A direct substitution into (1) gives the identity

    r^(-2p)G(r)=R^(2Q) z^Q (1+z)^(p-m)
                A_n(R²z)(1+R²z)^(-w-Q-n).               (3)

All factors are analytic for |z|<min(1,R^-2). Multiplying the exact generalized binomial series with the finite polynomial A_n proves existence, convergence and the rational coefficient algorithm. Terms below Q vanish. The value A_n(0)=P_n(1)=1 gives M_Q. Also

    A_n'(0)=n-2P_n'(1)=n-n(n+1)=-n².

The Legendre differential equation at1 gives P_n'(1)=n(n+1)/2, or this identity follows directly from the finite polynomial recurrence. Differentiating (3) at zero after removing z^Q gives formula(2).

For R>1 and w+Q+n>0, the point z=-R^-2 is a pole: A_n(-1)=2^n c_n is nonzero, and (1+z)^(p-m) is analytic and nonzero there. Thus the radius of convergence is exactly R^-2. A larger radial scale moves the guaranteed convergence region outward. It does not establish an approximation error from a finite prefix at r comparable to R.

## Explicit finite-prefix remainder bound

For 0<=z<eta<min(1,R^-2), define a=p-m, B=w+Q+n and

    C_eta=R^(2Q) eta^Q (1-eta)^(-|a|)
           [sum_k |[v^k]A_n| (R²eta)^k] (1-R²eta)^(-B).

The generalized binomial estimate |binom(a,k)|<=(|a|)_k/k! implies |(1+zeta)^a|<=(1-eta)^(-|a|) on |zeta|=eta; the other factors of(3) obey the remaining terms of C_eta. Cauchy's coefficient bound therefore gives |M_q|<=C_eta eta^-q. Summing the geometric tail proves

    |r^(-2p)G(r)-sum_(q=0)^K M_q z^q|
       <= C_eta (z/eta)^(K+1)/(1-z/eta).                 (4)

This explicit bound may be conservative, but it states the condition needed to turn a finite series into a certified tail approximation. It is not automatically small for the scales used by an optimizer. Differentiated residual tails need corresponding derivative bounds, not merely(4) for the potential.

## Cartesian Taylor evaluation

At a rational point(x0,y0), write s0=x0²+y0² and

    D=2x0 h+2y0 k+h²+k².

To compute derivatives through total order d, it suffices to compute the radial scalar series in a variable z through z^d, substitute z=D, multiply by the exact polynomial expansion of H_m(x0+h,y0+k), and discard monomials of total degree>d. Terms omitted before composition have degree at least d+1 afterward because D has no constant term. For positive A, the Taylor coefficients of(A+z)^a are binom(a,l)A^(a-l); integer powers at A=0 are evaluated as polynomials. Scalar products and the Legendre recurrence are truncated only after the required degree. Multiplying the coefficient of h^i k^j by i!j! gives the derivative.

Every scalar operation is exact rational until positive real powers are evaluated with outward Arb arithmetic. The resulting intervals enclose the exact derivatives. Products of field intervals then enclose

    F=(c x+U1)rho_x+(c y+U2)rho_y-rho.

No finite-difference step or floating threshold is used to enforce a zero. At the origin, the degree argument in statement1 supplies exact vanishing checks.

## Dependencies, verification plan and scope

The finite Legendre recurrence and binomial theorem supply the algebra. The field convention and exact c are those separately checked in the baseline and candidate audits. The verification program compares formula(3) against the copied N1 exact-moment implementation on a finite parameter grid, checks(2), and compares Cartesian jets with the older canonical evaluator when R=1. These are checks of the formula and implementation, not a claim about all future candidate coefficients.

The extra denominator R²+s is not part of the current single-scale polynomial residual algebra. A candidate with R!=1 must use a new integration proof or an explicit error-controlled approximation before inheriting any whole-plane norm certificate. The present result supplies exact point and asymptotic checks only.
