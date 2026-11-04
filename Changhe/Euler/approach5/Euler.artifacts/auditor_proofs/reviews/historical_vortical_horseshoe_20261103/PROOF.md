# Historical vortical-horseshoe construction audit

## 1. Exact scope, notation and regularity

Let O be open in R3, 0<c<1/2, omega real, J(x,y,z)=(-y,x,0), A=cI-omega J, k=1-2c>0 and lambda=1+c. Let U in C2(O;R3), P in C1(O) satisfy

    (1-c)U+(B.grad)U+omega JU+grad P=0,
    div U=0, B=Ay+U, Omega=curl U.                     (E)

The derivative convention is (DU)ij=partial_j U_i, and [V,W]=(V.grad)W-(W.grad)V. Write Phi_s for the maximal flow of B and Psi_t=Phi_(-t). Compact invariance below means invariance in both time directions. For K compactly contained in O this also gives complete trajectories: a finite maximal endpoint would lie in a compact neighborhood where B is bounded and locally Lipschitz, allowing the ordinary differential equation to be continued. There is no claim that every trajectory in O is complete.

The original historical question, proof, answer and Cartesian checker are pinned in the team records. Every source section and the full checker were read. The algebraic replay passed in 3.944395709782839 actual seconds on CPU55, nice19, OMP1; its plan preceded execution. These algebraic checks are supplementary to the arguments below. The retained answer has one absolute Markdown target replaced by its relative pinned target; both hashes and the path-only normalization are recorded.

The conclusions concern local exact profiles, compact invariant dynamics and necessary conditions. They neither construct nor exclude a general vortical horseshoe. The original question's F6 explicitly assumes a>0, kappa nonzero and omega nonzero. Those conditions are retained when discussing its periodic orbit, despite the abbreviated restatement in the source proof. No decay at infinity is assumed or proved here. The existence assertions in the question's F5 and F8 are not used.

## 2. Lamb form, vorticity transport and pressure periods

Let nu=dy1 wedge dy2 wedge dy3, beta=U.dy and alpha=(B cross Omega).dy. The elementary vector identity

    grad((Ay).U+|U|^2/2)=A^T U+(B.grad)U+B cross Omega

and (E) give alpha=k beta+dH, where H=(Ay).U+|U|^2/2+P. Although P was assumed only C1, (E) makes its gradient C1 and hence P is C2, so the following differentiations are legitimate. Direct exterior differentiation and contraction give

    d beta=i_Omega nu, i_B d beta=-alpha,
    d alpha=k d beta, alpha(B)=0, L_B alpha=-k alpha.

The last equality is Cartan's identity i_B d alpha+d(alpha(B)). Thus Phi_s^*alpha=e^(-ks)alpha. Taking the curl of the Lamb equation gives

    curl(B cross Omega)=-3c Omega-[B,Omega]=k Omega,
    [B,Omega]=-lambda Omega,
    D Phi_s Omega(x)=e^(lambda s)Omega(Phi_s x).        (1)

Here div B=3c and div Omega=0. Conversely the bracket and divergence equations make alpha-k beta closed. A single-valued pressure exists on O precisely when this closed form is exact, or equivalently has zero integral around every closed curve in each connected component. If it is dH, define P=H-(Ay).U-|U|^2/2 and reverse the calculation. This is the full global period condition on O, not a normalization at infinity.

Cartan's formula also gives L_B beta=-k beta+d(beta(B)-H). Integrating over a transported closed curve yields circulation multiplied by e^(-ks). A periodic B-orbit has zero circulation, either because its time-shifted image is the same oriented curve or by integrating BH=-k U.B over one period. Curl transport alone does not imply this period condition on a multiply connected domain.

## 3. The exact nonrotating conclusion and its counterexample

Put X=cy+U, Q=P+c(c-1)|y|^2/2 and H0=Q+|X|^2/2. Substitution into (E) gives

    (B.grad)X+kX+omega JX+grad Q=0,
    BH0=-k|X|^2-omega(Jy).grad P.                     (2)

For omega=0, X=B, so H0 decreases strictly along every nonstationary orbit. A recurrent point must be stationary: if B(x) is nonzero, H0 decreases by a definite positive amount during a short initial interval, remains nonincreasing thereafter, and cannot return to its initial value along a sequence returning to x.

Every invariant probability on compact K is supported on equilibria. For clarity this also holds for a probability invariant merely under the time-one map: integrate

    H0(Phi_1 x)-H0(x)=-k int_0^1 |B(Phi_s x)|^2 ds.

The left integral is zero by invariance, while the right integrand is continuous and nonnegative. It follows that B=0 almost everywhere and hence on the measure's support. The metric entropy of its time-one map is zero. The variational principle for a continuous self-map of a compact metric space then gives zero topological entropy. This invocation needs no assumption that a time-one invariant probability was already invariant for the whole flow. The standard variational principle is the sole entropy-theoretic input here.

The assertion that every compact invariant set consists of equilibria is false even for a smooth exact nonrotating profile. Let

    phi=-x^3/3+x y^2, U=grad phi,
    P=-k phi-cy_vector.grad phi-|grad phi|^2/2.

Since Delta phi=0, U is divergence free; the gradient form of the Lamb identity gives (E). Its carrier is

    B=(cx-x^2+y^2, cy+2xy, cz).

The compact segment {(x,0,0):0<=x<=c} is invariant. Its interior solves x'=x(c-x), a complete heteroclinic connection between the endpoint equilibria. Thus absence of recurrence is a statement about nonstationary recurrent points, not absence of nonstationary points in compact invariant sets. The polynomial U is not a decaying global counterexample to the campaign conjecture.

## 4. Uniform hyperbolicity and normalized return coordinates

Suppose K is compactly contained in O, fully invariant, and B and Omega never vanish on K. They cannot be parallel at a point x: if Omega(x)=q B(x), (1) and D Phi_s B=B(Phi_s x) imply Omega(Phi_s x)=q e^(-lambda s)B(Phi_s x). Compactness bounds B above and |Omega| below, contradicting this identity as s tends to positive infinity. Hence alpha is nonzero near K.

Set n=alpha_sharp/|alpha|^2. Since alpha(n)=1 and L_B alpha=-k alpha,

    [B,n]=kn+fB+gOmega

for continuous f,g bounded on K. Define uniformly convergent integrals

    a(x)=int_0^infinity e^(-ks) f(Phi_s x) ds,
    b(x)=int_0^infinity e^(-(k+lambda)s) g(Phi_s x) ds.

These functions are continuous by dominated convergence. A change of variables along an orbit, followed by the fundamental theorem of calculus, gives Ba=ka-f and Bb=(k+lambda)b-g. This only requires differentiation along the orbit; ambient differentiability of a,b is not assumed. Thus S=n+aB+bOmega satisfies [B,S]=kS along orbits, and the variational equation yields

    D Phi_s B=B(Phi_s x),
    D Phi_s Omega=e^(lambda s)Omega(Phi_s x),
    D Phi_s S=e^(-ks)S(Phi_s x).                       (3)

Because alpha(S)=1, B,Omega,S form a continuous frame on K, with bounded frame and inverse. Equation (3) proves uniform hyperbolicity. For Psi the stable line is R Omega with decay e^(-lambda t), the central line R B, and the unstable line R S with growth e^(kt), up to uniform bounded factors. The argument remains true for a divergence-free C1 field W in place of Omega, provided the same bracket and divergence identities hold and B,W are nonzero on K. It therefore supplies no new obstruction based on W=curl U.

Choose a local section tangent to Omega and transverse to B. Since d alpha=k i_Omega nu, its restriction to this section is closed and nonzero. Choose u so alpha|section=du and v as the actual flow parameter of Omega, so Omega=partial_v. These choices are compatible because alpha(Omega)=0. For a return map R(x)=Psi_tau(x)(x) to another such section, differentiate the hitting condition in the Omega direction. The transported Omega lies in the target section, whereas B is transverse, forcing Omega tau=0. Pulling back alpha gives

    d u_out=e^(k tau)du,
    partial_v v_out=e^(-lambda tau).

Consequently, on each local branch,

    R(u,v)=(F(u), F'(u)^(-lambda/k)v+G(u)),
    tau(u)=log(F'(u))/k.                              (4)

For a positive return time F'>1. Merely assuming Omega parallel to partial_v, without its exact normalization, would not justify the displayed affine coefficient.

## 5. An abstract horseshoe obeying the return constraints

Let p=lambda/k>1, rho=3^(-p)<1/3 and T=log(3)/k. On the two strips [0,1/3]x[0,1] and [2/3,1]x[0,1], define branches

    R0(u,v)=(3u,rho v),
    R1(u,v)=(3u-2,rho v+1-rho).

Both extend smoothly to separate neighborhoods. The maximal two-sided invariant set has a unique bi-infinite binary itinerary: future symbols specify the ternary 0,2 digits of u, while past symbols specify v through its contracting affine recursion. Conversely each itinerary determines both coordinates by convergent series. This is a conjugacy with the two-sided full shift. The images lie in disjoint horizontal strips, so the restriction is an invertible Cantor dynamics.

Both branches satisfy (4), with time T, derivative diag(3,rho) and determinant

    3rho=exp((k-lambda)T)=exp(-3cT).

Its constant-roof suspension is an abstract compact flow with entropy log(2)/T. The suspended derivative cocycle has exponents k,0,-lambda. This statement is about the abstract return system and its cocycle; it does not construct a smooth Euclidean vector field, specify a Euclidean curl, solve a pressure period, or realize an Euler profile. It shows only that the displayed return identities alone permit positive entropy.

## 6. Cylindrical profiles, exact pressure and tube isolation

On r>0 take kappa nonzero and real constants C,D, with

    U_r=-r/2+C/r, U_theta=kappa r+D/r, U_z=z.

Cylindrical differentiation gives div U=0, Omega=2 kappa e_z and [B,Omega]=-lambda Omega. Direct substitution gives

    alpha-k beta=dHstar-(2 kappa C+kD)dtheta,
    Hstar=[kappa(kappa-omega)+k/4]r^2
          +(2 kappa D-kC)log r-k z^2/2.

On a full annular product domain, dtheta has period 2pi around the angular circle, while Hstar is single-valued. The necessary and sufficient pressure condition is therefore 2 kappa C+kD=0. This proves, in particular, that arbitrarily small changes of D alone can preserve the bracket while destroying single-valued pressure.

For a>0 set C=ka^2/2 and D=-kappa a^2. The condition holds and a pressure is

    P=(kappa^2/2+1/8)r^2
      -(2 kappa^2+k^2/2)a^2 log r
      -(kappa^2/2+k^2/8)a^4/r^2-z^2.                 (5)

All three original momentum components and divergence vanish exactly, as also checked by the retained Cartesian replay. The pressure is smooth and single-valued for r>0, and may be shifted by a constant. With q=r^2-a^2 the carrier equations are

    q'=-kq, z'=lambda z,
    theta'=kappa-omega-kappa a^2/r^2.                 (6)

Any full trajectory in a compact subset of r>0 must have q=z=0, since the explicit exponentials in (6) otherwise diverge in one time direction or reach the excluded axis. On this circle theta'=-omega. For omega nonzero this is a periodic orbit of period T0=2pi/|omega| with Phi normal exponents -k,lambda. For omega=0 it is a circle of equilibria, not a periodic orbit, and the following periodic-orbit continuation proof does not apply. The source's original F6 assumed omega nonzero; this qualification must accompany its abbreviated standalone restatement.

For Psi, q'=kq,z'=-lambda z, so the derivative of q^2-z^2 is 2kq^2+2lambda z^2. The periodic orbit is isolated in a sufficiently small tube. This remains true under sufficiently small C1 perturbations defined on a slightly larger tube: angular speed stays nonzero, giving a local return map, and the fixed point continues since its derivative diag(e^(kT0),e^(-lambda T0)) has no eigenvalue 1. After recentering, a small disk has

    Q(Rx)-Q(x)>=delta |x|^2, Q(x)=x1^2-x2^2, delta>0.

For a two-sided orbit remaining in this disk, telescoping and boundedness give summability of |x_n|^2 over all integers, so x_n tends to zero at both ends. Telescoping again with zero endpoint limits implies x_n=0 for every n. Thus any perturbed homoclinic excursion must leave that small tube. This is ordinary local hyperbolic isolation and does not prove rigidity of the full family of nearby Euler solutions.

## 7. Product reductions and the exact perturbation obstruction

Suppose Omega=q e is a constant nonzero vector and the domain is a product with connected fibers in the e direction. Equation (1) gives partial_e B=lambda e. In coordinates (xi,z) with e=partial_z this integrates to

    B(xi,z)=(b(xi),lambda z+h(xi)).                    (7)

If two points of a compact full invariant set have the same xi, uniqueness of the planar ordinary differential equation keeps their xi trajectories identical and their z difference equals e^(lambda s) times its initial value. Boundedness for positive time forces that difference to vanish. Projection is therefore an injective continuous map from the compact set into the plane, hence a homeomorphism onto its image, conjugating the flows. The product condition ensures b,h are single-valued; it cannot be discarded on an arbitrary domain.

For a regular invariant set, b is nonzero on its projection: if b(xi)=0, a full bounded orbit of z'=lambda z+h(xi) must be the vertical equilibrium, giving B=0. The planar Poincare-Bendixson theorem applied to this compact regular flow implies every recurrent point lies on a periodic orbit. Every ergodic invariant probability is then supported on a periodic orbit, so the variational principle gives zero entropy. In particular it cannot contain the requested horseshoe. These are the standard planar-flow and entropy inputs, with their regularity, compactness and no-equilibrium premises stated explicitly.

For the cylindrical background U0 in Section6, a single-valued potential perturbation U=U0+grad phi preserves constant vorticity. Divergence gives Delta phi=0. Subtracting the bracket equations yields partial_z grad phi=0, so on an annular product

    phi=f(x,y)+bz+constant, Delta_(x,y)f=0.

Thus (7) still applies. This is only a necessary condition; pressure periods can impose more restrictions. In contrast, a general perturbation u satisfies the linearized system

    div u=0,
    [B0,curl u]+lambda curl u-2 kappa partial_z u=0,

and the exact nonlinear bracket adds [u,curl u]. Choosing a divergence-free perturbation alone does not solve this equation or the pressure periods.

There is also a precise spectral obstruction. Let a hyperbolic B-periodic orbit of an exact background have period T0 and no normal multiplier e^(lambda T0). For every sufficiently C1-close exact profile, its continued periodic orbit has Omega=0. Otherwise (1) over its period T would give D Phi_T Omega=e^(lambda T)Omega. Since e^(lambda T)>1, this eigenvector is not the flow direction, and the same value is a normal multiplier. Continuity of period and monodromy contradicts the fixed spectral gap. This argument does not require the background orbit to be irrotational as a premise, although the gap already forces that conclusion there. It gives no obstruction for a deliberately resonant background and cannot be replaced by unquantified language about exponents of order one.

## 8. Verdict, dependencies and unresolved conclusions

The exact identities, corrected nonrotating conclusion, compact-set hyperbolicity, normalized return formulas, abstract compatible horseshoe, pressure-period obstruction, qualified cylindrical periodic orbit, local tube isolation, product reduction and spectral-gap statement are confirmed as proved above. The false original statement that every compact nonrotating invariant set consists of equilibria is explicitly refuted by Section3. The zero-rotation cylinder is an equilibrium circle, so periodic language there must retain omega nonzero from the original F6.

Dependencies are elementary vector and exterior calculus, local existence/continuation and variational equations for C1 vector fields, the inverse-function argument for a hyperbolic fixed point, the planar Poincare-Bendixson theorem on a compact regular invariant set, and the compact-space variational principle. The latter two are used only for the stated entropy consequences. No global trajectory completeness, pressure normalization at infinity, finite energy, helicity sign or derivative decay is inserted.

Neither a smooth Euclidean realization of the abstract horseshoe nor a general local Euler exclusion has been supplied. No exact nonlinear perturbative solution with a homoclinic return is established. No conclusion about attracting examples, all prescribed rotation rates, or smooth decaying global profiles follows. The source's preference for existence is a heuristic and receives no proof verdict. The historical external-agent model claim is not independently attested by this audit; current collaboration remains through the configured team files.
