# Repeated audit of the smooth-profile energy theorem

Status: repeated independent audit CONFIRMED at A2619-A2621 after all six sections were postread; the unrestricted extrapolation remains OPEN at A2622. This document covers the C1 theorem and the critical refinement, not the weak-profile extensions or all endpoint corollaries.

## 1. Statement, hypotheses and scope

Let 0<c<1 and omega be any finite real number. Put J(y1,y2,y3)=(-y2,y1,0), A=cI-omega J and B(y)=Ay+U(y). Suppose U is C1 on R3, P is C1 on R3, and

    (1-c)U+(B.grad)U+omega JU+grad P=0, div U=0.       (1)

Assume M=sup|U|<infinity and U(R.) tends to zero in distributions as R tends to infinity. Uniform decay of U implies these assumptions. Set

    E(R)=integral_{|y|<R}|U|^2,
    alpha=5-2/c, g(R)=R^(-alpha)E(R).

Then:

(a) If c<2/5, U=0 and P is constant.
(b) If c=2/5, U is in L2 and its exterior energy T(R) is O(R^(-5)).
(c) If c>2/5, there is L>=0 with |g(R)-L|<=C/R for R>=2; L>0 unless U=0.
(d) In (c), if epsilon(R)=sup_{|y|>=R}|U(y)| tends to zero, then

    |g(R)-L|<=C[epsilon(R/2)/R+R^((alpha-5)/2)].       (2)

The constants can be chosen using only c, M and E(4), independently of omega. In the target range 2/5<c<1/2, these are necessary energy asymptotics, not the requested unrestricted nonexistence theorem. In particular the possibility L>0 is not excluded. Part (b) also does not assert U=0.

No integrability, decay of derivatives, pressure normalization, pressure growth, or characteristic completeness is an extra premise. All integrations below have their boundary terms specified. Standard Fourier L2 calculus and the local regularity and mean-value property of harmonic distributions are the only analytic background facts used.

## 2. Local energy and canonical pressure gradient

Write q=|U|^2/2. Taking the dot product of (1) with U and using div B=3c and U.JU=0 gives

    (1-5c/2)|U|^2+div(qB+PU)=0.                     (3)

The divergence theorem on a finite ball is valid for C1 fields. Since (Jy).y=0, and the integral of U.n over every sphere is zero, for any constant p

    (cR/2)E'(R)+(1-5c/2)E(R)
        =-integral_{|y|=R}(q+P-p)U.n.                (4)

Consequently for 0<R1<R2,

    g(R2)-g(R1)
      =-(2/c) integral_{R1<|y|<R2}
           |y|^(-1-alpha)(q+P-p)U.(y/|y|).          (5)

The constant p may be chosen separately for each annulus. There is no pressure boundary term at infinity in this identity.

For the pressure argument define T_ij by its Fourier multiplier -xi_i xi_j/|xi|^2, and K_ij(y)=(3y_i y_j-delta_ij|y|^2)/(4pi|y|^5) off zero. For every compactly supported smooth test phi, T_ij partial_k phi belongs to L1: L2 boundedness treats a fixed ball and integration by parts in the kernel gives O(|y|^(-4)) outside twice the support radius. Thus the bounded tensor F_ij=U_i U_j defines

    <G_k,phi>=-sum_ij integral F_ij T_ij partial_k phi.   (6)

Taking divergence in (1) gives -Delta P=partial_i partial_j F_ij. The two rotation terms cancel in this operation. Fourier multiplication shows that h_k=partial_k P-G_k is a harmonic distribution and hence a smooth harmonic function. This step does not require P to be tempered.

It remains to rule out an arbitrary harmonic remainder, not merely a constant one. Write U_R(z)=U(Rz). Testing the rescaled equation gives

    <(partial_k P)(R.),psi>
      =integral U_R.Lambda_k psi
          +R^(-1)sum_j integral U_R,k U_R,j partial_j psi,
    Lambda_k psi=(4c-1)psi e_k-omega psi J^T e_k
                        +(Az.grad psi)e_k.          (7)

Meanwhile homogeneity of the multiplier in (6) gives

    <G_k(R.),psi>
        =-R^(-1)sum_ij integral F_ij(Rz)T_ij partial_k psi.  (8)

Here the pullback of a distribution under R. includes its usual R^(-3) testing factor. Fix x and a smooth radial test phi with integral one. The mean-value property gives

    h_k(x)=<h_k(R.),psi_R>, psi_R(z)=phi(z-x/R).      (9)

The two terms of order R^(-1) in (7)-(8) vanish uniformly for these translated tests, because their required L1 norms are translation invariant. The remaining integral vanishes as well. Indeed boundedness and distributional dilation decay imply integral U_R.psi tends to zero for every L1 test by density of compactly supported smooth tests. This remains true for tests converging in L1. In (7), Lambda_k psi_R tends to Lambda_k phi in L1. Hence h_k(x)=0 for every x, and

    grad P=G.                                       (10)

Although (7) contains omega, it is used only to identify the pressure, at each fixed finite omega. The quantitative pressure estimates following (10) contain no omega.

## 3. Annular pressure and flux bounds

For fixed R split F into its restrictions F1 to R/2<=|z|<4R, F2 to |z|<R/2, and F3 to |z|>=4R. Put Pi1=sum T_ij F1_ij, Pi2=sum T_ij F2_ij and

    Pi3(x)=integral_{|z|>=4R}
             sum_ij [K_ij(x-z)-K_ij(-z)]F_ij(z), |x|<2R.

The subtraction makes this integral absolutely convergent for bounded U. Its derivative is also absolutely convergent. Formula (10), self-adjointness of T_ij and the oddness of partial_k K_ij show that the gradient of P-Pi1-Pi2-Pi3 vanishes in the connected ball B(0,2R). Thus for some real p_R,

    P=p_R+Pi1+Pi2+Pi3 almost everywhere in that ball. (11)

On the annulus R<|x|<2R,

    ||Pi1||_2<=epsilon(R/2)E(4R)^(1/2),
    |Pi2(x)|<=C R^(-3)E(R/2),
    |Pi3(x)|<=C R I(R),
    I(R)=integral_{|z|>=4R}|z|^(-4)|U(z)|^2
          <=4 integral_{4R}^infinity r^(-5)E(r)dr.  (12)

The first bound follows from Plancherel and the Frobenius norm one of xi tensor xi/|xi|^2, followed by |F|^2=|U|^4. For the second, |x-z|>=R/2 and |K_ij(w)U_i U_j| summed over i,j is bounded by C|w|^(-3)|U|^2. For the third, the mean-value theorem gives a bound C|x||z|^(-4)|U|^2 on the subtracted integrand. The last bound is integration by parts in integral r^(-4)E'(r)dr. Its outer boundary is zero since E(r)<=CM^2r^3; its inner boundary is negative and is discarded. No sign of the pressure is used.

Let Phi(R)=integral_{R<|y|<2R}|q+P-p_R||U|. Cauchy-Schwarz, (11)-(12), and the annulus volume give

    Phi(R)<=C[epsilon(R)E(2R)+epsilon(R/2)E(4R)
             +R^(3/2)E(2R)^(1/2)
                     {R^(-3)E(R/2)+R I(R)}].         (13)

If E(r)<=K r^mu for all r>=1 and 0<=mu<=3, then for R>=2,

    I(R)<=C K R^(mu-4),
    Phi(R)<=C(MK+K^(3/2))R^mu.                       (14)

Indeed the pressure terms initially have exponent (3mu-3)/2, no larger than mu in this range. The denominator 4-mu is at least one. All constants in (12)-(14) can therefore be taken independent of mu in [0,3], apart from the displayed K.

## 4. Dyadic bootstrap and all three parameter regimes

Combining (5) and (14), any R<=R1<R2<=2R satisfies

    |g(R2)-g(R1)|<=C R^beta, beta=mu-1-alpha.        (15)

For beta>0, summing backwards from R to a radius in [2,4) yields E(R)<=C R^(mu-1). For beta=0, the number of annuli is O(1+log R), so E(R)<=C R^(mu-1)(1+log R). For beta<0, summing forwards yields a Cauchy estimate for g at all real radii and

    L=lim g(R), |g(R)-L|<=C R^beta.                 (16)

The initial segment [1,2] can always be included using E(2). Backward sums depend on the base values of g on [2,4], bounded in terms of c and E(4). Start from E(r)<=CM^2r^3.

If alpha<0, the first three backward steps give exponents 3,2,1,0. With mu=0, beta=-1-alpha. If beta>0 or beta=0 the next estimate is respectively O(R^(-1)) or O(R^(-1)(1+log R)); if beta<0 then g has a finite limit and E(R)=R^alpha g(R) tends to zero. In every case nonnegative monotonicity of E forces E=0. This proves (a).

If 0<alpha<3, lower mu by one as long as mu-1>alpha. If equality occurs, absorb the logarithm into R^(1/4), using the new exponent mu-3/4=alpha+1/4. Thus eventually mu-1<alpha, with mu in [alpha,3]. Formula (16) gives a finite nonnegative L. Boundedness of g then supplies E(r)<=K r^alpha. Applying (16) again with mu=alpha gives |g-L|<=C/R.

If this L is zero, E(R)<=C R^(alpha-1). While alpha-j>=0, (16) with mu=alpha-j gives E(R)<=C R^(alpha-j-1), since the same limit of g is zero. After finitely many steps the exponent is negative. Monotonicity of E again gives U=0. This proves (c).

Under uniform decay, (13) with mu=alpha improves the annular increment to

    C[epsilon(R/2)R^(-1)+R^((alpha-5)/2)].

Its forward geometric sum proves (2). Both terms are o(R^(-1)) since epsilon tends to zero and alpha<3. This proves (d).

If alpha=0, the exponents descend 3,2,1 and then give E(R)<=C(1+log R). Bound this by CR^(1/4) and apply (16) to deduce finite total energy. The bound with mu=0 then gives exterior energy O(R^(-1)). The sharper estimate is proved next.

## 5. Critical exterior energy and its limit

Now c=2/5 and T(R)=integral_{|y|>R}|U|^2 tends to zero. Revisit (13) before replacing annular integrals by E. The cubic and Pi1 terms are at most C M T(R/2). The Pi2 term is at most C R^(-3/2)||U||_2^2 T(R)^(1/2). For Pi3 use

    R I(R)<=R(4R)^(-4)T(4R)<=C R^(-3)||U||_2^2.

Therefore

    Phi(R)<=C[T(R/2)+R^(-3/2)T(R)^(1/2)].            (17)

At alpha=0, sum the finite-annulus identity (5) over radii R,2R,4R,... and pass to infinity. The absolute sum is bounded by (17), because T is nonincreasing and the factors R^(-1) and R^(-5/2) sum geometrically. This explicitly justifies the signed exterior energy identity and yields

    T(R)<=C R^(-1)T(R/2)+C R^(-5/2)T(R)^(1/2).     (18)

Starting even from T(R)=O(1), if T(R)=O(R^(-tau)), (18) gives the new exponent min(tau+1,(5+tau)/2). Four steps reach tau=4. The first term of (18) is then O(R^(-5)); Young's inequality bounds the second by T(R)/2+CR^(-5). Absorption proves T(R)=O(R^(-5)), completing (b).

This estimate contains no conclusion that T vanishes at finite R, and does not prove critical nonexistence. For c>2/5 the energy growth L R^alpha likewise need not vanish merely because U decays. No step of this proof estimates DU or uses characteristic flow. Thus derivative-decay and global dynamical conclusions require their own arguments and are outside this audit.

## 6. Sources and repeated-audit finding

The source is Section 2.0-2.5 of the current coordinator report, with Proposition 2.7. Its complete statements, energy identity, pressure proof, annular estimates, dyadic proof and critical refinement were read this shift. Endpoint corollaries and the embedded weak theorem are not covered by this reconstruction. The source's explicit pressure constants 4/pi and 192/pi were also checked from its displayed kernel bounds; the theorem here only needs absolute constants.

The source is the existing configured model theory/coordinator work. This reconstruction supplies the independent check. Runtime provider identity is not independently attested. No new model call, numerical experiment or formal build was used. The pressure normalization, all limits and boundary terms, the parameter cases and arbitrary finite omega show no mathematical gap at the stated scope. The unrestricted target conjecture remains open.
