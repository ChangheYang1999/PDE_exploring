# Classified invariant measures and unclassified limit points

Status: A781-A783 CONFIRMED. Independent reconstruction of LIT132 and the remaining B33 referee comparison. These are dynamical countertests and covector facts, not Euler counterexamples.

## 1. A complete constant-divergence countertest in three dimensions

For any c>0 there is a smooth complete vector field B on R3, with div B=3c, having a forward orbit whose omega-limit K is a circle. Every invariant probability on K is supported on two equilibria, while K also contains the two connecting trajectories between them.

To construct it, first use polar coordinates(r,theta) in the annulus 3/4<r<5/4. Put s=r-1 and let

    r'=-s^3, theta'=sin(theta)^2+s^2.

Multiply the Cartesian field by a smooth radial cutoff equal1 on 7/8<=r<=9/8 and supported in the original annulus. Its zero extension is a smooth compactly supported planar field F. For initial0<s0<1/8, the forward orbit stays in the region where the cutoff is1. Direct integration gives s(t)=(s0^(-2)+2t)^(-1/2), while the increasing real lift of theta satisfies

    theta(t)-theta(0)>=(1/2)log(1+2s0^2t)->infinity.

It crosses every fixed angle modulo2pi at arbitrarily late times. Because r(t)->1, its omega-limit is exactly the unit circle. On that circle theta'=sin(theta)^2, with only the two equilibria theta=0,pi; each open semicircle is one complete connecting orbit.

On either open semicircle, zeta=-cot(theta) is a coordinate in R with zeta'=1. The restriction of any finite invariant measure to this invariant semicircle becomes a finite translation-invariant measure on R. Its values on integer translates of a half-open unit interval are equal and summable, hence zero, and those intervals cover R. Thus every invariant probability on the circle is a convex combination of its two equilibrium atoms.

Set d=div F and define

    B(x,y,z)=(F1(x,y),F2(x,y),z(3c-d(x,y))).

Then div B=3c exactly. B has at most linear growth since F,d are bounded. More directly, its planar equation is complete and the vertical equation has an explicit exponential solution finite on every bounded time interval. Therefore B is complete in both directions. The invariant plane z=0 retains the circle and its limit orbit.

This verifies all claimed properties. It does not make B an Euler carrier: outside the planar support B=(0,0,3cz), so B-(cI-omega J)(x,y,z) has linear growth. No actual curl, helicity or Euler transport is imposed.

## 2. Why a bounded measurable covector fixes an exponent

Let a C1 field B have a compact full-flow-invariant set K and invariant probability nu. Write Phi_t for the flow. Let u be a bounded measurable covector section, nonzero almost everywhere, and suppose for a real rho, on a common full-measure domain and every integer n>=0,

    u(Phi_n x)=exp(rho n)DPhi_n(x)^(-T)u(x).           (1)

Then -rho is an exponent of the inverse-transpose cocycle at almost every point, and rho is an exponent of the original derivative cocycle. No integrability of log|u| is needed.

Indeed, the derivative and inverse derivative over unit time are bounded on K, so the multiplicative ergodic theorem applies. The sets E_m={|u|>=1/m} exhaust its nonzero set. Recurrence of the probability-preserving map Phi_1 gives, for almost every x in some E_m, arbitrarily large n_j with Phi_(n_j)x in E_m. If |u|<=M, equation(1) gives

    |DPhi_n(x)^(-T)u(x)|<=M exp(-rho n),
    |DPhi_(n_j)(x)^(-T)u(x)|>=m^(-1)exp(-rho n_j).

At a multiplicative-ergodic regular point the exponent of every nonzero vector exists. The upper bound and recurrent lower subsequence force its value to be -rho. The inverse-transpose spectrum is the negative original spectrum, proving the claim. Bounded time intervals compare discrete and continuous exponents. This argument applies without ergodicity of nu.

Similarly DPhi_n B(x)=B(Phi_n x) gives exponent0 if B!=0 almost everywhere. In dimension3, if rho<0 and div B=3c, these two distinct exponents and the determinant identity give the multiset{0,rho,3c-rho}. This spectrum alone does not imply periodicity or classify all points of K.

## 3. Precise comparison with the B33 referee

The complete referee answer in Theory Agent B in the team records was read, including its repairs. Its periodic no-entry argument agrees with A541: the H-level avoids stable faces and the carrier points outward through unstable faces. Arbitrarily late visits would force eventual trapping; the unstable scalar then forces the orbit to be the cycle, impossible for the vortical line. No-entry alone does not say the intersection times are a terminal interval. The equilibrium proof uses a positive quadratic form satisfying C^TP+PC=I and therefore covers complex, nonnormal and Jordan cases. An ordinary square is inadequate.

The inherited rho<=-a is necessary to deduce the hyperbolic nonflat first-family condition rho<-kappa. The weaker rho<0 does not exclude the other spectral intervals. All these corrections are retained in the standalone A541-A542 proof.

Its finite-network argument also agrees with A542: on a C2 regular level use the C1 projected field. Invariant C1 graphs can be subtracted and the original components factored without assuming a C2 coordinate change. Positive saddle trace yields transverse passage distances r_next>=C r^theta,theta<1; finitely many tubes make the constants uniform. An orbit approaching a nontrivial finite network would have r->0, contradicting this lower bound. Hyperbolicity and finite-network structure are extra premises in this argument. The later A658 supplies an independent stronger actual-profile convergence theorem; it does not retrospectively validate the old measure-only inference.

## 4. The two additional referee countertests

On T2 let v=(1,alpha) with irrational alpha, f=2-cos(2pi x)-cos(2pi y), and X=fv. Choose an irrational line orbit avoiding the unique zero q. Its reparametrized linear time tends to infinity in both directions: a finite terminal linear time would reach a regular point because that whole line avoids q, contradicting cessation of the flow there. Thus its two limit sets are T2.

If mu is an invariant probability, nu=f mu is invariant for the linear flow in the weak sense integral v.grad phi dnu=0. Testing all Fourier modes and irrationality shows nu=C times Haar measure. If C>0, then away from q, mu=C f^(-1) times Haar measure. But f is comparable to squared distance near q, so this measure has infinite mass. Therefore C=0 and mu is the single atom at q. This verifies the referee's separate measure-support counterexample; no Euler interpretation is made.

For its clock countertest, on an annulus let B=-kappa(r-1)partial_r+partial_theta and W=(r-1)B. Along an orbit with r>1, r-1=C exp(-kappa t),theta=theta0+t. With tau=1/(kappa(r-1)), one has B=kappa tau W,tau'=kappa tau,[B,W]=-kappa W, yet the omega-limit is the whole rotating circle. Thus these clock and parallelism identities alone do not prove convergence. No completeness outside the annulus, actual-curl relation or Euler equation is claimed.

## 5. Scope and evidence

The examples refute an abstract inference, not any stronger theorem using the full Euler identities. The covector exponent proof uses finite-measure recurrence and the compact multiplicative-ergodic theorem already used in the confirmed campaign proofs, with its full integrability hypotheses checked here. All constructions and estimates are exact analytical calculations, with no computation. Source snapshots accompany the proof.

The B33 referee explicitly reports that its attempted model consultation failed before obtaining a review. It is not counted as successful model collaboration. Continuing comparison uses existing configured-model team files, without a new client or agent and without independent runtime attestation.
