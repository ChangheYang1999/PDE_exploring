# Exact weighted tail tests for the canonical candidate family

## Statement, spaces and scope

Fix the exact campaign parameter c=4076476460239181/2251799813685248,
gamma=1/c and delta=1-gamma. Write E_a=L2(R2,(1+r^2)^(-a)dX).
The density R is one of the exact canonical rational-coefficient
potential candidates listed in data/inputs.json. All velocities use the
canonical IPM choice, including the contact term. This audit treats
only the listed unscaled polynomial-potential candidates; a scaled
rational-pole candidate needs its own expansion and is not covered by
a coinciding file name or branch label.

For -2<a<=1+gamma the previously audited weighted-tail theorem
../weighted_forced_tails/PROOF.md implies the following necessary
condition. If R+h is an exact stationary S1 solution at this c with
h in E_a, every finite homogeneous residual sector of R of exponent
q>=a-1 must vanish. Equality is included: r^(a-1) has logarithmically
divergent squared E_a norm at infinity. The theorem's annular weak
argument, not merely nonmembership of F(R) in E_a, establishes this
necessity without differentiability assumptions on h beyond its stated
weak equation. Its velocity bounds hold on the centrally odd class.

We independently compute all sectors needed for every a in this
interval. The first nonzero exponent q_* gives an excluded correction
class for -2<a<=q_*+1. For q_*+1<a<=1+gamma this particular necessary
tail test gives no obstruction; it proves no existence. The exact
rational threshold q_*+1 is the statement. A decimal approximation
must not replace it with an expanded interval.

The audit also compares the first four density profiles of the
candidates. Equality of these profiles is sufficient for equality of
the affine L2 classes: all omitted terms have exponent below -1,
and the exact candidates are smooth on compact sets. Equality of
classes does not identify distances from different references.

## Direct expansion of the potential

The canonical input represents

    chi=sum_(j,m) (1+r^2)^(p_j) P_jm(t) cos(2m theta),
    p_j=(3+gamma-j delta)/2,
    t=r^2/(1+r^2),
    R=-d_y Delta chi, psi=d_x d_y chi, U=grad-perp psi.

Every P_jm is a finite polynomial with exact rational coefficients.
With z=r^-2,

    (1+r^2)^p P(t)
      =r^(2p) (1+z)^p P(1/(1+z)).

Its coefficients at z^0 and z^1 are respectively

    A_0=P(1), A_1=p P(1)-P'(1).                              (1)

The corresponding homogeneous potential term is A_q r^d cos(n theta),
d=2p-2q, n=2m. Its density contributions are

    sin((n+1)theta): -A_q(d^2-n^2)(d-2-n)/2,
    sin((n-1)theta): +A_q(d^2-n^2)(d-2+n)/2,                  (2)

at exponent e=d-3. Its stream contributions are

    sin((n+2)theta): +A_q(d-n)(d-n-2)/4,
    sin((n-2)theta): -A_q(d+n)(d+n-2)/4,                     (3)

at exponent e+1. Negative sine frequencies change sign and the zero
frequency vanishes. Formulas (2)-(3) follow by differentiating the
single homogeneous monomial. They bypass the peer's construction and
endpoint differentiation of the complete density and stream polynomials.

For every resulting angular density Theta and stream Psi, we check
coefficientwise the angular Poisson equation

    [d_theta^2+(e+1)^2]Psi=-e cos(theta)Theta+sin(theta)Theta'. (4)

No numerical norm or sample-value comparison replaces this identity.

## Complete residual sectors above the threshold

Index a sector by (K,L), with

    e_(K,L)=1-K delta-2L, K>=1, L>=0.

The input density and stream have K=j+1<=8. The drift contribution
is (c e_(K,L)-1)Theta_(K,L). Two homogeneous terms contribute to the
sector (K1+K2,L1+L2) by

    B(Psi1,Theta2)=-e2 Psi1' Theta2+(e1+1)Psi1 Theta2'.       (5)

Every coefficient of (5) is computed using exact sine/cosine product
identities. Thus the complete residual coefficient is the drift term
plus all pairs with matching K and L. The checker retains K<=9 and
L<=1 and verifies all angular coefficients exactly.

This finite set includes every sector with exponent at least -3:
K>=10 gives 1-10delta<-3 and L>=2 gives 1-delta-4<-3. The exact
radial factors are analytic in z near zero, so truncation has a
uniform differentiated asymptotic remainder. The finite number of
branches and products leaves a remainder O(r^(-3-epsilon)) for some
explicitly positive epsilon determined by these omitted exponents.
It belongs to E_a for every a>-2. Distinct retained sector labels
have distinct exponents at this exact c, checked in rational arithmetic.

Consequently, the largest nonzero computed sector is the genuine
leading residual sector, and all zero tests above any weighted
threshold are complete. A nonzero trigonometric polynomial has
positive angular L2 norm; no lower bound on that norm is needed for
the qualitative obstruction. We also enclose its norm with Arb to
compare the peer's approximate diagnostics.

## Independent comparisons and interpretation

The checker uses the canonical inputs already reconstructed in this
lane, records their hashes, and exports every density, stream and
residual coefficient as exact JSON. For the five candidates of T2
the review of T4-249 R3 it compares the complete nonzero-sector set, all18
Poisson checks, exact q_*, the nonzero first-descendant density set,
and every printed sector norm. It separately compares the first four
profiles to those of007, auditing the common-affine-class assertion
in the review of T4-234 R3.

The expected first sectors, to be verified rather than assumed, are:
state131 at(2,0), d2 and Mpen2 at(7,0), and005 and007 at(4,1).
The last is a non-ladder descendant from regularization. It cannot be
dropped merely because the leading branch coefficients satisfy the
ladder equations. For other listed candidates the output states the
computed sector; it is not inferred from an optimization label.

A confirmed exclusion concerns the exact frozen reference, fixed c,
canonical velocity and the specified correction class. It does not
exclude corrections in a larger weighted class, perturbations of the
leading angular profile, or arbitrary stationary IPM solutions.
