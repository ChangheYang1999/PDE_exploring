# Real noninteger configurations of the degree-23 node equations

Written 2026-10-21T22:51:43.807256+00:00 before implementation and candidate arithmetic. Status: OPEN until all exact gates below pass. This is an existence statement for a finite auxiliary node system, not for the full-plane IPM equation or a finite polynomial profile.

## Exact statement and input convention

There are two proposed configurations. The first has A0=1, multiplicities (3,3,1,1,1,1,1), e=6 and eta in (25,26). The second has A0=1, multiplicities (2,2,1,1,1,1,1,1,1), e=8 and eta in (25,26). In both, put Aj=2 mu_j, T=eta-23 and n=(eta-23)/2. The claim is that distinct complex nodes x_j, closed under conjugation with their weights and avoiding 0, eta-1 and eta, exist and satisfy

    (eta-1)^l + sum Aj x_j^l = 0  (1<=l<=e),
    sum 1/(eta-x_j) = 0,
    sum Aj/(eta-x_j) = -T/eta.

Thus 1<n<3/2 and n is not an integer. The nodes are the roots of two monic real polynomials p and q of degrees (2,5) or (2,7), with weights (6,2) or (4,2). The claimed theorem uses exact rational centers and radii in the producer's JSON files, imported through the frozen source manifest of research/degree23_grouped_moment_obstruction. The verifier recomputes its own rational class polynomials, Jacobian inverse and interval bounds. The producer's claimed inclusion margins, inverse Jacobian and root bounds are not accepted as premises.

The algebraic reduction is the two-class construction proved in the sibling degree23 PROOF.md and independently implemented in independent_code/degree23_algebra.py. All relevant coefficient, solved-moment and logarithmic identities are rechecked for these two configurations. The unknown pair sum is s, called x in that module; the other unknown is eta. If m=e-1 is the degree of q, the remaining two equations F1=F2=0 are the primitive numerator polynomials of moments m and m+1. Reconstruction denominators are nonzero integer multiples of powers of T. Since eta lies in (25,26), T>2, so zeros of these numerators imply the moments themselves vanish.

## Rational interval conventions

A real interval [a,b] has exact rational endpoints. Addition, subtraction, multiplication and division use outward-containing rational formulas; division is permitted only if 0 is outside the denominator interval. Integer powers are computed by products, with exponent0 equal to1. Polynomial evaluation uses nested Horner arithmetic, so every evaluated interval contains the value at every point of its parameter box. No floating point value is used in an inequality establishing the theorem.

A complex rectangle is a pair of real intervals. Its arithmetic is induced by (a+ib)(c+id)=(ac-bd)+i(ad+bc). The sum of the maximum absolute values of its real and imaginary parts bounds the complex modulus above. The larger of the minimum absolute values of those intervals bounds the modulus below. These are deliberately simple rational bounds; a square root is unnecessary. Check their implementations against explicit manufactured intervals before candidate evaluation.

## Existence of a real zero of the residual equations

Let z0=(s0,eta0) be the two exact rational coordinates read from the input, and let X=z0+[-r,r]^2 with r=10^(-80). Recompute the exact 2 by 2 Jacobian J0=DF(z0), check det J0 is nonzero, and put Y=J0^(-1), calculated by the elementary rational formula. Evaluate an interval matrix J(X) enclosing DF on X and E=I-Y J(X). Let q be the maximum of the two row sums of absolute upper bounds for E. Let b=Y F(z0), evaluated exactly.

If q<1 and |b_i|+q r<r for i=1,2, the map G(z)=z-Y F(z) maps X strictly into itself: the mean value formula on the convex box gives |G(z)-z0|_infinity <= max_i |b_i|+q r. The same derivative bound makes G a contraction with constant q. The complete metric space X therefore contains a unique fixed point z*. Since Y is invertible, F(z*)=0. The Jacobian interval enclosure and contraction inequalities are exact rational calculations. They give existence and uniqueness within X; no global uniqueness is claimed. Exact endpoint comparisons establish X_eta subset (25,26) and hence 1<n<3/2.

A check using the scalar q is slightly stronger than separate row constants. The calculation records its own q, displacement bounds and positive margins, even when they differ from the producer's published bounds. An input Newton approximation alone is not an existence proof.

## Uniform root disks and the node hypotheses

Evaluate every coefficient of p and q as an interval over X. For each proposed root center c in Q+iQ and rational radius R=10^(-65), expand p(c+w) or q(c+w) as sum a_k w^k by polynomial arithmetic, with interval complex coefficients enclosing all parameters in X. Let U_k bound |a_k| above and let L1 bound |a_1| below. Verify

    U_0 + sum_(k=2)^d U_k R^k < L1 R.

For every parameter in X and |w|=R, the right side is at most |a_1 w| and the left side bounds the modulus of the remaining terms. Rouche's theorem therefore gives exactly one zero, counted with multiplicity, in the disk |z-c|<R. The zero is simple. This conclusion is uniform over X, in particular at the real fixed point z*.

Verify that the number of disks assigned to each weight equals the corresponding polynomial degree, and that every pair of disks is disjoint. A sufficient exact check is max(|Re(c_i-c_j)|,|Im(c_i-c_j)|)>R_i+R_j. Thus these disks contain all roots of each polynomial and no two nodes coincide, even across the two polynomials. Check that every disk avoids 0 and all points of the real intervals X_eta and X_eta-1, using the same coordinate lower bound. Finally check that the disk family with its weights is invariant under complex conjugation. Real coefficients and uniqueness in each disk then make the full node multiset invariant under conjugation.

The solved moments and logarithmic identities from the independently reconstructed polynomials, together with F(z*)=0 and exclusion of eta from every disk, imply exactly the node equations stated above. The weights and distinctness are checked, not inferred from a numerical root finder.

## Optional rational-function identity

For v_j=x_j/(eta-1), put u_j=1/v_j-1. The forbidden nodes ensure u_j is neither0 nor-1 nor-1/eta. Define phi(u)=A0/u+sum Aj/(u-u_j). It has denominator D(u)=u product(u-u_j), degree e+2, and numerator degree e+1 with leading coefficient A0+sum Aj=23.

At u=-1, its k-th Taylor coefficient is minus [A0+sum Aj v_j^(k+1)], for 0<=k<=e-1, so the moment identities give a zero of order at least e. At u*=-1/eta, direct substitution and sum Aj/(eta-x_j)=-T/eta give phi(u*)=0: sum Aj x_j/(eta-x_j)=eta sum Aj/(eta-x_j)-sum Aj=-T-(23-A0)=-A0(eta-1), and substitution cancels the pole A0/u*. These e+1 zeros, with u* different from-1, determine the numerator. Hence

    phi(u)=23 (u+1)^e (u+1/eta) / [u product(u-u_j)].

This identity is a consequence of the proved finite equations. It does not require n to be an integer and does not produce a finite polynomial profile when n is noninteger. A symbolic sign check of the substitutions is included in the manufactured tests.

## Evidence and scope

The final gate must bind input bytes, all verifier modules, proofs, exact assertions and actual model-review responses. All 16 disks and both contraction tests must pass, as must every reconstruction identity and forbidden-node check. If a gate fails or is unexecuted, the corresponding existence claim stays OPEN. Successful arithmetic establishes two counterexamples to the stronger real-n exclusion, but leaves the integer-n exclusion and the principal full-plane IPM problem unchanged.
