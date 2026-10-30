# Independent continuous lower bound for the dyadic norm

## Exact statement and hypotheses

Let c=4076476460239181/2251799813685248 and A=1+1/c.
Let F be the full-plane stationary residual of the exact d2 reference
identified in verification/d2.json. Let 0<a<A, 0<s<1 and q=2+s.
Use the dyadic space Y of T4-058 with its specified cutoff functions
and shell normalization. In particular its core cutoff is one on
r<2, and its jth rescaled shell cutoff is one on
2^j<r<2^(j+1), for every integer j>=1.

Define

    J(a)=||(1+r²)^((2-a)/2) Delta F||_2,
    C(a)=sqrt(8 pi) (1+c-ca)²/(1+a).

The independently checked plateau estimate implies

    Y(F) >= 5^((a-2)/2) J(a).

The computation checks, on each cell with endpoints in
{0,1/4,1/2,3/4,1,5/4,3/2,A}, the strict inequality

    5^((l-2)/2) J(h) > C(l).

If every check passes, it follows that Y(F)>C(a) for all 0<a<A.
This is a numerical lower-bound certificate, not an existence theorem.

## Proof of the lower bound

On each plateau the cutoff derivatives vanish. Plancherel's identity
gives ||g||_(H^q)>=||Delta g||_2, since q>=2. Under X=2^j Z,
the Laplacian acquires a factor 2^(2j) and the two-dimensional L²
norm a factor 2^(-j). Combining this with the shell prefactor
2^((1-a)j) yields

    Y(F)² >= ||Delta F||²_(r<2)
      + sum_(j>=1) 2^(2(2-a)j)
          ||Delta F||²_(2^j<r<2^(j+1)).

The core and these annuli partition the plane up to circles of measure
zero. On the core, 1+r²<=5. On shell j, 1+r²<=5*2^(2j).
Because a<2, each coefficient above is at least
5^(a-2)(1+r²)^(2-a). Integrating proves the bound.

J(a) is nonincreasing in a by pointwise monotonicity of its nonnegative
squared integrand. The factor 5^((a-2)/2) is increasing. C(a) is
strictly decreasing on [0,A), since 1+c-ca is positive there
and decreases while 1+a increases. Thus for l<=a<=h,

    5^((a-2)/2)J(a) >= 5^((l-2)/2)J(h),
    C(a) <= C(l).

The finite cell inequalities establish the asserted uniform result.
The endpoints 0 and A are used for bounds by continuity; the
stationary inverse framework itself is invoked only on the open range.

## Exact finite integral and independent computation

Put t=r²/(1+r²), v=1-t and delta=1-1/c. The independently assembled
Cartesian residual is

    F=r sum_(ell,n) v^(ell delta/2) P_(ell,n)(t) sin(n theta).

Differentiate twice in Cartesian coordinates, including every
linear and nonlinear term, and add F_xx+F_yy. In the normalization
of the derivative engine this trace is

    Delta F=r sum_(ell,n) v^(1+ell delta/2)
                 L_(ell,n)(t) sin(n theta).

As an exact algebraic cross-check, for
T_d P=(1-2dt)P+2t(1-t)P', test

    t L_(ell,n) = T_d(T_d(P_(ell,n)))-n² P_(ell,n),
    d=ell delta/2.

Fourier orthogonality, r dr=dt/(2v²) and r²=t/v give

    J(a)²=(pi/2) sum_n sum_(ell,k)
      integral_0^1 v^(a+(ell+k)delta/2-3)(1-v)
                    L_(ell,n)(1-v)L_(k,n)(1-v) dv.

All diagonal terms are tested for integrability using their exact
vanishing order at v=0. Every polynomial product is formed exactly
and every off-diagonal term has multiplicity two. Each remaining
monomial v^b has integral 1/(b+1), after checking b>-1.
The finite sum is evaluated with outward ball arithmetic. Its positive
enclosure, multiplied by pi/2 and square-rooted, encloses J(a).

## Conditional consequence and scope

The actual inverse-floor theorem T4-097, when its full hypotheses
and independent review are supplied, gives M>=1/(1+c-ca).
The separately audited contraction-radius ceiling is
R<sqrt(8 pi)(1+c-ca)/(1+a). Consequently M Y(F)<=R would require
Y(F)<C(a). The cell certificate contradicts that requirement.

This excludes only that specified dyadic closure scheme for this
exact reference, conditional on the inverse-floor theorem and the
common normalization of its hypotheses. It does not exclude an exact
profile, another norm, an approximate-inverse method, or a different
reference. The scalar cover is new and needs a peer numerical check.
The seven peer point values are compared independently here.
