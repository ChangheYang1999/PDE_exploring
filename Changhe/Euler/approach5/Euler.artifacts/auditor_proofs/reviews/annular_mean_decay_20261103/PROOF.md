# Annular mean decay with bounded velocity and gradient

Status: the exact SL, MS, MD and MD-prime conclusions are PROVED by A499 CONFIRMED as consequences of A492 and A476. The historical occupation proof is retained below; Section7 gives the stronger direct proof. No separate kinematic counterexample is certified.

## 1. Exact statement and dependencies

Let U in C2(R3;R3), P in C1 solve the full rotating Euler profile equation

    (1-c)U+DU(Ay+U)+omega JU+grad P=0, div U=0,
    0<c<1, omega in R, A=cI-omega J.

Assume M=sup|U|<infinity and C1=sup||DU||_op<infinity. Write G=DU, W=curl U, B=Ay+U, e=Ay/|Ay| on y!=0, P_h=I-e tensor e,

    g=P_h G^T e,
    S_h=sym(P_h G P_h)-(tr(P_h G P_h)/2)P_h.

All unlabelled constants are finite for each fixed profile. Sections2-5 track their dependence through c,omega,M,C1, the A485 constants and the fixed cutoff. The later Section7 corollary may also use the compact C2 norms in A492; it asserts no uniform estimate in only M and C1. For r>=4,

    integral_{r<|y|<2r}|S_h(y)|_F^2 dy <= C r^2.       (SL)

For every delta>0 there is C_delta<infinity with

    |{r<|y|<2r:|W(y)|>=delta}| <= C_delta r^2, r>=1.  (MS)

For delta>2C1 the set is empty. Moreover, with the explicit positive exponent

    eta=2/(4C1+16c+3),
    r^(-3) integral_{r<|y|<2r}|G|_F^2 <= C r^(-eta), r>=4.  (MD)

The letter eta is used here to avoid confusion with the vorticity transport coefficient 1+c. The source calls this exponent kappa.

A485 supplies bounded grad P, G Ay and the directional bounds |Ge|+|W.e|<=C/|y|, without a pressure normalization. Its exact pointwise algebra gives

    G=S_h+e tensor g+R, ||R||<=C/|y|,
    W=g cross e+O(1/|y|),
    tr(G^2)=|S_h|_F^2+O(1/|y|),
    |G|_F^2=|S_h|_F^2+|g|^2+O(1/|y|).              (2)

Also |W|<=2C1 and lambda=lambda_max(S_h)>=0 satisfies lambda<=2C1. For the former, skew G is the cross-product map with vector W/2, whose operator norm is |W|/2 and is at most ||G||. For the latter, ||sym(P_h G P_h)||<=C1 and |tr(P_h G P_h)|/2<=C1. The nonzero eigenvalues of S_h are lambda,-lambda, so |S_h|_F=sqrt(2)lambda.

## 2. Planar strain in mean

The equation upgrades P to C2 and gives Delta P=-tr(G^2). Choose a nonnegative smooth compactly supported phi, equal to1 on {1<=|z|<=2}, with support in {1/4<|z|<4}. Integration by parts over its compact support gives

    integral phi(z) tr(G(rz)^2) dz
      =r^(-1) integral grad phi(z).grad P(rz) dz.     (3)

This is a single derivative scaling, since div_z grad P(rz)=r Delta P(rz). Its absolute value is at most C/r by A485. The error term in (2) is uniformly O(1/r) on the support for r>=4. Hence the nonnegative integral of |S_h(rz)|^2 over the unit annulus is at most C/r. Changing variables gives (SL). There is no integration over an unbounded boundary and no assumed sign of tr(G^2).

If U tends uniformly to0, A485 gives grad P->0 and r(|Ge|+|W.e|)->0 uniformly. The same argument then gives o(r^2) in (SL). This refinement is not used in (MS) or (MD).

## 3. A vorticity peak forces time in a fixed strain region

The case C1=0 is immediate, so put L=2C1>0. Fix 0<delta<=L and set

    Delta=2 log(2L/delta)>=2 log2,
    H_*={|y|>=1, |S_h(y)|_F>=1/4}.

The field B is globally Lipschitz and has a complete flow Phi_s. Its divergence is3c, so det D Phi_s=exp(3cs). Along every trajectory, q=|Phi_s x| satisfies cq-M<=q'<=cq+M away from the origin. When q>=2M/c, this implies cq/2<=q'<=2cq.

If r is large enough that r0=r exp(-2c Delta) exceeds a fixed R_*>max(4,2M/c), then every backward segment Phi_{-s}y, 0<=s<=Delta, starting at r<|y|<2r stays in

    r0<=|Phi_{-s}y|<=2r.                              (4)

To justify that it stays exterior before applying the inequalities, use the maximal segment on which its radius exceeds R_*. Integration there gives the lower bound r exp(-2cs)>R_* at any putative earlier exit if r0>R_*. A harmless enlargement of the threshold ensures this strict inequality. Thus no exit occurs.

Fix y with |W(y)|>=delta and parametrize the forward segment by Y(s)=Phi_{s-Delta}y, 0<=s<=Delta. The exact C1 vorticity equation is

    dW(Y(s))/ds=G W-W-omega J W.

It is linear in W along a fixed orbit. Its invertible fundamental matrix shows that W(Y(s)) never vanishes on this finite segment. Therefore w(s)=|W(Y(s))| is C1. Rotation makes no contribution to its derivative. From (2),

    W.GW <= lambda |W|^2+C|W|/|Y|,
    w' <= (lambda(Y)-1)w+C/r0.                       (5)

For example, the e tensor g term has size at most |W.e||g||W|, and the R term is at most C|W|^2/|Y|; all unweighted factors are bounded. Only the upper bound lambda-1<=L is needed in the variation-of-constants estimate. The source's stronger parenthetical |lambda-1|<=L is false when L<1, and is unnecessary.

Integration of (5) and w(0)<=L gives

    delta <= L exp(integral_0^Delta(lambda-1))
                  +C Delta exp(L Delta)/r0.          (6)

Choose r so that the last term is at most delta/2. Taking logarithms in (6) yields integral_0^Delta lambda>=Delta/2. If t(y) is the time in this segment with lambda>=1/4, then

    Delta/2 <= L t(y)+Delta/4,
    t(y)>=Delta/(4L).                                (7)

Every such point belongs to H_*. If the bounds make (7) impossible because L is small, the peak set is empty at these radii, which is consistent with all ensuing estimates. No lower bound on C1 is assumed.

## 4. Occupation measure and a delta-dependent radius threshold

Let X_r(delta) be the peak set in (MS). Reverse the segment parameter in (7), integrate over y and use Fubini and the exact positive Jacobian:

    (Delta/(4L)) |X_r(delta)|
      <= integral_0^Delta integral_{r<|y|<2r}
                       1_{H_*}(Phi_{-s}y) dy ds
      <= Delta exp(3c Delta)
                        |H_* intersect {r0<=|z|<=2r}|.   (8)

All functions are Borel and the integration domain has finite measure. From (SL) and Chebyshev, H_* has volume at most C q^2 on every dyadic annulus q<|z|<2q with q>=4. Covering the range [r0,2r] by such annuli gives a geometric sum at most C r^2, independently of their number. It follows that

    |X_r(delta)|<=C exp(3c Delta)r^2
                   <=C delta^(-6c)r^2                (9)

whenever the chosen radius conditions hold. For a fixed delta these conditions give a finite radius r_delta; below it the elementary annulus-volume bound is at most C r_delta r^2. This proves (MS).

For the quantitative rate restrict to 0<delta<=min(1,L). The condition in (6) and (4) is satisfied if

    r>=C delta^(-N),  N=4C1+4c+2.                    (10)

Indeed exp(L Delta)=(2L/delta)^(4C1), exp(2c Delta)=(2L/delta)^(4c), and Delta<=C/delta. The remaining division by delta costs one more power. The fixed exterior threshold is also covered by (10). Constants may depend on the profile bounds, but not on delta or r in this range.

## 5. The power rate and its precise consequences

For radii satisfying (10), split the W integral into X_r(delta) and its complement. Boundedness of W and (9) give

    r^(-3) integral_{r<|y|<2r}|W|^2
                   <=C delta^2+C delta^(-6c)/r.       (11)

Put N'=4C1+16c+3 and delta=r^(-1/N'). Eventually delta<=min(1,L) and (10) holds because N'-N=12c+1>0. Also N'>6c+2, so the second term in (11) is at most C r^(-2/N'). Consequently W has mean-square bound C r^(-eta). Since |g|<=|W|+C/|y|, (2) and (SL) prove (MD). Small radii r>=4 are absorbed into C.

For every p in [1,infinity), boundedness of G and Holder's inequality give

    r^(-3) integral_{r<|y|<2r}|G|^p
           <=C_p r^(-eta min(1,p/2)).                (12)

A finite number of such annuli covers any fixed compact rescaled annulus. Thus G(r.) tends strongly to0 in every finite Lp on every compact subset of R3 minus{0}, for the entire family r->infinity. Any subsequential quadratic H-measure is zero: its defining compactly localized quadratic pairings are bounded by the local L2 norm squared and hence vanish. No converse or full-sequence conclusion is being inferred from the vanishing of one selected defect measure.

For the physical rotating self-similar field, put tau=T-t, r=tau^(-c), y=r exp(-omega J s)x with s=-log tau. The orthogonal factors preserve norms and annuli, and |grad_x u|=tau^(-1)|G(y)|. For 0<rho<1, (12) therefore gives

    ||grad_x u(t)||_{Lp(rho<|x|<1/rho)}
       <=C_{rho,p} tau^(-1+c eta min(1,p/2)/p).      (13)

The exponent added to -1 is positive for every finite p, so its integral over T-1<t<T is finite. The same statement holds for physical vorticity. This is integrability of the spatial Lp norm in time on fixed annuli, not an L-infinity continuation criterion.

For any fixed positive threshold, (SL), (MS) and (2) also give volume O(r^2) for high full-gradient or full-strain sets. The threshold constants may diverge as the threshold tends to0. Neither these estimates nor (13) exclude pointwise high-strain peaks. They do not prove bounded DU from bounded or decaying U and do not prove DU->0.

## 6. Verification and scope

The source was read in full and pinned in the team records. The independent proof above checks all characteristic completeness, exterior trapping, vorticity nonvanishing, rotation cancellation, Jacobian signs, finite-volume integration and delta-radius dependencies. The only source repair identified on this read is the unnecessary absolute-value inequality in Step1; replace it by lambda-1<=L. No computation is required or used. The configured-model author is asked through the existing file exchange to check this reconstruction and its explicit small-L treatment before the final verdict.

The statement is conditional on U AND DU bounded. It holds for every finite omega, all0<c<1, C2 velocity and C1 pressure, without decay, helicity, finite energy or pressure normalization. A485 is its analytic dependency. Pointwise derivative decay was open when this occupation argument was written; A492 subsequently resolved it under the stated bounded-gradient hypothesis. Arbitrary-sign nonexistence remains open.

## 7. Consequence of the later confirmed pointwise theorem

A492, followed by A476, gives |G(y)|<=C/(1+|y|) under exactly the principal hypotheses in Section1, for every finite omega and0<c<1. Consequently |W(y)|+|S_h(y)|<=C/(1+|y|), and direct integration gives

    integral_(r<|y|<2r) (|G|^2+|W|^2+|S_h|^2) <= C r, r>=1.

This implies SL, MS and MD, and also the newer C38 statement MD' with its weaker upper bound C r^2. For MS, the peak set is empty once r>C/delta; below that threshold its volume is at most C r^3<=C_delta r^2. Since eta=2/(4C1+16c+3)<2, the normalized C/r^2 bound also implies MD. The finite-Lp and physical time-integrability consequences follow directly from the pointwise estimate, with the stronger decay r^-1 in every such Lp norm. Their constants may depend on the fixed annulus and p.

This is a noncircular consequence of the already independently confirmed A492 and A476. It does not certify the source's separate kinematic counterexample, and does not infer bounded DU from U tending to0. The occupation argument above does not itself establish the pointwise theorem; its historical limitations should not be mistaken for an unresolved bounded-gradient gap after A492.
