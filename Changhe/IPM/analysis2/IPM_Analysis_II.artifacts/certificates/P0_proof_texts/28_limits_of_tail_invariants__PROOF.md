# Limits of a tail-invariant argument in the weighted norm

Status: CONFIRMED V111 by independent recurrence and arithmetic checks, with lead analytical review CORRECT at07:41Z. The constructed functions are residual-shaped functions in a linear relaxation. They are not asserted to be residuals of any IPM potential.

## 1. Statement and purpose

Use the exact c, delta, a0=7delta/2-2, leading sine coefficients e_m and degree bound154 of topic26. Put mu=11/10, R=2^31, w_R=(1+r^2/R^2)^(-mu), and define

    P1(f)=||<r>^(-1/5) Df||2,
    P2(f)=||(1+4r^2)^(2/5) D2f||2,
    L_R(f)=||w_R f||_(dot H^-1),
    E_R(f)^2=P2(f)^2+2^22 P1(f)^2+2^53 L_R(f)^2,
    N_(s,R)(f)=E_R((1-Delta)^(s/2)f), 0<s<=1/2.

All tensor norms are ordered Cartesian Frobenius norms. The spaces are the compact parity completions used in topics16 and18. We construct a smooth even-x, odd-y function f with f_y(0)=0, leading tail r^(1-7delta)e(theta), all eight preceding sectors zero, and exactly the finite power representation allowed for residuals in topic26. An explicit bound for its complete N_(s,R) norm is given below. The certified value below2^-35 shows that the fixed leading tail and the finite power representation alone do not exclude the weighted sufficient residual threshold. Such a result does not imply the existence of an IPM reference with small residual.

## 2. An explicit finite-dimensional construction

For each odd m with e_m nonzero, put

    M_m=(m+1)/2+4, K_m=154-M_m,
    A_m={ell delta/2+k-2 : 1<=ell<=12, 0<=k<=K_m,
                             ell delta/2+k-2>=a0}.

Let q_m be the unique element of span{u^a:a in A_m} whose u^a0 coefficient is1 and whose norm ||u^mu q_m||_L2(0,1) is minimal. Existence and uniqueness follow from the positive definite Gram matrix. The orthogonal projection formula of topic26 makes this an exact definition using rational arithmetic. In particular

    D_m:=||u^mu q_m||2
       =(2(a0+mu)+1)^(-1/2)
          product_(a in A_m, a>a0) (a-a0)/(a+a0+2mu+1).

Set u=(1+r^2)^(-1), t=1-u, and

    f_m(r,theta)=e_m u^(3/2) t^(M_m-1/2) q_m(u) sin(m theta),
    f=sum_m f_m.

At infinity the u^a0 coefficient is1, so the leading tail is the required one. There are no smaller exponents. The compactified quantity w_m=t u^-2 H_m equals t^M_m q_m and has degree at most154 in the integer power variable; H_m=u^2 t^(M_m-1)q_m has degree at most153. Thus it has precisely the larger finite power representation of topic26. No claim is made that its coefficients satisfy the nonlinear identities of an actual residual.

At the origin, t^(M_m-1/2)sin(m theta) is r^(m+8) times a smooth radial analytic factor and sin(m theta). Since m is odd, r^m sin(m theta) is a homogeneous polynomial of the correct parity. All other factors are smooth functions of r^2 there. Hence f is smooth and its low center jets vanish. At infinity it and each derivative have the differentiated power decay of r^(1-7delta). Smooth radial cutoffs approximate it in all the weighted norms below.

## 3. Dilation and derivative bounds

Write g_m=u^mu q_m. This belongs to the power space with exponents a+mu for a in A_m. The exact dilation estimate of topic26 gives

    ||(u partial_u)^j g_m||2<=C_m^j D_m,
    C_m^2=sum_(a in A_m)(a+mu)^2
              +sum_(a<b)(2(a+mu)+1)(2(b+mu)+1).

Define A_(m,0)=1 and, for1<=k<=4,

    A_(m,k)=product_(j=0)^(k-1)(4C_m+2m+48/5+6j).

For each Cartesian derivative of order k, the complex polar derivative formulas produce a sum of angular modes with radial factor

    u^(alpha+k/2)t^(beta-k/2),
    alpha=2/5, beta=m/2+4,

times a polynomial in u applied to (u partial_u)^j g_m, j<=k. The sum of coefficient norms, with C_m^j as weights, is at most A_(m,k). Here coefficient norm means the sum of the absolute monomial coefficients. To verify the recurrence, use

    partial_x +/- i partial_y
       =exp(+/- i theta) r^-1(r partial_r +/- i partial_theta),
    r partial_r=-2ut partial_u.

After k steps the polynomial degree is at most k and the current angular order has absolute value at most m+k. The derivative of a coefficient polynomial costs at most4k in coefficient norm; the derivative of g costs at most4C_m; the radial prefactor and angular term together cost at most2m+48/5+2k. Their sum proves the stated factor with6k. The factors beta-k/2 remain positive for k<=4. Expressing each Cartesian derivative as an average of the complex derivatives does not increase this bound.

There are2^k ordered Cartesian components. Bounding each angular function by its coefficient sum and using the angular measure2pi and radial measure du/(2u^2) therefore gives

    ||omega1 D^k f_m||2
       <=2^(k/2)sqrt(pi)|e_m| A_(m,k) D_m,        k>=1,
    ||omega2 D^k f_m||2
       <=4^(2/5)2^(k/2)sqrt(pi)|e_m| A_(m,k) D_m, k>=2,
    ||r w_R D^k f_m||2
       <=R^(2mu)2^(k/2)sqrt(pi)|e_m| A_(m,k) D_m, k>=0,

for k<=4. For example the squared u powers after the measure are k-1 for the first estimate and k-2 for the second, hence nonnegative. For the last estimate use w_R<=R^(2mu)u^mu; its squared u power is k. All remaining t powers are nonnegative. Also omega2<=4^(2/5)u^(-2/5). These facts justify dropping the remaining factors by1, including at the endpoints.

Every f_m is centrally odd. The parity Hardy inequality gives L_R(h)<=||r w_R h||2 for it and for Delta f_m. Taking a trace costs at mostsqrt(2), so

    E_R(f_m-Delta f_m)
      <=sqrt(pi)|e_m|D_m [
          4^(2/5)(2A_(m,2)+4sqrt(2)A_(m,4))
          +2^11(sqrt(2)A_(m,1)+4A_(m,3))
          +2^(53/2)R^(2mu)(1+2sqrt(2)A_(m,2)) ].       (1)

The use of a sum of the three components, rather than their Euclidean combination, only enlarges the bound.

## 4. Bessel regularization and the complete norm

For0<tau<=2, the positive Bessel kernel of J^-tau=(1-Delta)^(-tau/2) is the heat mixture with gamma time parameter tau/2. Each radial moment of order0 through4 is at most the corresponding moment of J^-2. This follows either by the gamma convolution identity, with a nonnegative independent gamma time of parameter1-tau/2 added, or directly by integrating the beta identity. Thus

    integral(1+|z|)^4 b_tau(z) dz <=89+20pi<152.

The weight ratios for omega1, omega2, w_R and <r>w_R are all bounded by(1+|z|)^4. The weighted L2 norm of J^-tau is therefore at most152 for these weights. The exact divergence decomposition in16_weighted_fractional/SHARP_LOW_COMMUTATOR_PROOF.md, section4, then gives

    L_R(J^-tau h)<=(1+4mu)152 L_R(h)<821 L_R(h).

The derivatives commute with this convolution, so E_R(J^-tau h)<=821 E_R(h). This is a bounded operator on the same compact parity completion; it does not use translation invariance of the weighted negative norm.

Taking tau=2-s yields J^s f=J^-(2-s)(f-Delta f). Consequently, for every0<s<=1/2,

    N_(s,R)(f)<=821 sum_m E_R(f_m-Delta f_m),             (2)

with each summand bounded by(1). All terms are explicit algebraic expressions in the exact exponent and leading coefficients, except positive square roots and fixed positive powers, which can be enclosed by ball arithmetic.

## 5. Scope

The functions just constructed retain smooth parity, center compatibility, the fixed leading residual coefficient, all earlier cancellations, and the finite degree/power restrictions used in the uniform Route U obstruction. Their coefficients have not been shown to arise from (cX+U[rho]).D rho-rho. The nonlinear realizability constraint is therefore essential to any stronger weighted exclusion. Neither a low residual IPM reference nor an exact IPM solution follows from this construction.
