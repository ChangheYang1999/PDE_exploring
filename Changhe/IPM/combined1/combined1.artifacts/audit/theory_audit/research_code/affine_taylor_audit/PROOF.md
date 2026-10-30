# Exact Taylor repair and the linearized affine constraints

The nonlinear repair in T4-211 is not generally a particular solution of
its linearized constraint equation. This note checks the identification
made in R1-029 R3. It does not change the physical-metric damping lemma.

## Statement and notation

For a smooth potential chi near zero put rho=-partial_y Delta chi,
u=(-chi_xyy,chi_xxy), and F(chi)=(cX+u).grad rho-rho. Let C(chi) be the
five coefficients of x^2,y^2,x^4,x^2y^2,y^4 in F(chi)/y. Suppose chi has
the parity, strain and nonvanishing divisors of T4-211. Let eta be its
exact five-parameter repair there, so C(chi+eta)=0. Write alpha,beta for
the coefficients of eta_(2,1),eta_(0,3). Then

    C(chi)+DC(chi)[eta]
        = (0,0,192 alpha^2,8640 alpha beta,0).          (1)

In particular alpha != 0 implies DC(chi)[eta] != -C(chi). The nonlinear
repair still belongs to the frozen007 potential span when c=c007, and
preserves the tail and strain constraints. Those facts are distinct from
solving the linearized affine Taylor equation.

## Proof

Both rho and u depend linearly on the potential. Therefore the exact
quadratic expansion is

    F(chi+eta)=F(chi)+DF(chi)[eta]+u[eta].grad rho[eta].

The leading potential terms of eta have degree six and equal

    alpha x^4 y^2 + beta y^6.

Their density and velocity are respectively

    rho6=-24 alpha x^2 y-120 beta y^3,
    u6=(-8 alpha x^3,24 alpha x^2 y).

Direct differentiation and multiplication give

    u6.grad rho6 = -192 alpha^2 x^4 y
                         -8640 alpha beta x^2 y^3.

Every later potential term has degree at least eight. Its density and
velocity have degree at least five, so its interaction with the degree
six potential starts at degree seven in F and degree six in F/y. It
cannot contribute to the five coefficients in C. Extracting those
coefficients and using C(chi+eta)=0 proves (1).

The exact007 parameters are already independently reproduced in
N4-173/T4-227. The check in verification/result.json tests alpha != 0,
reconstructs both original and repaired jets from those exact inputs,
and compares all five entries of (1) with the exact derivative routine.
Its data are retained as exact JSON. This candidate check supplements
the displayed polynomial identity; it is not used to infer the identity
from finite examples.

Dependencies: the definitions above and the audited T4-211 projection.
The conclusion refutes the specific R1-029 identification. The abstract
affine minimization theorem remains valid for a w0 which actually solves
DC(chi)[w0]=-C(chi).
