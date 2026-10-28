# Three diagonal lower bounds with a homogeneous tail

## Exact statement

Use the real homogeneous Euclidean Holder seminorm
[f]_a=sup_(x!=y)|f(x)-f(y)|/|x-y|^a on the plane, modulo constants,
with0<a<1. Define T_xx by the circular principal-value kernel
K(z)=(z_1^2-z_2^2)/(2 pi |z|^4), using convergent kernel differences
at infinity for inputs of growth |z|^a. Put R_1^2=T_xx-I/2 and let
D_a be its seminorm operator norm. Then

    D_(1/2) >= 2.4389659544,
    D_(3/4) >= 2.8866494385,
    D_(9/10) >= 5.2405340577.

These are rigorous lower bounds, not exact norms. They also apply to
the supremum over compact smooth real test functions, by the approximation
proved in the setup. They concern homogeneous seminorms only.

## Witnesses and admissibility

For the corresponding rows use

| a | b | c | lambda |
|---|---|---|---|
|1/2|3/4|-3/20|1000/1021|
|3/4|3/4|-3/10|50/53|
|9/10|7/20|-3/10|10/11|

Let Z0(b) and its sign sigma be the axis polygon and signs defined in
../../PROOF.md and its cited polygon construction. The poles are0,e1
and the midpoint is m=e1/2. For z=m+(X,Y), X>0, put

    h=2^(a-1)X^a,
    g=2^(a-1)sigma(z)dist(z,Z0(b))^a,
    P(u)=(|u|^a+sign(u_1^2-u_2^2)(|u_1^2-u_2^2|/|u|)^a)/2,
    f(z)=max(-h,min(h,g+c,-1/2+lambda P(z-e1))).

Set P(0)=0 and extend f oddly across X=0. The certified profile
bounds are[P]_(1/2)<=1021/1000,[P]_(3/4)<=53/50 and
[P]_(9/10)<=11/10. Hence lambda[P]_a<=1. The Holder lattice
lemma proves[f]_a<=1. Its pole values are f(e1)=-1/2 and
f(0)=1/2, so in fact[f]_a=1.

Let I=pv integral_(R^2)(K(z-e1)-K(z))f(z)dz. The equality of the
norms of T_xx-I/2 and T_xx+I/2, proved by a quarter rotation, gives
D_a>=max(|I+1/2|,|I-1/2|)=|I|+1/2. All these integrals use the
same subtraction at each pole as the operator definition.

## Finite region and tail

The repaired polar cell rules of ../../PROOF.md, repairs/PROOF.md
relative to that file, and refined_cells/PROOF.md give outward
enclosures N for the right pole disk and M for the remaining midpoint
region truncated at radius R. The left pole disk contributes N by
reflection. Each saved task covers whole angular circles or the
specified clipped midpoint cells. The independent auditor proves
exact radial coverage, no duplicated tasks and matching parameters.
Its own exact rational sums do not import the cell driver.

The omitted tiny disk at each pole has absolute error at most

    E0=eps^a/a+eps^2(1/2+eps^a)/(2(1-eps)^2).

The omitted midpoint sliver has absolute error at most

    Es=2^(a+3)eta^(a+3)/(pi(a+3)sqrt(1-eta^2)).

Here eps and eta are the exact rational mesh endpoints recorded in
each manifest. The coverage proof and these remainder estimates are
in the cited polar-certificate proof.

For the exterior use the complete theorem in ../PROOF.md. Its scalar
condition lambda(1+2^(-a))>=1 is checked by outward arithmetic for
each row. Thus the tail equals

    T=2 a3(a) R^(a-1)/(1-a)

up to the explicit error E(a,b,c,R) of that theorem. The independent
auditor evaluates a3 by100 terms of its positive series and adds the
proved geometric remainder. It uses320-bit ball arithmetic. Therefore

    I in 2N+M+T+[-Etotal,Etotal],
    Etotal=2E0+Es+E(a,b,c,R).

Exact rational endpoints are retained before rounding the lower bound
|I|+1/2 downward to ten decimal places. The intervals are positive,
so the lower endpoint plus1/2 gives the displayed bounds.

## Reproducible evidence and scope

| a | completed tasks | cell evaluations | exact R |
|---|---:|---:|---|
|1/2|376|3129164|5722367659350217/1000000000000|
|3/4|398|4299752|39448136298135637/10000000000000|
|9/10|406|5015234|5898816360862063/5000000000000|

The task counts refer to complete prefixes of the saved manifests.
No unfinished task contributes. The analytic tail replaces the entire
remaining exterior, so full completion of the original longer manifest
is unnecessary. Local source hashes are checked against every task.

Run code/audit_note14_prefix_tail.py from the artifacts root, with the
manifest directory, --task-count and --out recorded in each output.
The three exact sums and all task hashes are in
../verification/a50_prefix376, ../verification/a75_prefix398 and
../verification/a90_prefix406. The acceptance manifest binds these
outputs, the analytic proof and its independent cross-read. V132
confirms the three numerical bounds; V130 confirms the tail theorem.
