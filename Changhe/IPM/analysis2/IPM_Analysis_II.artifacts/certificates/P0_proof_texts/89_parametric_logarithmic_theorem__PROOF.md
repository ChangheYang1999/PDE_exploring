# A logarithmic conditional theorem with adjustable higher derivatives

The bounds on the third velocity derivative and fourth density derivative can be enlarged by reducing the logarithmic parameter. The third density derivative also enters the native second-derivative energy. A larger coefficient in the derivative hierarchy controls that contribution. This gives explicit sufficient parameters for every finite set of these three bounds, while keeping the same native low metric and the same inverse and contraction constants.

## 1. Exact hypotheses and spaces

Use the canonical full-plane velocity U=(-R1R2,R1^2), with no harmonic addition, and Fourier inversion factor (2pi)^(-2). All densities are real, even in x and odd in y. All derivatives are ordered Cartesian tensors with Euclidean norm. Let rho and u=U[rho] be smooth sublinear reference fields of these parities, with every derivative of polynomial growth. Suppose

    R=2^31, d=4/9, 9/5<c<37/20,
    a0=rho_y(0)>=1, c+c[rho]=1, c[h]=partial_y U2[h](0).

Set <r>=(1+r2)^(1/2),

    omega0=<r>^(-6/5), omega1=<r>^(-1/5),
    omega2=(1+4r2)^(2/5), w=(1+r2/R2)^(-11/10),
    V=cX+u, A=[[rho_y,-rho_x/2],[-rho_x/2,0]],
    Mlow=(2c+1)I+sym Du+A,
    Mj=(1+c+V.D log omegaj)I-j sym DV+A, j=1,2.

Require

    Mlow >= [2/5+(11/5)c r2/(R2+r2)]I for r<=R,
    M1>=I/2 and M2>=I/2 on R2,                                  (1)

and the four global decay bounds

    sup r^d(|D rho|+r|D2rho|)<=186,
    sup r^(-1+d)|u|<=22, sup r^d|Du|<=22,
    sup r^(1+d)|D2u|<=56.                                       (2)

Retain the following five fixed derivative bounds:

    |Du|<=14/5, |D rho|<=16, <r>|D2u|<=3,
    |D2rho|<=3, <r>|D2rho|<=8.                                  (3)

Replace the other three bounds by arbitrary finite nonnegative constants:

    <r>|D3u|<=U3, <r>2|D3rho|<=B3, <r>2|D4rho|<=B4.             (4)

All inequalities are required everywhere. Require a continuous nonzero leading function

    T^(-gamma)rho(TX)->G(X)=r^gamma Theta(theta), gamma=1/c,       (5)

uniformly on compact annuli. Put

    a=198+B3/24, G3=a^2+352.

Choose a finite hierarchy coefficient Astar satisfying

    Astar>=2048, 7 Astar^2>=200 G3.                              (6)

This coefficient is unrelated to the matrix A above. For definiteness one may choose Astar=2048*2^m with the smallest integer m>=0 satisfying (6). Define

    Kstar=max(525,
              432+(272 U3+816 B3)/Astar,
              312+(1088/3)B3+(2176/(3 Astar))B4),
    0<tau<=min(2^-20,1/(768 Kstar)), 1/2<beta<=1,
    Q=(1+tau log(1-Delta))^beta, C=tau^(-beta)/sqrt(2beta-1),
    Pj(h)=||omegaj D^j h||2, L(h)=||wh||_(Hdot^-1),
    Mstar(h)^2=P2(Qh)^2+Astar^2 P1(Qh)^2
                              +Astar^2 2^31 L(h)^2,
    r0=2^-20/C, eta=r0/32.                                    (7)

The high and low spaces are the compact smooth S1 core completions in Mstar and L respectively. The homogeneous negative norm is the canonical Fourier norm, equivalently dual to centrally odd homogeneous H1 tests. The high space is realized as tempered distributions, with continuous first derivatives of h and U[h]; set b[h]=h_y(0).

Define the maximal distributional operators

    Akh=(cX+u+U[k]).Dh-h+U[h].D rho,
    Bkh=Akh-c[h]X.D rho.

**Theorem.** Under (1)-(7), for every Mstar(k)<=r0, Ak generates a strongly continuous high semigroup, is bijective onto the high space, and has inverse norm at most32. More precisely its norm is at most exp(-lambda(k)t), where

    lambda(k)=1/25-(3/2)Kstar beta tau(1+11tau)^3
                          -2^12 C Mstar(k)>1/32.                (8)

Its domain is exactly {h in Mstar:Akh in Mstar}. Its native low realization is consistent in P0 with the high one and has inverse norm at most6 on common forcing. If h is high and Akh lies in L intersect P0, h belongs to that actual low generator domain.

The maximal Bk domain is D(Ak) intersect ker c. For c[k]=0 its range is exactly {f in Mstar:b[f]=0}, with inverse norm at most32. If the actual reference residual F=(cX+u).D rho-rho belongs to Mstar and Mstar(F)<=eta, there is a unique exact correction in the entire high ball Mstar(h)<=r0 at fixed c. It is normalized by c[h]=0, retains a positive center slope and the full leading profile (5), and is constructed by an L contraction with factor at most3/16. The four outputs of topic87, with their projected angular moment, satisfy

    L(h)+H(h)+M3(h)+|c[h]|<=128 C Mstar(h)
                                  <=2^12 C Mstar(Akh).          (9)

There is no uniform upper bound on U3,B3,B4 in this theorem. There is still a concrete positive residual threshold for each choice of the constants. The threshold decreases with tau, and increasing Astar increases the residual norm. This result does not certify the remaining hypotheses or the residual smallness of a refit.

## 2. Space realization and conversions for the new hierarchy

Let M denote the native norm with coefficient2048 from83/85, at the present tau and beta. On the common core,

    M(h)<=Mstar(h)<=(Astar/2048)M(h).                             (10)

Therefore the completions are the same distributional space, with equivalent Hilbert norms. The continuity of b,c and the literal circular principal value from70/72/77 are retained, together with the reference-free estimates of84. Since M<=Mstar, every product and gradient bound there holds with Mstar on the right and the same constant. In particular

    ||Dh||infinity,||DU[h]||infinity<=4 C Mstar(h),
    L(U[q].Dh)<=2^15 C Mstar(h)L(q),
    ||omega Q(af)||2<=800 C Mstar(h)||omega Qf||2                 (11)

for omega=omega1 or omega2, a=Dh or DU[h]. The centrally odd top velocity bound remains P2(QU[h])<=(9/5)P2(Qh).

Set H=Qh and E1n(h)^2=P1(H)^2+2^31L(h)^2. The native interpolation83 is unchanged:

    P0(H)<=E1n/128<=Mstar/(128 Astar),
    P1(H)<=Mstar/Astar, P2(H)<=Mstar.                            (12)

Consequently Sstar(H)=P2(H)+Astar P1(H)+Astar P0(H) satisfies

    Sstar(Qh)<=(sqrt2+1/128)Mstar(h)<3Mstar(h)/2.                 (13)

If Estar(H)^2=P2(H)^2+Astar^2P1(H)^2+Astar^2 2^31 L(H)^2, the same positive-kernel proof83 gives

    Mstar(h)<=(1+8tau)Estar(Qh),
    Estar(Qh)<=[1+77*2^(17/2)R^(6/5)tau]Mstar(h).                (14)

For the second estimate use L(Qh-h)<77R^(6/5)tau P0(Qh). Multiplying by Astar*2^(31/2) and inserting (12) cancels Astar exactly. Thus (14) has the same large conversion factor as83; it is not improved by hiding a change of norm.

## 3. Native reference energy with the third derivative retained

The first derivative and native low identities depend only on (1)-(3). With H=Qh they give

    -<D A0 H,omega1^2 DH> >=(1/8)P1(H)^2-2^28L(h)^2.

Adding2^31 times the native low energy1/5 L(h)^2 gives

    first-plus-low energy >=(1/8)P1(H)^2+(3/40)2^31L(h)^2
                            >=(3/40)E1n(h)^2.                  (15)

The stronger3/40, before rounding it to1/20 in83, is useful here.

The exact top energy from07 contains the term U[H].D3rho. Keeping its coefficient gives

    top energy >=P2(H)^2/2-198P1(H)P2(H)
                    -(16/3)B3 P0(H)P2(H)-352P1(H)^2.

By (12), the two cross terms are at most a E1n P2, with a=198+B3/24. Young's inequality a E1n P2<=P2^2/4+a^2 E1n^2 therefore gives

    top energy >=P2(H)^2/4-G3 E1n(h)^2.                          (16)

Adding Astar^2 times (15) yields at least

    P2(H)^2/4+[3/40-G3/Astar^2]Astar^2 E1n(h)^2.

Condition (6) implies G3/Astar^2<=7/200=3/40-1/25. The native reference energy is therefore at least Mstar^2/25. This proves explicitly why a finite enlargement of B3 can be handled, and why its effect is present before tau is introduced.

When B3<=4096, (6) already holds with Astar=2048. Indeed G3 is increasing in B3>=0 and at B3=4096 the exact inequality7*2^22>=200[(198+4096/24)^2+352] holds. Thus within this large range the hierarchy need not change at all. No claim that a particular refit has this global B3 upper bound is inferred from a few point values.

## 4. Explicit dependence of the logarithmic commutator

Write K=log(1-Delta). Differentiate the small-fractional component bounds43 at zero, using K=2(d/ds)J^s at s=0. Retain U3,B3,B4 in the cross terms instead of substituting16,32,512. The exact same tensor estimates give

    P2([K,A0]H) <=525P2(H)+(272 U3+816 B3)P1(H)
                                      +(2176/3)B4 P0(H),
    P1([K,A0]H) <=432P1(H)+(1088/3)B3 P0(H),
    P0([K,A0]H) <=312P0(H).                                   (17)

For clarity, the cross-weight ratios are omega2/omega1<=2<r>, omega2/omega0<=2<r>2, omega1/omega0=<r>. The top transport coefficient is2*34*(2U3)*2=272U3. The two top coupling cross terms total2*2*34*(2B3)*(3/2)*2=816B3. The top undifferentiated input coefficient is2*34*(2B4)*(8/3)*2=(2176/3)B4. The first derivative undifferentiated input coefficient is2*34*B3*(8/3)*2=(1088/3)B3. Each factor2 from an ordered product derivative or from differentiating J^s is present. The diagonal bounds525,432 are independent of these three higher derivatives. The P0 line uses only |Du|<=14/5, |D2rho|<=3 and the dilation coefficient, as in83.

Multiplying the last two rows by Astar and summing proves

    Sstar([K,A0]H)<=Kstar Sstar(H),                              (18)

with Kstar exactly as in (7). The positive inverse (1+eta K)^(-b) has Sstar norm at most1+11eta for0<b<=1; this uses the same weight moments componentwise and is independent of Astar. The positive-power resolvent formula77/81 therefore gives

    Sstar([Q,A0]Q^-1H)
       <=Kstar beta tau(1+11tau)^3 Sstar(H).                    (19)

Its scalar integral coefficient is beta. Applying (13) and Cauchy-Schwarz to the two derivative energy components bounds the smooth logarithmic energy loss by (3/2)Kstar beta tau(1+11tau)^3 Mstar(h)^2. There is no logarithmic term in the native low energy. Since tau<=2^-20, (1+11tau)^3<2 and beta<=1. Thus this loss is less than3Kstar tau Mstar^2<=Mstar^2/256.

These distributional commutator bounds first hold on the Schwartz graph core. The finite higher-derivative constants and polynomial growth hypotheses make the products and limiting differentiated kernel formulas legitimate. The inequalities then extend by their stated bounded norms.

## 5. Rough terms, generator and nonlinear conclusion

For W=U[k], the coefficient and gradient estimates (11) imply exactly the direct differentiated estimate85 with Mstar replacing M. Its diagonal contributions are below1772 C Mstar(k) and its top mixed contribution is at most1440 C Mstar(k). Their sum is less than2^12 C Mstar(k). The first-derivative hierarchy coefficient cancels when taking the maximum of the diagonal energy costs, so it introduces no factor Astar. The single top mixed term is estimated directly against Mstar(h) and P2(Qk), not through a discarded low component. Together with (15)-(19) this gives (8).

For completeness, construct the operator before using strict decay. For smooth compact k, the complete smooth transport flow and the bounded reference coupling give a base Estar generator; finite B3 suffices for the second derivative coupling. Its smooth logarithmic commutator is bounded, with constants possibly depending on the higher derivatives of this fixed k. Conjugation by Q and (14) give a high generator with graph core Q^-1(Cc-infinity). These construction constants need not be uniform in k. The direct form estimate just proved is uniform in Mstar(k).

For a general high k choose compact smooth km converging in Mstar. Equation (11) gives uniform convergence of their velocity gradients. The unique P0 characteristic evolution with bounded reference coupling is their common limit. The P0 difference source is bounded by ||DU[km]-DU[kn]||infinity P1(hn), which tends to zero under (12) and the positive inverse-kernel derivative estimate. Weak high compactness, lower semicontinuity and the norm bound at0 give the strongly continuous high semigroup. P0 uniqueness proves its semigroup law. The cutoff, local Friedrichs and high Bochner integral argument88 identifies its maximal distributional domain. Finite-time generator identities and strict decay prove onto and injective inverse directions separately.

The native low form loss is still12||DW||infinity<=48 C Mstar(k). At the prescribed r0 its rate exceeds1/6. The simultaneous low/P0 dense core, characteristic consistency and low Bochner domain argument88 are unchanged, since (10) leaves all sets of high distributions and their maximal domains unchanged. In particular the inverse bound6 applies to the nonlinear difference source, which is in both L and P0 by (11),(12).

The prescribed tau and r0 give

    lambda(k)>=1/25-1/256-1/256=103/3200>1/32.

The first-order identity is still b[Akh]=c[k]b[h]+a0 c[h]. The high growth exponent remains1/5, so rescaling with (5) proves D(Bk)=D(Ak) intersect ker c and the exact normalized range when c[k]=0. All these statements concern the same canonical distributions, with a changed but equivalent norm.

The map T(k)=-Ak^-1F preserves the normalized closed high ball because32eta=r0. Its difference has low bound

    L(T(k1)-T(k2))<=6*2^15 C r0 L(k1-k2)=3L(k1-k2)/16.

Weak high compactness identifies the low limit of every Cauchy sequence in this ball and retains c=0. The ball is complete in L. The contraction therefore gives the exact fixed point. Any high-ball solution has (a0+b[h])c[h]=0, and |b[h]|<=4Cr0=2^-18<a0 forces its normalization. This proves uniqueness in the entire high ball. The tail and exponent assertions follow from the fixed growth gap1/5<gamma. Equation (9) follows from87 and M<=Mstar.

## 6. Recovery, scope and numerical use

At U3=16,B3=32,B4=512, Astar=2048 is admissible, Kstar<2^14, and tau=2^-24 satisfies (7). Thus the earlier theorem85 is recovered with the same norm, radius, threshold, inverse32 and contraction3/16. The present smooth-loss formula is somewhat smaller; that improvement is not needed for recovery.

For any finite U3,B3,B4 there is a finite dyadic Astar satisfying (6), then a positive tau satisfying (7). One may choose both parameters as exact rationals when the derivative bounds are rational. In particular the fixed D4rho<=512 requirement is removed from this parametric theorem. To apply it to a specific candidate, actual global upper bounds must still be supplied; a certified pointwise lower bound such as D4rho>592 is not an upper bound.

The already proved native low floors carry directly to Mstar with an additional factor Astar/2048, because its native low coefficient is Astar*2^(31/2). For tau<=2^-20 and beta>1/2, eta<2^-35. Thus even this largest possible upper estimate for the new threshold is far below the existing original and refit native residual floors. This is a conditional theory extension, not a closure of the case4 existence problem. The fixed lower-order derivative, matrix and decay requirements remain as stated in (1)-(3).
