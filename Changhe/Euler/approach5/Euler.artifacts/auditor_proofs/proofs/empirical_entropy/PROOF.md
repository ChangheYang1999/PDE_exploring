# Empirical entropy forced by a contracting bracket eigenfield

## Exact statement

Let B be a smooth complete vector field on R3, with div B=d constant, and let Psi_t denote its backward flow. Assume every backward trajectory is bounded. Let W be a continuous vector field satisfying

    W(Psi_t x)=exp(kappa t) D Psi_t(x) W(x),  t>=0,

where kappa>d. Write K(x) for the compact omega-limit set under Psi. For Lebesgue-almost every x with W(x) nonzero there is a probability nu that is a continuous-time empirical limit of this same x, is invariant under the full flow, is supported on K(x), and satisfies

    h_nu(Psi_1)>=kappa-d.

No divergence condition on W, Euler coupling, or uniform bound on all backward trajectories is assumed. Smoothness of B is required for the external entropy theorem used below. This proof does not establish the conclusion for a general C2 B.

## Derivative lower bound

Fix x with W(x) nonzero. On the compact closure of its backward trajectory let |W|<=M. Let sigma_1>=sigma_2>=sigma_3>0 be the singular values of D Psi_t(x). Transport implies

    sigma_3 <= exp(-kappa t)|W(Psi_t x)|/|W(x)|.

Liouville's determinant identity gives sigma_1 sigma_2 sigma_3=exp(-dt). Consequently

    ||exterior^2 D Psi_t(x)||
      >= exp((kappa-d)t)|W(x)|/|W(Psi_t x)|
      >= exp((kappa-d)t)|W(x)|/M.

The denominator is nonzero by transport. The lower exponential growth rate is at least kappa-d. If W(Psi_t x) tends to zero, the ratio to exp((kappa-d)t) tends to infinity. This latter statement does not imply a strict improvement of the exponential rate.

## Compactification and the exact external theorem

For each integer m>=1 choose a smooth cutoff that is one on a neighborhood of the closed radius-m ball and zero outside a larger ball. Cut off -B and extend it by zero across the point at infinity in S3. This defines a smooth complete flow and a smooth time-one diffeomorphism F_m on the compact smooth manifold S3.

Let E_m be the points whose whole backward trajectory stays in the radius-m ball. It is measurable, since it can be defined using nonnegative rational times. On trajectories of E_m the modified flow and its derivatives agree with the original flow. The sets E_m cover R3 by boundedness of backward trajectories. There is no claim that each radius-m ball itself is trapping.

Burguet's Main Theorem states: for a smooth map F of a compact smooth manifold, for Lebesgue-almost every x there is a measure mu in pw(x), the set of weak limits of the discrete empirical probabilities, for which

    h_mu(F)>=max_{0<=j<=dim M} limsup_n n^(-1) log ||exterior^j D F^n(x)||.

For j=0 the norm is one. The finite maximum can equivalently be put inside the limsup. Apply the theorem to F_m outside its null exceptional set, intersect with E_m, and use j=2 and the preceding estimate. Taking the countable union of these null exceptional sets gives the asserted almost-everywhere selection. On E_m the selected mu is an empirical limit for the original Psi_1 and has entropy at least kappa-d.

Since the trajectory is precompact, its distance to K(x) tends to zero. Testing the empirical measures against continuous functions supported away from K(x) proves supp mu is contained in K(x). Thus the entropy and invariance statements concern the original dynamics on K(x), not any cutoff region.

The actual manuscript used here is David Burguet, Entropy of physical measures for C-infinity smooth systems, arXiv:1812.04308v2, 17 January 2019, Main Theorem on printed page 8. Section 4, printed pages 17-18, proves the selection mu in pw(x), with the final limiting step justified by upper semicontinuity of metric entropy for a fixed smooth map. The manuscript is retained in the team records. The external deep entropy theorem is a dependency, not reproved here.

## Full-flow invariance and preservation of entropy

Set nu=integral_0^1 (Psi_s)_*mu ds. The Psi_1 invariance of mu implies full-flow invariance of nu. If the discrete empirical measures along integers n_i converge to mu, then for every continuous test f,

    (1/n_i) integral_0^{n_i} f(Psi_t x) dt
      =(1/n_i) sum_{j=0}^{n_i-1} integral_0^1 f(Psi_s(Psi_j x)) ds.

The function integral_0^1 f(Psi_s y) ds is continuous on the relevant compact set. This identity proves convergence to nu, so nu is an empirical limit of the same trajectory.

Each (Psi_s)_*mu is Psi_1-invariant and measure-theoretically conjugate to mu by Psi_s. Their entropies coincide. The harmonicity of entropy on invariant probabilities gives h_nu(Psi_1)=h_mu(Psi_1). Alternatively finite convex averages have the same entropy; their limit has entropy at least that value by smooth-map upper semicontinuity, which alone suffices for the claimed lower bound. The support remains in K(x), a full-flow invariant set.

## Euler consequence and exact remaining alternative

For a smooth rotating Euler profile with U=o(|y|), 0<c<1/2 and arbitrary real omega, let B=(cI-omega J)y+U, W=Omega=curl U. The verified completeness and transport identities give d=3c, kappa=1+c and kappa-d=1-2c>0. A fixed compact core Lambda contains every backward limit set.

If every ergodic full-flow invariant probability supported on Lambda intersect {Omega=0} has zero entropy, then

    Leb{x: Omega(x)!=0, K(x) subset {Omega=0}}=0.

Otherwise the empirical measure selected at a nonexceptional point of this set has positive entropy, is supported on the irrotational set, and its full-flow ergodic decomposition supplies a positive-entropy component there. This contradicts the additional zero-entropy assumption.

For a nonconstant real-analytic profile that assumption follows from A089: positive entropy on the irrotational set forces every derivative of Omega to vanish at a point, hence everywhere by analyticity. For a merely smooth profile, A089 gives flatness on the positive-entropy component's support, with no contradiction. The support need not be the entire K(x), and the approach to it need not be exponential.

## Verification and scope

This independently checks Section 1 of the coordinator's in the team records, including its countable-ball correction. The theorem is CONFIRMED as A186. The arbitrary smooth rotating nonexistence problem remains open.
