# No nondegenerate radial quotient profile even in the C1 class

Date: 2026-10-20. Status: complete independent proof; 47 exact supporting checks PASS at23:50:15; actual Claude Opus 5.5 independent review CONFIRMED on2026-10-21 at00:17Z. Scope: the radial quotient subclass rho=y f(|X|). The general nonradial problem remains open.

## 1. Statement

Let ell>1. Suppose rho is C^1 on the whole plane, rho(X)=y f(r), f is C^1 for r>0, and f extends continuously to r=0 with a=f(0)!=0. Suppose for some 0<gamma<1,

    |rho(X)|+(1+r)|grad rho(X)|<=C(1+r)^gamma.

Let U be the canonical full-plane velocity with the required parities, divergence zero, curl U=-rho_x and U=o(r) at infinity. Assume the classical transport equation

    (ell X+U).grad rho=rho

holds everywhere. These hypotheses are inconsistent. In particular no such profile exists in the smooth primary class or its radial C^1 variants. No sign, monotonicity or analyticity assumption on f is made. The stated regularity of f follows from rho in C^1; the proof uses only the density portion of the far-field growth bound.

## 2. Canonical radial inverse and center relation

Set

    J(r)=r^(-4) int_0^r s^3 f(s)ds, psi=-xy J(r).

Then r J'=f-4J. Differentiating this identity gives
r J''+5J'=f'. Direct differentiation of psi therefore gives -Delta psi=rho_x for r>0. The C^1 condition on rho implies r f'(r)->0 as r->0: along the vertical axis rho_y(0,r)=f(r)+r f'(r), and both rho_y(0,r) and f(r) tend to a. Thus J->a/4, r J'->0 and (r partial_r)^2 J->0. Every Cartesian second derivative of psi is a linear combination of J, rJ' and (r partial_r)^2 J with bounded angular coefficients; its limit is the corresponding derivative of -a xy/4. The removable-point lemma for a C^1 function with convergent second derivatives off one point shows that psi extends as C^2 and U=(-psi_y,psi_x) as C^1 at zero, with DU(0)=diag(a/4,-a/4). The Poisson identity holds there by continuity, so it has no point-supported defect.

For r>=1, the density growth along the vertical axis gives |f(r)|<=C r^(gamma-1). The defining integral yields J=O(r^(gamma-1)); also r J'=f-4J has that bound. Consequently U=O(r^gamma), in particular o(r). Its parities, divergence and curl have the required values. Two such canonical velocities differ by an entire harmonic vector field of sublinear growth. Interior harmonic derivative estimates force this difference to be constant; U1 is odd in x and even in y, and U2 is even in x and odd in y; these parities force the constant to vanish. Hence this explicit U is the canonical velocity.

Divide transport along the vertical axis by y and let y tend to zero. Its vertical linear coefficient is ell-a/4, so a!=0 implies

    ell-a/4=1.

Write D=ell-1. It follows that a=4D>0 and J(0)=D. This sign is derived, not assumed.

## 3. Two exact transport projections

Write dot f=r f'(r), dot J=f-4J and theta for the polar angle. The polar velocity is

    U_r/r=J cos(2theta),
    U_theta/r=(J-f/2)sin(2theta).

The density derivatives are rho_r=(f+dot f)sin(theta) and r^(-1)rho_theta=f cos(theta). Multiplying these expressions gives the exact residual decomposition

    R/r=C1 sin(theta)+C3 sin(3theta),
    C1=(ell-J/2)dot f+D f-f^2/4,
    C3=J f+(J/2)dot f-f^2/4.                         (1)

Full transport implies C1=C3=0 at every r>0. Near zero, f>0 and J>0; also v=ell-J is positive and tends to1. Subtract the two equations in(1):

    v dot f+(D-J)f=0.

Since J-D=1-v, this implies

    dot f/f=(1-v)/v.                                (2)

The equation C3=0 gives dot f/f=f/(2J)-2. Comparing with(2) yields

    f=g(J):=2J(ell+1-J)/(ell-J)=2J+2J/(ell-J),
    dot J=f-4J=2J(1-v)/v.                           (3)

Every division has been justified on a sufficiently small positive-radius interval. Differentiating f=g(J) gives dot f=g'(J)dot J, with

    g'(J)=2+2ell/v^2.

Together with(2)-(3) this gives

    0=(1-v)(2J g'(J)-f)/v,
    2J g'(J)-f=2J(v^2-v+2ell)/v^2.                 (4)

The second factor is strictly positive: J>0, v>0 and
v^2-v+2ell=(v-1/2)^2+2ell-1/4>0. Thus v=1 throughout that interval. We conclude J=D and f=4D there. No expansion beyond C^1 was used.

## 4. Continuation and contradiction

The equation C1=0 can be written, in t=log r,

    dot f=f(f-4D)/(4ell-2J), dot J=f-4J.             (5)

The constant pair f=4D, J=D is an equilibrium, and its denominator is 2ell+2>0. The right side of(5) is smooth on a neighborhood of this equilibrium, so the elementary local uniqueness theorem applies at every finite t where the pair takes this value. The set of such t is nonempty by Section3, closed by continuity, and open by local uniqueness. Since the solution is defined for all finite t, it equals the constant pair on the whole connected real line.

Hence rho=4D y everywhere. This contradicts the stated growth with gamma<1. It also makes U=diag(D,-D)X, inconsistent with the canonical sublinear law. Both contradictions use the growth hypothesis: it was needed to identify -xyJ as the canonical stream. The first contradiction already proves the theorem.

## 5. Relation to the projected finite-regularity family

Result90 constructs canonical C^1 radial pairs with C1=0 but C3<0. Their low origin regularity allows the first projection to vanish. This theorem shows that imposing the third projection eliminates them and every other C^1 nondegenerate radial quotient profile. It gives no exclusion for genuinely nonradial quotients, whose higher angular modes couple into C1 and C3.

Dependencies: the standard uniqueness theorem for a smooth ordinary differential equation and the elementary sublinear harmonic Liouville argument. All inverse and transport formulas are rederived above. Exact arithmetic checks support the algebra only; the proof supplies the continuum and regularity statements.
