# A triangular repair of the primitive thermal residual through degree four

Status: standalone informal argument written before implementation; symbolic Cartesian and rational controls passed. Written review183 by actual claude-opus-5-5 CONFIRMED the local algebra and triangular repair. Earlier178 and180 supplied no written audit. Restricted local trial-space construction only.

## Statement

The convention is exactly that of PROMPT.md: grad_perp Psi=(-Psi_y,Psi_x), Omega=-DeltaPsi and curl V=-Omega. The canonical relative kernel is K(z)=(z2,-z1)/(2pi|z|²), used as K(X-Y)-K(-Y). No sign change of temperature or a0 is made. Independent Cartesian and inverse controls use this same convention.

Let beta>2, a0 nonzero and Psi be a smooth stream on R², odd in x. Define

    Omega=-Delta Psi,
    V=(-Psi_y,Psi_x)-(-Psi_y(0),Psi_x(0)),
    W=beta(x,y)+V,
    F=W.grad Omega+Omega,
    Theta(x,y)=integral_0^x F(u,y) du,
    RT=W.grad Theta-(beta-2)Theta.

Assume Psi_xy(0)=c=1+beta/2 and Omega_x(0)=b0=4a0/beta. Write lambda1=(beta-2)/2 and lambda2=(3beta+2)/2. Let R=sqrt(1+x²+y²), and set

    K4=x y³ R^-8, K50=x^5 R^-8, K52=x y^4 R^-8.            (1)

There is a unique sequential addition e K4+f K50+h K52 which makes every coefficient of RT through total degree4 vanish, while preserving the center data. The correction is computed by:

    e=[x²y]RT / (3 lambda2 (2beta+1));                      (2)

recompute RT after adding e K4, and set

    f=[x^4]RT / (10 lambda1 (3lambda1+1)),
    h=[x²y²]RT / (12 lambda2 (lambda1+2lambda2+1)).          (3)

Then add f K50+h K52. The brackets in (2) and (3) are Taylor coefficients, not derivatives. Every denominator is nonzero for beta>2. The correction and its derivatives decay polynomially at infinity. In particular it preserves both leading stream coefficients p,p1 of packet130 and their two primitive moments. It introduces no free exterior harmonic field or velocity gauge. It preserves smoothness and x parity; it need not preserve off-center signs or any higher residual coefficient.

## Complete coefficient calculation

The terms of Psi through degree5 are

    Psi=l x+c xy+p3 x³+q xy²+d x³y+e0 xy³
                +f0 x^5+g x³y²+h0 xy^4+O(|X|^6).           (4)

The letters e0,f0,h0 are coefficients before correction. Subtracting the center velocity removes l. Put

    b0=-6p3-2q,
    b1=-6d-6e0,
    b20=-20f0-2g,
    b02=-6g-12h0.

Then Omega=b0 x+b1 xy+b20 x³+b02 xy²+O(|X|^4). The transport components needed here are

    W1=lambda1 x-2q xy-d x³-3e0 xy²+O(|X|^4),
    W2=lambda2 y+3p3 x²+q y²+3d x²y+e0 y³+O(|X|^4).

Differentiating Omega and collecting F yields

    [x]F=(lambda1+1)b0=2a0,
    [xy]F=(2beta+1)b1-2q b0,
    [x³]F=(3lambda1+1)b20-d b0+3p3 b1,
    [xy²]F=(lambda1+2lambda2+1)b02-q b1-3e0 b0.           (5)

Only stream terms through degree5 enter these coefficients: two derivatives form Omega, and W vanishes at0, so taking its transport does not lower the total degree further. Horizontal integration gives

    Theta=a0 x²+a1 x²y+a20 x^4+a02 x²y²+O(|X|^5),
    a1=[xy]F/2, a20=[x³]F/4, a02=[xy²]F/2.

Direct multiplication now gives all possible nonzero RT coefficients through degree4:

    [x²y]RT=lambda2 a1-4q a0,
    [x^4]RT=2lambda1 a20-2d a0+3p3 a1,
    [x²y²]RT=2lambda2 a02-6e0 a0-3q a1.                  (6)

The degree2 coefficient vanishes by 2lambda1=beta-2. No other monomial is possible: Theta and RT are even in x and divisible by x², and W(0)=0. Equations (5)-(6) prove that increasing e0 by delta changes the degree3 coefficient by -3lambda2(2beta+1)delta. Thus (2) annuls it. The local expansion K4=xy³+O(|X|^6) shows that this correction changes no other coefficient of Psi through degree5. It can change the two degree4 residuals through b1 and e0, which is why they are recomputed.

After the e0 correction, increasing f0 changes a20 by -5(3lambda1+1)delta, hence [x^4]RT by -10lambda1(3lambda1+1)delta. It changes neither the degree3 nor the x²y² residual. Increasing h0 changes a02 by -6(lambda1+2lambda2+1)delta, hence [x²y²]RT by -12lambda2(lambda1+2lambda2+1)delta. It changes neither of the other two residuals. Since K50=x^5+O(|X|^7), K52=xy^4+O(|X|^7), (3) proves the assertion and uniqueness. A second application gives exactly zero corrections.

## Canonical inverse, tail and scope

Each K is smooth and odd in x. Its first three derivatives at0 are zero, so gradPsi(0), Psi_xy(0) and Omega_x(0) are unchanged. K4=O_symbol(r^-4), K50,K52=O_symbol(r^-3). Their velocities decay at least as r^-4 and their vorticities at least as r^-5, with corresponding derivative bounds. The whole-plane once-subtracted Biot-Savart integral therefore converges. Its relative velocity agrees with grad_perp K-grad_perp K(0): their difference is an entire sublinear harmonic vector field vanishing at0, and growing-ball gradient estimates make it zero. Thus the rational stream correction is a change of the vorticity, with its own canonical full-plane velocity, not an appended harmonic strain.

For beta>2 both r^(2-1/beta) and r^(2-2/beta) grow at positive powers. The corrections decay and hence leave their coefficients and the two moments of packet130 unchanged. The proof concerns finite Taylor coefficients only. It neither solves the global thermal equation nor shows that a nearby B2 profile exists. Higher local obstructions, far-field remainders, symmetry axes, canonical inverse errors and independent residual tests remain necessary. The factor lambda1 in (3) becomes small as beta approaches2; no uniform conditioning as beta decreases to2 is claimed.

Dependencies: smooth Taylor calculus, the exact horizontal primitive definition, and the once-subtracted inverse uniqueness argument. Coefficients may be rationally certified when beta and the input jet are rational. Independent symbolic Cartesian controls passed. Written model review183 CONFIRMED the displayed calculation and scope.

Written UTC: 2026-10-21T05:55:55.130808+00:00
