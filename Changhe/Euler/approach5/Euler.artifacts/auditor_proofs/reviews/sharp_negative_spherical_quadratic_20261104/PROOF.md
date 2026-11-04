# The sharp uniform modal bound for the negative spherical source

## 1. Exact statement

Let U be a real C1 divergence-free field on R3, with E(R)=integral_(|y|<R)|U|^2 and E(R)/(L R^beta)->1, where L>0 and0<beta<1. Put

    t=(beta-3)/2, k=(beta+1)/2=t+2, m=2-beta=3-2k,
    D=k^2+2, H=t^2(k^2+4)/D, C_s=mt^2/D, C_*=16/13.

At a fixed center a let r_a=|y-a| and define

    F_a(R)=integral_(1<r_a<R) r_a^-beta |U|^2dy,
    G_a(R)=integral_(1<r_a<R) r_a^(2-beta)|DU|_F^2dy,
    q=tr((DU)^2), Q_a(r)=integral_(S2)q(a+rn)dn,
    K_a^-(R)=integral_1^R r^(4-beta)[-Q_a(r)]_+dr,
    J_a(R)=integral_1^R r^(4-beta)[Q_a(r)]_+dr.

Sphere area is4pi; the matrix derivative is Cartesian. If M=limsup G_a/(beta L log R) is finite, then M>=H, M and L are center-independent, and at every fixed center

    limsup K_a^-/(beta L log R)<=min(M,C_*(M-H)),
    limsup J_a/(beta L log R)
        <=min(M,m[1-beta+beta u(M)]+C_*(M-H)),
    u(M)=min(1,k^2/D+(M-H)/(2beta)).                 (1)

In particular, for every finite delta=M-H>=0, these coefficients are at most C_*delta and C_s+(m/2+C_*)delta respectively. There is no smallness restriction on delta. The constant C_* is sharp for the uniform modal quadratic inequality proved below. Global logarithmic optimality is not claimed.

This independently reconstructs all six sections and48obligations of source8ffb5b58. The negative part is after spherical averaging. The only earlier theorem used for the positive bound is the confirmed upper tangential envelope A3153; the Euler application uses A3053.

## 2. Exact mode identities and passage to a C1 field

Work first at a=0. Write U(rn)=r^t v(z,n), z=log r. Then F=integral|v|^2 dz dn and G=integral(|v_z+tv|^2+|grad_S v|^2)dz dn, with the angular derivative acting on Cartesian components. Solenoidality gives (partial_z+k)(v.n)+div_S v_T=0; the degree-zero radial mode vanishes by zero flux through every whole-space sphere.

For a real unit L2 harmonic Y, lambda=ell(ell+1), ell>=1, use

    v_pol=fY n+(f'+kf)grad_S Y/lambda,
    v_tor=h n cross grad_S Y.

The divergence relation makes f C2; the velocity and tangential coefficients, and h, are C1. Direct differentiation of n and integration of the harmonic gradient and Hessian give

    K_pol=f^2+(f'+kf)^2/lambda,
    D_pol=2(f'+tf)^2+[f''+(k+t)f'+tkf]^2/lambda
                                      +(lambda-2)f^2,
    K_tor=lambda h^2,
    D_tor=lambda[(h'+th)^2+lambda h^2].             (2)

Orthogonality for these integrated energies follows from harmonic integration by parts; it is not pointwise matrix orthogonality. Define

    Z_pol=f''^2/lambda+b_lambda f'^2+d_lambda f^2,
    b_lambda=2+(k^2+t^2-H)/lambda,
    d_lambda=(t^2-H)(1+k^2/lambda)+lambda+t^2-2,
    Z_tor=lambda[h'^2+(t^2+lambda-H)h^2].           (3)

Here b_lambda>=1, d_2=0, b_2=D/2+2beta/D>=9/8, d_lambda>=lambda-3-2/lambda>=4lambda/9 for lambda>=6, and t^2+lambda-H>=4beta/D>0. For the d bound use t^2-H=-2t^2/D>-2, t^2>1 and k^2<1; the last difference vanishes at6 and has positive derivative.

For compactly supported smooth eta>=0, expanding (2) and integrating the mixed derivatives gives

    integral eta(D_pol-HK_pol)=integral eta Z_pol
      -(k+t)/lambda integral eta'f'^2
      -[2t+((k+t)tk-Hk)/lambda]integral eta'f^2
      +tk/lambda integral eta''f^2,
    integral eta(D_tor-HK_tor)=integral eta Z_tor
      -t lambda integral eta'h^2.                 (4)

All errors sum to at most C_beta integral(|eta'|+|eta''|)|v|^2. In particular f'^2/lambda<=2(f'+kf)^2/lambda+2k^2f^2/lambda, uniformly in degree. Thus, with Z the sum of (3),

    integral eta Z=G_eta-HF_eta
             +O_beta(integral(|eta'|+|eta''|)|v|^2). (5)

Finite mode sums first prove this identity. Local angular H1 and radial derivative L2 convergence give convergence of both energies and all uniformly bounded error terms. The nonnegative main terms pass monotonically, proving local integrability of Z and (5) for the whole C1 field.

Set A(z)=integral|v.n|^2 and K(z)=integral|v|^2. The identity q=div div(U tensor U), tested with radial functions, gives in distributions

    Qflat=r^(5-beta)Q_0(r)
       =A''+(2beta-2)A'+beta(beta-2)A-K'+mK.        (6)

For a poloidal mode, set p=f' and w=f''. Substitution of A=f^2 and K=K_pol gives

    Q_pol=s_lambda f^2+A_lambda fp+B_lambda fw
                         +C_lambda p^2-2pw/lambda,
    s_lambda=m(1-beta+k^2/lambda),
    A_lambda=8k-10+6k(1-k)/lambda,
    B_lambda=2(1-k/lambda),
    C_lambda=2+(3-4k)/lambda.                      (7)

For a toroidal mode Q_tor=m lambda h^2-2lambda hh'. Equation(6) has no cross terms because A and K have none. For general C1 fields, local L2 convergence of DU implies local L1 convergence of tr((DU)^2), by the matrix inequality

    |tr(B^2)-tr(C^2)|<=|B-C|_F(|B|_F+|C|_F).

Consequently the source sums pass in local L1 in z. No second derivative of the full C1 velocity is assumed.

## 3. The degree-one inequality and its determinant

At lambda=2, s_2=mt^2/2, A_2=t(5-3k), B_2=-t, C_2=7/2-2k. Completing the f square gives

    Q_pol+C_* Z_pol
       =(mt^2/2)[f+((5-3k)p-w)/(mt)]^2
                            +P_2p^2+R_2pw+W_2w^2,
    P_2=C_*b_2+C_2-(5-3k)^2/(2m),
    R_2=-t/m, W_2=(C_*-1/m)/2.                    (8)

Here W_2>=3/26. For a transparent determinant computation, observe

    2m C_2-(5-3k)^2=-t^2,
    P_2=C_*b_2-t^2/(2m),
    P_2W_2-R_2^2/4
       =C_*[2b_2(C_*m-1)-t^2]/(4m).

Also 2b_2=(k^4+4k^2+8k)/D and C_*m-1=(35-32k)/13. Therefore the numerator reduces by the exact polynomial identity

    (k^4+4k^2+8k)(35-32k)-13(k-2)^2D
       =2(1-k)(16k^4+5k^3+43k^2+140k-52).

Writing T(k) for the last polynomial gives

    P_2W_2-R_2^2/4=8(1-k)T(k)/(169Dm)>0,
    T(1/2)=243/8,
    T'(k)=64k^3+15k^2+86k+140>0.

Since W_2>0, positivity of this determinant implies P_2>0 and positivity of the residual two-dimensional form. This proves Q_pol+C_*Z_pol>=0 for every degree-one jet, for the entire open range1/2<k<1.

## 4. Every higher degree and the toroidal modes

For lambda>=6 complete the w square in (7):

    Q_pol+C_*Z_pol
      =(C_*/lambda)[w+(lambda B_lambda f-2p)/(2C_*)]^2
                         +P f^2+R fp+S p^2,
    P=s_lambda+C_*d_lambda-(lambda-k)^2/(C_*lambda),
    R=A_lambda+B_lambda/C_*,
    S=C_lambda+C_*b_lambda-1/(C_*lambda).           (9)

Put x=1-k in(0,1/2) and v=t^2k^2/D. Since t^2>1 and k^2/D>1/9, v>1/9. Since k(2-k)<1 and D>9/4, v<4/9. The exact identity

    d_lambda=lambda-2+v-2v/lambda

therefore gives d_lambda>=lambda-17/9-8/(9lambda). Also b_lambda>=2-2/lambda, C_lambda>=2-1/lambda and s_lambda>=2x+4x^2. Using2k/C_*>=1/C_* and k^2<=1 yields

    P>=(C_*-1/C_*)lambda-17C_*/9
        -8C_*/(9lambda)+1/C_*-1/(C_*lambda)+2x+4x^2
      >=7633/11232+2x+4x^2>2/3+2x+4x^2,
    S>=2+2C_*-(1+2C_*+1/C_*)/lambda
      >=4679/1248>3.                              (10)

Both lower expressions increase with lambda, so evaluation at6 proves these exact fractions. The mixed coefficient is

    R=8k-67/8+k(35/8-6k)/lambda.

The last numerator decreases on[1/2,1], from11/16 to-13/8. Thus R<=-3/8+11/96<0, and R>=-(31/48+8x). It follows that

    4PS-R^2>12(2/3+2x+4x^2)-(31/48+8x)^2
       =8-961/2304+(41/3)x-16x^2
       >=17471/2304+(17/3)x>0,                    (11)

using x^2<=x/2. This proves positivity in (9) for every real lambda>=6, hence every higher angular degree. There is no finite-degree extrapolation.

For a toroidal mode,

    m h^2-2hh'=m(h-h'/m)^2-h'^2/m>=-h'^2.

Since Z_tor>=lambda h'^2, Q_tor>=-Z_tor>=-C_*Z_tor. Summation, local L1 source convergence and an almost-everywhere subsequence give

    [-Qflat]_+<=C_*Z                              (12)

almost everywhere for the full field.

## 5. Sharp modal constant, cutoffs and centers

At the limiting endpoint k=1, t=-1,m=1,H=5/3,b_2=13/6. The jet(f,p,w)=(19,3,-13) gives

    Q_pol=361/2-114-247+27/2+39=-128,
    Z_pol=169/2+(13/6)9=104.

Thus -Q_pol/Z_pol=16/13. By continuity, for every smaller constant there is an admissible k<1 sufficiently close to1 and the same jet violating that smaller comparison. Any jet is realized by a quadratic polynomial in z near a positive radius, multiplied by a smooth cutoff equal to1 there; the poloidal divergence formula then gives a smooth solenoidal annular field. If a whole-space energy-ratio field is desired, choose the same radial coefficient to vanish near0 and to become a nonzero constant outside a larger annulus, with that constant normalized to L. The local jet remains unchanged and E(R)/(LR^beta)->1. This verifies modal admissibility but does not produce a logarithmic extremizer.

Stieltjes integration gives F(R)=beta L log R+o(log R), and each fixed-width distant logarithmic velocity strip has bounded energy. Choose eta_R=1 on[0,log R], supported in(-log2,log(2R)), with0<=eta_R<=1 and uniformly bounded first two derivatives. Equations(5),(12) give

    K_0^-(R)<=C_* integral eta_R Z
           <=C_*[G_0(2R)-HF_0(R)]+C_beta,U.        (13)

Only the inner fixed gradient strip contributes an extra finite constant; no outer gradient-strip bound is needed. Division by beta L log R proves the second part of the minimum in(1). The direct inequality |q|<=|DU|_F^2 proves K_0^-<=G_0 and J_0<=G_0, giving the other parts. Nonnegativity of Z and the inner-cutoff version of(5) also give M>=H.

The signed identity(6) integrated against eta_R is

    integral eta_R Qflat=m(1-beta)F_eta+m beta T_eta+O(1).

Its boundary terms are integral[eta_R''+(2m-1)eta_R']A+integral eta_R'|v_T|^2, both controlled by velocity strips. The upper tangential theorem A3153, or T_eta<=T_0(2R)+O(1), gives limsup T_eta/(beta L log R)<=u(M). Since[Qflat]_+=Qflat+[-Qflat]_+, equations(5),(12) prove the positive bound in(1). The identity m(1-beta+beta k^2/D)=C_s gives the stated simpler linear bound. No sign of an uncontrolled boundary term is used.

Ball inclusions preserve the energy ratio and L under a fixed translation. The gradient weights at two fixed centers have ratio tending uniformly to1 outside any sufficiently large fixed ball, while integration radii differ by at most the distance between the centers. Comparing in both directions gives the same extended-real normalized gradient limsup M. Applying the argument anew at each center proves all statements there; the Euler equation is not translated.

## 6. Euler scope

For a nonzero full rotating profile U,P in C1, with U bounded, U(R.) tending to zero distributionally,2/5<c<1/2 and arbitrary finite omega, A3053 supplies the energy ratio with beta=5-2/c and L>0. Under the additional finite-M hypothesis, (1) holds with this beta for every finite omega. Uniform velocity decay gives boundedness and distributional blow-down, but no finite gradient budget is proved here.

The source8ffb5b58, all48obligations and the formal-status note are fully read. The independent proof uses no mathematical computation, numerical optimization, formal build or new external source. The constant16/13 is optimal only for the uniform modal inequality; full logarithmic optimality, eventual source positivity, control of the pointwise negative source and the main arbitrary-omega nonexistence conjecture remain open.

## 7. Exact degree-one constant for a fixed exponent

The C comparison additionally gives a rational expression for the least constant at degree one for fixed beta. Its determinant computation and sampled positivity can be replaced by the following complete analytic argument. Replace C_* in (8) by a real c. The f square stays unchanged, and the residual coefficients are

    P(c)=c b_2-t^2/(2m), R(c)=-t/m,
    W(c)=(c-1/m)/2,
    det(c)=c[2b_2(cm-1)-t^2]/(4m).

Since b_2>0 and t!=0, put c_1=(2b_2+t^2)/(2m b_2)>1/m. At c=c_1, W>0 and the determinant is zero, so P=R^2/(4W)>0 and the residual form is positive semidefinite. For c<1/m its w coefficient is negative. At c=1/m the nonzero mixed coefficient prevents positive semidefiniteness. For 1/m<c<c_1 the determinant is negative. Since f is free to minimize its square, these failures are failures of the complete three-variable quadratic form. Thus c_1 is exactly the least degree-one constant, with no numerical premise.

For b=beta, define Q=b^2+2b+9 and N=b^4+4b^3+22b^2+100b+81. The identity 2b_2=N/(4Q), together with t^2=(b-3)^2/4, gives

    c_1(beta)=(2b^4+28b^2+64b+162)
             /(162+119b-56b^2-14b^3-2b^4-b^5).

The denominator is (2-b)N>0. In this formula

    16 denominator - 13 numerator
      =2(1-b)(8b^4+37b^3+149b^2+779b+243)>0,

so c_1(beta)<16/13 at every admissible beta, while its limit as beta tends to one is16/13 and its limit as beta tends to zero is1. Furthermore c_1-1 has the sign of

    b[b^4+4b^3+14b^2+84b-55].

The bracket is strictly increasing on[0,1], negative at zero and positive at one, so it has a unique root there. These fixed-degree facts do not prove the proposed optimum over all degrees at fixed beta, nor the optimum of the global logarithmic inequality.

## 8. Reconciliation with the existing C comparison

The entire seven-item C comparison of 2026-11-04T11:08:15Z was read and retained. Items1-3 agree with the exact identities and analytical inequalities of Sections2-4. Item4 contains numerical diagnostics, which are not used. The uniform sharpness in item5 agrees with Section5; the fixed-degree rational expression is proved analytically in Section7, independently of its sampled positive-semidefinite checks. The sampled minimum and numerical location of the root are not certified here. Item6's proposed fixed-beta optimum over all degrees remains unproved by this review. Item7 correctly identifies the convergence as local angular and radial Parseval convergence, already spelled out in Section2, and retracts the earlier numerical implication as a proof. No new hypothesis or mathematical gap was found.

The collaboration used the existing C agent configured as model; the actual provider execution is independently unattested. Only file exchange was used. No additional model client or agent was launched.
