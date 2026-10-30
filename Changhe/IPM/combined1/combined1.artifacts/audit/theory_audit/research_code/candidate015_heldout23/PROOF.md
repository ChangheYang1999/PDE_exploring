# Whole-plane monomial probes without high-degree expansion

Status: complete analytic derivation; each numerical application remains
OPEN until independently reproduced. This is a necessary-distance test,
not an existence criterion.

## Statement and assumptions

Let R be a smooth S1 density, even in x and odd in y, with smooth canonical
incompressible velocity U_R and growth O(r^gamma), 0<gamma<1. Fix c=1/gamma.
Suppose rho=R+h is an exact distributional solution of

    (cX+U[rho]).grad rho-rho=0,

where h is S1 in L2(R2), U[rho]=U_R+U[h], and the Fourier multiplier
U has symbol (xi1 xi2/|xi|2,-xi1^2/|xi|2). Then ||U[h]||2<=||h||2.
For every positive odd n and integer K>=(n-1)/2 define

    t=r2/(1+r2), v=1-t, phi=r v2 t^K sin(n theta).

With F=(cX+U_R).grad R-R, set

    I=int F phi, M=(2c+1)phi+(cX+U_R).grad phi,
    D=||M||2+||phi grad R||2, H=||grad phi||infinity.

For any certified Hbar>=H with Hbar>0, every such solution satisfies

    ||h||2 >= 2|I|/[D+sqrt(D2+4 Hbar |I|)].             (1)

The exact candidate015 input and its canonical conversion are frozen in
../new_successor_weak/data/015. This application uses n=23,K=600. The pair
is absent from the102 objective rows explicitly stored in the raw candidate's
metadata and is in the held-out set of theory_v04. The same absence is
checked for the documented013 parent objective. This is a held-out label
relative to the documented objectives; it does not assert that the candidate
was selected without inspecting any previous diagnostics. The necessary
inequality itself is valid regardless of that label. No optimality or
span-wide lower bound is inferred.

## Weak proof and regularity

At the origin, r^(2K+1)sin(n theta) is a polynomial harmonic of degree n
times a nonnegative integral power of r2. The remaining factor is smooth
in r2. Thus phi is smooth on the plane. At infinity phi=O(r^-3) and its
gradient is O(r^-4). All reference pairings are absolutely integrable.

Subtract the reference equation and first test with compactly supported
cutoffs of phi. Integration by parts gives a term bounded by ||M||2||h||2,
a term bounded by ||phi grad R||2||U[h]||2, and the quadratic term bounded
by H||h||2||U[h]||2. The cutoff terms vanish by Cauchy-Schwarz on escaping
annuli and the displayed decay. Thus |I|<=D||h||2+Hbar||h||2^2, which gives
(1). The same integration by parts gives I=-int R M for the reference;
this identity is checked independently in every computation.

## Exact radial supremum

Write A=2K+1, B=2K+4. The radial and angular gradient amplitudes are

    g(t)=t^K(1-t)^2(A-Bt),
    q(t)=n t^K(1-t)^2.

At fixed radius, maximizing the squared norm over theta gives
max(g(t)^2,q(t)^2), because sin(n theta)^2+cos(n theta)^2=1.
For K>0 both amplitudes vanish at t=0 and t=1. The positive angular
amplitude has its maximum at t=K/(K+2). The non-endpoint critical points
of g are exactly the roots in (0,1) of

    B(K+3)t^2-[(K+2)A+(K+1)B]t+KA=0.                  (2)

Indeed this is g'(t) after dividing by t^(K-1)(1-t).
The maximum of |g| occurs at an endpoint or a critical point; zeros
of g cannot create a positive maximum. Outward arithmetic enclosing
the roots of (2) and these three values therefore certifies H.
Round their upper endpoints upward to a rational Hbar. The case K=0
would additionally retain the endpoint g(0)=1 and is not used here.

## Compact polynomial fields and moments

Use the exact polar fields

    R=r sum_(j,m) v^((j+1)delta/2) R_jm(t) sin(m theta),
    psi=r2 sum_(j,m) v^((j+1)delta/2) S_jm(t) sin(m theta),
    delta=1-gamma, U_R=grad-perp psi.

Keep t^K outside every polynomial operation. The two probe amplitudes
are then represented by 1 and A-Bt. Products contributing to ||M||2^2
and ||phi grad R||2^2 have the common factor t^(2K); those contributing
to either formula for I have t^K. Angular orthogonality and elementary
sine/cosine products are exact, and every background angular mode that
can contribute is retained. This is the same full-plane derivation as
../new_successor_weak/PROOF.md, with the large monomial kept factored.

Every remaining radial scalar has the form

    int_0^1 t^(L+1)(1-t)^b P(t)dt, b>-1, L>=0 integer. (3)

For P=sum p_j t^j define B_l(b)=int t^(l+1)(1-t)^b dt. Direct integration
gives B_0=1/[(b+1)(b+2)]. Integration by parts, whose boundary terms
vanish for b>-1, gives

    B_(l+1)(b)=(l+2)/(l+b+3) B_l(b).

Thus (3)=sum_j p_j B_(L+j)(b), without expanding t^L about the other
endpoint. All factors have exact rational parameters and positive
denominators. Finite outward arithmetic gives an enclosing interval;
positivity of norm squares, separation of the pairing from zero,
agreement of the two pairing formulas and the strict rational radius
are required checks. No truncated tail expansion or finite-radius
quadrature is used.

## Scope and dependencies

Dependencies are the audited L2 velocity multiplier, weak identity and
polar field construction; exact raw canonicalization is separately bound
to its hashes. The candidate is not changed. A positive number from (1)
only excludes a ball smaller than that number in the stated canonical
L2 chart. All source, code and result hashes, actual runtimes, precision,
endpoint exponents, exact probe and supremum evidence are retained.
