# Two constant axis ratios: independent physical-coordinate reduction

## Status, statement and hypotheses

The informal reduction was written before the symbolic code. The independent physical-coordinate derivation, both exact charts and the integer elimination certificate are complete. The restricted theorem below is CONFIRMED. The lead's z442 calculations supplied untrusted comparison data, whose needed identities were independently proved. No B2 endpoint follows.

Fix beta>2. Let W, Theta, Omega be smooth on R^2, with W_1 and Omega odd in x and W_2 and Theta even in x. Assume W(0)=0, div W=2 beta, Omega=partial_y W_1-partial_x W_2, and

    W.grad Theta=(beta-2)Theta,    W.grad Omega+Omega=Theta_x.

Assume Theta(0,y)=0, Theta(x,y)=a0 x^2+O(|(x,y)|^3) at0 with a0 nonzero, and W(X)=beta X+o(|X|) uniformly at infinity. Put H(y)=Theta_xx(0,y), phi(y)=W_2(0,y), and let J be the component of {H!=0} containing0. Define I_2=Theta_xxxx(0,y)/H(y)^2 and I_3=partial_x^6 Theta(0,y)/H(y)^3 on J.

Theorem: I_2 and I_3 cannot both be constant on J. No bounds on higher velocity derivatives at infinity or on the ends of J are assumed. Profiles with varying ratios remain unexcluded.

## 1. Axis identities and normalization

Set A0=H(0), alpha=(beta-2)/2, L=(3 beta+2)/2, a=(A0/H)^(1/2)>0 on J, and A(y)=integral_0^y a(s)ds. Then a(0)=1. Divergence gives w=W_1x(0,y)=2 beta-phi'. The x^2 temperature coefficient is phi H'+2wH=(beta-2)H. It implies (a phi)'=La, so

    phi=LA/a,    phi'(0)=L,    w(0)=alpha.

The first vorticity coefficient b=Omega_x(0,y) satisfies

    phi b'+(1+w)b=H,    b(0)=2A0/beta.

Every point of J tends backward under the scalar axis flow to0: phi has the sign of y, has no intervening zero, and equals Ly+O(y^2) near0. If A0>0, then H>0. The integrating-factor formula, starting from a sufficiently small nonzero point where b>0, proves b>0 everywhere on J.

For every real lambda!=0, W^lambda(X)=W(lambda X)/lambda, Theta^lambda(X)=Theta(lambda X)/lambda and Omega^lambda(X)=Omega(lambda X) preserve all the hypotheses, by the chain rule. In particular a^lambda(y)=a(lambda y), A0^lambda=lambda A0, and r_n^lambda=lambda^n r_n for r_n=a^(n)(0)/n!. The constants B0,D0,c2 below scale as lambda^3 B0, lambda^5 D0, lambda c2. Constancy of I_2,I_3 and the conditions B0=0,c2=0 are preserved. Taking lambda=-1 can arrange A0>0 for the closing sign argument, without preserving an intermediate chart normalization.

## 2. Independent derivation in physical x

Assume I_2,I_3 constant. Taylor expansion with smooth divisible remainders, locally on every compact part of J, gives

    Theta=H x^2/2+B x^4/4+D x^6/6+O(x^8),
    H=A0/a^2, B=B0/a^4, D=D0/a^6,
    B0=I_2 A0^2/6, D0=I_3 A0^3/120.

Write W_2=phi+p x^2+q x^4+O(x^6). Divergence and parity imply

    W_1=w x-p' x^3/3-q' x^5/5+O(x^7).

The x^4 temperature coefficient is

    wB-p'H/3+phi B'/4+pH'/2=(beta-2)B/4.

Since w-phi a'/a=alpha, this gives (a^3 p)'=d2 a, with d2=3 alpha B0/(2A0). Thus p=(c2+d2 A)/a^3. The x^6 coefficient is

    wD-p'B/3-q'H/5+phi D'/6+pB'/4+qH'/2=(beta-2)D/6.

Using the preceding identity gives (a^5 q)'=d4 a, where d4=10 alpha D0/(3A0)-5 alpha B0^2/(2A0^2), hence q=(c4+d4 A)/a^5. Here c2=p(0), c4=q(0). These are finite jet consequences, not a separable ansatz off the axis.

The curl identity gives Omega=b x+e x^3+O(x^5), with b=-phi''-2p and e=-p''/3-4q. The x and x^3 vorticity coefficients give the exact ODEs

    R1=phi b'+(1+w)b-A0/a^2=0,
    R3=phi e'+(1+3w)e-p'b/3+p b'-B0/a^4=0.          (N)

These physical-coordinate formulas are the independent starting point for this lane's code. The lead's transformed coefficients should equal a^2 R1 and a^4 R3; that comparison is a control, not a premise.

## 3. Finite compatibility and exact certificate

Use Taylor jets a=sum r_n y^n, r0=1, and A=sum r_n y^(n+1)/(n+1). The exactly verified coefficient of r_(n+1) in the y^n equation of 4A0 a^5 R1 is A0 lambda(n+1), where

    lambda(m)=(3 beta+2)m^2((3 beta+2)m-2 beta-2)>0.

The physical-equation and principal-weight checks verify this identity for general m; the two finite chart calculations also check each multiplier directly. The degree0 identity, obtained directly at0 in(N), is

    A0=beta((3 beta+2)r1-4c2)/4.                   (Y0)

It partitions the problem into two charts after legitimate scaling:

    chart0: r1=0, c2=-1, A0=beta;
    chart1: r1=1, c2=t, A0=beta(3 beta+2-4t)/4!=0.

Eliminate r2,...,r9 with the y^1,...,y^8 equations of R1, then c4,D0 with the y^0,y^1 equations of R3. Every divisor must be registered and shown nonzero for beta>2,A0!=0. The remaining y^2,...,y^6 equations of R3 are polynomial compatibility conditions after these divisions.

(C): those conditions imply B0=0 in chart0 and t=0,B0=0 in chart1. The certificate below links every needed polynomial to(N), registers all divisors and exceptional parameters, and proves the resultant identities and coprimality over the integers. Agreement at a few exponents would not prove(C).

For modular verification, if P,Q are integer polynomials in t,beta of degrees m,n in t, their Sylvester determinant has beta degree at most n deg_beta(P)+m deg_beta(Q). Every integer coefficient is bounded by B=||P||_1^n||Q||_1^m, where the norms sum absolute coefficients in both variables. Expand the determinant, use the coefficient l1 product inequality, and bound the sum over permutations by the product of row sums. Each of the n P rows contributes ||P||_1 and each of the m Q rows contributes ||Q||_1. Equality at more points than the degree bound proves polynomial equality modulo that prime. Distinct primes with product exceeding the sum of the coefficient bounds for the true and claimed determinant then prove exact equality. Fixed formal Sylvester dimensions must be kept where leading coefficients vanish at an evaluation point.

## 3a. Completed elimination certificate

Set u=B0. Each reduced polynomial and every removed factor is recorded in exact sparse rational JSON, generated from(N), in verification/chart0_reduced.json and chart1_reduced.json. The associated denominator and factor certificates give exact factorizations. Every removed beta factor is proved nonzero for beta>2 by expanding at beta=2+z and checking that all coefficients have one sign, with at least one nonzero coefficient. The other removed factor is 3beta+2-4t, excluded by A0!=0. No branch u=0 or t=0 is discarded without being retained separately.

In chart0, each reduced equation contains u exactly once. For u!=0 divide by u and call the resulting equations F2,...,F6. The first is linear in u, and its coefficient pair has constant gcd in Q[beta], so it cannot vanish identically at a parameter. Exact resultants Res_u(F2,F3), Res_u(F2,F4) have gcd, up to a nonzero constant,

    beta2 (3beta-4)(3beta+2)2(5beta+3)(13beta+8).

This never vanishes for beta>2, so the equations have no common u in that range. Hence u=0.

In chart1, the reduced equations are F2,...,F6. For j=3,4,5 take Res_u(F2,Fj), factor exactly and retain the positive-degree-in-t factors Gj after removing only nonzero beta factors and the factors t and 3beta+2-4t. The branch t=0 remains separate. Their (t,beta) bidegrees are (10,37),(12,42),(15,54). If t!=0 and all original equations vanish, then G3=G4=G5=0. The two resultants R34=Res_t(G3,G4) and R35=Res_t(G3,G5) must therefore both vanish at beta. Exact integer identities and a maximal-gcd certificate give degrees744 and945, and gcd, up to a nonzero constant,

    beta (216beta3+677beta2+420beta+64)
    (5beta+3)4(3beta-1)6(13beta+8)9(7beta+4)12
    (3beta-4)17(beta-2)21(2beta+1)42(3beta+2)104.

Its degree is219, and every displayed factor is nonzero for beta>2. Thus t=0. At t=0, factor the first three equations, retain the u=0 branch, and eliminate u!=0 as in chart0. The exact resultant gcd is, up to a nonzero constant,

    beta2(beta-2)2(2beta+1)2(3beta-1)(3beta+2)4(7beta+4),

which again has no root above2. This proves u=0 and completes(C).

Here the exponents printed immediately after parentheses or variable names are ordinary nonnegative integer powers. The sparse JSON, rather than this typography, is the exact certificate input. The three small gcd checks use exact polynomial division. For the large gcd, exact division gives quotient degrees525 and726; their reductions modulo2147483647 preserve leading degrees and are coprime. Any nonconstant rational common divisor would survive at such a good prime, so the integer gcd is maximal over Q.

The large resultant arrays were imported as untrusted integer claims. This lane proved their equality with the resultants of its own Gj using the coefficient bound in section3 and direct finite-field polynomial resultants. At the distinct nodes100003+17k, k=0,...,D, it checked D+1 values per prime:865 points for D=864 and1096 for D=1095. The products of47 and61 distinct proved primes respectively exceed the sum of the true determinant coefficient bound and the maximum absolute claimed coefficient. Consequently both identities hold in Z[beta], not merely at sampled real exponents. The two modulus bit lengths are2867 and3721; the corresponding bound bit lengths are2867 and3687, and the exact strict inequalities are saved. The first finite-field prime is below2^61-1000033. No CRT reconstruction or interpolation is used in this independent verification. Formal Sylvester determinants are used if either leading coefficient drops; manufactured tests exercise that case, though no such drop occurred at these certificate nodes.

The certificate is computer-assisted exact algebra; it relies on the implemented integer arithmetic and determinant/polynomial routines. It is not a Lean formalization. Reproduction commands, code hashes, exact inputs, failures and their narrow implementation repairs are retained in verification/SUMMARY.md and build_inputs.json.

## 4. Global contradiction

If B0=c2=0, normalize A0>0. Then p=0 and b=-phi''. Section1 gives b>0, so phi is strictly concave. For y<0 in J, phi(y)<Ly<0. A finite left endpoint of J must be a zero of phi: if phi were nonzero there, the smooth linear ODE phi H'=[2phi'-(3beta+2)]H would continue the nonzero H through it. This contradicts that a finite component endpoint is a zero of H. Such a finite zero of phi is inconsistent with phi(y)<Ly. At an infinite left endpoint, division by y<0 gives phi(y)/y>L>beta, contrary to sublinearity. Thus B0=c2=0 is impossible, excluding chart1 under(C).

In chart0, (C) gives B0=0,r1=0,A0+beta c2=0. The constant a=1,A=y solves R1. The same triangular coefficient lambda(m), nonzero for m>=2, inductively makes every derivative of a-1 at0 vanish. This is smooth Taylor induction, not analyticity.

For uniqueness set Z=(a,ya',y^2 a'',A/y), Z*=(1,0,0,1). A/y extends smoothly as integral_0^1 a(sy)ds; Z-Z* is flat. After the stated nonzero multiplications, the equation yR1 can be expressed as yZ'=F(y,Z), with F smooth near(0,Z*) and F(y,Z*)=0. The nonvanishing leading coefficient and polynomial weight identities needed here are included among the required exact algebraic controls. The mean-value formula gives yE'=M(y)E for E=Z-Z*, with M bounded. Gronwall from y to y1>0 gives |E(y1)|<=(y1/y)^K|E(y)|, which contradicts flatness if E(y1)!=0. The same argument with y replaced by -y works on the left. Thus a=1 near0.

On J away from0, A has the sign of y and a>0. The a''' coefficient in R1 is nonzero, so ordinary uniqueness for the regular system in(A,a,a',a'') continues a=1,A=y across each half of J. A finite endpoint would then have H=A0!=0 by continuity, impossible. Hence J=R, but phi=Ly contradicts phi(y)/y tending to beta. This excludes chart0 and completes the theorem.

## Dependencies and scope

Only finite smooth Taylor expansion, integrating factors, the mean-value formula, Gronwall, and ordinary ODE uniqueness are used outside the finite algebraic certificate. All uses of sublinearity are explicit. No integration by parts at infinity, real analyticity, or off-axis separability is assumed. The full-plane inverse is not needed for this necessary condition because the stated divergence and curl identities suffice. Formal proof assistant execution is prohibited and is not used. Exact polynomial inputs and certificates must be stored with provenance as JSON in verification/. The full B2 existence problem remains OPEN despite this restricted theorem.
