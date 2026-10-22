# Enforcing the first transverse center equations in a tail-compatible chart

Written UTC 2026-10-21T04:53:29.801953+00:00 before implementation. Status: CONFIRMED by own exact/Cartesian/inverse controls 2026-10-21T05:03:32.829297+00:00; actual Opus165/166/168 supplied no written audit, explicitly recorded. This is a finite-dimensional search family, not an existence or nonexistence theorem.

## Statement and field definitions

Fix 2<beta<3, a0!=0, eta real, s=1/beta, c=1+beta/2, mu=1+3beta/2, M=2beta+1 and q0=4a0/beta. Put R=sqrt(1+x2+y2), t=R^(-s), z=y/R, k=2-s, m=1-2s and k1=2-2s. Here x2 and y2 mean squares. For a polynomial H define

    S_k H=-[(k2-1)H-3zH'+(1-z2)H''],
    L_q H=qzH+(1-z2)H',
    D_m H=[m+(2-m)z2]H-z(1-z2)H'.

Choose arbitrary leading polynomials P,Q of degree<=J-1, J>=2. With A=S_k P and R0=zP-(1-z2)P', define uniquely

    S_k1 P10=-sR0 A+kP[(1-z2)A'-zA]-D_m Q,
    Q10=mR0 Q+kP[(1-z2)Q'-2zQ].

The inverse on polynomials is well-defined because S_k1 U_j=[(j+1)2-k1^2]U_j and 1<k1<4/3, where U_j is the second-kind Chebyshev polynomial. Both P10,Q10 have degree<=2J-1, as proved by direct polar differentiation in packet117.

Let n>=4, K=2J. Write T_i for the first-kind Chebyshev polynomial, and

    E_i(t)=T_i(2t-1)-(-1)^i-2(-1)^(i-1)i2 t, i>=2,
    B_i(t)=T_i(2t-1)-(-1)^i, i>=1.

For finite core coefficients C,D set

    p=x R^(1-s)[P(z)+tP10(z)+sum_(i=2..n-1,j=0..K-1) C_ij0 E_i(t)T_j(z)
       +R^-1{(eta/beta)L_(1-s)P(z)+sum_(i=1..n-1,j=0..K-1) C_ij1 B_i(t)T_j(z)}],
    Theta=x2 R^(-1-2s)[Q(z)+tQ10(z)+sum_(i=2..n-1,j=0..K-1) D_ij0 E_i(t)T_j(z)
       +R^-1{(eta/beta)L_(-1-2s)Q(z)+sum_(i=1..n-1,j=0..K-1) D_ij1 B_i(t)T_j(z)}],
    Psi=p-x p_x(0), U=(-Psi_y,Psi_x), Omega=-DeltaPsi, W=beta X+U.

All coefficients except the following six are free:

    C_200,C_300,C_210,C_310,D_200,D_210.                 (1)

There is exactly one choice of these six that imposes

    p_x(0)=-eta, Psi_xy(0)=c, Omega_x(0)=q0,
    Theta_xx(0)/2=a0,
    [x2 y]R_Theta=0, [x y]R_Omega=0.                   (2)

Here R_Theta=W.gradTheta-(beta-2)Theta and R_Omega=W.gradOmega+Omega-Theta_x. Every chosen field is smooth on the full plane, has B2 parity and Theta=0 on the axis, is exactly nontrivial at the center, has sublinear canonical relative velocity, and satisfies the first nonlinear integer and constant-induced fractional tail identities of packet117. These properties do not imply either full PDE. No positivity is imposed. The parameter beta remains fixed or freely variable within (2,3), and eta is a shape parameter, not a removable uniform-velocity gauge.

## Exact center equations

Use the local notation

    gamma=p_x(0), c0=Psi_xy(0), b0=Omega_x(0),
    c1=Psi_xyy(0), b1=Omega_xy(0),
    a=Theta_xx(0)/2, a1=Theta_xxy(0)/2.

Direct Taylor expansion of the defining Cartesian PDE gives

    [x2]R_Theta=(beta-2c0+2)a,
    [x2 y]R_Theta=(2beta-c0+2)a1-2a c1,
    [x]R_Omega=(beta-c0+1)b0-2a,
    [x y]R_Omega=M b1-c1 b0-2a1.                     (3)

For completeness, Theta=x2(a+a1y+O(r2)), Omega=x(b0+b1y+O(r2)), W1=x(beta-c0-c1y+O(r2)) and W2=(beta+c0)y+O(r2). Substitution proves (3); the absence of a constant in W2 uses the moving-center subtraction. With c0=c, b0=q0 and a=a0, (3) reduces exactly to

    a1=2a0 c1/mu,
    b1=(q0+4a0/mu)c1/M.                             (4)

These two additional identities involve no higher center coefficient. They are linear conditions on the complete ordinary coefficient pair for fixed beta,a0.

## Unique sequential elimination

First set all six pivots in (1) to0 and add the remaining leading and core terms. Odd angular pivots do not change gamma,b0 or c1. Use E2=8t2 and E3=32t3-48t2. The two even stream pivots have moment matrix

    (gamma,b0): [[8,-16],[-32(1-3s),64(1-s)]],
    determinant=1024s>0.

With Delta_gamma=-eta-gamma and Delta_b=q0-b0, set

    C_300=[Delta_b+4(1-3s)Delta_gamma]/(128s),
    C_200=Delta_gamma/8+2C_300.                       (5)

Recompute c1 of this stream. It will not be changed by either remaining odd stream pivot. Put target_b1=(q0+4a0/mu)c1/M, Delta_c=c-c0 and Delta_b1=target_b1-b1. The odd stream pivots are

    xR^(1-s)E2(t)T1(z)=8xy R^(-3s),
    xR^(1-s)E3(t)T1(z)=32xy R^(-4s)-48xy R^(-3s).

For xy R^q, c0=1 and b1=-6q. This follows from R^q=1+q(x2+y2)/2+O(r4) and Delta[xy(x2+y2)]=12xy. Thus their matrix is

    (c0,b1): [[8,-16],[144s,-96s]],
    determinant=1536s>0.

The unique corrections are

    C_310=[Delta_b1-18s Delta_c]/(192s),
    C_210=Delta_c/8+2C_310.                          (6)

Finally, the temperature pivots have respective (a,a1) moments (8,0) and (0,8). With the existing temperature moments a,a1, put

    D_200=(a0-a)/8,
    D_210=[2a0 c1/mu-a1]/8.                         (7)

Equations (5)-(7) prove existence and uniqueness. The coupling from the even stream pivots to c1 is accounted for by recomputing c1 before (6)-(7). The odd stream pivots do not change c1, so no circular system is hidden. The full six-by-six affine pivot map is triangular by blocks with nonzero determinants.

## Tail preservation, inverse and differentiability

Every pivot is an E_i core term. It vanishes at t=0 with its first derivative, so it changes neither P,Q nor P10,Q10. It also changes no shift1 endpoint, and therefore none of the first constant-induced fractional tail relations. The exact identities for the constant eta continue to hold because (5) imposes gamma=-eta. No independent drift was inserted into W.

The smoothness, full-plane parity and inverse argument can also be read directly from the formula. R>=1; the slowest velocity grows like r^(1-s), while Omega=O(r^-s). The centered U has zero value at0. The whole-plane subtracted Biot-Savart integral converges for this decay, is sublinear, and differs from U by an entire harmonic vector field with sublinear growth and value0 at0. The growing-ball gradient estimate makes that difference0. This uses no box boundary or exterior strain.

For rational beta,eta,a0 and free coordinates, the formulas give rational ordinary coefficients. Exact JSON is the input to the center and tail certificates. At fixed beta,a0 the coefficient map has total polynomial degree at most2 in eta and the free coordinates: the prescribed tail coefficients are quadratic, and all pivot corrections are linear functionals of those coefficients. Every core coordinate has a constant linear direction, including its induced temperature correction through c1. Therefore the centered unit-step difference of the coefficient map is exactly its derivative in rational arithmetic. The residual Jacobian uses this derivative and the Cartesian product rule; only the beta derivative needs a numerical differentiation in the planned solver. No uniform conditioning near beta2 is claimed.

## Scope and dependencies

Packet118 gives independently checked closed rational center moments and (3). Packet117 gives the first-tail polynomial calculus and the two-shift family, including its canonical inverse. The matrix calculations and sequential elimination here are new. Controls must rederive both matrices by Cartesian differentiation and verify (2), tails and Jacobians after exact serialization. A manufactured forcing test may check solver plumbing but is not a solution to the unforced equations.

Finitely many zero Taylor coefficients and correct first tail terms do not imply a small residual between them. The previously rejected packet117 fields cannot be reclassified by this construction: the new chart changes their fields. All fresh fits require new residual, inverse, nontriviality and local higher-order tests. Neither a failed fit nor the finite angular-family restriction excludes a limiting profile as resolution increases. No Lean formalization is attempted.

## Independent higher-center coefficient check

The actual ordinary coefficient fields can be expanded independently of the six-pivot chart. For R=(1+x2+y2)^(1/2), use the finite generalized binomial series of (1+x2+y2)^q through total degree6, the ordinary Chebyshev recurrence T_(n+1)=2zT_n-T_(n-1), and polynomial addition/multiplication. Remove only the x monomial from Psi to implement its exact relative velocity. Then apply the Cartesian -Delta and transport operators to those rational polynomials. Their coefficients through degree4 in R_Theta and degree3 in R_Omega equal those of the actual smooth fields: omitted stream terms start at degree7, differentiation in the vorticity equation lowers by at most3, and W vanishes at0; omitted temperature terms start at degree7 and are differentiated at most once. In particular the lower coefficients enforced by the chart must all be exactly0. A nonzero higher coefficient rejects the serialized field as an exact local solution. It does not bound the distance to a different profile. Serialized coefficient inputs and these certificates are hashed together. Numerical smallness of a coefficient is not used for rejection.
