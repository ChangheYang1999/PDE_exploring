# Period conditions on a basin and on a periodic vortex cylinder

## Statement and scope

Fix 0<c<1/2 and any real omega. Put a=1-2c, kappa=1+c, A=cI-omega J. Let B,W be C1 fields on an open set O in R3 with

    div B=3c, div W=0, [B,W]=-kappa W.

Assume the B flow Phi is complete on O; write Psi_t=Phi_-t. Let K be a compact transitive regular uniformly hyperbolic attractor for Psi, with one-dimensional stable and unstable bundles and flow direction R B. Let N be a compact trapping neighborhood, with Psi_t N contained in int N for all t>0 and K equal to the intersection of these images. Define

    V = union_{t>=0} Phi_t(int N).

The following statements audit C29, Proposition5.11 and Remark5.12. The periodic-detection theorem A271 is a dependency: under the specified regular hyperbolic hypotheses, the periodic orbit classes span H1(int N;R). No corresponding assertion for an arbitrary singular attractor is assumed.

1. The inclusion int N into V induces isomorphisms on all homotopy groups and integral homology groups.
2. Given U=B-Ay and curl U=W throughout V, a single-valued pressure on V exists exactly when the closed form a U.flat-(B cross W).flat has zero periods on int N. Equivalently, U has zero circulation on a spanning family of the periodic orbits just described.
3. For a periodic orbit gamma of Psi, of minimal period L, suppose B and W are independent along gamma. The vortex lines through gamma form an intrinsically cylindrical injectively immersed leaf. In its coordinates (s,tau) in (R/LZ) times R,

       W=partial_tau,   -B=partial_s-kappa tau partial_tau,
       Psi_t(s,tau)=(s+t,exp(-kappa t)tau).

   For a C2 profile and its reduced Bernoulli function H,

       h=U.W=-partial_tau(H restricted to the leaf)/a,
       g=U.B=(partial_s H-kappa tau partial_tau H)/a.

   The helicity transport equation on this leaf is equality of mixed partials. Every intrinsic C2 periodic function e(s,tau) gives abstract g,h satisfying that identity and the loop condition through these formulas. This converse makes no assertion about extension to an ambient H or about actual Euler velocities.
4. In the explicitly marked positive-branch B24 Lorenz template, two periodic classes form an integral basis of the genus-two trapping handlebody. They are the LR and RRL itineraries. This supplies two pressure period tests, given curl U=W. It is a result about this template, not all singular attractors.

## 1. Compact sets enter the trapping region uniformly

V is open and invariant under every finite carrier time. If Q is a compact subset of V, choose for each point an entering time and an open neighborhood entering int N at that time. A finite subcover and the trapping property give a single T with Psi_T(Q) contained in int N.

Apply this to the compact image of a sphere, a singular cycle, a homotopy or a bounding chain. The homotopy Psi_{sT}, 0<=s<=1, moves that image into int N. If its initial image already lies in int N, the same homotopy stays there. These two facts prove surjectivity and injectivity on every homotopy and homology group. Moving base points follow paths inside int N, which give the standard identifications of based homotopy groups. Components are handled by the same path argument.

## 2. The pressure form and its periods

Set alpha=(B cross W).flat and delta=a U.flat-alpha. The vector identity

    curl(B cross W)=-3c W-[B,W]=a W

implies d delta=0 exactly when curl U=W. The rotating momentum equation is equivalent to

    a U+grad H=B cross W,
    H=P+|U|^2/2+(Ay).U.

Thus it has a single-valued pressure precisely when delta is exact. Closed real one-forms annihilate torsion and are exact precisely when all real homology periods vanish. Part1 transfers this test between int N and V. On a carrier orbit alpha(B)=0, so its delta period equals a times the U circulation. Apply A271 to the regular attractor. Its special single-generator result for a torus boundary is retained only under that theorem's hypotheses.

## 3. Completeness of the vortex lines through gamma

A bounded vector field on an arbitrary open set need not have a complete flow there. The source's boundedness sentence alone is insufficient. Here the bracket relation and complete carrier flow repair the issue without a new hypothesis.

Let p belong to gamma. The local commutation identity is

    Psi_T Gamma_tau = Gamma_{tau exp(-kappa T)} Psi_T.

There is a common epsilon>0 for which the W flow is defined for |tau|<epsilon from every point of the compact orbit gamma, with image in V. For any s,tau choose T large enough that |tau|exp(-kappa T)<epsilon and define

    E(s,tau)=Psi_-T Gamma_{tau exp(-kappa T)} Psi_{s+T}p.

All operations take place in V. The local commutation law makes the value independent of every sufficiently large T. Differentiating in tau gives partial_tau E=W(E), so this extends the vortex solution to every real tau. It is periodic in s with period L. The same law gives

    partial_s E=-B(E)+kappa tau W(E)

and the stated carrier formula.

Independence of B,W is preserved along this image: pushing their span by a vortex flow changes B only by a multiple of W, and pushing along the carrier multiplies W by a nonzero scalar. Hence E is an immersion.

Suppose E(s,tau)=E(s',tau'). Apply Psi_{nL}. The two fixed points Psi_s p and Psi_s' p of gamma are then joined by a vortex segment whose time is (tau'-tau)exp(-kappa nL). Letting n tend to infinity proves equality of these two points, hence s=s' modulo L. A local flow box for the nonzero W then forces tau=tau'. E is injective. It need not be an embedding onto a closed subset of the ambient basin.

The W arcs near gamma are its stable arcs by the unique local stable manifolds of the regular hyperbolic flow. Their complete extensions give the whole corresponding stable leaf. In particular the cylinder has no orientation-reversing identification: the stable multiplier is exp(-kappa L)>0.

## 4. What the intrinsic scalar equations say

Write e=H composed with E. The Lamb identity paired with W and B gives W H=-a h and B H=-a g, hence the two displayed formulas. Since g,h are C1 and E is C1, these formulas also show e is C2 at the regularity stated.

Direct differentiation gives

    B h+kappa h
      = (partial_s partial_tau e-kappa tau partial_tau^2 e-kappa partial_tau e)/a
      = W g.

The restriction of alpha to the leaf is zero, so U.flat=-dH/a there. Zero circulation around the cylinder is precisely the zero increment of e after s increases by L. Conversely both identities follow by differentiation for every intrinsic C2 function e periodic in s. For example e=-a tau gives h=1 in this abstract system, and reversing its sign gives h=-1.

These examples are not ambient profile constructions. If an immersed leaf accumulates on K, continuity of an ambient H imposes compatibility between distinct accumulating portions of the leaf. The intrinsic converse does not supply that compatibility, decay, curl coupling, or the normal Lamb equation. Thus the conclusion is limited to the enumerated leafwise equations; it is not a theorem that every global periodic-observable argument fails.

## 5. Two explicitly independent Lorenz template periods

Use the marked B24 genus-two template and its usual positive-branch quotient map

    f(x)=sign(x) K0 (|x|^q-1/2),
    q=(1-c/2)/(2-5c/2), K0=1+1/(sqrt(2)q),
    I=[-K0/2,K0/2],
    c0<c<1/2, c0=2(2-sqrt(2))/(5-sqrt(2)).

Then 1/sqrt(2)<q<1 and K0/2<=1. On the positive branch f(x)+x is negative near zero and positive at K0/2. Its zero gives an LR cycle of minimal period2.

Put x0=2^(-1/q), so f(x0)=0. The inequality f(K0/2)>x0 follows without a computation. Both K0 and (K0/2)^q are nonincreasing in q, their latter value exceeds1/2, and 2^(-1/q) is increasing. Therefore

    K0((K0/2)^q-1/2)-2^(-1/q)
      >= 1/(2 sqrt(2))-1/4 > 0.

There is x1 in (x0,K0/2) with f(x1)=x0. On J0=(x0,x1), the first and second image intervals are (0,x0) and (-K0/2,0). The continuous function f^3(x)-x is negative near x0 and positive near x1. A zero has the itinerary RRL and minimal period3.

Uniform contraction on the stable fibers of this marked template lifts these periodic quotient points to periodic flow orbits. The identified core-loop basis l,r of this handlebody assigns class n_L l+n_R r to an itinerary. The two classes are therefore (1,1) and (1,2), whose determinant is1. This specific template identification is essential; a symbolic itinerary in an arbitrary flow alone does not determine ambient homology.

For the formal opposite map -f the same intermediate-value argument gives one fixed point on each branch, with the two separate core classes if that alternative geometric marking is realized. No assertion of an additional bracket-model realization with that orientation is needed here. The positive-branch B24 template suffices.

Given curl U=W, zero U circulation on the two exhibited orbits makes delta exact on N and, by Part1, on its basin. Any closed rectifiable homoclinic loop of the zero is then also a zero-period cycle. Since alpha vanishes on its regular carrier arcs, its action identity is

    integral_R |B|^2 dt = -2 omega Area_xy(loop).

Rectifiability is an explicit premise; bounded B on the compact loop then also makes the action integral finite. No pointwise helicity sign follows from this loop identity.

## Verification and limitations

The complete source propositions were read and the algebra was reconstructed. No numerical computation was needed. The evidence directory records source hashes and retained copies. A271, the local stable-manifold theorem and the already audited marked B24 construction are named dependencies. This result is uniform in finite omega and does not assume axisymmetry, finite energy or outgoing carrier trajectories. It does not prove nonexistence.
