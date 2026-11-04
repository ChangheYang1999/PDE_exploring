# Exact regular suspension on an unmarked figure-eight exterior

## Exact statement

Fix 0<c<1/2. Put lambda=1+c, mu=1-2c, delta=3c, K=(3+sqrt(5))/2, r=lambda/mu>1 and T=log(K)/mu. There exist a smooth compact oriented three-manifold N, smooth vector fields B,W on N, and a smooth positive volume form m such that

    div_m B=3c,     div_m W=0,     [B,W]=-(1+c)W.

Both fields are nowhere zero and independent. The field -B points strictly inward on the boundary. Its maximal invariant set is a nontrivial transitive hyperbolic attractor with rates -(1+c), 0, and 1-2c. It is the constant-roof suspension of the surface attractor in the team records. The underlying manifold N is diffeomorphic to the unmarked figure-eight knot exterior.

Here an unmarked exterior means that no particular boundary curve has yet been identified with the knot meridian. In particular this theorem does not verify the transverse-meridian condition of the Euclidean completion theorem. The identities use m, not a preselected Euclidean volume. No field U with W=curl U is constructed. There is no Euler counterexample or Liouville conclusion.

## 1. Exact tensors and smooth boundary

Take M,F,D,S,f,Y,eta and the source p from the analytic surface construction. Let nu be the area form defined by i_Y nu=eta on S. Since d eta=0,

    div_nu Y=0,     f*nu=K^(1-r)nu=exp(-delta T)nu.

Every point of M\{p} has a positive forward iterate in int(S). Indeed points of the attractor already lie there; for points in its complementary ribbon this follows from intersection F^(-n)(D)={p}, with strict trapping excluding a boundary-only exception. Extend the tensors to M\{p} by

    Y_x=exp(-lambda nT)(DF_x^n)^(-1)Y_(F^n x),
    eta_x=K^(-n)((F^n)*eta)_x,

whenever F^n x lies in int(S). The exact identities on S make these definitions independent of n. They are smooth on an open cover. The extension of eta agrees with the original global eta. Extend nu accordingly. All tensors now obey the required covariance under F throughout M\{p}.

In the suspension with relation (z,t+T)~(Fz,t), define

    X=partial_t,    B=-partial_t,
    W=exp(lambda t)Y,
    m=exp(-delta t) dt wedge nu.

Under (z,t)->(Fz,t-T), the factors exp(-lambda T) in DF(Y) and exp(-delta T) in F*nu cancel the displayed weights exactly. The fields and volume therefore descend smoothly with all derivatives. Direct differentiation gives div_m B=delta, div_m W=0 and [B,W]=-lambda W. The two fields are independent since one has a nonzero time component and the other is tangent to the surface.

For completeness, a smooth strictly transverse trapping boundary can be chosen as follows. The annulus S\int(fS) joins the inner circle f(partial S) to the outer circle partial S. Choose a smooth outward annular vector field V, with its inner and outer collar germs related by F_*V=V. Positive radial components permit interpolation between those collar germs. Rescale V so every crossing time L(theta) is less than T. In its trajectory coordinates, slow it by the factor 1+(T-L(theta)) beta(theta,s), where beta is a smooth nonnegative interior bump with integral one on each crossing arc. Now every crossing time is exactly T, and the collar germs are unchanged.

Let C_t be the image of the inner circle at time t, and let S_t be the once-holed-torus region bounded by C_t containing fS. Then S_0=fS, S_T=S, and S_t increases. Set

    N={(z,t):0<=t<=T, z in S_t}/((z,T)~(fz,0)).

The collar covariance makes the boundary smooth across the seam. In a boundary crossing coordinate s(z), its inside is t-s(z)>=0. Thus X(t-s)=1: -B=X is strictly inward. This construction replaces the corner boundary of the ordinary embedding quotient by a smooth annular sweep; it does not alter its topology or peripheral homotopy classes.

The phase-zero section of the maximal invariant set is intersection f^n(S). The exact stable and unstable multipliers of f are exp(-lambda T) and exp(mu T), so the suspended flow has the stated rates. Transitivity of a constant-roof suspension follows by letting the dense base orbit meet each base open set and using the intervening continuous time to reach each required phase interval.

## 2. The embedding quotient and its complementary solid torus

Consider first

    Q_f=(S times [0,1])/((x,1)~(fx,0))

inside the closed torus bundle Q_F obtained by suspending F on M. This is a genuine compact three-manifold with boundary corners. Near f(partial S) at the seam, a two-dimensional transverse section is one half-plane joined to one quadrant along a half-axis, hence a sector of angle 3pi/2. It is a topological half-plane, with no branching. Its product with the boundary-circle coordinate gives the local manifold chart. The boundary consists of two annuli, one vertical and one at the seam, and is a torus.

The closed complement is the embedding quotient of the disc map g=F^(-1)|D:D->int(D), with time reversed. Its nested images shrink uniformly to p. To identify this quotient, choose a homeomorphism from D\int(gD) to a round annulus, prescribing compatible boundary values under g and a fixed radial contraction z->qz. Extend inward by the iterates of g and q. Uniform shrinking makes this extension and its inverse continuous at the centre. It conjugates g to the radial contraction.

The quotient for that radial contraction is a solid torus whose core is the suspended fixed point. One may see it in the quotient of R^2 times R by (z,t+1)~(qz,t), trivialized by a continuously rescaled plane coordinate. The annular fundamental-domain construction also shows that the complement of the core in this solid torus is a torus collar. Thus Q_f is a compact core of Q_F minus the source orbit. The smooth annular boundary sweep in Section 1 gives the same compact exterior: the swept collar is contained between the two successive boundary tori furnished by S and fS, and straightening that annular collar identifies their interiors and boundary tori.

## 3. Identifying the unmarked exterior

Deleting the source orbit from Q_F gives the mapping torus of F on the once-punctured torus M\{p}. The map F fixes p and acts on H1 by A=[[2,1],[1,1]]. The mapping class group of a torus with one marked point, equivalently one puncture, is SL(2,Z), detected by this homology action. Therefore the punctured-torus monodromy has class A.

The mapping torus of this punctured-torus class is the figure-eight knot complement. This particular identification, and the mapping-class identification just used, are stated in the actual Bonahon-Wong-Yang manuscript retained in the team records: page 1 and the start of Section 2 on printed page 3. The matrix is the product of the two opposite Dehn-twist generators in its convention. The retained manuscript is arXiv:2203.05730v1, dated 14 March 2022; the title and the relevant passages were inspected, not inferred from an abstract.

Taking compact cores across the torus collars gives the homeomorphism with the compact figure-eight exterior. Rounding the displayed smooth corners and using uniqueness of compatible smoothing in dimension three gives the same diffeomorphism type. No assertion about a specified boundary slope is part of this identification.

## 4. Why the meridian remains separate

A circle around the puncture in a fibre is the meridian of the deleted source orbit in the closed torus bundle. Under the figure-eight-complement identification it is the fibre boundary, hence the knot longitude. Confusing these two meridians would invalidate the completion argument.

Also, degree one in the suspension-time direction specifies a homology class in the exterior but does not specify a unique boundary slope: meridian plus any integer multiple of longitude has that same exterior homology class. Thus that degree alone is insufficient.

The surface map f can be extended from fS to a boundary-preserving self-diffeomorphism h of S. On the complementary annulus, one can modify h by arbitrary boundary Dehn twists, leaving a neighborhood of the attractor unchanged. The relative-boundary mapping class group has the boundary-twist central extension described on printed pages 1-2 of the actual Levitt 2002 manuscript in the team records. Selecting a standard monodromy for this auxiliary h is not a proof that the original exact tensor boundary foliation has a transverse meridian.

A valid way to finish that extra step would be to identify an actual compact boundary leaf as meridional and compute its nonunit holonomy, then apply in the team records. Neither the unmarked topology nor the exact multipliers alone identifies that slope here.

## Dependencies and evidence

- in the team records: explicit smooth exact surface triple and source basin.
- in the team records: the earlier conditional seam and boundary argument, now supplied with its surface input.
- in the team records: inspected team topology argument.
- in the team records: hashes and retrieval times for the actual primary sources.

The remaining external topological ingredients are the standard marked-torus mapping-class theorem, the cited figure-eight monodromy identification, annulus extension, and three-dimensional smoothing uniqueness. No computation is used as evidence for a topological claim. The pending meridional issue and all Euler self-consistency conditions remain outside the theorem.
