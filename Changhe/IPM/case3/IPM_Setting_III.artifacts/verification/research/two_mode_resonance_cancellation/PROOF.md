# Two-mode cancellation of the first resonant source

Verifier result 158. Informal proof written 2026-10-21 before the exact coefficient and root checks. Numerical root locations supplied by the lead are hypotheses to check, not evidence for the conclusions below.

## Statement, notation and scope

For ell=3 let K=5, M=2; for ell=5/2 let K=9, M=4. Write p=1/ell, delta=1-p, and s_k=p-k delta. For Theta_e(theta)=sin(theta)+e sin(3theta), define density coefficients P_k, particular stream coefficients H_k, and the resonant source g(e) by the recurrence below. These are finite algebraic definitions over Q[e]. The exact calculation below certifies that g has two distinct positive real roots in (0,1) when ell=3 and four when ell=5/2. Exact rational isolating brackets are below; complete polynomial coefficients are in the accompanying exact JSON. Each root gives a smooth trace positive in the upper half-plane whose first resonant source coefficient vanishes.

This is a statement about a functional of a trace. It constructs neither an actual exterior solution with that trace nor a full-plane profile. For an exact profile with the prescribed trace, previous finite-depth expansion and radial-sector isolation identify g as the first resonant source. Vanishing of this coefficient removes that particular first obstruction. It asserts neither absence of later logarithms nor existence of a wholly log-free expansion. Setting III remains OPEN.

## Finite recurrence and its interpretation

Put P_0=Theta_e. For each i<K, form the source of r^(s_i)P_i by applying

    D_s sin(n theta) = (s-n)/2 sin((n+1)theta)
                         + (s+n)/2 sin((n-1)theta).

Use sin(-n theta)=-sin(n theta) and sin(0)=0. If G_i=D_(s_i)P_i, define (H_i)_m=(G_i)_m/[m^2-(s_i+1)^2] for positive even m. All these denominators are nonzero for i<K in the two specified cases: the finite list of s_i+1 contains no nonzero even integer. The zero source mode is absent by parity even when s_i+1=0. The stream is r^(s_i+1)H_i.

For a stream term h_m sin(m theta) at index i and a density term a_n sin(n theta) at index j, the coefficient of U_i.grad rho_j at its common radial degree is

    h_m a_n/2 [((s_i+1)n-m s_j) sin((n+m)theta)
              -((s_i+1)n+m s_j) sin((n-m)theta)].

Denote this bilinear operation by B_ij. Define

    P_k = 1/(ell k delta) sum_(i+j=k-1) B_ij(H_i,P_j),
    g(e) = [sin(M theta)] D_(s_K)P_K.

The transport multiplier is ell s_k-1=-ell k delta, which accounts for the sign in this formula. Inductively P_k is homogeneous of degree k+1 in the input amplitudes, so g is a rational polynomial of degree at most K+1 in e. Computing every coefficient through degree K+1 entails no truncation error. The actual positive sine support is contained in n<=4k+3 for P_k and m<=4k+4 for its source, by induction from the initial highest frequency 3.

The earlier inverse and finite-depth expansion proofs show that for an actual exact profile this recurrence describes its induced sector. Harmonic streams first have density-deficit increments 4,6,8,... . At ell=3 the resonant deficit K delta=10/3 is below4. At ell=5/2 it is27/5, and subtracting the only possible harmonic increment4 leaves7/5, not an integer multiple of delta=3/5. Thus no harmonic contribution changes g in either case. This isolation uses radial deficits only, so the two-mode trace causes no change to the argument.

## Independent coefficient verification

One implementation uses the displayed positive real sine formulas. The other uses signed Laurent modes of exp(i theta), with rational coefficients after factoring out i. It derives Cartesian x and y differentiation by the homogeneous power rule and obtains advection from the two Cartesian derivative products. It uses Laurent convolution rather than the sine-product formula. Both implementations retain all e powers, compare every P_k, source and H_k, and verify the Cartesian Poisson equation. Their constant coefficient agrees with the independently verified pure-trace coefficient from result150. No lead or external-review code is imported or executed.

The exact full coefficient arrays, all intermediate coefficients, and rational root brackets are in verification/EXACT_CHECKS.json from the successful calculation. Equality of the two computations checks the finite arithmetic; the interpretation for profiles depends on the proved recurrence and isolation just given.

## Root certification

For a rational polynomial g, evaluation at rational endpoints is exact by Horner's rule. Opposite nonzero signs at the endpoints give a root by continuity. Disjoint brackets give distinct roots. To check the stated counts rather than merely existence, use the Sturm sequence g,g',-rem(g,g'),... over Q, normalizing each nonzero remainder only by a positive rational factor. Polynomial division verifies every recurrence. A nonzero last constant makes g square-free. At any real argument not a root of the sequence, let V be the number of sign changes, with zero entries omitted. Sturm's theorem gives V(a)-V(b) roots in (a,b) when g(a)g(b)!=0; the signs at infinity are obtained from the leading coefficient and degree. These exact data certify both isolation and total counts. The theorem follows by the usual sign-change argument: across a zero of an intermediate sequence member the two neighboring signs are opposite and total variation is unchanged; across a simple zero of g variation drops by one as the argument increases. No other changes occur.

For every root in (0,1),

    Theta_e = sin(theta)[1+e(3-4 sin(theta)^2)].

For 0<theta<pi its bracket is at least1-e>0. Thus the cancellation examples have a strictly positive upper-half trace and the required angular parities. Scaling by any nonzero A multiplies g by A^(K+1); the roots in the relative amplitude e remain the same.

## Dependencies and verdict

Dependencies: elementary homogeneous Fourier calculus; result150's recurrence and radial-sector isolation; result142's finite-depth expansion only for the conditional profile interpretation; elementary polynomial division, continuity and the Sturm argument above. No assumption that a formal expansion is realized is used. The finite polynomial/root claim is CONFIRMED by the exact gate recorded below. The primary endpoint remains OPEN.

## Completed exact certificate

The own dual-algebra calculation completed at 2026-10-21T06:00:27.584813Z with 2980 passing exact checks in 2.78 seconds. It retains the complete rational polynomials, their intermediate expansions, the Sturm sequences, all division identities and refined rational brackets in verification/EXACT_CHECKS.json. The degree is exactly6 for ell=3 and exactly10 for ell=5/2. No other real roots exist.

For ell=3, the isolating intervals are (7/25,29/100) and (16/25,13/20), with opposite polynomial signs at each pair of endpoints. The Sturm variations at minus infinity,0,1,plus infinity are4,4,2,2. The two intervals have variations4 to3 and3 to2. Refined brackets have width (1/100)2^(-40); their midpoints are approximately0.28066166273196813 and0.6463522898809378. The decimals are labels for exact rational isolations, not independent root certificates.

For ell=5/2, the isolating intervals are (13/200,67/1000), (27/250,11/100), (7/20,44/125), and (593/1000,119/200). The Sturm variations at minus infinity,0,1,plus infinity are7,7,3,3; across the four brackets they decrease successively7 to6,6 to5,5 to4,4 to3. Refined widths are (1/500)2^(-40). Approximate midpoint labels are0.06594721793947883,0.1093408009627101,0.3505637599344618,0.5942044254804741.

The Sturm chains terminate in nonzero constants, so all these roots are simple. The proof's positive-trace observation applies to every one of them. This refutes universal nonvanishing of the first resonant functional on smooth positive upper-half traces. It does not refute any existence or nonexistence statement for actual profiles.
