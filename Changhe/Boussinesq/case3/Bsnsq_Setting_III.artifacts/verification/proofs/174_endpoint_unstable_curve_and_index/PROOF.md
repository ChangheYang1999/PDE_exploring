# Strong unstable flatness, endpoint curvature, and the index of a zero arc

Status: independently derived conditional theorems. Exact controls and the audit of the lead's proposed item 4.7(xiii) are to be recorded in verification/. Neither the incoming nor the accumulating endpoint case is excluded for general smooth B2 profiles.

## Statements and hypotheses

Use the oriented physical plane, curl W = partial_x W2 - partial_y W1. Assume smooth fields satisfying

    div W=4, Omega=-curl W,
    W.grad Theta=0, (W.grad+1)Omega=Theta_x.             (1)

Let p be an endpoint of a smooth zero half-arc gamma, with Theta(p)=L, every derivative of Theta-L and Omega zero at p, and DW(p)=4n tensor n. Use orthonormal coordinates (s,z), centered at p, with the s direction tangent toward p and away from gamma, and n the positive z direction. Assume gamma is the end of its connected zero component. The normal nullcline is z=k(s), k(0)=k'(0)=0. The reduced tangential function f(s)=W_s(s,k(s)) is zero for s<=0 and flat at0. If f is strictly positive or strictly negative just beyond0 the endpoint is called outgoing or incoming; otherwise exterior zeros accumulate at p. Coordinates here remain fixed physical orthonormal coordinates, not a nonlinear change of the forcing direction in (1).

The following assertions hold.

1. Every ambient derivative of Theta-L and Omega vanishes on the local strong unstable curve C of p. No endpoint type is needed.
2. If C enters s>0 arbitrarily close to p, it is impossible that W(0,z) is real analytic for |z|<delta and that Omega(s,z) is real analytic in z on that same connected interval for each 0<s<delta. W can be replaced by the B2 velocity U in this trace assumption because their difference is affine.
3. Write C as s=sigma(z). Its entire formal Taylor series is determined by the formal Taylor series of gamma at p. If kappa is the signed curvature of the arc with respect to n, with arclength increasing toward p, then

       sigma(z)=kappa'(0) z^3/18+O(z^4).               (2)

   In particular kappa'(0)!=0 implies the geometric premise in item2. This is a statement about jets. No convergence of the formal series, analyticity of gamma, or nonflatness when kappa'(0)=0 is asserted.

For the global conclusions assume additionally that gamma is the compact embedded zero-arc component containing0, DW has eigenvalues0,4 at every interior point, neither endpoint is accumulating, W(X)=2X+o(|X|) as |X| tends to infinity, W(SX)=S W(X) with S(x,y)=(-x,y), gamma intersects the axis only at0, and DW(0)=diag(0,4). These geometric hypotheses are independently established earlier for the beta-two B2 setting and are made explicit here.

4. Gamma is an isolated compact zero set. Its degree is (epsilon_-+epsilon_+)/2, with epsilon=+1 for outgoing and -1 for incoming. Reflection makes the endpoint types equal. Two incoming endpoints force degree2 in the complement of an isolating tube around gamma inside a sufficiently large disk, hence other zeros at positive distance from gamma.
5. In the two-incoming-endpoint case, if every other zero is isolated, there are finitely many. Their indices belong to{-1,0,+1}, and N_+1-N_-1=2. At least one index+1 zero lies in x>0, with its mirror in x<0. Every isolated index+1 zero of a coupled field (1) is a source: a full neighborhood has backward trajectories converging to it, Theta constant and Omega zero.

## Infinite-order propagation on the strong unstable curve

Put h=X-p and M=4n tensor n. The local strong unstable curve can be constructed without a center manifold. Write W(p+h)=Mh+N(h), N=O(|h|^2). In the Banach space with norm sup_(t<=0) e^(-4t)|h(t)| solve

    h(t)=r e^(4t)n + int_(-infinity)^t
             [P0+e^(4(t-v))P4] N(h(v)) dv,             (3)

where P4=n tensor n and P0=I-P4. Both integrals of a quadratic bound O(rho^2 e^(8v)) give O(rho^2 e^(8t)). The derivative of the nonlinear map has norm O(rho). On a small ball this is a contraction, depending smoothly on r: every derivative of order at least2 inserts at least two exponentially decaying variations, and the first derivative contains DN=O(rho e^(4v)). Differentiation under the integral is therefore justified at every fixed order. Invert I-D of the contraction by its norm-convergent Neumann series. This proves smooth dependence, not merely formal dependence. It is the special case lambda=0 of the full parameter proof in173.

Denote the solution with parameter r by h^(r). It has h^(r)(t)=r e^(4t)n+O(r^2 e^(8t)). Time-shift uniqueness proves invariance and identifies C={p+h^(r)(0)}. Its sufficiently short backward orbits remain in one fixed compact neighborhood and satisfy

    |phi_(-T)(q)-p| <= C_q e^(-4T).                   (4)

For each fixed m, all derivatives of phi_(-T) of order1 through m, evaluated at q in C, are at most C_m exp(K_m T). The first variation follows by Gronwall with bounded DW on the compact neighborhood. Every higher variation has the same linear equation plus products of lower variations and bounded higher derivatives of W. Induction, enlarging K_m to absorb any polynomial time factor, proves the bound. The neighborhood of q on which a finite-time flow is defined may shrink as T grows; its derivatives at q obey the stated bounds.

For each finite T, thermal transport is the identity of germs

    Theta-L=(Theta-L) composed with phi_(-T).

At q, any derivative of order m is a finite sum of derivatives of Theta-L at phi_(-T)q multiplied by flow derivatives. Flatness at p makes each such field derivative O(|phi_(-T)q-p|^N), for every N. Equation(4) dominates the exponential growth of all flow factors on choosing N sufficiently large. Letting T tend to infinity proves all ambient thermal derivatives zero at q.

The exact finite-time vorticity identity is

    Omega=e^(-T) Omega composed with phi_(-T)
          + int_0^T e^(-t) Theta_x composed with phi_(-t) dt.       (5)

Every derivative of its integrand at q is zero, because phi_(-t)q belongs to C and all thermal derivatives vanish there. The first term and all its derivatives tend to0 by the same arbitrary-order flatness argument for Omega. This proves item1, including points on either local branch of C and all three endpoint types. Values along the curve alone would not suffice for the analyticity argument; the proof gives ambient derivatives.

## Analytic transverse data and a positive-side crossing

The curve C has graph s=sigma(z), sigma(0)=sigma'(0)=0. Given the delta of the hypotheses, choose z_* sufficiently small with a=sigma(z_*)>0, also a<delta and |z_*|<delta. The intermediate value theorem makes every 0<s<a equal sigma(z_s) for some z_s between0 and z_*. At that point every z derivative of Omega(s,.) vanishes by item1. Real analyticity makes it zero near z_s, and the identity theorem on the stipulated common connected interval makes it zero throughout |z|<delta. Thus curl W=0 on a positive half-rectangle.

Constant divergence implies both components of W are harmonic there. The analytic value trace alone suffices to extend this restriction through s=0. If w0(z) is one component's trace, its holomorphic extension gives the real harmonic extension

    A(s,z)=[w0(z+i s)+w0(z-i s)]/2.

The function W_j-A has zero boundary trace on s=0. Its odd reflection is harmonic on a smaller full rectangle. One direct justification uses the original smoothness up to the line: tangential derivatives of the zero trace vanish, harmonicity gives the second normal derivative zero there, and odd reflection is C2 and harmonic. Its analytic extension therefore has the same full jet as the original smooth W at p.

The analytic implicit function theorem gives its analytic normal nullcline. On s>0 this is k(s) by uniqueness. Its analytic reduced tangential field has the Taylor series of the flat function f and hence vanishes near0. The actual W therefore vanishes on this graph for all sufficiently small positive s. This extends the same connected zero component through p, a contradiction even in the accumulating case. The extra crossing premise is essential to this argument; if C stays in s<=0, no zero point of Omega on a positive-side transverse line has been supplied.

## Formal uniqueness and the cubic coefficient

Because curl W is flat at p, the formal jet of W is a gradient grad H; this follows by integrating the closed formal one-form coefficient by coefficient. Set H(p)=0. Its formal Laplacian is4. The formal jet of gamma is a zero curve of grad H, and H is zero on it. In graph coordinates d=z-k(s), put P(s,d)=H(s,d+k(s)). The formal equation becomes

    (1+k'^2) P_dd -2k' P_sd +P_ss -k'' P_d=4,
    P(s,0)=0, P_d(s,0)=0.                             (6)

The coefficient 1+k'^2 is an invertible formal series. Comparing powers of d determines each next coefficient of P from the preceding ones. This proves uniqueness of the formal H and hence of the W jet from the arc jet. It invokes no convergent Cauchy problem.

Write k(s)=k0 s^2/2+k1 s^3/6+O(s^4). Here kappa'(0)=k1 because k'(0)=0 and the arclength speed is1 at0. The degree2 through degree4 terms forced by(6) are

    H2=2z^2,
    H3=-2k0 s^2 z+(2k0/3)z^3,
    H4=(k0^2/2)(s^4-6s^2z^2+z^4)
                         -(2k1/3)(s^3z-sz^3).        (7)

They have Lap H2=4 and Lap H3=Lap H4=0. Substituting z=k(s) makes both components of their gradient zero through cubic order. The remaining terms of H start at degree5 and cannot affect the cubic invariance calculation.

Let sigma(z)=a2 z^2+a3 z^3+O(z^4). Curve invariance says

    W_s(sigma(z),z)=sigma'(z) W_z(sigma(z),z).

Using(7), the left side has no quadratic term and cubic coefficient -4k0 a2+2k1/3. The right side has quadratic coefficient8a2 and cubic coefficient12a3+4k0 a2. Therefore a2=0 and a3=k1/18, proving(2). At every higher order m, the unknown coefficient of sigma enters as4m times that coefficient on the right; the left has no linear W_s term. All other terms have been fixed at earlier orders. This proves the assertion about the whole formal jet.

As a check in signed-distance coordinates (xi,d) about an arclength curve, Lap H=4 gives H=2d^2+(2/3)kappa(xi)d^3+O(d^4). A gradient trajectory has dxi/dd=H_xi/[(1-kappa d)^2 H_d]=kappa'(0)d^2/6+O(d^3) when it starts at p. Integration gives xi=kappa'(0)d^3/18+O(d^4). Conversion back to Cartesian s,z preserves this cubic coefficient. Equation(7) is the independent Cartesian derivation used for the check, so the result does not depend on a sign convention left implicit in Fermi coordinates.

## Degree of the compact arc

At each interior point the rank-one derivative has a regular normal component. Its nullcline is a unique smooth curve and is filled locally by gamma; there are no other nearby zeros. The nonaccumulating endpoint hypotheses give the same local isolation there. A finite cover and compactness isolate all of gamma from the remaining zero set.

Extend an arclength parametrization a little past both ends and use an oriented thin tubular chart F(a,b). Pull back the vector field by DF^(-1). At points of the zero arc its derivative has normal component derivative4. Uniform implicit inversion gives the normal nullcline b=k(a) throughout a short extended tube. As a map for computing degree, substitute t=b-k(a) and write it as

    (f(a)+d(a,t)t, c(a,t)t), c>0.                     (8)

The substituted second component is not asserted to be the time derivative of t. This is a map homotopy, not a dynamical-coordinate identity. The signs of f at the left and right ends are respectively -epsilon_- and epsilon_+. To identify these signs with exterior center drift, keep the genuine coordinates (a,b) before substituting t. Write a finite C4 center manifold as b=n(a), and put t=n(a)-k(a) only after evaluating the field there. Its true invariance equation is c(n-k)=n'(f+d(n-k)). Thus n-k=n'f/(c-n'd), and its tangential velocity is P=f+d(n-k)=cf/(c-n'd). Here n' is the derivative of b=n(a), not of n-k. The local center manifold contains all nearby equilibria by the complete-orbit property of the finite center-manifold theorem. At the endpoint n'=0 because the center direction is tangent to the arc; hence c-n'd stays positive on a short chart. This proves the sign identification and invariance of the endpoint type under changing charts. The actual time derivative of t would be ct-k'(f+dt); it is not used as ct.

Homotope(8) to(f(a),t) by replacing d with(1-v)d and c with(1-v)c+v, 0<=v<=1. A zero on the boundary is impossible: the second component excludes the horizontal sides, while at a vertical side its only zero is t=0, where f is nonzero. The oriented domain chart and shear preserve degree. Multiplication by DF^(-1) also preserves degree: it extends over a contractible rectangle into GL+(2), and can be contracted to a positive-determinant constant matrix without creating a boundary zero. Product degree now gives

    ind(gamma)=[sgn f(right)-sgn f(left)]/2
              =(epsilon_-+epsilon_+)/2.              (9)

Sublinear velocity makes W dot X positive on all sufficiently large circles, so the straight homotopy to2X proves degree1 on a large disk. Since gamma is the connected zero component containing the reflection-fixed origin, reflection maps gamma to itself; it does not produce a second arc. It preserves the outward endpoint direction and incoming/outgoing type. Hence two incoming endpoints give ind(gamma)=-1, and additivity gives degree2 outside the isolating tube. This forces additional zeros, without needing their isolation.

## Isolated exterior zeros, the axis, and sources

For the rest of this paragraph assume both endpoints are incoming. If all exterior zeros are isolated, they form a compact discrete set: the arc has a zero-free separating tube and all zeros lie in a large disk. A compact infinite set would have an exterior accumulation point, so this set is finite. At any isolated zero, trace DW=4. If DW is invertible its index is sign det DW. If singular its distinct eigenvalues are0,4; eliminating a regular normal component reduces the local degree to a scalar function with no zeros on either punctured side. Its degree is one of-1,0,+1. Degree additivity proves N_+1-N_-1=2.

Set b(y)=W2(0,y). Its total one-dimensional degree is1 since b(y)=2y+o(|y|). The origin contributes1 because b'(0)=4. Thus all exterior axis indices sum to0 in one dimension. At an axis zero, parity gives DW=diag(a,b'), a+b'=4. Its planar index is at most its one-dimensional axis index. If both diagonal terms are nonzero and b'<0, then a>0 and both indices are-1; if b'>0 the planar index is at most+1. If b'=0, then a=4 and W1=x A with A>0, so reduction to W1=0 is exactly reduction to the axis and the two indices agree. If a=0, then b'=4 and the axis index is+1, an upper bound on the planar index. The planar indices of exterior axis zeros therefore sum to a nonpositive integer. Reflection preserves each isolated point's index (one orientation reversal in domain and one in range). Thus the total index in x>0 is at least1, forcing a point of index+1 there.

It remains to check the source claim, including a singular derivative. In the invertible case, differentiated transport gives DW(q)^T grad Theta(q)=0. Hence grad Theta(q)=0, and (1) at q gives Omega(q)=0. Therefore DW(q) is symmetric. Positive determinant and trace4 make it positive definite. On a sufficiently small ball (X-q) dot W(X)>=c|X-q|^2. Every backward trajectory in that ball remains there and converges to q.

In the singular case the eigenvalues are0,4. Use a finite C4 center manifold and the smooth strong unstable curve, which are transverse, to choose local coordinates sending them to v=0 and u=0. This is an explicit use of the finite-regularity local center-manifold theorem, not an assertion of a smooth center manifold. For example, Podvigina, The center manifold theorem for center eigenvalues with non-zero real parts, arXiv:physics/0601074v1, Theorem3, gives a local C4 invariant graph. The primary PDF defines alpha_+=alpha_-=0 for center spectrum{0}, beta_+=4, and beta_-=infinity for the empty stable spectrum. For k=4 its two inequalities are exactly0<4/4 and0<infinity. Apply the theorem to the smooth local vector field after centering q; a smooth cutoff extends that local field for the theorem stated on R^2. The nonlinear remainder after subtracting DW(q) has value and derivative zero. Its C4 graph flattening yields a C3 transformed field, sufficient for the two Hadamard divisions and bounded coefficients below. Invariance and Hadamard division give

    u'=g(u)+uv B(u,v), v'=v D(u,v), D>2, |B|<=M.      (10)

The local degree is that of g. Index+1 and isolation give g(u)/u>0 for u!=0 sufficiently small. In backward time T, |v|<=|v0|e^(-2T). For k>M/2 the small neighborhood

    |v|<epsilon, |u| exp(k|v|)<delta

is backward invariant, since away from u=0

    d/dT [log|u|+k|v|]
       =-g(u)/u-vB-kD|v| <= (M-2k)|v| <=0.

The sign of u is preserved. Put w=|u| and multiply it by exp(int_0^T v B dt). Its derivative is -exp(int vB) g(u) sgn(u), strictly negative for u!=0. The exponential has a finite positive limit since |v| is integrable. Thus w has a limit. A positive limit would place |g(u)| above a positive constant eventually and force the nonnegative multiplied quantity to decrease at a fixed positive rate forever, which is impossible. Hence u,v tend to0. The case u=0 already follows from the v estimate. This proves a full backward-attracting neighborhood in the singular case too.

In either case transport and continuity make Theta=Theta(q) throughout this neighborhood. Every backward orbit stays in a compact local set. Equation(5) then reduces to Omega=e^(-T)Omega composed with phi_(-T); boundedness yields Omega=0. The word source refers to this local backward-attracting property, including degenerate sources, not necessarily exponential convergence in the center direction.

## Scope, dependencies and controls

Dependencies are the displayed smooth local field hypotheses, the previously audited B2 zero-arc geometry (45), the contraction theorem with estimates given here and in173, finite-dimensional flow variational equations, elementary degree and the finite C4 center-manifold theorem. The argument neither promotes finite jets to analytic solutions nor imposes a boundary, a second reflection, fixed physical center, or a free strain. Index+1 sources are compatible with local coupled equations: for epsilon>0 the local gradient field of H=2y^2+epsilon Re(x+i y)^4 has div4, curl0, a degenerate isolated source at0, and satisfies(1) with constant Theta. It has no required B2 center jet and is not a global profile. This example confirms that the index restriction itself is not a contradiction.

Planned exact controls: independently solve the degree4 harmonic polynomial coefficient equations and the cubic invariance equation; verify formal graph-coordinate Laplacian, symbolic source and axis-index cases, transport signs and the local degenerate harmonic example. Model advice will be checked against this proof and those controls. No Lean or Lake is run, and numerical evidence is not used to prove these analytic assertions.

Written UTC 2026-10-21T14:05:24.677632+00:00, before the new exact controls.
