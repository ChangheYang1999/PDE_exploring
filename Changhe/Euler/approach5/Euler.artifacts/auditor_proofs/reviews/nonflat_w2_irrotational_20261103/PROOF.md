# Nonflat W2 zeros, their transverse geometry, and local irrotational models

Status: independently checked at the exact conditional actual-tail and local-model scopes below. The full six-section B56 consultation and both parent statements were read. Read after A1130-A1131 and A1185-A1186. The parent phrase about all approach directions needs the transverse qualification in Section5.

## 1. Hypotheses and actual-profile dependencies

Fix2/5<c<1/2 and finite omega. Set A=cI-omega J, L=(1-c)I+omega J, X(x)=Ax, a=1-2c, b=2(1-c), p=(1-c)/c and q=b/a>6. Let V be the actual natural tail of the C2 zero-helicity profile under the campaign's natural decay hypotheses, and let W=curl V, k=X.V, S=P2-|V|^2/2. Thus V is C1,alpha for every alpha<1, P2 is C2,alpha locally, and

    div V=0, V.W=0, -Delta P2=tr((DV)^2),
    W.grad S=0, grad k cross grad S=0 on {W!=0},
    V(exp(sA)x)=exp(-sL)V(x),
    k(exp(sA)x)=exp(-as)k(x), S(exp(sA)x)=exp(-bs)S(x).

Suppose w is an escaping lower-window W2 direction with M=DV(w)!=0. The previously audited A1130-A1131 give V=W=S=P2=0 at w, w in supp W, w outside closure Z for Z=int{k=0}, and open irrotational patches accumulating at w. They also give ell=grad S(w)=grad P2(w), with ell=C_u m_infinity, C_u>0, at rate rho=-b; ell=0 at the strict rate rho<-b. These are actual-profile inputs, not consequences of an arbitrary local tail.

The exact scattering map is C1 with invertible derivative and W(Xi y)=D Xi(y)Omega(y). At a zero of W this implies point differentiability

    DW(w)=T D Omega(y0) T^(-1), T=D Xi(y0), y0=Xi^(-1)(w).

Indeed Omega(y0)=0, so continuity of D Xi suffices for the product expansion. No D2 Xi is needed. The C1 map follows from the integral variational equation with coefficient exp(-tA)DU(Phi_t y)exp(tA), whose norm is O(exp(-t)); its inverse converges, and its determinant is1. The Cauchy vorticity identity gives the displayed push-forward formula. These steps retain the actual escaping and natural-bound hypotheses.

## 2. Irrotational potentials have an independent harmonic pressure term

Differentiating homogeneity and k gives

    DV X=-LV, grad k=X cross W-aV.

On any open irrotational component, phi=-k/a is a single-valued potential, V=grad phi, Delta phi=0 and X.grad phi=-a phi. The Bochner differentiation gives Delta(|grad phi|^2/2)=|D2 phi|^2. Hence Q=P2+|grad phi|^2/2 is harmonic and has weight -b. Conversely every harmonic pair phi,Q with weights -a,-b supplies

    V=grad phi, k=-a phi, P2=Q-|grad phi|^2/2,
    S=Q-|grad phi|^2,

satisfying all displayed local tail equations. In particular Delta S=-2|D2 phi|^2. The equations do not require DV V+grad P2=0; that expression equals grad Q. A full original-profile Bernoulli formula cannot be imposed on this tail pressure without another argument.

For a scalar with twisted degree d and tau=omega/c, the angular harmonic operator is

    L_d=Delta_S+tau^2 K_rot^2+tau(2d+1)K_rot+d(d+1).

This follows by replacing r partial_r by d+tau K_rot in the polar Laplacian. For phi, d=1-p lies in(-1/2,0), so d(d+1)<0. For Q, d=-2p. The principal matrix is uniformly positive definite on every sphere chart. At w the common potential traces are phi=grad phi=Q=0 and grad Q=ell. They give no full-boundary vanishing condition.

## 3. The point Hessian and the four nodal half-curves

M is symmetric, trace free and M X(w)=0. Write E=X(w)^perp; its transverse eigenvalues are sigma,-sigma with sigma>0. Thus |V(w+h)|>=sigma|h|/2 on E for small h. The map (s,h) to exp(sA)(w+h) is a local diffeomorphism, so nearby velocity zeros lie only on the twisted ray.

Let N=DW(w), which exists by Section1, and D=D grad k(w)=[X(w)]_cross N-aM. This is symmetric and annihilates X(w). The identity grad k cross V=kW follows by crossing grad k=X cross W-aV with V. Its quadratic Taylor term gives (Dh) cross (Mh)=0. On E, M is invertible, so D M^(-1) sends every vector to a parallel vector. Applying it to a basis and their sum makes it a scalar multiple of I; hence D=lambda M. Accumulating irrotational points can be placed in w+E by twisted flow. There grad k=-aV. Dividing along a convergent transverse direction makes lambda=-a.

Outside closure Z, A963 gives k=0 implies W=0. The quadratic k=-a h.Mh/2+o(|h|^2) has two distinct null lines. Intermediate values on shrinking transverse circles give nodal points approaching both, where W=0. Differentiability of W makes N annihilate both lines, and homogeneity gives N X=0. Therefore

    D grad k(w)=-aM, DW(w)=0.

This agrees also with the contrapositive of A1185-A1186. No C2 neighborhood regularity of V is asserted.

In the eigenbasis, r^(-2)k tends uniformly to -a sigma cos(2theta)/2 and its angular derivative tends to the derivative of that sinusoid. Four simple roots and monotonicity near each give exactly four nodal half-curves. They are C1 off0 by the implicit function theorem. At a root, partial_r k=o(r) and |partial_theta k|>=c0 r^2, so r theta'(r) tends to0. Their C1 extensions have the four null tangent directions. Twisted flow lifts them to surfaces with empty interior. Each surface has W=0, but it need not be disjoint from supp W.

## 4. The exact transverse accumulation restriction

The rank identity extends to supp W by continuity. Contract it with X, using X.grad k=-ak and X.grad S=-bS, to obtain

    bS grad k=ak grad S.                              (4.1)

The point derivative H=D grad S(w) exists because grad(|V|^2/2)(w+h)=M^T M h+o(|h|). Thus H=D2P2-M^TM and tr H=-2|M|^2=-4sigma^2. Also ell in E; if ell=0, scalar homogeneity gives H X=0 and the trace is its trace on E.

Take vortical points w+r_n e_n in the transverse plane with unit e_n tending to e in E. If ell!=0, the degree-two part of(4.1) is

    b(ell.e)D e=(a/2)(e.D e)ell.

Dotting with e, b-a/2>0 gives (ell.e)(e.D e)=0. If ell.e were nonzero, the vector equation would give D e=0, impossible on E. Hence ell.e=e.D e=0. Only the line orthogonal to ell is available. At the endpoint ell=C_u m_infinity this forces C_n=m_infinity.M m_infinity=0; the shear C_s remains allowed.

If ell=0, the degree-three part is

    b(e.H e)D e=a(e.D e)H e.

As b-a=1, dotting gives (e.H e)(e.D e)=0. Consequently either H e=0 or both quadratic forms vanish on e. A negative definite H on E allows no direction. If H is singular, its negative trace makes it negative semidefinite of rank1, and only its kernel line is possible. If H is nonsingular and indefinite, its two null lines can share at most one with the trace-free form D: sharing both would make the forms proportional and force tr H=0. Thus again at most one unoriented transverse line is possible. Support supplies at least one direction.

Compactness of the transverse unit circle now shows that every closed transverse angular sector avoiding that line is irrotational sufficiently close to w. Otherwise a sequence there would have a forbidden limiting direction. This permits vortical regions narrowing towards the line; it does not establish or exclude their existence.

## 5. Necessary correction to the compressed parent wording

The inner proof correctly restricts the sequence to w+E. The compressed parent statements omit that restriction when they say that all vortical approach directions lie on a single line. That literal three-dimensional statement does not follow and is false as a conditional geometric assertion.

Indeed, from any transverse vortical sequence w+h_n tending to w, twisted invariance makes exp(s_n A)(w+h_n) vortical. Choose s_n=sqrt(|h_n|), so h_n=o(s_n). The normalized displacement then tends to X(w)/|X(w)|. Taking negative s_n gives the opposite ray; choosing s_n comparable to |h_n| also adds arbitrary X-components to a transverse limiting direction. The one-line result is therefore a result on a transverse section, or after projection along the twisted flow. All conclusions in Section4 use that precise formulation.

## 6. Interfaces and the maximum argument

A boundary point of a maximal irrotational component lies in supp W, or a zero-vorticity ball would enlarge the component. At a regular nodal boundary point, (4.1) gives S=0. On each fixed adjacent vortical component, k has fixed nonzero sign and differentiation gives S=D_C |k|^q for a finite component constant. At a nodal point in that component's closure, S and grad S tend to0 since q>1. There is no uniform bound on constants from infinitely many distinct components.

A nonzero maximal global irrotational component cannot have its entire angular boundary in {k=0}. The continuous angular k solves L_(1-p) k=0. A positive maximum or negative minimum, attained in the compact closure and not on its zero boundary, contradicts the negative zeroth-order coefficient. This also covers the whole sphere. It does not exclude one local nodal side of a component.

At an interface with k!=0, the potential-side difference S-D_C|k|^q has zero value and first derivative traces, but

    Delta(S-D_C|k|^q)=-2|D2 phi|^2
              -D_C q(q-1)|k|^(q-2)|grad k|^2.

It is generally not harmonic, so harmonic uniqueness from Cauchy data is unavailable. A velocity-jump vortex sheet is incompatible with C1 V. An interface where continuous W tends to0 is not excluded by that regularity.

## 7. Convergent local harmonic models for every omega

Use coordinates z>0, zeta=x+iy, R^2=x^2+y^2 and a cone R<epsilon z with0<epsilon<1. For real d and integer m>=1 set beta=d-m+im omega/c, A0=1, and

    A_(n+1)=-[(beta-2n)(beta-2n-1)]
                        /[4(n+1)(m+n+1)] A_n,
    F_(d,m)=zeta^m sum_(n>=0) A_n R^(2n) z^(beta-2n).

Use the real logarithm of z. The coefficient ratio tends to -1 unless the series terminates. Therefore the power series converges for R<z; all differentiated series converge on compact subsets because differentiation introduces only polynomial factors in n. Its analytic factors and locally normally convergent power series give real analyticity also on the positive axis.

The identity Delta_(x,y)(zeta^m R^(2n))=4n(m+n)zeta^m R^(2n-2) makes consecutive terms cancel the z second derivative, so Delta F=0. Under exp(sA), each term is multiplied by exp([c(m+beta)-im omega]s)=exp(cd s). Thus the desired twisted degrees hold exactly.

At w=(0,0,1), take phi=(1/2)Re F_(1-p,2). It has phi=grad phi=0 and Hessian diag(1,-1,0). The harmonic choice Q=Re[(1+i)F_(-2p,1)] gives grad S=(1,-1,0), which is null for M. The choice Q=Re F_(-2p,2) gives grad S=0 and H=diag(0,-4,0), realizing the allowed singular-H jet. In both cases V=W=S=P2=0 at w and the local tail equations all hold. The choice Q=0 also satisfies them but has H|E=-2I, so it cannot be attached to supported vortical accumulation with the same jets.

## 8. Scope and provenance

The examples have W=0 on their whole cone, so w is not in supp W. They realize the displayed point conditions, not an actual supported W2 endpoint, a global canonical pressure, or an original Euler profile. The four-sector and one-line restrictions do not eliminate the possible shear or narrowing vortical regions.

The parent agent is configured model; its nested consultation is the external referee (a second model) and reports an unsuccessful model credential lookup. It is not a completed model review. A focused comparison through the already running configured model agents remains requested. Exact source bytes and the availability record are retained. No numerical computation, formal build, new agent or model client is used here.
