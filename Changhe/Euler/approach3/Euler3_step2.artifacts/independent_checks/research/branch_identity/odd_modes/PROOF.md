# Odd azimuthal content obstructs equality with an even field

Status: proved exact Hilbert-space statement. Applying it to a computed shell fraction requires an error bound to obtain a certified numerical lower bound. No such bound is supplied by empirical quadrature refinement.

## Spaces, action and statement

Fix 0<a<b<infinity and let S={y in R^3: a<|y|<b}. Let mu be normalized Lebesgue volume measure on S and let H=L2(S,mu;R^3), with the usual real inner product and norm. Let Q_gamma be rotation by gamma about the z-axis and define the active vector-field action

(T_gamma U)(y)=Q_gamma U(Q_{-gamma} y).

Equalities in H are almost everywhere. Set E=(I+T_pi)/2 and O=(I-T_pi)/2. Then H is the orthogonal direct sum of the ranges of E and O, E and O are orthogonal projections, and they commute with every T_gamma. For U,V in H with ||U||,||V||>0 and T_pi V=V, every real gamma satisfies

||T_gamma U-V||^2 = ||OU||^2 + ||T_gamma EU-V||^2,

d_gamma(U,V) := ||T_gamma U-V||/min(||U||,||V||)
               >= ||OU||/min(||U||,||V||) >= ||OU||/||U||.       (1)

The same lower bound holds for unit-normalized shape distance

||T_gamma U/||U|| - V/||V|||| >= ||OU||/||U||.                   (2)

Thus a positive odd fraction excludes equality, at every axial rotation, with any nonzero even field, regardless of amplitude. These statements apply separately on every shell, and their maximum gives a lower bound for the maximum-over-shells distance. They do not identify a new Euler branch or validate a solution.

## Proof

The substitution x=Q_{-gamma}y preserves S and mu, and Q_gamma preserves vector dot products. Therefore T_gamma is an isometry and T_gamma T_beta=T_{gamma+beta}. Since Q_{2pi}=I, T_pi^2=I. Its inverse and adjoint are T_pi, so it is self-adjoint. Expanding the products gives E^2=E, O^2=O, EO=OE=0 and E+O=I. Self-adjointness gives orthogonality of their ranges. The rotation group identity gives commutation with T_gamma and hence preservation of both ranges.

Decompose T_gamma U-V=T_gamma OU+(T_gamma EU-V). The first term is odd, and the second is even because V is even. Their inner product vanishes. Pythagoras and isometry prove the equality and (1). For (2), replace U,V by their individual unit normalizations, apply the same Pythagoras identity, and use linearity of O. Every denominator is positive by hypothesis.

## Relation to the saved potential coefficients

Let the saved potentials be smooth sums of radial functions times real solid harmonics r^ell Y_{ell m}(theta,phi), including radial-dependent angular phases. A shift phi -> phi-pi multiplies each real cosine or sine harmonic by (-1)^m. Radial functions and radial-dependent phases are unchanged by Q_pi. Define the toroidal-poloidal velocity by U=curl(y T)+curl curl(y S), with the same convention as the field reconstruction proof. Curl commutes with proper rotations: differentiating Q F(Q^{-1}y) by the chain rule and using invariance of the Levi-Civita tensor for det Q=1 gives curl(T_gamma F)=T_gamma(curl F). Multiplication of a scalar by y has the corresponding covariance. Consequently the velocity contribution of a potential mode m is an eigenfield of T_pi with eigenvalue (-1)^m. Keeping only odd m in all channels therefore equals OU; keeping even m equals EU. This uses the vector-field rotation action. Applying a scalar half-period test to individual Cartesian components without rotating the vectors is incorrect.

The coefficient-to-field map can have null directions. Odd coefficients alone do not prove OU is nonzero; its field norm must be evaluated or otherwise bounded. The proof does not infer parity from the optimizer's parameter vector length.

## Discrete implementation and scope

For positive quadrature weights with an even, uniformly spaced azimuthal grid, equal weights on half-turn pairs, and nonzero sampled norms, T_pi is represented exactly by pairing phi with phi-pi and multiplying vectors by diag(-1,-1,1). This finite-dimensional map is an orthogonal involution in exact arithmetic. All projection identities above hold for that half-turn action, even before a continuum error bound. For arbitrary rotations, isometry of sampled norms follows when the cylindrical components are finite Fourier sums with |m|<=M and the azimuthal count N_phi>2M: the equally spaced rule integrates every product frequency through 2M exactly. The positive polar and radial weights can then be arbitrary. Their approximation of the continuum integral remains a separate issue.

The independent numerical check uses the exact saved F-projected P3 FREE endpoint, three fresh spatial grids, and both the half-turn projection and independent Fourier reconstruction. It compares the field norm with and without rotation and compares half-turn projection with zeroing odd or even coefficients. Passing these numerical checks gives an empirical odd fraction on the specified shells, not a rigorous lower bound rounded upward. In particular a computed 0.206 may be described as about 21 per cent, but not as a certified lower bound of at least 0.21.

Dependencies: elementary rotations and change of variables, Hilbert-space projection algebra, the chain rule for curl covariance, and finite Fourier orthogonality. The finite potential representation and independent evaluator are documented in ../../field_reconstruction/PROOF.md and ../../represented_tail_decay/PROOF.md. No formal proof has been built.
