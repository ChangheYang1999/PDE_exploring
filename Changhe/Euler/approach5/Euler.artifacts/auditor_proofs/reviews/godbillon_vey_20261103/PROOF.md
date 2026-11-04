# Scope audit of the Godbillon-Vey route

## Sources actually read

The actual fourteen-page arXiv2002.09992v2 manuscript by Thomas Machon, dated July8,2020, and the actual eight-page arXiv2001.01305v1 manuscript, dated January5,2020, were read in full from the retained PDFs and their text extractions. Their appendices and references are included in that reading. Printed page8 of the first paper was separately inspected as an image to verify the transport passage. Exact copies and hashes are in verification. The literature agent's source note and LIT86 countertest were read in full.

This is an audit of the displayed differential identities, hypotheses and applicability. It does not independently certify every foliation extension or the infinite-dimensional restricted Poisson construction. Reading an argument is distinguished from proving all of its analytic premises.

## 1. What the elementary construction proves

Let M be a compact oriented smooth three-manifold, possibly with boundary, and let theta be a smooth nowhere-zero one-form with theta wedge d theta=0. Write d theta=theta wedge eta. Such eta exists locally by linear algebra and globally by choosing a smooth vector field X with theta(X)=1 and taking eta=i_X d theta. Define GV(theta,eta)=integral_M eta wedge d eta.

The ambiguity in eta is addition of f theta. Since d2 theta=0 implies theta wedge d eta=0,

    (eta+f theta) wedge d(eta+f theta)-eta wedge d eta
       =df wedge d theta=d(f d theta).

Thus the integral is unchanged when M is closed, or when the boundary pullback of d theta vanishes. For d theta=i_w vol, tangency of w to the boundary gives exactly this latter condition.

For rescaling theta by a nowhere-zero real function h, one may take eta'=eta-d log|h|, so the change is

    -d(log|h| d eta).

Its boundary integral need not vanish from the preceding vorticity tangency alone. A boundary leaf condition is sufficient. This verifies the source's distinction between the closed-manifold foliation invariant and the boundary-dependent construction; it does not establish the further independence from the chosen integrable potential theta.

The source first imposes uniqueness of that integrable potential. Its Section2.1 addresses nonuniqueness using density assumptions on complements of zero sets and convergence of smooth approximations to possibly singular coefficients. The mixed-interior case is explicitly qualified by regularity of its regions. This audit has not proved these extension and convergence assertions for arbitrary C2 fields, arbitrary zero sets or infinite-volume domains. They therefore remain unavailable as automatic campaign inputs.

## 2. The transport inference and its exact correction

For D=partial_t+L_u, the assumptions D(d theta)=0 and theta wedge d theta=0 give locally D theta=d chi and only

    d chi wedge d theta=0.

They do not imply d chi=0. The complete [counterexample and corrected rotating identity](auditor_proofs/proofs/integrable_potential_transport/PROOF.md) establish this without boundary or completeness loopholes. On the flat torus, u=(2+sin y,0,0), p=0, theta=(2+sin y)dx is nowhere zero and integrable, yet L_u theta=d((2+sin y)^2/2) is nonzero. The explicit transported gauge theta_t=theta-t d((2+sin y)^2/2) also shows why an advected-gauge theorem is unaffected.

The alternative justification following equation31 on the source's printed page8 omits this wedge factor. Its preceding argument using advected Clebsch functions is a different assertion and is compatible with the example. The example has multiple integrable potentials, so it refutes no theorem retaining genuine uniqueness. The image confirms the exact printed text; this is not an extraction error.

For the physical velocity form of the rotating profile, the correct identity is

    L_B(U.flat)=-(1-2c)U.flat+d(|U|^2/2-P).

Zero pointwise helicity gives W.grad(|U|^2/2-P)=0, not constancy of that scalar. The exact local singular shear in the linked proof verifies that its gradient can be nonzero under the full local similarity equation.

## 3. Why the dynamical claims do not give the campaign theorem

The first paper's steady-flow obstruction concerns an ordinary Euler velocity stationary in physical time. A rotating similarity profile stationary in its similarity variables generally yields a time-dependent physical Euler field. Its local expression for an eta vector uses

    eta_vector=(w cross u)/(u.A_potential).

Where the denominator is nonzero, direct curl differentiation and the vorticity equation give

    eta_vector.curl eta_vector
      =-(w cross u).partial_t w/(u.A_potential)^2.

Here the gradient of the scalar reciprocal has zero dot product with its cross product with w cross u. A vanishing denominator requires separate local choices; no uniform finite bound follows across its zeros from this formula. The source's later replacement of u.A_potential by its spatial mean expressly discards fluctuations and is an approximation, not an unconditional coercive estimate.

The invariant is unchanged under constant nonzero rescaling of theta and d theta, since the same eta can be used. Its dimensionless character supplies no contradiction from the self-similar amplitude factor alone. Finiteness of the integral, its nonzero value for a hypothetical target profile, boundary terms at infinity and the behavior at zeros have not been established.

The source handles selected Morse and Kupka singularities and discusses more complicated zeros separately. A closed Kupka component can provide a periodic vortex line in that setting. No assertion that every nonzero C2 whole-space integrable vorticity has such a closed component was established. A noncompact line in R3 need not close. Thus the campaign exclusion of periodic vortex lines does not by itself discharge this route.

## 4. Restricted Casimir manuscript

The second source assumes a homology three-sphere, works with a connected component of smooth nonvanishing integrable one-forms and alters the functional derivative by the ambiguity arising from that constrained space. Its Section4.6 expresses the Godbillon-Vey functional as a restricted Casimir. The paper explicitly qualifies the rigor and leaves aspects of the functional-space characterization incomplete.

This is a formulation of a conservation law on a restricted compact smooth phase space. No whole-space C2 Liouville theorem, removal of zeros or finite integral at infinity is claimed by the argument audited here. Those source hypotheses are not supplied by the campaign's uniform velocity decay.

## Verdict scope

The bare automatic-transport inference is refuted by an exact complete example. The corrected local identities and the stated elementary boundary calculations are proved. Applicability of a global Godbillon-Vey obstruction to the whole-space rotating decay-only problem remains OPEN. No claim is made here that the global invariant or a theorem with transported-gauge or uniqueness premises is false.
