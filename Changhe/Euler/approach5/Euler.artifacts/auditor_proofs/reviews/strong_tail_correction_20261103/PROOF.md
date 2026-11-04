# Strong nonlinear tail correction and the next carrier covector coefficient

Status: CONFIRMED as A539 after complete source comparison, independent reconstruction and full postread. The formerly submitted regularity inputs are confirmed as A530,A533,A538. No computation was needed.

## 1. Hypotheses and conclusions

Let 2/5<c<1/2, omega in R, p=(1-c)/c, a=1-2c, A=cI-omega J, L=(1-c)I+omega J and Q_t=exp(omega tJ), with J(x1,x2,x3)=(-x2,x1,0). Let U in C2(R3;R3), P in C1(R3) solve

    div U=0, LU+DU(Ax+U)+grad P=0,
    |U(y)|<=C(1+|y|)^-p,
    |DU(y)|<=C(1+|y|)^(-p-1).                            (1)

The constant C may depend on the profile,c,omega. Let D=R3 minus{0}, V its actual velocity tail and Pinf its canonical pressure constant. The canonical limiting pressure is

    P2=partial_i partial_j Gamma*(V_i V_j),
    Gamma(x)=1/(4pi|x|).

The tensor formula is interpreted as the canonical distribution, as in A530. Define

    u_t(x)=exp((1-c)t)Q_t U(exp(tA)x),
    p_t(x)=exp(2(1-c)t)(P(exp(tA)x)-Pinf),
    z_t=exp(t)(u_t-V), S_t=p_t-|u_t|^2/2,
    S=P2-|V|^2/2, Z=DV V+grad P2,
    Wstar=curl V, E=-aV+Ax cross Wstar.                   (2)

For every 0<alpha<1,

    p_t -> P2 in C^(2,alpha)loc(D),
    S_t -> S in C^(1,alpha)loc(D),
    z_t -> Z in C^alpha loc(D).                          (3)

For each finite q>3, z_t are uniformly bounded in W^(1,q)loc(D), and Z belongs to that space. No convergence of Dz_t in C0 and no C2 convergence of u_t is asserted.

For an escaping B-orbit y_t=Phi_t(y0), B=Ay+U, set

    x_t=exp(-tA)y_t -> v!=0,
    G(t)=exp((1-c)t)Q_t grad H(y_t),
    H=P+|U|^2/2+(Ay).U, g=U.B.

Then

    exp(t)(G(t)-E(v)) -> DV(v)^T E(v)-a grad S(v).        (4)

This is a coefficient along the actual B-orbit. It is not a differentiated expansion along the linear A-flow. No helicity or symmetry assumption is needed for(3)-(4).

Suppose, in addition, this escaping orbit has

    H(y_t)=Pinf, g(y_t)=0,
    aU(y_t)=(exp(mu t)f0-1)grad H(y_t),
    mu>=1, f0!=0, V(v)!=0, E(v)=0.                       (5)

Then

    S(v)=0;
    mu=1 implies grad S(v)=-V(v)/f0!=0;
    mu>1 implies grad S(v)=0.                            (6)

The explicit conditions(5) are supplied either by A518 on its lower-vortical level, or by A536 on any zero-g component with lambda>1, with mu=a(lambda-1). They can also simply be imposed as the hypotheses of this last corollary. They are not consequences of(1) alone.

## 2. Pressure Hessian convergence

A530 gives p_t->P2 in C1loc(D). A533 or A538 gives u_t->V in C^(1,gamma)loc for every gamma<1. A538 further gives uniform local W^(2,q) bounds for every finite q>3.

The rescaled Poisson equation is

    -Delta p_t=tr((Du_t)^2).                              (7)

Fix nested open balls with closures B0 inside B1 inside D. For a chosen alpha<1, select gamma with alpha<gamma<1. The right side of(7) converges in C^gamma(B1) to tr((DV)^2). Distributional convergence, or the canonical tensor identity, identifies this as -Delta P2. Interior Poisson regularity gives P2 in C^(2,gamma) on smaller balls. Applying the interior Schauder estimate to p_t-P2 gives

    ||p_t-P2||_(C^(2,alpha)(B0))
       <=C[||p_t-P2||_(C0(B1))
          +||tr((Du_t)^2)-tr((DV)^2)||_(C^alpha(B1))] ->0.

If necessary take one additional intermediate ball before this application. A finite cover handles any compact subset of D. Products with u_t now give S_t->S in C^(1,alpha). Every ball stays a positive distance from the singular origin; no global Schauder estimate is used.

## 3. An exact fixed-position integral for the correction

Put n_t=Du_t u_t+grad p_t. Directly differentiating the rescaling and using the full profile equation gives

    partial_t u_t=-exp(-t)n_t.                            (8)

The already established local convergence implies

    n_t -> Z in C^alpha loc(D) for every alpha<1.          (9)

At a fixed x, integrate(8) from t to infinity, using u_t->V and the local uniform bound on n_t. This gives the exact formula

    z_t(x)=integral_0^infinity exp(-s)n_(t+s)(x)ds.        (10)

The spatial argument stays fixed. Thus on each compact set, using norms on a slightly larger finite union of balls,

    ||z_t-Z||_(C^alpha)
       <=sup_(r>=t)||n_r-Z||_(C^alpha) ->0.               (11)

This estimate follows directly for the supremum norm and every Holder difference quotient. It needs no interchange of a classical derivative with an improper integral.

For finite q>3, differentiating the product in n_t in the weak sense produces D2u_t times bounded u_t, two bounded first derivatives, and D2p_t. A538 and Section2 therefore imply

    sup_(t>=t0)||n_t||_(W^(1,q)(K))<infinity             (12)

on a neighborhood of any compact K. Test(10) against a compactly supported smooth spatial function and use Fubini and the exponential kernel. The weak derivatives of z_t are the corresponding integrals of weak derivatives of n_(t+s). Minkowski gives the same uniform W^(1,q) bound for z_t. Weak compactness combined with(11) gives Z in W^(1,q)loc. Neither this bound nor(11) asserts uniform convergence of the derivatives.

## 4. The exact carrier covector equation

The boundedness in(1) gives a complete B-flow. An escaping orbit has the scattering limit v!=0 by A533's elementary radial estimate. Its x_t remains in a compact annulus for large t and satisfies

    x_t'=exp(-t)u_t(x_t),
    |x_t-v|=O(exp(-t)).                                  (13)

Let N=grad H. The exact Lamb and scalar identities, valid without zero helicity, are

    N=-aU+B cross W,
    B.grad H=-ag,
    H-g=P-|U|^2/2.                                      (14)

H is C2 because the first right side is C1. Differentiating the second identity gives

    D2H B=-a grad g-(A^T+DU^T)N.

The derivative of exp((1-c)t)Q_t along y_t cancels A^T up to aI. Using the last identity in(14), and the transformations of DU and the scalar gradient, yields

    G'(t)=exp(-t)[a grad S_t(x_t)-Du_t(x_t)^T G(t)].       (15)

In detail, exp((1-c)t)Q_t grad(P-|U|^2/2)(y_t)=exp(-t)grad S_t(x_t), while exp((1-c)t)Q_t DU(y_t)^T N(y_t)=exp(-t)Du_t(x_t)^T G(t). These establish every factor and sign in(15).

The rescaled first identity in(14) reads

    G(t)=-a u_t(x_t)+Ax_t cross curl u_t(x_t)
                         +exp(-t)u_t(x_t) cross curl u_t(x_t).

It follows that G(t)->E(v). The bracket in(15) converges to

    a grad S(v)-DV(v)^T E(v)

and is bounded for sufficiently large t. Integrate(15) from t to infinity and multiply by exp(t). Dominated convergence with the integrable kernel exp(-s) gives precisely(4). All limits are for the specified orbit. Uniformity on a noncompact set of initial points is not claimed.

## 5. Pressure-deficit zeros on a parallel level orbit

Under(5), H-g=P-|U|^2/2 gives S_t(x_t)=0 exactly. Uniform convergence and x_t->v imply S(v)=0. The parallel identity in(5) gives

    G(t)=a u_t(x_t)/(exp(mu t)f0-1)

for all sufficiently large t. If mu=1, exp(t)G(t)->aV(v)/f0. If mu>1, that limit is zero. Since E(v)=0, formula(4) identifies these same limits with -a grad S(v). This proves(6), including the negative sign and nonzero endpoint gradient.

For the A518 construction, mu=1 is rho=-2(1-c), and mu>1 is the strict lower branch. For A536, the endpoint is lambda=2(1-c)/(1-2c). Both interpretations require their global zero-helicity and natural-tail assumptions. The conclusion is a necessary regular or critical zero condition, not an exclusion of either branch.

## 6. Dependencies and review scope

The complete LIT138 source was read. A530 supplies canonical pressure convergence, A533/A538 supply C1alpha velocity convergence, and A538 supplies the additional W2q estimate for(12). Section2 uses the ordinary interior Schauder estimate. Sections3-5 are exact rescaling, weak differentiation and dominated convergence, all written out above. The direct formula(8)-(10) is an independent short derivation of the source's transport integral.

The existing configured-model Theory Agent C review of the local derivative estimate was read in full, as were its earlier pressure/scalar review and the coordinator's pressure review. The configured identifier is the primary model; provider runtime is not independently attested. These sources agree on the input statements. The new correction and actual-orbit coefficient are provided for continued file comparison. No new client, computation or external theorem about Euler continuation is used.
