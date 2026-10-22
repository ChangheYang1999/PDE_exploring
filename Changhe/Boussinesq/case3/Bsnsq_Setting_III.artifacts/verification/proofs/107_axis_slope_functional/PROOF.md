# Axis slope as a monotone functional of the axial velocity

Written UTC: 2026-10-21T02:08:09.688757+00:00
Status: independent analytic proof; own5 exact exponent checks and15 independent ODE/functional states passed. Actual Opus138 full written review confirms the formulas and monotonicity; packet106 compatibility is a separate dependency. A necessary relation on a zero-free half-axis, not a full-profile existence or exclusion theorem.

## Hypotheses and conventions

Let beta>2, a0>0, alpha=1/beta, p=beta/2-1, mu=3beta/2+1 and ell=mu/beta. Consider the upper axis y=r>0 of a smooth hypothetical B2 solution, with

    W dot grad Omega+Omega=Theta_x,
    W dot grad Theta=(beta-2)Theta, div W=2beta.

Assume x-reflection symmetry and local expansions

    W1=x A(r)+O(x³), W2=v(r)+O(x²),
    Theta=x² a(r)+O(x⁴), Omega=x g(r)+O(x³).

Assume v(r)>0 for r>0, v(r)=mu r+O(r²) near0, v(r)=beta r+O(r^(1-alpha)) at infinity, and a(0)=a0. The derivatives used below exist, and the center relations of the prompt hold. We use P and rho for exponents to avoid confusing them with p or the vorticity coefficient g.

## Exact axis identities

Divergence gives A+v'=2beta. The x² coefficient of temperature transport and x coefficient of vorticity transport give

    v a'=(2v'-2mu)a,
    v g'+(2beta+1-v')g=2a.                             (1)

In particular g(0)=4a0/beta. Define

    zeta(r)=r exp[int_0^r (mu/v(s)-1/s) ds],
    P=(2beta+1)/mu, rho=(beta+1)/mu.                    (2)

The integrand in(2) is bounded near0 by the assumed Taylor estimate, and zeta'=mu zeta/v with zeta/r->1. Solving the first equation of(1) with a(0)=a0 yields

    a=a0 v²/(mu² zeta²).                               (3)

An integrating factor for the second equation is zeta^P/v. Since P>1, its product with a bounded g tends to0 at r=0. Equations(1)-(3) then give

    g(r)=(2a0/mu²) v(r) zeta(r)^(-P)
          int_0^r zeta(s)^(-rho) ds.                   (4)

The exponent identity P-2=-rho was used. Near0 the integral is r^(1-rho)/(1-rho), and P+rho=2, since

    (2beta+1)+(beta+1)=3beta+2=2mu.

Thus (4) has a finite positive center limit2a0/[mu(1-rho)]=4a0/beta, as required.

## Convergence and the far-field coefficient

Since v=beta r+O(r^(1-alpha)), the function mu/v-ell/r is O(r^(-1-alpha)). Consequently a finite constant C>0 exists with

    zeta(r)=C r^ell(1+O(r^(-alpha))).                  (5)

Also0<rho<1 and ell rho=1+alpha>1. Hence

    I=int_0^infinity zeta(s)^(-rho) ds

is finite and strictly positive. Equations(4)-(5) give the exact positive far-field coefficient

    Q=lim_{r->infinity} r^(1+alpha)g(r)
      =(2a0 beta/mu²) C^(-P) I.                       (6)

No homogeneous angular expansion was needed to prove this axis limit. If the solution has the class-A angular asymptotic, Q must agree with its corresponding one-sided angular derivative coefficient. Formula(6) uses the entire axial velocity profile, not merely its values or slopes at0 and infinity.

## Correct monotonicity

Let v1,v2 satisfy these hypotheses with the same beta and a0, and suppose v1(r)>=v2(r)>0 for every r>0. From(2), zeta1<=zeta2. Moreover

    log(C1/C2)=mu int_0^infinity(1/v1-1/v2)dr<=0.      (7)

This integral converges near0 because both slopes are mu and their differences are O(r²), and at infinity by the common beta and assumed decaying relative remainder. Thus C1<=C2, I1>=I2, and

    Q1>=Q2.

If the velocities are not identical, continuity gives a positive-length interval of strict inequality, so(7) is strict and Q1>Q2. The statement "increasing v lowers Q" is therefore refuted. The source model's written answer had the correct increasing sign; the numerics note reversed it.

## Explicit length family and absence of a subsystem upper bound

For L>0 choose

    v_L(r)=mu r(1+(r/L)²)/(1+ell(r/L)²).

Then zeta_L=r(1+(r/L)²)^((ell-1)/2), C_L=L^(1-ell). With m=1/(2ell), substitution r=L u gives

    int_0^infinity zeta_L^(-rho)dr
       =(L^(1-rho)/2) B(m/2,alpha/2).

The beta integral converges because both arguments are positive. Inserting this in(6), using P(ell-1)+1-rho=1+alpha, yields

    Q_L=(a0 beta/mu²) B(m/2,alpha/2) L^(1+alpha).      (8)

The velocities increase pointwise with L. Hence this family also verifies the direction of monotonicity. At fixed beta,a0, Q_L has no finite upper bound in the abstract axis ODE subsystem.

There is a stronger, still limited compatibility statement. Packet106 constructs, for a fixed beta and sufficiently large amplitude A, positive canonical vorticity Omega_A=A Delta U-Delta psi_c with a0=A and axis velocity v_1. Scaling its length by L and taking A=a0 L gives coefficient a0 after rescaling and axis velocity v_L. The positive-vorticity domination is valid whenever A exceeds its fixed finite threshold, hence for all sufficiently large L. Therefore the unbounded sequence Q_L in(8) is compatible with smooth positive vorticity, the canonical relative inverse, the center strain, and the stated axis subsystem at fixed beta,a0. It does not solve either off-axis transport equation and is not a counterexample to an upper bound that additionally uses those equations or global chart properties.

## Dependencies and evidence

Dependencies are elementary ODE integration and the beta integral. The final strengthened compatibility statement uses packet106's independently proved positive-vorticity construction. No numerical transport code is reused. Exact parameter checks, independent quadrature and differential-equation tests are in verification. No Lean or Lake verification is claimed.
