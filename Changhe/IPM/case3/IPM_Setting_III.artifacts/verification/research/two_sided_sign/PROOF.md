# Two-sided density bounds under the source dynamics

Date: 2026-10-20. Status: independently proved; source dynamics is an additional hypothesis. No existence conclusion.

## 1. Statement, notation and dependencies

Let (rho,U,ell) be an exact primary full-plane IPM profile with the symmetry, canonical inverse and growth assumptions of PROMPT. Put a=rho_y(0)!=0, p=1/ell in (0,1), A=2ell-1 and W=ell X+U. Assume Hdyn: zero is the only equilibrium, every nonzero backward orbit tends to zero and every nonzero forward orbit escapes. Define q=rho/(a y) off y=0 and q(x,0)=rho_y(x,0)/a. This extension is smooth by oddness in y.

Then there exist finite constants 0<c<=C such that on the whole plane

    c(1+|X|)^(p-1) <= q(X) <= C(1+|X|)^(p-1).              (1)

Furthermore the smooth far-field trace satisfies

    Theta0'(0)/a > 0,
    min_(0<=theta<=pi) Theta0(theta)/(a sin(theta)) > 0,     (2)

where the quotient at the endpoints is defined by its smooth extension. Conversely, (1) implies Hdyn. The constants depend on the profile and its spatial scale. This does not determine ell or a, and it makes no assertion that Hdyn holds for every primary profile.

Dependencies: the exact source and axis identities (results2,4), strict-sign equivalence and its nonhyperbolic case (result29), and all-order far-field bounds and the trace (result32). The forward implication also follows from result38, but its finite-equilibrium removal is not required here: Hdyn itself supplies strict sign and absence of axis equilibria.

## 2. Axis amplitude of the derivative

Write w(x)=W1(x,0) and g(x)=rho_y(x,0). The differentiated transport equation and div W=2ell give

    w g'=(w'-A)g.                                        (3)

Hdyn implies w(x)>0 for x>0 and g/a>0 everywhere on the axis. This can also be checked directly: w is positive near zero, cannot change sign without an equilibrium, and the nonzero g near zero propagates by the scalar ODE(3). By the far-field symbol bounds,

    w(x)=ell x+O(x^p),  w'(x)=ell+O(x^(p-1)).

Since ell-A=1-ell=ell(p-1),

    g'/g=(p-1)/x + e(x),  e(x)=O(x^(p-2)).                (4)

The error is integrable at infinity because p<1. Integrating the logarithm from any fixed x0>0 therefore gives a finite nonzero signed constant G with G/a>0 and

    g(x)=G x^(p-1)(1+O(x^(p-1))).                         (5)

In detail, log(|g(x)| x^(1-p)) is its value at x0 plus the convergent integral of e, so its exponential cannot vanish or become infinite. The tail integral is O(x^(p-1)).

The C1 angular far-field convergence gives

    r^(1-p)g(r)=partial_theta[r^(-p)rho(r cos(theta),r sin(theta))]_(theta=0)
                -> Theta0'(0).

Thus G=Theta0'(0), proving the first assertion in(2). Reflection symmetry gives the same positive endpoint quotient at theta=pi, since Theta0'(pi)=-Theta0'(0).

## 3. Interior angles and uniform division by sin(theta)

Hdyn and the characteristic formula give rho/a>0 for y>0. To show that this strict sign does not degenerate at a fixed far angle, use the exterior scattering map. Every angle theta_infty in (0,pi) corresponds to a trajectory meeting a fixed large upper semicircle at a point with positive rho/a. Along that trajectory, the exact relation e^(-t)rho(Phi_t X)=rho(X) and the nonzero radial scattering amplitude identify Theta0(theta_infty)/a as that positive value times a positive finite factor. Therefore Theta0/a>0 throughout (0,pi). This argument uses existence and invertibility of the exterior angular scattering map, which follow by integrating the angular equation and its derivatives using the symbol bounds. No compactness limit of merely positive functions is used to infer strict positivity.

By smoothness, oddness at the endpoints and(5), the function H(theta)=Theta0(theta)/(a sin(theta)) extends continuously to [0,pi], is positive there, and has a positive minimum and a finite maximum.

Put F_r(theta)=r^(-p)rho(r cos(theta),r sin(theta)). The far-field theorem gives ||F_r-Theta0||_(C1)<=C0 r^(p-1), and F_r-Theta0 vanishes at both endpoints. The fundamental theorem of calculus bounds its value by C0 r^(p-1) min(theta,pi-theta). Since min(theta,pi-theta)<=C1 sin(theta) on [0,pi], division by sin(theta) retains the same uniform error, including at the endpoints. Consequently

    q(r cos(theta),r sin(theta))
      =r^(p-1)[H(theta)+O(r^(p-1))]

uniformly on the upper semicircle. Reflection gives the same bound below it. The positive minimum of H proves(1) outside a sufficiently large disk.

## 4. Interior completion and converse

On a fixed compact disk, q is smooth and strictly positive: off the axis this is the strict-sign characterization, and on the axis it is g/a>0. Its minimum is positive and its maximum finite. Combining these bounds with the exterior bounds proves(1) everywhere, after changing c,C and replacing r by1+r.

Conversely, (1) implies rho/(a y)>0 off the axis, hence Hdyn by the independently proved strict-sign equivalence, including possible degenerate axis equilibria. This converse does not rely on numerical signs or a finite spatial box.

Scope: an exact profile satisfying Hdyn has a strictly positive normalized far trace, with a uniform angular margin, and its density is quantitatively comparable to a y(1+r)^(p-1). For an approximate field, sampled positivity alone proves none of the hypotheses used above.
