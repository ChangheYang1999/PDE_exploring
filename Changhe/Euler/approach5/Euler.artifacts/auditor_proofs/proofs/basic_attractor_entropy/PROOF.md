# Entropy and physical measure of a regular basic backward attractor

## Statement and scope

Let 0<c<1/2, omega be any real number, and let U in C2(R3;R3), P in C2(R3) solve the rotating profile equation, with div U=0 and U=o(|y|) uniformly at infinity. Write

B=(cI-omega J)y+U, Omega=curl U, a=1-2c, b=1+c,

and let Phi_s be the complete B-flow. Suppose A is a basic hyperbolic attractor of the backward flow Psi_t=Phi_{-t}, in the following precise sense: A is compact, contains no zero of B, is hyperbolic and locally maximal, has dense periodic orbits, is topologically transitive, and has a trapping neighborhood. Suppose also that Omega has no zero on A.

Then the backward unstable bundle is one-dimensional and its Jacobian satisfies

J_t^u(x)=exp(a t) g(x)/g(Psi_t x)

for a continuous function g:A->(0,infinity). Consequently

h_top(Psi_1|A)=a.

There is a unique flow-invariant measure of maximal entropy on A. It is the equilibrium measure for the geometric unstable potential, and Lebesgue-almost every point in the basin of A is generic for it under continuous-time averages. Its entropy is a. These conclusions do not require a C1 stable foliation. They do not assert that the time-one map is ergodic for this measure.

The basic-set and nonvanishing-vorticity assumptions are additional dynamical conditions. This is not a proof that a general profile has such an attractor or that its whole trapping core has entropy exactly a.

## Proof of the Jacobian formula

The exact transport identities are

DPhi_s(x) B(x)=B(Phi_s x),
DPhi_s(x) Omega(x)=exp(b s) Omega(Phi_s x),
alpha_{Phi_s x} DPhi_s(x)=exp(-a s) alpha_x,

where alpha_x(v)=det(B(x),Omega(x),v). These were checked in A002 and A056.

First alpha cannot vanish on A. If Omega(x)=lambda B(x) with lambda nonzero, the first two identities give

Omega(Phi_s x)=lambda exp(-b s) B(Phi_s x).

Along the bounded full orbit, bounded Omega implies B(Phi_{-t}x)->0. Compactness then gives a zero of B in A, contrary to the hypothesis.

By A056 the forward splitting is E^s plus RB plus ROmega, with contraction exponent -a on E^s and expansion exponent b on ROmega. Thus the unstable line of Psi is E^s. The kernel of alpha is RB plus ROmega. Define

g(x)=sup{|alpha_x(v)|: v in E^s(x), |v|=1}.

Continuity, transversality and compactness give 0<min_A g<=max_A g<infinity. For a unit vector v in E^s(x), the covector transport identity at s=-t yields

exp(a t)g(x)=|alpha_{Psi_t x}(DPsi_t v)|
              =g(Psi_t x)|DPsi_t v|.

This proves the formula. No Livsic theorem is needed, and there is no periodic-orbit-to-global-cohomology gap.

## Entropy and the measure

Let q^u(x)=-d/dt log J_t^u(x) at t=0. For a C2 hyperbolic flow this is a Holder continuous potential. Its time integral is -log J_t^u(x). Every flow-invariant probability nu on A therefore satisfies

integral q^u dnu = -integral log J_1^u dnu = -a,

because log g-log g composed with Psi_1 has zero integral.

The variational principle gives

P(Psi|A,q^u)=sup_nu (h_nu(Psi_1)-a)=h_top(Psi_1|A)-a.

Bowen and Ruelle, Proposition 4.4(b), give P(Psi|A,q^u)=0 for a basic attractor. Their Lemma 4.1 and Theorem 3.3 give a unique equilibrium probability for this Holder potential, among flow-invariant probabilities. Since its integral is the same for all such probabilities, that probability is exactly the unique flow-invariant measure maximizing entropy. The entropy is a. Their Theorem 5.1 gives its continuous-time genericity for Lebesgue-almost every point of the attractor basin.

These theorems are stated for flows on a compact manifold. This causes no gap here: multiply the vector field outside a neighborhood of the compact trapping region by a smooth cutoff, extend it by zero to the one-point compactification S3, and apply the theorems there. The vector field and its flow agree on the trapping region. Any point in the original basin eventually enters that region. Pullbacks by finite-time diffeomorphisms preserve null sets, so the full-basin conclusion transfers to the original flow.

## Source verification

Actual source: R. Bowen and D. Ruelle, The ergodic theory of Axiom A flows, Inventiones Mathematicae 29 (1975), 181-202. The author-hosted manuscript is retained at in the team records, with extracted text beside it and retrieval metadata in retrievals.jsonl.

The basic-set definition on page 181 includes transitivity and dense periodic orbits. Theorem 3.3 is on page 187. The unstable potential and Lemma 4.1 are on page 189. Proposition 4.4 and its proof are on page 190. Theorem 5.1 and proof begin on page 191. Theorem 5.6 on pages 195-196 proves that positive-volume stable basin is equivalent to being an attractor for a C2 BASIC hyperbolic set. Rendered pages 190 and 196 were visually checked to remove OCR ambiguity in the pressure inequality and the quantifiers.

## What the source does not settle

CO5-prime starts with an arbitrary maximal invariant subset of a level set R_delta. Neither transitivity nor dense periodic orbits has been established there. Theorem 5.6 cannot be cited directly with that set substituted for a basic set. A separate reduction or a more general theorem is required. A union of several basic attractors also does not inherit uniqueness of the maximizing flow measure from the result above.
