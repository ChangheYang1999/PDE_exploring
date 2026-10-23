# Independent audit of exported nodal stream data

Written before code, 2026-10-21 UTC. This result concerns the unique polynomial interpolating the explicitly exported binary64 Lobatto nodes and binary64 stream values. It does not replace the canonical inverse of the saved smooth density.

## Statement and exact data convention

Let t_i be distinct nodes with t_0=-1 and y_i the values of a stream mode. Parse each repr(float64) as the exact rational value of its round-tripped binary64 number. There is a unique polynomial P of degree at most N through these N+1 data. Endpoint derivatives of this polynomial can be computed by the recurrence below without any producer implementation. At finite precision, agreement at two precisions is supporting numerical evidence, not an interval enclosure. P(-1)=y_0 itself is exact.

The map and stream are

    r^2=L^2 sigma 2^(-2 kappa) (1-sigma)^(-2 kappa),
    psi_n=r^2(1-sigma)P_n(2sigma-1)sin(n theta), n=2m.

Smoothness at zero requires P_n^j(-1)=0 for 0<=j<=m-2, as proved in the parent result107. A single nonzero required coefficient refutes exact smoothness of this literal interpolant. This statement does not classify its size relative to floating-point error, or diagnose the limiting density.

## Barycentric Taylor recurrence

Put h_i=t_i+1 for i>0, w_i=1/product_(j!=i)(t_i-t_j), b_i=w_i/w_0. For delta=t+1, the exact polynomial identity is

    P(-1+delta)=[y_0+delta sum_(i>0) b_i y_i/(delta-h_i)]
                 /[1+delta sum_(i>0) b_i/(delta-h_i)].

This follows by dividing the usual Lagrange representation by its denominator: the barycentric formula agrees at every node, hence equals the interpolating polynomial. Expanding 1/(delta-h_i)=-sum_(k>=0)delta^k/h_i^(k+1) in a disc smaller than the first node spacing gives

    d_j=-sum_(i>0) b_i/h_i^j,
    n_j=-sum_(i>0) b_i y_i/h_i^j,
    p_0=y_0,
    p_j=n_j-sum_(l=1)^j d_l p_(j-l), j>=1.

Here P(-1+delta)=sum p_j delta^j and P^(j)(-1)=j! p_j. The recurrence is exact; finite truncation does not affect lower coefficients. Products and sums are evaluated independently using Decimal arithmetic at two precisions. Manufactured polynomials with known Taylor coefficients and independently generated nodes test the recurrence and ordering.

## Physical coefficients and transparent conditional cleaning

Let A=2^(2kappa)/L^2. Series inversion gives sigma=A r^2-2kappa A^2 r^4+O(r^6). Therefore the physical radial coefficients of psi_n are

    v_2=P_n(-1),
    v_4=A(2P_n'(-1)-P_n(-1)),
    v_6=A^2[2P_n''(-1)-(4kappa+2)P_n'(-1)+2kappa P_n(-1)].

Literal nonzero v_2 at n>=4 gives a nonsmooth quadratic stream. The saved density has rho=ay+O(r^3), hence the nonpolynomial linear residual contribution is a partial_x of those quadratic modes. For a general r^q sin(n theta),

    partial_x(r^q sin(n theta))
      =r^(q-1)[(q+n)sin((n-1)theta)+(q-n)sin((n+1)theta)]/2.

For any finite set of nonzero forbidden modes, the highest mode contributes a nonzero highest residual frequency, so the leading nonsmooth term cannot vanish through cancellation. The literal raw residual thus fails C1, and its ordered D2 norm has logarithmic divergence, if any forbidden quadratic stream coefficient is nonzero. These coefficients may be at roundoff scale and must be reported as such.

As a separate diagnostic, suppose P_n(-1) is subtracted from each mode n>=4. This is an explicitly changed interpolant; it is not silently substituted for the export. Then forbidden quartic coefficients at n>=6 are v_4=2A P_n'(-1). Their cubic residual has coefficients s_j obtained by the displayed derivative identity with q=4 and multiplication by a. Result107 gives the D4 log coefficient pi sum_j [(j^2-9)(j^2-1)]^2 s_j^2. Frequencies j=1,3 vanish in this formula automatically.

If the entire required lower Taylor part is also removed, so P_n'(-1)=0 for n>=6, the forbidden sextic coefficients at n>=8 are v_6=2A^2 P_n''(-1). Result115 gives the D6 log coefficient pi sum_j [product_(h=0)^5(j+5-2h)]^2 s_j^2, with the derivative identity now q=6. This second changed-interpolant diagnostic shows what a first-derivative-only test misses. It is not the total sextic residual of the original export, whose lower nonpolynomial terms interact with higher density jets.

## Scope and checks

The raw endpoint values alone decide literal exact smoothness. The independent numerical derivative calculation measures the larger endpoint defects and validates or refutes quoted producer numbers. It checks required orders only through the stated finite cutoff; it cannot prove all-order regularity from small numbers. Actual exported nodes differ slightly from ideal cosine nodes, so the reported object is the interpolation at the supplied rounded nodes. Tiny differences near roundoff are not interpreted as a solver defect. The whole-plane canonical residual norm of the smooth Q density remains a different, finite quantity.
