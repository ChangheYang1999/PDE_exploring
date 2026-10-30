# Exact reconstruction and norm audit of the scaled six-generator fixture

## Statement and exact input

Fix c=4076476460239181/2251799813685248, gamma=1/c and delta=1-gamma.
Put s=x^2+y^2, H_m=Re(x+i y)^(2m), p_j=(3+gamma-j delta)/2,
t_R=s/(R^2+s), and u_R=R^2/(R^2+s). For each row in the exact JSON
input define the potential term

    a H_m (1+s)^(p_j-m) t_R^w u_R^q P_N(2t_R-1).

The six rows(a,j,m,w,N,q,R) are
(3/7,1,2,0,2,4,25),(-2/5,0,3,0,1,4,25),
(5/11,2,1,0,1,4,25),(1/3,0,0,1,2,4,25),
(7/2,3,1,0,0,4,25),(-1/9,3,2,1,0,4,10).
Let chi be their sum, rho=-chi_xxy-chi_yyy,
u=(-chi_xyy,chi_xxy), and F=(c(x,y)+u).grad rho-rho.
All are smooth on the whole plane because every denominator is positive
and H_m is a polynomial. All terms have q=4, so the extra radial factor
is O(r^-8), with the corresponding differentiated decay. The norms

    G0=||F||_2, rF=||rF||_2, G1=||grad F||_2,
    P2=||(1+4r^2)^(2/5) D2F||_2

are finite. The Hessian norm counts F_xy twice. This result verifies
all exact Fourier-rational field components of F and its derivatives
of total order at most2, then independently encloses these four
whole-plane norms. The fixture is the same exact six-generator input
as the frozen N3 test. It is not candidate016 or017 and its verification
does not certify their complete norm records.

## Independent exact field construction

Use t=s/(1+s), v=1-t and the independently proved rational potential
representation in ../joint_scaled_factored_weak/PROOF.md. A derivative
of chi of total order d is

    sum_(j,n) v^(-p_j) r^(-d) A_(j,n)(t) trig(n theta),

with A rational and denominator factors1+99v or1+624v. Its Cartesian
recurrence comes directly from polar differentiation and is independent
of the N3 packed generator expansion. For d=3,...,6 the numerator of
every A is exactly divisible by t^ceil(d/2); verify this division in
Q[t]. Since p_j=2-(j+1)delta/2, the resulting rational field has the
packed degree e=d-3 form

    e even: r v^(e/2) sum v^(ell delta/2) B_(ell,n)(t) trig(n theta),
    e odd: v^((e-1)/2) sum v^(ell delta/2) B_(ell,n)(t) trig(n theta),
    ell=j+1, B=A/t^ceil(d/2).

This follows by substituting r^2=t/v; every leftover v power cancels.
It proves that the different packed conventions describe identical
physical fields, without testing them only at selected points.

Construct every derivative of rho and u through order3 from these
potential derivatives. For alpha=(a,b), |alpha|<=2, the product rule
and D^alpha(x_i partial_i rho)=x_i partial_i D^alpha rho+
alpha_i D^alpha rho give

 D^alpha F = c(x D^alpha rho_x+y D^alpha rho_y)
             +(c|alpha|-1)D^alpha rho
             +sum_(beta<=alpha) binom(alpha,beta)
                (D^beta u1 D^(alpha-beta)rho_x
                 +D^beta u2 D^(alpha-beta)rho_y).

Here binom(alpha,beta)=binom(a,beta_x)binom(b,beta_y). When multiplying
packed degrees e1,e2 with e1+e2=e+1 to obtain degree e, the radial
prefactors introduce an extra t exactly when both e1,e2 are even;
otherwise no extra factor is needed. This is checked by r^2=t/v.
Coordinates x,y have degree0 and ell0, with coefficients cos(theta)
and sin(theta). Elementary trigonometric product identities produce
all modes exactly, including the zero cosine and negative-frequency
signs. This construction differentiates the original physical formula
by Leibniz expansion; N3 instead assembles F and differentiates its
packed expression. Compare all coefficients after multiplying by
positive common denominators. Exact zero differences prove equality
for every r>0,theta, and continuity extends it to the origin.

As an additional independent check, the Cartesian Taylor-jet evaluator
constructs chi directly as a polynomial in coordinate increments through
order6. Extract its exact factorial-scaled derivatives and use the same
physical Leibniz identity. Outward ball comparisons at four named rational
points test F, its five first/second derivatives and the five base fields.
These finite point tests are supplementary to the complete exact equality.

## Whole-plane integration

For a packed degree e field, its radial prefactor squared times
r dr is (1/2)v^(e-3)t dt when e is even, and
(1/2)v^(e-3)dt when e is odd. Orthogonality contributes pi for every
positive sine or cosine square and2pi for cosine0. Sum all ordered
same-frequency pairs independently, with the binomial multiplicity
for the degree-e derivative tensor. Group the exact rational functions
by total branch exponent L=ell+ell'. Then every norm-square term is

    (pi/2) integral_0^1 v^(e-3+L delta/2+a)
       t^(epsilon+tp) W_L(t) dt,
    epsilon=1 for even e,0 for odd e.

The four choices(e,a,tp) are(0,0,0),(0,-1,1),(1,0,0),(2,-4/5,0).
For the final norm multiply the integrand by(1+3t)^(4/5), since
1+4r^2=(1+3t)/v. Strip any exact v factors from the complete rational
numerator and require the remaining endpoint exponent b>-1. The fixture
has sufficient decay for this condition; the checker must establish it
rather than assume it from a floating value. Denominators are positive.

Use our exact partial-fraction replay and fixed-b pole-order moment
recurrence from ../rational_pole_moments/PROOF.md. N3 uses its separate
base-exponent recurrence and accumulator, accepted on finite fixtures in
N4-302. Every actual integrated group in this fixture is retained in the
result with exponent, factor orders, complete decomposition replay and
accuracy. Thus the whole norm is bounded without radial truncation or
quadrature. Shared Arb arithmetic is disclosed.

For the P2 weight put z=(3t-3/2)/(5/2), so |z|<=3/5. Truncate the
binomial series of(1+z)^(4/5) after degree56. The magnitude ratio of
successive binomial coefficients after that degree is less than1;
hence the absolute remainder is bounded by the first omitted coefficient
magnitude times(3/5)^57/(1-3/5). Multiply this uniform bound by the
nonnegative unweighted squared integrand and integrate. The resulting
lower and upper square bounds enclose the exact weighted energy even
though individual branch groups may have either sign. Positive square
roots yield the norm enclosures. Compare containing square and norm
balls, never a rounded endpoint as if it contained the exact value.

## Dependencies and scope

The exact six-row JSON, frozen N3 modules accepted in N4-302, own
rational-field and Taylor-jet sources, proof, and every result are
bound by SHA256. Frozen peer modules are executed only from this lane.
No source is executed from a read-only foreign directory. All exact
polynomial identities, grouped integrals and scalar comparisons are
asserted. The informal argument precedes execution. No formal proof
assistant is used. The statement certifies this fixture and its finite
field identities; actual large candidate norm certificates remain a
separate audit.
