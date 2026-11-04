# Local critical-node countertests and the normalized open-zero scalar system

Status: A947-A951 CONFIRMED at the stated local or conditional scope; A952 OPEN for actual global exclusion. These are local tail constructions and conditional deductions, not actual global profiles.

## 1. Exact local setting and nodal geometry

Fix 2/5<c<1/2 and omega in R. Set A=cI-omega J, X(x)=Ax, a=1-2c, b=2(1-c), q=b/a and Jx=(-x2,x1,0). Work in a neighborhood of a point z!=0. A local tail here obeys

    XV=-((1-c)I+omega J)V, div V=0,
    W=curl V, V.W=0,
    k=X.V, grad k=X cross W-aV,
    grad k cross V=kW,
    X S=-bS, Wk=WS=0,
    grad k cross grad S=0,
    P2=S+|V|^2/2, -Delta P2=tr((DV)^2).

On vortical components with k!=0 the examples below also have S=D|k|^q, with a constant D per component.

For a C1 field V!=0 satisfying these identities, V-perpendicular is integrable: the one-form beta=V.dx has beta wedge d beta=0. To see the needed C1 chart directly, choose V3!=0 and T_i=partial_i-(V_i/V3)partial_3, i=1,2. Their bracket is vertical and beta annihilates it, so it is zero. The commuting flows give the foliation chart. The identity

    grad k=((grad k.V)/|V|^2)V+k(V cross W)/|V|^2

makes k solve a homogeneous scalar ODE along each plaque. Thus locally k=A0 K(f), where f is a transverse coordinate, K is C1 and A0 is positive continuous. At a nodal point, differentiating is valid without differentiating A0, because K=0: dk=A0 K'(f)df. Critical roots can have either sign behavior. If the data and chart are analytic, accumulating zeros of the one-variable analytic K force its local identically-zero case. No analyticity of a general actual tail is inferred.

## 2. Analytic germs with arbitrary critical multiplicity

For every integer m>=2, construct analytic f,ell near z with df!=0, f(z)=0 and

    V=exp(ell)grad f, k=exp(ell)f^m,
    P2=|V|^2/2, S=0.

The multiplier exp(ell) is a positive analytic function, not a claimed constant. Impose the transport equations

    Xf=K(f), Xell=-a-K'(f), K(f)=f^m.

Then X grad f=K'(f)grad f-A^T grad f gives the required homogeneity of V. Also W=exp(ell)grad ell cross grad f, so V.W=0 and the k identities follow directly. The rank and first-integral equations for S=0 are automatic.

Put n=grad f, d=grad ell, F=D2f, G=D2ell. Divergence is equivalent to

    Delta f+n.d=0.

Under this equation the pressure residual divided by exp(2ell) is

    (|n|^2 I-n tensor n):G
      +2|F|^2+5F(n,d)+(n.d)^2+2|n|^2|d|^2.

Indeed DV=exp(ell)(F+n tensor d) gives tr((DV)^2)/exp(2ell)=|F|^2+2F(n,d)+(n.d)^2. The Laplacian of |V|^2/2 divided by exp(2ell) is |F|^2+4F(n,d)+n.grad Delta f+|n|^2(Delta ell+2|d|^2). Differentiating divergence gives grad Delta f=-Gn-Fd, producing the displayed coefficient5. Thus its vanishing is exactly Poisson after imposing divergence.

Choose orthonormal e1,e2 perpendicular to X(z). On the transverse plane z+t e1+s e2 impose along s=0

    f(t,0)=t, f_s(t,0)=0,
    ell(t,0)=0, ell_s(t,0)=0.

The transport equations determine all derivatives containing X. In particular F X=K'(f)n-A^T n and G X=-K''(f)n-A^T d. On the transverse plane divergence and the displayed pressure equation are analytic second-order equations. At z, n=e1. The coefficient for solving the first equation for f_ss is1, and it contains no second derivatives of ell. After this solution, the coefficient for solving the second equation for ell_ss is |n|^2-(n.e2)^2=1. By continuity and the analytic implicit-function theorem the equations have analytic normal form. The other derivatives have total order at most2 and normal order below2.

Apply the analytic Cauchy-Kovalevskaya theorem for systems in this normal form, with the displayed analytic Cauchy data. The exact standard-form hypothesis was checked in Gantumur's 2014 notes, Theorem33, printed page16; the obtained primary PDF and text are retained in verification. Extend by the two transport equations along X. Divergence scales by exp(-t), and both pressure terms scale by exp(-2t), so the equations imposed on the plane hold on the full three-dimensional neighborhood.

At z, V=e1 and grad ell=-aX(z)/|X(z)|^2. Thus W=-a X(z) cross e1/|X(z)|^2!=0. Shrinking preserves nonzero V,W,df. Every node lies on f=0 and is critical. Taking m=2 gives one sign for k; m=3 gives a sign change. These are genuine analytic germs of all the stated local tail equations, including Poisson.

## 3. A nonzero S example and the degenerate scalar equation

At c=3/7 one has q=8. Repeat Section2 with m=2 and S=k^8, P2=|V|^2/2+k^8. Add exp(-2ell)Delta(exp(8ell)f^16) to the pressure equation. Its second-derivative coefficients vanish on f=0, so the same noncharacteristic determinant persists. The analytic construction gives k>=0, S>0 off its critical nodal sheet, and V,W!=0. This disproves a purely local assertion that a one-signed critical node forces S=0 nearby or V=0. The nonzero-S construction is asserted only at this parameter; the S=0 construction works at every allowed c and omega.

For sufficiently differentiable local fields, direct differentiation gives

    Delta S=-2|sym DV|^2-V.Delta V,
    (|V|^2 I-V tensor V):D2k+((DV)V).grad k
      +k Delta S+2k|sym DV|^2=0.

The second identity follows by curling grad k cross V=kW and dotting with V, using curl W=-Delta V. On S=D|k|^q the principal matrix becomes (|V|^2+qS)I-V tensor V. Its eigenvalue in the V direction is qS: zero at S=0, tending to zero at the node when S>0, and negative when S<0. The usual uniformly elliptic strong minimum principle therefore does not supply the proposed conclusion, which is also contradicted by the explicit analytic germs. This does not rule out every possible degenerate-PDE argument with additional hypotheses.

## 4. Conditional accumulation statements for actual profiles

Use the full actual-profile hypotheses, canonical pressure and scattering constructions stated in the team records. Suppose, conditionally, regular vortical nodal components M_n with the confirmed normalization U=b_n grad H accumulate at a critical tail node z with V(z)!=0. Then |b_n|=|V(z_n)|/|grad k(z_n)| tends to infinity.

On a component with 1+a b_n!=0, compare Lie_B(U.dx)=-aU.dx-dQ with b_n Lie_B(dH)=-ab_n dH+ab_n dQ. It follows that (1+a b_n)dQ=0. Evaluation of U=b_n grad H on B gives (1+a b_n)g=0. Hence g=dQ=0, and forward escape forces H=Q=0. These apply to every sufficiently late M_n because |b_n| tends to infinity.

Pull back z_n through Xi and pass to the limit: H=Q=dH=dQ=0 on the limiting original joint leaf. Finite original flow maps carry the sequence of components to each point of that leaf. The carrier Kelvin identity prevents U from vanishing there, since a zero would propagate and contradict V(z)!=0; independence of B,Omega then propagates by their affine bracket.

In a regular joint-flow chart near any point of the limiting leaf, the nearby components are distinct plaques. A fixed smooth transverse curve intersects them at points p_n tending to p. Both scalar values vanish on those plaques; both gradients vanish on the limiting plaque. Their Hessians annihilate its tangent plane. Taylor expansion along the transverse sequence therefore forces the remaining normal coefficient to vanish. Thus D2H=D2Q=0 on the limiting leaf. Pointwise rank at a zero gradient alone would not prove this.

For omega=0 the bounded backward orbit obeys B|y|^2=2|B|^2/c, so |B|^2 is integrable in backward time and has bounded time derivative on its compact range. Hence B tends to zero backward. The identity B cross Omega=aU then gives U and y tending to zero. The flat Q jet yields sym DU(0)=0 through Delta Q=-2|sym DU|^2-U.Delta U. Along the far backward part of the orbit, d|Omega|^2/dt<=-|Omega|^2. Boundedness of Omega backward forces it to be zero, a contradiction.

These are valid conditional deductions but their proposed actual accumulation configuration is already impossible by A897, which excludes every regular vortical tail node. They do not transfer zero Hessians to the remaining noninterior critical leaves of C44. No uniform global b_n bound is established or needed here.

## 5. Normalization and consistency of the open-zero scalar system

For an actual open L-zero component with transported scalar s>0 satisfying s(Phi_t y)=exp(-bt)s(y), write H=h(s), Q=q_C(s). Let sigma be the constant sign of the nonzero tail S and eta=a/b. The tail pressure limit gives q_C(s)/s->sigma as s decreases to zero. If

    q_C=h-(s/eta)h', h(s)=o(s^eta),

then integrating (h/s^eta)'=-eta q_C(s)s^(-eta-1) from0 to s gives

    h(s)=-eta s^eta integral_0^s q_C(u)u^(-eta-1)du
         =-a sigma s+o(s),

because eta/(1-eta)=a. For either sign sigma the explicit scalar pair

    h(s)=-sigma eta s exp(-s)/(1-eta),
    q_C(s)=sigma s exp(-s)(1-s/(1-eta))

satisfies the equation, both endpoint conditions h/s^eta->0 and the normalized tail limit. Integration of the derivative identity gives the convergent weighted cancellation integral_0^infinity q_C(s)s^(-eta-1)ds=0. This is a scalar consistency example only; it supplies no velocity, full pressure equation or global matching.

## 6. Verification and remaining scope

The complete submitted question, nine-section proof and verification note were read. The matrix pressure reduction, transport, principal coefficients, scalar equations and conditional accumulation argument were independently checked by hand. No polynomial spot test is used as proof. The Cauchy-Kovalevskaya source was obtained and its exact standard-form theorem read. The source's direct model attempt failed at credential retrieval before invocation; it is not a model review. Existing configured model agent comparison remains the collaboration path, with no independently attested provider runtime.

No constructed germ is shown to extend around a full azimuthal band, across the origin, or to the canonical pressure of an actual global profile. Accumulation of regular actual vortical nodes is now excluded by A897. The actual remaining noninterior critical nodes instead have V!=0 by A939 if they exist, and their joint closures contain plane leaves only by A941. Exclusion of those planes and of open-zero actual regions remains unresolved. The source does not establish method completeness or the full rotating conjecture.
