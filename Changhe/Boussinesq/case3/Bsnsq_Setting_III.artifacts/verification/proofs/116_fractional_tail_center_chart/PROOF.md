# A smooth center chart imposing the first constant-induced tail identities

Written UTC 2026-10-21T03:25:26.876437+00:00, before implementation. Status updated 2026-10-21T03:35:51.677104+00:00: algebraic construction and implementation controls CONFIRMED by own derivation and tests. Actual Opus152/153 returned no written audit, so external model confirmation is unavailable. Exploratory fits remain pending. This is a trial-space parameterization, not a profile or a nonexistence theorem.

## Statement and notation

Let 2<beta<3, s=1/beta, a0!=0, eta real, n>=3 and J>=2 integers. Set R=sqrt(1+x²+y²), t=R^-s, z=y/R. Let T_i be Chebyshev polynomials and B_i(t)=T_i(2t-1)-(-1)^i for i>=1. Thus B_i(0)=0. Define the angular operator

    L_c P=c z P+(1-z²)P'.

Choose freely polynomials P0,Q0 of degree<=J-1 in z and core coefficients of B_i(t) T_j(z), i=1,...,n-1. The shift0 core has j=0,...,J-1 and the shift1 core j=0,...,J. Put

    P(t,z)=P0(z)+sum c_ij0 B_i(t)T_j(z),
    Ptilde(t,z)=(eta/beta) L_(1-s) P0(z)
                    +sum c_ij1 B_i(t)T_j(z),
    Q(t,z)=Q0(z)+sum d_ij0 B_i(t)T_j(z),
    Qtilde(t,z)=(eta/beta) L_(-1-2s) Q0(z)
                    +sum d_ij1 B_i(t)T_j(z),
    p=x R^(1-s) [P(t,z)+R^-1 Ptilde(t,z)],
    Theta=x² R^(-1-2s) [Q(t,z)+R^-1 Qtilde(t,z)],
    Psi=p-x p_x(0), V=(-Psi_y,Psi_x), Omega=-Delta Psi.

The three stream core coefficients c_(1,0,0), c_(2,0,0), c_(1,1,0) and the temperature core coefficient d_(1,0,0) can be determined uniquely from

    p_x(0)=-eta, Psi_xy(0)=1+beta/2,
    Omega_x(0)=4a0/beta, Theta_xx(0)/2=a0.             (1)

All remaining leading and core coefficients are free. The resulting fields are smooth and have B2 parity and Theta(0,y)=0. The velocity is the canonical relative full-plane inverse with V(0)=0; its constant term after the growing homogeneous terms is (0,eta). It obeys V=o(r), and Omega has polynomial decay. Both first fractional-tail identities of packet115 are exact, for every choice of the remaining coefficients. No positivity or vorticity sign is imposed. The construction does not impose the other PDE residual coefficients or make the residuals small.

This is an affine parameterization in the free field coefficients for fixed beta and eta, with constant rank for all beta in(2,3). Its coefficient maps are affine in eta for fixed beta and fixed free coordinates. Eta is a coordinate constrained by p_x(0)=-eta, not an independently appended velocity or an arbitrary fitted material-center drift.

## Exact angular action and representation

The identities (1-z²)T_j'=j(T_(j-1)-z T_j) and z T_j=(T_(j+1)+T_(j-1))/2 for j>=1 give

    L_c T_0=c T_1,
    L_c T_j=((c+j)/2)T_(j-1)+((c-j)/2)T_(j+1), j>=1.  (2)

Thus the leading shifted polynomials have degree<=J. The one extra shifted angular degree is required to avoid setting the highest leading coefficient artificially to zero. The B_i form a basis of all radial polynomials of degree<=n-1 that vanish at t=0: subtracting the endpoint value is an invertible change from the usual Chebyshev basis with its constant coefficient separated. Hence all fields displayed are finite linear combinations of the packet114 two-shift basis, with n radial indices and J+1 angular indices, and a zero highest angular coefficient in the unshifted block.

## Center moments and fixed pivots

For an ordinary raw basis element

    p_ijd=x R^(1-s-d) T_i(2t-1) T_j(z),

write v_j=T_j(0) in{0,1,-1}, w_j=T_j'(0)=j sin(j pi/2). Since T_i(1)=1, T_i'(1)=i², t=1-s r²/2+O(r^4), z=y+O(r³), its three center moments are

    p_ijd,x(0)=v_j,
    p_ijd,xy(0)=w_j,
    (-Delta p_ijd)_x(0)=-[4(1-s-d-2i²s)-j²] v_j.      (3)

For the last formula, the radial x r² term contributes4 times its radial exponent, and T_j''(0)=-j²v_j contributes the angular second derivative. Subtracting an affine x term changes neither of the last two moments. The corresponding temperature basis has Theta_xx(0)/2=v_j. These formulas can also be obtained by expanding the functions through degree3 and degree2, respectively.

The stream pivot functions are x R^(1-s) B_1(t), x R^(1-s) B_2(t), and x R^(1-s) B_1(t)z. In the row order (p_x, Psi_xy, Omega_x), their moment matrix is

    M=[[2,0,0], [0,0,2], [-8(1-2s),32s,0]],
    det M=-128s != 0.                                  (4)

Indeed B_1=2t, B_2=8t²-8t. None of these pivots changes P0 or Ptilde(0,z), since each B_i vanishes at0. Let gamma,c,b denote the moments of the stream with these three coefficients temporarily zero. The unique corrections are

    c_(1,0,0)=(-eta-gamma)/2,
    c_(1,1,0)=(1+beta/2-c)/2,
    c_(2,0,0)=[4a0/beta-b+8(1-2s)c_(1,0,0)]/(32s).     (5)

The temperature pivot has center coefficient2 and does not affect either leading angular polynomial. If A is the current center coefficient with its pivot zero, set d_(1,0,0)=(a0-A)/2. This proves (1), uniqueness, and the constant-rank assertion. Since the angular blocks in(2) are affine in eta and the moment matrix(4) is independent of eta, formulas(5) are affine in eta as well. The two field-coordinate dimensions before eliminating pivots are each M0=J+(n-1)(2J+1). After eliminating the pivots they are M0-3 and M0-1. Including free beta and eta gives2M0-2 scalar parameters.

## Canonical inverse and asymptotic identities

Every raw factor is smooth because R>=1. It is odd in x for p and even in x for Theta. The subtraction makes Psi_x(0)=0 and parity gives Psi_y(0)=0. Derivatives of the displayed powers give Omega=O(r^-s), D Omega=O(r^-s-1), and V=O(r^(1-s))+O(1). The once-subtracted full-plane kernel for this vorticity converges absolutely at infinity and locally in its standard sense. It has the same divergence and curl as V and is zero at0. Their difference is an entire harmonic vector field of sublinear growth; the harmonic gradient estimate on growing balls makes it constant, and its value at0 is zero. Thus the constructed V is exactly the canonical relative inverse. No free harmonic or affine strain is added.

Since beta is not an integer in(2,3), no ungauged velocity term has homogeneity degree0. The sole constant term is therefore -p_x(0)=eta in the vertical component. At infinity B_i(0)=0, so the leading unshifted angular polynomials are P0,Q0 and the leading shifted ones are precisely the first terms of Ptilde,Qtilde in their definitions. Packet115's direct exponent matching shows that these are exactly the necessary first constant-induced relations:

    P1=(eta/beta)L_(1-s)P0,
    Q1=(eta/beta)L_(-1-2s)Q0.

For clarity, the associated residual coefficients vanish at degrees -1-s in the vorticity equation and -2s in the temperature equation. The unshifted nonlinear transport terms generally have nonzero coefficients at other degrees. The construction does not annul them.

## Exact serialization and verification scope

For rational beta,eta,a0 and free chart coordinates, formulas(2),(3),(5) reconstruct rational coefficients in the ordinary two-shift Chebyshev basis. Exact JSON chart inputs and their rational reconstruction suffice to check all four center conditions and both polynomial tail identities without trusting a floating-point solver flag. Floating-point coordinates can be interpreted as their exact binary rationals before this reconstruction. Rounded coefficients used during a fit need not satisfy the constraints exactly; their defects must be measured separately.

Dependencies: the elementary Chebyshev identities, smooth Taylor expansion, the canonical-inverse uniqueness argument of packets108/114, and packet115's independently written exponent-matching proof. No formal Lean proof is claimed. Finitely many angular modes still cannot give an exact admissible profile by packets83/84; this excludes exact solutions at fixed resolution, not arbitrarily accurate approximations or limits. This chart covers a specific trial family in2<beta<3, not the beta2 endpoint or beta>=3.
