# Cubic origin relations for an exact C3 profile

Status: CONFIRMED after independent derivation and the completed Opus 5.5 review at ../../evidence/opus_review_09/answer.md. Date: 2026-10-20. The actual returned model was claude-opus-5-5; all proposed clarifications were independently checked.

## Exact statement and scope

Replace local smoothness of rho in the primary class by C3, retaining a0=rho_y(0) nonzero, the parities, the defining PDE, the canonical inverse and the same sublinear density/gradient growth. Explicitly, U=(-psi_y,psi_x), -Delta psi=rho_x, W=c_l X+U, W dot grad rho=rho, c_l>1, and for some 0<gamma<1, |rho(X)|+(1+|X|)|grad rho(X)| <= C(1+|X|)^gamma. The canonical law fixes the modal inverse and excludes a harmonic strain. Then rho has the Taylor expansion

    rho=a0 y+b x^2 y+e y^3+o(r^3),

and psi has a quartic Peano expansion

    psi=cxy+q1 x^3 y+q2 xy^3+o(r^4).

The relations are c=1-c_l, A=2c_l-1,

    q1=-2Ab/(3a0), q2=-2e/a0,
    q1+q2=-b/3, 6e=(a0-2A)b,
    q1-q2=lim_(epsilon -> 0) integral_epsilon^infinity f4(r) r^(-3) dr,

where f4 is the sin(4 theta) coefficient of rho_x. The final integral is improper; no absolute convergence at zero is claimed at C3 regularity. For C^(3,alpha), alpha>0, it is absolutely convergent by f4=O(r^(2+alpha)).

Dependencies are the canonical modal inverse and center relation in ../inverse/PROOF.md and ../origin/PROOF.md. The inverse has enough local regularity to give U continuously differentiable: local elliptic estimates, or the local singular integral after subtracting smooth Taylor terms, give psi in C^(3,alpha) for every alpha<1 when rho is C3. The proof below uses only the linear expansion of U until it derives more from the transport equation.

## Obtaining the quartic expansion from the coupled equation

The C3 Taylor expansion and parity give

    rho_x=2bxy+o(r^2), rho_y=a0+b x^2+3e y^2+o(r^2).

By continuity rho_y is nonzero in a neighborhood of zero. The center relation gives W1=Ax+o(r). Solve the exact transport equation for W2:

    W2=(rho-W1 rho_x)/rho_y
       =y-(2Ab/a0)x^2 y-(2e/a0)y^3+o(r^3).

Since psi_x=W2-c_l y and psi(0,y)=0 by oddness in x, integrate in x along the horizontal segment from (0,y) to (x,y). The remainder is o(r^4), uniformly in direction: its integrand is bounded by o(1)(x^2+y^2)^(3/2), and the segment has length at most r. This proves the quartic Peano expansion and the formulas for q1,q2.

A Peano expansion alone need not justify twice differentiating the remainder. Instead define

    psi_epsilon(X)=[psi(epsilon X)-c epsilon^2 x y]/epsilon^4.

It converges locally uniformly to Q4=q1 x^3 y+q2 xy^3. The exact Poisson equation gives

    -Delta_X psi_epsilon=epsilon^(-2) rho_x(epsilon X) -> 2bxy

locally uniformly. Pass to distributions to conclude -Delta Q4=2bxy. Therefore 6(q1+q2)=-2b, which yields the remaining local relation. This step does not assert C4 regularity of psi.

## The improper nonlocal moment

Let h4 be the sin(4 theta) stream coefficient. Since the leading quadratic term of rho_x is 2bxy, it has no sin(4 theta) part, so f4=o(r^2). The canonical modal formula gives

    h4(r)/r^4=(1/8)[r^(-8) integral_0^r s^5 f4(s) ds
                          + integral_r^infinity s^(-3) f4(s) ds].

The first term in brackets tends to zero by f4=o(r^2). The quartic Peano expansion gives h4(r)/r^4 -> (q1-q2)/8. Consequently the improper integral converges and equals q1-q2. Its tail at infinity converges absolutely: the gradient hypothesis gives |f4(r)|=O(r^(gamma-1)), so |f4(r)|r^(-3)=O(r^(gamma-4)). This is an implication of the coupled equation, not C3 regularity alone.

## Why the coupled equation is essential

Choose smooth radial cutoffs equal to one near zero and compactly supported, and set near zero

    rho=a0 y+r^3 sin(5 theta)/log(1/r),  a0>0.

Use the cutoffs to define it globally, and extend the second term by zero at zero. Every derivative through order three of the second term tends to zero at zero, since it is a degree-three angularly smooth function multiplied by 1/log(1/r), whose radial derivatives add inverse logarithmic factors. Thus rho is C3 with cubic Taylor coefficients b=e=0 and the required parities and sublinear growth. Its sin(3 theta) coefficient is zero, so the canonical strain is c=-a0/4. Choosing c_l=1+a0/4 satisfies the primary center relation.

Nevertheless its source has

    f4(r)=4r^2/log(1/r)+(1/2)r^2/log(1/r)^2

near zero. The improper integral of f4/r^3 diverges to positive infinity. The stream function therefore has no finite quartic Peano coefficient in that mode. This manufactured pair cannot satisfy the transport equation; it demonstrates exactly why one must use that equation in the preceding proof. It is not a counterexample to the theorem, nor an admissible smooth primary profile.
