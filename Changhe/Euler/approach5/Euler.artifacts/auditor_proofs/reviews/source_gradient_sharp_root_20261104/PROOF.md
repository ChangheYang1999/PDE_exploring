# Spherical geometry and discrete equality in the source-gradient bound

## 1. Exact theorem and scope

Let the rotation matrix J send (y1,y2,y3) to (-y2,y1,0), and let e3=(0,0,1). Let U in C1(R3;R3) be divergence-free, with E(R)=integral_(B_R)|U|^2 and E(R)/(LR^beta)->1, where L>0 and0<beta<1. Set

    t=(beta-3)/2, k=t+2=(beta+1)/2, m=2-beta,
    K_beta=beta m(1-beta),
    H_beta=t^2(k^2+4)/(k^2+2), x_star=k^2/(k^2+2).

Write U_T=U-(U.n)n with n=y/|y|. On1<|y|<R let F be the integral of r^(-beta)|U|^2, T that of r^(-beta)|U_T|^2, and G that of r^m|DU|_F^2. Put q=tr((DU)^2), Q(r)=integral_(S2)q(rn), J(R)=integral_1^R r^(4-beta)[Q(r)]_+dr, and I(R)=integral_(1<r<R)r^m[q]_+. Suppose limsup G/(beta L log R)<=M<infinity. The separately confirmed localized Hardy theorem A3125 implies M>=H_beta. Define

    A=M+4beta-2,
    d(M)=2k^2/[A+sqrt(A^2-8beta k^2)].

Then liminf T/(beta L log R)>=d(M) and liminf J/log R>=K_beta L+m beta^2 L d(M), with the same source bound for I. Every fixed center has the same result with its own gradient premise and tangent planes.

For Lambda=ell(ell+1), ell=1,2,..., put

    x_ell=k^2/(Lambda+k^2),
    M_ell=t^2+Lambda(Lambda+t^2-2)/(Lambda+k^2).

There is a smooth decaying solenoidal field with exact origin energy LR^beta for R>=2, energy LR^beta+O_a(R^(beta-2)) at each fixed center, and

    T_a=beta L x_ell log R+O_a(1),
    G_a=beta L M_ell log R+O_a(1),
    J_a=[K_beta L+m beta^2 L x_ell]log R+O_a(1).

Here d(M_ell)=x_ell, so the tangential and spherical-source inequalities are optimal at those discrete M values, including M_1=H_beta. The fields have smooth Poisson pressures but fail full rotating Euler for all real c,omega. No optimality at intermediate M or for pointwise I is asserted in this theorem; the later LIT383 claim has a separate review. The input LIT38136f87758, all eight sections,58 checks and support note, is retained in verification. The full existing C comparison of09:45:54Z is checked in Section9.

## 2. The full spherical identity

Write z=log r and U=r^t v=r^t(f n+w), with w tangent. Direct differentiation gives

    f_z+kf+div_S w=0,
    F=integral|v|^2, T=integral|w|^2,
    G=integral(|v_z+t v|^2+|nabla_S v|^2),

where the last derivative acts on Cartesian components, and the integrals run over0<z<log R and S2 with ordinary area measure. In a unit tangent direction e the normal and tangential derivatives are (e(f)-w.e)n and f e+D_e w. Their squared sums integrate to

    integral|nabla_S v|^2
      =integral[|grad_S f|^2+2f^2+|D_Sw|^2+|w|^2-4grad_S f.w].

The two cross terms before integration are -2grad f.w and2f div w. Their integrals combine to the displayed -4 term. The integrated one-form identity on the unit sphere is

    integral(|D_Sw|^2+|w|^2)
      =integral[(div_Sw)^2+(curl_Sw)^2].

One obtains it by integrating the divergence and curl squares and commuting the two covariant derivatives; the Ricci tensor of the unit S2 is the metric. The scalar curl convention uses w_2;1-w_1;2, so its square enters once. Smooth approximation in H1 on the compact sphere proves these identities for C1 fields.

Choose a smooth0<=eta<=1 supported in0<z<log R, equal to1 for log2<=z<=log(R/2), with bounded first derivative on the two strips. Denote the eta-weighted integrals by F_eta,T_eta,R_eta=F_eta-T_eta,A_eta=integral eta|grad f|^2,Z_f=integral eta|f_z|^2,Z_w=integral eta|w_z|^2 and C_w=integral eta|curl w|^2. Divergence gives

    integral eta grad f.w=k R_eta-(1/2)integral eta' f^2.

Use div w=-f_z-kf in the one-form identity. Its cross term is -k integral eta'f^2; the -4 pairing contributes +2 integral eta'f^2. The radial square contributes Z_f+Z_w+t^2F_eta-t integral eta'|v|^2. Since k^2-4k+2=t^2-2 and2-k=-t, the exact sum is

    G_eta=A_eta+(t^2-2)R_eta+t^2F_eta
      +2Z_f+Z_w+C_w-t integral eta'(|v|^2+f^2).       (1)

No cutoff integral has a prescribed sign, and no boundary derivative trace is estimated.

## 3. Scalar reduction with precise limits

The energy ratio gives uniformly bounded velocity energy on both endpoint strips; for the outer strip it is at most (R/2)^(-beta)E(R). Thus F_eta=F+O(1), T_eta=T+O(1), and the last term of (1) is O(1). Also0<=G_eta<=G. Finite-interval radial integration by parts gives

    F=R^(-beta)E(R)-E(1)+beta integral_1^R r^(-beta-1)E(r)dr
     =beta L log R+o(log R).

Take a sequence with T/(beta L log R)->x and G/(beta L log R)->g<infinity. Equation(1) and0<=R_eta<=F_eta show A_eta=O(log R), even when t^2-2 is negative. If x=0, the divergence pairing and Cauchy-Schwarz give k R_eta+O(1)<=sqrt(A_eta T_eta)=o(log R), contradicting R_eta/(beta L log R)->1. Hence x>0, and the same pairing gives

    liminf A_eta/(beta L log R)>=k^2(1-x)^2/x.

Discarding the three nonnegative square terms in (1), and taking account of G>=G_eta, yields

    g>=t^2+(t^2-2)(1-x)+k^2(1-x)^2/x
      =h(x):=k^2/x+2beta x+2-4beta.                  (2)

This argument allows x=1 as well; then the lower bound for A_eta is0. No convergent gradient ratio is assumed globally.

## 4. The smaller root and the source estimate

Direct substitution gives h(x_star)=H_beta. On0<x<=x_star,

    h'(x)=-k^2/x^2+2beta<0,

since2beta k^2/(k^2+2)^2<1. For example u/(u+2)^2<=1/8 for u>0 proves the latter. Therefore for M>=H_beta the smaller root of h(x)=M lies in(0,x_star], and is strictly before the unique minimum of h. The quadratic2beta x^2-Ax+k^2 has positive leading coefficient and strictly positive discriminant; rationalization gives the stated d(M). A is positive already at H_beta, since A=k^2/x_star+2beta x_star. Every positive x satisfying h(x)<=M is at least d(M).

Choose a sequence realizing the tangential liminf. The assumed gradient limsup permits a further convergent gradient-ratio subsequence, with limit g<=M. Equation(2) proves the tangential lower bound.

The source bound uses only q=partial_i partial_j(U_iU_j), tested against a smooth nonnegative radial function equal to r^m outside B2 and zero in B1, times a cutoff at2R. The uncut Hessian is m r^(-beta)(I-beta n tensor n). Inner errors are fixed, and the annular differentiated-cutoff error is bounded by C R^(-beta)E(2R)=O(1). The remaining Hessian term is nonnegative. Positivity and radiality bound the tested source above by J(2R)+C. Replacing R by R/2 costs only bounded increments of F,T. Thus

    J(R)>=m[(1-beta)F(R)+beta T(R)]-C.

Its logarithmic limit and J<=I give the claimed source bounds. The compact test is not convex. Ball inclusions transfer the energy ratio to fixed centers with the same L, and the proof then applies to the translated kinematic field. This does not translate the Euler equation.

## 5. Homogeneous equality and all-degree completion

Let Y be a real L2-normalized zonal harmonic of degree ell. For a smooth radial f define

    V_f=fY n+(r f'+2f)grad_S Y/Lambda.

Its radial divergence is (r f'+2f)Y/r and the tangential divergence is its negative. On r>=2 take f=b r^t, b^2=beta L/(1+k^2/Lambda). Then v=b(Yn+k grad Y/Lambda), with total sphere norm b^2(1+k^2/Lambda) and tangential norm b^2 k^2/Lambda. The angular derivative identity of Section2 gives b^2(Lambda+t^2-2), so its full gradient quotient is M_ell. Algebra gives M_ell=h(x_ell); since x_ell<=x_star, d(M_ell)=x_ell, and M_1=H_beta.

At the origin use f_in=b2^(t-ell+1)r^(ell-1). Then V_f is b2^(t-ell+1)/ell times the gradient of the harmonic polynomial r^ellY. It is smooth. Interpolate f_in and b r^t on2-epsilon<r<2 using a smooth cutoff. Their values agree at2, so their difference is O(epsilon); the cutoff's O(1/epsilon) derivative therefore leaves f and f' uniformly bounded on this shrinking annulus. For fixed ell the resulting energy tends to the interior energy

    b^2 2^(2t-2ell+2) (1+Lambda/ell^2)
       2^(2ell+1)/(2ell+1)=b^2 2^beta/ell.

The desired energy is b^2(1+k^2/Lambda)2^beta/beta, strictly larger since beta<1<=ell(1+k^2/Lambda). For a sufficiently small fixed epsilon the deficit D0 is positive. Add a0 eta0(r)Jy with eta0=1 near0 and support in B_(1/2), choosing a0>0 to fill D0. This azimuthal field is solenoidal and pointwise perpendicular to the zonal poloidal field. Hence the energies add exactly. The exterior shell energy is beta L r^(beta-1), and the completed origin energy is LR^beta for all R>=2.

## 6. Source coefficient and translations of the equalities

For a homogeneous solenoidal field with sphere norm K0 and tangential sphere norm T0, a compact radial test psi away from0 gives the Hessian pairing

    integral [(K0-T0)r^(beta-1)psi''+T0 r^(beta-2)psi']dr.

Integration twice in the first term and once in the second yields

    Q(r)=m[(1-beta)K0+beta T0]r^(beta-5).

Its coefficient is positive. With K0=beta L and T0=beta L x_ell this gives the asserted J coefficient. The T and G coefficients follow directly from their constant logarithmic densities.

The poloidal field has inversion parity (-1)^(ell+1), whereas the compact azimuthal part is odd. Their perpendicularity makes the full squared norm even. Consequently the first center derivative of E_a(R) at0 is0. Its second center derivative is a sphere integral of grad|U|^2, bounded by C_a R^2 R^(2t-1)=C_a R^(beta-2). Taylor's formula gives the stated energy remainder. All exterior derivatives obey D^hU=O(r^(t-h)).

The translated tangential density differs by O_a(r^(2t-1))=O_a(r^(beta-4)), including changes of the radial projection if the comparison is made in unshifted coordinates. After its weight and Jacobian the error is O_a(r^-2). The differences of |DU|^2 and q are O_a(r^(2t-3))=O_a(r^(beta-6)), again giving O_a(r^-2) after their critical weights and Jacobian. The Lipschitz property of the positive-part map permits the same estimate for the angular integral defining J. Integrating these errors proves the all-center O_a(1) remainders. Bounded inner regions contribute finite constants.

## 7. Poisson pressure and the three origin cases

Define P0 by the distributional Hessian of N(y)=1/(4pi|y|) convolved with U_iU_j, including its local delta term. Smooth local data justify the principal value. Far annuli contribute O(R^-3 E_a(2R))=O(R^(beta-3)), summable. Splitting off compact data allows all derivatives of the far part to fall on the smooth separated kernel. Thus P0 is smooth and -Delta P0=q. This does not impose full momentum.

Near0 the added field is a0Jy. For ell=1 the poloidal field is a constant axial vector d e3. Its derivatives vanish and J e3=0, so the curl of the pressure-free full momentum is2a0e3 for all c,omega. For ell>=3 the poloidal field is a homogeneous polynomial of degree ell-1>=2. Thus U(0)=0 and DU(0)=a0J. Differentiating the nonlinear term at0 gives (DU(0))^2 because the term involving U(0) vanishes. The same curl2a0e3 results.

For ell=2 choose the sign of Y so that the interior gradient matrix is S=diag(s,s,-2s) with s>0. Then U(0)=0 and M=DU(0)=S+a0J commutes with J. At0 the derivative of the pressure-free expression is

    (1-c)M+M(cI-omega J)+M^2+omega JM=M+M^2.

Its antisymmetric part is a0(1+2s)J, with nonzero curl2a0(1+2s)e3. This sign choice is essential to the stated simple obstruction and changes no norm. In every case a C1 pressure gradient has distributional curl0 and cannot cancel this nonzero continuous curl.

## 8. Full-profile application and limits

The full profile equation is (1-c)U+[((cI-omega J)y+U).grad]U+omega JU+grad P=0, with div U=0. For a nonzero bounded full C1 velocity and C1 pressure satisfying Hb in2/5<c<1/2, A3053 and its repeated audit supply the energy premise with beta=5-2/c, L>0 and remainder O(R^(beta-1)). Here Hb is distributional convergence U(R.)->0 on compact sets; uniform decay implies it. The finite normalized gradient coefficient is additional. A bound |DU|_F<=D r^(-1/c) outside a ball gives M=4piD^2/(beta L), necessarily at least H_beta. The argument applies to every finite omega without imposing symmetry on U.

The inequality itself covers all angular fields, while the equality examples use single zonal modes. Their pointwise source can change sign, so equality for J is not automatically equality for I. Optimality between the discrete M_ell values, optimality for I, automatic derivative bounds, full-Euler coefficient optimality and unrestricted rotating nonexistence remain open. This is a complete informal reconstruction; no formalization, mathematical computation or external-source retrieval was performed.


## 9. Existing C comparison and independently checked refinements

The full nine-part C comparison of09:45:54Z is retained in the team records, SHA256 f3362b3ec881bf3201458c3c4fac8ee484bfe0ec24ae1a8db0d3479d7c7c8f24. Its source and reconstruction reading is explicit; it did not read the fifty-eight source obligations or the support note. Those were read in this audit. Its numerical script, test fields, reported quadratures and decimal ratios were not executed or certified here. The configured C agent is model according to the run, with actual provider execution independently unattested.

Parts1-4 agree with Sections2-7. Pointwise, the sphere expansion acquires the divergence2 div_S(fw); its sphere integral is0. Also

    div_S(D_w w-(div_S w)w)
      =tr((D_Sw)^2)+|w|^2-(div_Sw)^2,
    |D_Sw|^2-tr((D_Sw)^2)=(curl_Sw)^2.

These identities derive the one-form formula with one curl square. As an exact check, w=sin(theta)e_phi has |D_Sw|^2+|w|^2=1+cos^2(theta) and curl_Sw=2cos(theta); both integrals are16pi/3. The cutoff coefficient is -t, with no sign claim on its integral. The all-degree core energy calculation and the degree-two sign choice agree exactly. For Y_2=sqrt(5/(16pi))(3mu^2-1), the Hessian of r^2Y_2 is sqrt(5/(4pi))diag(-1,-1,2); reversing Y_2 gives the positive s used in Section7.

Part5 extends equality beyond zonal harmonics. Every real normalized harmonic of degree ell has the same sphere energies because the integrations use only its eigenvalue Lambda. For a nonzonal harmonic, pointwise orthogonality to the compact Jy fill need not hold, but the sphere-integrated cross term is a radial factor times integral_S2 partial_phi Y=0. Thus the same positive energy deficit and fill work. At degree two the harmonic core has a symmetric traceless matrix S, and the momentum derivative is

    M+M^2+omega(JM-MJ),  M=S+a0J.

The commutator JS-SJ is symmetric and has zero curl. The skew part of SJ+JS has axial vector -S e3, so the residual curl is2a0(e3-S e3). A chosen harmonic is therefore covered when S e3!=e3. If necessary reverse its sign: S e3=e3 and -S e3=e3 cannot both hold. For example S proportional to diag(1,-1,0) gives a non-axisymmetric equality field with curl2a0e3. At ell1 the core is constant plus a0Jy and at ell>=3 its constant jet is0 and linear jet a0J, so their curl obstruction still holds. Although a nonzonal completed field's full energy density need not be even in the core, its homogeneous exterior density is even, which suffices for the large-radius boundary argument in Section6. This proves existence of nonzonal equality controls; it does not claim that every arbitrary unsigned degree-two choice has a nonzero core curl.

Part6 is confirmed analytically for ell1 only: its exterior source is

    q=3b^2t^2/(8pi)[(k+3)mu^2-k]r^(beta-5).

It is negative on an open equatorial belt and positive near the poles, so its pointwise positive-source coefficient strictly exceeds its spherical positive-source coefficient. The higher-degree decimal observations are not proofs and no general higher-degree sign classification is inferred.

Part7's strict improvement over A3133 follows directly. Define

    g(x)=t^2+[k-(k+1)x]^2/x.

Its positive-branch inverse at M is the earlier d_beta(M-t^2). Algebra gives

    h(x)-g(x)=[(t+1)^2+1]-[(t+1)^2+2]x.

For x=d(M)<=x_star<1/3 this is positive. On0<x<k/(k+1), g is strictly decreasing; x_star is in this interval. Hence g(d(M))<M implies d_beta(M-t^2)<d(M). Since d_beta is strictly decreasing and t^2>0,

    d(M)>d_beta(M-t^2)>d_beta(M),  M>=H_beta.

Both new and earlier roots obey M d(M)->k^2 at infinity. This is an analytical comparison, not a conclusion from sampled ratios. Part8 points to the separately pending LIT383 optimization and establishes nothing additional here. Part9's kinematic-versus-profile distinction is preserved. The unresolved statements of Section8 refer to this result's scope; later verdicts can resolve parts of that scope separately.
