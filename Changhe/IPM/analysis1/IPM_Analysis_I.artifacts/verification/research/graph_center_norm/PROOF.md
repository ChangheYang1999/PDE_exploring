# Central coefficient in the weighted H1 graph norm

## Statement and hypotheses

Fix L>0, 0<k<1 and0<alpha<1. Write r=|X| and

    m(r)=(r/L)^3(1+r^2/L^2)^((k-3)/2),
    w(r)=m(r)^(-2)(1+r^2/L^2)^(-3/2),
    ||h||_X^2=integral_R2 [h^2+r^2|grad h|^2] w(r) dX.

Weak derivatives are used. Assume a background rho and its canonical divergence-free velocity U[rho] satisfy the following bounds, for finite constants A,B,D and a real c_l:

    |grad rho| <= A r^(1+alpha),  |D2 rho| <= A r^alpha,   0<r<=1,
    |grad rho| <= D r^(k-1),      |D2 rho| <= D r^(k-2), r>=1,
    V=c_l X+U[rho] is C1 near the closed unit disk,
    V(0)=0, |V|<=B r and |DV|<=B there.

The norms on finite dimensional derivatives are Euclidean operator norms; increasing A,B,D covers any equivalent coordinate convention. The density is locally C^{2,alpha}, and its velocity has the needed local regularity on every compact set. The first two bounds near the origin follow from C^{2,alpha} and the strong cubic factorization when all Taylor coefficients of orders at most2 vanish. The global derivative bounds and the canonical velocity assumptions remain explicit hypotheses, not consequences of a generic growth bound on rho alone.

Put G=X dot grad rho. Define the full linearized expression

    Lh=V dot grad h-h+U[h] dot grad rho+(Sigma(h)/3)G,
    Sigma(h)=psi[h]_xy(0),  -Delta psi[h]=partial_x h,
    U[h]=(-partial_y psi[h],partial_x psi[h]).

For0<delta<=min(1,L) define

    h_delta=x^2 y (1-r^2/delta^2)_+^6.

It is C5 and compactly supported, with continuous even-even factor of value1 at0. Then G belongs to X, h_delta and Lh_delta belong to X, and

    ||h_delta||_X <= C delta,
    ||Lh_delta||_X <= C1 delta + C2 delta^(2+alpha)
                              +(delta^2/168)||G||_X.       (1)

Here the finite constants depend on L,k,alpha,A,B,D and the one fixed unit bump, not on delta. In particular both norms tend to zero. Its exact canonical strain is

    Sigma(h_delta)=delta^2/56.                            (2)

Let D_L be any linear perturbation domain containing these bumps and closed under their addition, on which h and Lh belong to X and the continuous center factor J(h) exists. Give it the graph norm ||h||_X+||Lh||_X. Every level {J=j} is dense in D_L with this norm. In particular J is not bounded in this graph norm, and imposing J=0 does not by itself give a closed normalized domain in that topology.

If a nonzero K in D_L satisfies LK=0, then no finite constant C can satisfy

    ||h||_X <= C ||Lh||_X  for all h in D_L with J(h)=0.   (3)

Indeed this is already false if J(K)=0, and otherwise the normalized sequence K-J(K)h_delta converges to K in graph norm. For an exact profile, the scaling candidate K=rho-X dot grad rho may supply such a kernel vector, but only if its canonical scaling identity, domain membership and center trace have separately been proved. This conditional observation is not an existence theorem and not an assertion that any numerical retained vector is a kernel.

## The weighted norm near the two ends

For0<r<=1 the weight is bounded above by C_w r^(-6). Forr>=1 it is bounded above by C_w r^(-2k-3), with a finite C_w depending on L,k. These follow directly from the displayed expression for w by comparison of1+r^2/L^2 with constants on the first region and with r^2 on the second. The bounds on rho give

    |G|+r|grad G| <= C A r^(2+alpha), 0<r<=1,
    |G|+r|grad G| <= C D r^k,         r>=1.

The corresponding radial norm integrals are bounded by constants times integral_0^1 r^(-1+2alpha) dr and integral_1^infinity r^(-2) dr. Both converge. Thus G belongs to X.

Write H(Z)=Z_1^2 Z_2(1-|Z|^2)_+^6, so h_delta(X)=delta^3 H(X/delta). Its derivatives are bounded by C r^2 and C r for the first and second derivatives when r<=delta; its value is bounded by C r^3. This follows from expanding H as a finite polynomial on its disk, where every term has degree at least3, and rescaling with r/delta<=1. The same bounds hold on the support boundary by C5 matching. Substitution in X with w<=C_w r^(-6) gives ||h_delta||_X<=C delta.

## Canonical velocity of the unit bump

Let chi(s)=(1-s)^6 for0<=s<=1, and zero afterwards. The density is

    H(r,theta)=r^3 chi(r^2)(sin theta+sin3theta)/4.

Its x derivative has only the stream modes sin2theta and sin4theta:

    partial_x H=f2(r)sin2theta+f4(r)sin4theta,
    f2=r^2 chi(r^2)+(r^4/2)chi'(r^2),
    f4=(r^4/4)chi'(r^2).                                  (4)

For n=2,4 let

    psi_n(r)=[r^(-n) integral_0^r s^(n+1) f_n(s) ds
                +r^n integral_r^infinity s^(1-n) f_n(s) ds]/(2n).

This solves the radial Poisson equation by direct differentiation and has no added singular or growing harmonic term. Since f2 is a polynomial in even powers starting at r^2 and f4 starts at r^4, both integrals give finite polynomials inside the unit disk, with no logarithmic resonance. Each term r^j sin(n theta) has j-n a nonnegative even integer, so the inner stream function is a Cartesian polynomial. Outside the disk it is a linear combination of r^(-2)sin2theta and r^(-4)sin4theta. The formula matches the value and first derivative at1; the source is C4, so the derivatives needed here also match.

Consequently the canonical velocity W=U[H] satisfies, for a finite constant C_H,

    |W(Z)|<=C_H |Z|,  |DW(Z)|<=C_H,       |Z|<=1,
    |W(Z)|<=C_H |Z|^(-3), |DW(Z)|<=C_H |Z|^(-4), |Z|>=1. (5)

The first bound uses W(0)=0, which follows from the polynomial stream modes and parity. The exterior bounds follow by differentiating the two explicit homogeneous modes. No general singular-integral regularity estimate is needed for this particular bump.

The canonical Green formula commutes with the dilation: U[h_delta](X)=delta^3 W(X/delta). In particular

    |U[h_delta]|<=C_H delta^2 r, |DU[h_delta]|<=C_H delta^2, r<=delta,
    |U[h_delta]|<=C_H delta^6 r^(-3),
    |DU[h_delta]|<=C_H delta^6 r^(-4),                      r>=delta. (6)

The strain identity from the same Green formula is the sin3theta density moment. Therefore

    Sigma(H)=(1/4) integral_0^1 r(1-r^2)^6 dr=1/56.

The dilation gives(2). The stream convention is fixed by -Delta psi=partial_x h and U=(-psi_y,psi_x); no affine strain is included.

## Bounds for the linearized image

The transport and multiplication terms are compactly supported. From the background bounds on V and DV and the bump derivative bounds,

    |V dot grad h_delta|<=C B r^3,
    |grad(V dot grad h_delta)|<=C B r^2, r<=delta.

Thus ||V dot grad h_delta-h_delta||_X<=C1 delta. Its weak derivatives have no interface measures because h_delta is C5 and V is C1.

For Q_delta=U[h_delta] dot grad rho, the product rule and(6) give bounds on |Q_delta|+r|grad Q_delta| by

    C A delta^2 r^(2+alpha),      0<r<=delta,
    C A delta^6 r^(alpha-2),      delta<=r<=1,
    C D delta^6 r^(k-4),          r>=1.                    (7)

For the first region the square norm is at most C delta^4 integral_0^delta r^(-1+2alpha) dr = C delta^(4+2alpha). For the second it is at most

    C delta^12 integral_delta^1 r^(2alpha-9) dr
       <= C delta^(4+2alpha)/(8-2alpha).

For the third it is at most C delta^12 integral_1^infinity r^(-10) dr=C delta^12/9. Since0<delta<=1 and0<alpha<1, this is also bounded by C delta^(4+2alpha). The product is locally C1 and its weak derivatives are the classical ones. The three estimates prove ||Q_delta||_X<=C2 delta^(2+alpha). Equation(2) bounds the remaining rank-one term exactly by(delta^2/168)||G||_X. This proves(1).

## Graph density and inverse consequence

For any h in D_L and any prescribed real j, set

    h_(delta,j)=h+(j-J(h))h_delta.

It belongs to D_L by the assumed linear-domain closure, and its central coefficient is exactly j. The difference tends to zero in graph norm by(1). Thus every level is dense within D_L. No density in a larger completion is asserted without an identification of that completion. In particular the sequence h_delta has coefficient1 and graph norm tending to zero, which contradicts any boundedness estimate for J.

If LK=0 and K is nonzero, then K_delta=K-J(K)h_delta has coefficient zero, ||K_delta||_X tends to the positive number||K||_X, and ||LK_delta||_X tends to zero. This contradicts(3). If J(K)=0 the constant sequence K already contradicts it. An equivalent image norm, or a row discretization not linked to X, is not automatically covered by this argument.

The actual scaling identity, when its hypotheses hold, gives LK=epsilon-X dot grad epsilon at a trial. It is zero only at an exact solution. At a trial the same normalized sequence converges to this particular nonzero image, which yields only a conditional limiting quotient, not a vanishing singular value. The claims concern the chosen X graph topology. Adding a norm that controls the factor or choosing another admissible inverse formulation can change the conclusion.

## Verification and limits

The proof is written before new computation. Independently reconstruct(4), the exact finite Green polynomials, matching jets, the strain1/56 and the exterior derivative exponents by two symbolic/rational methods. Check all elementary radial integral exponents and positive denominators. The finite constants C,C1,C2 need only existence for the topology conclusion; no candidate-specific numerical bound or nonzero kernel is claimed. Request actual Opus5.5 adversarial review of the graph-domain, near-origin weak derivative and nonlocal-tail arguments. All actual matrix spectra, global inverse constructions in other norms, physical forcing certificates and IPM endpoints remain OPEN.
