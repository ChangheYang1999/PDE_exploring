# Modal finite energy parts and helicity transfers

Audit A214. Written: 2026-11-02T22:00:53Z. Status: CONFIRMED.

## Statement and hypotheses

Let U,P be a real C^2 rotating Euler profile, with U tending to zero uniformly, 2/5<c<1/2, and any finite omega. Let u_m be the angular vector modes in the rotation-covariant convention, w_m=curl u_m, N_m the same projection of (U.grad)U, and Pi_m the pressure modes. Thus

    (1-c-im omega)u_m+c(y.grad)u_m+N_m+grad Pi_m=0,
    div u_m=0.

Assume |D^j U(y)|<=C(1+|y|)^(-alpha-j), j=0,1,2, where alpha=(1-c)/c in (1,3/2). Put s=3-2alpha=5-2/c>0 and kappa=1-5c/2=-cs/2<0. After subtracting the constant zero-mode pressure, Pi_m=O(|y|^-1). Define

    tau_m=-Re integral conjugate(u_m).N_m,
    chi_m=-Re integral N_m.conjugate(w_m),
    H_m=integral u_m.conjugate(w_m).

These integrals are absolutely convergent, H_m is real, the tau and chi series are absolutely summable and each sums to zero. There are L_m>=0 such that

    integral_(B_R)|u_m|^2=L_m R^s+tau_m/kappa+O(R^(1-alpha)),
    (1-2c)H_m=chi_m,
    lim_R [c Im integral_(B_R) conjugate(u_m).(y.grad)u_m
           -m omega integral_(B_R)|u_m|^2]
      =-Im integral conjugate(u_m).N_m.

If the only possible modes are +/-1 and +/-2, put a=u_1, b=u_2, eta=curl a, zeta=curl b,

    Z=integral ((a.grad)a).conjugate(b),
    Y=integral ((a.grad)a).conjugate(zeta).

Then tau_1=Re Z=-tau_2, chi_1=Re Y=-chi_2, both imaginary limits equal -Im Z, and L_1+L_2>0 unless U=0. Without the extra derivative decay, but retaining U->0 and 0<c<1/2, vanishing of either a or b forces U=0.

## Pressure and summation

The mode projections preserve the indicated pointwise radial bounds. The mode equation gives grad Pi_m=O(r^-alpha). Integrating along rays gives finite pressure limits; comparison along sphere arcs shows the limits agree. A nonzero angular mode has limit zero by equivariance; subtract the common zero-mode limit. The Poisson source -div N_m is bounded and O(r^(-2alpha-2)), hence integrable. Its Newton potential tends to zero and is O(1/r), by splitting into |z|<r/2, |z-y|<r/2 and the remaining region. The difference from Pi_m is entire harmonic and tends to zero, so vanishes.

The tau and chi integrands are O(r^(-3alpha-1)) and O(r^(-3alpha-2)), respectively. Parseval on the rotation orbit through y gives sum_m |u_m(y)|^2<=C(1+r)^(-2alpha), and analogous estimates for N_m and w_m. Cauchy-Schwarz in m and then integration show absolute summability, so summation and volume integration commute. Mode orthogonality on a ball gives

    sum_m integral_(B_R) conjugate(u_m).N_m
       =integral_(S_R) (|U|^2/2)U.n,
    sum_m integral_(B_R) N_m.conjugate(w_m)
       =integral_(S_R) (|U|^2/2)W.n.

These are O(R^(2-3alpha)) and O(R^(1-3alpha)), both tending to zero. This proves the two sum rules. Infinite angular support causes no additional convergence assumption.

## Energy finite parts and the imaginary identity

Pair the mode equation with conjugate(u_m), integrate on B_R, and take real parts. With E_m(R)=integral_(B_R)|u_m|^2 one obtains

    (cR/2)E_m'+kappa E_m
       =tau_m(R)-Re integral_(S_R)Pi_m conjugate(u_m).n,
    tau_m(R)=tau_m+O(R^(2-3alpha)).

The pressure flux is O(R^(1-alpha)), and 2-3alpha<1-alpha. Therefore

    (R^-s E_m)'=(2/c)R^(-s-1)[tau_m+O(R^(1-alpha))].

The right side is absolutely integrable at infinity since s>0 and s+alpha>1. Integration from R to infinity gives the stated expansion and the sign L_m>=0. This proof uses absolute integrability, not a supposed monotonicity for a possibly negative tau_m. The imaginary part of the same pairing has only the dilation, rotation, nonlinear and pressure-flux terms; the last tends to zero and gives the stated limit.

## Helicity

The product |u_m||w_m|=O(r^(-2alpha-1)) is integrable because alpha>1. Integration by parts for curl has boundary O(R^(2-2alpha))->0 and proves H_m is real. Put K_m=integral ((y.grad)u_m).conjugate(w_m), which is also absolutely convergent. The identity curl((y.grad)u_m)=(y.grad)w_m+w_m and a second integration by parts give

    conjugate(K_m)=-K_m-2H_m.

All boundary terms are O(R^(2-2alpha)). Consequently Re K_m=-H_m. The pressure pairing with conjugate(w_m) has zero limit, since its boundary is O(R^-alpha). Taking the real part of the mode equation paired with conjugate(w_m) gives (1-2c)H_m=chi_m; the rotation term has zero real part because H_m is real.

## Four-mode transfer algebra

For support contained in {+/-1,+/-2},

    N_1=(b.grad)conjugate(a)+(conjugate(a).grad)b,
    N_2=(a.grad)a.

Divergence-free integration by parts gives integral conjugate(a).N_1=-conjugate(Z) and integral conjugate(b).N_2=Z. The surface errors are O(R^(2-3alpha)). For helicity use

    N_1=grad(b.conjugate(a))-b cross conjugate(eta)-conjugate(a) cross zeta.

Pairing with conjugate(eta), and using (a.grad)a=grad(a.a/2)-a cross eta, gives integral N_1.conjugate(eta)=-conjugate(Y); the mode-2 integral is Y. These are exactly the transfer relations above. If L_1+L_2=0, the finite parts cancel and E_1(R)+E_2(R)=O(R^(1-alpha))->0, forcing both modes to vanish. If one mode is absent without the derivative decay, the remaining mode solves the decaying linear mode equation, whose kernel is zero by A090; hence U=0.

## Exact local example and limitations

Let e=(1,i,0), xi=y_1+i y_2, a=e, b=xi e. With

    Pi_0=-2(y_1^2+y_2^2),
    Pi_1=-(3-c-i omega)xi,
    Pi_2=-(1-2i omega)xi^2/2,
    Pi_3=Pi_4=0,

the five nonnegative mode equations all hold. Indeed N_0=4(y_1,y_2,0), N_1=2e and N_2=N_3=N_4=0. The real field is U=(2+2y_1,-2y_2,0). Direct substitution gives the pressure

    P=-[(6-2c)y_1+3y_1^2+4omega y_1y_2+y_2^2+2omega y_2].

This example is not decaying. The finite parts tau_m/kappa have no positivity sign; divergent nonnegative energies may have either sign after their leading term is removed. Neither the balances nor this example settles the four-mode decaying-profile problem. This proves precisely Theory Agent C C22, the finite-spectrum note Section 6, without a numerical test.
