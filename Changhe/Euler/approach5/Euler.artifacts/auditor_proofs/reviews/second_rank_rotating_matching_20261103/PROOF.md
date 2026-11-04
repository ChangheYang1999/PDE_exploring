# Second-order rank obstruction for rotating harmonic germs

## 1. Exact statements

Let 0<c<1/2, c!=1/3, omega any finite real number, a=1-2c, d=1-c, Jx=e3 cross x, A=cI-omega J and X=Ax. For a local C4 harmonic function f satisfying X.grad f=-af, at a point with grad f!=0, the field R=grad f cross(D2f grad f) cannot satisfy R=DR=D2R=0. Only its fourth jet is used.

Consequently, for 1/3<c<1/2 and every omega, let V in C3(D;R3), P in C3(D), D=R3 minus{0}, satisfy div V=0, DV X=-((1-c)I+omega J)V and Delta P=-tr((DV)^2). Put W=curl V, k=X.V, E=|V|^2, S=P-E/2 and F=grad k cross grad S. Assume F=0 on W!=0. Then no nonzero irrotational open germ can have Q=P+E/2 identically zero. No pressure homogeneity or scalar comparison is imposed. The global C3 premise and the zero remainder are retained.

## 2. What vanishing through second order implies

At the point write g=grad f, e=|g|^2>0, H=D2f and T=D3f. Define lambda=(g.Hg)/e and z=Hg-lambda g in a neighborhood. Since g.z=0 identically and R=g cross z, successively differentiating shows z=Dz=D2z=0: at each order the remaining derivative of z is both parallel and orthogonal to g because all lower ones have vanished.

D(Hg)=T_g+H^2 is symmetric. The skew part of Dz is therefore the negative skew part of g tensor grad lambda. This and its first derivative vanish. Set kappa=(g.grad lambda)/e and h=grad lambda-kappa g. Applying the same parallel-and-orthogonal argument gives h=Dh=0. Therefore grad lambda=kappa g and D2lambda=kappa H+g tensor grad kappa. Symmetry of this Hessian gives grad kappa=gamma g for some real gamma. The original Dz=0 identity becomes

    T_g=lambda H-H^2+kappa g tensor g.

All these identities involve at most fourth derivatives. Harmonicity gives tr H=0 and tr T_v=0 for every v.

## 3. Trace and homogeneity contradiction

The neighborhood identity tr Dz=|H|^2-g.grad lambda, evaluated and differentiated at the point, gives

    |H|^2=kappa e,
    grad |H|^2=(2 kappa lambda+gamma e)g.

Contract the second identity with g. From the tensor identity in Section2 the same contraction is 2 tr(T_g H)=4 kappa lambda e-2 tr(H^3). Hence

    tr(H^3)=kappa lambda e-gamma e^2/2.

Under the local flow F_t=e^(ct)exp(-omega tJ), the gradient scales as e^(-dt) times that rotation and the Hessian as e^(-t) times rotational conjugation. Thus lambda scales as e^(-t), and its gradient as e^(-(1+c)t) times the rotation. The defining quotient for kappa then scales as e^(-2ct). No completeness beyond small local times is needed.

Differentiated homogeneity gives HX=-((dI+omega J)g). Contract with g, use Hg=lambda g, g.Jg=0 and X.g=-af to obtain af lambda=de. In particular f and lambda are nonzero. The identities Xlambda=-lambda and Xkappa=-2c kappa now give

    kappa=lambda^2/(de), gamma=2c lambda^3/(d^2 e^2).

The trace formula becomes tr(H^3)=a lambda^3/d^2. On the other hand H has eigenvalues lambda,mu,nu, with mu+nu=-lambda and tr(H^2)=lambda^2/d. Hence mu nu=a lambda^2/(2d). Their sum of cubes is three times their product, giving tr(H^3)=3a lambda^3/(2d). Since a lambda!=0, equality forces 3d=2, or c=1/3. This proves the local contradiction for every rotation. At c=1/3, f=C/|x| is a real countertest: harmonic off zero, satisfying the scalar transport for every omega, with nonzero gradient and R identically zero.

## 4. The global germ supplies precisely the forbidden jets

Let O be the component of int{W=0} containing a forbidden germ. Homogeneity makes it invariant under the explicit linear flow. The Lamb identity grad k=-aV+X cross W gives V=-grad k/a and Delta k=0 on O. Also Q is harmonic there because DV is symmetric and Delta(E/2)=tr((DV)^2). Unique continuation gives Q=0 on O.

There is a relative boundary point x* in D with V(x*)!=0. To see this, suppose otherwise. With sigma=omega/c and m=a/c in(0,1), use coordinates x=r exp(-sigma log r J)n. They identify O with positive r times an angular open domain. Write k=r^(-m)psi(n). Its harmonic equation is

    (Delta_S2+sigma^2 Y^2+sigma(1-2m)Y+m(m-1))psi=0,
    Y=(Jn).grad_S2.

The principal part is positive elliptic; the zeroth-order coefficient is strictly negative. Under the supposed boundary condition psi vanishes on its angular boundary. Its compact closure therefore admits no positive or negative extremum, so psi=0. The same argument includes the full sphere. This would make V=0 on O, a contradiction. Thus x* exists. It lies in supp W, because a connected irrotational ball about it would join O and contradict boundary membership.

The global C3 pair makes F a C2 field. On the open vortical set F and its derivatives through order2 vanish; continuity extends all those zeros to x*. On O put f=k. Its one-sided derivatives through order4 are g=-aV, H=-aDV, T=-aD2V and D4f=-aD3V, all having continuous limits at x*. Symmetry, harmonicity and differentiated homogeneity persist in the limits. Also g!=0 and F=-(2/a^2)R on O, with the same identity differentiated twice. Thus the limiting jets satisfy R=DR=D2R=0, contrary to Section3. There is no global C4 potential assumption and no derivative D3W.

## 5. Verification and limitations

All six submitted sections and these five independent sections were read. Both scalar homogeneity exponents, both cubic trace calculations, the rotating angular operator and every derivative order were independently checked by hand. The proof uses harmonic regularity, harmonic unique continuation and a compact maximum argument. No numerical computation is needed.

LIT276 supplies first-order stationary rank zeros for nonzero rotation and is consistent with this second-order obstruction. The latter requires C3 rather than C2 for arbitrary rotation. Nonzero harmonic remainder, natural C1,alpha matching, global regularity improvement and the bare-decay conjecture remain open. The local algebraic range is broader than the global matching range; the latter uses m in(0,1).
