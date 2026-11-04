# Bounded velocity and bounded gradient force derivative decay

Status: independent reconstruction of LIT120. CONFIRMED as A492 after a complete independent proof, repeated full postreads and focused existing-agent review. Bounded DU is an explicit hypothesis. This settles that restricted derivative-decay question, without settling the full nonexistence conjecture.

## 1. Exact theorem and notation

Let U in C2(R3;R3) and P in C1(R3) solve

    (1-c)U+DU(Ay+U)+omega JU+grad P=0, div U=0,
    A=cI-omega J, 0<c<1, omega in R,

where J generates rotation around the third axis. Assume

    M=sup_R3 |U|<infinity, L=sup_R3 ||DU||_op<infinity.

Write G=DU, W=curl U and B=Ay+U. Then there are finite constants C,R0 such that

    |W(y)|<=C/|y|,
    ||DU(y)||<=C(1+log|y|)/|y|,                 (1)

for |y|>=R0. Consequently DU tends uniformly to zero and

    integral_1^infinity sup_(|y|>=r)||DU(y)|| dr/r<infinity. (2)

Constants may depend on c,omega,M,L and the C2 norm of U on one fixed compact annulus. No uniformity over omega or profile data is asserted. Velocity decay, finite energy, a pressure normalization and a helicity condition are not assumed. The cases M=0 or L=0 have G=W=0 and are immediate.

The only previously established analytic input is A485 and the elementary localized kernel estimate recalled and justified in Section2. A485 gives, for e(y)=Ay/|Ay|,

    |G(y)e(y)|+|W(y).e(y)|<=C/|y|, |y|>=1.      (3)

Since |Ay|>=c|y|, differentiation of this explicit e gives |De(y)|<=C/|y|. Also |W|<=2L. A485 itself uses only the hypotheses above and contains its complete actual-pressure and exterior-flow argument. Nothing in its proof requires (1) or (2).

## 2. A polynomial bound for local Holder seminorms

We first prove that some finite N>=1 satisfies

    [G]_(1/2,B(y,|y|/8))<=C |y|^N              (4)

uniformly at large |y|. This permits rapid growth of the seminorm and does not assume uniform continuity at infinity.

Set terminal physical time T=1, tau=1-t, s=-log tau, Q_s=exp(omega sJ), y=exp(sA)x. The exact rotating change of variables is

    u(x,t)=tau^(-(1-c))Q_s U(y),
    xi(x,t)=curl_x u=tau^(-1)Q_s W(y).

It solves physical Euler for t<1, and

    |u|<=M tau^(-(1-c)), ||grad_x u||<=L/tau,
    |xi|<=w(t):=2L/tau.                           (5)

The pressure scaling is irrelevant below. Every finite preterminal interval has a complete physical particle flow, because the velocity is globally bounded and globally Lipschitz on it.

Here is the local elliptic estimate used in transport. Let E be a ball centered on the unit sphere with E+d inside the fixed annulus 1/2<|x|<3/2, where E+d denotes the concentric radius enlargement and 0<d<=1/16. Then

    [grad u]_(1/2,E)<=C[xi]_(1/2,E+d)
       +C w d^(-1/2)(1+log(1/d))+C Z,
    Z=tau^(-(1-c))+w.                             (6)

All constants in this paragraph are uniform over these balls. To verify (6), choose a fixed smooth cutoff chi0 supported in 1/16<|x|<16 and equal to1 on 1/8<|x|<8. With N3(x)=1/(4pi|x|), define BS(f)=curl(N3*f). The difference h=u-BS(chi0 xi) is harmonic on 1/8<|x|<8: -Delta u=curl xi there and -Delta BS(chi0 xi)=curl xi there. It need not be curl-free. The integrable degree-minus-two kernel and bounded support give |BS(chi0 xi)|<=Cw on fixed inner neighborhoods, so |h|<=CZ there. Interior harmonic estimates bound its first two derivatives on the smaller fixed annulus by CZ, hence also the Holder seminorm needed in (6).

Choose a second cutoff chi supported in E+d, equal to1 on E+d/2, with |Dchi|<=C/d. The derivative of BS has a constant local term and a degree-minus-three kernel with zero spherical mean. For compactly supported f,

    [D BS(f)]_(1/2)<=C[f]_(1/2).

For clarity, at two points separated by q, subtract the center value on the balls of radius2q. The inner integrals are bounded by C[f]_(1/2)q^(1/2). On the common exterior the kernel difference is bounded by Cq r^(-4); multiplying by [f]_(1/2)r^(1/2) and integrating in three dimensions gives C[f]_(1/2)q integral_(2q)^infinity r^(-3/2)dr, again the stated bound. The boundaries of the removed balls lie in a comparable annulus and have the same estimate; spherical cancellation controls the constant terms. This is the usual direct homogeneous Holder estimate, not a continuation theorem.

The zero extension of chi xi satisfies

    [chi xi]_(1/2,R3)<=[xi]_(1/2,E+d)+Cw d^(-1/2).

Pairs crossing the support boundary satisfy the same bound by the cutoff Lipschitz estimate. The remaining data (chi0-chi)xi vanish at distance at least d/2 from E. Direct integration of its kernel gives supremum Cw(1+log(1/d)) and Lipschitz constant Cw/d for its BS derivative. Interpolating the oscillation and Lipschitz bounds on the convex ball gives Holder seminorm at most Cw d^(-1/2)(1+log(1/d)). Combining these terms with h proves (6). No integrability of w through T is used.

Choose t0<1 so close to1 that (2M/c)(1-t0)^c<=1/8. For each |xstar|=1 let

    d0(t)=1/4+(2M/c)(1-t)^c,
    Theta(t)=[xi(t)]_(1/2,B(xstar,d0(t))).

The defining balls lie in 1/2<|x|<3/2. Their initial seminorms are uniformly bounded by the C2 norm on a fixed compact annulus. For two particle paths ending in this ball at time t, their earlier displacement over [q,t] is at most

    delta(q,t)=(M/c)((1-q)^c-(1-t)^c).

They lie at time q in E(q,t)=B(xstar,d0(t)+delta), and its delta enlargement is exactly B(xstar,d0(q)). Further,

    M(t-q)<=delta(q,t)<=1/16,
    |X_1(q)-X_2(q)|<=((1-q)/(1-t))^L |X_1(t)-X_2(t)|. (7)

The lower displacement bound follows from 0<c<1 and 1-q<=1. The last inequality follows from the global gradient bound in (5), by backward Gronwall. The strict margin is available for q<t; the endpoint q=t has no effect on time integration.

Integrate d xi/dt=(grad u)xi along each path and subtract. At the earlier points, the product difference is bounded by

    [(L/(1-q))Theta(q)+w(q)[grad u]_(1/2,E(q,t))]
                                  |X_1(q)-X_2(q)|^(1/2).

Use (6) with d=delta and then (7). With ell(v)=v^(-1/2)(1+|log v|), whose integral on (0,1] is finite, this gives

    Theta(t)<=((1-t0)/(1-t))^(L/2)Theta(t0)
      +integral_(t0)^t ((1-q)/(1-t))^(L/2)
         [(L/(1-q)+Cw(q))Theta(q)
             +Cw(q)^2 ell(t-q)+Cw(q)Z(q)]dq.       (8)

Constants absorb the fixed positive M in (7). Set Y(t)=(1-t)^(L/2)Theta(t). Since w,Z<=C/(1-q), the inhomogeneous integral in (8), after this multiplication, is at most C(1+Theta(t0))(1-t)^(-2). Indeed (1-q)^(L/2)<=1, (1-q)^(-2)<=(1-t)^(-2), and ell is integrable. This is a nondecreasing majorant. The coefficient of Y is at most C0/(1-q), with finite C0. Integral Gronwall therefore gives

    Theta(t)<=C(1-t)^(-N0), N0=2+C0+L/2.          (9)

Every seminorm is finite and locally bounded for t<1, and Borel as a supremum of continuous difference quotients on continuously varying open balls. Thus Gronwall is applied to actual finite functions. The divergent integral of w only increases the finite polynomial exponent C0; it is never assumed finite at T.

Take E=B(xstar,1/8), d=1/16 in (6). Its enlargement is contained in the ball defining Theta(t). Equations (5),(9) give [grad_x u]_(1/2,E)<=C tau^(-N1) for a finite N1, uniformly over xstar. For a prescribed y of radius R, put tau=R^(-1/c) and xstar=exp(-sA)y, so |xstar|=1. The profile image of this physical ball is B(y,R/8). Rotations preserve Euclidean norms, and the exact seminorm scaling is

    [G]_(1/2,B(y,R/8))
        =tau^(1+c/2)[grad_x u]_(1/2,B(xstar,1/8)).

Increasing a finite exponent to N>=1 proves (4).

## 3. A logarithmic div-curl estimate with an explicit cutoff

Let v be C2 on B(0,2ell) in R^n, n=2 or3, with ell>=1. Choose a smooth cutoff chi equal to1 on B(0,ell), whose support is a compact subset of B(0,2ell), and whose derivatives have the usual powers ell^(-j). Extend chi v by zero. Let F be the collection

    div(chi v), partial_i(chi v)_j-partial_j(chi v)_i.

If ||F||_infinity<=epsilon and [F]_(1/2,R^n)<=K, then for 0<eta<=1,

    |Dv(0)|<=C_n[K eta^(1/2)
                    +epsilon(1+log(2ell/eta))].    (10)

Indeed Delta v_i=partial_i div v+sum_j partial_j(partial_j v_i-partial_i v_j). Apply this identity to the compactly supported chi v and its Newtonian representation. Its differentiated representation consists of second derivatives of the Newtonian kernel acting on components of F. In both n=2 and n=3 these are a bounded constant local term and a principal-value kernel of degree -n with zero spherical mean. On |z|<eta subtract F(0), giving C K integral_0^eta r^(-1/2)dr. On eta<|z|<2ell use the supremum, giving C epsilon log(2ell/eta). Outside the support F=0; the local term is C epsilon. This proves (10). Distributional integration by parts is legitimate for the compactly supported C2 field. In dimension two the logarithmic fundamental solution causes no extra harmonic gradient, since the differentiated identity is the exact compact-support representation.

In our applications ell is a positive power of R and K<=C R^N2 for a finite N2. Choosing eta=R^(-2N2-4) makes the near term O(R^-2), while log(2ell/eta)<=C(1+log R). There is no need to control a global Hessian norm by a power; the local Holder bound (4) suffices.

## 4. A frozen Euclidean plane controls the tangential block

Fix y, R=|y| large. Put n=e(y), P0=I-n tensor n, ell=R^(1/2), and on the fixed affine Euclidean plane y+n-perp define

    V(v)=P0 U(y+v), v in n-perp, |v|<2ell.

For R>256 the disk lies in B(y,R/8), and segments joining its points to y stay at radius at least R/2. The vector n and projection P0 are constant as v varies. At z=y+v,

    |e(z)-n|<=C ell/R,
    div_plane V=tr G(z)-n.G(z)n=-n.G(z)n,
    curl_plane V=W(z).n.                           (11)

The scalar curl uses the orientation whose unit normal is n. Equations (11) are exact two-dimensional derivatives; no derivative of a moving projection has been discarded. Explicitly |G(z)n|<=|G(z)e(z)|+L|e(z)-n| and |W(z).n|<=|W(z).e(z)|+2L|e(z)-n|. By (3), |G|<=L and |W|<=2L,

    |div_plane V|+|curl_plane V|<=C(1+ell)/R.

Multiplication by the cutoff of Section3 adds only terms Dchi times V, bounded by CM/ell. The full compactly supported planar div-curl data thus obey

    ||F||_infinity<=C R^(-1/2), [F]_(1/2)<=C R^N2. (12)

Here the Holder bound follows from (4), restriction to the plane, constant projections and the cutoff product rule. Bounded U and G bound the other product terms. Zero extension is harmless because the cutoff support lies strictly inside the disk; crossing pairs are controlled by its derivative bound. For instance [V]_(1/2)<=sqrt(2ML), by interpolating min(2M,L|v-v'|).

Apply (10) in dimension two with eta=R^(-2N2-4). At the center D_plane V=P0 G(y)P0 as an operator on n-perp. We obtain

    ||P0 G(y)P0||<=C R^(-1/2)(1+log R).            (13)

Thus the complete tangential block tends uniformly to zero. Neither small mean strain nor a bound on only its trace would imply this step; the exact planar derivatives and the bounded planar velocity are used.

## 5. Vorticity transport gives uniform inverse-radius decay

At each point now use its own e=e(y) and P=I-e tensor e. The exact matrix decomposition is

    G=H+e tensor g+h tensor e,
    H=PGP, g=PG^T e, h=Ge.                         (14)

The e-e entry is included in h tensor e, so it is not lost or counted twice. By (3), |h|+|W.e|<=C/|y| and |g|<=L. The block H satisfies (13). For q=|W|>0,

    W.GW<=||H||q^2+|W.e||g|q+|W.h||W.e|
           <=(||H||+C/|y|)q^2+Cq/|y|.           (15)

For the last term one may use |W.e|<=q and |h|<=C/|y|; for the middle term use the separate axial estimate. The full vorticity profile equation, valid for C2 U, is

    dW/ds=GW-W-omega JW

along the B flow. Its linear fundamental matrix is invertible on finite segments. A trajectory with nonzero terminal W therefore has q>0 throughout the segment, making differentiation of q legitimate. Skew rotation contributes zero, so

    q'<=-(1-||H||-C/|y|)q+C/|y|.                (16)

Choose beta=(1+c)/2, for which c<beta<1. By (13) a fixed R1 can be chosen with 1-||H||-C/|y|>=beta outside R1 and R1>2M/c. Since DB=A+G is bounded and B has linear growth, the B flow is globally complete. Its radial function obeys

    cr-M<=r'<=cr+M.

Every exterior point has a finite backward crossing of r=R1. Indeed otherwise r>=R1 for all negative times and the lower differential inequality r'>=cr/2 gives r(-t)<=r(0)e^(-ct/2), a contradiction for large t. The crossing is unique on the exterior segment because r'>0 there.

Parametrize the ensuing forward segment by 0<=s<=t, with r(0)=R1 and r(t)=R. With k=M/c the integrated inequalities give

    k+(R1-k)e^(cs)<=r(s)<=(R1+k)e^(cs)-k.

In particular R/r(s)<=C e^(c(t-s)). Integrate (16):

    q(y)<=2L e^(-beta t)
        +C integral_0^t e^(-beta(t-s))/r(s) ds
      <=C/R+(C/R)integral_0^t e^(-(beta-c)(t-s)) ds
      <=C/R.                                      (17)

The initial term is bounded by C/R because R<=(R1+k)e^(ct) and beta>c. The constant is independent of the crossing point and terminal direction. Trajectories with W identically zero satisfy (17) immediately. This proves the first assertion of (1).

## 6. A three-dimensional cutoff recovers the full gradient

Fix y of radius R and use ell=R/32. The ball B(y,2ell) lies inside B(y,R/8), and its radii are comparable to R. Apply Section3 in dimension three to v(z)=U(y+z). The cutoff divergence is only grad chi.U, bounded by CM/R, since div U=0. Its antisymmetric derivative data are bounded by C/R using (17) and the cutoff terms. By (4), all data have a Holder seminorm bounded by C R^N3 for some finite N3. Therefore (10), with eta=R^(-2N3-4), gives

    ||G(y)||<=C(1+log R)/R.

This proves the second assertion of (1). The function (1+log R)/R is nonincreasing for R>=1, and its integral against dR/R is finite. Boundedness on the remaining compact region proves (2).

## 7. Scope, circularity and collaboration checks

A485 -> polynomial Holder control using only bounded U,DU -> fixed-plane div-curl -> tangential block decay -> vorticity decay -> full derivative decay. Neither C38 mean decay, a derivative Dini condition, a vorticity decay condition, a strain gap nor an invariant-measure theorem is used to establish any arrow. The proof uses exact Euclidean planes and constant projections; it makes no ansatz about the profile. All omega are allowed, without division by omega or a smallness assumption. The restriction c<1 is used in A485, in the physical displacement and margin bounds, and in the choice c<beta<1.

If U also tends uniformly to zero and 1/3<c<1, the previously confirmed A477, with its scattering dependency A210, gives its stronger natural gradient estimate. That is an additional corollary, not a premise here. The theorem still does not show bounded DU from U->0, does not supply the interior growth hypotheses of the conditional coverage theorem, and does not exclude a general Euler profile in the campaign interval. The mandatory decay-only problem remains open.

The entire LIT120 source was read before this reconstruction and is pinned in verification. Sections2-6 above were checked independently, including the cutoff support, Holder scaling, signs of the radial inequalities and the damping exponent. The entire223-line coordinator review and the integral agent's independent complete C39 proof have now been read and checked. The coordinator review deliberately did not read this reconstruction, and independently agrees with every new step. Its kernel and pressure dependencies were read rather than rederived there; those dependencies and the inline Holder closure are proved in full above and in A485.

## 8. An independent planar check by Cauchy-Pompeiu

The integral agent's C39 supplies a second proof of the planar step, which we verify here. Let F be complex-valued and C1 on the closed disk of radius ell, and let g=dbar F be Holder with exponent alpha in(0,1]. Stokes applied to F(z) dz/z^2 on eta<|z|<ell, followed by eta tending to zero, gives

    dF(0)=(1/(2pi i)) integral_(|z|=ell) F(z) dz/z^2
             -(1/pi) PV integral_(|z|<ell) g(z) z^-2 dA.

The inner circle tends to2pi i dF(0): the constant and dbar F(0) zbar Taylor terms integrate to zero. The kernel z^-2 has zero angular mean. Subtract g(0) for |z|<delta and use its supremum on the remaining annulus. For0<delta<=ell this yields

    |dF(0)|<=sup_boundary|F|/ell
                 +(2/alpha)[g]_alpha delta^alpha
                 +2sup|g| log(ell/delta).

Choose an oriented orthonormal frame(f1,f2,n), let F=U.f1-i U.f2 on the frozen plane and H_ij=fi.G fj. Direct differentiation gives dF=((H11-H22)-i(H12+H21))/2 and g=-(n.Gn+i W.n)/2. Thus |dF(0)| is exactly the operator norm of the symmetric trace-free part of P0GP0. With ell=R^1/2, (3)-(4), and delta a sufficiently negative power of R, the bound is C R^-1/2(1+log R). Its trace and antisymmetric part at the center are O(1/R) by (3), recovering the entire matrix bound (13). This proof also exposes why control of divergence and curl alone would be insufficient without the Holder input.

## 9. Review outcome and immediate corollaries

All six precision points in the focused review are already explicit above: the Holder closure is part of this proof, De is differentiated directly, the planar triangle inequalities and large-radius inclusion are displayed, all trajectories are finite exterior segments, the larger harmless remainder in (15) is allowed, and every use of c<1 is named. There is no unresolved mathematical objection. The full proof was read again before confirmation. The coordinator is configured for the primary model; its review identifies a coordinator subagent without independent runtime model attestation. The integral agent author is separately configured for that same model, again configuration evidence only.

A476 now adds bounded DU to its equivalent conditions for bounded C2 profiles. Indeed bounded DU implies the Dini bound by this theorem; conversely Dini decay gives an exterior bound and compact regularity gives a global bound. Its strain bound Lambda<1 already implies bounded DU. Choosing kappa in(c,1) in A476 after Lambda=0 also improves the gradient bound here to O(1/R): its localized estimate is O(R^(-kappa/c)log R+R^-1). This stronger corollary still requires no velocity decay.

For every fixed physical exterior radius rho>0, (1) gives sup_(|x|>=rho)|grad u(x,t)|<=C_rho (1-t)^(c-1)(1+|log(1-t)|) near1, since (1+log r)/r decreases at large r. Its time integral is finite because c>0. The corresponding exterior vorticity supremum is at most C_rho(1-t)^(c-1), also integrable. This verifies the physical conclusions of the weaker integral-agent C39 estimate without its numerical checks. With uniform U decay and1/3<c<1, A477 gives the natural stronger derivative rate. None of these conclusions supplies the missing boundedness of DU from U tending to zero.
