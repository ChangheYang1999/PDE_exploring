# Global-source map formulation and the adjoint center-strain identity

Status: the corrected equivalence and the absolutely convergent identity below have standalone proofs. They supply necessary conditions and an equivalent formulation, not exclusion of the global-source class. The generating-function discussion includes an explicit limitation.

## 1. Setting, dependencies and notation

Let beta>2, lambda=(beta-2)/2, mu=(3beta+2)/2, nu=1/beta, and L=diag(lambda,mu). The physical point is Y=(x,y). We use

    W=beta Y+V, div V=0, -curl V=Omega,
    W.gradTheta=(beta-2)Theta,
    W.gradOmega+Omega=Theta_x.

The fields are smooth on the whole plane. V(0)=0, V=o(|Y|), Theta is even in x, Omega is odd in x, Theta(0,y)=0, and Theta=a0 x^2+O(|Y|^3), a0!=0. Class A supplies the canonical relative inverse and, with fixed constants,

    |V(Y)|<=C(1+|Y|)^(1-nu),
    |Omega(Y)|<=C(1+|Y|)^(-nu),
    |gradTheta(Y)|<=C(1+|Y|)^(-2nu).

Class G means that0 is the only zero of W. Its complete flow is denoted phi_t. Every nonzero backward orbit tends to0 and every nonzero forward orbit escapes. Packet48 proves a smooth, area-preserving parity-equivariant coordinate map Xi with Xi(0)=0 and DXi(0)=I. In these coordinates Theta=a0 xi^2 and W has the triangular normal form

    lambda xi partial_xi + (mu eta+kappa xi^k) partial_eta,

where kappa can be nonzero only if mu=k lambda and k is even. The linear formulation below assumes kappa=0. This includes all nonresonant beta; it does not silently discard the resonant alternative. The adjoint identity does not need kappa=0.

The inverse map is written X(Z)=(x(Z),y(Z)), Z=(xi,eta). The matrix J rotates counterclockwise, J(a,b)=(-b,a). Curl of a vector or covector represented by two components means partial_1 v_2-partial_2 v_1. The scalar strain kernel is K(Y)=xy/|Y|^4; it differs from the vector Biot-Savart kernel.

Dependencies: packet48 for global source coordinates; packets33,36 for the class A bounds; the full-plane inverse uniqueness in packet63; elementary differential forms, ODE estimates, the inverse function theorem and Fubini's theorem. No inference rests on a teammate's numerical summary.

## 2. Corrected map equivalence in the linearizable case

Consider a smooth orientation-preserving diffeomorphism X of the plane such that

    X(0)=0, DX(0)=I, det DX=1,
    x(-xi,eta)=-x(xi,eta), y(-xi,eta)=y(xi,eta).

For g=DX^T DX and D=(LZ).grad_Z, impose

    (D+1) curl_Z(g LZ) = -2 a0 xi y_eta,                  (E1)
    V(X(Z))=DX(Z)LZ-beta X(Z)=o(|X(Z)|),                 (E2)

and the physical decay condition |Omega(Y)|<=C(1+|Y|)^(-delta) for some delta>0, with

    Omega(X(Z))=-curl_Z(g LZ).

These are equivalent to a class G profile with the above normalization whose selected smooth normal form has kappa=0. The decay condition can equivalently be replaced by the broad polynomial bound together with the previously proved class reduction, but is explicit here.

To prove the forward direction, pull back the velocity one-form:

    X^*(W_1 dx+W_2 dy)=(DX^T W).dZ=(g LZ).dZ.

Exterior differentiation commutes with pullback, and X preserves area. Hence

    (curl_Y W)(X(Z))=curl_Z(g LZ).                       (2.1)

The inverse derivative matrix also gives xi_x=y_eta. Consequently Theta_x(X(Z))=2a0 xi y_eta. Since the physical transport derivative becomes D, the vorticity equation gives E1, while E2 is exactly the required relative sublinear velocity. Parity and the centering conditions are inherited from Xi.

Conversely, define W=X_*(LZ), Theta(X(Z))=a0 xi^2 and Omega=-curl W. Area preservation gives div W=tr L=2beta. Formula(2.1) and E1 give the vorticity transport equation. Also W.gradTheta=2lambda Theta=(beta-2)Theta. The map conditions imply parity, W(0)=0, DW(0)=L, and the temperature expansion Theta=a0x^2+O(|Y|^3). The fixed axis of reflection is mapped onto itself: equivariance and injectivity give both inclusions, so Theta vanishes on the entire physical axis. The flow is conjugate to e^(tL), so it is complete, has unique zero0, and has all nonzero backward orbits tending to0. A plane diffeomorphism is proper, so nonzero forward orbits escape.

Set V=W-beta Y. Then div V=0, -curl V=Omega, and V(0)=0. The relative Biot-Savart inverse exists from the decay condition and has sublinear growth. Its difference from V is a globally harmonic sublinear vector field. The harmonic derivative estimate makes this difference constant, and the origin condition makes it zero. Thus E2 fixes the full-plane inverse without an added harmonic strain. Finally differentiate the vorticity equation at0: parity gives gradOmega(0)=(b0,0), and

    (1+lambda)b0=2a0, so b0=4a0/beta.

The remaining center identities follow from DW(0)=L. The polynomial temperature bound also follows, rather than being an additional hidden map hypothesis. Fix 0<epsilon<beta and choose R so large that the radial component of W is at least (beta-epsilon)|Y| outside B_R, using E2. Every point outside that ball has a finite backward hitting time t_R of its boundary: its backward radius decreases at a rate at least beta-epsilon until it reaches R. Integration gives t_R<=(beta-epsilon)^(-1)log(|Y|/R). Temperature transport and boundedness on the circle then give

    |Theta(Y)|<=C exp[(beta-2)t_R]
              <=C (|Y|/R)^((beta-2)/(beta-epsilon)).

Thus both source fields obey the broad polynomial control required in the prompt. The already proved class reduction applies, if the sharper class A estimates are desired. This proves all required conditions.

The condition X(0)=0 is indispensable in this formulation. Adding a vertical constant to X preserves its derivative, area and parity and preserves the displayed local differential equation E1. It also preserves sublinear growth up to a constant in E2. It moves the zero of the pushed-forward field away from the prescribed material center. The uncentered conditions therefore do not entail V(0)=0 or DW(0)=L.

## 3. Explicit formulas and the polynomial diagnostic

Differentiating the components of g LZ gives

    curl_Z(g LZ)=(lambda-mu)g12
      +lambda xi (partial_xi g12-partial_eta g11)
      +mu eta (partial_xi g22-partial_eta g12).           (3.1)

The scalar resolvent is unique among functions bounded on backward orbits:

    Omega(X(Z))=2a0 xi integral_{-infinity}^0
       e^((1+lambda)s) y_eta(e^(sL)Z) ds.                (3.2)

Indeed integrating (D+1)Omega=2a0 xi y_eta gives this formula, and its omitted endpoint is e^-T Omega(X(e^-TL Z)), which tends to0 by smoothness near0. The integrand is integrable near minus infinity because y_eta tends to1 and 1+lambda>0.

For the shear X=(xi,eta-kprime xi^2), with kprime=-4a0/[beta(beta+6)], one obtains

    W=(lambda x, mu y-2a0 x^2/beta),
    Theta=a0 x^2, Omega=(4a0/beta)x.

These satisfy E1 and the local coupled equations. They violate E2 and the vorticity decay assumption. They confirm the sign and expose why E1 by itself is insufficient.

For a perturbation X=Z+epsilon J gradH+O(epsilon^2), the first variation is

    delta g11=-2H_xi_eta,
    delta g12=H_xi_xi-H_eta_eta,
    delta g22=2H_xi_eta,
    delta curl_Z(g LZ)=D(Delta H)
                  +(lambda-mu)(H_xi_xi-H_eta_eta).

The linearized area condition holds because div(J gradH)=0. This is an algebraic linearization; no small-amplitude branch is asserted.

## 4. A generating function is only a local chart without an extra hypothesis

A type2 generating function F(xi,y), with eta=F_xi and x=F_y, can be introduced wherever the projection (xi,eta)->(xi,y(xi,eta)) is invertible. Its local determinant is y_eta. Where this is nonzero, the one-form eta dxi+x dy is closed: its exterior derivative is d eta wedge dxi+dx wedge dy=0 by area preservation. On a simply connected projection chart it is therefore dF. Near0, y_eta=1, so such a chart exists. Parity permits F to be odd in xi after adding a constant.

Area preservation and reflection symmetry alone do not give a global chart. Here is a smooth counterexample to that inference, not a B2 profile. Choose a>2rho>0 and two disjoint disks centered at (a,0) and (-a,0), both disjoint from0. Let H be a compactly supported smooth Hamiltonian equal to ((xi-a)^2+eta^2)/2 on a smaller disk at (a,0), with the negative reflected expression on the other disk; thus H is odd in xi. Its Hamiltonian flow J gradH preserves area, commutes with reflection and is the identity near0 and infinity. The time-pi/2 map rotates a neighborhood of (a,0) by pi/2, and therefore y_eta=0 there. It has X(0)=0 and DX(0)=I but the projection fails to be a local diffeomorphism. This example does not satisfy E2 and is used only to disprove the claimed implication from map geometry alone. A global generating function for an actual profile would require a further argument, including global projection injectivity and surjectivity.

## 5. Absolute majorant for the vorticity resolvent

Put f=Theta_x and

    J_f(Y)=integral_0^infinity e^-t |f(phi_-t Y)| dt.

Then, in class G,

    J_f(Y)<=C|Y| near0,
    J_f(Y)<=C(1+|Y|)^(-nu) for |Y| large.               (5.1)

Near0, the symmetric positive matrix DW(0)=diag(lambda,mu) gives a small backward-invariant ball and |phi_-t Y|<=e^(-a t)|Y| there, for some a>0. Smoothness and gradTheta(0)=0 give |f(Z)|<=C|Z|. Integration yields the first estimate. Globally f is bounded, so J_f is bounded on every compact set with no issue of a nonuniform entrance time.

For large r=|Y|, choose a fixed R so that the radial velocity is positive for rho>=R. Let tau be the backward hitting time of that circle. On 0<=t<=tau,

    d log rho(t)/dt=-beta+O(rho(t)^(-nu)).

Changing variable from t to rho, using radial speed at least beta rho/2, bounds the integral of rho^-nu uniformly by C R^-nu. Thus

    C_R^-1 r e^-beta t <=rho(t)<=C_R r e^-beta t,
    C_R^-1 r^nu <=e^tau<=C_R r^nu.

The integral up to tau is bounded by

    C r^(-2nu) integral_0^tau e^t dt <= C r^-nu,

because beta nu=1. After tau, boundedness of f gives at most C e^-tau<=C r^-nu. This proves(5.1). It also proves absolute convergence of the ordinary scalar resolvent Omega(Y)=integral_0^infinity e^-t f(phi_-tY)dt.

## 6. The adjoint center-strain identity

For each Y!=0 define

    M(Y)=integral_0^infinity e^((2beta-1)t) K(phi_tY)dt,
    K(Y)=xy/|Y|^4.

This integral is absolutely convergent for each such Y. Its finite initial segment avoids0, and after escape the radius is comparable to e^(beta t), so its absolute tail is O(e^-t). It satisfies the transport identity

    W.grad M+(2beta-1)M=-K                              (6.1)

in the directional sense along the flow. To see this without presupposing an integrable spatial derivative, shift the time variable in M(phi_sY):

    M(phi_sY)=e^(-(2beta-1)s)
      [M(Y)-integral_0^s e^((2beta-1)t)K(phi_tY)dt].

Differentiate in s at0.

The origin strain has the exact absolutely convergent formula

    c=Psi_xy(0)=(1/pi) integral K(Y)Omega(Y)dY
      =(1/pi) integral Theta_x(Y)M(Y)dY.               (6.2)

For the first equality, differentiate the full-plane relative stream kernel. The mixed derivative of -log|X-Y|/(2pi) at X=0 is K(Y)/pi. The source is O(r) near0 by odd parity, and is O(r^-nu) at infinity; therefore this integral is absolutely convergent at both ends. Differentiation can also be established by a small-ball cutoff and the local smooth-source potential formula; no point-mass term contributes to the mixed derivative.

The only potentially delicate step in the second equality is Fubini. Its absolute majorant before changing variables is

    integral |K(Y)| J_f(Y)dY.

By(5.1), this is bounded near0 by C integral_0^1 dr and at infinity by C integral_1^infinity r^(-1-nu)dr. It is finite. Substitute the vorticity resolvent, set X=phi_-tY, and use dY=e^(2beta t)dX. Fubini then gives exactly the second integral in(6.2), including its factor and sign. In particular integral |Theta_x M| is finite. The material center requires c=1+beta/2, so(6.2) is a global necessary compatibility identity.

No unproved integration by parts turning Theta_x M into -Theta M_x is used. Such a step would require its own singular-center and infinity boundary estimates. No sign of M, M_x or the product in(6.2) is inferred from the definition. This identity alone is not a contradiction.

## 7. Audit provenance and scope

The source draft was the lead's notes/g_map.md, independently read and copied with its hash to opus_reviews/64_global_map_audit/lead_source.md. Its centering omission, global generating-function claim, and unqualified far-field scaling require the repairs stated here or in a subsequent precise asymptotic theorem. The core pullback, shear and linearization identities were derived directly.

Actual model request64 used the existing permitted Python Bedrock client and returned model claude-opus-5-5, HTTP200, stop_reason refusal, with no audit text. This is an availability limitation for that exchange and is not an endorsement. The earlier inverse review exchanges62 and63 did return written audits and were independently checked. No model was substituted.

This packet constructs no admissible profile and excludes no member of G. Its map equivalence is conditional on the already established smooth linearizable coordinate case; its adjoint identity covers all of G, including the triangular resonance. No numerical or formal proof assistant computation is treated as proof of the PDE.
