# Corrections to the dynamical report statements

## Scope

These checks concern Theory Agent B in the team records as read on 2026-11-02 around 22:25 UTC. Write B=(cI-omega J)y+U, Omega=curl U, phi for the carrier flow, and psi_t=phi_-t. The previously proved circulation, spectrum, null-basin and entropy statements remain valid with their exact hypotheses. Three qualifications and one incorrect example need repair before the draft is copied verbatim.

## 1. Flow domain in the circulation law

For a C2 exact profile, the local identity L_B(U.dy)=-(1-2c)U.dy+d(|U|^2/2-P) gives

    integral over phi_s(C) of U.dy = exp((2c-1)s) integral over C of U.dy

for every closed C1 curve C and every time interval on which its flow image exists. H0 alone does not supply completeness. Adding uniform sublinearity gives |B(y)|<=C(1+|y|), hence completeness and the law for all real s. A periodic orbit itself has a complete flow regardless of the behavior elsewhere, so the periodic conclusions need no global completeness assumption.

## 2. The affine example in Remark D1(iii)

The draft uses

    U=[diag(s1,-1-s1,1)+vJ]y, s1=-1/2,

and claims circular backward limit sets in 0<c<1/2. Its horizontal carrier is

    B_h=(c-1/2)y_h+(v-omega)J y_h,

so every nonzero horizontal radius obeys d|y_h|/ds=(c-1/2)|y_h|. No nonstationary periodic circle exists, and the horizontal radius grows without bound backward. Also curl U=2v e3, so it is irrotational only if v=0. The claimed example is false.

A correct replacement, for every c>0 and omega!=0, is

    U=(-c y1,-c y2,2c y3), phi=(-c(y1^2+y2^2)+2c y3^2)/2.

This is the gradient of a harmonic quadratic. Every harmonic gradient is an exact profile with

    P=-(1-2c)phi-[(cI-omega J)y].grad phi-|grad phi|^2/2.

To verify the formula, differentiate [(Ay).grad phi], use Hess(phi)Ay+A^T grad phi and A^T=cI+omega J, and cancel terms in the momentum equation. Here B=(-omega J y_h,3c y3). Every nonzero horizontal circle at y3=0 has period 2pi/|omega|. For every point with y_h!=0 the backward limit is the circle at the same horizontal radius, since y3 decays backward while the horizontal angle rotates uniformly. This proves sharpness of the period bound within nondecaying exact profiles. It violates uniform sublinearity, so it is not a counterexample to the requested Liouville theorem.

## 3. Oseledets lines and quotient area in D2

Under the draft's compactly supported full-flow ergodic measure with B and Omega nonzero almost everywhere, apply the bounded-increment/logarithmic-coboundary argument in both time directions. It gives

    [log|Omega(phi_s x)|-log|Omega(x)|]/s -> 0,
    [log|B(phi_s x)|-log|B(x)|]/s -> 0

as s tends to either plus or minus infinity, almost everywhere. Thus the covariant lines R Omega and R B are the pure Oseledets lines of exponents 1+c and 0. The determinant gives the third exponent 2c-1. Forward growth alone would not justify identification with the pure Oseledets line: a vector can have components of smaller forward exponents. The two-sided argument closes that small presentation gap.

The quotient area expanded exactly by exp((1-2c)t) is the flux area form sigma=i_Omega vol on the local vortex-line quotient. For Euclidean quotient area the factor is instead

    exp((1-2c)t) |Omega(x)|/|Omega(psi_t x)|.

Indeed divide the full Jacobian exp(-3ct) by the stable-line length factor exp(-(1+c)t)|Omega(psi_t x)|/|Omega(x)|. On compact initial subsets of the vortical set and a common bounded forward-psi region, this yields the stated uniform lower area bound; it is not an exact Euclidean expansion law.

## 4. The missing limit-set hypothesis in D6

The entrance lemma proves the following. If K is a nonsingleton compact backward limit set of a precompact carrier orbit, and Omega is nowhere zero on K, then every carrier zero p in K has real spectrum

    {1+c,lambda2,lambda3}, lambda3<0<=lambda2,
    lambda2+lambda3=2c-1.

The proof needs late entrances toward p and late exits from a small neighborhood, supplied by the actual nonsingleton limit orbit. If both other eigenvalues had negative real part, p would be hyperbolic for -B with stable manifold equal to its vortex line. The compact vortical set meets that line only at p, whereas late entrances produce a different stable-manifold point in K, a contradiction. This is precisely A159, proved in auditor_proofs/proofs/nonlorenz_accumulation/PROOF.md.

An arbitrary nonsingleton compact invariant set need not supply any such orbit or entrances. For example, invariance alone does not exclude an isolated equilibrium component disjoint from the rest of the set. The draft's phrase 'or to any orbit in K accumulating on p' does not establish existence of that orbit. Restore K=alpha(a), nonsingleton, to the theorem. This check leaves the broader actual-Euler claim OPEN; it does not claim an Euler counterexample under the mandatory decay hypothesis.

## 5. Complete vortex lines in D5

The hypotheses for this section are H0, H1', c>0 and every finite omega. Put kappa=1+c and let Phi be the complete carrier flow. The frozen Omega flow is complete even though no global bound on Omega is assumed.

Fix a compact set E of initial points. All points Phi_-s(E), s>=0, lie in a common compact ball D by the radial trapping estimate. On a slightly larger ball the C1 vector field Omega has a common local existence time delta>0. Write chi for this local flow. For s>=0 and |tau|<=delta exp(kappa s), define

    z_s(tau)=Phi_s(chi_(exp(-kappa s)tau)(Phi_-s x)).

The exact Cauchy law D Phi_s Omega=exp(kappa s) Omega composed Phi_s gives z_s'=Omega(z_s) and z_s(0)=x. Uniqueness makes these solutions agree on overlapping intervals. Their intervals exhaust the real line. This proves completeness and the global conjugacy

    Psi_t chi_tau=chi_(exp(-kappa t)tau) Psi_t.

For a compact vortex segment, choose a sufficiently large backward-trapping ball containing it. Its images stay in that ball, and their lengths are at most M|tau|exp(-kappa t), where M bounds Omega on the ball. This proves contraction. On a compact regular hyperbolic set, the local vortex arc is therefore the local strong stable curve, by the local stable-manifold theorem and equal dimension. Iterating backward gives equality of the full strong stable curve with the complete vortex line. This supplies the missing completeness input to D5.12.

In the local coordinate map chi_tau(Psi_s gamma(r)), the first derivative column is -B, not B. Either sign gives invertibility; the correction does not change the inverse-function argument.

## 6. The survivor-disk argument in D5.10

Assume 0<c<1/2. Let C be a compact positive-volume set, forward invariant under Psi, lying in a regular level set where |Omega| and |B cross Omega| are bounded below. Its full invariant part is

    K=intersection_(n>=0) Psi_(nT)(C)

for any T>0. The nested compact sets Psi_(nT)(C) converge uniformly in distance to K. The latter is a nonsingular compact hyperbolic flow set. Its unstable line has rate a=1-2c, and its center-stable plane has rates 0 and -(1+c).

First choose T large enough that for f=Psi_T both the domination product and the inverse unstable norm are strictly less than one on K. The continuous splitting extends to a neighborhood N of K, and continuity preserves these strict estimates after shrinking N. Next replace C by C'=f^m(C) for sufficiently large m that C' is contained in N. This set is still compact, forward invariant, of positive volume, and has the same full invariant part K. The neutral flow line remains in the center-stable plane; no contraction of that whole plane is assumed.

The hypotheses of Alves-Pinheiro Theorem A are now met: the time-T map is C2, the splitting on C' is continuous and invariant/dominated on K, and the inverse norm on the extended unstable line is uniformly below one along every orbit in C'. A cutoff outside the relevant compact region extends the flow to a compact manifold without changing these statements. The theorem gives a local unstable interval D contained in K. It does not directly give the full unstable manifold through a point of D.

Choose p in the interior of D and a subsequence f^(n_j)p tending to q in K. For each fixed m>=0, f^(n_j-m)p tends to f^-m q. Expansion along D means that both intrinsic endpoint distances in f^(n_j-m)D tend to infinity. Thus these images contain a fixed-size local unstable interval about f^(n_j-m)p for all sufficiently large j. Continuous C1 dependence of local unstable manifolds and closedness of K give

    W^u_loc(f^-m q) contained in K,  for every m>=0.

Applying f^m and taking their union gives W^u(q) contained in K. Flow saturation then gives W^wu(q) contained in K. The point q is an accumulation point of forward images of D and need not lie in the original D.

This proves D5.10 and supplies the two missing reductions in its submitted proof. The actual primary manuscript is retained in in the team records; the statement on printed pages 3-4 was read again during this audit. The source's uniformly contracting center-stable variants are not applied to a flow time map.

## 7. Entropy on an individual regular basic attractor

Let A be one of the compact regular basic backward attractors constructed in D5.8. The lower entropy bound on the entire trapping core in D4 does not, by itself, imply the same lower bound on A. The missing argument is as follows.

On the backward unstable line define g(x)=|alpha_x(e^u_x)| for a unit vector e^u_x, where alpha=(B cross Omega).dy. The sign of e^u does not matter. Compact transversality makes g continuous, positive and bounded away from zero. Covector transport gives the exact unstable Jacobian

    J_t^u(x)=exp(at)g(x)/g(Psi_t x),  a=1-2c.

For the geometric unstable potential q^u=-d/dt log J_t^u at t=0, every full-flow invariant probability on A therefore has integral -a. The geometric-pressure theorem for a C2 basic attracting flow gives P(q^u)=0. Hence the variational principle gives

    0=P(q^u)=h_top(Psi_1|A)-a.

This is the precise use of Bowen-Ruelle Proposition 4.4(b); the actual manuscript and its relevant passages were independently checked in A085. The attractor is basic here because D5.8 proves local maximality, transitivity and dense periodic orbits. No use is made of a discrete-time hyperbolic theorem that would incorrectly discard the neutral flow direction.

One may instead include a separate elementary unstable-disk entropy argument, but D4 plus Ruelle alone is not the argument. The exact entropy conclusion remains valid with the proof above.

## 8. Potential convention and current model scope

The report uses

    H=P+|X|^2/2+c(c-1)|y|^2/2-omega Jy.X,
    X=cy+U.

If Htilde=P+|U|^2/2+((cI-omega J)y).U, then H=Htilde-a c|y|^2/2. On a leaf tangent to span(B,Omega),

    X.dy=-dH/a,
    U.dy=-d(H/a+c|y|^2/2)=-dHtilde/a.

Thus the potential -H/a is for X.dy. If the words velocity one-form mean U.dy, the quadratic correction must be included. This is solely a convention issue, but must not be carried into a numerical or integral identity with the wrong potential.

At the initial review, A233-A234 supplied an exact regular volume-form bracket model on the unmarked figure-eight exterior, conditional on P4 for Euclidean completion. A242-A246 have since supplied that marking and completion for every 0<c<1/2 and finite omega. Neither the resulting global regular model nor the singular model has W=curl U. The remaining question is actual Euler coupling; the Euclidean regular construction is no longer open.


## 9. Circle and finite-network edge cases

For omega=0 the harmonic example has B=(0,0,3c y_3). Its backward trajectory is (y_1,y_2,e^(-3ct)y_3), so it converges to a point, not a circle. For omega!=0 the horizontal rotation has exactly the circle limit previously stated. Thus the repaired example needs this explicit case split.

For a finite network, the full proof in the team records gives convergence to a node whenever the limit is contained in the network. It excludes a nonsingleton network as the whole limit, while permitting singleton nodes as limits on their null stable sets. Its return law concerns the derivative g' of the scalar passage map; integrating the positive lower derivative bound gives the displacement expansion.


## 10. A nonzero constant profile has zero core entropy

Statement. For every c>0, finite real omega and nonzero vector u in R3, let J(y1,y2,y3)=(-y2,y1,0), A=cI-omega J,

    U(y)=u,  P(y)=-((1-c)u+omega Ju).y.

These smooth fields solve the rotating profile equation

    (1-c)U+(cy+U-omega Jy).grad U+omega JU+grad P=0,
    div U=0.

They satisfy uniform sublinearity, but not U(y)->0. The carrier B=Ay+u has a singleton bounded-forward-orbit core and hence zero topological entropy on that core.

Proof. DU=0 and the displayed pressure cancels the two remaining constant terms. Since A is invertible, p=-A^(-1)u is the unique carrier zero. The carrier flow is

    Phi_t(y)=p+exp(tA)(y-p)=p+exp(ct)exp(-omega tJ)(y-p).

The rotation preserves length, so every y!=p escapes to infinity in forward time. Thus the core is {p}, and a map on one point has entropy zero. This proves the claim.

Consequently D4's theorem correctly assumes nonconstant U in its smooth branch, but its later assertion that every nonzero profile has positive core entropy is false under H1'. Replace it by the theorem's exact scope: nonconstant smooth U, or the separate C2 hypothesis that Omega has no zero on the core. Under the stronger decay hypothesis a nonzero constant is excluded, but that stronger hypothesis is not imposed in D4. No challenge to the actual D4 theorem follows.

Dependencies: direct differentiation and the explicit matrix exponential only. This is an exact counterexample to the prose generalization, not to the decay conjecture.
