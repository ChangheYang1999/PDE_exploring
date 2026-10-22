# Interval evaluation of selected Cartesian residuals

Written 2026-10-22T08:38Z, before implementation and any candidate evaluation. Status OPEN until the proposed computations and separate checks pass. This is a finite-value result, not a bound over a region or an existence result.

## Statement and dependencies

Take either of the two exact beta=3 generating functions defined in research/core32_charts184/PROOF.md. Its exact dyadic parameters and coefficients are imported through the JSON definitions bound there. Write A=G_xeta and C=G_xx. Audit184 proves A>=E^(1/3)/100 on the whole plane and therefore a unique smooth inverse eta(x,y) of y=G_x(x,eta). Audit220 supplies finite root enclosures at the sampled dyadic coordinates. Here we seek, at a selected finite subset of these points, rigorous intervals for the Cartesian fields, derivatives, residual R and both pointwise normalizers. A successful interval is a bound at that exact point only. Every source and selection must be recorded before this computation; every failed enclosure must remain visible.

## Coordinate formulas

Let xi=G_eta and y=G_x. The generating stream function is Psi(x,y)=3xG_x+eta G_eta-6G, with the right side evaluated at the inverse eta(x,y). Differentiating y=G_x gives eta_x=-C/A and eta_y=1/A. The physical differential operators on functions of x,eta are therefore

    Dx = partial_x-(C/A)partial_eta,  Dy=A^(-1)partial_eta.

The generating identity gives W.grad xi=5xi and W.grad eta=eta. Solving the first identity for W1 and then using the second yields

    W1=(5G_eta-eta G_etaeta)/A,
    W2=C W1+A eta,
    U1=W1-3x,  U2=W2-3G_x.

In particular the last subtraction is the function G_x, not a constant y while differentiating. With the prompt's sign convention curl U=-Omega,

    Omega=Dy U1-Dx U2,
    Omega_x=Dx Omega,  Omega_y=Dy Omega,
    Theta=600 eta,  Theta_x=-600 C/A,  Theta_y=600/A.

It follows directly that

    R=W1 Omega_x+W2 Omega_y+Omega-Theta_x,
    N=abs(W1 Omega_x)+abs(W2 Omega_y)+abs(Omega)+abs(Theta_x),
    N2=abs(U1 Omega_x)+abs(U2 Omega_y)
       +abs(3(x Omega_x+y Omega_y)+Omega)+abs(Theta_x).

At x*y nonzero D=R/(x*y). Positive lower interval bounds for N,N2 permit interval division for abs(R)/N and abs(R)/N2. A zero-containing normalizer gives an undefined ratio, never an artificial floor. The temperature residual is W1 Theta_x+W2 Theta_y-Theta and is an algebraic identity from the same W and Theta definitions. Re-evaluating it tests arithmetic consistency only; it supplies no independent evidence for the P2 equation and no existence claim.

## Taylor interval computation

A bivariate Taylor array of total degree n stores partial_x^i partial_eta^j f/(i!j!) for i+j<=n. Sums use coefficient sums; products use finite convolution; differentiation multiplies the coefficient at (i+1,j) by i+1, or at (i,j+1) by j+1. A derivative lowers the available order. Coefficient-wise interval operations contain the corresponding exact arrays for every base eta in the input interval. Truncation is exact for these finite derivatives and is not an approximation to a finite spatial displacement.

For an analytic scalar function f of a Taylor array Z, split Z=C+V with V's constant coefficient set to zero. The coefficient array through order n is exactly the truncation of sum_{k=0}^n f^(k)(C)V^k/k!. For reciprocals use f^(k)(C)/k!=(-1)^k C^(-k-1). For logarithms use log(C) and (-1)^(k-1)/(k C^k), k>=1. For exp(-C-V) use exp(-C)(-1)^k/k!. For C^p use C^p binom(p,k)C^(-k). These formulas are pointwise statements at the actual base C; outward interval evaluation of each coefficient therefore encloses all possible bases. We use the already tested400bit integer interval elementary operations of220 for the scalar values. The only fractional power is p=-1/6 with E>=1; evaluate it by monotonicity at the two rational endpoints and exact integer sixth-power comparisons. An interval meeting a singular scalar domain is refused.

The smooth expression

    E=1+x^2+(eta/s)^6, q=E^(-1/6),
    t=-log(1-(1-exp(-3))q)/3, w=(eta/s)^2 q^2,
    G=x eta q^(-2)[P(t,w)+sum exp(-(x^2+eta^2)/L^2)Q(u,v)]

with u=x^2/(R^2+x^2),v=eta^2/(R^2+eta^2), gives the required degree4 array. The displayed W formulas require G through degree2 and retain two derivatives of W; one derivative yields Omega and one further derivative yields grad Omega. Thus degree4 of G suffices.

## Stable Chebyshev derivative enclosure

The coefficients of P and Q are in shifted Chebyshev bases. Direct interval recurrence at an interval argument can greatly overestimate. For each Chebyshev argument Z0 in [-1,1], choose an exact dyadic midpoint m and radius rho containing Z0. Compute Taylor coefficients of T_n at the point m by interval recurrence T_0=1,T_1=z,T_{n+1}=2zT_n-T_{n-1}. Enclose the coefficient of order r at every z in Z0 by this point coefficient plus or minus rho M_{n,r+1}/r!, where M_{n,k} bounds abs(T_n^(k)) on [-1,1]. This follows from the mean value theorem.

Here M_{n,0}=1 and for 1<=k<=n,

    M_{n,k}=n*2^(k-1)*(k-1)!*binom(n+k-1,n-k),

with zero for k>n. To prove the bound without a numerical assumption, differentiate the generating identity for T_n to get T_n^(k)=n*2^(k-1)*(k-1)! C_{n-k}^k. This identity follows first from T_n'=n U_{n-1}, whose generating series is (1-2zt+t^2)^(-1), and then from partial_z C_j^lambda=2lambda C_{j-1}^{lambda+1}. For z=cos(theta), the generating series of C_j^k factors as (1-exp(i theta)t)^(-k)(1-exp(-i theta)t)^(-k). Each binomial-series coefficient has nonnegative magnitude; applying the triangle inequality to the coefficient convolution bounds abs(C_j^k(z)) by C_j^k(1). At z=1 the series is (1-t)^(-2k), whose coefficient is binom(j+2k-1,j). Substitution proves the claimed M. The r=0 bound for T_n follows from cos(n theta).

Compose these enclosed derivative coefficients with the zero-constant Taylor array Z-Z0. Tensor evaluation first contracts one coordinate in each row, then multiplies by the other coordinate's basis. All operations are outward interval arithmetic. The argument enclosure must be contained in [-1,1]; otherwise this method refuses rather than applying its bound outside its domain.

## Verification scope

Before candidates, test finite polynomial Taylor algebra against exact rational differentiation; test the Chebyshev bound identity and base perturbations; and compare the physical coordinate formulas for manufactured generating functions against independent symbolic differentiation of Psi and its Laplacian. A separate checker should reaggregate every accepted interval using integer endpoint arithmetic, verify positivity and ratio containment, and bind the exact source, root enclosure and selection. This second checker does not independently regenerate fourth derivatives. Compare to the completed130digit scalar values as a diagnostic only, never as an acceptance condition substituting for the proof.

No formal sources or Lean builds are used. The numerical inverse here is a coordinate inverse, not an elliptic quadrature. The canonical whole-plane velocity is inherited from184's separate theorem. This result cannot prove a nearby solution, a uniform residual threshold, a limiting profile, exponent selection, or the A1 endpoint.

Revision 2026-10-22T08:44:50.747221+00:00. Parameters M=3 and alpha=3 are exactly those in184: Msets the eta compactification power6 and alpha sets the logarithmicmap. The amp600is the stored multiplier ofeta; the physical center slope remains600/G_xeta(0), as184states. The evaluator nowrequires this storedamplitude. The original PROMPT forcing is explicitlyTheta_x; signs above use that convention. All paths are relative to the verifier working directory.

For generalG, the streamfunction identity can be checked without the manufacturedtest. Write S=3xG_x+etaG_eta-6G. Then S_x=3xC+etaA-3G_x and S_eta=3xA+etaG_etaeta-5G_eta. Thus -DyS=-S_eta/A=W1-3x and DxS=S_x-(C/A)S_eta=CW1+Aeta-3G_x=W2-3G_x. This proves the W-derived U formula for every sufficientlysmoothGwithApositive. The manufacturedtest onlychecks its implementation.

Any rawdivision with a zero-containing xyintervalnowrecords Dundefined while preservingotherenclosures. Root/sourcebindingis an explicitacceptancepremise: the finalrunnerandchecker must bind exactNPZ/JSONbytes, coordinate x,y and the twoindependentendpointbrackets for thatveryG. No unbound220hint is enough. Sharper160/140/120bit brackets may be tested from the same130digithint, withboth220endpointimplementations; these new selectedbrackets must themselves be recordedandchecked. They are not inheritedmerelyfromthewider220brackets.

Post-implementation revision 2026-10-22T08:53:25.188729+00:00: PROMPT.md lines14and35to37 explicitly define U=(-Psi_y,Psi_x), -DeltaPsi=Omega and the forcingTheta_x. Those equations fix the orientation used here. Source conventions remain those of184. Constructor input arrays must be nonempty rectangular matrices with nonempty rows; M is required in the source JSON numeric form3, so a string3 fails safely. A runner catches and records each refusal, including Chebyshev range and scalar domain failures. No domain clamping is implemented or assumed. Degree96 endpoint tests check pointrecurrence and exact derivativeidentity, while finite-width tests exercise the envelope separately. The nonlinear synthetic formula is now also tested at nonzero-width base intervals using endpoint and midpoint MPdiagnostics.
