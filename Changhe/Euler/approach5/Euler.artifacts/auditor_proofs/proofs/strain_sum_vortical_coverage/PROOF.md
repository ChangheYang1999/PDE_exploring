# A sharper finite-regularity criterion from the retained branch count

Date: 2026-11-03T01:37:05Z. CONFIRMED A373 after independent reconstruction, a focused configured-model review and the literature agent's review. The configuration of the existing coordinator agent is the primary model; provider identity is not independently attested. No separate model client was used.

## 1. Exact theorem and notation

Let r>=3 be an integer, 0<c<1/2 and omega any finite real number. Let U in C^r(R3;R3) and P in C1(R3) solve

    (1-c)U+((cI-omega J)y+U).grad U+omega JU+grad P=0,
    div U=0,             Jy=(-y2,y1,0),

and assume uniform sublinearity |U(y)|/|y|->0. Put B=(cI-omega J)y+U, W=curl U, a=1-2c, kappa=1+c and Psi_t=Phi_-t, where Phi is the complete B flow.

Choose R2>R1>0, b0>0 and a smooth radial cutoff rho equal to one near Q={|y|<=R1}, positive for |y|<R2 and zero for |y|>=R2, with (cy+U).y>=b0|y|2 for |y|>=R1. Define

    Y=-rho(cy+U), X=omega Jy+Y, S(y)=sym DY(y),
    Lplus=max(0,sup_y lambda_max(S(y))),
    Lminus=max(0,sup_y -lambda_min(S(y))),
    Sigma=Lplus+Lminus, L=sup_y ||S(y)||_operator.

All these constants are finite. If

    (r-1)(1-2c)>Sigma,                                      (1)

then almost every point of O={W!=0} lies in the continuous-time basin of one of countably many compactly supported full-flow-ergodic probabilities nu_i of Psi. Each satisfies

    nu_i(B!=0,W!=0)=1,
    spectrum(Psi,nu_i)=(a,0,-kappa),
    h_(nu_i)(Psi_1)=a,

and has absolutely continuous conditional probabilities on its one-dimensional full unstable plaques. Each basin has positive volume and lies in O. There are pairwise disjoint invariant open essential domains D_i with Bas(nu_i) subset D_i subset O, nu_i(D_i)=1, and Leb(D_i minus Bas(nu_i))=0. Their union covers O modulo a null set, and they are invariant under the complete B and W flows. If U is nonconstant, the family is nonempty.

Since Sigma<=2L, the simpler condition (r-1)(1-2c)>2L also suffices. No explicit omega term enters these strain constants, but the constants depend on the actual profile and the cutoff. For a nonconstant uniformly sublinear profile, Lplus>=a and Lminus>=kappa, hence Sigma>=2-c. Condition(1) therefore gives no C2 theorem. A support may meet either zero set; neither regular support nor a helicity sign is concluded.

This is a refinement of A312. The proof below supplies the sharper count and time selection; the complete unchanged capture argument is in A312, Sections2-5, with A305, A306, A307 and A308.

## 2. Sharper finite-time geometric count

Let g be the C^r diffeomorphism in A305, r>=3, and put

    Dplus=||Dg||infinity, Dminus=||Dg^-1||infinity,
    R=Dplus Dminus>=1.

Choose epsilon with epsilon^(j-1)||D^j g||<=Dplus for 2<=j<=r. The A305 tree can be chosen so that the number of small children is at most

    C_r R^(1/(r-1))(1+log R),                              (2)

where C_r depends only on r. All other conclusions of A305, including the individual large-length lower bound, affine slopes at most1/100, distortion below2, and finite-iterate compactness, remain unchanged.

Here is the exact count. The input curve has the A305 normalization: s=max|gamma'|<=epsilon, min|gamma'|>=s/D, and each derivative through r has norm bounded by a fixed normalization constant times s. Here eta=1/100 and D=50/49. For F=g composed gamma the chain rule and the chosen rescaling give

    ||F^(r)||<=A_r Dplus s,
    min|F'|>=s/(D Dminus),
    max|F'|<=Dplus s.

Consequently both the highest-derivative-to-minimum-speed ratio and the maximum-to-minimum-speed ratio are bounded by constants depending only on r times R. Divide the parameter interval into N equal parts with

    N=ceil((D A_r R/delta_r)^(1/(r-1))).

Since R>=1, N<=C_r R^(1/(r-1)). On each normalized part F_j, its highest derivative is at most delta_r times min|F_j'|. The Taylor polynomial P_j of F_j' has degree r-2 and uniform vector error at most delta_r min|F_j'|/(r-1)!.

Partition at roots of |P_j|2 minus squared dyadic thresholds between one half of min|F_j'| and a fixed multiple of R min|F_j'|. The number of thresholds is O_r(1+log R). Each polynomial has degree at most2(r-2); an identically zero polynomial adds no cuts. These partitions therefore contribute O_r(1+log R) pieces, each having speed ratio below4 after adding the Taylor error.

The vector Vandermonde interpolation argument of A305 bounds every derivative through r relative to the minimum speed on a normalized piece by a constant depending only on r. A fixed further division into K_r pieces, with K_r>=100, makes each bounded. This adds only an r-dependent factor. The total number of intermediate pieces is precisely bounded by (2).

Finally normalize speed. If an intermediate curve has maximum speed v>epsilon, split into ceil(v/epsilon) equal pieces. Every resulting output has maximum speed greater than epsilon/3, so all are large. Each uncut intermediate curve contributes at most one small output. Thus the potentially huge number of speed-normalization pieces does not enter the small-child count. This proves (2), with no dependence of C_r on g, its iterate length, its higher jets, the ambient dimension or epsilon.

## 3. Derivative estimates with separate strain bounds

For X=omega Jy+Y, the variational identity is

    d|v_t|2/dt=2 v_t.S(Theta_t y)v_t.

Hence for t>=0,

    ||DTheta_t||<=exp(Lplus t),
    ||DTheta_-t||<=exp(Lminus t).

The forward estimate uses lambda_max S, and the inverse estimate uses lambda_max(-S). These are separate estimates, not a claim about one orbit simultaneously achieving both extrema. For g=Theta_p,

    R_g<=exp(p Sigma).

Apply (2) to g. Since x^(1/(r-1))(1+log x) is increasing for x>=1,

    log A_g<=log C_r+p Sigma/(r-1)+log(1+p Sigma).           (3)

This logarithmic factor is why the convenient exponent3 in A305 should not be retained when deriving an asymptotic regularity threshold.

## 4. Fixed-r time selection

If the vortical set is empty, there is nothing to construct. Otherwise A312's covector law gives the full tangent upper exponent a=1-2c on a positive-length subset of each selected original target, and a<=Lplus. Under (1), choose

    Sigma/(r-1)<chi<chi'<a.

For g=Theta_p use

    h=p chi+2, alpha=p chi'-1, L_word=p Lplus,
    q=ceil(p Sigma)+4,
    theta0=(chi'-chi)/(2Lplus), beta=theta0/2.

The logarithms of tangent derivative ratios lie between -p Lminus and p Lplus. Their integer parts therefore occupy at most ceil(p Sigma)+2 bins, so q is a safe bound. For large p, 1<h<alpha<=L_word and theta=(alpha-h)/(L_word-h)>=theta0. Equation(3) gives

    h-log A_g >= p(chi-Sigma/(r-1))+2-log C_r-log(1+p Sigma).

The right side grows linearly with a positive leading coefficient. Therefore choose p so that its product with theta0-beta exceeds log(32q)+1. A306's finite-time bad-set estimate is at most2exp(-n).

Only after fixing p choose epsilon for the r jets of g and construct the original interval tree. Its later target-density restriction and the Borel-Cantelli selection are exactly those in A312. All A307 invariant-curve and A308 capture steps are unchanged. This proves the stated theorem: count(2), fixed-r time selection and the unchanged capture proof supply every required step.

## 5. Necessary size of the constants

For a nonconstant uniformly sublinear profile, W is nonzero somewhere. Its compact backward orbit and the inverse bound give

    exp(-Lminus t)|W(x)| <= |D Psi_t W(x)| <= M exp(-kappa t),

so Lminus>=kappa. Since curl(B cross W)=aW, the set B cross W!=0 has positive volume when W is nonzero. The covector transport at one such point gives ||D Psi_t||>=C exp(a t), hence Lplus>=a. Therefore Sigma>=a+kappa=2-c.

These are implications for the chosen cutoff's constants. They do not bound the strain above, nor prove exclusion when condition(1) fails. For primary c>2/5 the resulting lower bound on r grows without bound as c approaches1/2.

## 6. Verification and remaining scope

The only new ingredient beyond A312 is replacing M2 by Dplus Dminus in the already explicit A305 count, and retaining its logarithmic factor. The key review target is independence of C_r from p. Higher derivatives of the iterate influence epsilon only; the chain-rule rescaling absorbs them before the count. The second target is the separate forward/inverse strain estimate and its use in the derivative-bin range. The third is the strict parameter order, with fixed r then p then epsilon and only then the density subset.

This refinement proves a weaker sufficient premise for coverage. It proves no C2 coverage, regular-attractor coverage, helicity sign or nonexistence. The focused coordinator review independently checked the count, its constants and the strict parameter order; its precision items are incorporated above. In particular, the necessary lower bound implies r>=10 at c=2/5 and r>=17 at c=0.45. These are limitations of this sufficient criterion, not regularity obstructions for arbitrary profiles. Input snapshots and hashes are in verification. No numerical computation, server, external model client or formal build was used.
