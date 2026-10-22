# The next vorticity jet does not restrict the simple-endpoint constructions

Status: complete informal proof written before symbolic controls. This is a local finite-jet statement only.

## Statement

Take any real analytic local functions b,T,eta,v,D constructed in P299, at fixed beta>0, chosen orientation epsilon, q in {0,1}, and constants C!=0,ell. Use the signed coordinate s=epsilon(y_*-y), c=3beta+2. In particular

    b=epsilon B, B=s(c+x(s)), B'=c+z(s),
    T=s^3g, eta=s^3h, v=s^(4-q)w, D=ell s^(6-q)g^2,

where x,z,g,h,w are analytic, x(0)=z(0)=0, g(0)=C, and B'=dB/ds. These functions satisfy the four relations

    b T_y+(3beta+2-2b_y)T=0,
    b eta_y+(2beta+1-b_y)eta=T,
    eta=-b_yy-2v,
    b D_y+(7beta+2-4b_y)D=8v_yT-12vT_y.             (1)

There is an analytic gamma, vanishing to order at least m=6-q at s=0, such that

    b gamma_y+(6beta+1-3b_y)gamma
       = D+2v_y eta-6v eta_y.                       (2)

It is unique among analytic gamma of order at least m. Defining p_5=-gamma-2v_yy then supplies the next Poisson jet, gamma=-p_5-2v_yy. Thus this next vorticity equation does not restrict beta,C,ell or the extended ratio limit already attained by P299. No full hierarchy or canonical inverse is asserted.

More concretely, these data admit local parity-compatible analytic polynomials in the horizontal variable whose Poisson equation is exact and whose thermal and vorticity residuals vanish through horizontal orders four and three, respectively. This is not a local exact B2 solution: the untested higher coefficients may be nonzero.

## Derivation of the fifth relation

Write the local stream function and temperature jets as

    Psi(x,y)=h_0(y)x + v(y)x^3/3 + p_5(y)x^5/120 + O(x^7),
    Theta(x,y)=T(y)x^2/2 + D(y)x^4/24 + O(x^6).

Set Omega=-Delta Psi. Then Omega=eta x+gamma x^3/6+O(x^5), with eta=-h_0''-2v and gamma=-p_5-2v_yy. Let h_0'=b_y-beta, so the relative transport jets are

    W_1=(2beta-b_y)x - v_y x^3/3 + O(x^5),
    W_2=b+v x^2+O(x^4).

The coefficient of x^3 in W.grad Omega+Omega-Theta_x, multiplied by six, is

    b gamma_y+(6beta+1-3b_y)gamma-2v_y eta+6v eta_y-D.

This is (2). Its coefficient of x is the second relation of (1). The thermal residual coefficients of x^2 and x^4 are exactly the first and fourth relations of (1), divided by two and 24, respectively. This derivation is algebraic and introduces no full-plane inverse.

## Analytic solution of the next equation

Since d/dy=-epsilon d/ds and b_y=-B', equation (2) is

    B gamma'-(6beta+1+3B')gamma
      = -D+2epsilon v' eta-6epsilon v eta'.         (3)

The right side has order at least m=6-q: D has that order, v'eta has order at least (3-q)+3, and v eta' has order at least (4-q)+2. Divide (3) by c+x(s), which is nonzero near zero. This gives

    s gamma' - a(s) gamma = f(s),
    a(s)=(6beta+1+3(c+z(s)))/(c+x(s)),
    f(s)=(-D+2epsilon v'eta-6epsilon v eta')/(c+x(s)). (4)

Both a and f are analytic, f=O(s^m), and

    a_*=a(0)=3+(6beta+1)/c=5-3/c <5 <= m.          (5)

The strict inequality holds for every finite beta>0. Define the analytic nonvanishing function

    E(s)=exp(integral_0^s (a(t)-a_*)/t dt), E(0)=1.

The integrand has a removable singularity because a is analytic. In a sufficiently small complex disk, expand f/E=sum_{j>=m} f_j s^j. The series

    gamma(s)=E(s) sum_{j>=m} f_j s^j/(j-a_*)       (6)

converges on every smaller disk: each denominator is at least m-a_*>0 and the numerator series is analytic. Differentiating the convergent series gives s gamma'-a(s)gamma=f(s), because sE'/E=a(s)-a_*. Its real coefficients ensure that gamma is real on the real axis.

If two analytic solutions both vanish to order at least m, divide their difference by E. Its Taylor coefficients u_j would satisfy (j-a_*)u_j=0 for j>=m. Every denominator is positive, so the difference is zero. This proves existence and the stated uniqueness without excluding exceptional beta for which a_* is an integer below m. For example beta=1/3 gives a_*=4 and an analytic homogeneous solution s^4 E, excluded by the required order m>=5. Such lower-order homogeneous terms are irrelevant to this constructed solution.

## Local finite-jet realization and scope

Choose an arbitrary constant u_* and set h_0(y)=b(y)-beta(y-y_*)+u_*. Use the finite polynomials

    Psi=h_0 x+v x^3/3+p_5 x^5/120,
    Theta=T x^2/2+D x^4/24,
    Omega=-Delta Psi,
    U=(-Psi_y,Psi_x),
    W=beta(x,y-y_*)+U-(0,u_*).

Then U(0,y_*)=(0,u_*), b(y_*)=0, and W has the jets used above. Omega and Psi are odd in x, while Theta is even and vanishes on x=0. The Poisson equation is exact locally by definition, and the four relations (1) and the new relation (2) imply

    W.grad Theta-(beta-2)Theta=O(x^6),
    W.grad Omega+Omega-Theta_x=O(x^5),

uniformly for y on a compact subinterval of the analytic neighborhood. The big-O statements refer to x tending to zero. They are finite Taylor cancellations, not small residual claims on a macroscopic region. At the endpoint T(y_*)=0, so this point is not the nonzero-temperature-jet material center required by the main prompt. Its use here is only the local endpoint of an axis component.

No claim identifies the local polynomial inverse with a canonical full-plane Biot-Savart operator. No global extension, far-field behavior, full hierarchy, a0 normalization or exact stationary profile follows. Every extended ratio limit from P299 persists through this additional finite-jet test; the general B2 question remains OPEN.

## Dependencies and verification

P299 supplies the analytic data and its explicitly displayed four relations; its complete proof is at ../299_simple_endpoint_all_limits/PROOF.md. The current packet proves (2) and the finite polynomial realization independently. Symbolic differentiation controls and the source hash of P299 belong in verification/. No Lean or Lake build is performed or claimed.
