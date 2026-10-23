# Draft 48 audit: logarithm propagation, inversion degree and numerical transcription

Written 2026-10-21 before this result's supporting code. Verifier result153. This is an audit of a frozen report, not a new existence or nonexistence theorem. Source hashes are in verification/manifest.json. The frozen report has SHA256 76bc73847acb08c54ba598f6104922691be9095d179f0f5d27c6386a7f4e8054.

## 1. Objects and scope

Use ell>1, p=1/ell, delta=1-p and Setting III parities: rho is even in x and odd in y; the canonical stream solves -Delta psi=rho_x, U=(-psi_y,psi_x), U=o(r). Outside a disc suppose (ell X+U).grad rho=rho, rho and U have the all-order symbol bounds S^p, and r^(-p)rho tends uniformly to a smooth angular trace Theta. The standalone expansion proof is ../smooth_angular_far_field/PROOF.md. Its hypotheses, construction of the canonical full-plane inverse, cutoff multipoles and finite-depth remainder estimates are explicit there. This audit checks the new statement3.68 and appendixA.3.68 against that proof and checks numerical claims against independently recomputed saved data from results144 and147. It does not rerun the entire historical report or all producers' solves.

For this proof m is the positive even stream frequency. The report indexes the same frequency as 2j, j>=1. Its harmonic velocity degrees -2j-1 are exactly our -m-1. Let A={p-k delta-2l:k,l>=0 integers} and H={-m-1:m>=2 even}. Equal numerical degrees and logarithmic coefficients must be collected.

## 2. Resonance introduces logs; lower nonresonant terms can retain them

Draft3.68(c) says that, for rational delta, 'a logarithm can occur only at a degree p-k delta-2l=-2m-1'. This is not the conclusion of the expansion proof. The proof restricts where inversion can first introduce a logarithm into logfree data, not all degrees at which a logarithm can subsequently occur.

To see the distinction directly, put z=log r. At density degree s, a source r^(s-1)G(z,theta) is inverted using a stream r^(s+1)Q(z,theta), where

    [-partial_theta^2-(s+1)^2-2(s+1)partial_z-partial_z^2]Q=G.  (1)

On sin(m theta) the diagonal coefficient is m^2-(s+1)^2. If it is nonzero, a source with a nonzero coefficient g_d z^d at its largest log power has solution coefficient q_d=g_d/[m^2-(s+1)^2], which is nonzero. Nonresonant inversion preserves an existing log; it does not remove it. At s=-m-1 the equation becomes -Q''+2mQ'=G, so logfree nonzero G produces one power of z. Products then also carry such logs to other degrees. The radial transport inverse

    Tf(r)=ell^(-1) r^p integral_r^infty t^(-p-1) f(t)dt

preserves a nonzero highest log coefficient at every degree s<p, multiplying it by 1/[ell(p-s)]. None of these statements requires a convergent infinite expansion.

A concrete conditional consequence is supplied by result150. Assume Theta=A0 sin(theta), A0!=0 and ell=3. That result proves that the stream contains

    (g/4) r^(-2) log r sin(2theta),
    g=-(177047/301056000000) A0^6 !=0.                    (2)

Its polar velocity at highest log power is -(g/2)r^(-3)log r times (cos2theta,sin2theta). Advecting the leading density A0 r^(1/3)sin(theta) gives highest-log forcing

    -(A0 g/4) r^(-11/3) log r
           *[(2/3)sin(theta)+(4/3)sin(3theta)].           (3)

The linear transport coefficient at degree -11/3 is ell(-11/3-p)=-12. Since transport plus advection is zero, (3) yields the density term

    r^(-11/3) log r
           *[-A0 g/72 sin(theta)-A0 g/36 sin(3theta)].   (4)

Its degree -11/3 is not a negative odd integer, hence does not belong to H. Both angular coefficients in (4) are nonzero. The uniqueness of finite asymptotic coefficients makes these actual conditional coefficients of any exterior profile satisfying the hypotheses, not terms removable by choosing a different expansion. Global harmonic multipoles are logfree at this order and cannot cancel them. The corresponding ell=5/2 consequence has density-log degree -28/5, also outside H; its coefficients are those in result150.

This is not an existence counterexample to a universal assertion about an as-yet unproved branch. Existence of such exterior/global profiles is not supplied by result150. It is a definite counterexample to the claimed algebraic restriction on logarithm propagation in the finite-depth construction and an explicit conditional implication incompatible with that restriction if the pure-trace branch exists. The report should state the proved rule only: a first logarithm can arise from a Poisson resonance s=-2j-1; subsequent logarithms can propagate to lower, nonresonant density and velocity degrees. Irrational delta rules out the first resonance and therefore rules out every log. The rational divisibility condition (k+1)u=2vJ, j=J+l-1>=1, remains correct for a resonant inversion.

## 3. Log-degree bound in the resonant mode

AppendixA.3.68 Step2'' calls d the degree of the full angular polynomial P, then writes that Q_m 'has degree d+1'. In fact it has degree at most d+1. It can vanish identically, or have a smaller degree, if the projection G_m has smaller degree or vanishes. If G_m is a nonzero polynomial of degree e, the finite formula

    V=sum_(i=0)^e G_m^(i)/(2m)^(i+1), Q(z)=integral_0^z V(t)dt

gives degree exactly e+1. Its leading coefficient is the leading coefficient of G_m divided by 2m(e+1), which is nonzero. With the report's frequency2j replace2m by4j.

For example s=-3 and P=sin(3theta) give, by direct Cartesian differentiation in polar form,

    partial_x[r^(-3)sin(3theta)]=-3 r^(-4)sin(4theta).

The possible resonant stream frequency is2, but its source projection is zero and Q_2=0. The source degree in log is0 while the resonant solution does not have degree1. By contrast P=sin(theta) gives source -2r^(-4)sin(2theta), and the particular stream is -(1/2)r^(-2)log r sin(2theta). This also checks the normalization and sign.

## 4. Remaining analytic changes

The external referee aud21 zero-trace repair is correct. A compact density rho=y eta(r^2), eta smooth, compactly supported, nonnegative and nonzero, has trace0 and exterior equation0=0. Its nonzero canonical quadrupole gives velocity of degree-3, with no degree-p term. Thus the finite velocity expression need only belong to S^p; its degree-p coefficient, if nonzero, is logfree. The repaired Step3' says precisely this and its proof uses no nonzero leading velocity. The own proof was repaired likewise and its5722 exact supporting checks rerun. The external audit's failed Opus request is not an Opus review; the lead's separate actual Opus5.5 hand review is archived independently.

The smooth angular inversion has denominator4j^2-(s+1)^2 and rapid Fourier decay. The compact-source multipole bound is C_L j^(-L)(2R1)^(2j+2)/[4j(2j+2)], giving differentiated geometric tails outside4R1. These factors agree with the own full-plane inverse. The sign of the transport inverse and the loss-free product bound S^(p+b-1) agree. The induction descends in steps greater than delta/2; uniqueness follows by dividing a largest nonzero degree/log-power difference by that monomial. Neither a same-order nonlinear equation nor an assertion of infinite-series convergence is introduced.

The dynamic rescaling change of variables and its corrected finite-time integral criterion match result149. For a steady state to give a Setting III candidate one needs BOTH cw>0 and cx/cw>1. The new Section7 writes cw>0 but omits the second condition; add it explicitly. Algebraic division rho*=rho/cw by itself works at other ratios, but those ratios are outside the task's admissible range. The slope gauge, e_tau=-2cw e-f and cw=-f/(2e), and the warning about a time-dependent radial map are correct.

## 5. Numerical transcription method and result

For N36, read the own frozen binary-coefficient state and the previously independent144 summary: same N24 seed,1000 evaluations, a=22.7932978879435, c=-1.5 within6e-14, Delta=-5.73624412852878e-14. Canonical selected ratios are NF=1.96567881169529e-7 at(0,0.758632161037305) and NV=1.36913873992965e-7 at(0,0.760681974293331). The first absolute residual is6.0987940e-6 and local-grid absolute maximum6.1157948e-6. Slopes drift4.222256percent fromN32 while NF decreases20.855495percent. The inverse changed atN36, so this is not an experiment changing only resolution. The stored binary exponent has ell*p_saved-1=2^-54; its absolute residual grows to about1.44628e85 near1e250. The table's high derivative norms and the raw Cartesian near-axis cancellation witness are rounded consistently. These are finite-point and exact finite-formula facts, not uniform error bounds or a limiting solution.

For the24 low-slope states, use the separately parsed exact coefficients from147. Let a=B0(-1), d0=B0'(-1), b1=B1(-1), b_c=2d0-a+b1, e_c=2d0-a-b1, ell_c=L2^(-kappa). Direct Taylor expansion gives

    rho=y[a+(b_c x^2+e_c y^2)/ell_c^2+O(r^4)],
    q=rho/(a y)=1+(b_c x^2+e_c y^2)/(a ell_c^2)+O(r^4).

All24 have a>0. Exactly21 have e_c/a>0, so q>1 on the punctured small y-axis, including all12 releases. The other3 have both b_c/a and e_c/a negative, hence q<1 on a punctured sufficiently small disc, while the global q<=1 condition remains OPEN. They are exactly lsF_cl1.5_N96_a0.75, lsF_cl3.0_N64_a3 and lsF_cl3.0_N96_a3. Each starts at a/D=1.5. The report names them correctly. Six initial64x16 releases leave the low-slope regime on their first accepted steps;96x24 continuations begin outside, and the cl1.5,a/D0.5 continuation accepts no step. The two resolution-specific ell triples are distinguished correctly. These claims follow from the frozen logs and exact coefficient audit, not from trusting the producer table's residual columns.

The six inverse-comparison maximizers in4.7(c) now correctly belong to the checker's canonical evaluation on the producer's sample sets. This audit does not extend those six-point comparisons to other states or assert their causal mechanism.

## 6. Verdict and dependencies

CONFIRMED: the stated numerical repairs, N36 numbers and limitations, the zero-trace repair, the angular inverse constants and finite-depth induction, and the corrected dynamic-rescaling formulas.

REFUTED as an algebraic inference: restricting every logarithmic degree to resonant degrees. CORRECTION REQUIRED: narrow3.68(c) to first-generation resonance and allow subsequent propagation; change 'degree d+1' to 'at most d+1'; add cx/cw>1 for a Setting III steady candidate. Conditional pure-trace calculations do not assert existence.

OPEN: global existence or nonexistence, convergence of the numerical sequence, and a decisive endpoint. The report must not use this audit as permission to finish the unattended run.

Dependencies: own results142,144,147,149,150 and their exact/numerical evidence. No producer code is imported or executed. The supporting checker for this audit will use only frozen summaries plus independent exact low-degree polynomial identities and rational arithmetic. No servers, JavaScript/TypeScript, RLScience cluster, Lean/Lake or external posting is involved.
