# Smaller coefficients in the weighted first and second derivative energies

## 1. Statement and dependencies

Let the background be exact state131, with the canonical full-plane velocity and even-x, odd-y density parity. Put

    L_fix h=(cX+Ubar).D h-h+U[h].D rhobar,
    R=2^35, w=(1+r2/R2)^(-11/10), L(h)=||w h||_(Hdot^-1),
    omega0=<r>^(-6/5), omega1=<r>^(-1/5),
    omega2=(1+4r2)^(2/5), Pj(h)=||omegaj D^j h||_2,
    E1(h)^2=P1(h)^2+2^31 L(h)^2,
    E2(h)^2=P2(h)^2+2^22 E1(h)^2.

Here <r>=(1+r2)^(1/2), and every derivative tensor is the ordered Cartesian tensor with its Euclidean norm. Spaces are the completions of compact smooth parity functions in the displayed norms. The linear operator has the same transport-plus-bounded-coupling generator realization as H2_INVERSE_PROOF.md. It has consistent bijective inverses on E1 and E2, with bounds10 and20 respectively. Its semigroup decays at rates1/10 and1/20.

The hypotheses used are the following previously confirmed inequalities for the same exact reference:

    weighted low energy margin>=1/5 at R=2^35;
    M1(omega1), M2(omega2)>=I/2;
    |D rhobar|<16, <r>|D2 rhobar|<=8,
    <r>2|D3 rhobar|<=32, <r>|D2 Ubar|<=3;
    ||U||_(L2(omega0^2),central odd)<=8/3,
    ||U||_(L2(omega1^2))<=3/2,
    ||U||_(L2(omega2^2),central odd)<=9/5.

The first is V072, the matrices are V036, the derivative bounds are V024 and V045, and the weighted velocity bounds are V044. These hypotheses are not automatically true for a repaired or refitted reference. The new norms have smaller fixed coefficients than the earlier weighted hierarchy. No nonlinear conclusion or small-residual assertion is made here.

## 2. Exact identity and weight derivatives

For v=omega^2, a=D rhobar, b=v a, and a scalar compact smooth f, the audited integration-by-parts identity is

    -sum_i int b.U[partial_i f] partial_i f
      =int v Df^T A Df
       +(1/2)int(v_xy rho_x-v_xx rho_y-v_x rho_xy+v_y rho_xx)f2
       +sum_i int f (partial_i b).U[partial_i f],
    A=[[rho_y,-rho_x/2],[-rho_x/2,0]].                       (1)

All terms in(1) are retained. The scalar coefficient, in absolute value, is at most

    (1/2)(|D2v|_F |D rho|+|Dv| |D2rho|_F).                 (2)

For v1=<r>^(-2/5), direct radial differentiation gives

    |Dv1|<= (2/5)v1/<r>,
    |D2v1|_F<= (2sqrt(2)/5+24/25)v1/<r>2
                <(8/5)v1/<r>2.                           (3)

For v2=(1+4r2)^(4/5), one similarly obtains

    |Dv2|<=2v2/<r>, |D2v2|_F<=10v2/<r>2.                  (4)

For an explicit check of(4), set t=r2. The function t(1+t)/(1+4t)^2 has maximum1/12, at t=1/2. Hence the first constant is at most16/(5sqrt(3))<2. For the second constant the triangle bound is

    (32sqrt(2)/5)(1+t)/(1+4t)
       +(256/25)t(1+t)/(1+4t)^2
      <=32sqrt(2)/5+64/75<64/7+64/75<10.

We used sqrt(2)<10/7. The actual Hessian contains a negative radial rank-one term; the triangle bound is an upper bound and does not rely on its sign.

The weight ratios used below are

    omega1/omega0=<r>,
    omega2/omega1<=2<r>, omega2/omega0<=2<r>2.               (5)

## 3. First derivative energy

In(1), take f=h and v=v1. Equations(2)-(3) give a scalar error at most(72/5)P0^2 and

    |D(v1 D rhobar)|/(sqrt(v1) omega0)<=72/5.

The identity's last term therefore costs at most(108/5)P0 P1, by the unrestricted omega1 velocity bound3/2. The additional term obtained by differentiating the density-gradient coefficient costs at most8*(8/3)P0 P1. The transport and principal nonlocal terms give precisely M1. Consequently

    -<D L_fix h,omega1^2 D h>
      >=(1/2)P1^2-(644/15)P0 P1-(72/5)P0^2
      >=(3/8)P1^2-2^12 P0^2.                              (6)

For the last step, Young's inequality uses

    (644/15)P0P1 <=(1/8)P1^2+2(644/15)^2P0^2,
    2(644/15)^2+72/5 <2^12.

No component count is hidden in these estimates: the Riesz constants are scalar-to-vector bounds, and tensor Cauchy-Schwarz sums all ordered derivatives.

For completeness, the low interpolation is uniform for every R>=1:

    P0^2<=epsilon P1^2+(25+epsilon^(-1))L^2.                (7)

To prove it, set a=omega0^2/w. Direct differentiation gives a<=omega1 and |Da|<=5omega0. Pair wh with ah in Hdot^-1/Hdot^1 to obtain P0^2<=L(P1+5P0), and apply Young's inequality. The angular parity permits every dual test. For epsilon=2^-15, (6)-(7) imply

    -<D L_fix h,omega1^2 D h>
      >=(1/4)P1^2-(2^27+25*2^12)L^2.                      (8)

The exact inequality2^27+25*2^12<2^31/10 and the low margin1/5 now give

    -<L_fix h,h>_E1 >=(1/10) E1(h)^2.                     (9)

Equation(7) at epsilon=1 also gives P0<=E1, since26<=2^31.

## 4. Second derivative energy

Apply(1) to f=partial_j h and sum j, using v=v2. By(4)-(5),

    |D(v2 D rhobar)|/(sqrt(v2) omega1)
      <=2(8+2*16)=80.

The identity's last term therefore costs at most144 P1P2, using the centrally odd omega2 velocity bound9/5. Its scalar term costs at most

    4*(1/2)(10*16+2*8)P1^2=352P1^2.                       (10)

The remaining transport term D2Ubar.Dh costs6P1P2. The two differentiated nonlocal terms containing U[Dh].D2rhobar together cost48P1P2, using the omega1 bound3/2. The last term U[h].D3rhobar costs(512/3)P0P2, using the omega0 bound8/3. The remaining principal contribution is exactly M2. Thus

    -<D2 L_fix h,omega2^2 D2h>
      >=(1/2)P2^2-198P1P2-(512/3)P0P2-352P1^2
      >=(1/2)P2^2-370E1P2-352E1^2
      >=(1/4)P2^2-140000E1^2.                             (11)

The two scalar comparisons are198+512/3<370 and370^2+352<140000. Adding2^22 times(9) gives

    -<L_fix h,h>_E2 >=(1/20)E2(h)^2,                      (12)

because140000<2^22(1/10-1/20). Equations(10)-(11) explicitly include every lower-order weight, background-transport and nonlocal coefficient term.

## 5. Realization, inverse and scope

The transport flow is complete, smooth, parity preserving, with bounded finite-time derivatives and the weighted second-derivative bounds established in H2_INVERSE_PROOF.md. It acts on these new spaces by exactly the same product and weight-ratio estimates. The background coupling U[h].D rhobar is bounded on E1 and E2 by the displayed coefficient and Riesz bounds, and on the low space by V067 and the parity multiplier estimate. The resulting bounded-perturbation Duhamel series is consistent with the low semigroup.

Compact smooth parity functions form a common graph core: approximate the transport resolvent integral by finite sums of transported compact functions, then use bounded perturbation. The energy inequalities(9),(12) pass to the generator domains. Exponential decay gives the inverse as minus the integral of the semigroup over nonnegative time. The generator identity for finite integrals and closedness prove surjectivity; a constant orbit and strict decay prove injectivity. These arguments apply to the same low realization and prove consistency, not only separate coercive inequalities.

The accepted density residual belongs to both spaces since its leading exponent2/c-1 is below1/5, and its derivative asymptotics have the same weighted threshold. Smooth truncations converge at infinity and the center is regular. This membership is unchanged by the finite positive coefficients or the choiceR=2^35. The result controls weighted derivatives through order2 and hence h itself in adapted local Holder norms below exponent1; it does not alone supply a C1 trace, the singular functional, or nonlinear high solvability. Those stronger claims require a compatible fractional construction.
