# A smooth decaying field with small momentum residual and persistent strain

Status: CONFIRMED in A505 as a smooth non-profile with the stated residual estimates. It is not a counterexample to exact Euler or to any class of proof methods using exact momentum.

## 1. Exact statement

Fix 0<c<1, any finite real omega, and lambda>=1. There are U,P in C-infinity(R3), with U vector valued, such that, with A=cI-omega J, G=DU, W=curl U and e(y)=Ay/|Ay| for y!=0,

    div U=0, sup|DU|<infinity,
    U=O(r^-3), W=O(r^-2),
    -Delta P=tr((DU)^2), grad P=O(r^(-5/3)),
    R=(1-c)U+DU(Ay+U)+omega JU+grad P=O(r^(-5/3)),
    r(|Ge|+|W.e|)->0.                                      (1)

Nevertheless, for every z>=2,

    G(0,0,z)=diag(lambda,-lambda,0),
    (DR)11(0,0,z)-(DR)22(0,0,z)=2lambda.                    (2)

The positive axis is an outgoing characteristic of B=Ay+U. Thus the full gradient does not tend to zero, and R is not identically zero. Constants may depend on the fixed c,omega,lambda and cutoffs. No assertion of an exact or approximate formal solution beyond (1) is made.

## 2. Smooth cusp construction

Let sigma(t)=exp(-1/t) for t>0 and zero for t<=0. Define

    eta(t)=sigma(-t)/(sigma(-t)+sigma(t+1)),
    chi(z)=sigma(z-1)/(sigma(z-1)+sigma(2-z)).

The denominators are positive. These are smooth, with eta=1 for t<=-1, eta=0 for t>=0, chi=0 for z<=1 and chi=1 for z>=2. Put rho=sqrt(x^2+y^2), and for z>1,rho>0 set

    tau=log(rho z^3)/z^2,
    h(rho,z)=eta(tau), psi=lambda chi(z) x y h(rho,z),
    U=(partial_y psi,-partial_x psi,0).                      (3)

At rho=0 set h=1, and for z<=1 set psi=0. On every neighborhood of a finite point of the axis with z>1, h is identically one close enough to the axis. For z near one, this core radius has a positive local lower bound, so there is no corner singularity at (rho,z)=(0,1). Flatness of chi and eta gives smoothness at all other interfaces. Therefore U is smooth globally and divergence free by commuting mixed derivatives. Its support is in z>1,rho<z^-3.

On the transition region for z>=2, -1<=tau<=0 and

    tau_rho=1/(z^2 rho), tau_z=3/z^3-2tau/z.

Consequently

    |rho h_rho|+|rho^2 h_rhorho|<=Cz^-2,
    |h_z|<=Cz^-1, |partial_z(rho h_rho)|<=Cz^-3.

Differentiating (3) gives

    |U|<=C rho, |D_(x,y)U|<=C, |partial_z U|<=C rho/z.        (4)

On the support at large radius, rho<=z^-3 and r is comparable to z. Compact regularity handles the remaining region, proving bounded DU and the claimed velocity rate.

The vertical vorticity is

    W3=-lambda chi(z) (xy/rho^2)
          [eta''(tau)/z^4+4eta'(tau)/z^2].                  (5)

Indeed Delta_(x,y)(xy h)=xy(h_rhorho+5h_rho/rho). The expression vanishes near the axis and has a smooth interpretation there. The horizontal vorticity is (-partial_z U2,partial_z U1), with size C rho/z. Hence W3=O(z^-2) and the horizontal part is O(z^-4), proving W=O(r^-2).

For z>=2 and rho<z^-3 exp(-z^2), h=1 and U=(lambda x,-lambda y,0). This gives the first equality of (2).

## 3. Directional estimates

On the large cusp |e-e3|<=C rho/z since c>0. Equation (4) implies |Ge|<=C rho/z. Equation (5) and the horizontal vorticity estimate give |W.e|<=C(z^-2+rho^2/z^2). Multiplication by r, comparable to z, proves the limit in (1). Outside the support these derivatives vanish.

The third row of G is zero, so |G^T e|<=C rho/z as well. Thus the projected shear Pi_e G^T e tends to zero. Also

    |GAy|<=|D_(x,y)U| |(Ay)_(x,y)|+cz|partial_z U|
           <=C rho.                                       (6)

These are additional direct estimates; no exact Euler consequence is used.

## 4. A genuine Newtonian pressure with small gradient

Let f=tr(G^2). It is smooth, bounded and supported in the cusp. Its absolute tail mass is bounded by

    integral_(|xi|>R)|f(xi)|dxi <= C integral_(R/2)^infinity z^-6 dz
                               <= C R^-5.                 (7)

Thus f is in L1 and L-infinity. Define the ordinary convergent potential

    P(y)=(1/(4pi)) integral f(xi)/|y-xi| dxi.                (8)

Its local singularity is integrable, and its tail converges against L1 f. Splitting off a smooth compactly supported localization around each point proves local smoothness; derivatives of the remaining kernel may be passed under the integral. Thus P is smooth and -Delta P=f exactly.

For any q in L1 intersect L-infinity, splitting the gradient kernel at distance a gives

    |grad(-Delta)^(-1)q(y)|<=C[a||q||infinity+a^-2||q||1]
                           <=C||q||infinity^(2/3)||q||1^(1/3).

At |y|=r, split f into |xi|<r/2 and its complement. The inner contribution to grad P is O(r^-2). Equation (7) and the last estimate bound the outer contribution by O(r^-5/3). This proves the pressure-gradient bound uniformly in direction. Equations (4),(6), bounded G and this pressure estimate give the stated residual bound in (1).

## 5. A nonvanishing derivative of the residual

In each open linear core, write D=diag(lambda,-lambda,0). Since DG=0 there,

    DR=D+omega(JD-DJ)+D^2+D^2P.                             (9)

To check the coefficient, differentiate LU+G(Ay+U): LG+GA+G^2=G+omega(JG-GJ)+G^2. There is no missing factor c.

Let Q rotate the horizontal plane by pi/2. The stream function obeys psi(Qy)=-psi(y), so U(Qy)=-Q U(y). Differentiating gives G(Qy)=-QG(y)Q^T and therefore f(Qy)=f(y). The radial Newtonian kernel preserves this symmetry, giving P(Qy)=P(y). On the fixed axis, the Hessian has P11=P22. In (9), the commutator has zero diagonal and the first two entries of D^2 are equal. Their residual difference is exactly 2lambda, proving the second equality of (2). In particular ||DR||op>=lambda there.

On the positive axis U=0 and Ay=(0,0,cz), so z'=cz is its exact carrier equation. This proves persistent strain along the entire outgoing axis without asserting that the surrounding cusp is a material tube.

## 6. What the construction does and does not refute

The construction refutes any implication from the explicit properties in (1), with merely R->0, to DU->0. It retains smoothness, bounded gradient, fast velocity decay, decaying vorticity, the exact pressure Poisson equation and the displayed directional limits.

It does not satisfy R=0. Therefore it does not rule out an argument using the exact undifferentiated momentum equation. In particular, the statement 'every proof must use exact vorticity transport' does not follow from this example. Exact testing of momentum could capture information not controlled by the C0 size of R. A precise conclusion is: the listed pointwise asymptotic estimates, Poisson identity and a uniformly vanishing residual are insufficient. No impossibility theorem for all proof methods is claimed.

The full original source and the complete configured-model coordinator check were read. The inner source consultation failed, followed by the separate coordinator review; no model substitution or successful failed call is asserted. Every displayed identity above was derived directly. The source's optional symbolic check was not rerun because this analytic reconstruction is sufficient and no numerical claim is being made.
