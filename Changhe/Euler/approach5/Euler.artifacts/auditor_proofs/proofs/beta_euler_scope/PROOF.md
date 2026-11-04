# Scope corrections for the Euler-coupled singular basin note

## Statement and dependencies

This audits in the team records against A095, A147, A155, A159, A278, A309 and the actual regularity hypotheses. Fix 0<c<1/2, a=1-2c, kappa=1+c, A=cI-omega J, B=Ay+U, Omega=curl U. Profiles are C2 where used. The main arbitrary-omega decaying-profile conjecture remains open.

At a vortical zero p, DB(p)Omega(p)=kappa Omega(p). Under A147's compact full-invariant set with Omega nowhere zero and an incoming regular orbit, or A159's nonsingleton backward limit with Omega nowhere zero, the other eigenvalues are real and have the form

    lambda_3<0<=lambda_2, lambda_2+lambda_3=-a.

These facts do not imply lambda_2<kappa and do not turn a zero eigenvalue into a stable eigenvalue. The stronger manifold wording of Z3, and Z2's unconditional description as two stable directions, require correction.

## 1. An exact affine test of the eigenvalue statements

Let omega be any nonzero real number, let s be real, and define

    S=diag(s,-1-s,1), G=S+omega J,
    U(y)=G y, Omega=2 omega e3,
    B(y)=diag(c+s,c-1-s,kappa)y.

U is divergence free. Since S Omega=Omega and J Omega=0, the exact affine compatibility condition from A095 holds. More directly, the matrix

    M=G+G^2+omega[J,G]

is symmetric. Indeed the only possible off-diagonal antisymmetric part is in the horizontal block, where the sum of S's horizontal entries is -1, giving cancellation between G and G^2; the remaining commutator contribution is symmetric. Thus

    P(y)=-y.M y/2

makes the full rotating momentum residual zero. This also follows by substituting B=Ay+Gy into that equation; its linear coefficient is exactly M.

If s>1, lambda_2=c+s>kappa and lambda_3=c-1-s<0. For Psi the horizontal first coordinate contracts faster than the vertical vortex direction. The vortex line is a stable line, but it is not the strongest stable line. If s=-c, lambda_2=0 and lambda_3=-a. The exact Psi-stable set of the origin is just the vertical line; a second horizontal direction is a center direction and does not converge. A two-dimensional center-stable plane exists in this example, but it is not the stable set.

These are exact local and global affine profiles, with no decay. They refute only the claimed inference from the listed first-order data. They are not counterexamples to the target conjecture or constructions of compact singular attractors.

For 0<lambda_2<kappa the usual hyperbolic stable-manifold statement supplies a two-dimensional stable manifold with Omega as its strongest stable direction. For lambda_2>0 without the strict ordering there is still a two-dimensional stable manifold, but its strongest direction need not be Omega. At lambda_2=0 only a center-stable manifold can be asserted from this spectrum. A separately chosen vortex-saturated center-stable construction would need its own proof.

## 2. Compact-set and network hypotheses must remain explicit

A147 assumes Omega nowhere zero on the entire compact full-invariant set. A159 assumes this on the entire nonsingleton backward limit, not just at one zero p. The definition of case(beta) in the note mentions a vortical zero and nonstationary orbits but does not itself restate that uniform vortical hypothesis. If this case is meant to exclude every vorticity zero on its limit, say so. Otherwise its invocation of A147/A159 is conditional, and the broader claim is open.

A155 excludes a nontrivial backward limit equal to a finite hyperbolic vortical heteroclinic network and proves nullness of the corresponding exceptional basins. It does not exclude a singleton equilibrium as a backward limit of points on its stable manifold. Retain 'nonsingleton' in Z4 or state the null-basin conclusion. A finite network with genuine connections is the intended nontrivial case.

## 3. What the helicity-free transfer actually proves

Assume explicitly the two additional properties in Section4 of BETA_EULER:

- up to a volume-null subset of the open basin V, each point lies on a complete vortex line through a regular point of the compact limiting set K;
- a periodic orbit gamma of carrier period L has weak stable trace dense in K.

Assume h=U.Omega=0 on V. Then Omega H=-a h gives constancy of H on each such vortex line. H is constant along every strong stable arc through gamma, with its value determined by phase on gamma. Therefore H composed with Psi_L equals H on its weak stable trace. Continuity and density give this equality on K. Commutation extends it along the vortex lines through K, and their full-volume coverage of V plus continuity gives it throughout V.

Differentiating this periodic identity along B proves the same carrier-periodicity for g=-B H/a. The audited given-basin mean-energy argument HF-per, A313, then makes H constant on V for a decaying profile in its stated c-range. This deduction does not use a regularity claim for the singular attractor beyond the two explicit properties.

There is no exclusion of a single constant-H basin here. To deduce U=0 by A309, its coverage and the hypotheses forcing constant H must hold on every essential basin. 'With coverage' alone does not transfer h=0 on one basin to the others. Likewise the source's assertion that the singular stable manifold is automatically the two-dimensional vortex sheet cannot be used to establish the first property in the zero-eigenvalue case.

## 4. Pressure periods

For a bracket pair with U=B-Ay and curl U=W on a genus-two trapping neighborhood, pressure existence is equivalent to vanishing of the two real cohomology periods of a U.flat-(B cross W).flat. This is A249's closed-form criterion. Replacing an arbitrary homology basis by two periodic orbits additionally requires that their classes span. For the explicitly marked B24 template the LR and RRL construction in the team records establishes this directly. No singular Livsic theorem is needed for that particular template, and no general periodic spanning theorem for all case(beta) sets is inferred.

## Audit conclusion

The local eigenvalue and circulation identities remain useful necessary conditions. The conditional helicity-free transfer gives H constant on the specified basin. The note's broader manifold and global-exclusion sentences do not follow as written. Neither the corrected local constraints nor the template pressure periods yield a nonexistence theorem for an unrestricted sign-changing singular basin.
