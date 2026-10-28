# Retaining the lower-derivative coefficients in the fractional theorem

Status: CONFIRMED V090 after complete analytical and512-bit arithmetic audit. All constants are sufficient bounds. The norm itself is unchanged.

## Exact statement

Let the reference rho have the density parity rho(-x,y)=rho(x,y), rho(x,-y)=-rho(x,y), and let u=U[rho], where U=(-R1 R2,R1^2) is the canonical full-plane velocity. Fix c, put b=cX+u and

    L_fix h=b.Dh-h+U[h].D rho, A_k=L_fix+U[k].D.

Use all reference hypotheses W0,Wn,W2,W3,Wm of ../16_weighted_fractional/REFERENCE_AUDIT.md. Assume its low energy margin1/5, either through the W1 certificate at R=2^35 or through the replacement W1 certificate in ../17_weight_radius/PROOF.md at R=2^32. For a general reference these are hypotheses, not automatic consequences of proximity to state131. If a leading angular profile is asserted, also impose Wt. Existence below additionally requires the stated residual smallness, replacing Ws.

Put

    w_R=(1+r^2/R^2)^(-11/10), L_R(h)=||w_R h||_(dot H^-1),
    omega0=<r>^(-6/5), omega1=<r>^(-1/5),
    omega2=(1+4r^2)^(2/5), Pj(h)=||omegaj D^j h||_2,
    E_R(h)^2=P2(h)^2+2^22 P1(h)^2+2^53 L_R(h)^2,
    N(h)=N_(s,R)(h)=E_R(J^s h), J=(1-Delta)^(1/2).

Derivatives are ordered Cartesian tensors with Euclidean norm. The low and high spaces are completions of compact smooth parity densities. The canonical distributional realization and velocity are those in the cited reference hypotheses. On the maximal high domain {h in N: A_k h in N}, for0<s<=2^-12,

    ||exp(t A_k)||_(N->N)
       <=exp[-t(1/20-2^23 s-400 N(k)/sqrt(s))].              (1)

A positive rate gives a bijective inverse with the reciprocal-rate bound. The compatible low inverse has norm at most6 whenever that rate is positive. The following explicit choice is admissible:

    s=3*2^-31, r0=5*2^-32, eta=2^-35.                      (2)

For N(k)<=r0 the high inverse has norm at most40. If the normalized reference satisfies N(F(rho;c))<=eta, there is a unique normalized exact correction h in N(h)<=r0. Its low-metric contraction factor is less than2/5. The normalization is c[h]=0, with the exact strain including its contact term. The origin slope stays positive. The exponent and full leading angular profile are fixed.

For alpha=s/2, p=8/s and kappa=p+4, define

    C_ad(h)=||h||_(C^alpha(B2))
      +sup_(j>=0) 2^(-j/4)
          (||h||_(Linf(Aj))+2^(j alpha)[h]_(C^alpha(Aj))),
    Aj={2^j<=r<=2^(j+1)},
    M(h)=(int_(r<1) r^-kappa |h-h_y(0)y|^p dX)^(1/p).

Then

    L_R(h)+C_ad(h)+M(h)+|c[h]|<=2^8 s^(-3/2) N(h).         (3)

At (2) the same sum is at most2^58 N(A_k h). For a general positive rate beta in (1), the inverse constant in (3) is2^8 s^(-3/2)/beta.

No actual reference smallness is asserted. For original131 and R=2^32, V089 gives N(F)>2^82, so the gap over (2) is greater than2^117. At R=2^35 the previous V084 bound gives a gap greater than2^124. Both lower bounds apply at the new s.

## 1. Localization with the coefficients retained

The proved interpolation inequality

    P0(H)^2<=P1(H)^2+26 L_R(H)^2

implies P0(H)<=E_R(H)/2048. Directly P1(H)<=E_R(H)/2048 and P2(H)<=E_R(H). This is the only new ingredient needed in the localization step.

Use the C3 radial partition from ../16_weighted_fractional/PROOF.md. Its rescaled pieces F_j have the already proved estimate

    ||F_j||_(H2)<=t_j^(1/5)(507P0(H)+40P1(H)+P2(H)).

Therefore the former constant548 is replaced by

    K=1+547/2048=2595/2048.                               (4)

The partition, supports, derivatives, Fourier normalization and distributional convergence are unchanged. For H=J^s g and0<s<=1/2, the Fourier integral calculation gives

    (2pi)^-1 int |xi||g_hat| <=2K N(g)/sqrt(s)<4 N(g)/sqrt(s),
    ||Dg||_infinity<=4 N(g)/sqrt(s),
    [Dg]_(C^(s/2))<=6K sqrt(2/pi) N(g)/sqrt(s)<8 N(g)/sqrt(s).
                                                                    (5)

Indeed the geometric scale sum is less than6 and its radial Fourier constant is less than1/(3sqrt(s)); the Holder calculation uses the same scale sum and its exact beta-integral. The pointwise velocity multiplier has Euclidean norm at most1, so (5) holds for U[g] with the same constants. The original distributional Fourier argument excludes an undetected term at frequency zero.

Weighted Bessel-kernel estimates, applied before throwing away the coefficients, give

    P0(g)<=N(g)/512, P1(g)<=N(g)/1024, P2(g)<=3N(g).        (6)

The growth localization constant is now

    507/512+40/1024+3=2063/512.

At most three partition pieces meet a point and 2^(1/5)<5/4. Planar H2 embedding has constant less than1. Hence

    |g(X)|<=16 max(1,r)^(1/5) N(g),                       (7)

since (15/4)(2063/512)<16. The corresponding canonical velocity has this bound multiplied by13/2. Thus its sublinear representative and the far subtraction remain justified.

## 2. Sobolev derivative multiplication

For0<s<=1/2 the unitary Fourier product calculation in the previous proof gives

    ||vf||_(H^s)<=s^(-1/2)||v||_(H^(1+s))||f||_(H^s).

For v=Dg, its low-frequency Fourier L1 norm is bounded by4 N(g)/sqrt(s) from (5), and low-frequency multiplication costs at most twice that constant. The high-frequency piece has H^(1+s) norm at most sqrt(2) N(g), because H=J^s g and P2(H)>=||D2H||2. Consequently

    ||Dg f||_(H^s)<=16 N(g)/sqrt(s)||f||_(H^s),            (8)

using8+sqrt(2)<16. The same statement holds for DU[g], with Euclidean contractions and no extra component factor.

For any of the weights in the derivative and direct low commutator arguments, the relative Bessel commutator estimate is bounded by400s. Thus (8), commuting the weight at both ends, yields

    ||v J^s(Dg f)||2<=32 N(g)/sqrt(s)||v J^s f||2,         (9)

since16(1+400s)+1600s<32 for s<=2^-12. The derivative weights had the stronger bound102s; using400s is a common upper bound. No new weighted Riesz estimate is assumed.

## 3. Every rough energy term

Write n=N(k), W=U[k]. The direct low-commutator proof is uniform in R>=1. Its relative double-commutator gives, on either v=w_R or v=<r>w_R,

    ||v [J^s,W.D]J^-s f||2<=8 n/sqrt(s)||vf||2.

Here (1+2200s)4<8 for s<=2^-12. Subtracting multiplication by DW from (9) gives the safe bound40 n/sqrt(s) for [J^s,DW]J^-s. The exact negative-order factorization therefore gives

    L_R([J^s,W.D]J^-s h)
       <=[(27/5)*8+(16/5)*40] n/sqrt(s) L_R(h)
       =(856/5)n/sqrt(s)L_R(h).                          (10)

The factorization is h=-div(w_R^-1 q)-Dlog(w_R).w_R^-1 q, q=D(-Delta)^-1(w_R h), together with

    [partial_i,[J^s,W.D]J^-s]
                    =sum_j partial_j[J^s,partial_i W_j]J^-s.

It uses div W=0. All scalar Hardy remainders are centrally odd. These are the identical identities used in the already audited direct proof; the constants in their inputs are the only changes.

The native low transport costs12||DW||_infinity<=48 n/sqrt(s). In the top derivative component the three costs are

    (14/5)*4, 2*32, (9/5)*32,

and in the first derivative component they are (11/5)*4 and32. The factor9/5 is the proved weighted velocity bound on the odd second derivatives of k. No third derivative of W is used. Summing all components gives

    664/5+204/5+48+856/5=1964/5<400.                       (11)

The fixed-reference smooth commutator is unchanged and remains bounded by2^23s. Adding (11) to the base E_R rate1/20 proves (1) on the compact core.

## 4. The improved low bilinear constant

For a centrally odd homogeneous H1 test phi, the dyadic cutoff construction in section7 of ../16_weighted_fractional/ROUGH_INVERSE_PROOF.md has rescaled H1 norm at most69 times the gradient energy on the enlarged annulus. Those enlarged annuli overlap at most four times. Retain the sharper Fourier coefficient in that construction: for q=4/s,

    ||f||q<=C_q ||f||H1,
    C_q=(2pi)^(-1+s/2)[pi(2-s)/s]^((2-s)/4)<=s^-1/2.

The last inequality follows because the bracket is greater than1, its exponent is at most1/2, and (2pi)^(-1+s/2)<=(2pi)^(-1/2). The scaling exponents and reciprocal omega2 weights are at most one on the inner and outer annuli. The lq sum is bounded by the l2 sum. Consequently

    ||phi/omega2||_(4/s)<=138 s^-1/2||Dphi||2.             (12)

For p=2/(1-s/2), the unitary Hausdorff-Young and Holder calculation gives ||f||p<=||f||Hs. Also ||omega2 D2g||Hs<=2N(g), by the same relative weight estimate as before. Equations (12) and Holder give

    ||D2g phi||2<=276 N(g)/sqrt(s)||Dphi||2.

The other derivative of Dg phi costs at most4 N(g)/sqrt(s)||Dphi||2 by (5). Thus the dual derivative multiplier has norm at most280 N(g)/sqrt(s). Applying the canonical low velocity bound13/2 proves

    L_R(U[h].Dg)<=1820 N(g)/sqrt(s)L_R(h)
                      <=2^11 N(g)/sqrt(s)L_R(h).         (13)

The dual test is centrally odd after the even derivative coefficient is multiplied into it. The product agrees with its distributional meaning by smooth density.

## 5. Domains, normalization and numerical parameters

The map J^s:N->E_R is onto, the smooth core is dense, and (5) gives uniform C1 convergence of the approximating velocities. The common P0 realization, maximal distributional high domain, and low/high consistency are proved in sections6 and8 of the previous theorem. Their seven dependencies are audited explicitly in its sharp version. Each remains valid here: all restrictions used in (4)-(13) are0<s<=2^-12, and the low inclusion is still L_R(h)<=6*2^(-53/2)N(h). There is no radius conversion.

For precision, the one changed automatic low-rate bound is this: positivity of (1) gives400n/sqrt(s)<1/20, and hence ||DW||infinity<1/2000. Therefore1/5-12||DW||infinity>1/6. The low inverse integral exists whenever the high inverse integral does, and the two agree on their common forcing space. The common P0 generator and the Duhamel identity also put nonlinear differences in the low domain. These facts prove surjectivity and injectivity, not merely an energy inequality.

At (2), sqrt(s)=sqrt(6)*2^-16, so n/sqrt(s)<=5/(65536sqrt(6)). Since sqrt(6)>12/5,

    beta>=1/20-3/256-2000/(65536sqrt(6))
          >6283/245760>1/40.                            (14)

Thus40eta=r0. By (13), the low contraction factor is at most

    6*2^11*r0/sqrt(s)=15/(16sqrt(6))<25/64<2/5.           (15)

The ball is complete in the low metric by weak high compactness and distributional identification. The exact origin identity remains

    (A_k h)_y(0)=c[k]h_y(0)+rho_y(0)c[h].

The reference residual has zero y derivative at0. On c[k]=0, inverse application therefore preserves c[h]=0. The slope change is at most4r0/sqrt(s)<2^-12, so the positive reference slope stays positive. The resulting contraction is the same normalized formulation P. The fixed leading profile assertion follows from (7) and gamma>1/5; exponent and logarithmic variations are excluded by this chosen space.

## 6. The four output quantities

On each annulus t<=r<=2t, (7) gives sup|h|<=20t^(1/5)N. The elementary interpolation inequality between this supremum and (5) gives

    t^alpha[h]C^alpha<=40s^-1/2 t^(1/5+(4/5)alpha)N.

The exponent is less than1/4. On B2 the same supremum and Holder constants hold without powers of t. Consequently C_ad(h)<=120s^-1/2N<128s^-1/2N.

At the origin parity gives Dh(0)=(0,h_y(0)). Taylor integration of (5) yields

    |h-h_y(0)y|<=8s^-1/2N r^(1+alpha)/(1+alpha).

Since p alpha=4, the radial moment integral contributes pi^(1/p)<2. Hence M(h)<=16s^-1/2N.

Finally use the exact canonical strain formula

    c[h]=-h_y(0)/4+(1/pi)PV int sin(3theta)h/r^3 dX.

The near integral, after subtracting the linear jet, is bounded by32/[pi alpha(1+alpha)]s^-1/2N. Its far integral is at most2P0(h)<=N/256, by weighted Cauchy-Schwarz. The contact term is at mosts^-1/2N. Since alpha=s/2 and pi>3, the total is less than32s^-3/2N. Together with L_R(h)<=N this proves (3), because1+128+16+32<256.

At (2),40*256*s^-3/2<2^58; equivalently40*(2/3)^(3/2)<32. This proves the stated inverse output bound. These estimates directly control h; they do not substitute a separate Holder norm of h_x as the unknown.

## Evidence and scope

The arithmetic script verification/constants.py checks every new rational comparison and encloses the square-root quantities with Arb. It binds this proof and all imported proof files by their hashes. The analytic arguments above are required in addition to its output. No numerical residual estimate is used to establish these constants. The original residual lower bounds are independently certified in the earlier annular proofs.
