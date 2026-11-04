# Localized remainder energy and weighted pressure work

## Exact assumptions and notation

Let 2/5<c<1/2 and omega be finite. Let U in C2(R3;R3) and P in C1(R3) solve the full divergence-free rotating profile equation, with A=cI-omega J, B=Ay+U. Assume U bounded, its distributional blow-down zero, and the Dini condition integral_1^infinity sup_(|y|>=r)|DU(y)| dr/r<infinity. Normalize P to its canonical Riesz-transform pressure, choosing its additive constant accordingly.

Use the confirmed scattering and finite-remainder theorems A209-A210 and A250. Their exact needed output is: S is a measure-preserving C1 diffeomorphism off the compact null set K, S^-1(0)=K, |S(y)-y|<=C, S Phi_s=exp(sA)S; V is continuous off0, distributionally divergence-free and twisted homogeneous; W=U-V belongs to L2; U-V=o(|y|^-k), |U|<=C(1+|y|)^-k, |Omega|<=C(1+|y|)^(-k-1), where k=(1-c)/c in (1,3/2). Put

    alpha=3-2k=5-2/c, gamma=(5c-2)/2=c alpha/2,
    q=|U|^2/2, f=-V.(Omega cross U),
    Jflux=(Ay)|W|^2/2+(q+P)W.

The letter Jflux is a vector flux, not the rotation matrix J. V and W are assigned arbitrary values at the origin, which does not affect any integral.

## The local and global flux identities

The linear tail equation is

    (Ay.grad)V=-(1-c)V-omega JV.

Subtract it from the profile equation and dot with W. Because W.JW=0, div W=0 and div(Ay)=3c, the product rule gives

    div Jflux=gamma|W|^2-W.((U.grad)U-grad q)
              =gamma|W|^2+V.(Omega cross U).

Thus f=gamma|W|^2-div Jflux. This identity is distributional when F=V|S2 is merely continuous. On every compact annulus the derivative of V along the smooth nonvanishing field Ay exists by its explicit homogeneity, and the product rule for |W|^2 follows in those flow coordinates. Products with q+P use div W=0 and smooth coefficients. Alternatively A250 supplies the required local weak derivatives.

At the origin, |W|=O(r^-k), and the flux through a sphere is O(r^(3-2k)+r^(2-k)), which vanishes. Therefore no point source is lost. The function f is absolutely integrable: it is O(r^-k) at0 and O(r^(-3k-1)) at infinity.

The velocity U is in L4, by boundedness near0 and its tail bound outside. This does not require W to be globally bounded: W generally is singular at0. The canonical pressure P is in L2 by boundedness of the double Riesz transform on U_i U_j in L2. Thus (q+P)W is in L1. Testing the local identity with a radial cutoff chi_R gives errors bounded by

    C integral_(R<|y|<2R)|W|^2+(C/R)||(q+P)W||_1,

which tend to zero. Consequently

    integral f=gamma||W||_2^2.

On the open irrotational set f=0, so div Jflux=gamma|W|^2 there.

## Arbitrary open domains and exact sign requirement

For a smooth compactly supported test chi,

    integral chi f=gamma integral chi|W|^2+integral Jflux.grad chi.

For an arbitrary open D choose 0<=chi_j<=1, smooth and compactly supported in D, tending pointwise to1_D. Since f and |W|^2 are in L1, the limit

    b_D=-lim_j integral Jflux.grad chi_j

exists and is independent of the chosen exhaustion. It satisfies

    N_D:=integral_D f=gamma integral_D|W|^2-b_D.

For bounded regular D it agrees with the usual outward flux, including the harmless integrable singularity at0. For unbounded D, this proof establishes the cutoff flux. Identification with an ordinary improper or absolutely convergent boundary integral requires a separate convergence argument and is not automatic from boundary smoothness.

If disjoint open D_i cover almost every point of {Omega!=0}, let E' be their complement. The family is countable and f=0 almost everywhere on E'. Moreover sum_i |b_Di| is finite, bounded by gamma||W||_2^2+||f||_1. Summing gives

    sum_i b_Di=-gamma integral_E' |W|^2<=0.

Thus N_D<=0 is exactly the additional inequality b_D>=gamma integral_D|W|^2. The identities do not prove it. If every b_Di>=0, they all vanish and W=0 almost everywhere on E'; this does not alone make W vanish on the D_i. If the stronger inequalities N_Di<=0 hold for every i, the global identity forces W=0.

On a regular B-invariant boundary patch, B.n=0 gives (Ay).n=-U.n, hence direct expansion yields

    Jflux.n=(P+U.V-|V|^2/2)U.n-(q+P)V.n.

Neither normal component vanishes merely because B or Omega is tangent.

## Bernoulli and fundamental-domain forms

Let H=P+q+(Ay).U and a=1-2c. The Lamb identity gives

    f=a V.U+V.grad H+V.(Omega cross Ay).

On bounded regular domains, div V=0 converts the middle term into the boundary flux H V.n. On the whole space these terms cannot in general be split into convergent integrals. In fact

    integral_(B_R) V.U=(R^alpha/alpha)||F||_2^2+O(R^(alpha/2)).

This follows from U=V+W, the exact integral of |V|^2, and Cauchy-Schwarz. It tends to positive infinity only when F is nonzero. The zero-profile exception must be retained.

For B-invariant open D and tau>0, set

    E_tau={y in D minus K:1<=|S(y)|<exp(c tau)}.

Its B-flow translates Phi_(n tau) E_tau, n in Z, partition D minus K up to boundaries of zero volume. The scattering map proves this directly in radial coordinates. It also gives |E_tau|<infinity. Since det D Phi_s=exp(3cs),

    N_D=sum_(n in Z) exp(3cn tau) integral_(E_tau) f(Phi_(n tau)y)dy.

The series is absolutely convergent because f is in L1. Its tails near K tend to zero. No scalar sign law for f follows from the vector vorticity-transport identity.

## Energy along B orbits

Put e_y(s)=|U(Phi_s y)|^2/2 and pi_y(s)=(U.grad P)(Phi_s y). Dotting the profile equation with U gives

    d/ds [exp(2(1-c)s)e_y(s)]=-exp(2(1-c)s)pi_y(s).

For this identity and its negative-time integral, only bounded U and the profile equation are needed, with 0<c<1. Every negative B orbit is bounded because y.B>=c|y|^2-||U||infinity|y|. Along its compact closure U.grad P is bounded. Therefore the negative-time integral converges absolutely and

    |U(y)|^2/2=-integral_(-infinity)^0 exp(2(1-c)s)pi_y(s)ds.

Under the scattering assumptions and y outside K,

    lim_(s->infinity) exp(2(1-c)s)e_y(s)=|V(Sy)|^2/2.

Indeed Phi_s y is within a uniform bounded distance of exp(sA)S(y). After rescaling to a fixed annulus, the continuity of V and the uniform little-o remainder prove the limit. Integrating the orbit identity yields the full pressure-work limit, with no assertion of absolute convergence at positive infinity.

## Weighted basin pressure work

For any B-invariant open D set Sigma_D=pi(S(D minus K)). For each finite R>0 the integral

    I_D(R)=integral_(D intersect {|S|<R}) |S|^-alpha U.grad P

is absolutely convergent. The preimage of the bounded scattering ball is bounded, U.grad P is bounded there, and |S|^-alpha is locally integrable by measure preservation and alpha<3. Values on null K do not matter.

Parametrize z=exp(sA)w with |w|=1, so dz=c exp(3cs)ds dA(w). Because 3c-c alpha=2(1-c), changing variables and integrating the exact orbit derivative gives, for T=log R/c,

    I_D(R)=-c integral_(Sigma_D) exp(2(1-c)T)
                            |U(S^-1(exp(TA)w))|^2/2 dA(w).

The negative-time endpoint is zero uniformly, by bounded U. The positive-time integrands converge uniformly to |F(w)|^2/2: the same uniform tail and bounded-displacement estimate applies over all S2. They are uniformly bounded, so dominated convergence gives

    lim_(R->infinity) I_D(R)=-(c/2) integral_(Sigma_D)|F|^2.

This is -gamma times the basin energy constant of A274. It has no boundary term on D because the integration follows complete B rays of the invariant scattering cone. Its negative sign does not contradict the profile equation; an independent nonnegative pressure-work inequality would still be required for exclusion.

## Physical scaling and scope

For t<Tphys put s=-log(Tphys-t) and

    u(x,t)=exp((1-c)s)exp(omega sJ)U(exp(sA)x).

The profile equation is equivalent to the physical Euler equation with pressure exp(2(1-c)s)P(exp(sA)x). Homogeneity makes the same rescaling of V equal to V(x). Therefore

    ||u(t)-V||_2^2=(Tphys-t)^(5c-2)||W||_2^2 ->0.

Its derivative is exactly -(5c-2)(Tphys-t)^(5c-3)||W||_2^2; half this derivative equals -(Tphys-t)^(5c-3) integral f. This follows directly from the scalar norm formula and the proved global identity, without an unproved time-differentiation of a singular field. The renormalized energy difference also vanishes by A250's cross-term limit. None of these statements gives a new sign contradiction.

The audit confirms Theory Agent A C27 and B.9 with the explicit qualifications about the singular origin, unbounded boundary fluxes, and the zero-profile exception. All Dini and canonical-pressure inputs remain visible.

## Supplement: absolute convergence of the weighted pressure work

Retain this proof's full Dini hypotheses and 2/5<c<1/2, with k=(1-c)/c in (1,3/2) and alpha=3-2k in (0,1). The previously proved signed limit is in fact an absolutely convergent integral.

The checked tail theorem gives |U(y)|<=C(1+|y|)^-k, hence U in L4 and canonical P in L2. The localized div-curl estimate in the team records gives g=(U.grad)U in L2. Since Delta P=-div g, the Fourier multiplier for grad P is the negative orthogonal gradient projection of g and is bounded on L2. This identifies the actual gradient: P is already the canonical L2 representative, so its Fourier transform is a function, and no polynomial gradient supported at frequency zero can be added. Therefore grad P belongs to L2.

Also |S|^-alpha U belongs to L2. On {|S|<R0}, boundedness of U and measure preservation of S give

    integral_(|S|<R0) |S|^-2alpha |U|^2
       <=||U||_infinity^2 integral_(|z|<R0)|z|^-2alpha dz<infinity,

because 2alpha<3. The null set K=S^-1(0) can be assigned arbitrary integrand values. At infinity |S(y)| is comparable to |y| by its bounded displacement. The squared integrand is then O(|y|^(-2alpha-2k))=O(|y|^(-6+2k)), which is integrable because k<3/2.

Cauchy-Schwarz proves

    integral_R3 |S|^-alpha |U.grad P|<infinity.

Thus for every measurable D the weighted work is absolutely integrable, and for each invariant open D the already checked identity becomes

    integral_D |S|^-alpha U.grad P=-(c/2)integral_SigmaD |F|^2.

This strengthens A276. Its gradient and tail estimates use the actual curl coupling through their earlier inputs; it is not a statement about independent transported fields. No sign contradiction follows.
