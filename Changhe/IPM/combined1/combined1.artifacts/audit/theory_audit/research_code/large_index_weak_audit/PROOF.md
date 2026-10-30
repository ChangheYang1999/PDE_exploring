# Independent large-index weak norms and matched envelopes

## Statement and hypotheses

Let R be the exact canonical candidate007, with c=4076476460239181/2^51,
gamma=1/c and delta=1-gamma. Use the immutable canonical input bound in
the source manifest. Let h be a real S1 L2 correction such that R+h
solves (cX+U[R+h]).grad(R+h)-(R+h)=0 in distributions, with canonical
U[R+h]=U_R+U[h] and the standard L2 multiplier U. The reference fields
are smooth, sublinear and obey the already audited origin and tail
constraints. For each K in {1024,100000,1000000,3000000,10000000,10000000000},
put t=r^2/(1+r^2), v=1-t and phi=r v^2 t^K sin(theta). Define

    I=int F phi, F=(cX+U_R).grad R-R,
    M=(2c+1)phi+(cX+U_R).grad phi,
    C=||phi grad R||2, D=||M||2+C, Hbar=2/K^2.

The computation checks Hbar>||grad phi||infinity and therefore proves
for each accepted record

    ||h||2 >= 2|I|/(D+sqrt(D^2+4 Hbar |I|)).            (1)

All quantities in this note refer to whole-plane Lebesgue norms and
full-circle angular integrals. The scalar records remain OPEN until
compared with the independent Cartesian construction. A strict floor
is claimed only when verified with outward arithmetic.

The matched numerical-model envelopes are

    Benv=||v^2 t^K [1+2Kv+4t] |U_R|||2,
    Cenv=||r v^2 t^K |grad R|||2,
    A=||(2c+1)phi+cX.grad phi||2.

They satisfy ||M||2<=A+Benv and C<=Cenv. The comparison against the
frozen numerical model uses Benv and Cenv themselves. Neither an
estimate for a different denominator nor a finite-radius quadrature
can replace this comparison.

## Weak proof and endpoints

Subtract the stationary equations and test with phi times a smooth
compact cutoff. Divergence-free transport and integration by parts give

    I=int h M-int phi U[h].grad R+int h U[h].grad phi.

The multiplier norm is at most one on L2. Every term converges by
Cauchy-Schwarz: phi=O(r^-3), grad phi=O(r^-4), and the reference growth
is O(r^gamma), gamma<1. Escaping-annulus L2 norms tend to zero, which
also removes the cutoff errors. The origin is smooth since phi equals
y(r^2)^K/(1+r^2)^(K+2). Consequently |I|<=D||h||2+Hbar||h||2^2 and(1)
follows. Integration by parts in the reference equation gives the
separate identity I=-int R M. All-c extensions require the separately
audited common-leading-tail chart, not just these L2 hypotheses.

## Independent polar fields

Use the already audited exact polar constructor

    R=r sum v^a_j R_jn(t) sin(n theta),
    psi=r^2 sum v^a_j S_jm(t) sin(m theta),
    a_j=(j+1)delta/2, U_R=grad-perp psi.

Write D_d P=(d-2a_j t)P+2tv P'. Then

    R_r=sum v^a_j D_1 R_jn sin(n theta),
    R_theta/r=sum v^a_j n R_jn cos(n theta),
    U_r=-r sum v^a_j m S_jm cos(m theta),
    U_theta=r sum v^a_j D_2 S_jm sin(m theta).

For g=(2K+1)-(2K+4)t, grad phi has polar amplitudes v^2t^K g and
v^2t^K. Exact sine and cosine product identities give every harmonic
of M. No background mode is discarded. Squaring within each frequency
and retaining every cross term gives ||M||2^2. For C^2, directly
integrate sin(theta)^2 times the squared polar gradient of R. Its exact
angular multipliers for indices n,m are

    ac=2[n=m]-[|n-m|=2]+[n+m=2],
    bc=2[n=m]-[|n-m|=2]-[n+m=2],

with overall angular factor pi/4. Thus radial-derivative products use
ac and n m R_n R_m products use bc. This is independent of the peer's
Cartesian field squaring.

For Benv and Cenv, polar orthogonality gives, with all matching angular
indices retained, the product polynomials

    m^2 S_jm S_km+(D_2 S_jm)(D_2 S_km),
    n^2 R_jn R_kn+(D_1 R_jn)(D_1 R_kn),

respectively. Multiply the first by [5+(2K-4)v]^2. In both cases the
radial measure is (pi/2)t^(2K+1)v^(1+(j+k+2)delta/2)dt. Nonzero polar
modes have angular integral pi; there is no constant polar mode here.
This directly proves the matched envelope formulas without importing
the peer's Cartesian transformation. The linear A is integrated from
the exact polynomial (2c+1)+cg in the same measure with exponent1.

## Finite radial integration at very large K

Every integral is a finite sum of moments

    int_0^1 t^(L+1)(1-t)^b P(t)dt, b>-1.

Start with B(L+2,b+1)=Gamma(L+2)Gamma(b+1)/Gamma(L+b+3). The moment of
t^(j+1) is the moment of t^j multiplied by
(L+j+2)/(L+j+b+3). All factors have exact positive parameters. Arb
Gamma and arithmetic give enclosing intervals. This uses K only as a
scalar parameter; no array of length K and no expansion of t^K is
formed. Check every complete positive energy has over150 relative bits.

The independent reference pairing is recomputed as -int R M and is
compared with both peer formulas and this lane's already audited exact
radial-adjoint full-residual pairing at each K. That latter proof and
result are hashed as dependencies. Agreement alone is not used to
assert a uniform asymptotic remainder or a global maximum over K.

## Exact gradient bound for the finite list

At fixed radius, maximize over theta to obtain the larger of
v^2(1-v)^K and |v^2(1-v)^K[-3+(2K+4)v]|. The angular amplitude has its
only positive critical point v=2/(K+2). The radial derivative after
removing v(1-v)^(K-1) is

    -6+(9K+18)v-(2K+4)(K+3)v^2.

Its discriminant is3(K+2)(11K+6). Check the polynomial identity exactly,
enclose both roots in(0,1), and evaluate all three amplitudes outward.
Both endpoints vanish. Their strict comparison with2/K^2 is a complete
maximum certificate for each listed K, not a sampled bound.

## Frozen model comparison and scope

For every available matching N1 row, regard the stored binary64 estimate
as its exact rational value. Compute its ratio to Benv or Cenv and its
absolute relative error, then compare with the independent peer record.
A ratio strictly below one disproves use of that particular stored
estimate as an upper bound for the corresponding whole-plane norm.
This does not disprove a correctly enlarged envelope or a proved
asymptotic rate. All computations are local, one worker, with no formal
build, server, JavaScript or remote compute. Exact coefficients remain
in JSON inputs; the proof precedes the numerical application.
