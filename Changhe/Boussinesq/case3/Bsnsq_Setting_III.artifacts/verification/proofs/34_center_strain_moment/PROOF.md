# The center strain identity and its correct polar temperature moment

Date:2026-10-20. Status: CONFIRMED by independent differentiation and the full argument below; external review pending. This is a necessary identity, not a nonexistence theorem.

## Exact statement and hypotheses

Let beta>0. Let Omega,Theta,V be smooth on R2 with V(0)=0, div V=0, -curl V=Omega, and W=beta X+V. Assume

    W.gradOmega+Omega=Theta_x,
    Omega(-x,y)=-Omega(x,y), Theta=x^2 F(x,y) near0 with F smooth,
    |Omega(X)|<=C r^(-delta), |V(X)|<=C r^(1-kappa),
    |Theta(X)|<=C r^m, |Theta_x(X)|<=C r^(-sigma)   for r>=1,

where delta,kappa,sigma>0 and m<1. Suppose V is the canonical relative Biot-Savart inverse, with K(Z)=(Z2,-Z1)/(2pi|Z|^2). Set

    c=-partial_x V1(0)=Psi_xy(0),
    phi(X)=xy/(pi r^4).

Then all terms below are absolutely convergent and

    c=Lambda+NL,
    Lambda=integral phi Theta_x dX
          =(1/pi)integral Theta(X) sin(3theta)/r^3 dX,
    NL=integral Omega V.grad phi dX.                     (1)

Here theta is the polar angle from the positive x-axis, and dX is plane area measure. In radial-angular measure the Lambda integral is (1/pi)integral Theta(r,theta)sin(3theta) r^(-2) dr dtheta. The distinction between dX=r dr dtheta and dr dtheta accounts for the error being corrected.

The conditions follow for exact class A profiles from the confirmed derivative bootstrap33 and its gradient-transport consequence. The present identity is proved under the displayed hypotheses and also stands independently under those explicit hypotheses. Temperature positivity is not assumed. For B2 with a0=1, the additional center jet relation gives c=1+beta/2.

## Center kernel and convergence

The inverse derivative at0 has ordinary kernel

    -partial_{X1}K1(-Y)=Y1 Y2/(pi |Y|^4)=phi(Y).

Its distributional local delta term has zero coefficient in this off-diagonal Hessian component; alternatively Omega(0)=0 would annihilate it. Because Omega is odd in x and smooth, Omega=O(r) at0. Thus phi Omega=O(r^-1) locally, which is integrable in two dimensions. At infinity it is O(r^-2-delta), also integrable. Differentiating the inverse in distributions, or first removing a small disk and passing to the limit, gives

    c=integral phi Omega dX.                             (2)

Near0, Theta_x=O(r), V=O(r), and grad phi=O(r^-3). Thus phi Theta_x and Omega V.grad phi are both O(r^-1). At infinity their respective bounds are O(r^-2-sigma) and O(r^-2-delta-kappa). The rewritten temperature integrand is O(r^-1) near0 and O(r^(m-3)) at infinity. These are all absolutely integrable under the stated exponents.

## Testing the vorticity equation

Integrate over the annulus epsilon<r<R. The boundary term from phi W.gradOmega is integral phi Omega W.n dS. It is O(epsilon) on the inner circle, since W=O(r), and O(R^-delta) on the outer circle. Both vanish in their limits. Since div W=2beta and X.grad phi=-2phi,

    integral phi W.gradOmega dX
      =-integral Omega[W.grad phi+2beta phi]dX
      =-integral Omega V.grad phi dX=-NL.

The vorticity equation now gives -NL+c=Lambda, proving the first equality in(1).

## Integrating the temperature term

A second integration by parts on the same annuli has boundary term integral phi Theta n1 dS. This is O(epsilon) near0 and O(R^(m-1)) at infinity, so it vanishes. Direct differentiation gives

    -partial_x phi
       =y(3x^2-y^2)/(pi r^6)
       =sin(3theta)/(pi r^3).                            (3)

Indeed y(3x^2-y^2)=r^3[3sin(theta)cos(theta)^2-sin(theta)^3]=r^3 sin(3theta). Formula(3) proves the second equality in(1). The Cartesian expression in the numerics lane's note10 was correct; its conversion to sin(3theta)/r^2 with dX was not.

## Exact manufactured temperature

Take Theta=x^2(1+a y)exp(-r^2/L^2), with L>0 and a real. No transport or vorticity equation is claimed for this manufacture. It tests only the second integration by parts and the radial power. The odd part in y alone contributes. Elementary polar Gaussian integrals give

    integral phi Theta_x dX
      =(2a/pi)[(pi/4)(L^2/2)-(pi/8)(L^2/2)]
      =a L^2/8.

For the second term inside the brackets, the factor x^2/L^2 in Theta_x contributes radial integral (1/L^2)integral r^3 exp(-r^2/L^2)dr=L^2/2. The correct polar expression yields the same value using integral cos(theta)^2 sin(theta)sin(3theta)dtheta=pi/4. The erroneous expression would instead give

    (1/pi)integral Theta sin(3theta)/r^2 dX
       =a L^3 sqrt(pi)/16,

which disagrees except at an accidental choice of L. Multiple radial scales distinguish the formulas.

## Scope and dependencies

This is a global necessary identity with explicit convergence hypotheses. It supplies no sign or magnitude bound for Lambda+NL, and does not exclude B2. The assertion Theta>=0 for beta>2 holds on the backward basin of the normalized source under the established transport argument; no global positivity assumption is added here. The proof uses only direct kernel differentiation, annular integration by parts, elementary polar algebra and Gaussian integrals. No formalization is claimed.
