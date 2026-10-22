Written 2026-10-21T20:00:51.823369+00:00 before the new audit.

# Dependency of the source bounds on the canonical moment archive

## Statement, conventions and scope

This is a dependency audit of accepted numerical and analytic results for the exact normalized modal_v2 trial, with two separate entries for the original X3 axis computations. It is not a new enclosure computation. The three labels refer only to mathematical dependence on topic31's original_knots.jsonl.gz:

(a) The stated result has a recorded derivation independent of that archive.
(b) Its only mathematical inputs from that archive are complete density polynomials H, including their exact geometry. Topic99 has independently checked those H inputs. No I/J anchor is used in the calculation of the stated quantity.
(c) The recorded derivation uses I/J endpoint moment balls, directly or through a derived velocity bound. Independent full reproduction of those moments remains the open topic156 obligation at writing.

A hash of the full archive can appear in a (b) provenance manifest even though only H enters the formula. Conversely, two different local propagation methods starting with identical I/J anchor balls do not remove their common moment dependency. Independent integration in topic25 supplies a separate route to its point scalars. The labels do not assert that every other prerequisite has newly been proved here. Every analytic conclusion retains its original domain and regularity hypotheses.

The precise claim is the table in TABLE.md. Numerical ceilings and exact statements are those of the cited accepted artifacts. The fresh check will rehash their dependency records, compare the reported exact scalar inputs and record current source excerpts. No numerical field or norm is recomputed.

## Proof by following the mathematical inputs

Density: rho=r^3 sum_j H_j(t) sin((2j+1)theta). Cartesian differentiation through order2 depends only on H,Hprime,Hsecond and r,theta. Topic84's export_density.py copies only density_polynomials and span geometry. check_hessian.py then differentiates that finite expansion. Its bound holds for every center in the imported bracket, so verifying the existence of the trial's root is unnecessary for this full-bracket Hessian assertion. This proves label(b), irrespective of the full-archive hash in its manifest.

Velocity: psi=(r^4/2)sum_n (J_n-I_n)sin(2n theta), U=(-psi_y,psi_x). The local ODEs Iprime=-(2n+4)I+H_(n-1), Jprime=(2n-4)J-H_n require endpoint values. Topic85 export_moments.py imports i_left and j_right from the canonical archive, and both engines of its whole-disc Hessian calculation start from them. Topic89 evaluates its root and matrix with the same imported moment_inputs.json; changing the local integral formula does not change those initial data. Topic95 likewise uses those moment anchors for the third and fourth velocity derivatives. These are(c).

Composition: topic86 substitutes M_V and M_rho into C_V=(417/10)M_V+3M_rho and E=delta C_V. Topic92 has the same M_V in C_s=(12s+9/2)M_V+3M_rho. Their actual source coefficients are(c). The rational inequalities viewed solely as conditional algebra are independent, but that is a different statement from an actual trial coefficient bound. Topic97 imports both those constants and the high velocity derivative ceilings of95 before integrating the cutoff and applying96, so its actual auxiliary inverse ceilings are(c). The isolated dilation identities and domain correspondence of96 are(a) as conditional analytic theorems; their application to95 does not become archive-independent.

Moving source: topic94 takes the fine point values from25, but forms m=A_lower-M_V R0 and bounds the moved transverse eigenvalue by eps2+M_V eps0/m. Thus its quantitative movement and radius2.1886e-8 are(c). The reference value mu-1 alone is(a). The source-box and local-K1 conclusions also import84/85/89, hence are(c).

Sobolev source box: topic102 separately derives CU,Csigma,Cy,CH from whole-plane Fourier integrals. These universal embedding constants are(a). However the coefficient b1=c1+(M_V/m0)c0, with c0=CU+(xmax/3)Csigma and c1=(4/3)Csigma, uses the velocity Hessian and m0 obtained with that Hessian. Its bound0.06970585 and the resulting radius3.2318e-7 are(c). The exact source defect in its numerator is independently supplied by25, but dividing by a coefficient containing M_V retains(c).

Four-point source jets: topic76 source_jet_corrections uses only source_result.json from25 for D=|(mu-1)g| and C=|mu-1|+|g|+|gprime|. Topic25 certify_source.py builds exact density polynomials from modal_v2.json, integrates canonical inner and outer analytic anchors, and propagates through the original spline spans itself. It does not load the topic31 archive. Thus25 and these76 scalar consequences are(a). The existing exact D lower endpoint will be compared against6.70197e-7; this is only a new comparison of an already accepted exact endpoint, not a new source integration.

Axis control: topics2/8/10 use the original X3 data, canonical kernel integrals and elementary angular formulas. B=3L^2/[4(1-k)] and the normalized strain constant K=L^2/(1-k)[1/36+sqrt(3)/(8pi)] require only L,k. Positivity uses X3 spline coefficients and its independently integrated central strain. The axis values at7 and10 use direct paired-kernel integration of original X3. None requires the normalized modal trial's topic31 archive, so these are(a).

The same bracket P,A,mu,g quoted by89 can also be obtained from25's strictly finer independent point certificate: this is a separate(a) route for those point scalars only. It does not remove(c) from89's whole-disc DV variation or cutoff-sign application. The fresh exact comparison will verify the inclusion in the quoted broader bracket and scalar box. No replacement of85's derivative certificate is inferred.

## Evidentiary limit

The new checker verifies file identities and exact inherited scalar comparisons; the code readings establish which inputs mathematically enter each result. A manifest edge alone is not evidence that every datum in the referenced file is used, and absence of a literal filename alone is not proof of independence. The formulas and data paths above supply the argument. Existing proof and evidence files remain immutable. Any decisive IPM endpoint, full global inverse, X3 neighbourhood or new physical derivative certificate remains OPEN.
