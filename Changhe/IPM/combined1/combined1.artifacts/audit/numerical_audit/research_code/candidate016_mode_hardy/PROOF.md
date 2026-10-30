# Candidate016: complete angular-divergence upper bound for the negative norm

## Exact statement and hypotheses

Fix c=4076476460239181/2251799813685248, gamma=1/c and delta=1-gamma.
Let chi be the exact rational potential of C1-N1-016-legqs25-quot013,
coefficient SHA256
a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42.
Its generator convention is that of ../joint_scaled_factored_weak/PROOF.md.
Put rho=-partial_y Delta chi, u=(-chi_xyy,chi_xxy), and
F=(cX+u).grad rho-rho. Let r=|X|, t=r^2/(1+r^2), v=1-t.
All functions and coefficients below are real. L2 norms use ordinary
Lebesgue measure on R2 and the complete angular interval[0,2pi].

Define the homogeneous negative norm by

 H(F)=sup {|integral F phi| : phi in C_c^infinity(R2), ||grad phi||2<=1}.

Equivalently, when finite this is ||(-Delta)^(-1/2)F||2 with the unitary
Fourier transform and multiplier |xi|^-1. The proof below uses the dual
definition and does not require a numerical Fourier transform.

Suppose F is a finite pure sine series

 F(r,theta)=sum_(n in E) f_n(r) sin(n theta), E subset positive integers,

and rF belongs to L2(R2). Then

 H(F)^2 <= B^2 := sum_(n in E) ||r f_n(r) sin(n theta)||2^2/n^2.       (1)

For the specified candidate, the exact checker must establish its full
sine-only representation, every nonzero frequency in E, all complete
weighted radial integrals, and containing intervals for B. Only a passing
computation establishes a numerical upper bound. The proposed independent
comparison is with every row of the frozen N3 Hardy record, never with a
truncated angular sum. B is an upper bound for H(F), not its exact value.

## Proof of the negative-norm estimate

In polar coordinates define the tangential vector field

 A(r,theta)=-e_theta r sum_(n in E) f_n(r) cos(n theta)/n.

Angular orthogonality gives

 ||A||2^2=pi sum_(n in E) n^-2 integral_0^infinity r^3 f_n(r)^2 dr=B^2.

The sine and cosine angular square integrals are both pi. Since n>=1,
B<=||rF||2, so A is an L2 vector field. For any smooth compactly supported
phi, Fubini and integration by parts on the angular circle give

 -integral A.grad phi
 =integral_0^infinity integral_0^(2pi)
       sum_n f_n(r) cos(n theta)/n * partial_theta phi * r dtheta dr
 =integral F phi.

The first expression is absolutely integrable by Cauchy-Schwarz. The
identity first holds on annuli; radial boundary contributions vanish
because A is tangential. At the origin the smooth finite candidate F and
compact test make the limiting identity valid. More generally the same
identity follows by angular integration and L2 approximation whenever the
left and right distributional pairings exist. Thus div A=F in
distributions. Cauchy-Schwarz proves

 |integral F phi|<=||A||2 ||grad phi||2,

which proves(1). In particular no orthogonality assertion about the
negative norm itself is needed. If desired, the Fourier characterization
follows from Fhat=i xi.Ahat and the Riesz representation of the continuous
functional on the closure of compactly supported gradients.

## Exact reconstruction and complete mode integrals

Reconstruct F from the raw potential using the exact Laurent-product
algorithm proved in ../scaled_product_norms/PROOF.md. It gives

 f_n(r)=r sum_ell v^(ell delta/2) A_(ell,n)(t),

where A is a rational function whose only permitted denominator factors
are1+a v, a in{99,624,2499,9999}, with nonnegative integer powers. The
actual016 input uses only624. Every factor is positive on[0,1]. Reject
any cosine component, zero frequency or missing declared frequency.
Recompute the canonical representation hash from every exact numerator,
denominator exponent and(ell,kind,n) key. Require equality with the exact
F representation already checked against Cartesian jets in the own
full-norm production. A hash match is a compact binding to that checked
representation, not a substitute for the present reconstruction.

For each fixed n, expand every ordered pair of branches and combine terms
with the same branch sum E. Write the resulting rational function as
G_E(t). The complete mode square is

 ||r F_n||2^2 = (pi/2) sum_E integral_0^1
                         v^(E delta/2-4) (1-v)^2 G_E(1-v) dv.       (2)

Indeed rF_n=r^2 sum v^(ell delta/2)A, r dr=-dv/(2v^2), and
r^4=(1-v)^2/v^2. This accounts for the complete Jacobian, both radial
factors and the angular integral pi. Exact polynomial division extracts
all powers v^q from each numerator. Require

 E delta/2-4+q > -1

for every nonzero complete group before evaluating any integral. A failed
endpoint test leaves the mode OPEN; analytic continuation is not used.

Use exact rational partial fractions and the outward positive-pole
moment algorithm in ../rational_pole_moments/PROOF.md. Replay the exact
common-denominator identity. Every nonzero complete moment and each final
positive mode square must have more than150 relative accuracy bits. Sum
all complete groups before taking square roots. No finite-radius cutoff,
angular sampling, quadrature, omitted mode or tail approximation occurs.
Since the series is finite, its summed mode squares equal||rF||2^2
exactly. Compare this independent sum with the previously accepted rF
interval as an additional normalization check.

## Independent comparison and optional energy consequence

Freeze the N3 Hardy JSON and its code as text. For each mode compare all
three displayed balls: rF_n squared, rF_n and rF_n/n. They must contain
the own intervals. Require the exact same frequency set and complete
component counts after the documented representation conventions are
accounted for. The total B must lie in the displayed H_upper_ball. The
long H_upper string is an outward endpoint, not a ball necessarily
containing B; verify its direction against the independently computed B.
The historical N3 record binds its entry script, raw-candidate hash and
cache pathname, not every dependency or the cache's bytes. The present
reproduction certifies the numerical table for the actual raw candidate,
without claiming to have observed that earlier cache or execution.

If independently accepted intervals for G0=||F||2, G1=||grad F||2 and
P2=||(1+4r^2)^(2/5) D2F||2 are available, define

 E2^2=P2^2+2^14 G1^2+2^18 G0^2+2^18(20/21) H(F)^2.

Nonnegativity gives the lower bound obtained by dropping H(F)^2. Inserting
B for H(F) gives an upper bound. Directed interval arithmetic supplies
explicit rational lower and upper endpoints. This consequence is
conditional on those component acceptances until they are bound by the
checker. It asserts no inverse, smallness condition, nonlinear closure or
existence result. It does not set H(F)=B.

## Source and restart discipline

Write this proof before its checker. Bind the complete own module graph,
accepted exact Laurent fixtures, candidate JSON and manifest, the frozen
N3 comparison inputs and the accepted own F/rF record before arithmetic;
recheck all hashes afterward. Import no peer implementation. The checker
uses own packed-field and rational-moment modules and its own mode loop.
It does not import the full production fixture helper that initializes
peer modules. Save each completed mode immutably; on restart rebind all
its inputs before reusing it. A failed check, omitted mode or unfinished
calculation leaves the corresponding result OPEN.
