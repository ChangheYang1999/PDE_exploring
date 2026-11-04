# Exterior gauge rigidity and the mirror plane

## 1. Statements, scope and dependencies

Let 0<c<1/2, omega be any real number, Jx=e3 cross x, A=cI-omega J, a=1-2c and b=1+c. Suppose U belongs to C2(R3;R3), P belongs to C1(R3), div U=0, U tends uniformly to zero at infinity, and

    (1-c)U + (B.grad)U + omega JU + grad P = 0,    B=Ax+U.

Put Omega=curl U and H0=P+|U|^2/2+(Ax).U. No bound on DU at infinity and no helicity assumption is made. The equation improves P to C2 locally. All pressures in this proof may be shifted by constants.

The exterior theorem is the following. If lambda is a nonzero real number and f belongs to C3(R3) with bounded gradient, and

    Omega.(U+lambda x+grad f)=0

outside a compact set, then U=0. This strengthens the smooth, 2/5<c<1/2 formulation of Theory Agent A C47 without altering its proof.

For the same C2 class, mirror symmetry U(Rx)=RU(x), R=diag(1,1,-1), forces Omega=0 on the entire plane x3=0. The basin conclusions below retain C-infinity regularity and 2/5<c<1/2 because they use the previously confirmed essential-basin and helicity-sign theorems. They are not silently extended to C2.

Dependencies are A014 (no nonconstant periodic Omega orbit), A048-A049 (complete volume-preserving Omega flow and almost-everywhere recurrence), and, only for the basin clauses, A207,A223,A308-A309. The full proofs in `auditor_proofs/proofs/vortex_geometry/PROOF.md`, `auditor_proofs/proofs/frozen_flow_recurrence/PROOF.md` and `auditor_proofs/proofs/helicity_sign_liouville/PROOF.md` were reread. Section 3 supplies the completeness and recurrence argument needed for the regularity extension. No numerical evidence enters.

## 2. Exact algebra and pressure reduction

For a C2 divergence-free U, define B=Ax+U whether or not the momentum equation holds. Its residual without pressure is

    aU + grad(|U|^2/2+(Ax).U) - B cross Omega.

Taking curl gives [B,Omega]+b Omega. Indeed,

    curl(B cross Omega)=-3c Omega-[B,Omega],

because div Omega=0 and div B=3c. Therefore the pressure equation is equivalent on simply connected R3 to

    [B,Omega]=-b Omega.

For a solution, the equivalent Lamb identity is

    aU+grad H0=B cross Omega.

For W=U+lambda x+grad f and Q=H0-a(lambda |x|2/2+f), it gives

    aW+grad Q=B cross Omega,    Omega.Q=-a Omega.W,
    curl W=Omega,    W.flat wedge dW.flat=(Omega.W) dx1 wedge dx2 wedge dx3.

The last identity is the exact Frobenius condition used below. The notation W here denotes a gauge-shifted velocity, not a far-field vorticity. Also B.H0=-a U.B, and [B,Omega] applied to U.B yields B.(U.Omega)=-b U.Omega+Omega.(U.B).

## 3. Flow facts at C2 regularity

Write Phi_t for the B flow and Gamma_s for the Omega flow. Since U is bounded, B has linear growth, hence Phi is complete. Every negative Phi orbit starting in a fixed compact set stays in a larger compact set. One way to see this is the radial differential inequality B.r>=cr-||U||infinity and its backward counterpart. The Cauchy identity is

    Omega(Phi_t x)=exp(-bt) D Phi_t(x) Omega(x).

A local Omega existence time delta can be chosen uniformly on a compact set containing all Phi_{-t}x, t>=0. Conjugating those local solutions gives

    Gamma_s x=Phi_t Gamma_{exp(-bt)s}(Phi_{-t}x)

for |s|<=delta exp(bt). Uniqueness makes these definitions consistent. Letting t increase constructs the full Omega flow in both time directions. For x in a fixed bounded set, the radial Phi estimate gives

    |Gamma_s x| <= C(1+|s|)^(c/b).

Omega is C1 and divergence free, so this complete flow preserves Lebesgue measure. If a positive-measure wandering set for Gamma_1 had a bounded positive-measure subset F, its first N+1 disjoint images would lie in a ball of volume at most C(1+N)^(3c/b). This contradicts (N+1)|F| since 3c/b<1 exactly when c<1/2. Thus the time-one map is conservative. The measure recurrence theorem, applied to a countable basis of bounded balls, gives recurrence to the starting point for almost every point. The same argument applies backward.

For completeness, a periodic Omega orbit of period T would be carried by Phi_{-t} to an Omega orbit of period T exp(-bt), all inside one compact set. On that set Omega has a finite Lipschitz constant L. A nonconstant periodic solution of an L-Lipschitz autonomous field has a positive period lower bound: subtract its time mean, use the field Lipschitz bound and the periodic Poincare inequality to obtain T>=2pi/L. The shrinking periods contradict this. These arguments use only C2 U, boundedness and the displayed commutator, not a uniform derivative bound or a pressure normalization.

## 4. Exterior integral spheres

Set M=||U||infinity and Mf=||grad f||infinity. Since lambda is nonzero,

    W.theta=lambda r+O(1),    B.W=c lambda r^2+O(r),

uniformly in theta=x/r. Choose R0 large enough that Omega.W=0, |W.theta|>=|lambda|r/2 and B.W has the nonzero sign of lambda whenever r>R0.

In spherical coordinates the plane field ker W.flat is

    ker(dr+beta),    beta=r W_tan.dtheta/(W.theta).

Its angular norm is at most K=2(M+Mf)/|lambda|. It is C2, radially transverse and integrable by Section 2. For p with |p|=r0>R0+pi K, lift each shortest great-circle segment of length less than pi from theta0=p/r0 horizontally from p. The radial variation is at most K times the angular length, so all lifts stay in r>R0.

Here is the flat-connection detail. In local angular coordinates the horizontal fields are Xi=partial_i-beta_i partial_r. Their bracket is vertical. Integrability says it is horizontal as well, and radial transversality then makes it zero. Consequently neighboring horizontal lifts form an integral graph. Applying this observation along the radial fan of spherical geodesics shows that the lifted endpoints define a single C2 graph r=rho(theta) on S2 minus the antipode, with d rho=-beta and |grad rho|<=K. This is local path independence, not an unproved global holonomy assertion.

Near the antipode, the difference of rho at points on a small latitude is bounded by K times the short latitude length. Together with the meridional bound this proves a unique limiting radius. It is still larger than R0. In a sufficiently small Frobenius chart at the limiting point, the graph on a punctured spherical disk is connected and tangent to the plane field. Its plaque coordinate is constant, so it extends across the missing point by that plaque. The result is a compact embedded C2 sphere Sigma_p, everywhere normal to W and lying in the exterior region.

## 5. Recurrence on a sphere and completion of the exterior theorem

Omega is tangent to Sigma_p and its complete flow preserves this compact sphere. Let n=W/|W|. Projecting the Lamb identity onto the tangent plane gives

    grad_Sigma Q=(B.n) n cross Omega.

The scalar B.n is nonzero there. Thus Q restricted to Sigma_p is a regular first integral wherever Omega is nonzero.

Suppose Omega is nonzero at some point with r>R0+pi K. This is an open condition in three-dimensional space, so almost-everywhere volume recurrence supplies a recurrent point p in that open set. Construct Sigma_p only after choosing p. If Gamma_{s_j}p tends to p with s_j tending to infinity, then each return is on Sigma_p and on the level Q=Q(p). In a surface neighborhood of p that level is one regular arc and is parametrized by Gamma_tau p for |tau|<tau0. Embeddedness ensures that sufficiently close ambient returns are in this neighborhood. Therefore Gamma_{s_j}p=Gamma_{tau_j}p for bounded tau_j. This makes p periodic, contradicting Section 3.

It follows that Omega vanishes outside a ball. The bounded open set O={Omega!=0} is Phi-invariant by the Cauchy identity. Since div B=3c,

    |O|=|Phi_t O|=exp(3ct)|O|.

Finite volume forces |O|=0, and openness makes O empty. Finally div U=curl U=0 implies that each component of U is harmonic. Bounded harmonic functions on R3 are constant, and uniform decay makes that constant zero. This is the only last step that needs div U after the commutator has already been assumed.

The argument does not restrict volume recurrence to a prescribed null surface. It also does not assume that all regular first-integral levels on a sphere are periodic. It constructs a periodic orbit from one selected recurrent regular point.

## 6. Basin signs and finite one-sided variation

Now retain C-infinity regularity and 2/5<c<1/2. The confirmed basin theorem supplies a countable family of open sets D_nu contained in O, invariant under Phi and Gamma, covering O modulo a null set. Each carries a compactly supported full-flow ergodic physical probability nu, with nu(D_nu)=1 and almost every point of D_nu in its continuous-time basin. The helicity closure A309 states that one sign of U.Omega on every such D_nu, with signs allowed to differ, forces U=0.

For lambda!=0 and bounded grad f, suppose k=Omega.W has one sign on each D_nu. On such a set Omega.Q=-ak makes Q monotone along each complete vortex line. At a forward recurrent point, continuity returns Q arbitrarily close to its initial value, so monotonicity forces constancy. Therefore k=0 at almost every point in every D_nu, hence almost everywhere on O. It is zero outside O and is continuous, so it is zero everywhere. Section 5 applies. The pair (lambda,f)=(0,0) is exactly A309.

The sign condition may be weakened to

    min(integral_0^infinity k_+(Gamma_s x) ds,
        integral_0^infinity k_-(Gamma_s x) ds)<infinity

at almost every point of every basin. At a recurrent point the signed integrals along return times tend to zero, by Omega.Q=-ak. Finiteness of one monotone one-sided integral therefore bounds the other. Hence the absolute integral is finite. If k(x)!=0, continuity gives a fixed positive absolute integral on a short orbit interval starting near x. Infinitely many sufficiently separated return times yield disjoint such intervals and contradict finiteness. Thus k(x)=0, and the preceding closure applies.

For lambda!=0 the same argument works at C2 if the one-sided-variation premise is supplied at almost every point of O directly. This last formulation does not require the smooth basin construction. Recurrence by itself gives no such variation bound.

A nonzero smooth profile must consequently have an unbounded set where Omega.W!=0 for every allowed lambda!=0,f, and some essential basin must carry both signs. The corresponding assertions for two different gauges need not concern the same basin.

## 7. The mirror plane and the first normal jet

Let R=diag(1,1,-1) and assume U(Rx)=RU(x). Since R commutes with J and A, the equation implies P(Rx)=P(x): the difference is constant and vanishes on the fixed plane Pi. The curl transformation is Omega(Rx)=-R Omega(x). Hence on Pi, B3=U3=0 and Omega=w e3.

Set q=(B1,B2) on Pi. The third component of curl(B cross Omega)=a Omega gives

    div_2(wq)=-a w.

The chain rule for the locally Lipschitz function |w| gives div_2(|w|q)=-a|w| distributionally. On a circle of radius R>M/c, q.n>=cR-M>0. The divergence theorem, first for almost every R if necessary, yields

    0 <= integral_circle |w| q.n = -a integral_disk |w| <= 0.

Large such disks exhaust the plane, so w=0 everywhere. Thus Omega=0 on Pi, every point there is Gamma-fixed, Pi is Phi-invariant, and aU=-grad H0 there. Also h=U.Omega is odd under R. This proof works in the C2 class and for every 0<c<1/2.

For the normal-jet statement assume U is C-infinity. Define zeta=partial_3 Omega_h on Pi, beta=partial_3 B3=3c-div_2 q and eta=zeta1 dx2-zeta2 dx1. Differentiating the horizontal commutator before using w=0 gives

    [q,zeta]=-(b+beta)zeta+w partial_3^2 B_h.

After plane vanishing this becomes [q,zeta]=-(b+beta)zeta. Cartan's formula for eta=i_zeta(dx1 wedge dx2) then gives

    Lie_q eta=(div_2 q-b-beta)eta=-(a+2beta)eta.

The coefficient has no established sign. Plane vanishing alone is not unique continuation off Pi.

## 8. Mirror basins and the exact tests

For the smooth basin class in Section 6, D_nu is disjoint from Pi. Both open half-spaces are invariant under the complete Phi flow. Since nu(D_nu)=1, ergodicity puts nu in one half-space. If D_nu had a nonempty part in the other half-space, that open part would contain a basin-generic point. A nonnegative continuous compactly supported observable in the first half-space with positive nu mean would then have zero time average along this point's orbit, a contradiction. Thus D_nu lies wholly in one half-space.

Reflection conjugates Phi to itself, maps the basin of nu to the basin of R_*nu, and preserves null sets. The definition of D_nu as the maximal open subset of O whose non-basin part is null therefore gives R(D_nu)=D_{R_*nu}. These basins lie in opposite half-spaces. A sign of h on every upper-half-space basin gives a sign on every lower one by oddness and hence U=0 by A309. Conversely U=0 makes the condition vacuous. No basin is reflection-invariant, so oddness does not force a sign change inside one basin.

For omega!=0 the orthogonal maps commuting with J are diag(Rot_theta,epsilon), epsilon=+-1. Among the improper maps, only theta=0 has a positive-dimensional fixed set, namely Pi; all other improper maps have just the origin fixed. Proper rotations do have an axis of fixed points. The classification supplies no theorem exhausting useful symmetry arguments.

Two direct exact examples test these conclusions outside the decay class. Write coordinates (x,y,z). First, take omega!=0 and

    U=((c-1)x-omega y, omega x-cy, z),
    P=(c(1-c)+omega^2)(x^2+y^2)/2+a omega xy-z^2.

Then B=(-ax,0,bz), Omega=2omega e3, h=2omega z and

    H0=a((1-c)x^2+2omega xy+cy2-z^2)/2.

For a linear field U=Mx the full momentum equation is equivalent to M+M^2+omega[J,M]+Hess P=0, with tr M=0. Substituting this displayed matrix verifies both identities entry by entry. Its backward carrier flow is (exp(at)x,y,exp(-bt)z), with exponents (a,0,-b). Every invariant probability is supported on x=z=0, by recurrence under the expanding and contracting coordinates; its ergodic probabilities are Dirac masses and have no ambient physical basin. Gamma is a translation. The field is mirror symmetric but not decaying, and Omega does not vanish on Pi. Thus it is a test of local algebra and of the necessity of a global hypothesis, not a counterexample to the target conjecture.

Second, at omega=0,

    U=(b x+z^2,0,-bz),
    P=-b(2+c)x^2/2-bc z^2/2.

Direct substitution gives div U=0 and the full momentum equation. Here Omega=(0,2z,0), so Omega vanishes exactly on Pi. On the plane, q=((1+2c)x,cy), zeta=(0,2), beta=-1 and [q,zeta]=-c zeta, agreeing with the jet law. This nondecaying example prevents deriving off-plane vanishing from plane data and the local equations alone.

## 9. Source qualifications and open steps

The mathematical exterior, basin and mirror theorems above are confirmed. The method-classification table in C47 Section 6 is not a theorem and is not promoted.

There is an explicit defect in saying that every step of the full exterior U=0 theorem survives the T1 compact gauge replacement. Take U=0, Omega=0, B=Ax, H0=0 and a nonzero compactly supported smooth F. Put v=-grad F/a and Hnew=F. Then a v+grad Hnew=B cross Omega, curl v=Omega, all exterior gauge conditions and geometric inputs hold, and v is bounded and decaying. But v is nonzero, because div v=-Delta F/a need not vanish. The final harmonic step of Section 5 therefore fails. Under the replacement f_new=f+F/a, the shifted pair (W,Q) is unchanged; the geometric conclusion Omega=0 is gauge-invariant, while the full velocity conclusion needs the divergence condition. This refutes the literal definition of T1-blind as every step going through, and does not refute Theorem E for actual profiles.

Similarly, a decoupled-model comparison is conditional on checking all the stated flow, divergence and regularity hypotheses on that model. A claim that only one known identity can distinguish it, or that the listed null tests exhaust scalar methods, is not established by these arguments.

For omega!=0, Ax cannot be represented as lambda x+grad f as a vector field, because curl(Ax)=-2omega e3. This does not by itself rule out a scalar coincidence Omega.Ax=Omega.(lambda x+grad f) for a particular field Omega. What is established is that B.Omega=0 is not the Frobenius condition for ker B.flat: that condition is B.Omega-2omega B3=0. A basin sign of B.Omega has no proved closure here.

A sign only outside a compact set, a sign near a physical-measure support, and the case lambda=0 with a general bounded grad f remain open by these methods. So do propagation of H0=0 from such supports, nonlocal pressure signs and the exclusion of a basin carrying both helicity signs. The positive weighted quantity integral exp(-|x|2)h^2/(1+h^2) merely repackages h=0; no identity shown here forces it to vanish. For omega!=0, B.(cx+U)=|B+(omega/2)Jx|2-(omega2/4)|Jx|2 is not coercive. No unrestricted nonzero-rotation nonexistence theorem follows.
