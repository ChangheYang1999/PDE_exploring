# Global identities for a nonvanishing tail scalar

Status: CONFIRMED at A618, A619, A620, A621. Exact hypotheses, proof and limitations are stated below. Informal independent verification; no formal build or numerical proof is claimed.

## 1. Exact setting and conclusions

Let 1<p<3/2, c=1/(p+1), omega be any finite real number, Jx=(-x2,x1,0), A=cI-omega J, and D=R3 minus {0}. Put

    t=omega/c, lambda=p-1, mu=2-p, eta=lambda/(2p), a=c lambda.

Let V in C1(D;R3) satisfy div V=0 and

    V(exp(sA)x)=exp(-(1-c)s) exp(-omega sJ)V(x).

Let S in C1(D) satisfy S(exp(sA)x)=exp(-2(1-c)s)S(x). Define W=curl V and k=(Ax).V. Assume

    W.grad S=0 on D,
    grad k cross grad S=0 on {W!=0},
    S has no zeros on D.                                      (1)

No helicity or pressure equation is needed until Section6. Set rho=log r, z=cos(theta), chi=phi+t rho, w=1-z^2, and write

    V.flat=exp(-lambda rho)(K d rho+beta),
    S=exp(-2p rho)h,
    beta=-(H/w)dz+F dchi, K=R-tF,
    V=r^-p[R er+(H/sin(theta))e_theta+(F/sin(theta))e_phi].

Here K and beta are global C1 scalar and one-form on S2, interpreted intrinsically at the poles. Let Z=partial_chi be the smooth rotation field and M=g_S2^-1+t^2 Z tensor Z. Let f=|h|^eta>0 and g=K/f. There are global potentials psi in C1(S2) and Psi Lipschitz on S2, with Psi of mean0, such that

    beta=f dpsi-(g/lambda)df,
    dPsi=sgn(g)dpsi almost everywhere, sgn(0)=0.

Then a finite nonnegative number D0 satisfies

    D0+lambda mu integral_S2 |K|
       =t mu integral_S2 (|g|+lambda Psi) Zf.                  (2)

It follows that V=0 if t=0, if S is axisymmetric, or if K is identically0. Also V=0 if {W!=0} is dense in D. A nonzero field satisfying (1) must therefore have a positive twist term, a nonaxisymmetric scalar and an open irrotational region. No sign of the twist term is established in general.

For the finite-mode conclusion additionally assume V.W=0 and S=P2-|V|^2/2, where P2 in C1(D) has twisted degree -2(1-c) and solves

    -Delta P2=partial_i partial_j(V_i V_j)

in distributions on D. If R,H,F have Fourier support |m|<=N in chi and

    eta is not j/m for any 1<=j<=N and 1<=m<=2N,               (3)

then V=0. In particular N<=3 suffices since 0<eta<1/6. This still assumes S has no zeros. The low degree here refers to the velocity's angular amplitudes, not to the pressure multipoles of a full profile.

Finally, for the kinematic statement alone let 1<p<2, let V in C1(D) have the stated homogeneity and div V=V.curl V=0. Then k has a zero in D. Equivalently no such field has k everywhere nonzero. No scalar or pressure is used.

## 2. Global differential identities

In the coordinates above, the Euclidean metric is exp(2rho) times

    d rho^2+dz^2/w+w(dchi-t d rho)^2.

Its volume density relative to d rho dz dchi is exp(3rho). Raising the one-form V.flat with this inverse metric gives the rho component proportional to K+tF, the z component proportional to w beta_z, and the chi component proportional to tK+(1/w+t^2)F. Differentiating its volume flux proves

    div_S2(M beta)+t mu beta(Z)+mu K+t ZK=0.                  (4)

This is an intrinsic sphere equation; no polar boundary contribution is omitted.

Exterior differentiation gives

    d(V.flat)=exp(-lambda rho)[d beta-d rho wedge(lambda beta+dK)].

The equation W.grad S=0, equivalently dS wedge d(V.flat)=0, is therefore

    2p h d beta=lambda dh wedge beta+dh wedge dK.             (5)

Since h never vanishes and df/f=eta dh/h, (5) implies that

    delta=beta/f+(g/lambda)dlog f

is closed in distributions. A continuous distributionally closed one-form on simply connected S2 has a global C1 potential; local mollification and path integration prove this usual form of the Poincare lemma. This gives psi and the displayed formula for beta.

The radial and tangential parts of dk wedge dS=0 on W!=0 give 2p h dK=lambda K dh and dK wedge dh=0. Hence dg=0 there. At a point with W=0 the full two-form d(V.flat) vanishes, so dK=-lambda beta and consequently dg=-lambda dpsi. We have pointwise on all S2

    dg wedge dpsi=0,
    M(dg,dpsi)=-M(dg,dg)/lambda.                              (6)

Only the implication W=0 implies dK=-lambda beta was required. The converse at a point also follows from (5) when h!=0, because it then forces d beta=0. Without h!=0 or another condition, the radial equation alone does not describe the entire zero set of W.

For every smooth real function varphi, (6) shows that varphi(g)dpsi is distributionally closed. Let Psi_varphi be its mean0 global potential. These operations are valid with h merely C1: all first-derivative products are continuous and the exterior derivatives are distributional.

## 3. Integration and the scalar zero set of g

Multiply (4) by varphi(g), integrate over S2 and let J0 be any primitive of varphi. Where dg!=0, (6) gives beta=-dK/lambda. Where dg=0 the derivative term vanishes. Thus integration by parts yields

    I_varphi+lambda mu integral fg varphi(g)
      =t integral [lambda mu Psi_varphi
                    +(mu-lambda)g varphi(g)+lambda J0(g)] Zf, (7)

where

    I_varphi=integral varphi'(g)[f M(dg,dg)+g M(df,dg)].

For an independent sign check, the two rotational terms before combination are

    integral varphi(g) beta(Z)
       =-integral [Psi_varphi+g varphi(g)/lambda] Zf,
    integral varphi(g) ZK
       = integral [g varphi(g)-J0(g)] Zf.

They follow from div_S2 Z=0 and dPsi_varphi=varphi(g)dpsi. Together with the positive term mu K in (4), they give exactly (7).

Choose varphi_epsilon(s)=s/sqrt(s^2+epsilon^2) and J0_epsilon(s)=sqrt(s^2+epsilon^2). The mean0 potentials have uniformly bounded gradients and hence uniformly bounded values. Dominated convergence gives

    dPsi_epsilon -> sgn(g)dpsi in every finite Lq.

Arzela-Ascoli and uniqueness of a mean0 potential give uniform convergence of the entire family to a Lipschitz Psi. This also treats positive-measure sets where g=0; varphi_epsilon(0)=0 exactly.

Write I_epsilon=A_epsilon+B_epsilon with

    A_epsilon=integral f epsilon^2(g^2+epsilon^2)^(-3/2)M(dg,dg)>=0.

Cauchy-Schwarz and varphi_epsilon'(g)g^2<=epsilon imply

    |B_epsilon|<=C sqrt(epsilon A_epsilon),

because f is bounded below and df,M are bounded on S2. Every term on the right of (7) is uniformly bounded, and fg varphi_epsilon(g)>=0. Hence A_epsilon-C sqrt(epsilon A_epsilon)<=C, which bounds A_epsilon. It follows that B_epsilon->0. All other terms in (7) converge; consequently A_epsilon has a finite limit D0>=0. Equation(2) follows. This limit argument does not assume monotonicity in epsilon.

## 4. Rigidity consequences and their precise scopes

If K=0, then g=0 and beta=f dpsi. Since beta/f is C1, psi is C2. Equation(4) becomes

    div_S2(f M dpsi)+t mu f Zpsi=0.                            (8)

Its principal tensor is C1 and uniformly positive, the drift is bounded, and there is no zeroth-order term. The strong maximum principle on the compact connected sphere gives psi constant, beta0 and V0. This is a classical uniformly elliptic argument at the stated regularity; no singular-weight maximum principle is being invoked.

If t=0 or Zh=0, then Zf=0 or the coefficient t is0. Equation(2) forces K0 because lambda mu>0, and (8) finishes. These cases impose no symmetry on V. They do not extend to arbitrary zeros of h by this proof.

If W!=0 is dense, continuity and (6) give g constant. The full one-form

    |S|^-eta V.flat=g d rho+beta/f
       =d[g rho+psi-(g/lambda)log f]

has potential Phi. If g!=0, Phi0 is a compact C1 graph over S2 in the global coordinates (rho, angular variable with rotation by t rho). It surrounds the origin and has no critical point since its derivative along fixed twisted angles is g. Orienting it by grad Phi, its V-flux is

    integral |S|^eta |grad Phi|>0.

The divergence theorem applied after excising a small ordinary sphere makes the same flux zero: its inner boundary flux is O(epsilon^(2-p))->0. The possible reversal between this orientation and the outward orientation affects only a sign, not the contradiction. If g0 use (8). This proves the density consequence and the asserted necessary positive twist term for a nonzero field.

## 5. Kinematic zero of k

For any homogeneous C1 field at 1<p<2 the vector identity is

    grad k=-aV+(Ax) cross W.

If V.W=0, taking its cross product with V gives grad k cross V=kW. Thus on k!=0,

    curl(V/k)=W/k-grad k cross V/k^2=0.

Suppose k never vanishes. D is simply connected, so V/k=grad Phi globally. In twisted coordinates the radial coefficient of V.flat/k is1/c, hence

    Phi=rho/c+phi0(angular variable).

The angular function phi0 is C1 globally on S2. Therefore Phi0 is a compact C1 graph surrounding0 and grad Phi!=0. On this surface V=k grad Phi, and k has one strict sign by connectedness of D. Its flux oriented by grad Phi is nonzero. Div V0 and the small-sphere bound O(epsilon^(2-p)) instead force zero flux. This contradiction proves the kinematic statement. It does not assert that V has a zero where k does, or that a zero lies in a vortical region.

## 6. Canonical pressure and the finite Fourier argument

Write P2=r^-2p u. The angular pressure operator is

    L_t=(w partial_z)_z+(1/w+t^2)partial_chichi
             +t(1-4p)partial_chi+2p(2p-1).

On the spherical harmonic with indices(l,m), its eigenvalue is

    2p(2p-1)-l(l+1)-t^2 m^2+i t(1-4p)m.

For t m!=0 the imaginary part is nonzero. For t m=0 it cannot vanish: when t=0 the value2p(2p-1) lies strictly between2 and6 and is not l(l+1); when m=0 the same argument applies. This proves uniqueness of a global regular solution; existence here is assumed through P2. Rotation covariance then shows that the pressure has no Fourier modes beyond those of its source. In particular, if R,H,F have degree at most N, their derivative matrix in the orthonormal spherical frame has entries of degree at most N. Thus q=tr((DV)^2), e=|V|^2/2 on the sphere, u and h=u-e have degrees at most2N. This uses global pressure uniqueness, not merely the local Poisson equation.

At a fixed nonpolar latitude, if W is not identically0 as a function of chi, its finite Fourier components imply that its nonzero set is dense in that circle. Rank and continuity imply

    h K_chi=eta K h_chi                                      (9)

everywhere on that circle. If K is not identically0, compare the highest positive Fourier frequency of the two nonzero real trigonometric polynomials K,h. Degrees j,m give (j-eta m)K_j h_m=0. If only one has positive degree this is impossible as well. Under(3), K and h are both constant on this circle. If K is identically0, its chi derivative is also0. Therefore v=ZK vanishes at every non-irrotational latitude.

The scalar v is continuous on S2 and zero at the poles. If its maximum were positive, it would occur away from the poles in a neighborhood where v>0. Every latitude through that neighborhood must be entirely irrotational by the previous paragraph. On this open region grad k=-aV, so k is harmonic and smooth. Both K and v satisfy

    L_lambda v=0,
    L_lambda=(w partial_z)_z+(1/w+t^2)partial_chichi
                   +t(1-2lambda)partial_chi-lambda(1-lambda).

At the positive maximum the principal second derivatives contribute nonpositively, first derivatives vanish, and the strictly negative zeroth-order term gives a contradiction. The negative minimum is treated by -v. Hence K is globally axisymmetric. Harmonic regularity supplies all derivatives needed at these extrema even though globally V is only C1.

Let I be a connected interval of nonpolar latitudes with K(z)!=0. At its non-irrotational latitudes equation(9) already makes h independent of chi. Let J0 be a maximal open interval of irrotational latitudes inside I. On it k is axisymmetric and harmonic and V=-grad k/a, so V,e,q are axisymmetric. Each nonzero Fourier mode h_m=u_m solves

    (w h_m')'+[2p(2p-1)-(1/w+t^2)m^2+i t(1-4p)m]h_m=0.      (10)

If an endpoint z0 of J0 lies inside I, non-irrotational latitudes accumulate there. Thus h_m has accumulating zeros and its C1 regularity gives h_m(z0)=h_m'(z0)=0. The coefficients of (10) are regular there; extension to the endpoint and uniqueness for its two-dimensional first-order system give h_m0 throughout J0.

The alternative J0=I is impossible. K has one nonzero sign on I, vanishes at every nonpolar endpoint, is regular at any included pole, and solves L_lambda K0 on the corresponding band or cap. A positive maximum of K or -K must be interior in the sphere, contradicting its strictly negative zeroth-order coefficient. If I is the whole interval, the same maximum argument takes place on S2. This proves Zh0 wherever K!=0. Irrotational latitudes not inside an interval J0 are limits of non-irrotational ones, so continuity includes them.

At any latitude with K!=0, Zf0. At a latitude with K0, the whole circle has g0, and the regularized potentials obey ZPsi_epsilon=varphi_epsilon(0)Zpsi0. Their uniform limit Psi is constant on that circle. Consequently its contribution to integral(|g|+lambda Psi)Zf is also0, by periodic integration of Zf. Fubini proves that the entire twist term in(2) is0. Thus K0 and then V0.

The resonance condition is necessary for any hypothetical nonzero finite-mode field with a nonvanishing scalar; it is not sufficient to construct one. For 1<=N<=3, j/m>=1/(2N)>=1/6>eta, so no resonance occurs. When N=0 all amplitudes and the unique pressure are already axisymmetric, and Section4 applies directly. Such fields of higher degree also require an open irrotational latitude band: the open irrotational region from Section4 contains a product rectangle, and vanishing of the finite Fourier vorticity on its chi interval gives vanishing on each whole latitude circle.

## 7. Undivided nodal and strictly negative scalar systems

For completeness, the exact nodal reduction in the source does not require the assumptions of Sections2-4 at zeros. Given global regular K,beta, reconstruct V as in Section1 and set

    e=((K+t beta(Z))^2+|beta|_S2^2)/2,
    q=tr((DV)^2) on r1,
    h=-L_t^-1 q-e.

The five tail conditions are exactly (4),

    K d beta+beta wedge dK=0,
    2p h d beta=lambda dh wedge beta+dh wedge dK,

and, on O={(d beta,lambda beta+dK)!=(0,0)},

    2p h dK=lambda K dh,
    dK wedge dh=0.

Indeed the first displayed two-form is the angular coefficient of V.flat wedge d(V.flat), the second equation expresses dS wedge d(V.flat)=0, and the final pair expresses dk wedge dS=0. The set O is the actual W!=0 set. At h0, the last wedge equation cannot be discarded. No arbitrary homogeneous pressure summand is available.

When h<0, put f=|h|^eta, g=K/f and use the global psi already constructed. The equivalent regular system is

    div(M beta)+t mu beta(Z)+mu K+t ZK=0,
    L_t(e-f^(1/eta))=-q,
    dg=0 or dg=-lambda dpsi at every point,
    beta=f dpsi-(g/lambda)df, K=fg.

To check sufficiency set sigma0=rho-(log f)/lambda. Then

    V.flat=exp(-lambda sigma0)(g d sigma0+dpsi),
    S=-exp(-2p sigma0),
    d(V.flat)=-exp(-lambda sigma0)d sigma0 wedge(dg+lambda dpsi).

The helicity three-form is proportional to d sigma0 wedge dpsi wedge dg and vanishes by the pointwise alternative. Since d sigma0 has radial coefficient1 and dg+lambda dpsi is angular, W0 is exactly dg+lambda dpsi0. Off this set dg0, giving rank; the other wedge equations follow directly. These are equivalent systems, not existence or nonexistence proofs. The sign of the twist term and arbitrary nodal behavior remain open.

## 8. Verification and full-profile application

All arguments above have been independently reconstructed from the full source answer and all three source in the team records files. No numerical computation is used. Ordinary Poincare, harmonic regularity, divergence and maximum principles appear with their necessary regularity, compactness and boundary conditions stated in place. The actual configured-model coordinator check is a separate source comparison; the inner answer explicitly reports failed model credentials, not a successful second-model call.

For a target full C2/C1 Euler profile with global zero helicity, U->0 and DU=O(sqrt r), the confirmed derivative and scattering theorems supply its natural tail and all hypotheses used here. The confirmed vanishing-tail implication then sends V0 to U0. Each conditional conclusion retains the nonvanishing scalar or finite-mode premise stated in Section1. Unrestricted bare-decay nonexistence is not obtained.
