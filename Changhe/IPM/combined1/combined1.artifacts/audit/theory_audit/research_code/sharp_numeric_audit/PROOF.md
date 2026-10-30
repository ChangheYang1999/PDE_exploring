# Numerical consequences of the two sharpened L2 frameworks

## 1. Statement and inputs

For a smooth S1 reference rho on R2, let U=(-R1R2,R1^2), V=cX+U[rho] and F=V.grad rho-rho. The Riesz convention is symbol i xi_j/|xi|. Define J^s=(1-Delta)^(s/2), omega=(1+r^2)^(1/2), and

    E_w(g)^2=||omega D^2g||2^2+w1||Dg||2^2+w2||g||2^2,
    X_(s,w)(g)=E_w(J^s g).

The tensor norm includes every ordered Cartesian derivative, so ||D^2g||2^2 has Fourier weight |xi|^4. The two framework balls considered here are

    sharp:  s=1/7744, (w1,w2)=(2^14,2^18), R=147/200000,
             eta=76219/10^9;
    sharpw: s=1/5184, (w1,w2)=(2^15,2^20), R=1351/10^6,
             eta=4207/20000000.

The ball is X_(s,w)(h)<=R. The sufficient residual threshold in the separately audited conditional theorem is X_(s,w)(F)<=eta. No candidate existence follows from these definitions alone.

This audit computes two separate consequences. First, the already independently reconstructed point fields for candidates002,003,004 exclude each of these two correction balls. Second, the four independently confirmed raw norms of d2 give a lower and upper bound for X_(s,w)(F). Each assertion is numerical only after the exact input hashes and outward interval comparisons in the output have passed.

## 2. Pointwise necessary test

Because omega>=1, w1>=2 and w2>=1, the Fourier identity gives ||h||H^(2+s)<=X_(s,w)(h). With the Fourier inverse normalization (2pi)^-2 in two dimensions, Cauchy-Schwarz gives for real h

    ||h||infinity, ||U[h]||infinity <= C0 R,
    ||Dh||infinity <= C1 R,
    C0=[4pi(1+s)]^(-1/2), C1=[8pi s(1+s)]^(-1/2).

For the gradient bound, apply the scalar directional inequality to the direction of the gradient at the point; the angular integral of the squared directional frequency is half the full radial integral. The velocity multiplier has vector magnitude at most one, so the same scalar Sobolev bound applies. These constants and the corresponding S1 refinements were independently audited earlier; no S1 improvement is needed here.

The exact correction equation is

    F+V.grad h-h+U[h].grad rho+U[h].grad h=0.

At any point where the smooth background is evaluated, continuity of h and Dh implies

    |F|<=R[C1|V|+C0(1+|grad rho|)]+C0 C1 R^2.             (1)

Thus a strictly positive interval lower bound for the gap between the two sides rules out every correction in the closed ball. This is a necessary condition, so it does not use any sufficient inverse hypothesis. The source fields are T4's independent polar reconstructions checked against N4's Cartesian path. The postprocessor evaluates only the new rational parameter pairs; it does not substitute a numerical residual for an exact equation.

## 3. Raw-norm conversion for d2

Write P=||omega D^2F||2, G1=||DF||2, G0=||F||2, Q=||omega D^3F||2, and E=(P^2+w1 G1^2+w2 G0^2)^(1/2). The already audited fractional comparison from T4-042 gives, for 0<s<=2^-10,

    [(1-48s/25)^2 P^2+w1 G1^2+w2 G0^2]^(1/2)
        <=X_(s,w)(F)
        <=E^(1-s)[2Q^2+C_w E^2]^(s/2)+(48s/25)E,           (2)

where C_w=max(1+32/25+w1,1+w2/w1). Briefly, the upper bound follows by interpolating E(J^s F) between order0 and order1 and bounding the weight commutator by48s/25; the lower bound applies the inverse commutator estimate to the weighted Hessian, while J^s expands the unweighted L2 and gradient norms. The coefficient48/25 and the order1 bound defining C_w are proved in the separately audited T4-042 theorem, which is an explicit dependency here.

For the present weights C_w is409657/25 or819257/25. The factors in (2) increase in every nonnegative input P,G1,G0,Q. Therefore lower raw endpoints give the displayed lower bound and upper endpoints give the upper bound. The code evaluates noninteger powers in outward Arb arithmetic. It checks overlap with N4's independently computed conversion and divides the lower bound by the exact eta.

The raw G0,G1,P2,Q3 intervals are not newly proved by this postprocessing. Their cross-lane confirmations are dependencies recorded in the campaign ledgers. This audit verifies their assembled consequences. No Hdot^-1 component, pointwise norm, or unconfirmed optimization loss is used as a substitute for them.

## 4. Scope

All point exclusions are for the fixed exponent and exact candidate hashes named in the output. The d2 lower bounds rule out the sufficient residual tests for d2. They are not lower bounds for every conceivable candidate, and the upper bounds do not make d2 feasible. The analysis says nothing about a different affine reference or a different correction ball. No proof assistant is run.
