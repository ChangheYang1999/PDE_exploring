# Axisymmetric actual tails have no regular pressure-deficit sheet

Status: CONFIRMED, A556, after complete source comparison and postread. This is a conditional tail theorem, not unrestricted profile nonexistence.

## 1. Exact theorem and application

Let1/3<c<1/2, omega finite real, p=(1-c)/c in(1,2), a=1-2c=c(p-1), Jx=(-x2,x1,0), A=cI-omega J and D=R3 minus{0}. Let V in C1(D;R3) and P2 in C1(D) be vector-axisymmetric and scalar-axisymmetric about the third axis, homogeneous of degrees-p and-2p. Write W=curl V, S=P2-|V|^2/2 and k=(Ax).V. Assume

    div V=0, V.W=0,
    -Delta P2=partial_i partial_j(V_i V_j) on D,
    W.grad S=0,
    grad k cross grad S=0 on {W!=0}.                 (1)

The pressure equation is distributional; all other quantities in (1) are continuous and their equalities classical. Then no x in D satisfies

    S(x)=0, grad S(x)!=0, W(x)!=0.                   (2)

Nonzero V at such a point need not be added as a hypothesis. A second consequence is that no open angular interval carries the nonzero meridional plateau V=r^-p H0 e_theta/sin(theta), H0!=0. No global or local assumption E=grad k=0 is imposed.

For a full globally helicity-free C2/C1 target profile,2/5<c<1/2,any finite omega, with natural bounds |U|<=C(1+r)^-p and |DU|<=C(1+r)^(-p-1), suppose its actual leading V is axisymmetric about the rotation axis. Then the A534/A536 escaping-sheet endpoint mu1 is impossible. The natural bounds may equivalently be supplied here by the confirmed U->0, DU=O(sqrt r) screen. This rules out rho=-2(1-c) at a vortical carrier equilibrium or lambda=2(1-c)/(1-2c) for the relevant general zero-g component. The symmetry of V is extra. It neither follows from A552's pressure-multipole symmetry nor implies that the full U is symmetric. Other rates and general tails remain open.

## 2. Full spherical formulas

Put z=cos(theta), s=sin(theta), w=1-z^2, t=omega/c. On -1<z<1 write

    V=r^-p[R e_r+(H/s)e_theta+(F/s)e_phi],
    P2=r^-2p u, S=r^-2p h,
    e=(R^2+(H^2+F^2)/w)/2, h=u-e,
    K=R-tF, k=c r^(1-p)K.                           (3)

The functions are C1 on the interior. Divergence and curl give

    H'=(2-p)R,
    W=r^-p-1[-F'e_r+(p-1)F e_theta/s
                         +(-(p-1)H/s+sR')e_phi].   (4)

Thus H in C2. Dotting the velocity with (4), the two meridional-azimuthal product terms cancel, giving

    F R'-R F'=0.                                   (5)

Dotting (4) with grad S gives

    2pF'h-(p-1)Fh'=0.                              (6)

The rank equation is

    grad k cross grad S
      =c s r^-3p-1[(p-1)K h'-2pK'h]e_phi=0         (7)

where W!=0. Cartesian continuity at a pole implies H=s V_theta->0 there. This is the only pole condition needed.

## 3. Regular zeros force a local nonzero plateau

An axisymmetric scalar gradient at an axial point is axial. Homogeneity gives x.grad S=-2pS. At an axial S-zero the gradient must therefore vanish. A point in (2) lies off the axis, at some z0 with h(z0)=0 and h'(z0)!=0.

Shrink to an interval about z0 where W!=0 and h' has no zero. On each punctured side h has no zero and (6) integrates to

    F=D_+ |h|^beta or D_- |h|^beta,
    beta=(p-1)/(2p) in(0,1/4).                      (8)

Indeed the derivative of F|h|^-beta is zero. A nonzero constant makes F' unbounded at z0 because h' has a nonzero limit and beta<1. Since F is C1, both constants vanish. Continuity gives F=0 on the whole smaller interval.

Now K=R. Equation(7) on that interval gives the same equation and argument for R, so R=0 there. Divergence makes H constant, say H0. If H0=0, V and W would both vanish on the interval, contradicting W(z0)!=0. Thus H0!=0, proving the local plateau claim and also the redundant V nonvanishing.

## 4. Actual Poisson and a positive endpoint constraint

For a C1 divergence-free field, local mollification and convergence in C1 verify partial_i partial_j(V_iV_j)=tr((DV)^2) distributionally. The spherical matrix M=r^(p+1)DV is

    [ -pR,    -sR'-H/s,              -F/s;
      -pH/s,   (p-1)R-zH/w,         -zF/w;
      -pF/s,   -F'-zF/w,             R+zH/w ].       (9)

Separated radial and angular tests in the pressure equation give

    (w u')'+kappa u=-tr(M^2), kappa=2p(2p-1).       (10)

The matrix is continuous and w>0 on each compact interior interval. Equation(10) with u in C1 implies u in C2. It does not imply second derivatives for R or F.

Consider a one-sided interval with endpoint q in(-1,1), on which

    (R,F)=b(b1,b2), b>0, b1^2+b2^2=1,
    h=C b^nu, nu=2p/(p-1)>4,                       (11)

and R(q)=F(q)=0. The constants in (11) belong only to this interval. Let Hq=H(q), dR=R'(q), dF=F'(q) and wq=1-q^2. On the interval b=b1R+b2F, so it extends C1 to q, b=O(|z-q|), b' is bounded. Thus h(q)=h'(q)=0 and h'=O(|z-q|^(nu-1)); its one-sided derivative at q is0.

Differentiate the kinetic energy only at q using difference quotients. The derivative of R R' there is dR^2, because R(z)=dR(z-q)+o(|z-q|) and R'(z)->dR. The F term is identical. The H term uses H'=(2-p)R and H in C2. The result is

    e(q)=Hq^2/(2wq), e'(q)=qHq^2/wq^2,
    e''(q)=dR^2+[dF^2+(2-p)Hq dR]/wq
                         +Hq^2[1/wq^2+4q^2/wq^3]. (12)

No R'' or F'' occurs. Since u=e+h is C2, its actual second derivative equals this one-sided value. At R=F=0 the matrix (9) gives

    tr(M^2)=2pHq dR+2pHq^2/wq+2q^2Hq^2/wq^2.

Substituting (12) into (10) yields exactly

    wq dR^2+dF^2+(p+2)Hq dR
      +[(2p^2+p+1)/wq+4q^2/wq^2]Hq^2=0.           (13)

The (dR,Hq) quadratic has first diagonal entry wq>0 and four times its determinant

    4wq[(2p^2+p+1)/wq+4q^2/wq^2]-(p+2)^2
                         =7p^2+16q^2/wq>0.         (14)

It is positive definite. The remaining term dF^2 is nonnegative. Hence (13) forces Hq=dR=dF=0. In particular a component of type(11) cannot end with Hq!=0.

## 5. The local plateau cannot end, including accumulating components

Extend the plateau of Section3 to the maximal connected open interval I on which R=F=0 and H=H0!=0. Suppose its right endpoint z* is interior. Continuity of the derivatives gives R=F=R'=F'=0 there. By (4), W(z*)=-(p-1)H0 e_phi/s is nonzero. Choose a small interval J around z* where W!=0 and |H|>=|H0|/2.

If there are nonzero amplitudes R^2+F^2 immediately to the right of z*, take one such point inside J and its component C of {R^2+F^2>0}. Its left endpoint q is at least z*, because a whole interval just to the left lies in the zero plateau. It is at most the chosen point, so belongs to J. At q the amplitude is0 and Hq!=0.

On C put b=(R^2+F^2)^1/2. Equation(5) gives that (R,F)/b is a constant unit vector: its normal derivative is0 because of its fixed length, and its tangential derivative is a multiple of R F'-F R'=0. Thus the first relation of (11) holds. If b2!=0, F=b2b never vanishes, and (6) gives h=C0 b^nu. If b2=0, F=0 and R=b1b is nonzero; (7), which is available on the portion(q,x) inside J, gives the same formula there. In either case the constant is finite on that fixed component segment. Section4 then contradicts Hq!=0.

Consequently no nonzero amplitude can occur immediately to the right, which extends the plateau past z*, a contradiction. The left endpoint is treated by reversing the interval. This uses one component at a time. Infinitely many components accumulating at z* do not require a uniform constant or a common nonvanishing-order assumption.

There are no interior endpoints, so I=(-1,1). Then H is the nonzero constant H0 all the way to both poles, contrary to H->0. This proves the plateau impossibility, and Section3 proves (2).

## 6. Checking the full-profile premises and scope

At the full-profile scope in Section1, A533/A538 give V in C1alpha locally, for every alpha<1. A530/A539 give its actual canonical P2 with at least C1 regularity. If V is axisymmetric, its twisted homogeneity becomes ordinary homogeneity. The canonical tensor pressure preserves that symmetry and has degree-2p. Uniform tail convergence of the velocity and its first derivatives passes div V=0 and the global zero-helicity identity to V. A531 gives W.grad S=0.

The rank condition is also a necessary tail condition, not an optional strengthening. On compact subsets of {W!=0}, the rescaled actual vorticity is nonzero for all large t. There the full A413 identity dH wedge d(P-|U|^2/2)=0 applies. Pull back by exp(tA) and multiply each covector by its respective positive scaling factor. The first scaled gradient converges locally uniformly to grad k by A509/A534; the second converges to grad S by A530/A539. Their wedge therefore tends to grad k wedge grad S=0. This is the global compact-annulus version of the rank step already used in A534.

At mu1, A534 or the A536 general-level version gives a scattering point where S=0, grad S=-V/f0!=0, V!=0 and W!=0. Section1 excludes that point if V is axisymmetric. All uses of full-profile information are explicit. The theorem does not apply to merely axisymmetric pressure, nor to the axisymmetric pressure multipole of A552, and it does not exclude mu>1 critical S-sheets. No unconditional derivative bound or unrestricted nonexistence is inferred.

## 7. Comparison and evidence

The complete LIT146 source was read and compared. Every spherical formula and coefficient in (13)-(14) was checked manually. Its local C1 proof and selection of a component next to a plateau were checked independently; no symbolic script was needed here. The narrower poloidal case is independently proved in auditor_proofs/reviews/proper_poloidal_cone_20261103/PROOF.md by a plateau-edge Peano expansion. These are two distinct ways to isolate the rank obstruction.

LIT144/LIT145 and CO28 can satisfy their smaller listed conditions, but their nonzero plateau violates (1) somewhere near its boundary. The exact canonical countertest remains useful at that narrowed scope. Existing configured-model source exchange continues through working files. No successful focused reply on this new synthesis is assumed before it is actually received. No new client, computation or formal build.
