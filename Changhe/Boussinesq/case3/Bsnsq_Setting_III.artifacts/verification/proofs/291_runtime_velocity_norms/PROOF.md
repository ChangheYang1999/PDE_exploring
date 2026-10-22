# Independent inverse norms and the runtime quadrature comparison

## Exact statement, definitions and scope

Let Omega and f be two literal stored smooth-at-center spline vorticities on the full plane, odd in x, with the native source representation retained. In this packet the far-field decay exponent satisfies 0<s<1, since every beta and beta_seed is greater than3 or equal to3. Their relative inverse is B[g](X)=U[g](X)-U[g](0), for the Biot-Savart kernel (Z2,-Z1)/(2 pi |Z|^2). The forced relative velocity is V=B[Omega]+lambda B[f]. This differs from the defining B2 relative velocity B[Omega]. The dilation beta X is not included in V.

At a fixed radius r and the 181 angles phi_j=j pi/182, 1<=j<=181, use X_j=(r sin phi_j,-r cos phi_j). Define the finite norm M(V)=max_(j,a)|V_a(X_j)|, where a=1,2. This is a maximum of Cartesian components, not the Euclidean norm. Let V12 and V48 denote any two runtime approximations, and D=M(V48-V12). Then

    |M(V48)-M(V)| <= M(V48-V),
    D <= M(V48-V)+M(V12-V).

Consequently at least one approximation has finite-grid error at least D/2. There is no implication that either error is at most D. If the input consists only of D and M(V48), their numerical values and ratios can be checked arithmetically, and M(V) can be computed independently, but the full error M(V48-V) is not reconstructible without the component arrays. A lower estimate based on the first inequality is conditional on the stored runtime norm being accurate and on control of the independent inverse error. With ordinary floating-point quadrature it is a numerical diagnostic, not a rigorous error enclosure.

## Complete proof of the norm claims

For each j,a, the triangle inequality gives |V48_a(X_j)|<=|V_a(X_j)|+|(V48-V)_a(X_j)|. Taking maxima gives M(V48)<=M(V)+M(V48-V). Interchanging V and V48 gives the absolute-value bound. Applying the same triangle inequality to V48-V12=(V48-V)+(V-V12) gives the second bound. If both summands were less than D/2, their sum would be less than D, a contradiction. To disprove an upper bound by D, take V12=V48=V+Z for any nonzero finite array Z. Then D=0 but both errors equal M(Z)>0. These facts require no PDE hypothesis.

## Separately implemented full-plane inverse

Write the vorticity g in the finite sine series g(r,phi)=sum_(n>=1) H_n(r) sin(n phi), with phi measured from the negative y-axis as above. Let Psi=sum p_n(r) sin(n phi), where -Delta Psi=g and U=(-Psi_y,Psi_x). For n>=2 the canonical regular, sublinear-velocity inverse is

 p_n(r)=[r^(-n) integral_0^r rho^(n+1)H_n(rho) d rho
         +r^n integral_r^infinity rho^(1-n)H_n(rho) d rho]/(2n).

The scalar radial ODE p_n''+p_n'/r-n^2p_n/r^2=-H_n follows by polar differentiation. Differentiating the displayed expression, the boundary terms cancel; its first derivative is one half of minus the inner term divided by r plus the outer term divided by r. Substitution establishes the ODE. The inner integral is regular at zero for the stored smooth-at-center modes. The outer integral converges because H_n=O(r^-s) with s>0 and n>=2. The formula produces velocity O(r^(1-s)), up to lower-order terms, and excludes both the origin-singular r^-n and the growing harmonic r^n for n>=2. This is the unique full-plane regular inverse with sublinear velocity in these modes.

For n=1 the outer integral may diverge, but subtraction of U(0) is finite. Taking the same expression with a finite outer cutoff and subtracting its origin derivative yields

 p_1(r)/r = [r^-2 integral_0^r rho^2 H_1(rho)d rho - integral_0^r H_1(rho)d rho]/2,
 p_1'(r) = [-r^-2 integral_0^r rho^2 H_1(rho)d rho - integral_0^r H_1(rho)d rho]/2.

These identities follow directly by cancellation of the integral from r to the cutoff against that from zero to the cutoff. Differentiation verifies the ODE and the relative gauge. Any remaining full-plane harmonic velocity of sublinear growth is constant, by the interior harmonic derivative estimate on disks with radius tending to infinity. Its value at the origin fixes the constant. Thus the formulas agree with the full-plane relative kernel, independently of a finite numerical wall.

The numerical implementation performs the inner quadrature in rho=r t^2, 0<=t<=1. For n>=2 the exterior uses rho=r/t^b, b=1/s, which retains the entire infinite exterior. These are physical-radius quadratures with power substitutions; no NUM quadrature cells, Green matrices, interpolation or derivative code are reused. Cartesian velocities are reconstructed from U_r=-sum n p_n cos(n phi)/r and U_phi=sum p_n' sin(n phi). The raw spline reader uses an independent SciPy BSpline evaluation and explicit angular product identities. Separate original manufactured tests of this inverse are dependencies and remain recorded in their source packets.

Each input source is reconstructed in its own beta_seed geometry, and added linearly with its exact stored lambda. The audit evaluates the identical finite angle set as the published runtime table. It uses two adaptive tolerances on radii through 1e9 to assess numerical sensitivity, not to assert certified quadrature error. The task is to compare independent norms and audit the arithmetic and scope of the reported two-order comparison. Without saved component arrays it cannot reproduce the runtime difference vector, establish which quadrature order is closer to the exact inverse, or bound the interpolation error. None of these data proves a B2 profile, a root shift or convergence.

## Inputs, dependencies and order of work

The six runtime JSON tables, six corresponding raw archives and read-only source used to identify the angle and norm conventions are hashed in the manifest before evaluation. The mathematical proof above precedes every new numerical control. Formal proof assistant sources are not supplied; no Lean or lake build is run. The complete statements and proofs of the norm and inverse formulas are included here, while manufactured tests of the unchanged verifier implementation are retained as dependencies. This is an independent numerical diagnostic with explicitly conditional interpretation of the runtime-reported values.

Written 2026-10-22T06:11:21.852932+00:00 before controls.

Implementation description clarified 2026-10-22T06:13:34.806174+00:00; the computations are unchanged.

## Post-review corrections and explicit conventions

Opus501 identified a dummy-variable typo in the displayed Green integrals: the integrand must use H_n(rho), not H_n(r). The independently implemented numerical integrands already evaluated H_n at the integration variable, as the frozen source code shows. The original and intermediate proof files are preserved; the displayed formulas are corrected above. No numerical field was changed. The input class is now explicitly restricted to0<s<1, which all six archives satisfy, so no claim about faster-decay Green asymptotics is needed here. The Cartesian basis vectors are e_r=(sin(phi),-cos(phi)) and e_phi=(cos(phi),sin(phi)). Runtime comparison is conditional on the reported arrays using this same component norm, angle set, native source and relative gauge. The runtime source was inspected read-only to identify these conventions, but its component arrays were not independently reproduced.

Corrections written 2026-10-22T06:15:08.304560+00:00 before symbolic formula controls.
