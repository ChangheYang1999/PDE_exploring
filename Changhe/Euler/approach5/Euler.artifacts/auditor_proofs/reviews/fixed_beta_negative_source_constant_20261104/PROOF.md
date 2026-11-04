# Exact modal negative-source constant at a fixed exponent

Status: independent reconstruction, reconciled with the existing Theory Agent C  comparison. This proves a modal optimum and a conditional logarithmic estimate, not the optimum of the latter.

## 1. Statement and scope

Let U be a real C1 divergence-free vector field on R3. Suppose 0<beta<1, L>0 and E(R)=integral_(B_R)|U|^2 satisfies E(R)/(L R^beta)->1. Define

    t=(beta-3)/2, k=(beta+1)/2=t+2, m=2-beta,
    D=k^2+2, H=t^2(k^2+4)/D, C_s=mt^2/D,
    b_2=D/2+2beta/D,
    c_1=(2b_2+t^2)/(2m b_2), C_beta=max(1,c_1).

For a fixed center a put r=|y-a|, q=tr((DU)^2), Q_a(r)=integral_S2 q(a+rn)dn, with sphere area4pi, and

    F_a(R)=integral_(1<r<R) r^(-beta)|U|^2,
    G_a(R)=integral_(1<r<R) r^(2-beta)|DU|_F^2,
    K_a^-(R)=integral_1^R r^(4-beta)[-Q_a(r)]_+ dr,
    J_a(R)=integral_1^R r^(4-beta)[Q_a(r)]_+ dr.

Assume M=limsup G_a(R)/(beta L log R)<infinity. Then the same M is obtained at any other fixed center, M>=H, and, with delta=M-H,

    limsup K_a^-/(beta L log R)<=min(M,C_beta delta),
    limsup J_a/(beta L log R)
       <=min(M,m[1-beta+beta u(M)]+C_beta delta),
    u(M)=min(1,k^2/D+delta/(2beta)).                    (1)

In particular the last bound is at most C_s+(m/2+C_beta)delta. The constant C_beta is exactly the least constant in the modal quadratic comparison used below. The least possible constant in the global logarithmic estimate is not determined.

The reviewed source is LIT396, SHA256 bea4d5bd40d42aa1abc7a5eb9d2a0069f3a2de8b6df3bd2ccc41f29736ad7600, seven sections and fifty manual obligations. Dependencies are the full harmonic/compact-cutoff framework of LIT391/A3186, the upper tangential-energy bound A3153 and, only for the Euler application, A3053. None of LIT394's construction or numerical optimization is a premise.

## 2. Full harmonic representation and nonnegative defect

For the kinematic calculation translate a to zero, set z=log r and U(rn)=r^t v(z,n). The divergence equation is (partial_z+k)(v.n)+div_S v_T=0. The radial degree-zero mode is zero by flux through balls. For a real orthonormal spherical harmonic Y of degree ell>=1, lambda=ell(ell+1), the poloidal and toroidal modes are

    fY n+(f'+kf)grad_S Y/lambda,
    h n cross grad_S Y.

Although U is only C1, the radial divergence relation makes f C2. Their velocity and Cartesian-gradient sphere densities are

    K_p=f^2+(f'+kf)^2/lambda,
    D_p=2(f'+tf)^2+[f''+(k+t)f'+tkf]^2/lambda
         +(lambda-2)f^2,
    K_t=lambda h^2, D_t=lambda[(h'+th)^2+lambda h^2].

Distinct harmonics and the two types are orthogonal in these sphere integrals. After integration by parts in z, the defect D-HK has nonnegative density

    Z_p=f''^2/lambda+b_lambda f'^2+d_lambda f^2,
    b_lambda=2+(k^2+t^2-H)/lambda,
    d_lambda=(t^2-H)(1+k^2/lambda)+lambda+t^2-2,
    Z_t=lambda[h'^2+(t^2+lambda-H)h^2].                (2)

Here b_lambda>=1, d_2=0, b_2=D/2+2beta/D>=9/8, d_lambda>=4lambda/9 for lambda>=6, and t^2+lambda-H>0. For example t^2-H=-2t^2/D lies in(-2,0), and d_lambda>=lambda-3-2/lambda>=4lambda/9 for lambda>=6. The toroidal minimum is t^2+2-H=4beta/D>0.

For a nonnegative smooth compact logarithmic cutoff eta, the precise poloidal correction is

    integral eta(D_p-HK_p)=integral eta Z_p
      -(k+t)/lambda integral eta' f'^2
      -[2t+((k+t)tk-Hk)/lambda] integral eta' f^2
      +tk/lambda integral eta'' f^2.                  (3)

The toroidal correction is -t lambda integral eta' h^2. The errors summed over modes are at most A_beta integral (|eta'|+|eta''|)|v|^2. Uniformity follows from f'^2/lambda<=2(f'+kf)^2/lambda+2k^2f^2/lambda. Thus no angularly weighted derivative-strip bound is being inserted. Parseval gives local L2 convergence of the velocity and Cartesian gradients; nonnegative Z sums pass by monotone convergence. In particular the full defect satisfies

    integral eta Z=G_eta-HF_eta+O_beta(velocity strips). (4)

## 3. Sphere source and the exact degree-one optimum

Write A=integral_S2|v.n|^2 and K=integral_S2|v|^2. Distributional integration of q=div div(U tensor U) gives

    Q_flat=r^(5-beta)Q_0(r)
      =A''+(2beta-2)A'+beta(beta-2)A-K'-(beta-2)K.      (5)

For a poloidal jet p=f', w=f'', substituting A=f^2 and K=f^2+(p+kf)^2/lambda gives

    Q_p=s_lambda f^2+A_lambda fp+B_lambda fw
           +C_lambda p^2-2pw/lambda,
    s_lambda=m(1-beta+k^2/lambda),
    A_lambda=8k-10+(6k-6k^2)/lambda,
    B_lambda=2(1-k/lambda), C_lambda=2+(3-4k)/lambda.   (6)

For a toroidal mode Q_t=m lambda h^2-2lambda hh'. These identities use only first derivatives of the original velocity: for finite harmonics f is C2, and for the full field the source converges in L1 from local L2 convergence of DU and |tr(A^2)-tr(B^2)|<=|A-B|_F(|A|_F+|B|_F).

At lambda=2, completing f gives

    Q_p=(mt^2/2)[f+((5-3k)p-w)/(mt)]^2
          -(tp+w)^2/(2m),
    Z_p=b_2 p^2+w^2/2.                               (7)

The identity needed for this is 2m(7/2-2k)-(5-3k)^2=-t^2. Weighted Cauchy-Schwarz bounds (tp+w)^2 by (t^2/b_2+2)Z_p. Hence Q_p+c_1 Z_p>=0. The nonzero jet

    p=t/b_2, w=2, f=-((5-3k)p-w)/(mt)

attains equality and has Z_p>0. Therefore c_1 is the exact least degree-one constant at this fixed beta.

## 4. All higher degrees admit the constant one

For every real lambda>=6, completing w in (6)+(2) gives

    Q_p+Z_p=[w-p+(lambda-k)f]^2/lambda
               +P f^2+R fp+S p^2,
    P=s_lambda+d_lambda-(lambda-k)^2/lambda,
    R=A_lambda+B_lambda, S=C_lambda+b_lambda-1/lambda. (8)

Put x=1-k in(0,1/2), v_0=t^2k^2/D>0. Direct simplification yields

    P=4x^2+v_0+(2xk^2-2v_0)/lambda
        >=4x^2+(2/3)v_0>0,
    R=-8x+(4k-6k^2)/lambda,
    S=4+[2-4k+k^2-2t^2/D]/lambda>=7/2.

The bound for S uses 2-4k+k^2>=-1 and t^2/D<1. An exact determinant expansion is

    D^2 lambda^2(4PS-R^2)
       =P_2(k)(lambda-6)^2+P_1(x)(lambda-6)+P_0(x),
    P_2(k)=16k^2(k-2)^2D,
    P_1(x)=20x^8-96x^7+440x^6-1008x^5+1184x^4
             -384x^3-440x^2-304x+460,
    P_0(x)=8x^9+44x^8-304x^7+1376x^6-3552x^5
             +4680x^4-2960x^3-608x^2-488x+1036.       (9)

The first coefficient is positive. Dropping positive monomials and using x<=1/2 on each negative monomial proves

    P_1>=460-152-110-48-63/2-3/4=471/4,
    P_0>=1036-244-152-370-111-19/8=1253/8.

Thus 4PS-R^2>0 for every lambda>=6. With P>0 this proves Q_p+Z_p>=0 for every higher angular degree, without a truncation or sample grid. For the toroidal part,

    m h^2-2hh'=m(h-h'/m)^2-h'^2/m>=-h'^2,

since m>1, while Z_t>=lambda h'^2. Hence Q_t+Z_t>=0. Summing and passing by the L1 convergence above yields

    [-Q_flat]_+<=C_beta Z                              (10)

almost everywhere. The negative part here follows the sphere integral.

## 5. Modal sharpness and dependence on beta

Degree one forces every modal constant to be at least c_1. Higher degrees force it to be at least1: choose f=1,p=0,w=-lambda, for which

    Q_p=s_lambda-2lambda+2k,
    Z_p=lambda+d_lambda=2lambda+O_beta(1).

Their ratio -Q_p/Z_p tends to1 as lambda tends to infinity through ell(ell+1). Every finite jet is admissible: choose a smooth scalar coefficient with that Taylor jet on an annulus, zero near the origin and constant outside a larger annulus, then use the poloidal formula. The resulting whole-space C-infinity solenoidal field decays and has an energy ratio with a positive L fixed by the nonzero tail coefficient. The local jet is unaltered. This proves modal necessity; a localized annular jet does not establish logarithmic sharpness or solve Euler.

For b=beta,

    c_1=(2b^4+28b^2+64b+162)/[(2-b)(b^4+4b^3+22b^2+100b+81)].

The denominator is positive. Subtracting the denominator from the numerator gives b(b^4+4b^3+14b^2+84b-55). The quartic has positive derivative on[0,1] and values -55 and48 at its endpoints, so has exactly one root beta_1 in(0,1). Consequently C_beta=1 for beta<=beta_1 and C_beta=c_1 for beta>beta_1. Also

    16 denominator-13 numerator
      =2(1-b)(8b^4+37b^3+149b^2+779b+243)>0.

Therefore 1<=C_beta<16/13 and C_beta tends to16/13 as beta tends to1. The least constant uniform in beta remains16/13. No numerical location or sampled extremum is required.

## 6. Compact cutoffs, logarithmic limits and centers

Stieltjes integration gives F_0(R)=beta L log R+o(log R), and the energy-ratio assumption bounds velocity energy on every fixed-width far logarithmic strip. Choose eta_R between0 and1, equal to1 on[0,log R], supported in(-log2,log(2R)), with first two derivatives bounded independently of R. Its inner strip contributes a finite constant, and (4),(10) imply

    K_0^-(R)<=C_beta[G_0(2R)-HF_0(R)]+C(beta,U).

After division by beta L log R this gives C_beta(M-H). The same nonnegative-defect relation gives M>=H. Directly |q|<=|DU|_F^2 implies K_0^-<=G_0 and J_0<=G_0.

The signed radial-Hessian identity is

    integral eta_R Q_flat=m(1-beta)F_eta+m beta T_eta+O(1),

where T_eta is the weighted tangential velocity energy. A3153 applies with the same cutoffs and yields limsup T_eta/(beta L log R)<=u(M). Since [Q_flat]_+=Q_flat+[-Q_flat]_+, add this signed estimate to (10), using the cutoff which dominates the interval of interest. This proves the J bound in (1). The identity m(1-beta+beta k^2/D)=C_s then gives its linear version. There is no assumed bound on the outer gradient strip; G_0(2R) is retained until taking its limsup.

Ball inclusion transfers E(R)~LR^beta between fixed centers. Outside a sufficiently large fixed ball the two positive gradient weights have ratio arbitrarily close to1, and their cutoff radii differ by at most the distance between centers. Comparison in both directions proves equality of the normalized gradient limsups. The finite-core terms vanish after division by log R. Applying the kinematic proof at each center proves (1) there; no translation of Euler momentum is made.

## 7. Euler consequence, verification and limitations

By A3053, every nonzero bounded C1/C1 solution of the full rotating profile equation with distributional blow-down zero and 2/5<c<1/2 has the required energy ratio with beta=5-2/c and L>0. If it additionally has finite M, it obeys (1) at every center, for every finite omega and without symmetry. Uniform decay gives the boundedness and blow-down hypotheses but has not supplied finite M.

The local exact diagnostic in check_exact.py (accompanying artifacts) checks seventeen algebraic identities or negative controls, including the source independently derived from (5), determinant coefficients, equality jet and rational factorizations. All passed at the actual time recorded in the team records. These checks only guard transcription; the positivity, convergence, cutoff and sharpness arguments are the analytic proof above. The existing configured model C agent has compared the result; its actual provider execution is independently unattested.

The fixed-beta modal question left open in A3196 is resolved by this argument. The optimum of the global logarithmic coefficient, eventual nonnegativity of Q_a, a bound for the pointwise negative part before sphere integration, automatic finite M and the arbitrary-omega nonexistence conjecture remain unresolved. In particular M=H gives K_a^-=o(log R), not an eventual source sign.


## 8. Comparison and coefficient scopes

The complete seven-item C comparison of 11:32:49Z is retained in the team records. Its analytical checks agree with Sections 1-7. The additional Sturm calculation, sampled eigenvalues, sampled toroidal supremum and numerical root are not adopted as proof evidence. The elementary coefficient bounds in (9) prove the required positivity directly. In the compact-cutoff argument F_eta/(beta L log R) tends to one, so any negative coefficient of F_eta creates no sign ambiguity. Equivalently one can use F_eta>=F(R) for that negative coefficient.

The comparison's assertion about nonattainment when beta<beta_1 means a jet with positive defect and the extremal negative quotient. A zero jet trivially has equality and does not determine the least constant. The degree-one completion is strict at the quotient one for positive Z when c_1<1; for each fixed higher degree (8)-(9) are positive definite, and the toroidal estimate is strict at that quotient. The high-degree sequence still forces the least constant one. At beta>=beta_1 the degree-one jet attains C_beta.

Combining Section 6 with A3204 gives a rigorous interval [1/m,C_beta] for the least global coefficient C_K in the inequality limsup K_a^-/(beta L log R)<=C_K(M-H), over all the stated kinematic fields. The corresponding coefficient uniform in beta lies in [1,16/13]. This does not assert the same interval for a coefficient multiplying delta in the bound limsup J_a/(beta L log R)<=C_s+C_J delta: the proved upper coefficient there is m/2+C_beta, whereas A3204 supplies only the lower bound 1/m. Nor does A3204 supply 1/m as a lower bound for the coefficient after the larger baseline m[1-beta+beta u(M)]. These distinct baselines must remain explicit when reporting coefficient ranges.
