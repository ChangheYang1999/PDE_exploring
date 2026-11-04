# Exact line decay and scalar geometry at a vortical tail-velocity zero

Status: independent audit of LIT200. Its rate rigidity agrees with A1022. The directional strain identity, scalar geometry and exact positive line limits below are confirmed. They do not exclude the permitted saddle.

## 1. Exact statement and notation

Let 2/5<c<1/2, omega be any finite real number, Jx=(-x2,x1,0), A=cI-omega J, X(x)=Ax, a=1-2c, b=2(1-c), kappa=1+c, p=(1-c)/c, q=b/a>6. Suppose U in C2(R3;R3) and P in C1(R3) satisfy

    div U=0, (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0,
    |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1)

for one finite constant C. Put B=Ax+U, Omega=curl U and let Phi_t, Gamma_tau be the complete carrier and vortex flows. Let Xi:E->R3 minus{0} be the actual C1 scattering diffeomorphism from the forward escaping set. Use the actual leading tails V, W=curl V and P2, with the canonical pressure determined by the original momentum equation. Set

    k=X.V, S=P2-|V|^2/2,
    F(w)=W(w)-(w.W(w)/c)Aw,
    Y(w)=V(w)-(w.V(w))w, w in S2.

Suppose V(w0)=0 and W(w0)!=0. Then W(w0)=lambda Aw0 for a nonzero real lambda. With y0=Xi^(-1)(w0) and tau0=1/(kappa lambda), define p0=Gamma_(-tau0)y0. The following statements hold.

1. p0 is a vortical carrier equilibrium, U(p0)!=0, and

       DB(p0)^T U(p0)=-b U(p0),
       spec DB(p0)={kappa,-b,1}, spec DF(w0)={b lambda,-lambda}.

   For n0=U(p0)/|U(p0)|,

       n0.(sym DU(p0))n0=c-2.                        (1)

   This is a directional quadratic-form value, not an assertion that n0 is a strain eigenvector.
2. Both F and Y have nondegenerate saddles at w0. With M=DV(w0),

       2|sym M|^2/|W(w0)|^2=(2q-1)^2.               (2)

   The norms here are the Euclidean norm of W and the Frobenius norm of the matrix. Also

       S(w0)=P2(w0)=0, grad S(w0)=grad P2(w0)!=0.     (3)

   Each scalar changes sign in every sufficiently small neighborhood and has its own local zero surface containing the twisted ray. The two surfaces are not asserted to coincide.
3. Along y(t)=Phi_t y0, as t->+infinity,

       e^(-ct)|y(t)| -> 1,
       e^((2-c)t)|U(y(t))| -> C_U in (0,infinity),
       e^t|Omega(y(t))| -> |lambda| |Aw0|.            (4)

   These are limits on this particular line, not uniform asymptotics on nearby trajectories.
4. On sufficiently small compact patches about w0 in the punctured ambient domain or on S2, |S|^(-a/b) is locally integrable. This supplies no global reciprocal-integrability hypothesis at other zeros.

## 2. Actual endpoint, quotient and pressure rate

A1018-A1022, with a complete independent proof in the team records, establish the actual endpoint, the C1 quotient transfer, and the exact rate. Here is the dependence of the rate on the hypotheses.

A963/A970 put w0 in an open zero-k cone. Scattering transports the relation W(w0)=lambda Aw0 to

    Omega(y(t))=lambda e^(-kappa t)B(y(t)),
    y(t)=Gamma_(tau0 e^(kappa t))p0.                 (5)

Original vortex completeness and uniqueness give the genuine vortical equilibrium at tau=0. This endpoint argument uses neither a completion of the tail flow at its deleted origin nor an extension of Xi to the core.

At the equilibrium write DB(p0)^T U(p0)=rho U(p0). The confirmed spectrum and C1 transverse comparison give

    spec DB(p0)={kappa,rho,-a-rho},
    spec DF(w0)={-lambda rho,lambda(a+rho)}.           (6)

The actual line covector law gives

    d_t log|U(y(t))|=rho-c-n(t).sym DU(y(t))n(t),      (7)

where n(t)=U(y(t))/|U(y(t))|. This U never vanishes, by invertible covector transport from the nonzero equilibrium velocity. The derivative bound makes the last term integrable. Since the leading velocity vanishes at w0, A602 gives rho<-a.

The canonical gradient bound is

    |grad P(x)|<=C'(1+|x|)^(-2p-1),                  (8)

proved independently by the proportional-radius cutoff argument A516 in the team records. The submitted source uses the equivalent confirmed two-zero-moment proof A673-A675. Both arguments apply here, remove the harmonic ambiguity through the original momentum equation, and use no pressure-sign assumption.

On the line,

    grad P=DU^T U-(a+rho)U.

Divide its norm bound by |U|. If rho>-b, (7)-(8) and |y(t)| comparable to e^(ct) make the right side of

    |a+rho|<=|DU|+|grad P|/|U|

converge to zero. This would give rho=-a, already excluded. Hence rho<=-b.

The local pointwise jet classification A1017 in the team records says that, in an orthonormal basis of (Aw0)^perp,

    M restricted to (Aw0)^perp=[[mu,-nu],[nu,-mu]],
    nu!=0, lambda=2nu/|Aw0|,
    eta=|mu/nu| in {0,q-1,2q-1}.

The two eigenvalues of DF/lambda are a(1+eta)/2 and a(1-eta)/2. By rho<-a and (6), the positive one is -rho, independent of the sign of lambda. Thus only rho=-b/2 or rho=-b is possible. The pressure gap selects rho=-b and eta=2q-1. This last jet case has grad S(w0)!=0. Since b-a=1, (6) gives the spectra in Section 1.

Dot DB(p0)^T U(p0)=-bU(p0) with n0. The skew rotation contributes n0.Jn0=0, so c+n0.sym DU(p0)n0=-b. Because -b-c=c-2, this proves (1). In the displayed basis, |sym M|^2=2mu^2 and |W|^2=4nu^2, proving (2).

## 3. Scalar surfaces and their local reciprocal weight

The actual tail identities on the open zero-k cone are

    X.grad S=-bS, W.grad S=0, aV=X cross W.

At w0, W=lambda X with lambda!=0, so S(w0)=0. Since V(w0)=0, P2(w0)=S(w0)=0 and

    grad P2(w0)-grad S(w0)=M^T V(w0)=0.

The third resonance established above gives their common nonzero gradient. V is locally C^(1,alpha) and P2 locally C^(2,alpha) for every 0<alpha<1, so both S and P2 are C1 near the point. The implicit function theorem gives their separate zero surfaces and sign changes. Twisted homogeneity propagates (3) along the ray e^(tA)w0, and puts that ray in each zero set. Equality of the first derivatives at one point does not imply equality of the two surfaces.

The angular derivative of S is also nonzero at w0. Indeed X.grad S=0 there; if grad S had zero tangent projection to S2, it would be a multiple of w0, and w0.X=c>0 would force that multiple to vanish. Thus S is a transverse coordinate on a sphere patch as well as on an ambient patch. A C1 coordinate change has bounded local Jacobian and inverse Jacobian. In these coordinates the only singular integral is a bounded factor times

    integral_(-epsilon)^epsilon |s|^(-a/b) ds < infinity,

because 0<a/b<1. This proves only local integrability near this regular scalar zero.

For completeness, the determinant of DF is -b lambda^2<0. The tangent-velocity derivative has determinant

    det DY(w0)=(c^2/|Aw0|^2)(nu^2-mu^2)<0,

since eta=2q-1>1. This verifies both nondegenerate saddle assertions without using the nodal mass estimates, whose noninterior-node hypothesis fails in this open zero-k cone.

## 4. Exact positive asymptotic constants on the original line

By definition of the actual scattering map,

    e^(-tA)y(t)->w0.

The skew factor of e^(tA) is orthogonal, so e^(-ct)|y(t)| tends to |w0|=1. In particular, for all sufficiently large t, the derivative bound gives |DU(y(t))|<=C1 e^(-t), since c(p+1)=1. Thus

    integral_0^infinity |n(t).sym DU(y(t))n(t)| dt < infinity.

Integrating (7) with rho=-b yields the explicit positive constant

    C_U=|U(y0)| exp(-integral_0^infinity n(t).sym DU(y(t))n(t) dt),
    e^((b+c)t)|U(y(t))|->C_U.

Since b+c=2-c, this is the second limit in (4). It describes the first nonzero physical velocity along this orbit, whose leading homogeneous velocity is zero.

As A commutes with its exponential and U(y(t)) is negligible after multiplication by e^(-ct),

    e^(-ct)|B(y(t))|->|Aw0|.

Equation (5) then gives

    e^t|Omega(y(t))|
      =|lambda| e^(-ct)|B(y(t))|->|lambda| |Aw0|>0.

This proves all three limits, including both signs of lambda. No higher derivative or uniform remainder estimate on a neighborhood is used.

## 5. Verification, comparison and limitations

All six sections of the LIT200 submission were read and compared with the already confirmed A1018-A1022, A1017, A516 and A602 proofs. The independent argument above confirms its extra conclusions and resolves its formerly pending LIT199 dependency. Both pressure proofs give the same exponent and require the same natural bounds here. No numerical calculation or formal build is required.

The result imposes exact data at an actual vortical tail-velocity zero. It does not exclude that saddle, prove a global weighted flux estimate, exclude supported flat velocity zeros, remove zero helicity, or derive derivative decay from bare velocity decay. The unrestricted rotating-profile conjecture remains open.

The source and this auditor are configured the external referee (a second model). CO48 provides a received coordinator comparison of the earlier endpoint and quotient arguments, with the coordinator configured model. A focused reply on this exact-rate refinement remains pending; actual provider runtime is not independently attested. No new model client or invocation was used.
