# Finite flat stream terms, pressure and local index

Audit status: independent reconstruction of LIT205, LIT207 and the finite-order part of CO50. The conclusions below are conditional on the stated finite regularity and Taylor hypotheses. They do not establish these hypotheses for an actual scattering tail.

## 1. Exact local statement

Fix 2/5<c<1/2 and any finite real omega. Let Jx=(-x2,x1,0), A=cI-omega J, X(x)=Ax, a=1-2c, b=2(1-c), q=b/a>6 and L=(1-c)I+omega J. Let x0 be a nonzero point and m>=2 an integer. On a neighborhood of x0 assume V is C^m, Pi is C^(2m), W=curl V and S=Pi-|V|^2/2. Assume the identities

    div V=0, -Delta Pi=tr((DV)^2),
    X.V=0, X cross W=aV,
    DV X=-LV, X.grad S=-bS, W.grad S=0.        (1.1)

Assume V(x0)=DV(x0)=S(x0)=0 and the first nonzero Taylor term V_m of V at x0 has degree m. Put ell=|X(x0)|>0, e3=X(x0)/ell and E=e3-perp. Use positively oriented Euclidean coordinates (t,s,z3) centered at x0. Then V_m is a planar divergence-free vector polynomial, independent of z3, and has the unique homogeneous stream polynomial psi of degree N=m+1 with

    V_m=(-psi_s,psi_t,0).                       (1.2)

The first conclusion is that psi must change sign on the unit circle in E. No isolation hypothesis is needed for this conclusion.

For the second conclusion suppose additionally that V_m(ξ)!=0 for every nonzero ξ in E. Then the projection of W along X onto E has an isolated zero at x0 and index at most zero. If x0 is on S^2, its index agrees with that of the angular tangential velocity Y(w)=V(w)-(w.V(w))w. The argument establishing this index conclusion already works for q>2 when the other local identities and a>0 hold. We retain the campaign parameters in the joint statement.

A leading polynomial that vanishes on a nonzero direction does not satisfy the second hypothesis, even if the complete vector field has an isolated zero. Tail smoothness alone does not supply finite order or this nondegeneracy.

## 2. Taylor control and the transverse stream polynomial

The terms of degree m-1 in DV X=-LV give partial_3 V_m=0. The terms of degree m in X.V=0 give e3.V_m=0. The leading divergence equation is div_E V_m=0. The polynomial one-form (V_m)_2 dt-(V_m)_1 ds is closed and has a homogeneous polynomial primitive of degree m+1, obtained by integration on radial segments. Its derivatives give (1.2). The homogeneous degree N>0 fixes its additive constant. Consequently

    W_(m-1)=(Delta_E psi)e3.                    (2.1)

Only finite regularity is needed. For j=0,1,2, Taylor's theorem and V in C^m give

    D^j V=D^j V_m+o(r^(m-j)), r=|x-x0|,

with the natural interpretation when m=2. Thus |V|^2 has a Taylor expansion through order 2m whose remainder, gradient remainder and Laplacian remainder are respectively o(r^(2m)), o(r^(2m-1)) and o(r^(2m-2)). Pi in C^(2m) has corresponding differentiated Taylor expansions. Hence S has the controlled finite expansion used below even though we have not asserted S belongs to C^(2m) on a neighborhood. This distinction justifies the weaker C^m/C^(2m) statement.

On E, define

    F=W-[(W.e3)/(X.e3)]X.                       (2.2)

The denominator is nonzero near x0. This field is transverse and satisfies X cross F=aV. The map F -> X cross F on the fixed plane E is injective and has a smooth inverse on its image. Therefore F is C^m there, has no term of degree below m, and

    F_m=(a/ell) grad_E psi.                     (2.3)

This also explains why the degree m-1 term of W does not survive the projection. If grad psi is nonzero off the origin, compactness of the unit circle gives |grad psi(ξ)|>=d|ξ|^m for some d>0. The remainder in (2.3) then makes F nonzero on a sufficiently small punctured disk and identifies its index with that of grad psi.

## 3. The first scalar term

The vector equation X cross W=aV and X.V=0 give the exact decomposition

    W=rho X-a(X cross V)/|X|^2,
    rho=(X.W)/|X|^2.

Combining the two scalar transport equations in (1.1) gives, without dividing by S,

    -a(X cross V).grad S=b(X.W)S.              (3.1)

Let H_l be the first nonzero term of the controlled expansion of S, if such a term exists for 1<=l<=2m. The degree l-1 term of X.grad S=-bS gives partial_3 H_l=0. The degree m+l-1 terms of (3.1), using X0=ell e3 and (1.2)-(2.1), yield

    grad psi.grad H_l=q H_l Delta psi.          (3.2)

For l<2m, the pressure equation implies Delta H_l=0: both tr((DV)^2) and Delta(|V|^2/2) start at degree 2m-2. The l=1 case is automatically harmonic. If all terms of S below degree 2m vanish, the same statements about invariance and (3.2) hold for H_2m, including if that polynomial is zero. Its Laplacian is instead determined by Section 4.

Write psi=r^N g(theta) and H_l=r^l h(theta) in E. Then (3.2) is

    g' h'=D_l h,
    D_l=q(N^2 g+g'')-Nl g.                     (3.3)

These are polynomial identities followed by identities of smooth trigonometric polynomials. Differentiating (3.3) does not require additional regularity of the original fields.

## 4. The pressure identity at degree 2m

If all lower scalar terms vanish, set H=H_2m. The planar derivative of V_m is R D^2 psi with R=[[0,-1],[1,0]], so

    tr((D V_m)^2)=-2 det D^2 psi.

The degree 2m-2 pressure equation is therefore

    Delta H=2 det D^2 psi-Delta(|grad psi|^2/2)
      =-(psi_tt-psi_ss)^2-4psi_ts^2
        -grad psi.grad Delta psi.              (4.1)

This identity is obtained from Delta(|grad psi|^2/2)=|D^2 psi|^2+grad psi.grad Delta psi. All terms are planar at this degree. At r=1 and any angle with g'=0,

    grad psi.grad Delta psi
       =N(N-2)g(N^2 g+g'').                    (4.2)

Indeed Delta psi=r^(N-2)(N^2 g+g'') and grad psi is radial at that angle. No sign of the full pressure is assumed.

## 5. An exact trigonometric derivative bound

For every real trigonometric polynomial T of degree at most N,

    ||T''||_infinity <= N^2 ||T||_infinity.     (5.1)

Here is the finite interpolation proof needed in Section 6. Set theta_j=pi j/N for 0<=j<2N and

    K(theta)=1+2 sum_(k=1)^(N-1) cos(k theta)+cos(N theta)
            =sin(N theta) cot(theta/2).

At multiples of 2pi the expression is interpreted by its continuous limit. Direct Fourier orthogonality on these 2N points proves

    T''(0)=(1/(2N)) sum_j T(theta_j) K''(-theta_j).  (5.2)

For |k|<N, the discrete sum selects exactly the frequency k with coefficient -k^2. For the highest cosine the two coefficients -N^2/2 add. The remaining highest sine has zero samples and zero second derivative at zero, so it also obeys (5.2). This verifies all modes, rather than applying an interpolation formula outside its dimension.

Let w_j=K''(-theta_j)/(2N). Differentiating the kernel, or its cosine sum at zero, gives

    w_0=-(2N^2+1)/6,
    w_j=-(-1)^j/[2 sin^2(pi j/(2N))], 1<=j<2N.

Every w_j(-1)^j is negative. Apply (5.2) to cos(N theta): its sampled values are (-1)^j and T''(0)=-N^2. Thus sum_j |w_j|=N^2, which proves (5.1) at zero by the triangle inequality. Translation proves it at every angle. This argument is exact; it uses no quadrature or numerical estimate.

If 0<=g<=M with M>0, apply (5.1) to g-M/2. At an angle theta0 of maximum,

    g=M, g'=0, -N^2 M/2<=g''<=0,
    K0=N^2 M+g''>=N^2 M/2>0.                  (5.3)

The restriction of a degree N homogeneous polynomial to the circle has trigonometric degree at most N, as required.

## 6. A one-sign stream term is impossible

Suppose psi does not change sign. Reversing the sign of psi in the homogeneous equations changes both sides of (3.2) by the same sign and leaves (4.1) unchanged. Hence assume g>=0 and g not identically zero. Use the maximum angle of (5.3). For every 1<=l<=2m=2N-2,

    D_l(theta0)=qK0-NlM>=NM(qN/2-l)>0,
    D_l(theta0)-j g''(theta0)>0, j=1,2.        (6.1)

The displayed strict inequalities hold for q>6 and N>=3.

If the first nonzero scalar term has l<2m, (3.3) at theta0 implies h(theta0)=0. A nonzero planar harmonic homogeneous polynomial of positive degree has angular part A cos(l theta)+B sin(l theta), so this zero is simple. Differentiate (3.3) once. Since g'=h=0 at theta0, it gives (g''-D_l)h'=0, contradicting (6.1) and simplicity. Thus all scalar terms of degrees below 2m vanish.

For H=H_2m, possibly zero, the same identity and its first derivative imply h=h'=0 at theta0. Differentiating twice leaves (2g''-D_l)h''=0, and (6.1) gives h''=0. Consequently Delta H(theta0)=(2m)^2h+h''=0.

But (4.2) equals N(N-2)M K0>0, since N>=3. Equation (4.1) gives Delta H(theta0)<0. This contradiction proves that psi changes sign. It includes semidefinite polynomials whose gradients vanish on whole lines.

## 7. The isolated-leading-term index and the weaker q>2 route

Assume grad psi has no zero on the unit circle. Its complex form is

    grad psi=e^(i theta)(N g+i g').             (7.1)

Now g and g' have no common zero, so every zero of g is simple. There are 2j such zeros for some integer j>=0. If j>=1, the winding number of N g+i g' is -j: the positive imaginary ray is met exactly at the j zeros of g with g'>0, and the argument derivative at each crossing is -N<0. If j=0, the expression stays in one open half-plane and has winding number zero. Thus

    index(grad psi)=1-j.                        (7.2)

In the campaign range Section 6 forces j>=1, proving index<=0.

For completeness, the local nonpositive-index theorem needs only q>2. Positive index in (7.2) would force g to have one strict sign. Take g>0 and an angle of minimum, so g'=0 and g''>=0. For 1<=l<=2N-2,

    D_l-j g''=N(qN-l)g+(q-j)g''>0,
    j=0,1,2.

The lower harmonic-term contradiction and the three equalities h=h'=h''=0 from Section 6 apply at this minimum. The pressure term (4.2) is again strictly positive, giving the same contradiction. This second argument does not need (5.1). It confirms the wider q>2 range stated in LIT205 without extending LIT207 beyond its audited hypotheses.

## 8. The angular index is the same index

Suppose x0 lies on S^2. On the sphere the projection of W along X is

    F_s=W-[(w.W)/c]Aw=-(a/c)(w cross Y),
    Y=V-(w.V)w.                                (8.1)

To verify this, use w.Aw=c, X.V=0 and X cross W=aV. Taking w cross (X cross W)=a w cross V gives X(w.W)-cW=a w cross V, which is (8.1). Multiplication by a nonzero real scalar and a quarter-turn both have positive determinant in two dimensions and preserve winding number.

The section E near x0 and S^2 are related by following the smooth X flow e^(tA), since X(x0).x0=c>0. The local hitting-time map is a smooth diffeomorphism. The homogeneity of V gives

    W(e^(tA)x)=e^(-t)e^(-omega tJ)W(x)
             =e^(-(1+c)t) D(e^(tA)) W(x).

Projecting to either transverse section removes the added X multiple from differentiating the hitting time. Thus the two projected fields are carried into each other by the derivative of the section map and a positive factor. Their local indices agree. Only local flow times are involved; neither global completeness of W nor a time change through its zero is required.

## 9. Conditional global closure when k is identically zero

Let U in C^2(R^3), P in C^1(R^3) solve the exact rotating profile equation

    (1-c)U+((Ay+U).grad)U+omega JU=-grad P,
    div U=0, U.curl U=0,

with 2/5<c<1/2 and any finite omega. Put p=(1-c)/c and assume, for some finite C,

    |U(y)|<=C(1+|y|)^(-p),
    |DU(y)|<=C(1+|y|)^(-p-1).

Let V,P2,W be the actual scattering tails and assume k=(Ax).V=0 throughout D=R^3 minus {0}. Let T0 consist of w in supp W on S^2 with V(w)=DV(w)=P2(w)=0. Suppose at every w in T0 there is an integer m>=2 for which V is C^m and P2 is C^(2m) near w, the first nonzero velocity Taylor term has degree m, and its restriction to (Aw)-perp is nonzero off the origin. Then U=0.

Here is the complete global reduction using already confirmed actual-tail results. The identity X cross W=aV and W=curl V imply supp V=supp W: an open zero set for W gives V=0, and an open zero set for V gives W=0. A1053 places the boundary of this support on S^2 in T0. At such a boundary point the extra Taylor assumption and Section 2 make the projected W nonzero on a punctured transverse disk. The homogeneity of W and the section map in Section 8 then give a punctured spherical neighborhood inside supp W. This contradicts the existence of complement points arbitrarily close to a support boundary. Hence the support has no boundary, and connectedness of S^2 makes it empty or the whole sphere.

If the support is empty, T0 is empty, and the already confirmed common-zero theorem A1057 gives U=0. Suppose the support is the whole sphere. The angular zeros of Y are exactly the zeros of V, because a radial V with X.V=0 satisfies c(w.V)=0. At a flat zero in T0, Sections 2,7,8 give isolation and index<=0. At a flat zero with P2!=0, the nondegenerate elliptic potential argument of A1050-A1052 gives isolation and strictly negative index; the option of local identical vanishing is incompatible with full support. At a vortical zero the actual profile correspondence A1018-A1020 gives index -1. A nonflat irrotational zero is absent by the original-flow nilpotence consequence A1107, since here Z=int{k=0}=D. Alternatively its transverse symmetric trace-free linearization would give index -1, which is sufficient for this argument.

Thus every zero is isolated. Their set is closed in the compact sphere; an infinite such set would have an accumulation point which is itself a nonisolated zero. Therefore there are finitely many. Poincare-Hopf gives total index 2, contradicting the nonpositive index of each zero. This proves the conditional global theorem.

The proof explicitly uses original-profile information at vortical zeros and in the common-zero theorem. Local vortical node germs which lack an original profile do not invalidate it.

## 10. Source comparison and model provenance

LIT205 Sections 1-9 and LIT207 Sections 1-6 were read in full and reconstructed above. Their smooth hypotheses imply the finite regularity hypotheses here. LIT205's isolated-leading-index and conditional global conclusions pass. LIT207's sign-change conclusion passes without an isolation assumption. No inference from sign change to an index bound is made in the degenerate-leading case.

The coordinator's in the team records, read in full, independently checks the finite-order calculation in Section 3 and states that C^m for V and C^(2m) for pressure suffice. Section 2 above verifies the differentiated Peano expansions needed for precisely that relaxation. Its CO50(a)-(b) agree with A1106 and A1108, and its Section 4 correctly keeps fixed-neighborhood o(tau) open. The additional under-N extension in A1109 is needed before applying the zero-derivative estimate at all possible boundary-Z points. The source correction retracting CO49's pressure-negativity inference agrees with A1081-A1082.

The coordinator agent is configured for the primary model. The received coordinator check is a focused model comparison, rather than merely an unanswered request. Runtime model identity remains unattested. The nested the external referee (a second model) source explicitly reports that its requested second-model consultation did not run; it is not counted as a model review. No new agent or model client was started in this agent.

## 11. Dependencies and remaining scope

The local argument is self-contained apart from elementary multivariable Taylor theory, winding numbers and basic local ODE flow facts. Its trigonometric inequality is proved explicitly. The global statement additionally uses A1018-A1020, A1050-A1053, A1057 and, optionally, A1107; their standalone proofs are indexed in the team records. Poincare-Hopf is applied to a C^1 angular field with a finite set of isolated zeros on the compact sphere.

The argument does not prove smoothness of the scattering tail from smoothness of U, does not exclude infinite-order flatness, does not control a sign-changing leading stream polynomial with nonisolated gradient, and does not close the branches where k is not identically zero. No assumption about analyticity of U is transferred to V. The unrestricted bare-decay, arbitrary-helicity, all-omega campaign conjecture remains open.

No numerical computation, formal proof build or prohibited execution is part of this proof. Exact source snapshots and post-read verification evidence are stored alongside it.
