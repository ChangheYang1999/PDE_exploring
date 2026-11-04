# Actual tail rays, original equilibria and the no-flat-zero criterion

Status: independent mathematical reconstruction of LIT199. Sections 1-7 prove its three claims. Section 8 adds an exact equilibrium-rate restriction by combining previously confirmed estimates. The bare-decay conjecture remains open.

A tail vortex ray has a finite-time endpoint at the deleted origin of the tail domain. For an actual profile this ray can be pulled back before taking the endpoint: the original vorticity field is bounded and its flow is complete. This supplies a genuine carrier equilibrium. Its transverse linearization constrains the angular tail zero and makes the global index count useful.

## 1. Statement and exact hypotheses

Fix 2/5<c<1/2 and any finite real omega. Write

    Jx=(-x2,x1,0), A=cI-omega J, X(x)=Ax,
    a=1-2c, kappa=1+c, b=2(1-c), q=b/a>6,
    p=(1-c)/c, T_s=exp(sA), Q_s=exp(omega sJ).

Let U in C2(R3;R3) and P in C1(R3) satisfy

    div U=0,
    (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0,
    |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1)

for a finite constant C. Set B=Ax+U and Omega=curl U. Denote their complete flows by Phi_s and Gamma_tau. Let E be the set of points whose forward B-orbit escapes to infinity. The confirmed actual scattering map Xi:E->D, D=R3 minus {0}, is a C1 diffeomorphism. The actual tails V and W=curl V obey

    Xi Phi_s=T_s Xi, DXi B=X composed Xi, DXi Omega=W composed Xi,
    V(T_s x)=exp(-(1-c)s)Q_s^T V(x),
    W(T_s x)=exp(-s)Q_s^T W(x),
    V in C^(1,alpha)_loc(D) for every 0<alpha<1.

The actual pressure tail P2 is normalized by the limiting original pressure and satisfies the confirmed tail equations. Put

    k=X.V, S=P2-|V|^2/2,
    Y(w)=V(w)-(w.V(w))w, w in S2,
    Tflat={w in S2: V(w)=0, DV(w)=0} intersect supp(W|S2).

Support is the closure of the angular nonzero set of W. The derivative DV is the ambient derivative on D. Then:

1. If W(w0)=lambda Aw0 with w0 in S2 and lambda!=0, the point y0=Xi^(-1)(w0) lies on an escaping half of the original vortex line through a vortical carrier equilibrium p0. With tau0=1/(kappa lambda),

       p0=Gamma_(-tau0)y0, B(p0)=0, Omega(p0)!=0,
       Phi_s y0=Gamma_(tau0 exp(kappa s))p0.

2. At every zero V(w0)=0 with W(w0)!=0 the projected tail-vorticity field

       F(w)=W(w)-(w.W(w)/c)Aw

   is C^(1,alpha) near w0. Both F and Y have a nondegenerate saddle there. If DB(p0)^T U(p0)=rho U(p0) is the equilibrium covector rate, then

       rho=-b,
       spec DB(p0)={kappa,-b,1},
       spec DF(w0)={b lambda,-lambda},
       grad S(w0)!=0.

3. If Tflat is empty, U=0. Equivalently any nonzero profile in this exact class has a supported flat tail-velocity zero.

No uniform estimate in omega is asserted. The statements hold separately for every finite omega. They do not remove global zero helicity or either natural bound.

## 2. Taking the endpoint in the original flow

The vector field B is locally Lipschitz with at most linear growth; Omega is C1 and bounded. Therefore both original flows are complete, with C1 flow maps. Their bracket, using [B,Omega]=D Omega B-DB Omega, is

    [B,Omega]=-kappa Omega.                              (1)

Suppose W(w0)=lambda Aw0!=0, set y0=Xi^(-1)(w0), and write y(s)=Phi_s y0. Scattering and homogeneity give

    W(T_s w0)=lambda exp(-kappa s)X(T_s w0),
    Omega(y(s))=lambda exp(-kappa s)B(y(s)).             (2)

The second identity follows by applying the invertible DXi(y(s)); it is an identity on the original orbit. Define tau(s)=exp(kappa s)/(kappa lambda), so tau'(s)=exp(kappa s)/lambda. Equation (2) implies dy/dtau=Omega(y), including when lambda is negative. Uniqueness yields

    y(s)=Gamma_(tau(s)-tau0)y0, tau0=1/(kappa lambda).

As s tends to minus infinity, tau(s) tends to zero from its fixed sign. The complete original flow gives the finite endpoint p0=Gamma_(-tau0)y0. Equation B(y(s))=kappa tau(s)Omega(y(s)) implies B(p0)=0 by continuity. If Omega(p0)=0, uniqueness would make Gamma_tau p0 constant, whereas Omega(y0)!=0 by the scattering pushforward. Thus p0 is vortical.

From (1), or by differentiating the pullback Gamma_tau^* B, one gets globally along this line

    B(Gamma_tau p0)=kappa tau Omega(Gamma_tau p0),
    Phi_s Gamma_tau p0=Gamma_(exp(kappa s)tau)p0.         (3)

Indeed d_tau(Gamma_tau^* B)=Gamma_tau^*[Omega,B]=kappa Omega, with initial value B(p0)=0. The selected half-line belongs to E because it is exactly the carrier orbit through y0. There is no assertion that Xi extends differentiably to p0, or that the tail vorticity has a complete flow on D.

## 3. A differentiable quotient despite only C1 coordinates

Choose a smooth disk chi(v), v near 0 in R2, through p0 transverse to Omega(p0). The C1 map Theta(tau,v)=Gamma_tau chi(v) is locally invertible near (0,0), and also near (tau0,0). These two local neighborhoods suffice; one globally injective flow box over the whole segment is unnecessary.

Decompose B on the initial disk as

    B(chi(v))=b0(v)Omega(chi(v))+Dchi(v)b(v).

The basis matrix is C1 and invertible. Consequently b0 and b are C1 and vanish at 0. Pulling back (1) along Gamma gives the exact coordinate fields

    Omega_hat=partial_tau,
    B_hat=(kappa tau+b0(v))partial_tau+b(v).partial_v.    (4)

This explicit formula establishes C1 coefficients. A general C1 change of coordinates would not automatically preserve that regularity.

At the equilibrium the derivative of B_hat is

    [[kappa, Db0(0)], [0, Db(0)]].                      (5)

It is similar to DB(p0). To justify this with only C1 Theta, use first-order expansions in DTheta B_hat=B composed Theta: both vector fields vanish at the center, and continuity of DTheta makes its varying part times B_hat an o(distance) error. Thus no D2Theta is needed. Db(0) represents DB(p0) on the quotient by the invariant Omega line.

The confirmed equilibrium spectrum theorem A468 gives a real rho such that

    U(p0)!=0, DB(p0)^T U(p0)=rho U(p0),
    spec DB(p0)={kappa,rho,-a-rho},
    DB(p0)Omega(p0)=kappa Omega(p0).                    (6)

Here U(p0)=-Ap0!=0. The nonzero conclusion uses global zero helicity at a vortical carrier equilibrium, including its first differential, and excludes p0=0. Therefore

    spec Db(0)={rho,-a-rho}.                            (7)

The quotient statement remains valid if eigenvalues coincide or a Jordan block occurs: the invariant Omega line contributes one factor kappa to the characteristic polynomial.

## 4. Transferring the quotient to the tail sphere

On the section tau=tau0, project Omega along B. By (4) its v-coordinate field is

    R(v)=-b(v)/(kappa tau0+b0(v)),
    R(0)=0, DR(0)=-lambda Db(0).                       (8)

The denominator is nonzero on a small disk. Define the smooth twisted normalization on D by

    t(x)=log|x|/c, N(x)=exp(-t(x)A)x in S2.

It has DN X=0 and kernel DN(x)=R X(x). The map

    psi(v)=N(Xi(Theta(tau0,v)))

is C1 and locally invertible at 0. At y0 the disk is transverse to Omega, hence to B=kappa tau0 Omega, while DXi maps B to X. This proves injectivity of Dpsi between two-dimensional tangent spaces.

For x=T_t w, direct differentiation and homogeneity give

    dt_x(h)=x.h/(c|x|^2),
    DN(x)h=exp(-tA)(h-X(x)dt_x(h)),
    DN(x)W(x)=exp(-kappa t)F(w).                       (9)

The projection along B does not affect the last pushforward because DN DXi B=0. Hence

    Dpsi(v)R(v)=exp(-kappa t(Xi(Theta(tau0,v))))F(psi(v)). (10)

At v=0, psi(0)=w0, t(w0)=0, and both vector fields vanish. Whenever F is C1 near w0, first-order expansion of (10) proves

    Dpsi(0)DR(0)=DF(w0)Dpsi(0).

Continuity of Dpsi suffices, since it multiplies R(v)=O(|v|). The scalar factor is continuous and equals 1 at the zero; no derivative of it is used. Equations (7)-(8) now give

    spec DF(w0)={-lambda rho,lambda(a+rho)}.             (11)

## 5. Every actual vortical velocity zero is a saddle

Let V(w0)=0 and W(w0)!=0. The interior-zero theorem A963/A970 applies at exactly the hypotheses of Section 1. It makes k zero on a neighborhood of w0 and, by homogeneity, on an open twisted cone. The identity

    grad k=X cross W-aV

gives W(w0)=lambda X(w0) with lambda!=0. Thus Sections 2-4 apply. On that cone,

    aV=X cross W,
    F(w)=-a(I-X(w) tensor w/c)(X(w) cross V(w))/|X(w)|^2. (12)

The smooth coefficients and C^(1,alpha) velocity make F C^(1,alpha), supplying the regularity needed in (11) without assuming W is C1.

We give a direct strict-rate argument, independent of the local LIT198 nonresonance calculation. The confirmed covector transport on the equilibrium vortex line gives

    U!=0, U.B=0,
    (B.grad)U=rho U-DB^T U.

For n=U/|U| and S_U=sym DU it follows that along y(s)=Phi_s y0,

    d_s log|U(y(s))|=rho-c-n.S_U(y(s))n.                (13)

The escape comparison |y(s)| comparable to exp(cs), and c(p+1)=1, imply |DU(y(s))|<=C exp(-s) for large s. Integrating (13) gives

    exp(-(rho-c)s)|U(y(s))| -> C_*>0.

Since x_s=T_(-s)y(s) tends to Xi(y0)=w0, locally uniform actual-tail convergence implies

    |V(w0)|=lim_(s->infinity)(C_*+o(1))exp((rho+a)s).

The left side is zero. A positive finite C_* therefore forces rho<-a. This is the argument of A602, whose line-transport input does not use any tail-index conclusion. Consequently (11) has two nonzero real eigenvalues of opposite signs:

    det DF(w0)=lambda^2 rho(-a-rho)<0.                  (14)

For completeness, differentiate X.V=0 and the homogeneity of V at the zero. If M=DV(w0) and X0=X(w0), then M X0=M^T X0=0 and tr M=0. In an oriented orthonormal basis of G=X0^perp diagonalizing its symmetric part, the restriction is

    Mbar=[[mu,-nu],[nu,-mu]], nu!=0,
    W(w0)=2nu X0/|X0|, lambda=2nu/|X0|.

The two angular determinants are

    det DF(w0)=(a^2/|X0|^2)(nu^2-mu^2),
    det DY(w0)=(c^2/|X0|^2)(nu^2-mu^2).                (15)

The second follows from orthogonal projection onto T_w0 S2 and w0.X0=c; the first follows from the oblique projection in (12). Their ratio is positive. Thus Y also has a nondegenerate saddle of index -1. These are statements about linearized local fields, not about nodal mass estimates. In fact the zero is in the interior of {k=0}, so nodal hypotheses excluding such regions cannot be invoked there.

## 6. The no-flat-zero theorem

Suppose U!=0 and Tflat is empty. The confirmed boundary theorem A973-A975/A984-A986 gives k=0 throughout D. The confirmed A999 density argument gives supp(W|S2)=S2: an open irrotational region of a nonzero globally zero-k tail would have a supported flat velocity zero on its boundary. The case W identically zero is already the zero profile by the actual scattering and global decay. These two inputs retain all global hypotheses of Section 1.

If Y(w)=0, then V(w) is radial. Since X.V=0 and w.X=c>0, this forces V(w)=0. Thus the zeros of Y are exactly the zeros of V. At a zero with W!=0, Section 5 gives index -1. At a zero with W=0, M is symmetric, trace free and annihilates X0. If M=0 the point belongs to Tflat by density, contrary to the premise. Otherwise Mbar has nonzero opposite real eigenvalues. Its determinant, and the positive projection factor in (15), make this zero of Y another nondegenerate saddle of index -1.

All zeros are isolated. The zero set is closed in compact S2, so it is finite: an infinite sequence of distinct zeros would accumulate at a zero that is not isolated. The Poincare-Hopf index sum for the C1 tangent field Y must equal the Euler characteristic 2. A finite collection of index -1 zeros, including the possibility of no zeros, cannot have that sum. The contradiction proves U=0.

This removes the independent globally zero-k alternative only when Tflat is absent. It does not exclude a globally zero-k tail with supported flat zeros.

## 7. Comparison with the submitted proof

LIT199 uses A496 to obtain rho<=-a and uses LIT198 to exclude equality or a nonnegative determinant. Both inputs are confirmed and their dependencies precede the proposed transfer. Its route is valid. Section 5 above instead derives the strict inequality directly from A602 and the actual zero V(w0)=0. This removes LIT198 from the dependency list for the saddle conclusion and the conditional no-flat-zero theorem.

The complete eight-section LIT199 source was read. The finite endpoint, both signs of lambda, the two local sections, the explicit C1 coefficients, the quotient multiplicities, the normalization factor, and differentiation only at zeros were checked independently. Sections 2-4 close A1003's formerly missing actual-ray inference. They do not transfer completeness of an arbitrary formal tail, extend Xi to the compact core, or realize arbitrary local tails as global profiles.

## 8. Exact rate from pressure and local tail jets

We now refine Section 5. Let w0 be any vortical velocity zero. The canonical pressure estimate A516 applies because 1<p<3/2 and the full natural bounds hold. It gives

    |grad P(y)|=O(|y|^(-2p-1)).

Its normalization comes from the actual momentum equation and the verified canonical-pressure theorem, not from a choice of harmonic addition to a Poisson solution. On the equilibrium vortex line, the covector law and momentum give exactly

    grad P=DU^T U-(a+rho)U.                              (16)

By (13), |U(y(s))| is comparable to |y(s)|^((rho-c)/c), with positive constants. If -b<rho<-a, dividing (16) by |U| gives

    |a+rho| <= |DU|+|grad P|/|U| -> 0,

because -(2p+1)-(rho-c)/c=(-b-rho)/c<0. This contradicts rho<-a. Therefore rho<=-b.

The local jet classification A1017 applies on the zero-k cone about w0. It uses the actual equations W.grad S=0, X.grad S=-bS, the Poisson equation, and C^(1,alpha) V. In the notation of (15), it states

    eta=|mu/nu| belongs to {0,q-1,2q-1}.

For eta=2q-1 the gradient grad S(w0) is nonzero. For eta=q-1 it is zero and the Hessian of S has rank one and negative trace. Eta=0 is pure rotation. No second derivative of W, or of F when grad S is nonzero, is used in that classification.

By the same matrix calculation as (15), the eigenvalues of DF divided by lambda are

    { (a/2)(1+eta), (a/2)(1-eta) }.

Equation (11) gives the same unordered pair as {-rho,a+rho}. Since rho<-a, one member is positive and the other negative. Thus eta>1 and

    rho=-(a/2)(1+eta).

The two remaining possibilities are rho=-b/2 and rho=-b. The pressure bound rho<=-b excludes the former. Hence

    rho=-b, eta=2q-1, grad S(w0)!=0.

Since b-a=1, (6) and (11) become precisely

    spec DB(p0)={kappa,-b,1},
    spec DF(w0)={b lambda,-lambda}.

This proves the strengthening in Section 1. It is a necessary condition at such a zero. It neither constructs a profile nor excludes a saddle with these permitted data.

## 9. Dependencies, verification and scope

The exact inputs are A210/A533/A538 for actual tails and their C1 regularity; the confirmed C1 scattering diffeomorphism and vorticity pushforward; A413/A468 and the line part of A540 for equilibrium covector transport; A602 for the independently repeated escape amplitude argument; A963/A970 for interior zero-k neighborhoods; A973-A975/A984-A986 and A999 for the no-flat global alternative and density; and elementary local coordinate and index calculations. Section 8 additionally uses A516 and A1017. It is not needed for Section 6.

The theoretical test was whether original completeness supplies the endpoint, whether available C1 regularity suffices for the transverse spectrum, and whether the index argument covers all zeros. Each requirement is explicitly met. There are no hidden flux boundary terms, no global pressure sign, no assumption of complete tail-vorticity flow, and no smallness or symmetry condition on omega. The unrestricted conjecture, zero-helicity removal, derivative-bound removal, and supported flat zeros remain open.

This is an informal proof with no numerical calculation or formal build. The complete source snapshot and hashes are in verification; formal_sources records that no formalization was attempted under the run restrictions. Existing configured model agents are the permitted comparison channel. No focused model response to this new proof is claimed until an actual reply is received and checked.
