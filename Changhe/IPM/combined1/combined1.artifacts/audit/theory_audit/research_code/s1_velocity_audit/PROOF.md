# S1 improvement of the weighted IPM velocity bound

## Exact statement and dependencies

Let0<a<2. Let w(r)>0 be radial, with log w(e^t) locally absolutely continuous and0<=p(t)=-(log w(e^t))'<=a almost everywhere. Define the real Hilbert space H of functions h in L2(w^2 dx) that are even in x and odd in y. For unweighted compact smooth inputs let U be the velocity with Fourier multipliers (xi1 xi2/|xi|^2,-xi1^2/|xi|^2), extended by the bound below.

For n>=2 put K_n=(n+a)/(n-a). On l2(N_0) let M be the symmetric tridiagonal matrix

    M_00=2, M_ii=3+K_(2i)^2 (i>=1),
    M_(i,i+1)=M_(i+1,i)=1+K_(2i+2).

Then M is a bounded positive operator and

    ||w U[h]||2 <= sqrt(||M||/8) ||w h||2.                   (1)

In particular certified sufficient constants for a=6/5,13/10,7/5,3/2,19/10 are respectively1.616466,1.836267,2.142307,2.585263,13.806975. Each displayed decimal denotes the exact rational with denominator10^6.

The dependency is T4-054, independently confirmed by T1 R1-010: the conjugated future Beurling block of index n>=2 has norm at mostK_n, and each past block of positive index k has norm at most1. Those statements hold for these general weights. This audit independently reconstructs every subsequent mode and norm factor.

## Mode calculation

Set t=log r and g_i(t)=w(e^t)e^t times the radial coefficient of sin((2i+1)theta) in h. Smooth finite angular sums are dense. Thus

    ||w h||2^2=pi sum_i ||g_i||L2(dt)^2.

Write B for the complex Beurling multiplier (xi1-i xi2)^2/|xi|^2. Then U2+iU1=-(I+B)h/2. The input complex mode m=2i+1 is g_i/(2i) and the mode -m is -g_i/(2i), where the i in the denominator denotes the imaginary unit only. The Beurling operator lowers each angular index by2.

Consequently the positive output index j=2i+1 has bracket g_i+T_(2i+2)g_(i+1), divided by2i. The output index -1 vanishes exactly: the incoming positive index1 has the identity block and cancels the original index-1 coefficient. At negative output index -(2i+3), the bracket is -(g_(i+1)+P_(2i+2)g_i), again divided by2i. There are no further outputs.

Let x_i=||g_i||. Orthogonality of complex exponentials, followed by the velocity factor1/4, gives

    ||w U[h]||2^2
    = (pi/8) sum_i [||g_i+T_(2i+2)g_(i+1)||^2
                       +||g_(i+1)+P_(2i+2)g_i||^2]
    <= (pi/8) sum_i [(x_i+K_(2i+2)x_(i+1))^2
                       +(x_(i+1)+x_i)^2]
    = (pi/8) <Mx,x>.                                      (2)

The constant pi/8 includes the complex Fourier coefficient1/2, angular integral2pi, and velocity factor1/4. Expanding the two squares yields exactly the matrix above, including the exceptional diagonal2 at i=0. Its coefficients are bounded because a<2. Equation(2) both proves positivity and gives(1). Density extends U uniquely; no weighted boundedness is assumed in order to prove it.

## Infinite matrix certificate

Let v_i>0, not necessarily in l2, and suppose (Mv)_i<=rho v_i for every i. For each finite real vector z, symmetry, nonnegative entries and

    2|z_i z_j| <= (v_j/v_i)|z_i|^2+(v_i/v_j)|z_j|^2

give |<Mz,z>|<=rho||z||^2. Hence ||M||<=rho. This proves the required Schur test directly, including the constant-tail positive vectors used here.

The independent code constructs a candidate positive vector by power iteration of a64 by64 floating tridiagonal matrix. Those floating computations are only a search for rational data. The vector is rounded to denominator10^14 and a positive tail1/10^12 is added; all later checks are exact fractions. Extend by that same constant tail from index64. Check every row0 through65 exactly. For i>=66, the row ratio is

    5+K_(2i)^2+K_(2i)+K_(2i+2),

which decreases with i since K_n decreases with n. One further exact check controls the entire tail. Finally the code verifies rho<=8C^2 for each exact displayed C. It stores the positive vector and all margins in JSON, so the certificate does not depend on accepting power iteration as proof.

## Scope and independent review status

This proves T1 TP-2 and provides an independent certificate for its five rational constants. It improves the low contraction coefficient of T4-041 and supplies the velocity constant in T4-058. It does not prove the high resolvent estimate of either framework, or any candidate existence. The true optimal S1 operator norm is not claimed to equal sqrt(||M||/8); the triangle inequalities may lose sharpness. T1's floating lower estimates are not used.
