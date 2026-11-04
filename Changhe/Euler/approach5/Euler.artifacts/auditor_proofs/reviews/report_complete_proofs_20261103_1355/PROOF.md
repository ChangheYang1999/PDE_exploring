# Audit of the assembled complete-proof sections

Status: CONFIRMED at the mathematical scopes specified below. The immutable assembled report is the snapshot in the team records. This audit covers all of Sections2A,2B,2C and2D, not the appendices or the previously identified front-matter errors.

## 1. Exact baseline and coverage of the audit

Put Jx=(-x2,x1,0), A=cI-omega J, B=Ax+U and Omega=curl U. The equation is

    div U=0,
    (1-c)U+DU B+omega JU+grad P=0.

Here omega is an arbitrary finite real number. Regularity, c-range and decay are specified separately below. The four source sections contain476,661,1056 and1000 lines respectively. Every line of these four immutable sections was read in this pass. The current2C and2D changes were also compared with the previously completely audited A490 andA479 snapshots. There are1019 unchanged lines in2C and977 in2D. Those counts are provenance information, not substitutes for the fresh complete reading.

The external dynamical and harmonic-analysis theorems remain the identified dependencies in those sections. This pass checks their uses and the changes to the proof chain. It does not claim a new retrieval or verification of every cited textbook theorem number. The actual printed Ledrappier-Young statements used here were checked in A479/A481 and remain the same statements.

## 2. Energy and pressure statements

Section2A concerns bounded C1 profiles with C1 pressure and its explicitly stated bounded-tail hypothesis Hb. For0<c<1, the energy exponent is alpha=5-2/c. Its pressure normalization, annular flux estimates and energy conclusions are the previously confirmed A031,A040,A219,A229,A385 statements, now checked again in the assembled text. Uniform decay implies Hb. The c=2/5 conclusion is finite kinetic energy; in2/5<c<1/2 the energy law allows positive growth of order R^alpha and does not imply finite energy or U=0.

The pressure proof first represents its gradient by differentiated double Riesz kernels. The differentiated far kernel is integrable, and the remaining harmonic distribution is controlled by scaled tests. It does not use a false L-infinity bound for an undifferentiated Riesz transform. The arbitrary additive pressure constant is removed or canceled exactly where needed. The divergence calculation cancels the two rotation terms before deriving the Poisson equation.

The annular decomposition separates a local L2 singular-integral term, an inner contribution bounded by R^-3 E(R/2), and an outer term controlled by R times a weighted energy tail. Cauchy-Schwarz and the shell geometry give the stated flux bound. The differential energy identity is then integrated with the factor R^-alpha. Its finite bootstrap begins with the bounded-velocity R^3 bound; no improved decay is assumed in the first step. At c=2/5, the separate tail recurrence and Young inequality provide the stated endpoint. At supercritical c the normalized positive limit is compatible with infinite total energy.

The velocity and vorticity Lorentz corollaries retain their different exponent ranges. In particular the quoted vorticity statement has1<=q<infinity. The Biot-Savart argument removes the harmonic remainder using the global velocity hypothesis. The weak-profile theorem is cited with its original audited proof, not newly reproduced here. The bounded-background reduction identifies a constant velocity and a translated decaying remainder by its own harmonic-pressure and scaling argument. No new error was found in the assembled2A proof at these exact scopes.

## 3. Dynamical statements and their limits

Section2B assumes U in C2, P in C1, uniform sublinearity and0<c<1/2 unless an individual identity states a wider range. The carrier is complete because it has at most linear growth. Radial escape and backward trapping use B(x).x=c|x|^2+U(x).x, so the rotation contributes no radial term. Cauchy transport and the constant divergence give exact vorticity and covector identities for every omega.

The nullity proof for singleton backward limits uses a compact cover of the eligible saddle set and a local trapped graph of positive codimension. It does not take an uncountable union of pointwise null stable manifolds. The proof that an all-equilibrium backward limit is a point uses connectedness, rank reduction, an interval of equilibria, two local invariant surfaces and a finite-passage estimate. Its essential hypothesis is that the entire limit set consists of equilibria. The endpoint estimate controls center drift by the entry and exit normal coordinates, rather than by passage time.

The entropy proof in the smooth class uses one loop with nonzero circulation, exponential growth of its backward length, an explicit compactification, and the cited smooth volume-growth theorem. At fixed finite regularity it retains the stated derivative-growth loss. Its loss-free C2 alternative assumes vorticity nonvanishing on the whole core. Neither version silently removes its extra premise.

In the regular compact region, exact transport supplies a hyperbolic splitting. The vortex flow is complete by conjugating a uniform local vortex segment through the complete carrier flow. The proof never assumes a global vorticity bound. The construction of attracting regular sets uses this vortex shift and local unstable curves. Positive-measure survivors produce a local unstable interval first; accumulation of expanded intervals then supplies the full unstable leaf. The later countable-basin argument uses that completed step.

The Lorenz-type eigenvalue restriction concerns a nonsingleton backward limit set on which vorticity never vanishes. Its entrance lemma requires an actual orbit approaching the whole limit set. It does not apply to every compact invariant set. Regular attractors and singular kinematic models are not excluded by these results, and fields used in those models are not silently identified with curl U. No new error was found in2B at these scopes.

## 4. Smooth vortical coverage and the finite-regularity condition

Theorem C in2C is the following previously confirmed mathematical statement. If U is globally C-infinity, P is C1, U is uniformly sublinear and0<c<1/2, then almost every vortical point belongs to one of countably many positive-volume continuous-time basins. Their probabilities are compactly supported, invariant and ergodic for the whole backward carrier flow, give full mass to B!=0 and Omega!=0, have spectrum(1-2c,0,-1-c), entropy1-2c, and absolutely continuous full unstable conditionals. Their invariant open essential basin domains are pairwise disjoint and cover the vortical region modulo a null set. Supports may meet either zero set. Time-one ergodicity is not asserted.

The proof selects the derivative order before the iterate length and the small curve scale. The affine tree counts nonlarge outputs, not all small outputs. The distortion estimate compares endpoint parametrizations directly and does not multiply distortion constants over time. The hyperbolic-time count retains its exponentially small bad-set estimate after restricting to a positive-measure target. The original density subset is selected without changing the prior parameters.

For each finite selection window, the incoming curves have a positive length and minimum-speed bound. The relative-entropy estimate supplies joint absolute continuity on this noncollapsing class. For the increasing limit over windows, the curve marginal of each member is dominated by the limiting marginal; null sets for the latter reference measure are therefore null for every member and for their increasing limit. This is the repaired argument in the current text.

Original approximants keep both their depth-to-time equality and asymptotically full target fraction. The vorticity-zero stable-plaque lemma uses real-time transport, a full derivative conorm in tempered coordinates and the C2 carrier bound. The transverse intersection of an approximating carrier strip with such a zero plaque contradicts its vortical origin. The capture box uses a curve in the interior of a trapping ball. The countable test family includes the time-averaged tests needed for continuous-time genericity.

The measurable-kernel argument uses rho_s=mu_s+lambda_s and joint Radon-Nikodym densities. Applying the leaf-null hypothesis to the measurable set where the arclength density vanishes proves conditional absolute continuity without selecting singular supports. The entropy directions are assigned to the stated lower-bound theorem and Ruelle inequality; the converse Ledrappier-Young theorem is used only in its valid direction. Full-plaque positivity is supplied by its Corollaries6.1.4 and6.2, not inferred solely from positivity at regular points.

For a fixed integer r>=2, the theorem remains conditional on Gamma_E<r(1-2c) for every vortical component E, where Gamma_E is the maximal backward top exponent on the singular part of the component core. The maximum is attained only for a nonempty singular part; the empty value is minus infinity. A separate iterate and gap are permitted for each component. The countable union does not require a uniform gap. Unconditional C2 coverage remains OPEN. The current full2C text is confirmed at precisely its smooth and conditional finite-r scopes.

## 5. Helicity-sign rigidity

Let2/5<=c<1/2, omega arbitrary, U globally C2, P C1, and U decay uniformly. Assume the separately specified coverage package(CI) of2D. For each resulting essential basin domain D_nu, assume U.Omega has one sign, with the sign allowed to differ between domains. Then U=0. Global C-infinity supplies(CI) without a growth premise; fixed Cr supplies it under the2C componentwise growth condition. These are Theorems L-infinity and L, respectively.

The complete vortex flow has polynomial displacement exponent c/(1+c). Since3c/(1+c)<1, the volume of all integer iterates of a wandering subset grows too slowly to accommodate linearly many disjoint equal-volume copies. The same argument for positive and negative integer steps yields recurrence. A helicity sign makes the Bernoulli function monotone along vortex lines, and recurrence forces helicity to vanish throughout each such invariant open domain.

The pressure is normalized by the unique constant Pinf for which the reduced Bernoulli function H0=H-Pinf has vanishing large-ball quadratic mean. The2A energy bound E(R)<=C R^(5-2/c) gives the transported L2 estimate integral_Q |H0(Phi_t y)|^2 dy<=C_Q exp(-2(1-2c)t). It does not give pointwise decay on every orbit.

A full-arclength set of two-sided generic points on an unstable plaque generates a positive-volume box by carrier and vortex flow. Zero helicity makes H0 independent of the vortex coordinate. Forward carrier time averages on that box equal the invariant measure average. The transported estimate forces this average to vanish, hence H0 vanishes on the support, basin and essential domain. This uses genericity in both carrier time directions and bounded support values; it does not integrate by parts against a singular invariant measure.

Coverage then makes H0 zero throughout the vortical region. At its boundary the Lamb identity gives U=0. Extending U from the irrotational interior by zero gives a locally Lipschitz field with zero divergence and curl distributionally, even if the boundary has positive measure. Harmonic continuation eliminates this extension. Thus H0=0 globally and P-Pinf=|U|^2/2.

Finally test the pressure Poisson equation against chi_R sqrt(1+|x|^2). The stress main term is nonnegative and at least chi_R |U|^2/(1+|x|^2)^(3/2). The cutoff error is at most C R^-1 E(2R), which tends to zero because5-2/c<1. Thus U=0. Every pressure constant and boundary term in this chain is accounted for. No new error was found in the current full2D proof.

## 6. Uniqueness of covering basin families

Let O be measurable. Let F and G be two at most countable families of Borel probabilities for the same complete flow. Suppose every basin is a Borel subset of O with positive Lebesgue measure, and each family's basins cover O modulo a null set. Define a basin by convergence of all bounded continuous time averages.

Then F=G as sets of probabilities. Indeed, fix nu in F. Its positive-measure basin cannot be contained in the null complement of the union of the G basins. Choose x in its intersection with one G basin, say that of mu. All bounded continuous averages at x have both limits, so their integrals under nu and mu agree. Such tests determine Borel probabilities on Euclidean space, hence nu=mu. Reverse the roles of F and G. The maximal open essential domains also coincide because their definitions use only O and the basin of the probability.

This proves the family comparison left as a remark in2D point39. Both the smooth and sufficiently high finite-regularity coverage constructions satisfy the hypotheses, so either construction gives exactly the same family and domains for a fixed smooth profile. No uniqueness of a single physical probability is claimed.

## 7. Admissible cutoffs in the older strain criterion

The short2D reference to the older A312 criterion must be read with its source's admissible cutoff. The source was reread completely in this pass: rho is smooth and radial, equals one near a backward-trapping ball Q, is positive inside a larger ball and vanishes outside it. Put Y=-rho(cx+U), L=sup||sym DY||. For integer r>=3, (r-1)(1-2c)>3L is a sufficient coverage condition.

The actual cutoff carrier is omega Jx+Y. Its skew rotational derivative contributes zero to the quadratic tangent estimate, so ||DTheta_t||<=exp(L|t|). It agrees with the original backward carrier near Q. Thus the absence of an explicit omega term in L is justified. The source does not authorize an arbitrary radial function that fails to equal one near the trapping region. The newer componentwise growth theorem does not use this old criterion.

## 8. Verdict boundary and dependencies

The current four complete-proof sections are CONFIRMED at the stated scopes. This fresh complete reading does not cure the pressure-gauge, boundary-Z, clock or hypothesis wording errors recorded in A1209-A1216 elsewhere in the snapshot. It does not certify unread appendices, unchecked literature priority claims, or every summarized external theorem number. The unrestricted C2 decaying rotating-profile conjecture, with arbitrary helicity and arbitrary omega, remains OPEN.

The dependency record is the current four sections together with A219,A229,A385,A479,A490 and the individual proof verdicts identified there. The added family comparison in Section6 is proved here directly. No numerical computation, formal build, new agent or remote client was used.
