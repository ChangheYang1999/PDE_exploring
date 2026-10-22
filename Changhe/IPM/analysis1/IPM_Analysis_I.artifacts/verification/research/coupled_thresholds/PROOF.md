# Frozen Sobolev coercivity and the scope of cusp thresholds

Date: 2026-10-20. Status: CONFIRMED analytic frozen-model theorem after actual Claude Opus 5.5 review; its detected arithmetic error is corrected and recorded. This addresses the frozen whole-plane operator only and audits a specific assertion of SPEC v2. It does not settle any variable-coefficient Fredholm index.

## Statement and spaces

Let A>1, g>=0 and L=A x partial_x+y partial_y-1-gM, where M has Fourier symbol xi^2/(xi^2+eta^2). Let H_s be the homogeneous Fourier completion defined in ../frozen_conjugation/PROOF.md, and use the graph closure of the smooth Fourier core avoiding zero. Set

b=(A+3)/2, s_fast=(g+b)/A, s_slow=b.

If s<min(s_fast,s_slow), put delta=min(b-s,g+b-A s)>0. Then L is bijective from its graph domain to H_s and ||L^(-1)||<=1/delta. If s>max(s_fast,s_slow), the same conclusion holds with delta=min(s-b,A s-g-b)>0. In either range no normalized sequence in this graph domain can have image tending to zero in the same H_s norm. The result holds also after restriction to odd y, or even x and odd y.

The constants A and g here are arbitrary real parameters. Rounded illustrative profile numbers do not certify actual source data.

## Proof

Write D=A xi partial_xi+eta partial_eta, r=|(xi,eta)| and m=xi^2/r^2. For h in the core, let F=r^s h_hat. Fourier differentiation gives

r^s L_hat(r^(-s)F)=-D F-(A+2)F+s[1+(A-1)m]F-gmF.

The skew-adjoint Fourier dilation generator is S_hat=-D-(A+1)/2, with the domain proved explicitly in the conjugation note. Thus the transformed operator is S_hat+C, where C is the bounded self-adjoint multiplication operator

C=s-b+[s(A-1)-g]m.

Its values lie between the two endpoint numbers s-b and A s-g-b, since 0<=m<=1. The real energy identity is therefore

Re <Lh,h>_{H_s}=integral [s-b+(s(A-1)-g)m]|F|^2.

If s lies below both thresholds, this is at most -delta ||h||^2. Above both it is at least delta ||h||^2. Cauchy-Schwarz gives ||Lh||>=delta||h||, first on the core and then on its graph closure. A bounded perturbation of a closed generator is closed on the same domain: a graph-convergent pair for S_hat+C is graph-convergent for S_hat after subtracting the bounded C term. The same core remains a core by equivalence of the two graph norms.

For surjectivity, the adjoint is -S_hat+C on the same domain, since C is bounded self-adjoint. It has the identical real energy and hence zero kernel. The range of L is closed: if Lh_n converges, the lower bound makes h_n Cauchy and closedness supplies its limit in the domain. Its orthogonal complement is the adjoint kernel, hence zero. Its closed dense range is the full Hilbert space. This proves the inverse bound. All operators and their adjoints preserve the stated reflection subspaces, so the same proof applies there.

## Ordinary inhomogeneous Sobolev spaces below both thresholds

For 0<=s<min(s_fast,s_slow), the same bound and bijectivity also hold in the ordinary whole-plane H^s norm. Conjugate by (1+|zeta|^2)^(s/2) instead of r^s. The bounded real multiplier is now

C_s(zeta)=-b-gm+s [r^2/(1+r^2)] [1+(A-1)m].

Since s>=0 and the last factor is positive, C_s is at most s-b+[s(A-1)-g]m, hence at most -delta. It is bounded below by a finite constant as well. The same closed-generator, adjoint and closed-range argument proves surjectivity and the inverse estimate. This removes the homogeneous-representative issue for this particular lower range. The graph domain still matters. Neither a disc with unspecified exterior data nor a variable-coefficient profile is treated. For s above both thresholds this inhomogeneous argument does not give positive coercivity, because low frequencies retain a negative real part.

## Consequence for SPEC v2

With the exact illustrative decimals A=10.1507252 and g=29.75, s_fast is about 3.5785977735 and s_slow=6.5753626. At the ordinary order s=3, both energy endpoints are strictly negative and delta=3.5753626. Thus the frozen whole-plane operator has the proved bound ||h||_{H_3} <= (1/3.5753626)||Lh||_{H_3}. This refutes a same-order Weyl-sequence assertion for this realization below the fast threshold. It does not exclude local homogeneous solutions with nonzero exterior data.

SPEC v2 section 3.2 says that radial packets give approximate kernels in every space below the thresholds. That claim is not in its cited proof. The packet report section 3 retains the cutoff error of the same order as h and obtains vanishing residual only when the output has fewer derivatives. Its sections 4 and 5 explicitly distinguish this derivative-gap result from same-order estimates. Its section 6 already states the negative Sobolev energy below s_fast. The model cusp regularity threshold and the radial symmetric-part zero are valid computations; they do not imply a below-threshold same-order approximate kernel.

The same-order Hoelder result, a variable-coefficient source estimate, and the global transport and coupled Fredholm indices remain OPEN. In particular, a claim that both norms in every possible two-norm scheme must lie above the fast threshold does not follow from these packet calculations. No opposite global existence or invertibility theorem is asserted.

## Audit correction

The first draft mistakenly used only the fast endpoint 5.873187 as delta at s=3. The actual Opus 5.5 review caught this. Exact rational recomputation gives the slow endpoint 3.5753626, which is the smaller one and the correct constant. The initial team note has a timestamped correction; no numerical source data are being certified by these decimals.
