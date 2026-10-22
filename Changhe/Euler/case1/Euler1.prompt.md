# Research task: genuinely two-fold 3D Euler self-similar profiles, prioritizing 2/5 < c_l < 1/2

You are conducting a numerical PDE research project, not merely writing a plan. Develop, test, and run a resource-conscious, resumable search for smooth, genuinely non-axisymmetric, two-fold rotationally symmetric self-similar profiles of the unforced incompressible 3D Euler equations on R^3. Borrow the direct profile-solving/PINN approach of Ganeshram–Duruisseaux–Anandkumar, but solve the FULL THREE-DIMENSIONAL equations, not their axisymmetric reduction.

This prompt is self-contained. Do not assume earlier conversations, existing candidate data, or access to the authors' unpublished code. Implement and execute a LONG-DURATION CAMPAIGN of at least 96 hours of measured, non-overlapping active numerical experiment time (not merely a plan, a one-hour pilot, or 96 nominal wall-clock hours with idle periods). Prepare durable resumption across process/session interruptions. Distinguish a numerical candidate, an exact profile, stability, and blowup from one smooth finite-energy initial condition. These are different achievements. If execution tools cannot actually remain active for 96 hours, do not pretend that they did: checkpoint, report completed active time, and provide a one-command continuation path.

## 1. Main objective and scope

The primary target is a nontrivial, non-affine, genuinely m=2 profile with

    0.4 < c_l < 0.5.

Prefer a numerically resolved separation from 0.5, not a fitted value such as 0.499999 whose discrepancy from 0.5 is smaller than numerical sensitivity. Do not minimize c_l as an independent objective: solve the equations and determine which exponents are supported.

A candidate at c_l=0.5 is a secondary result or calibration, not achievement of the subcritical target. Preserve a credible candidate outside the primary interval, but clearly label its different significance. Failure of a search or of a restricted ansatz is not a nonexistence theorem.

We initially seek an isotropic, single-spatial-scale, time-independent similarity profile centered at a point on the fixed z-axis. Paired off-axis peaks inside this shrinking core are allowed. We are not claiming to cover anisotropic, discretely self-similar, rotating-profile, or multiple macroscopic-center blowup mechanisms.

Do not introduce a physical boundary, external force, compressibility, z-periodicity, reflection symmetry, or a modified convection law into the final problem. Homotopies used only for initialization must be explicitly identified and returned to the exact Euler equations before assessing a candidate.

## 2. Source audit: borrow the method, not incompatible assumptions

Consult these primary sources when accessible, recording versions and the specific methods actually used:

[R1] Ganeshram, Duruisseaux, Anandkumar, "Self-Similar Singularity of the Euler Equations on R^3," arXiv:2609.10867, especially the numerical-methods supplement.
https://arxiv.org/abs/2609.10867

[R2] Wang, Liu, Li, Anandkumar, Hou, "High precision PINNs in unbounded domains: application to singularity formulation in PDEs," arXiv:2506.19243.
https://arxiv.org/abs/2506.19243
The paper links this public implementation:
https://github.com/RoyWangyx/High-precision-PINNs-unbounded-domains-

[R3] Constantin, Ignatova, Vicol, "On putative self-similarity for incompressible 3D Euler," arXiv:2602.17570. Check the hypotheses of the finite-energy, local-outgoing, and axisymmetric restrictions.
https://arxiv.org/abs/2602.17570

[R4] "SS-eSOAP: Self-Scaled Adaptive Preconditioning for Physics-Informed Learning," arXiv:2608.29448.
https://arxiv.org/abs/2608.29448

The transferable ideas are direct stationary residual minimization, smooth representations, FP64, constraints against degeneracy, wide-range sampling, staged optimization, and separate validation. Our symmetry, equations, seeds, gauges, diagnostics, and search schedule below are proposed adaptations, not claims about the authors' implementation. Verify missing details rather than inventing them. A formalization repository is not automatically the training-code repository.

Do not spend the whole session on literature review. If a source or implementation is inaccessible, record that limitation and proceed from the explicit equations below. Do not mislabel a standard optimizer as SS-eSOAP or SS-Broyden.

## 3. Exact ansatz, sign conventions, and equations

Let tau=T-t>0 and y=(x-x_*)/tau^{c_l}, with x_* on the z-axis. Set

    u(x,t) = tau^{c_l-1} U(y),
    p(x,t) = tau^{2c_l-2} P(y).

Here c_l is the positive physical spatial-collapse exponent. It is not an independently normalized dynamic-rescaling coefficient. The velocity exponent is c_l-1, and

    omega(x,t) = tau^{-1} Omega(y),    Omega = curl U.

The canonical stationary system is

    (1-c_l) U + (c_l y + U)·grad U + grad P = 0,
    div U = 0.                                                (E)

All differential operators in (E) act on physical similarity coordinates y, not computational coordinates. Derive (E) independently and test its signs before optimization.

An optional axial recentering parameter C is allowed:

    (1-c_l) U + (c_l y + C e_z + U)·grad U + grad P = 0.         (E_C)

It corresponds to y=(x-z_c(t)e_z)/tau^{c_l} and

    z_c'(t) = -C tau^{c_l-1},
    z_c(t) = z_* + (C/c_l) tau^{c_l}.

A constant C is a representation/centering freedom, not a new physical mechanism: Y=y+(C/c_l)e_z and U_hat(Y)=U(Y-(C/c_l)e_z) remove C. If C is optimized, add one appropriate axial centering condition and report the equivalent canonical profile. Do not impose both U(0)=0 and another unrelated center condition without checking their compatibility. Do not introduce horizontal drift or a rotating frame in this initial project.

Use velocity and pressure as the physical unknowns. Do not substitute the axisymmetric Gamma–eta system or a two-dimensional streamfunction inversion. Vorticity and a vector potential may be used as diagnostics or parameterizations, with their relation to U enforced exactly.

### Independent cylindrical formulation

For verification, write y=(r cos(theta),r sin(theta),z) and

    U = U^r e_r + U^theta e_theta + U^z e_z,
    B^r = c_l r + U^r,
    B^z = c_l z + C + U^z,
    D = B^r partial_r + (U^theta/r) partial_theta + B^z partial_z.

Then (E_C) is exactly

    (1-c_l) U^r     + D U^r     - (U^theta)^2/r + partial_r P       = 0,
    (1-c_l) U^theta + D U^theta + U^r U^theta/r + partial_theta P/r = 0,
    (1-c_l) U^z     + D U^z                    + partial_z P       = 0,
    partial_r U^r + U^r/r + partial_theta U^theta/r + partial_z U^z = 0.

The angular transport and geometric terms are essential. Evaluate axis limits using Cartesian smoothness, not division by a small arbitrary cutoff r. Cross-check the Cartesian and cylindrical residuals away from the axis.

## 4. What m=2 means, and what it does NOT mean

Let Q=diag(-1,-1,1), rotation by pi about the z-axis. Require

    U(Qy)=Q U(y),    P(Qy)=P(y).

Thus U_1,U_2 are odd under simultaneous (y_1,y_2)->(-y_1,-y_2), while U_3,P are even under that simultaneous transformation. Do not impose separate x- or y-reflection parities.

In cylindrical components, all velocity components and pressure are pi-periodic in theta. Their allowed frequencies are n=0, ±2, ±4, ... . Keep both sine and cosine content. The corresponding Cartesian horizontal components have shifted angular frequencies; do not impose scalar pi-periodicity on U_1 or U_2.

The axisymmetric mean must remain free. Nonlinearity generates mean and higher harmonics. A model retaining only n=0,±2 is not an invariant reduction: if used as an initial truncation, validate the FULL residual, including generated n=±4 and beyond, and enlarge the representation. A fundamental wedge has periodic rotational identification, not slip-wall or reflection boundary conditions.

No z-even/odd symmetry, no theta-reflection symmetry, no no-swirl condition, and no full inversion parity are imposed. Do not require the peak vorticity to occur on the axis.

### Axis regularity

For a smooth m=2 Cartesian field, at fixed z,

    U_1 = a(z)y_1+b(z)y_2+O(r^3),
    U_2 = c(z)y_1+d(z)y_2+O(r^3),
    U_3 = w(z)+O(r^2),
    a(z)+d(z)+w'(z)=0.

The transverse 2x2 matrix is general, not restricted to an axisymmetric dilation-plus-rotation matrix. In particular, genuinely n=2 horizontal velocity can be O(r), not necessarily O(r^3).

If a cylindrical Fourier representation is used, derive and enforce the coupled smoothness conditions. In the convention f=sum_n f_n exp(i n theta), they include

    (U^r+i U^theta)_n = O(r^{|n+1|}),
    (U^r-i U^theta)_n = O(r^{|n-1|}),
    U^z_n, P_n        = O(r^{|n|}).

A smooth Cartesian representation is preferred initially because these conditions are automatic. Smooth activations alone do not prove a smooth limiting profile: check derivative convergence under refinement.

## 5. Parameterization and exact constraints

A convenient hard symmetry projection for a raw Cartesian vector network F and scalar network p_raw is

    S F(y) = [F(y)+Q F(Qy)]/2,
    S p_raw(y) = [p_raw(y)+p_raw(Qy)]/2.

Prefer exact incompressibility when computationally practical. For example, represent a smooth vector potential A and pressure, impose the same proper-rotation equivariance on A, and define

    U = curl A.

Check that the projection commutes with curl. Account for the extra derivative cost. A direct U,P network with a divergence residual is acceptable for exploration, but divergence must be independently controlled and reduced during refinement; a small combined loss is not sufficient.

Use smooth activations such as tanh. Do not use a piecewise-linear representation when evaluating the required second or higher derivatives. Do not multiply a divergence-free velocity by a cutoff or tail envelope and assume divergence remains zero; apply such factors at the potential level or explicitly correct the divergence.

Preserve representation flexibility. Hard constraints should implement true symmetry, regularity, or justified gauges. Any additional restriction is an explicitly labeled search branch, not the full problem.

## 6. Normalization and exclusion of false solutions

The profile equations have the genuine spatial scaling freedom

    U_a(y)=a U(y/a),    P_a(y)=a^2 P(y/a),    C_a=a C,    a>0.

Consequently grad U_a(y)=grad U(y/a). In particular, the supremum of vorticity is NOT freely adjustable by this symmetry. Do not impose ||Omega||_infinity=1 or an arbitrary derivative value and call it a gauge.

Use one justified spatial-scale normalization, one pressure-constant normalization, and, when needed, one centering and one angular-phase normalization. For example, ||U||_infinity=1 can fix the scale for a bounded nonzero profile, provided the numerical maximum is actually resolved. Track the core size to prevent escape from the domain. Do not independently fix several amplitudes or Taylor coefficients without counting the available freedoms.

A pressure gauge such as P(0)=0 cannot also be combined with P(infinity)=0 as a second arbitrary normalization. Use one constant gauge; asymptotic tests can concern grad P or P minus its limiting constant.

Explicitly reject zero, constant, globally affine, irrotational, axisymmetric, and boundary-supported artifacts as answers to the main target. Affine Euler profiles can have exactly zero PDE residual for every c_l and can possess genuine n=2 content. Nonzero angular modes alone do not exclude them.

Measure genuine non-axisymmetry using the correct vector group average

    U_axi(y) = (1/(2pi)) integral_0^{2pi} R_{-alpha} U(R_alpha y) d alpha,
    U_nonaxi = U-U_axi.

Also compute the n=2 Fourier energy of cylindrical velocity components on several core regions. A resolvable nonzero n=2 coefficient distinguishes the desired fundamental two-fold branch from an axisymmetric or purely four-fold branch.

Temporary lower bounds on non-axisymmetric content may help initialization. Use several strengths, then relax them and test persistence under the unmodified PDE objective. Do not declare success because an artificial penalty pins a nonzero n=2 component against the PDE. Compare the signal with refinement and validation errors.

Quantify non-affinity by fitting the best affine field on the core and reporting the remaining velocity, vorticity variation, and curvature. Check genuine three-dimensional dependence and stretching rather than mistaking an effectively two-dimensional artifact for the intended result.

## 7. Far field and finite-energy interpretation

The goal is a global similarity profile potentially usable as the inner limit of a solution with smooth finite-energy initial data. Do NOT require U itself to belong to L^2(R^3).

Indeed,

    integral_{|x-x_*|<R tau^{c_l}} |u|^2 dx
        = tau^{5c_l-2} integral_{|y|<R}|U|^2 dy.

This motivates c_l>=2/5 for a nonzero strongly convergent finite-energy core. The initial primary search stays strictly above 2/5; the endpoint requires separate treatment. The profile need not describe the original solution globally in physical space.

Write R=|y| and d=1-1/c_l. A natural candidate matching class is

    U(y) ~ R^d A_infinity(y/R),
    grad U, Omega = O(R^{d-1}) = O(R^{-1/c_l}),
    P-P_infinity ~ R^{2d} B_infinity(y/R),

with unknown angular functions, not prescribed axisymmetric ones. In our primary range, -3/2<d<-1. These are asymptotic search assumptions to test, not a theorem that every possible profile has this form. The velocity must decay; growing affine backgrounds and imposed external strain are excluded.

Do not impose compact support or exponential decay on the entire profile. Do not silently force a faster-decaying vorticity class potentially covered by a Liouville theorem. Check the hypotheses of any exclusion result before applying it.

If using explicit tails, enforce incompressibility of the leading angular field. Writing A_infinity=A_r n+A_T, its condition is

    div_{S^2} A_T + (d+2) A_r = 0.

Allow subleading corrections. In particular, the linear similarity operator annihilates degree d, while convection and the natural pressure gradient are of degree 2d-1. A correction of degree 2d-1 can therefore be necessary. Do not insist that the profile is exactly homogeneous outside a finite radius. Do not assume analyticity at a compactified infinity: that can exclude noninteger subleading powers even when the field is smooth at every finite point.

Use expanding domains plus tail diagnostics. Compare a flexible-tail representation with a tail-informed representation on promising branches. Do not accept a candidate that improves only because its core moves outward, shrinks below resolution, or pushes its transition layer to the outer boundary.

Pressure is nonlocal. Do not accept an arbitrary exterior harmonic field as an unrecorded forcing mechanism. For a serious candidate, examine a whole-space pressure or Biot–Savart consistency check with the tail included, or explicitly report this verification as unfinished.

## 8. Theoretical guardrails and local geometry

Audit [R3] before imposing geometric constraints. Its restrictions are hypothesis-dependent. In particular, do NOT enforce a local-outgoing condition at every stagnation point as a stabilization device for a c_l<1/2 search. Do not transplant an axisymmetric exclusion theorem to every finite-m profile.

Let

    V(y)=c_l y+C e_z+U(y).

The derived vorticity equation is

    Omega + V·grad Omega - (Omega·grad)U = 0.                  (V)

Find and classify zeros of V numerically, including off-axis pairs. Examine the symmetric part of grad V and nearby trajectories, not eigenvalues alone, when discussing a quadratic outgoing inequality.

Useful conditional local check: at an axis stagnation point shifted to y=0, with Omega(0) nonzero, symmetry gives

    grad U(0) = [[a,b,0],[c,d0,0],[0,0,e]],
    Omega(0)=(0,0,c-b).

Equation (V) and incompressibility imply

    e=1,    a+d0=-1.

Thus the trace of the transverse block of grad V is 2c_l-1<0 in our target range. An incoming transverse direction is compatible with, and forced in, this particular branch. Do not impose Omega(0) nonzero on all branches: vorticity may vanish on the axis and concentrate off-axis.

Another independent check: for a nonzero decaying exact profile, at an interior maximum y_max of |Omega|,

    Omega(y_max)·[grad U(y_max) Omega(y_max)] = |Omega(y_max)|^2.

Verify its approximate version at a carefully located maximum. It helps expose tiny-amplitude, nearly linear artifacts. It does not authorize arbitrary vorticity normalization.

## 9. Explicit, smooth, divergence-free seed family

Do not rely exclusively on random networks or unavailable author data. The following is a proposed initialization family, NOT an exact Euler profile.

Choose

    M = [[a,b,0],[c,-1-a,0],[0,0,1]],
    chi(y) = (1+|y|^2)^(-1/(2c_l)),
    A_seed(y) = -(chi(y)/3) [y cross (M y)],
    U_seed = curl A_seed,
    P_seed(y) = -(chi(y)^2/2) y·[(M+M^2)y].

Verify these facts before using it:

- trace M=0, and M+M^2 is symmetric.
- curl[-y cross (M y)/3]=M y.
- U_seed is smooth, divergence-free, and Q-equivariant.
- Near zero, U_seed=M y+O(|y|^3).
- Generically U_seed has an algebraic tail of degree d=1-1/c_l, and P_seed has degree 2d.
- For generic non-axisymmetric choices of M, the n=2 component is nonzero.

One starting choice is a=0.2, b=-0.4, c=0.7, c_l=0.45. Try other compatible matrices and additional off-axis seeds. Fit this family into the chosen network or use it as a base with flexible learned corrections. Do not restrict the final solution to this family, to its angular content, or to its extra accidental symmetries. In particular, release any additional inversion or axial parity of a seed.

The unlocalized affine field U=M y with P=-y·(M+M^2)y/2 is an exact residual unit test for any c_l, but is an inadmissible final answer because of its far field. This distinction must appear in the automated acceptance checks.

## 10. Numerical method and staged experiments

First choose a small, transparent implementation that can be independently tested. Use FP64 for the fields, derivatives, optimizer state, and scalar parameters; verify actual dtypes. Do not silently switch precision on an accelerator.

Suggested sequence:

A. Derive the equations and gauges; implement hard m=2 symmetry and the residuals. Test the exact affine family, symmetry, divergence, chain rules, and Cartesian/cylindrical agreement. Use manufactured smooth fields to test derivatives and residual identities.

B. Benchmark a small network and one seed at fixed c_l=0.45. Establish that the code trains, checkpoints, resumes, and evaluates untouched holdout points correctly. This is a smoke test, not a candidate announcement.

C. This is a 96-hour-minimum campaign, not a one-hour pilot. Test several seeds and fixed exponents, for example 0.49, 0.47, 0.45, 0.43, 0.41, using an explicit experiment queue, early screening, fair baseline comparisons, and continuation between promising runs. A c_l=0.5 control is useful but must not consume the entire search. In particular, search multiple genuinely non-axisymmetric seed families and keep some exploration budget for new branches instead of dedicating all time to the first low-training-loss candidate. An exponent fixed in an input configuration must NEVER be reported as found by optimization.

D. Jointly optimize c_l only after the representation and residuals behave sensibly. A bounded parameterization is allowed, but monitor bound saturation and the true derivative with respect to c_l. Refine promising values using neighboring fixed-c_l runs and a locally free c_l fit. A prescribed exponent is not an exponent discovered by the solver.

E. Refine the best genuinely non-axisymmetric branches with more capacity, more angular/spatial resolution, larger domains, and a different seed or representation. Add small correction networks when useful; all corrections must preserve hard symmetry and incompressibility.

Start with a robust first-order optimizer if needed. Prefer a verified curvature-aware implementation where available; SS-eSOAP and SS-Broyden are options, not required brand names. A documented Adam-to-L-BFGS fallback is acceptable. Estimate memory before any dense quasi-Newton state. During deterministic line searches, keep the objective and collocation set fixed; when changing them, handle optimizer history explicitly.

For wide-range sampling, consider sinh/asinh coordinate maps or a core-plus-logarithmic-shell sampler. Derive physical-coordinate derivatives and Jacobians. A huge transformed box does not, by itself, verify the infinite domain.

Sample the core, the axis and near-axis tube, intermediate shells, far-field shells, and low-transport regions. Combine baseline coverage with residual-adaptive points. Do not resample away a difficult region. Maintain validation and final-audit sets distinct from training; once a validation point drives training, it is no longer untouched holdout data.

A loss may combine momentum, divergence when needed, asymptotic matching, residual-derivative control, gauges, and temporary nondegeneracy constraints. Log every component separately. Do not make a component disappear by shrinking its learned weight. Derivative-of-residual penalties are not penalties forcing the physical velocity gradient to be small.

## 11. Independent validation and quantitative reporting

Recompute the following from saved parameters:

    R_m = (1-c_l)U + V·grad U + grad P,
    R_div = div U,
    R_omega = Omega + V·grad Omega - (Omega·grad)U,
    R_P = -Delta P - sum_{i,j}(partial_i U_j)(partial_j U_i).

The last two identities assume incompressibility; account for any divergence defect when comparing residual identities. Use an independently implemented validation path, Cartesian/cylindrical comparison, and selected finite-difference or interpolation checks. Reusing the same faulty derivative routine twice is not independent validation.

Report both absolute residuals and meaningful relative residuals. For example, on a finite physical-coordinate region D,

    eps_m(D) = ||R_m||_L2(D) /
      [(1-c_l)||U||_L2(D) + c_l||y·grad U||_L2(D)
       + |C| ||partial_z U||_L2(D)
       + ||(U·grad)U||_L2(D) + ||grad P||_L2(D)].

A nearly zero denominator is a degeneracy flag, not a reason to add an arbitrary large floor. Report eps_div relative to ||grad U||, and analogous term-normalized vorticity and pressure defects.

Use physical volume dy=r dr dtheta dz when reporting physical L^2 norms. Computational-coordinate MSE is a different quantity. Provide region-by-region RMS, high quantiles, and sampled maxima. Never call a sampled maximum a rigorous L-infinity bound.

Far-field linear terms may cancel at leading order while nonlinear terms are much smaller. Check the residual also at the nonlinear/subleading scale, typically R^{2d-1}; a normalization dominated by two large cancelling linear terms can conceal a bad tail.

Every serious candidate must be tested for:

1. Momentum, divergence, vorticity, and pressure consistency on independent points.
2. Exact m=2 symmetry, resolvable n=2 content, and absence of enforced extra symmetries.
3. Nontrivial vorticity, non-affinity, and genuine three-dimensional structure.
4. Axis regularity and bounded, convergent derivatives near all problematic regions.
5. Stable core shape and exponent under capacity, sampling, domain, and tail-model refinement.
6. No unresolved high angular modes or nonlinear aliasing.
7. Nondegeneracy after relaxing temporary symmetry-breaking penalties.
8. Stagnation-point geometry, peak-vorticity stretching, and compatibility with exclusion theorems.

As initial screening goals, seek regional relative momentum RMS below 1e-3. Aim for 1e-5 or better and substantially smaller divergence defects before describing a branch as a strong numerical candidate. Also report the other residuals and sampled maxima; these goals are not universal proof thresholds. A convergent sequence of independent tests matters more than a small aggregate training loss.

For a claim of a numerically resolved c_l<0.5, report the gap 0.5-c_l alongside exponent changes under free refits, discretization, domain enlargement, and tail changes. If these effects are comparable to the gap, label the result unresolved. Do not manufacture a statistical confidence interval from optimizer output.

## 12. Navier–Stokes relevance: a diagnostic, not a conclusion

With s=-log(tau), the corresponding rescaled NS equation is

    partial_s v + (1-c_l)v + (c_l y+v)·grad v + grad P
        = nu exp[-(1-2c_l)s] Delta v,
    div v=0,

in canonical coordinates. For fixed positive viscosity, c_l<1/2 makes the coefficient decay; c_l=1/2 does not.

For the best candidate, evaluate Delta U in stated core/tail-weighted diagnostics and report how large the viscous defect would be relative to the retained terms. Check derivative growth under refinement: a small scalar viscosity coefficient cannot compensate automatically for unresolved curvature.

Do not claim NS blowup from an Euler profile. Additional stability or a controlled unstable manifold, finite-energy outer matching, pressure control, and a construction from one fixed physical initial condition remain necessary. Optional linearized or short rescaled-dynamic tests may be done only after a credible profile exists. Finding an unstable stationary profile is still meaningful; do not reject it solely because forward relaxation does not converge to it.

## 13. Minimum 96-hour campaign: execution, hardware, monitoring, and resumption

THIS TASK IS EXPLICITLY AUTHORIZED AS A LONG-RUN RESEARCH CAMPAIGN. The requested minimum is 96 hours of MEASURED ACTIVE NUMERICAL EXPERIMENT TIME, accumulated over one or more safe sessions. Count actual non-overlapping wall-clock time spent running substantive optimization, simulation, or independent numerical validation. Exclude idle time, waiting for a human, suspended jobs, literature reading, environment setup, drafting reports, and offline periods. Do not multiply elapsed time by the number of parallel workers; concurrent 4-hour jobs count as 4 hours, not 16 hours. Log start/stop timestamps, resumed intervals, hardware, and the specific experiment ID for every interval. 96 hours is the minimum search budget, not a claim that a solution must exist or can be found within 96 hours.

Before computing, inspect the actual machine, current CPU/GPU use, memory and swap pressure, available RAM, disk, and existing jobs. Do not assume a GPU, a remote host, or access to the authors' hardware. Create a new isolated project directory. Do not modify unrelated repositories, manuscripts, prior experiments, global environments, or running jobs. Do not start external paid compute or connect to an unconfirmed remote machine. If an explicitly permitted and already configured remote computing host exists, prefer it over monopolizing a personal laptop; otherwise keep the laptop responsive.

Use hardware-conscious defaults and adapt them to measured machine capacity. On a personal laptop start with one worker and 1-2 numerical CPU threads or a demonstrably low-impact accelerator allocation, keep memory and disk headroom, set conservative process priority, monitor temperature/throttling where possible, and pause or lower load if swap or responsiveness deteriorates. A small four-hidden-layer width-32 model is an initial benchmark, not the final model. Prohibit silent, unlogged orphan workers. Long-running computation must use a supervised job runner or a clearly documented, user-authorized scheduler, with visible status and a reliable stop mechanism.

### Required campaign milestones (measured ACTIVE experiment hours)

- 0-6 h: Complete derivation/unit tests, end-to-end FP64 pilot, a first seed, and an exact-resume test. The hours used for reading/coding are NOT counted toward the 96-hour active-compute requirement. Correct the implementation before scaling up.
- 6-24 h: Explore multiple fixed c_l values and genuinely non-axisymmetric seeds, with independent training/holdout data. Include a baseline at c_l=1/2 for diagnosis, but keep the objective focused on 0.4<c_l<0.5. Save negative results and failure modes rather than only successful runs.
- 24-48 h: Extend the parameter/seed search and compare at least two reasonably different representations, initialization families, or optimizer strategies where practical. Use staged resolution, increasingly faithful tail constraints, and wider domains. Check for collapse to zero, axisymmetry, or affine artifacts.
- 48-72 h: Continue searching and invest serious refinement in the best branches. Where a candidate appears promising, jointly fit c_l, remove artificial anti-axisymmetry penalties, add higher angular content, and validate on expanded holdout shells. If nothing survives, redirect experiments to different seeds, flow geometry, or parameterizations; do not spend 24 hours polishing a known invalid artifact.
- 72-96 h: Adversarial verification of the strongest branches, refining high-error regions, axes, tails, pressure consistency, independent vorticity/Poisson checks, and c_l sensitivity. If no serious candidate exists, use this block for new systematic searches rather than idle validation. The 96-hour milestone is reached only after the measured active time is genuinely >=96h.
- After 96 h: Finish the currently meaningful experiment and issue a truthful final status, or continue longer if already authorized resources and promising follow-up experiments justify it. Do not invent successful outcomes to fill the target, and do not silently stop at 24, 48, or 72 hours because training plateaued.

The allocations above are guidelines, not rigid optimization quotas. Reallocate when evidence warrants, but the completed campaign must include both broad exploration and serious independent validation. Keep a best-candidate checkpoint and a diverse archive of alternatives; never overwrite all early candidates with the latest optimization state.

### Monitoring and lifecycle

- Store a machine-readable campaign ledger containing active_seconds, experiment IDs, start/end timestamps, configuration hashes, input/checkpoint hashes, machine/precision, metrics, interruptions, and reason for each branch change. Count non-overlapping active time across all workers.
- Write an atomic checkpoint frequently (initially every 10-30 minutes, and before any planned shutdown), plus a compact progress report at roughly 6, 12, 24, 48, 72, and 96 cumulative active hours. Reports must state measured progress and the strongest surviving numerical evidence, not just optimizer loss.
- Implement one-command launch, status, STOP, and RESUME commands. Test resume fidelity and make the queue resumable without replaying completed experiments. Use an interruption-safe mechanism actually supported by the environment. If the agent platform or terminal session has a lifetime limit, checkpoint before exit; do NOT claim autonomous future execution unless a real persistent job/scheduler has been configured and is operating. Supply the literal next command needed for a human/agent to resume.
- Add guardrails for disk exhaustion, runaway gradients/NaNs, memory pressure, failed checkpoints, and persistent mismatch between training and validation residual. Such failures trigger mitigation or safe suspension, not fabricated elapsed time.
- A rigorous mathematical obstruction covering the whole explicitly specified search class, if truly proved and independently checked, supersedes further blind numerical work. Otherwise do not treat lack of convergence as a proof of nonexistence. Safety/permission/resource constraints may force an earlier stop; state the blocker and actual active hours exactly.

Save model, optimizer, scalar parameters, random-generator state, sampling state, configuration, active-time ledger, and progress atomically. Test an interrupted-and-resumed run against a continuous run. A later CONTINUE instruction must resume the best current branch and its queued experiments, not restart the project or repeat the literature review.

## 14. Required deliverables and final status

Provide a reproducible project with:

- EQUATIONS.md: conventions, derivations, gauges, symmetry, and tail assumptions.
- SOURCE_NOTES.md: source versions, what was borrowed, and what was changed.
- Runnable training, validation, tests, and resume/reproduction commands.
- Configuration, saved candidates/checkpoints, and machine-readable experiment tables.
- REPORT.md: best result, regional residuals, exponent sensitivity, angular spectra, axis/tail tests, rejected artifacts, resource usage, and remaining gaps.
- STATE.json and NEXT_STEPS.md: exact restart state, cumulative non-overlapping active numerical hours, and the next prioritized experiments.
- CAMPAIGN_LEDGER.jsonl (or equivalent): independently auditable run intervals and per-experiment results.
- run/status/stop/resume scripts, with the exact command that restores work after any execution-session interruption.
- Progress snapshots at approximately 24, 48, 72, and 96 cumulative active hours, with independent validation summaries.

The report must explicitly answer:

Did we obtain a genuinely non-axisymmetric m=2 candidate? Is c_l numerically resolved below 1/2? Does the candidate survive removal of artificial nondegeneracy constraints and refinement? What is the worst validated region? Is the tail credible? What prevents a stronger conclusion?

Use an honest status such as STRONG NUMERICAL CANDIDATE, PRELIMINARY CANDIDATE, NO ACCEPTABLE CANDIDATE FOUND IN THIS SEARCH, or RIGOROUS OBSTRUCTION UNDER EXPLICIT ASSUMPTIONS. The last status requires an actual proof, not failed optimization.

Do not stop after producing a plan, code skeleton, or one-hour pilot. Carry out the authorized >=96-hour ACTIVE numerical campaign when the environment permits, with substantive experimentation and independent validation. If execution limits, hardware protections, or permissions prevent completion in the current session, checkpoint and state actual active hours and a precise continuation command, never pretend that 96 hours were completed. The success criterion is credible mathematical/numerical evidence, not simply spending compute or lowering a training loss.
