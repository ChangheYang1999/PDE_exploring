# Exact canonical center jets in the Cartesian-smooth basis

Date: 2026-10-20. This is an exact reconstruction theorem for a finite family of smooth density formulas. It provides necessary center tests for candidate profiles. It does not prove that any candidate solves transport or that a sequence converges smoothly.

## Formula, hypotheses and intended output

Let L>0 and 0<alpha<1/2. Let P_0,...,P_(M-1) be real polynomials and put P_k=0 for k>=M. Set

    r^2=x^2+y^2, w=(1+r^2/L^2)^(-alpha),
    sigma=r^2/(L^2+r^2), t=1-2w,
    rho=y*w*sum_(k=0)^(M-1) sigma^k P_k(t) cos(2k theta).       (1)

At the origin define (1) by its Cartesian expression below. Its exponent at infinity is p=1-2alpha in(0,1). Thus rho is smooth everywhere, even in x, odd in y, and obeys the sublinear density and gradient bound with exponent p. Its canonical velocity U=(-psi_y,psi_x) is the unique velocity with these parities, curl U=-rho_x, divergence zero and U=o(r). Set a=rho_y(0)=P_0(-1), which need not be normalized. Fix any ell>1 and form the true unforced residual

    R=(ell X+U).grad rho-rho.                                  (2)

The procedure below determines exactly the Taylor coefficients of rho and R through any requested odd degree 2J+1, and of psi through degree 2J+2. When the inputs L, alpha, ell and the polynomial coefficients are rational, every output is rational. Binary floating inputs are interpreted as the exact rationals actually stored, including the separately computed floating alpha. This is not a claim of exactness for rounded decimal parameters or for an ideal optimizer output.

The only analytic dependency is the canonical angular Green inverse proved in ../inverse/PROOF.md. The derivation below supplies the endpoint estimates and all higher harmonic coefficients needed here. Numerical comparisons use independent quadrature as tests, not as definitions of the exact coefficients.

## Cartesian density expansion

Write

    P_k(1-2w)=sum_l C_(k,l) w^l.

If P_k is provided in Chebyshev coefficients, obtain these C by the exact recurrence T_0=1, T_1=1-2w and T_(n+1)=2(1-2w)T_n-T_(n-1). The identity

    r^(2k) cos(2k theta)=Re(x+i y)^(2k)

rewrites (1) as the finite sum

    rho=sum_(k,l) C_(k,l)*y*Re(x+i y)^(2k)*L^(-2k)
                        *(1+r^2/L^2)^(-alpha(l+1)-k).          (3)

This proves the asserted local smoothness, including both axes. Expand the last factor using its ordinary convergent binomial series near zero. To obtain degree 2J+1, retain only k<=J and powers (r^2)^h with h<=J-k. The coefficient at h is

    (-1)^h * [b(b+1)...(b+h-1)]/h! * L^(-2h),
    b=alpha(l+1)+k.                                           (4)

Because the sum in k,l is finite, the resulting polynomial is the Taylor polynomial of the actual density. There is no differentiability inference from a polar fit.

## Canonical harmonic coefficients from global moments

Expand rho=sum_(m odd>=1) f_m(r) sin(m theta). The angular product identities give

    f_1/r=w[P_0(t)-sigma P_1(t)/2],
    f_(2j+1)/r=(w sigma^j/2)[P_j(t)-sigma P_(j+1)(t)], j>=1.   (5)

For each even n>=2, the sin(n theta) coefficient s_n of rho_x is

    s_n=1/2*[f'_(n-1)-(n-1)f_(n-1)/r
                     +f'_(n+1)+(n+1)f_(n+1)/r].              (6)

Smoothness implies s_n=O(r^n) at zero. At infinity it is O(r^(p-1)). The canonical solution of -Delta psi=rho_x has coefficient

    phi_n(r)=1/(2n)*[r^(-n) int_0^r s^(n+1) s_n(s) ds
                         +r^n int_r^infty s^(1-n) s_n(s) ds]. (7)

Both integrals have the required endpoints; in particular the second integrand is O(s) at zero and O(s^(p-n)) at infinity, and p-n<-1. The first term of (7) is O(r^(n+2)). Therefore the coefficient h_n of r^n sin(n theta) is

    h_n=1/(2n) int_0^infty s^(1-n) s_n(s) ds
       =-d_(n-1)/(4n) + (1/2) int_0^infty f_(n+1)(s)s^(-n) ds, (8)

where d_(n-1)=lim_(r->0) f_(n-1)(r)/r^(n-1). To prove the second equality, integrate the first bracket in (6) as the derivative of r^(1-n)f_(n-1). Its boundary values are d_(n-1) and zero. The other bracket has zero boundary values at both ends and leaves 2n times the displayed integral. These integrations are convergent. No unrenormalized two-dimensional center density kernel is used.

For n=2j the boundary coefficients are

    d_1=a,
    d_(2j-1)=P_(j-1)(-1)/(2L^(2j-2)), j>=2.                   (9)

Let I_j denote the integral on the right of (8). The substitution w=(1+r^2/L^2)^(-alpha) gives

    I_j=L^(2-2j)/(4alpha) * int_0^1 w^((j-1)/alpha)
                   [P_j(1-2w)-(1-w^(1/alpha))P_(j+1)(1-2w)] dw.

Consequently

    I_j=L^(2-2j)/(4alpha) * sum_l
          [(C_(j,l)-C_(j+1,l))/(l+1+(j-1)/alpha)
                        +C_(j+1,l)/(l+1+j/alpha)],            (10)
    h_(2j)=-d_(2j-1)/(8j)+I_j/2.                             (11)

All denominators in (10) are positive. This is an exact evaluation of the full-plane moments. In particular c=psi_xy(0)=2h_2=-a/4+I_1. One must retain the independently calculated defect ell+c-1 rather than force it to zero in this evaluator. Modes j greater than those visible in the requested local density degree can still affect h_(2j), and (10) includes them.

## Poisson recursion with the correct harmonic term

Write the homogeneous stream term of degree 2m as

    psi_(2m)=sum_(j=0)^(m-1) q_j x^(2j+1) y^(2m-2j-1).

The Taylor polynomial of rho_x at degree 2m-2 is known from (3)-(4). For j=0,...,m-2, equating the coefficient of x^(2j+1)y^(2m-2j-3) in -Delta psi=rho_x gives

    (2j+3)(2j+2)q_(j+1)
      +(2m-2j-1)(2m-2j-2)q_j=-(rho_x)_(2j+1,2m-2j-3).        (12)

There are m unknowns and m-1 equations. The missing homogeneous harmonic coefficient is fixed by (11). Indeed, the sin(2m theta) coefficient of the monomial x^(2j+1)y^(2m-2j-1) restricted to the unit circle is

    (-1)^(m-j+1)/2^(2m-1).

This follows by expanding cos(theta) and sin(theta) as complex exponentials. Hence impose

    sum_j (-1)^(m-j+1) q_j / 2^(2m-1)=h_(2m).                (13)

Equations (12)-(13) have exactly one solution: the kernel of (12) is the one-dimensional odd-odd harmonic space spanned by Im(x+i y)^(2m), whose coefficient in (13) is one. Thus this recursion gives the actual canonical Taylor term. It does not add a fitted polynomial strain. At m=1 it simply gives q_0=2h_2=c.

Repeat for m=1,...,J+1. Differentiate the resulting stream polynomial to obtain U through degree 2J+1. Multiply polynomial Taylor series in (2) and truncate to that degree. Every omitted term has higher degree and cannot alter an output coefficient. This proves the claimed reconstruction algorithm. An independent exact check of -Delta psi-rho_x through degree 2J is a required algebraic invariant of the implementation.

## Interpretation, scaling and verification limits

A nonzero R coefficient refutes exact transport for that stored finite formula. A small coefficient does not imply a nearby solution. For a sequence, convergence of any finite set of jets is necessary for smooth convergence in a fixed gauge but does not suffice; divergence of finitely many observed values at finitely many resolutions is not a proof of divergence of the sequence. The independently calculated a and c must be reported with these coefficients.

Under rho_lambda(X)=lambda rho(X/lambda), rho_d scales by lambda^(1-d) and psi_d by lambda^(2-d); a,c,ell remain invariant. Under the primary positive-axis asymptotic hypothesis K/a>0, the canonical reporting length is (K/a)^(1/(1-p)). Existing smooth controls use K=a and therefore this length is one, up to their actual stored constraint defects. This gauge applies to that subclass, not to every arbitrary formula in (1).

The tests include exact constant-mode radial densities, higher angular modes, exact Poisson and harmonic invariants, and an independent high-precision quadrature of (6)-(8). Candidate inputs are extracted into exact JSON with source hashes, and the checker reads these JSON inputs. The exact rational outputs are stored beside the verification data. The computation is an algebraic audit, not a formal Lean proof or an interval existence certificate.
