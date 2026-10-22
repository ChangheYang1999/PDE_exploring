# Horizontal offsets of the exact primitive

Status: complete informal argument, written before implementation. All controls passed. Written actual claude-opus-5-5 reviews186 and187 CONFIRMED formulas(1)-(10) and the full-function extension(11), respectively. The extension was written before its implementation. This is a necessary condition and a certificate for particular finite represented fields, not a nonexistence theorem for B2.

## Statement and hypotheses

Let F be smooth and odd in x and put Theta(x,y)=int_0^x F(u,y)du. Suppose, for some gamma>0,

    |Theta_y(x,y)| <= C (1+sqrt(x²+y²))^-gamma.             (1)

Every B2 profile in the class to which the already proved critical gradient estimate applies has(1), with gamma=2/beta. Here that gradient estimate is an explicit dependency, not derived from smoothness alone. There is no assumption of y reflection or a boundary at y=0.

Then for every finite y,

    H(y):=lim_(L->infinity) int_0^L [F(x,y)-F(x,0)]dx=0,  (2)
    lim_(L->infinity) int_0^L F_y(x,y)dx=0.               (3)

These limits are uniform for y in each compact interval. They need not be interpreted as separate convergent integrals of F. If also |F_y|<=C(1+r)^(-1-sigma) for sigma>0, the integral in(2) and that in(3) converge absolutely. The latter symbol condition holds for every finite primitive stream field considered below. It alone gives existence of H, not H=0.

For a finite source representation

    F(x,y)=sum_j c_j x^(2k_j+1) y^b_j (1+x²+y²)^q_j,     (4)

assume c_j,q_j are rational, k_j,b_j are nonnegative integers, and each nonzero monomial has strictly negative total asymptotic degree:

    2k_j+1+b_j+2q_j < 0.                                (5)

There is an exact finite formula for H(1). If its logarithmic coefficient vanishes, a sparse rational polynomial modulo t^d-2 decides whether H(1) is zero, where d is the least common multiple of the denominators of the finitely many exponents in that formula. A nonzero coefficient in the reduced polynomial is an exact rejection of(1), irrespective of how large d is. The certificate does not estimate the distance to a profile.

The stream source is formed using precisely the prompt convention: Omega=-DeltaPsi, V=(-Psi_y,Psi_x)-(-Psi_y(0),Psi_x(0)), W=beta X+V, and F=W.gradOmega+Omega. No inverse or drift parameter is fitted by this test. For a canonical stream in packets108/134 the source is(4), after exact rational coefficient expansion. Condition(5) is checked term by term before invoking the certificate.

## Proof of the horizontal constraints

The finite interval identities are

    int_0^L[F(x,y)-F(x,0)]dx = Theta(L,y)-Theta(L,0),
    int_0^L F_y(x,y)dx = Theta_y(L,y),

because Theta(0,y)=0 and its y derivative is0. For |y|<=M, the first right side is bounded by C M(1+L)^-gamma by integration in y, and the second by C(1+L)^-gamma. This proves(2)-(3), including compact uniformity, without interchanging an improper integral and a derivative.

If the additional bound on F_y holds, the mean-value formula gives

    |F(x,y)-F(x,0)| <= C_M (1+x)^(-1-sigma), |y|<=M.

This is integrable on x>=0. The same estimate applies directly to F_y. Thus H exists absolutely for those sources. Termwise differentiation of(4) gives this bound with sigma the minimum of the positive negatives of the degrees in(5). On bounded sets all monomials are smooth, since1+x²+y²>0. This proves all convergence assertions used below.

## Exact primitive and its finite part

For one monomial, put k=k_j, b=b_j, q=q_j and A=1+y². The substitution v=A+x² gives, for any real x,

    int_0^x u^(2k+1)(A+u²)^q du
      = (1/2) sum_(ell=0)^k binom(k,ell)(-A)^(k-ell)
          L_(q+ell+1)(A+x²,A),                          (6)

where L_p(B,A)=(B^p-A^p)/p if p!=0, and L_0(B,A)=log(B/A). The identity follows by expanding(v-A)^k dv/2, so it also holds for negative x by evenness. Multiplication by c y^b supplies the full monomial primitive. This finite expression distinguishes the exact primitive from a fixed quadrature approximation.

For the constant term as L->infinity, all p=q+ell+1 are less than1/2 by(5). A positive p therefore lies in(0,1/2); (A+L²)^p=L^(2p)+O(L^(2p-2)), with no constant term and an error tending to0. A negative p gives a term tending to0. A zero p gives2log L+o(1), with no constant term. Consequently, the finite constant for a nonresonant monomial is

    C_j(y)=a_j y^b A^e,
    e=q+k+1,
    a_j=-(c/2) sum_(ell=0)^k
                  binom(k,ell)(-1)^(k-ell)/(q+ell+1).    (7)

Here nonresonant means that none of the denominators vanishes. This is equivalently

    a_j = c (-1)^(k+1) k! /
                   [2 product_(ell=1)^(k+1)(q+ell)].    (8)

Formula(8) follows by integrating the polynomial expansion, or by partial fractions: both sides have the same simple poles and residues and decay at infinity. Formula(7) suffices for the certificate and avoids any reliance on special functions.

If a denominator vanishes, q=-ell-1. Since q+k+1=k-ell is a nonnegative integer less than(1-b)/2 by(5), necessarily ell=k and b=0. Thus q=-k-1, and the sole logarithmic term has coefficient c/2. The finite part is

    C_j(y)=D_j -(c/2) log(1+y²),                        (9)

where D_j is the rational constant from the nonresonant terms of(6). It cancels between y=1 and y=0.

For(4), expand each primitive at large L using(6). Their finite sum consists of finitely many positive powers of L, log L, a constant, and a remainder tending to0. The difference at y and0 converges by the previous section, so every positive-power and logarithmic coefficient in this difference must vanish. To see this, divide by the highest power and take the limit, successively subtract, and finally treat log L. Therefore its limit is exactly the difference of the finite constants, even if an individual integral diverges. We have proved

    H(1)=sum_(nonresonant j) a_j [2^e_j - 1_(b_j=0)]
                      - (1/2) sum_(resonant j)c_j log2. (10)

No independent renormalization convention changes H: it is the absolutely convergent difference in(2).

## An exact sparse algebraic certificate

Suppose the aggregate logarithmic coefficient in(10) is0. Let d>=1 be the least common multiple of all denominators of e_j, and t=2^(1/d)>0. For each e_j write d e_j = n_j d + r_j with integer n_j and0<=r_j<d. Then2^e_j=2^n_j t^r_j. Negative n_j still give rational factors. Thus(10) is P(t) for a rational polynomial P with degree<d, obtained by collecting finitely many powers and subtracting the rational constant terms.

The polynomial z^d-2 is irreducible over Q: Eisenstein's criterion at2 applies, since all nonleading coefficients are divisible by2 and the constant-2 is not divisible by4. Hence it is the minimal polynomial of t. A polynomial of degree<d vanishes at t only if it is the zero polynomial. Therefore H(1)=0 exactly if every collected rational coefficient vanishes. This proof also covers d=1. A large d requires no dense array and no root computation; only sparse integer residues and rational coefficients are stored.

If the logarithmic coefficient is nonzero, this algebraic certificate alone is not invoked. If P=0, log2>0 directly gives H(1)!=0. In the mixed case a separate certified inequality or further theorem would be needed. The point certificate returns OPEN for that case. The full-function certificate below decides whether H is identically0 by a different, elementary argument.

## Exact test of the entire offset function

The single value H(1) is weaker than H identically0. A stronger finite test avoids any transcendence theorem, including in the mixed logarithmic case. It also implements the natural strengthening suggested by written review186.

In addition to the terms(a,b,e) in(7), let kappa be the coefficient of log(1+y²) from(9). Define A=1+y². For b=2h use y^b=(A-1)^h; for b=2h+1 use y^b=y(A-1)^h. Expand these integer polynomials and collect equal real exponents. This gives finite sums

    H(y)=E(A)+y O(A)+kappa log A,
    E(A)=sum_gamma e_gamma A^gamma,
    O(A)=sum_gamma o_gamma A^gamma.                     (11)

The rational constants subtracted at y=0 in(10) belong to E at exponent0. All coefficients and exponents in(11) are rational for(4).

Then H(y)=0 for every real y if and only if every e_gamma, every o_gamma, and kappa vanish exactly. To prove this, replace y by-y and subtract; for y>0 this gives O(A)=0 on A>1. Put tau=log A. Distinct exponentials exp(gamma tau) are linearly independent: differentiating a finite identity through orders0,...,N-1 at a positive tau gives a Vandermonde system with nonzero determinant times nonzero exponential factors. Thus every o_gamma is0.

The even identity is sum e_gamma exp(gamma tau)+kappa tau=0. Differentiate twice. The terms with gamma=0 and the linear term disappear; exponential independence forces every coefficient with gamma!=0 to vanish. What remains is e_0+kappa tau=0, so e_0=kappa=0. The converse is direct. This proves the test. It uses an identity on an interval, not an attempted algebraic decision of a mixed value at one point.

For example, the two source monomials

    F=2x y³(1+x²+y²)^-3 -2x y(1+x²+y²)^-3

satisfy(5), and have H(y)=y(y²-1)/(2(1+y²)²). Here H(1)=0, but in(11) O(A)=(1/2)A^-1-A^-2 is nonzero. Thus the full certificate rejects a case missed by the point certificate. If all coefficients in(11) vanish, only this necessary condition is confirmed; the temperature transport equation and all other profile conditions remain unchecked.

## The condition is additional to the leading angular moments

Fix0<m<1 and write R=sqrt(1+x²+y²). Set

    Theta0=x² R^(m-2),
    Theta=Theta0+(1/2)e^(-y²)(1-e^(-x²)),
    F=Theta_x=2x R^(m-2)+(m-2)x³R^(m-4)+x e^(-x²-y²).

All fields in this example are smooth, with the target x parities and zero temperature on the axis. The leading homogeneous source is the x derivative of r^m cos²theta, so its homogeneous primitive is smooth on the circle, vanishes on the vertical axis, and has both leading primitive moments equal to0 by packet129. The rapidly decaying added source changes no leading source coefficient. It even leaves the uniform leading temperature value r^-mTheta unchanged.

For the first term, Theta0(L,y)-Theta0(L,0) tends to0, whereas the added primitive gives

    H(y)=(1/2)(e^(-y²)-1).

It is nonzero for y!=0. Thus leading angular compatibility alone does not imply the transverse-gradient condition(1). At a fixed nonzero y, the added Theta_y approaches-y e^(-y²), rather than0. This is a source/primitive counterexample, not an asserted stream solution of the vorticity equation. Its role is to distinguish the hypotheses. The certificate(10) applies directly to the actual serialized stream sources separately.

## Dependencies, scope and verification

Dependencies: the horizontal primitive reduction128; the exact canonical stream convention108/134; the already verified critical profile gradient bound when applying(1) to the full profile class; elementary integration, finite asymptotic sums and Eisenstein's criterion. The standalone statements(1)-(10) require only their explicit hypotheses.

Independent controls completed after this proof: symbolic differentiation of(6), direct physical quadrature of source differences, high-precision cancellation checks, rational sparse certificates, a resonant logarithmic example, and manufactured sources with H identically0 and with H nonzero. Fitting code and NUM code are not used in source evaluation. A numerical magnitude is distinct from the exact nonzero-polynomial verdict. No nearby-profile bound or global B2 exclusion follows.

Written UTC: 2026-10-21T06:35:46.009579+00:00

Full-function extension written UTC: 2026-10-21T06:40:24.307219+00:00
