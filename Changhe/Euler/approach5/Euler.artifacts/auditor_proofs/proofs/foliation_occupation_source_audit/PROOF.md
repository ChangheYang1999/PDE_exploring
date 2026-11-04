# Audit of smooth-foliation and occupation-time source use

Audit 2026-11-03T00:59:09Z. A330: CONFIRMED as an audit of the specified source hypotheses and the deductions below. It does not certify a new proof of the cited classification theorems or exclude an Euler profile.

## 1. Exact scope of the source statements

The actual retained primary texts listed in the team records were inspected at the recorded passages. The complete Zweimueller proof was read. The classification proofs were not reconstructed, and no claim of having read all seven articles in full is made.

Ghys1987's introductory theorem on printed page252 concerns an orientable C-infinity Anosov flow on a closed three-manifold. Both strong invariant line bundles must be C-infinity, and the nonsuspension conclusion is smooth orbit equivalence with an algebraic diagonal flow on a compact quotient of the universal cover of SL(2,R). It is not a fixed-time conjugacy assertion. The separate page253 theorem is for geodesic flow of a smooth negatively curved metric on a compact surface and assumes a C2 weak-stable foliation.

Hurder-Katok1990 Theorems3.1-3.4 and Corollary3.5 on printed pages17-19 require volume preservation and compact or closed three-dimensional Anosov dynamics. In the C-infinity case the specified transverse regularity beyond the o(s|log s|) threshold of one weak distribution eliminates the periodic obstruction and gives smooth weak distributions. Their passage to strong distributions uses an appropriate smooth invariant dual one-form. This audit deliberately makes no finite-r claim from the scanned superscripts.

Ghys1992 TheoremA assumes a volume-preserving C-infinity Anosov flow on a closed oriented three-manifold, with both weak foliations C2 and orientable. The algebraic conclusion follows after a smooth time change. TheoremB constructs flows with both weak foliations smooth and no invariant volume from distinct marked hyperbolic structures. TheoremC's additional pinching ratio is strictly below2. The Euler regular periodic rates have ratio (1+c)/(1-2c)>7 in the primary interval, so they do not meet that pinching screen.

Asaoka2012 Theorem1.1 attributes homogeneous classification of locally free affine-group actions to Ghys under a continuous invariant volume on a closed connected oriented three-manifold. Its own Theorem2.7 and Proposition2.8 construct nonhomogeneous smooth actions when a suitable closed one-form has nonzero cohomology. The displayed stable generator contracts at an exact constant exponential rate. AppendixB requires the extra C2 weak-unstable foliation in its specified fixed homogeneous quotient to recover homogeneity. The global classification input in the proof is used as cited, not reproved here. These facts refute the bare inference from an affine bracket and one smooth contracting generator to homogeneity.

Belliart1998's introduction likewise keeps continuous invariant volume. Its TheoremA explicitly excludes the affine group from its eigenvalue hypothesis. It cannot remove the missing volume premise in this application.

The supplied Euler basin structure gives neither a closed Anosov ambient manifold nor a smooth weak-unstable foliation. Its support may meet carrier or vorticity zeros. Thus none of the inspected classification statements presently gives the desired exclusion.

## 2. Direct checks of the Euler obstructions to those hypotheses

Let B=(cI-omega J)y+U, W=curl U, d=3c, kappa=1+c and a=kappa-d>0. The already audited equations give div B=d, div W=0 and [B,W]=-kappa W. For alpha=(B cross W).dy,

    curl(B cross W)=kappa W-dW=aW,
    alpha(W)=alpha(B)=0,
    alpha wedge d alpha=0,
    L_W alpha=0, Phi_t^*alpha=exp(-at)alpha.

The first identity follows by expanding curl of a cross product; the wedge identity is a alpha(W) times volume. Cartan's formula gives L_W alpha=0. The final covariance follows from transport and the determinant, as in A056. These identities hold where defined, but alpha can vanish at the exceptional zeros. Also alpha is not a dual form to B: a dual form used in the cited regularity theorem must evaluate to1 on B.

Suppose p is a regular periodic carrier point of period T>0. Liouville's formula gives det D Phi_T(p)=exp(dT). A positive continuous invariant density rho near that orbit would require rho(p)exp(dT)=rho(p), which is impossible. The transverse Poincare derivative has the same determinant since the flow direction has multiplier1 at the return point. A positive time change keeps the transverse return map, so cannot remove this obstruction. This excludes that additional invariant-volume hypothesis near the orbit. It does not exclude the Euler periodic orbit itself, whose carrier was never volume preserving.

For a variable-time backward return F(x)=Psi_(tau(x))(x), differentiation adds a multiple of B(F(x)), annihilated by alpha. Therefore

    F^*alpha=exp(a tau(x))alpha.

The multiplier can vary with the transverse coordinate. Fixed-time similarity is consequently not a proof of constant-slope transitions in a global transverse-affine atlas. Another construction might supply such an atlas, but the displayed covariance alone does not.

## 3. The exact occupation-time source limits

Zweimueller2004 proves the Hopf ratio theorem for integrable f,g with g>=0 and positive integral on a sigma-finite measure-preserving system. Ratios converge on the saturation where g is visited; in the conservative ergodic case the ratio equals integral f divided by integral g. The proof induces on a finite-measure return set and applies Birkhoff, then extends return-subsequence convergence by monotonicity for nonnegative functions.

In a nonergodic formulation, the invariant-set integral identity must be restricted to the visited saturation, as the proof explicitly does. On an invariant component where g vanishes identically and f does not, an unrestricted identity integral_I Qg=integral_I f would be false. This qualification does not affect the literature note's ratio statement or the proposed Euler application.

The source supplies no deterministic polynomial occupation denominator. A325 independently demonstrates the failure of that inference from conservativity and ergodicity alone by an explicit infinite-mean tower. It does not disprove a rate derived from Euler geometry.

Aaronson-Thaler-Zweimueller2004 studies two-branch interval maps under its explicit C2, full-branch, indifferent-endpoint and convexity assumptions; its distributional Theorem1 adds regularly varying endpoint behavior. Its Theorem2 concerns cusp occupations of infinite-measure sets, not arbitrary finite-volume Euclidean balls. These statements cannot be transferred without verifying the return-process hypotheses. No such verification for Euler is supplied.

## 4. What remains open

The exact algebraic comparison of hypothetical same-orbit bounds has threshold c<2/7: numerator exponent1-2a/kappa minus denominator exponent a/kappa equals1-3a/kappa. This is only an exponent calculation. In the primary range, no contradiction follows. The proposed smearing result supplies a different averaged comparison and specifies the extra Lq premise; its audit is separate.

A new global rigidity theorem for the actual basin geometry, a proof of the missing regularity or volume hypotheses, or an Euler-specific quantitative occupation argument remains necessary. The inspected citations do not presently provide one. The literature note is accurate with these scope qualifications. No unverified source is being used to label nonexistence PROVED.
