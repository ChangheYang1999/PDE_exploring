# The first pressure correction and its exact value on escaping sheets

Status: A575-A576 CONFIRMED after full source and independent proof postreads; A577-A578 record the separate limitations. The theorem excludes c=3/7. The numerical independence test and the source's unqualified resonant asymptotic are not certified.

## 1. Exact hypotheses and the correction limit

Fix2/5<c<1/2, c!=3/7, and a finite real omega. Put p=(1-c)/c in(1,3/2), a=1-2c, A=cI-omega J and Q_t=exp(omega tJ), where J(x1,x2,x3)=(-x2,x1,0). Suppose U in C2(R3;R3), P in C1(R3) solve the full incompressible rotating Euler profile equations and the natural bounds

    |U(y)|<=C(1+|y|)^-p, |DU(y)|<=C(1+|y|)^(-p-1).   (1)

These bounds follow from U->0 and DU=O(sqrt r) in this exact global target class by the confirmed derivative-screen results. They are not deduced from bare decay. Helicity is not needed for the pressure theorem.

Write D=R3 minus{0}, Pinf for the canonical pressure constant, V for the actual leading velocity, and P2 for its canonical pressure. Define

    u_t(x)=exp((1-c)t)Q_t U(exp(tA)x),
    p_t(x)=exp(2(1-c)t)[P(exp(tA)x)-Pinf],
    S_t=p_t-|u_t|^2/2, S=P2-|V|^2/2,
    Z=DV V+grad P2, z_t=exp(t)(u_t-V),
    M1=V tensor Z+Z tensor V.                        (2)

A516,A530,A533,A538-A539 supply V in C^(1,alpha)_loc(D) for every alpha<1, P2 in C^(2,alpha)_loc, z_t->Z in C^alpha_loc for every alpha<1, and

    |u_t(x)|+|V(x)|<=C|x|^-p,
    |z_t(x)|+|Z(x)|<=C|x|^(-2p-1), t>=0.             (3)

Set m_t=u_t tensor u_t-V tensor V and m=m_0. Factor the difference as (u_t-V) tensor u_t+V tensor(u_t-V). This proves, also in the shrinking core,

    exp(t)|m_t(x)|<=C|x|^(-3p-1),
    exp(t)m_t -> M1 in C^alpha_loc(D).               (4)

Using the expanded z_t tensor z_t expression alone would not directly give a uniform bound at arbitrarily small x. The factorization avoids that issue. The bound for M1 follows by taking the limit.

Put r_k=(k+5)c-2 and K={integer k>=0:r_k<1}={k>=0:k<3p-2}. Thus K={0,1} ifc>3/7 and K={0,1,2} ifc<3/7. By A550 the following are absolutely convergent single-integrand moments and harmonic multipoles:

    Mom_k=integral y^(tensor k) tensor[U tensor U-V tensor V](y)dy,
    Theta_k(x)=-((-1)^k/k!)D^(k+2)N(x):Mom_k,
    N(x)=-1/(4pi|x|), Delta N=delta_0.                (5)

There is a unique continuous p1 on D with

    p1(exp(sA)x)=exp(-(3-2c)s)p1(x),
    -Delta p1=partial_i partial_j(M1)_ij on D.       (6)

The distributional equation is only asserted on the punctured space. Moreover, uniformly on every compact subset of D,

    exp(t)[p_t-P2-sum_K exp(-r_k t)Theta_k(Q_t^T x)] -> p1,
    exp(t)[S_t-S-sum_K exp(-r_k t)Theta_k(Q_t^T x)] -> S1=p1-V.Z.  (7)

Thus p1 and S1 depend only on V and its canonical P2; the global low moments have been subtracted explicitly. No derivative convergence of z_t or of the expression in(7) is asserted.

## 2. Exact finite-part pressure formula and uniform convergence

Fix an annulus r1<=|x|<=r2, choose0<d<r1/8, and let N_d=chi(x/d)N with chi smooth, equal1 at radius<=1 and0 at radius>=2. Put T_d F=(D^2N_d)*F with tensor contraction, and K_d=D^2(N-N_d). The canonical pressure formulas give

    p_t-P2=-T_d m_t-integral K_d(x-y):m_t(y)dy.       (8)

The local distribution T_d includes its trace contact term. Let chi0(y) be1 for |y|<=r1/4 and0 for |y|>=r1/2. On this inner support K_d(x-y)=D^2N(x-y). Write k*=1+max K. Taylor expansion gives

    D^2N(x-y)=sum_K F_k(x,y)+R(x,y),
    F_k(x,y)=((-1)^k/k!)D^(k+2)N(x)[y^k],
    |R(x,y)|<=C|y|^(k*)                             (9)

uniformly on the annulus. Since c!=3/7,

    k<3p-2 for k in K, while k*>3p-2.                (10)

The exact change of variables y=exp(-tA)Y gives

    integral y^(tensor k) tensor m_t(y)dy
       =exp(-r_k t) Q_t^(tensor(k+2)) Mom_k.          (11)

Contract(11) with the radial Newtonian derivative. The inner portion of(8) equals the multipole sum plus

    sum_K integral (1-chi0(y))F_k(x,y):m_t(y)dy
                       -integral chi0(y)R(x,y):m_t(y)dy.    (12)

Multiply the remaining near, outer and inner expressions by exp(t) and use(4). Their limits define explicitly

    p1(x)=-T_d M1(x)
          -integral(1-chi0(y))K_d(x-y):M1(y)dy
          +sum_K integral(1-chi0(y))F_k(x,y):M1(y)dy
          -integral chi0(y)R(x,y):M1(y)dy.            (13)

Every displayed nonlocal integral is absolutely convergent. The outer kernel is smooth with decay at least |x-y|^-3 and avoids y0. In each moment-compensation term, the radial majorant at infinity is r^(k+1-3p), integrable exactly by k<3p-2. In the inner remainder it is r^(k*+1-3p), integrable at0 exactly by k*>3p-2. Their estimates are uniform in x on the annulus. Dominated convergence, with uniform convergence on intermediate compact annuli and uniform tail majorants, proves uniform convergence of all these pieces.

For the local term choose a fixed cutoff equal1 on each relevant ball. The local Hölder convergence in(4) gives convergence of that cutoff tensor in C^beta,0<beta<alpha<1. The truncated singular integral is bounded from this compactly supported C^beta class to continuous bounded functions. Directly, subtract the value at x in its homogeneous kernel: the singular integral is bounded by C[F]_beta integral_0^(2d) r^(beta-1)dr, together with the trace term and smooth annular terms bounded by C||F||infinity. Hence the near piece converges uniformly as well. This step does need positive Hölder control, which A539 supplies; uniform C0 convergence alone would not justify it.

Formula(13) proves the first limit in(7), continuity, and independence of the auxiliary cutoffs because it is the limit of the exact expression. The second follows from

    exp(t)(|u_t|^2-|V|^2)/2=V.z_t+exp(-t)|z_t|^2/2 -> V.Z

uniformly on every fixed compact subset of D.

## 3. Homogeneity, the Poisson equation and uniqueness

The exact rescaling identity is p_t(exp(sA)x)=exp(-2(1-c)s)p_(t+s)(x). The same holds for P2 without the time shift. Since Theta_k has degree-(k+3) and (k+3)c=2(1-c)+r_k,

    Theta_k(Q_t^T exp(sA)x)
       =exp(-(k+3)cs)Theta_k(Q_(t+s)^T x).

Consequently the expression on the first line of(7), before taking its limit, at exp(sA)x equals exp(-(3-2c)s) times that expression at time t+s and point x. For every fixed real s, pass to the limit. This gives the homogeneity in(6).

On D, -Delta p_t=partial_i partial_j(u_t,i u_t,j), while -Delta P2=partial_i partial_j(V_i V_j). All Theta_k are harmonic there. Thus the negative Laplacian of the expression in(7) tends in distributions to partial_i partial_j(M1)_ij. Local uniform convergence identifies it with -Delta p1. No integral of M1 through0 is used as an unrenormalized source.

For uniqueness, the difference h of two solutions is continuous and distributionally harmonic on D, hence smooth harmonic there by Weyl's lemma. Project h(r,.) onto the spherical harmonics of degree l. The radial equation gives a_l r^l+b_l r^(-l-1), with a_l,b_l in the finite-dimensional degree-l harmonic space. Rotations Q_s act isometrically on that space. Project the homogeneity relation and compare the two independent radial powers. Taking norms gives, for every real s,

    exp(cl s)||a_l||=exp(-(3-2c)s)||a_l||,
    exp(-c(l+1)s)||b_l||=exp(-(3-2c)s)||b_l||.

The first forces a_l0. The second permits b_l!=0 only when l=3p. Since3p is in(3,9/2), the only integer possibility is l4, equivalently c3/7, which has been excluded. Every spherical harmonic projection vanishes, so h0. This proves uniqueness for every finite omega, without a bound uniform as c approaches3/7.

At c3/7 uniqueness actually fails under(6): the nonzero axisymmetric function |x|^-5 P4(x3/|x|) is harmonic on D and has the required twisted homogeneity for every omega. This does not determine the correction selected by an actual profile at resonance; it explains precisely why the present uniqueness theorem excludes it.

## 4. Exact sheet value

Now impose global U.curl U=0 and take an A536 regular vortical zero-g component Sigma with lambda>1, or the regular component of a vortical carrier equilibrium with rho<-a. Put mu=a(lambda-1)=-a-rho>0 using the effective rho. The confirmed sheet results supply mu>=1, H=Pinf on Sigma, g0, and the following scattering statements for every escaping z in Sigma:

    y_t=Phi_t(z), v_t=exp(-tA)y_t -> v!=0,
    |v_t-v|<=C_z exp(-t), S_t(v_t)=0, S(v)=0.       (14)

Indeed H-g=P-|U|^2/2, so H=Pinf and g0 give the exact scalar equality in(14). This argument includes f(z)=0; extra nonvanishing conclusions below require f(z)!=0.

The scalar part of A550-A551 gives

    Theta_k(Q_t^T v)=0 for every real t and every k in K.    (15)

For clarity, insert(14) in the multipole expansion with any gamma between max_K r_k and1. Since S is C1 and v_t-v=O(exp(-t)), the resulting finite sum of exp(-r_k t)Theta_k(Q_t^T v) is O(exp(-gamma t)). Each coefficient is periodic in t if omega!=0 and constant if omega0. Multiply successively by exp(r_k t); a periodic function tending to0 must vanish identically. This proves(15), without a derivative expansion at rate1.

Each Theta_k is smooth near the compact rotation circle through v, and r_k>0. Therefore

    exp(-r_k t)Theta_k(Q_t^T v_t)=O(exp(-(1+r_k)t))=o(exp(-t)).

The exact trajectory identity is v_t'=exp(-t)u_t(v_t). Integrate to its terminal limit. Uniform convergence near v gives

    exp(t)(v_t-v) -> -V(v).                          (16)

Since S is C1, S(v_t)=-exp(-t)grad S(v).V(v)+o(exp(-t)). Apply the uniform expansion(7) at the moving point v_t, using(15) and continuity of S1. Equality S_t(v_t)=0 gives

    S1(v)=V(v).grad S(v),
    equivalently p1(v)=2V(v).grad P2(v).              (17)

The equivalence follows because V.DV V=V.DV^T V and Z=DV V+grad P2.

On Sigma*={f!=0}, where B cross W=f grad H, A534 gives V(v)!=0 and: if mu1, grad S(v)=-V(v)/f(z); if mu>1, grad S(v)=0. Consequently

    mu1: S1(v)=-|V(v)|^2/f(z)!=0;
    mu>1: S1(v)=0.                                  (18)

These are necessary conditions on actual escaping sheets. They do not exclude any of the presently remaining nonaxisymmetric rates by themselves.

## 5. What has and has not been verified

The full C39 Lemma27, Theorem28, Remark29 and the C38 exact pressure split were read, along with the confirmed tail-correction proof. This note independently verifies every uniform majorant, local singular-integral limit, scaling factor, harmonic resonance and moving-point substitution. No computation was needed. The actual source is the existing configured-model Theory Agent C agent; its findings and the precise limitations are returned through the auditor files. No new client or provider execution attestation is claimed.

The table in Remark29 is explicitly numerical, but its following assertion that condition(17) is not a consequence of four reduced conditions is not proved by approximate residuals alone. Its reported zero near c0.421577 and its tiny nonzero residuals have no supplied interval error bounds. They are observations, not certified independence or existence statements. The CO28 fields also omit the rank equation, so even a certified reduced counterexample would not settle dependence under all actual-tail conditions. A570 now excludes their whole axisymmetric actual-tail class under the full hypotheses.

Remark29(3)'s categorical statement that Mom2 diverges logarithmically at c3/7 is false as a universal claim: the exact global profile U0,Pconstant has V=Z=M1=0 and Mom2=0. More generally the upper bound in A550 permits a borderline logarithm but does not prove a nonzero coefficient or rule out oscillatory cancellation. The singularity of the integral estimate and the explicit harmonic ambiguity above are exact. The asserted detailed t exp(-t) and periodic correction formula has not been established here; it remains a separate resonant problem.

No limit for Dz_t, no higher-order correction, no unrestricted nodal statement and no bare-decay gradient bound is inferred. The generic-c pressure theorem is independent of helicity; its sheet application retains all global helicity and natural-tail assumptions. All finite omega are covered, including0. The isolated exponent c3/7 is explicitly outside this new theorem, while earlier generic multipole bounds A550-A552 remain valid there at their stated weaker remainder.
