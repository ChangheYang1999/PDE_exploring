# Pressure transport at a vortical tail-velocity zero

Status: complete independent audit of LIT198, with the additional classification in Section 8. The remaining global zero-scalar branch is not excluded.

## 1. Exact local statement and global application

Fix 2/5<c<1/2 and omega in R. Write J(x1,x2,x3)=(-x2,x1,0), A=cI-omega J, X(x)=Ax, a=1-2c, b=2(1-c) and q=b/a>6. On an open subset D0 of R3 minus {0} invariant under delta_t=exp(tA), suppose V is locally C^(1,alpha) for every 0<alpha<1 and P2 is C1. Set W=curl V, S=P2-|V|^2/2. Assume

    div V=0, -Delta P2=partial_i partial_j(V_i V_j),
    V(delta_t x)=exp(-(1-c)t)exp(-omega tJ)V(x),
    S(delta_t x)=exp(-bt)S(x),
    k:=X.V=0, W.grad S=0.                              (1)

The pressure equation is distributional. The last equation need only hold in a neighborhood of the zero under discussion. No arbitrary homogeneous pressure correction is made.

Let w0 in D0 intersect S2 satisfy V(w0)=0 and W0:=W(w0)!=0. Put M=DV(w0). If

    |W0|^2>=2|sym M|^2,                                (2)

then

    M h=(W0 cross h)/2, sym M=0,
    S(w0)=0, grad S(w0)=0, D2S(w0)=0,
    P2(w0)=0, grad P2(w0)=0, D2P2(w0)=M^T M.            (3)

The Hessians in (3) exist at the point. No C2 neighborhood of V or S is claimed. The angular zero of Y(w)=V(w)-(w.V(w))w is nondegenerate with index +1. For one finite local C and some R>0,

    |S(w)|<=C|w-w0|^(2q),  |w-w0|<R.                  (4)

On the corresponding small open cone, P2 is nonnegative and its zero set is exactly the twisted ray through w0. Thus this ray consists of local pressure minima.

For the global application, assume additionally that these are the actual tails of U in C2(R3;R3), P in C1(R3) satisfying

    div U=0, (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0,
    |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1),
    p=(1-c)/c.

Let Tflat={w in S2: V(w)=0,DV(w)=0} intersect supp(W|S2). The already confirmed A974/A984 and A999-A1002 say that if U!=0 and Tflat is empty, then k=0 globally and W!=0 is dense. At this scope, all angular velocity zeros are nondegenerate, and at least two distinct ones satisfy (3)-(4). This is a necessary configuration, not a contradiction or an original-profile realization theorem.

## 2. The oblique projection and its derivative

Differentiating the two homogeneity constraints gives

    DV X=-(1-c)V-omega JV,
    grad k=X cross W-aV.

Thus aV=X cross W. At w0, put X0=Aw0. Since w0.X0=c>0, X0 is transverse to T=T_(w0)S2. The zero and the differentiated constraints give

    M X0=0, M^T X0=0, W0=lambda X0, lambda!=0.          (5)

Let G=X0^perp, oriented by X0/|X0|. The restriction of M to G has, in an orthonormal basis diagonalizing its symmetric part, the form

    Mbar=[[mu,-nu],[nu,-mu]], lambda=2nu/|X0|,
    |sym M|^2=2mu^2, |W0|^2=4nu^2.                    (6)

Here nu!=0, and (2) is mu^2<=nu^2. The sign of nu and lambda is unrestricted.

For nearby w in S2 set

    Pi_w=I-X(w) tensor w/c,
    rho(w)=w.W(w)/c, F(w)=Pi_w W(w).

Then Pi_w is the projection onto T_w S2 along X(w). Since X cross W=aV,

    F(w)=-a Pi_w(X(w) cross V(w))/|X(w)|^2.             (7)

This expression makes F C^(1,alpha), despite W being only C^alpha. No derivative of W is used. At w0, F=0 and rho=lambda. For sigma=S|S2, the transport equations give

    F.grad_T sigma=b rho sigma.                         (8)

Indeed W=F+rho X and X.grad S=-bS.

The orthogonal projection P_G:T->G is invertible, with inverse Pi_(w0)|G. In coordinates identified with G by P_G, formula (7) gives

    D:=DF(w0)=-(a/|X0|)R Mbar
      =(a/|X0|)[[nu,-mu],[-mu,nu]],
    R=[[0,-1],[1,0]].                                  (9)

Only the derivative of V contributes because V(w0)=0. The two eigenvalues r1,r2 obey

    r1=a(nu+mu)/|X0|, r2=a(nu-mu)/|X0|,
    r_i/lambda in [0,a] under (2).                     (10)

These are the eigenvalues of the projected vortex field F, not of the tangent velocity Y.

## 3. The first two scalar jets vanish

Since W0=lambda X0, the identities W.grad S=0 and X.grad S=-bS first imply S(w0)=0. Hence P2(w0)=0.

In angular coordinates z centered at w0, let g=d sigma(0). Insert F(z)=Dz+o(|z|), rho(z)=lambda+o(1), sigma(z)=g.z+o(|z|) and grad sigma(z)=g+o(1) into (8). The terms linear in z give

    gD=b lambda g.

By (10), b lambda is not an eigenvalue because b>a and lambda!=0. Thus g=0. The twisted radial identity and the transversality of X0 give the full grad S(w0)=0.

Local elliptic regularity applies to

    Delta P2=-tr((DV)^2),

whose right side is C^alpha. Consequently P2 is locally C^(2,alpha). The displayed identity follows from the distributional equation and div V=0, with no second derivative of V required. At a velocity zero, grad(|V|^2/2)=DV^T V is differentiable, with derivative M^T M. Therefore

    Q:=D2S(w0)=D2P2(w0)-M^T M                           (11)

exists. Its angular restriction Q_T is the ordinary angular Hessian because g=0. Quadratic expansion of (8), requiring only F(z)=Dz+o(|z|), gives

    Q_T D+D^T Q_T=b lambda Q_T.                         (12)

One can use coordinates from (9), where D is symmetric. In a basis diagonalizing D, each entry of Q_T is multiplied by r_i+r_j-b lambda. These multipliers are nonzero: (r_i+r_j)/lambda belongs to [0,2a], while b>2a. Hence Q_T=0.

Differentiating X.grad S=-bS at the point is legitimate by (11). Since grad S(w0)=0, it gives QX0=0. Every vector is a sum of a vector in T and a multiple of X0. Thus Q_T=0 and QX0=0 imply Q=0 on all R3. This step does not differentiate a merely continuous vorticity or assert a C2 tail neighborhood.

## 4. The Poisson trace and the angular index

Taking the trace of (11) gives

    Delta S(w0)=-tr(M^2)-|M|^2=-2|sym M|^2.             (13)

The left side vanishes by Section 3. Therefore mu=0, M is skew symmetric, and its skew part is exactly [W0 cross]/2. This proves every identity in (3), including

    D2P2(w0)=(|W0|^2 I-W0 tensor W0)/4.

The tangent velocity Y and V have the same zeros: a radial V perpendicular to X must vanish because w.X=c. At a zero, DY is the orthogonal tangent projection of M. The direct determinant calculation in A1000 gives

    det DY(w0)=(c^2/|X0|^2)det Mbar
               =(c^2/|X0|^2)nu^2>0.                 (14)

Thus the zero is nondegenerate with index +1. In particular the initially allowed equality mu^2=nu^2 cannot occur. The oblique projection used to derive (9) and the orthogonal tangent projection used in (14) have distinct purposes.

## 5. Exact value order and the local pressure minimum

With mu=0, (9) becomes DF(w0)=(a lambda/2)I in every coordinate basis. Fix any one 0<alpha<1. Let epsilon=sign(lambda), ell=|lambda|, F_*=epsilon F, rho_*=epsilon rho and d=a ell/2>0. In a small coordinate disk,

    F_*(z)=dz+O(|z|^(1+alpha)),
    rho_*(z)=ell+O(|z|^alpha),
    F_*.grad sigma=b rho_* sigma.                       (15)

Choose its radius R so the radial logarithmic speed of F_* lies in [d/2,3d/2]. For every 0<|z|<R, the forward orbit reaches radius R at a finite time T, and its radius increases strictly before then. If r(t) denotes that radius, then

    integral_0^T r(t)^alpha dt<=2R^alpha/(alpha d),
    log(R/|z|)=dT+O(1),
    integral_0^T rho_*(z_t)dt=ell T+O(1).               (16)

All O(1) bounds are uniform over the starting points in this disk. They follow by integrating d(log r)/dt=d+O(r^alpha), with the first inequality controlling the accumulated error. Integration of the linear scalar ODE in (15), without dividing by sigma, yields

    |sigma(z)|<=sup_(|u|=R)|sigma(u)| exp(-b ell T+O(1))
              <=C|z|^(b ell/d)=C|z|^(2q).

Local equivalence of the chart distance and the sphere distance proves (4). No derivative of order 2q is inferred.

Nondegeneracy of Y implies |V(w)|>=m|w-w0| on a smaller disk for some m>0. Since 2q>2, (4) then gives |S|<=|V|^2/4, and

    P2=S+|V|^2/2>=|V|^2/4.

It is strictly positive off w0 on this disk. Both P2 and |V|^2 have homogeneity factor exp(-bt); a neighborhood of the ray is obtained by twisting and dilating the disk. This proves the claimed local minimum and its exact local zero set. The positive transverse pressure Hessian and positive Laplacian at the ray are consistent with this conclusion.

## 6. The global count

Use the actual-profile hypotheses and the previously confirmed alternative in Section 1. If U!=0 and Tflat is empty, k=0 globally and nonzero W is dense. At each velocity zero (5)-(6) hold.

A degenerate zero with W!=0 would satisfy mu^2=nu^2. Sections 3-4 exclude it. If W=0, M is symmetric, has zero trace, and annihilates X0. If M!=0 its two eigenvalues on G are nonzero and opposite, so the angular zero is a nondegenerate saddle of index -1. If M=0, density of W!=0 puts it in Tflat, contrary to the hypothesis. Every zero is therefore nondegenerate.

The zero set is closed in the compact sphere. If it were infinite, an accumulation point would itself be a zero and would not be isolated, contrary to nondegeneracy. Hence it is finite. Poincare-Hopf gives n_plus-n_minus=2. Every positive-index zero has nu^2>mu^2, necessarily W!=0, so Sections 3-5 apply. Thus n_plus>=2 and there are at least two distinct pure rotation zeros with the stated pressure behavior.

## 7. Dependencies, verification and limits

The local argument uses only (1), legitimate pointwise jets, the two distinct projections and the Poisson equation. The global application additionally uses the actual-tail existence and regularity, the no-Tflat alternative A974/A984, and the dense-vorticity conclusion A999. It does not use completeness of the tail vortex flow or transfer it from the original vorticity flow.

The source is the complete eight-section LIT198 proof. It was read in full and every step above was independently reconstructed. No computation is necessary: the theoretical test is whether the first- and second-jet equations use available derivatives and have nonzero multipliers. Equations (9)-(13) give that test exactly. Source bytes and hashes are retained under verification. No numerical observation is called a proof and no Lean/Lake build was run.

Neither the local pressure minimum nor the global index count excludes a nonzero profile. No global sign of P2 or S, maximum-principle conclusion, infinite-order flatness, analytic continuation or realization as an original W1 half-line follows. HF and the full natural derivative bound remain premises in the global application. Existing configured model comparison is requested through team files and is not counted as a received focused response.

## 8. Additional first-jet classification without the index inequality

The same calculation gives an independent refinement. Retain the local hypotheses (1) and V(w0)=0,W0!=0, but drop (2). Use mu,nu from (6) and let eta=|mu/nu|. Then necessarily

    eta in {0,q-1,2q-1}.                               (17)

The case eta=0 is exactly (3)-(4). If eta=q-1, grad S(w0)=0 and D2S(w0) is negative semidefinite of rank one. If eta=2q-1, grad S(w0)!=0. Both nonzero-strain cases are angular saddles, since q>6 makes eta>1. These are necessary conditions, not existence assertions.

To prove this, the first-order equation gD=b lambda g remains valid for any mu. If g!=0, one eigenvalue of D equals b lambda. By (9),

    (a/2)(1+mu/nu)=b or (a/2)(1-mu/nu)=b,

so eta=2q-1. Conversely, if eta differs from 2q-1, then g=0, and hence the ambient gradient vanishes. The second derivative Q exists by (11) independently of the gradient. When g=0 its angular restriction obeys (12) and QX0=0. In the eigenbasis of D, the possible second-order multipliers are 2r1-b lambda, r1+r2-b lambda, and 2r2-b lambda. The middle is (a-b)lambda!=0. The other two vanish exactly at eta=q-1.

If mu!=0, equation (13) gives tr Q=-4mu^2<0, so Q cannot vanish. Since QX0=0 and R3=T+RX0, its angular restriction cannot vanish either. Therefore eta=q-1. Only one diagonal entry in its D eigenbasis can survive; Q has rank one and its negative trace makes it negative semidefinite. Since q-1 and 2q-1 are distinct, the first-order equation forces grad S=0 in the former case. In the latter case grad S cannot vanish, because that would force the incompatible second-order resonance eta=q-1.

Finally eta=0 is the pure rotation case already proved, and every other eta is excluded by these two alternatives. This derivation uses no quadratic expansion of F when g!=0; such an expansion would not follow from C^(1,alpha) regularity. It also makes no statement about higher jets in the nonzero-gradient case.
