# Derivative residual bounds on the two infinite end regions

Written 2026-10-21T23:35:09.504881+00:00 before the new computation. All conclusions here concern the exact normalized finite modal trial, not the original X3 ansatz. Numerical application remains OPEN until the declared checks, actual second-model review and later independent adjudication are complete.

## Statement and inherited data

Let rho be the exact normalized trial of modal_repair/PROOF.md with the exact data in data_exact/modal_v2.json. Set k=1615536043799051/9007199254740992, L=8614738245908811/1125899906842624, c_l=1/k and c=3/k-1. Use the canonical full-plane velocity U=(-psi_y,psi_x), -Delta psi=rho_x, and eps=(c_l X+U).grad rho-rho. Put t=log r and

    a=-685794559684773/140737488355328,
    b=2289893859708677/281474976710656,
    alpha=a-5, beta=b+17, R_i=exp(alpha), R_o=exp(beta),
    w(r)=L^6 r^(-6)(1+r^2/L^2)^(3/2-k).

For a radial region A, define

    ||f||_X(A)^2=integral_A [f^2+r^2|grad f|^2]w(r) dX.

The finite angular expansions of eps and each t derivative have odd frequencies at most Omega=1043. Density frequencies are at most nu=521; stream frequencies are at most M=522. All angular norms below are Fourier coefficient l1 sums, hence are submultiplicative. The full-circle sine/cosine L2 identity has factor pi, not 2pi.

Inherit the accepted inner_majorant and outer_majorant results, their proof and actual output audits, and their exact density data. Their canonical archive premise for the actual normalization parameter is discharged by canonical_residual_composition. Inherit modal_annular_regularity for the C5 residual on the punctured plane, including exact spline joins. No numerical majorant is differentiated merely because it bounds a function.

This proof gives explicit computable upper bounds for eps and eps-eps_t on r<=R_i and r>=R_o. It does not bound their norms on alpha<t<beta. Under the remaining physical W hypotheses of coherent_derivative_norm_composition, the squared end bounds may be added to its squared annular bounds. Those W hypotheses remain OPEN.

## Exact inner density derivatives

On t=a+tau, tau<=0, write rho=rho_0+eta, rho_0=x^2 y. The accepted exact data give

    eta_j(r)=r^3 sum_(lambda,l) c_(j,lambda,l) exp(lambda tau) tau^l.

There are 262 slots, the last zero. The seven polynomial core rates are lambda=2,4,...,14 with l=0; the correction rate is b_i=3518437208883275/70368744177664 with l<=6. All coefficients are exact rationals. The cubic coefficients of rho_0 are exactly1/4 at sine frequencies1 and3 and zero elsewhere.

For p=0,...,3 set

    c^[p]_(j,lambda,l)
      =sum_(q=0)^p binom(p,q)(3+lambda)^(p-q)
          (l+q)!/l! c_(j,lambda,l+q),
    d_p=exp(-2a) sum_(j,lambda,l)
          |c^[p]_(j,lambda,l)| 5^l exp(-5(lambda-2)).

Missing polynomial coefficients are zero. The formula follows by applying (D_tau+3+lambda)^p to each polynomial before its exponential factor. For lambda>2, x^l exp(-(lambda-2)x) is decreasing on x>=5 provided 5(lambda-2)>=l. That exact inequality is checked for all present degrees. At lambda=2 only l=0 occurs. Therefore, on r<=R_i,

    ||D_t^p eta||_W <= d_p r^5, 0<=p<=3,
    ||D_theta D_t^p eta||_W <= nu d_p r^5.

The angular factor is a finite degree bound. The derivative formula is checked independently by repeated polynomial differentiation plus multiplication by3+lambda.

## Inner velocity derivatives from the Green equations

The accepted inner result at cutoff T=0 gives constants C_r,C_theta such that the remainder after the exact strain satisfies

    ||U_rem,r/r||_W<=C_r r^2,
    ||U_rem,theta/r||_W<=C_theta r^2

throughout r<=exp(a). Here U_rem=U-(-cx,cy). In the computation use the exact rational upper endpoints of its accepted C_r,C_theta intervals. This explicitly inherited bound is also valid on the smaller disk r<=R_i.

For stream mode m=2n define A_n,B_n by the canonical Green integrals and P_n=(A_n+B_n)/(2r^2), Q_n=(B_n-A_n)/(2r^2). Then

    P'_n=-2P_n+mQ_n, Q'_n=mP_n-2Q_n-f_n,
    partial_x rho=sum_n f_n(r)sin(2n theta).

Both identities follow by differentiating A'=-m A+r^2 f and B'=m B-r^2 f, with primes denoting D_t. The strain is P_1=Q_1=c and contributes zero to both homogeneous right sides. Subtract it before using these identities. The actual velocity factors are -P_n and Q_n, so absolute-value bounds retain the displayed signs only in the derivation.

Polar differentiation and collection of the two neighboring density modes imply

    sum_n |f_n-r^2 delta_(n1)| <= r^4(d_1+nu d_0),
    sum_n |f'_n-2r^2 delta_(n1)|
        <=r^4[d_2+(nu+1)d_1+nu d_0].

Indeed each density mode enters at most two neighboring source modes with coefficient1/2. For the differentiated estimate apply D_t-1 to (D_t plus or minus its angular frequency)eta_j, because partial_x contains r^(-1). The triangle inequality gives the stated three terms; no derivative bound of an already bounded remainder is assumed.

Put

    F_0=1+R_i^2(d_1+nu d_0),
    F_1=2+R_i^2[d_2+(nu+1)d_1+nu d_0],
    s_0=C_r, q_0=C_theta,
    s_1=2s_0+M q_0, q_1=M s_0+2q_0+F_0,
    s_2=2s_1+M q_1, q_2=M s_1+2q_1+F_1.

The ODE identities and m<=M prove ||D_t^p(U_rem,r/r)||_W<=s_p r^2 and ||D_t^p(U_rem,theta/r)||_W<=q_p r^2 for p=0,1,2. These are bounds for actual derivatives, obtained by substitution in the ODE, not by differentiating s_0 r^2.

## Inner residual and norm bounds

Exact normalization gives (c_l X+U_lin).grad rho_0-rho_0=0. Thus eps is the sum of the linear action on eta, U_rem.grad rho_0, and U_rem.grad eta. Applying Leibniz's rule p times yields, for p=0,1,2,

    ||D_t^p eps||_W <= B_p r^5,
    B_p=|c_l|d_(p+1)+d_p+|c|(d_(p+1)+nu d_p)
        +sum_(l=0)^p binom(p,l)3^(p-l)[(3/2)s_l+q_l]
        +R_i^2 sum_(l=0)^p binom(p,l)
             [s_l d_(p-l+1)+q_l nu d_(p-l)].

Here ||D_t rho_0||_W=(3/2)r^3, ||D_theta rho_0||_W=r^3 and subsequent t derivatives multiply by3. The coefficient c is constant, as are c_l and the strain Fourier factors. This accounts for every differentiated product.

Let

    C_i=pi L^6(1+R_i^2/L^2)^(3/2-k) R_i^6/6,
    I_0^2=C_i[(1+Omega^2)B_0^2+B_1^2],
    I_1^2=C_i[(1+Omega^2)(B_0+B_1)^2+(B_1+B_2)^2].

Because r^2|grad f|^2=f_t^2+f_theta^2, Parseval and the l1 bound give

    ||eps||_X(r<=R_i)<=I_0,
    ||eps-eps_t||_X(r<=R_i)<=I_1.

The radial integral is integral_0^R_i r^(10)r^(-6)r dr=R_i^6/6. The remaining weight factor is increasing since3/2-k>0. The derivative bounds imply these functions extend continuously with their first derivatives at0; no point-supported weak derivative is introduced. More explicitly eps and eps-eps_t are O(r^5), their classical gradients are O(r^4), and integration by parts across a circle of radius delta has boundary term O(delta^6), tending to zero.

## The precise coefficient meaning of the outer majorant

The accepted exterior construction gives a finite exact vector expansion

    eps_N(t)=sum_(gamma,l) e_(N,gamma,l) tau^l exp(gamma tau),
    tau=t-b>=0, gamma<=2k-1<0, l<=12.

Its saved positive coefficients C_(gamma,l) satisfy the stronger coefficient statement

    sum_N |e_(N,gamma,l)|<=C_(gamma,l).

This assertion must be verified from the inherited construction before application. Its proof is as follows. The exact Green particular and transient formulas and exact density formulas are exponential polynomials. The linear residual coefficient is collected before its absolute value. The leading linear coefficient vanishes exactly because c_l k=1. Each nonlinear term is a product of two finite angular polynomials and two finite radial polynomials. For a fixed radial monomial the angular l1 product bound gives the convolution of the absolute coefficient sums. Summing the positive convolutions and combining equal exact exponents is precisely the construction of C. No radial maximum has yet been taken at this stage. Negative angular frequencies are folded with their signs before any cancellation is discarded; discarding cancellation only enlarges C. There are1864 exact exponents and3508 stored monomial slots. The new audit must read the saved constituent P,Q,D,E,L arrays and all261 transient terms, reconstruct all2992 product blocks plus10 nonleading linear blocks, and verify the resulting whole coefficient interval comparisons with every saved C. Both saved construction and independently reassembled upper coefficient sums may be used; their larger upper endpoint remains safe.

For p=0,1,2 define nonnegative derivative coefficients

    C^[p]_(gamma,l)=sum_(q=0)^p binom(p,q)|gamma|^(p-q)
                     (l+q)!/l! C_(gamma,l+q).

Termwise differentiation of the finite exact residual expansion and the triangle inequality prove

    ||D_t^p eps(t)||_W <=sum_(gamma,l) C^[p]_(gamma,l) tau^l exp(gamma tau).

This uses coefficient bounds, not the derivative of a pointwise majorant. It is independently checked by applying the positive recurrence P -> P'+|gamma|P p times.

## Outer weighted integral bounds

Set T=17 and

    C_o=L^(3+2k) exp(-(1+2k)b)
          (1+L^2 exp(-2beta))^(3/2-k).

For t=b+tau, tau>=T, the exact weight obeys

    exp(2t)w(exp(t))<=C_o exp(-(1+2k)tau).

This follows by factoring (r/L)^(3-2k) from (1+r^2/L^2)^(3/2-k); the remaining factor decreases in t. For a>0 and integer n>=0, repeated integration by parts gives

    J_n(a,T)=integral_T^infinity tau^n exp(-a tau)d tau
       =exp(-aT) sum_(j=0)^n n!/(n-j)! T^(n-j)/a^(j+1).

An independent evaluation uses J_0=exp(-aT)/a and J_n=exp(-aT)T^n/a+(n/a)J_(n-1). Boundary terms vanish by exponential decay. Every a_gamma=1+2k-2gamma is strictly positive, as checked exactly for all1864 exponents.

Minkowski's inequality applied to a finite sum gives

    L_p=sum_(gamma,l) C^[p]_(gamma,l) sqrt(C_o J_(2l)(a_gamma,T)),
    O_0^2=pi[(1+Omega^2)L_0^2+L_1^2],
    O_1^2=pi[(1+Omega^2)(L_0+L_1)^2+(L_1+L_2)^2].

Thus ||eps||_X(r>=R_o)<=O_0 and ||eps-eps_t||_X(r>=R_o)<=O_1. Each L_p bounds the weighted radial L2 norm of the corresponding Fourier-Wiener sum. The angular derivative is bounded by Omega times that sum. The inequalities establish finite end norms without a finite radial truncation.

## Conditional full-plane composition

If all physical W hypotheses of the accepted coherent annulus theorem hold for this same canonical trial, its regularity hypothesis follows from the accepted exact annular regularity theorem. The two interface circles have measure zero and the actual functions have continuous derivatives across them. Additivity of the squared norm then yields

    ||eps||_X(R^2)^2 < (0.385656)^2+I_0^2+O_0^2,
    ||eps-eps_t||_X(R^2)^2 < (585.874)^2+I_1^2+O_1^2.

These remain conditional bounds until the physical W hypotheses are independently verified on all19389 true cells. Any terminating decimal displayed after computation is a strictly upward rational ceiling checked against both independent interval endpoints. No numerator norm, inverse bound, nonlinear closing estimate, original X3 distance, existence or exclusion follows.

## Required independent application

Read and rehash the complete accepted parent pin maps. Check all exact density slots, rates and cubic coefficients. Recompute all inner differentiated coefficients using Fraction and independent fmpq polynomial recursion. Use Arb512 for one complete positive calculation and mpmath.iv200 for the other. The second outer scalar integral uses the integration-by-parts recurrence, not the first finite factorial sum. Read every saved outer coefficient and independently reconstruct its constituent lineage; merely observing matching final counts is insufficient. Retain exact output intervals, full coverage counts, source freezes, actual model metadata and response. Do not accept a failed enclosure or inflate an old target. New bounds may honestly be coarse. Only after substantive actual Claude Opus5.5 review and a later own adjudication may the finite application be marked CONFIRMED. The annular W condition and IPM endpoint stay OPEN.
