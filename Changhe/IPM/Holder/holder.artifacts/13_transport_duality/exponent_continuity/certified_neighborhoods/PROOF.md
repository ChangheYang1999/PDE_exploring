# Certified exponent intervals with strict diagonal separation

## Statement and hypotheses

Use the real Euclidean homogeneous Holder spaces and operators from
../../../01_setup/PROOF.md. In particular C_alpha is the common norm of
T_xx and T_xy, and D_alpha is the norm of R_1^2=T_xx-I/2. The numbers in
verification/intervals.json specify closed intervals

    [alpha0-radius, alpha0+radius]

on which C_alpha<D_alpha. The centers, radii and cutoff exponents are
exact rational or integer input data. The scalar inequalities are checked
with directed 320-bit Arb enclosures by code/certify_separation_neighborhoods.py.
No floating LP estimate is used.

## Proof of the certificate rule

For each row, U is an accepted upper bound for C_alpha0, V is an accepted
lower bound for D_alpha0, and g=V-U>0. The source is the exact safe
endpoint fields of data/verified_table.json. Fix exact a<alpha0<b,
epsilon=2^(-N) and R=2^M. Evaluate the quantities Ebar, m and L of the
accepted continuity theorem in ../PROOF.md:

    Ebar = 2epsilon^a/(pi a)
           +(1+2epsilon)^b epsilon^2/(2(1-epsilon)^2)
           +2^b R^(b-1)/((1-b)(1-1/(4R^2))^2),
    m = (2/pi) log((R+1/2)/epsilon),
    L = max(1/(e a), (2R)^b log(2R)).

For any alpha in [a,b], that theorem gives

    D_alpha-C_alpha >= g-4Ebar-(2m+1/2)L |alpha-alpha0|.     (1)

The certificate checks that alpha0-radius and alpha0+radius lie in [a,b]
and in (0,1), and that the right side of (1), with radius replacing the
absolute difference, has a strictly positive lower endpoint. Therefore
the entire closed interval has strict separation. Finite precision only
weakens the certified margin; no equality decision is required.

The choice of cutoffs may use a floating initial guess. Each chosen
integer is then checked in the displayed exact rule, so the guess has no
logical role. These intervals are sufficient intervals only. They are
not assertions about the endpoints of the full separation set, nor do
they give the exact operator norms. Extremely short radii near alpha=1
reflect the conservative uniform-tail continuity estimate.

## Dependencies and status

The analytic dependency is the accepted exponent-continuity theorem.
The input operator endpoints are the already audited table entries.
The certificate records source hashes, all exact parameters, and the
positive margin enclosure for every row. No quadrature is repeated.
Every printed four-place lower bound is rounded down from the exact rational
lower endpoint of its Arb ball. A separate 640-bit implementation evaluates
the same formulas using logarithmic powers, verifies containment in the
320-bit enclosures, and checks every printed bound against its own lower
endpoint. Its record is verification/independent_replay.json. The final
acceptance status is recorded in the verifier ledger.
