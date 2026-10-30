# A point residual gives a necessary correction size

## Statement and hypotheses

Let s>0 and let N_s be the exact norm in ../alternative_route/PROOF.md, with all ordered derivatives and the stated positive energy weights. Let rho_bar be a C1 reference with a canonical velocity Ubar defined at the point X. Put

    V(X)=c X+Ubar(X),
    F(X)=V(X).grad rho_bar(X)-rho_bar(X),
    C0=1/[2 sqrt(pi(1+s))],
    C1=1/sqrt(8 pi s(1+s)),
    A(X)=C1 |V(X)|+C0[1+|grad rho_bar(X)|],
    B=C0 C1.

Every correction h in N_s for which F(rho_bar+h;c)=0 pointwise at X satisfies, with r=N_s(h),

    |F(X)| <= A(X) r+B r^2.                               (1)

Consequently

    N_s(h) >= 2 |F(X)|/[A(X)+sqrt(A(X)^2+4B |F(X)|)]       (2)

when F(X) is nonzero. Any strict violation of (1) with a proposed upper radius excludes a solution in that ball. This necessary test does not require the residual to belong to N_s, a background inverse, exact normalization, or far-field admissibility. Those conditions remain necessary for the separate sufficient closure theorems.

There is a corresponding test for a computed linear correction. Let L be the fixed-reference derivative and suppose g is in its high generator domain, N_s(g)<=m and N_s(F+Lg)<=epsilon. Then

    |F(X)| <= A(X) m+C0 epsilon.                          (3)

A violation excludes the proposed linear-defect certificate. It does not exclude a larger correction or a solution in a different function space.

## Proof of the pointwise constants

With the Fourier convention hat f(xi)=integral f(X) exp(-i X.xi) dX, the stated energy dominates H^(2+s): its squared polynomial multiplier is at least (1+|xi|^2)^(2+s), because omega>=1 and

    |xi|^4+2^14 |xi|^2+2^18 >= (1+|xi|^2)^2.

Fourier Cauchy-Schwarz and polar integration give

    |h(X)| <= C0 ||h||_(H^(2+s)) <= C0 N_s(h),

since (2pi)^(-2) integral (1+|xi|^2)^(-2-s) dxi =1/[4pi(1+s)]. The vector multiplier of U has Euclidean magnitude at most one. Apply the same bound to every real unit projection of U[h](X) to obtain

    |U[h](X)| <= C0 N_s(h).                               (4)

For each real unit vector e, the squared Cauchy-Schwarz constant for e.grad h(X) is

    (2pi)^(-2) integral |e.xi|^2 (1+|xi|^2)^(-2-s) dxi
       = 1/[8pi s(1+s)].

The value is independent of e by rotational symmetry. Taking e in the direction of the real vector grad h(X) yields

    |grad h(X)| <= C1 N_s(h).                             (5)

This pointwise directional calculation is a factor sqrt(2) sharper than summing separate bounds for the two gradient components. It is used only for this necessary witness test; no sharper rough-transport inverse constant is asserted.

## Proof of the residual inequalities

Expand the exact equation:

    0 = F + V.grad h - h + U[h].grad rho_bar + U[h].grad h.

Apply (4)-(5) term by term at X to obtain (1). The positive root of B r^2+A r-|F| is (2); the displayed rationalized form avoids subtracting two nearby positive numbers.

For the linear correction, F+Lg=D gives |F(X)|<=|Lg(X)|+|D(X)|. The same linear bounds give |Lg(X)|<=A(X)m, and (4)'s scalar bound gives |D(X)|<=C0 epsilon. This proves (3).

## Numerical use and scope

For a rigorous exclusion at radius r, it is enough to have a lower bound on |F(X)| and upper bounds on |V(X)| and |grad rho_bar(X)| at a single exact point, plus upper bounds for C0,C1. All quantities refer to one exact candidate and one norm ID. A finite mesh without interval error bounds does not supply this exclusion. The test is particularly useful before trying to certify an expensive Newton correction for a refit with large point residuals.

This note contains no measured candidate exclusion. It does not interpret failure of a sufficient residual threshold as nonexistence. Only inequality (1), independently necessary for a small correction, can support the exclusions described here.

## A uniform obstruction for every positive baseline gap

Suppose a proposed correction is in a ball of radius r for which the sharper baseline inverse gap is positive:

    1/10 - 4800s - 5r/sqrt(s) > 0.

Then s<1/48000 and r<sqrt(s)/50<1/10000. Using pi>3 gives the simple rational consequences

    C1 r < 1/240,    C0 r < 3/100000,
    C0 C1 r^2 < 1/8000000.

Therefore every exact solution in any such ball, for any admissible s, must satisfy at every point

    |F(X)| < |V(X)|/240
             +(3/100000)(1+|grad rho_bar(X)|)+1/8000000.  (6)

This is a necessary condition uniformly over all positive-gap balls, not just the particular s=2^-18, r=2^-16 choice. If a certified point value violates (6), no refinement of the scalar residual threshold or computed linear correction can close an existence proof inside one of those balls around that exact reference. It does not exclude an exact solution outside those balls, a different high norm, or a different reference.
