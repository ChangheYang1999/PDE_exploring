# A strain gap at infinity and quantitative decay of the profile gradient

Status: CONFIRMED by A476-A477 after full independent reconstruction, repeated postwrite inspection and the focused configured-model A15 review. This proof corrects the sign of the submitted Biot-Savart kernel and allows dependence on the initial compact-annulus C2 norm. No nonexistence theorem follows without further hypotheses.

## 1. Exact statements and conventions

Let 0<c<1, omega in R, and J(x1,x2,x3)=(-x2,x1,0). Let U in C2(R3;R3) and P in C1(R3) solve pointwise

    (1-c)U+B.grad U+omega JU+grad P=0, div U=0,
    B=Ay+U, A=cI-omega J.

Assume M0=sup|U|<infinity. Set W=curl U, S=sym DU, with operator norm for DU, and

    Lambda=limsup_(|y|->infinity) lambda_max(S(y)),
    m(r)=sup_(|y|>=r) ||DU(y)||,
    (D): integral_1^infinity m(r) dr/r<infinity.

Since tr S=0, Lambda is a well-defined extended number in [0,infinity].

**Localized decay proposition.** Suppose additionally C1=sup||DU||<infinity and there are 0<kappa<=1, C2>=0, R1>0 such that

    |W(y)|<=C2 |y|^(-kappa/c), |y|>=R1.             (1)

Then there are finite C,R, depending on this profile and the displayed parameters, such that

    ||DU(y)||<=C(|y|^(-kappa/c) log|y|+|y|^(-1)),
    |y|>=R.                                         (2)

In particular, dependence on a C2 norm on one compact annulus is allowed. A uniform bound using only M0,C1,C2,R1,c is not asserted.

**Strain-gap theorem.** If Lambda<1, then C1<infinity and (1)-(2) hold for every 0<kappa<1-Lambda. Consequently the following five conditions are equivalent:

1. DU tends uniformly to zero at infinity.
2. Lambda<1.
3. Lambda=0.
4. (D) holds.
5. ||DU(y)||<=C(1+|y|)^(-theta) for some C<infinity and theta>0.

Thus Lambda and limsup||DU|| each belong to {0} union [1,infinity]. Infinity is allowed.

**Natural-rate corollary.** Assume also 1/3<c<1 and U(R .) tends to zero in distributions as R tends to infinity. Then the preceding conditions are also equivalent to

    ||DU(y)||<=C(1+|y|)^(-1/c).                      (3)

This last statement uses the confirmed scattering-tail theorem A210. Boundedness and distributional dilation decay are exactly the hypothesis denoted Hb there. Uniform decay of U implies Hb but is not needed for (2).

All assertions are for arbitrary fixed omega. No pressure estimate, pressure normalization, helicity premise or angular symmetry is imposed. The vorticity equation is the only differential consequence of momentum used in the new argument.

## 2. From the strain bound to bounded gradient and vorticity decay

Assume Lambda<1 and choose 0<kappa<1-Lambda. Outside a sufficiently large ball, lambda_max(S)<=1-kappa. If lambda1>=lambda2>=lambda3 are its eigenvalues, trace zero gives

    0<=lambda1<=1-kappa, lambda3>=-2lambda1>=-2.

Hence ||S||<=2 there. The profile curl equation is

    B.grad W=DU W-W-omega JW,
    B.grad|W|^2=2 W.(S-I)W<=-2kappa|W|^2.            (4)

Completeness of B follows from its at most linear growth. Choose R1 greater than both the strain radius and 2M0/c. Along an exterior characteristic, r=|y| obeys

    cr-M0<=r'<=cr+M0.

Every point outside R1 therefore has a unique backward crossing of that sphere in finite time. To see finiteness, while r>=R1 the reverse radial derivative is at most -cr/2. The whole segment after the crossing stays exterior. If its forward duration is t, then

    r(t)<=(R1+M0/c)e^(ct).

Integrating (4) gives (1), with C2=(R1+M0/c)^(kappa/c) sup_(|y|=R1)|W(y)|. Since the skew part of DU has norm |W|/2, the exterior gradient is bounded; compact C1 continuity bounds the interior. It remains to prove the localized proposition.

## 3. Physical coordinates and fixed-annulus bounds

Fix a terminal time T and put tau=T-t, s=-log tau, Q_s=exp(omega s J), y=exp(sA)x. The corresponding physical Euler field and vorticity are

    u(x,t)=exp((1-c)s)Q_s U(y),
    grad u=exp(s)Q_s DU(y)Q_s^T,
    xi(x,t)=exp(s)Q_s W(y).

The profile equation gives incompressible Euler, and the C2 spatial regularity gives its classical C1 vorticity transport equation

    (partial_t+u.grad)xi=(grad u)xi.                  (5)

Assume M0>0, since otherwise U=0. Put L=2M0/c and choose t0 in [T-1,T) so that

    L(T-t0)^c<=1/8, (T-t0)^(-c)/16>=R1.

On t0<=t<T,

    |u|<=M0 tau^(-(1-c)), ||grad u||<=C1/tau,
    |xi|<=w(t):=C3 tau^(-(1-kappa)) for |x|>=1/16.    (6)

The bounds for u and w are integrable in time because c,kappa>0. Constants below may depend on a compact-annulus C2 norm of U corresponding to time t0. They are uniform over centers xstar on the unit sphere.

## 4. Local elliptic estimates, with the correct Biot-Savart sign

Let N(x)=1/(4pi|x|), so -Delta N=delta0. Define

    BS f=curl(N*f)
        =(1/(4pi)) integral f(z) cross (x-z)/|x-z|^3 dz.

The order of the cross product matters. It yields

    div BS f=0, curl BS f=f+grad(N*div f).             (7)

Choose a smooth cutoff chi0 supported in {1/16<=|x|<=16}, equal to one on {1/8<=|x|<=8}, with values in [0,1]. Let v=BS(xi chi0), h=u-v. The source div(xi chi0)=xi.grad chi0 vanishes on N0={1/8<|x|<8}. Equation (7), div u=0 and curl u=xi imply Delta h=0 there as distributions. Weyl's lemma makes h smooth and harmonic there. It need not be curl-free: curl h=-grad(N*(xi.grad chi0)) can be nonzero on N0, although its curl is zero. Only harmonicity is used. Since the Biot-Savart kernel has degree -2 and integrable singularity, |v|<=Cw. Interior harmonic estimates on N1={1/4<=|x|<=4} give

    |Dh|+|D2h|<=C Z(t),
    Z(t)=tau^(-(1-c))+w(t).                          (8)

For compactly supported Holder f, the degree -3 kernel of D BS consists of smooth zero-spherical-mean kernels and a constant matrix times f. Its elementary singular-integral estimates at Holder exponent 1/2 are

    [D BS f]_(1/2)<=C[f]_(1/2),                      (9)
    |D BS f(x)|<=C(epsilon^(1/2)[f]_(1/2)
      +||f||infinity(1+log(1/epsilon))+||f||1),        (10)

for 0<epsilon<=1. In (10), split the kernel at epsilon and1, subtract f(x) on the inner ball, and integrate r^(-1/2), r^(-1) and the bounded outer kernel, respectively. For (9), subtract the values at two points distance q apart. The near balls of radius2q contribute C[f]_(1/2)q^(1/2); subtract the center value using zero mean. On their common exterior, the difference of kernels is bounded by Cq r^(-4). Multiplying by [f]_(1/2)r^(1/2) and integrating gives C[f]_(1/2)q integral_(2q)^infinity r^(-3/2)dr=C[f]_(1/2)q^(1/2). The boundaries of the two near balls lie in a comparable annulus and satisfy the same bound. The local constant-matrix term is immediate. These estimates use only the kernel bounds and cancellation, with no unknown global C2 norm.

If f is bounded by w, supported in B16 and zero on E+d/2 for a ball E and 0<d<=1, direct integration gives

    sup_E|D BS f|<=Cw(1+log(1/d)),
    sup_E|D2 BS f|<=Cw/d.

Interpolation of the minimum of the oscillation and Lipschitz bounds on the convex ball gives

    [D BS f]_(1/2,E)<=Cw d^(-1/2)(1+log(1/d)).        (11)

For E+d contained in {1/2<=|x|<=3/2}, d<=1/16, take chi supported in E+d and equal to one on E+d/2, with |Dchi|<=C/d. Extending xi chi by zero,

    [xi chi]_(1/2,R3)<=[xi]_(1/2,E+d)+Cw d^(-1/2).

Pairs crossing the support boundary obey this estimate from the cutoff Lipschitz bound, so no extension of xi is needed. Decompose u=BS(xi chi)+BS(xi(chi0-chi))+h. Equations (8)-(11) give

    [grad u]_(1/2,E)<=C[xi]_(1/2,E+d)
      +Cw d^(-1/2)(1+log(1/d))+CZ,                  (12)
    sup_E||grad u||<=C epsilon^(1/2)
      ([xi]_(1/2,E+d)+w d^(-1/2))
      +Cw(1+log(1/epsilon)+log(1/d))+CZ.             (13)

## 5. Polynomial Holder control on shrinking balls

Fix |xstar|=1 and define

    r(t)=1/4+L(T-t)^c, B(t)=B(xstar,r(t)),
    Theta(t)=[xi(t)]_(1/2,B(t)).

These balls have radii between1/4 and3/8 and lie in the fixed annulus above. For a particle path ending at x in B(t), its backward displacement between rho and t is at most

    delta(rho,t)=(M0/c)((T-rho)^c-(T-t)^c).

Thus it stays in E(rho,t)=B(xstar,r(t)+delta), and

    E(rho,t)+delta=B(rho),
    M0(t-rho)<=delta(rho,t)<=1/16.                   (14)

The first equality is the reason for the factor2 in L. The lower bound follows from T-rho<=1 and c<1. For rho<t the margin is positive. The endpoint rho=t is irrelevant to integration.

The global gradient bound in (6) gives for two such backward paths

    |X1(rho)-X2(rho)|
      <=((T-rho)/(T-t))^C1 |x1-x2|.                 (15)

Integrate (5) along each path and subtract. The product Holder estimate for (grad u)xi, (12) with d=delta, and the inclusion E+d=B(rho) yield

    Theta(t)<=((T-t0)/(T-t))^(C1/2)Theta(t0)
      +integral_(t0)^t ((T-rho)/(T-t))^(C1/2)
       [(C1/(T-rho)+Cw(rho))Theta(rho)
        +Cw(rho)^2 ell(t-rho)+Cw(rho)Z(rho)] drho,   (16)

where ell(q)=q^(-1/2)(1+|log q|). Constants absorb M0 in (14). The kernel ell is integrable on (0,1]. In particular the localization has cost an integrable same-time margin term, not an unclosed seminorm on a larger future-time domain.

Put Y(t)=(T-t)^(C1/2)Theta(t). Since w,Z<=C/(T-rho), the inhomogeneous term in its inequality is at most

    a(t)=C(1+Theta(t0))(T-t)^(-2).

The remaining coefficient is beta(rho)=C1/(T-rho)+Cw(rho). The seminorm is finite and locally bounded before T, since xi is C1 on compact cylinders. It is Borel: it is the supremum of continuous difference quotients over pairs that remain in continuously moving open balls, or equivalently is lower semicontinuous. Integral Gronwall with nondecreasing a gives

    Theta(t)<=C4 (T-t)^(-N), N=2+3C1/2.              (17)

Here integral_(t0)^T w is finite. The constant C4 is uniform in xstar because Theta(t0) is bounded by the gradient of xi on the one compact annulus {1/2<=|x|<=3/2}. This is the local C2 dependence stated in Section1.

## 6. Returning to the profile

In (13) take E=B(xstar,1/8), d=1/16 and epsilon=(T-t)^(2N). The enlarged ball lies in B(t). Equations (17) and (6) give uniformly on |xstar|=1

    ||grad u(xstar,t)||
      <=C[1+tau^(-(1-kappa))(1+log(1/tau))
            +tau^(-(1-c))].                         (18)

Given large y, choose s=(log|y|)/c, t=T-exp(-s) and xstar=exp(-sA)y, whose norm is1. Multiplication of (18) by tau=|y|^(-1/c) gives (2); the extra |y|^(-1/c) term is bounded by |y|^(-1), since c<1. This proves the localized proposition and the strain-gap theorem.

For the equivalences: (D) implies m(r)->0 by monotonicity and the dyadic integral bound. Gradient decay implies Lambda=0; Lambda=0 implies Lambda<1; the theorem gives a positive power rate by absorbing the logarithm with an arbitrarily smaller exponent. A power rate implies (D). If either Lambda or limsup||DU|| were strictly between0 and1, the theorem would force it to be0. This proves the asserted gap, including its endpoint interpretation.

## 7. Removing the logarithm under the scattering hypotheses

Assume Hb, 1/3<c<1 and one of the equivalent conditions. The confirmed theorem A210 applies under (D) and gives

    |W(y)|<=C|y|^(-1/c),
    |U(y)|<=C|y|^(-(1-c)/c), |y|>=1.                (19)

Thus xi and u are uniformly bounded on the annulus |x|>=1/16 for t sufficiently close to T. In (8)-(13) we may take w and Z constant. The harmonic term only needs the velocity bound on its fixed annulus, so no global boundedness of the physical velocity up to T is asserted.

Let G(t)=sup_(|x|>=1/2)||grad u(x,t)||. From (D),

    integral_(t0)^T G(t)dt
      =integral_(s0)^infinity m(exp(cs)/2)ds
      =(1/c) integral_(exp(cs0)/2)^infinity m(r)dr/r
      <infinity.                                   (20)

The same shrinking balls and the global velocity displacement estimate still apply. Their convexity ensures that the segment between any pair of paths remains in the annulus where G controls the gradient. Thus (15) improves to a uniform Lipschitz factor exp(integral G). Repeating (16),

    Theta(t)<=C Theta(t0)
      +C integral_(t0)^t [(G(rho)+1)Theta(rho)
                           +ell(t-rho)+1] drho.

Gronwall and integrability of ell and G give a uniform Holder bound through T. Equation (13) with fixed epsilon=1 now gives a uniform physical gradient on the unit sphere. Return to profile variables to obtain (3). Conversely (3) plainly gives a positive power rate. This proves the natural-rate equivalence with exactly the stated Hb and c>1/3 assumptions.

## 8. Physical singularity sets and scope

For the globally self-similar physical field define Sigma_I as the set of nonzero xstar where

    limsup_((x,t)->(xstar,T),t<T) (T-t)||grad u(x,t)||>0,

and define Sigma_L as the set of nonzero xstar where the spatial gradient is not bounded on any spacetime neighborhood below T. These are the precise gradient-based sets of the separate C34 reconstruction; no temporal Lipschitz extension is implied. Its elementary scaling proof gives Sigma_I empty iff DU->0, and Sigma_L empty iff (3). Hence Sigma_I empty iff (D) under the strain-gap theorem, and Sigma_I, Sigma_L are simultaneously empty or nonempty under the natural-rate hypotheses.

Define Sigma_S by replacing the quantity in Sigma_I with (T-t)lambda_max(sym grad u) and requiring limsup at least1. Its eigenvalues are exactly those of S(y) after multiplication by T-t. Therefore Sigma_S is contained in Sigma_I. In fact the reverse inclusion follows by the following local version of Sections3-6.

Fix xstar!=0 outside Sigma_S. Since the strain limsup is strictly below1, choose rho in (0,|xstar|/2), kappa in (0,1) and t1<T such that

    (T-t)lambda_max(sym grad u(x,t))<=1-kappa,
    x in B(xstar,rho), t1<=t<T.                     (21)

Take t1 later so (M0/c)(T-t1)^c<rho/2. Every backward particle path ending in B(xstar,rho/2) at a time t>=t1 stays in B(xstar,rho) until t1: its displacement is bounded by the integral of the global velocity bound, which is at most (M0/c)(T-t1)^c. Existence on this finite interval follows from local C1 regularity and this displacement bound; no global gradient estimate is assumed here. Vorticity transport and (21) give

    |xi(x,t)|<=C(T-t)^(-(1-kappa)), x in B(xstar,rho/2).

The initial constant is a compact spatial supremum of xi at t1. Trace zero in (21) gives ||sym grad u||<=2(1-kappa)/(T-t) on the larger ball. Since the skew part has norm |xi|/2, it follows that ||grad u||<=C1local/(T-t) on B(xstar,rho/2), after increasing a finite constant.

Choose chi0 supported in B(xstar,rho/2), equal to one on B(xstar,3rho/8). The same non-solenoidal cutoff decomposition h=u-BS(xi chi0) has Delta h=0 where chi0=1. Its size is bounded by C[rho]((T-t)^(-(1-c))+(T-t)^(-(1-kappa))); hence its first two derivatives on B(xstar,rho/4) satisfy the same bound with different constants. This uses the global velocity bound, not a pressure normalization. The kernel estimates (9)-(13) apply with fixed lengths depending on rho.

For a center z in B(xstar,rho/32), put

    rlocal(t)=rho/32+L(T-t)^c, L=2M0/c.

Choose t0>=t1 so L(T-t0)^c<=rho/32 and t0>=T-1. All balls B(z,rlocal(t)), backward paths ending in them, enlarged balls at the earlier time, and the line segments between paired paths then lie in B(xstar,rho/4). Their same-time margin is still delta(q,t)=(M0/c)((T-q)^c-(T-t)^c). Their exact enlarged-ball identity is still E(q,t)+delta(q,t)=B(z,rlocal(q)). The local bound C1local/(T-t) now suffices for the paired-path estimate, because those connecting segments stay inside the controlled convex region. Thus the proof of (16)-(17) gives a polynomial Holder bound, uniformly in these centers z. Initial Holder constants are bounded on a single compact ball at t0.

Use the localized logarithmic estimate with E=B(z,rho/64) and d=rho/128, so E+d lies in B(z,rlocal(t)). The same epsilon=(T-t)^(2N) choice yields, uniformly for z in B(xstar,rho/32),

    (T-t)||grad u(z,t)||
      <=C[(T-t)^kappa(1+log(1/(T-t)))+(T-t)^c].      (22)

The harmless (T-t) term is absorbed since c<1. Both terms tend to zero. This proves xstar is outside Sigma_I, and therefore

    Sigma_I=Sigma_S.                                (23)

In particular every joint strain limsup at a nonzero spatial point belongs to {0} union [1,infinity]. The value1 may be approached from below; neither a strict inequality at an actual point nor a limit on a fixed spatial line is asserted. The exact self-similar symmetry makes both sets invariant under x->exp(sigma A)x for every real sigma, so a nonempty set contains a whole twisted ray. This is a joint spacetime concentration statement, not convergence along one particle trajectory.

Nothing here proves Lambda<1 from uniform decay of U. The bounded-profile theorem also includes nondecaying constant velocities and does not assert U=0. No computation is required: the argument consists of exact transport, kernel estimates, Gronwall and the previously confirmed scattering theorem. Numerical exponent checks would not resolve any analytic step and are not used.

## 9. Review record

The complete initial279-line submitted proof is pinned in the team records. Its displayed BS sign is corrected in Section4. Its restricted constant-dependence sentence is weakened explicitly in Sections1 and5 to include the compact-annulus C2 norm that its own proof uses. The focused review should inspect the Holder singular-integral bound, the harmonic decomposition for a cutoff vorticity that is not divergence free, the same-time margin and endpoint integrability, measurable seminorm and Gronwall, uniformity over the physical sphere, and the use of (D) in the natural-rate corollary. The full postwrite read is complete. The focused configured-model A15 review is pinned and has been checked in full, including its separate review of the local strengthening. A476-A477 give the final exact-scope verdicts. A further coordinator review was already running and is an additional check, not an assumed input.

The revised source, with both required corrections and the local equality (23), is separately pinned in the team records. Section8 reconstructs that new argument with explicit nested balls, local flow control and uniform initial norms. The local strengthening is included in A476 after the complete A15 response and a repeated independent check of every nested-ball inclusion. The A210 proof and its exact Hb and exponent hypotheses were also reread before A477.

Additional coordinator review read in full at 2026-11-03T05:20:10.741562+00:00: in the team records. Its three source-text repairs agree with this reconstruction; its optional final-ball names are now explicit above. The proposed further bootstrap remains an unaudited sketch. A476-A477 are unchanged.
