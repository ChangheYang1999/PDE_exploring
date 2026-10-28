# Closing check of the report's literature statements

## Statement and scope

Section 2 of the report frozen as version 38 (an earlier version of the report, not included) accurately classifies the primary statements listed below. The exact one-dimensional Hilbert constant is not a two-dimensional Riesz constant. The cited domain and Schauder results do not supply a numerical value for the whole-plane Euclidean homogeneous seminorm in this project.

This is a statement audit, not a new proof of every cited theorem. The files and the exact locations checked are bound by `verification/accepted.json`. The project inequalities depend on the independent proofs in the other topic folders.

## The exact one-dimensional results

Babenko's Theorem 1(2), in `conjugate_sharp_2014`, assumes a concave Dini modulus and states an exact maximal increment of the periodic conjugate function. Its kernel has the factor `-1/(2 pi)` multiplying the cotangent. The mass-matching relation gives the tangent identity used by the report. The article announces the proof's ingredients but does not contain the proof. The report says this explicitly. Its extension to angular and chordal Holder operator constants is supported separately by the project's direct proofs. No two-dimensional conclusion follows from this source.

Lemma 8 in `korneichuk_stechkin_2020` concerns bounded positive weights on two ordered finite intervals with equal mass. Decreasing mass matching bounds the difference of their weighted integrals by the modulus cost. Concavity gives scalar equality. The reversed endpoints in the second displayed cost integral are a typographical issue; the first integral and proof have the correct orientation. The report uses only the first expression, retains the bounded-weight hypothesis, and does not automatically extend this lemma to singular measures.

## Beurling and general singular-integral statements

The Main Lemma in `mov` uses a bounded domain with C^(1+epsilon) boundary and an even homogeneous convolution kernel with C^1 angular part and zero mean. Its Lip norm includes the supremum norm. The multiplier of the kernel's CZ norm is an unspecified function of dimension, exponent and domain. This is the scope stated in the report.

In `1604.07670`, Proposition 2 maps a Dini modulus to the sum of its near and far integrals. Substitution of t^alpha gives x^alpha/alpha+(x^alpha-x)/(1-alpha). Equality of that expression with the original modulus is not asserted. Theorem 3 is a boundedness theorem for the paper's regular Campanato moduli on C^(1,omega) domains, with no numerical norm. The report distinguishes the modulus transformation from an exact operator constant.

In `1201.5385`, Theorems 1.1 and 1.2 transfer Besov regularity of the boundary normal to Sobolev and Besov regularity of B chi_Omega. The fractional theorem requires 1<p<infinity, 0<alpha<1 and alpha p>1. Constants depend on the stated exponent and domain parameters. In `1201.5403`, Theorem 1.1 gives a converse under sufficiently small Lipschitz slope, including a boundary-length term. Their sharpness concerns regularity, not a numerical Holder norm. The report makes only this classification.

Definitions 3.1, 3.2 and 3.4 of `garcia_cuerva_gatto` respectively specify the kernel bounds, pre-existing L^2 boundedness and extension modulo constants. Theorem 3.6 assumes 0<alpha<epsilon<=1 and makes T(1)=0 in the quotient the criterion for Lip(alpha,mu) boundedness. The report retains L^2 boundedness and the quotient convention. It does not claim that kernel regularity alone is sufficient.

Theorem A of `holder_riesz_semigroups` assumes nonnegative iterated gradient form and the stated derivation intertwining identity. Corollary B treats a connected geodesically complete manifold with nonnegative Ricci curvature. The norms are first defined by a semigroup; Theorem 3.7 and Corollary 4.4 give comparisons, not isometries with the metric seminorm. The report correctly calls the result qualitative and first order.

## Schauder statements

Fife's Theorem 2.1, printed pages 513-514, estimates an inhomogeneous partial Holder norm under its kernel assumptions. The next page states dependence of C_3 on C_1,C_2,n,q,alpha without a numerical value. These pages were also read as rendered images. Display (2.2) has an anomalous printed inequality; no corrected version of that display is imported as a project hypothesis. The report's narrow statement that this is a partial Holder estimate with an unevaluated constant is supported.

Equations (4.8), (4.9) and (4.17) of `schauder_poisson` define the anisotropic full norm, start with an unspecified Schauder constant, and retain that constant under the stated nonnegative perturbation. The report correctly describes preservation of a constant, not computation of its value.

Theorems 1 and 4 of `schauder_germs` assert existence of a constant for the corresponding germ seminorms. The first requires 0<alpha<1<eta<2. The fourth assumes noninteger 0<alpha<eta<m and a scaling-homogeneous elliptic operator. The source itself notes that the indirect argument yields non-explicit constants. The report does not use these constants numerically.

Theorem 1.1 and (1.3) of `wang_schauder_2006` give a local Hessian estimate and the Holder factor 1/[alpha(1-alpha)] multiplied by an unspecified dimensional C_n. Its local full-norm setting is stated in the report. It is not an exact whole-plane seminorm formula.

## Unresolved source access

Nolder 1987, Arsenovic-Mateljevic 2021, Rode-Simonenko and its correction, and the relevant Astala-Iwaniec-Martin book theorem remain outside this audit. No new readable primary file was acquired in this check. Earlier unsupported access claims remain retracted. Titles, abstracts, contents pages and calls with no returned source text are not theorem evidence.

The closing search statement means only that the project did not find a published exact or explicit numerical bound for its specified two-dimensional norms. It is not a claim that none exists.
