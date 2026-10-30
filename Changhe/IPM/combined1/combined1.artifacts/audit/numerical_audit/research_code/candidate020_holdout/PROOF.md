# Candidate 020: exact shapes and recorded analytic objective span

## Statement, notation and hypotheses

Fix c=4076476460239181/2251799813685248, gamma=1/c and delta=1-gamma.
Set S=1+x^2+y^2, r=sqrt(x^2+y^2), t=r^2/S,
p_j=(3+gamma-j delta)/2 and H_m=Re(x+iy)^(2m). Let P_N denote the
Legendre polynomial with P_N(1)=1. The immutable candidate is
C1-N1-020-legqs25p50-quot013, with raw coefficient SHA256
bddbd3120852a815cfe850635564cb09ab52a98ec596a4cce3b72c98cf04f7cf.
Its potential generator shapes consist exactly of the 1922 shapes in the
accepted exact quotient of candidate 013 and the following 504 shapes:

 G_RjmN=H_m S^(p_j-m) [R^2/(R^2+r^2)]^4
                    P_N(2r^2/(R^2+r^2)-1),
 R in {25,50}, j in {1,2,3}, m in {9,...,15}, N in {0,...,11}.

Subject to the independently proved dimension theorem stated below,
these 2426 potential functions, and their densities -partial_y Delta G,
are linearly independent. This concerns the generator space, regardless
of which coefficients happen to vanish in the candidate. It gives no
conditioning estimate, optimizer minimum, inverse or existence theorem.

For odd n and integer K >= (n-1)/2 define
phi_(n,K)=r(1+r^2)^(-2)t^K sin(n theta). The recorded optimization history
007 -> 013 -> exact quotient -> 016 -> 020 uses the following analytic
weak-probe rows in its last stage: 27 first-mode rows with
K in {0,1,2,3,4,5,6,7,8,12,16,24,32,48,64,96,128,192,256,384,512,
768,1024,1536,2048,3072,4096}, and 40 rows with n in {3,5,...,17},
K=(n-1)/2+s, s in {0,8,32,128,512}. All earlier analytic weak rows in
this recorded history are contained in this 67-row list.

Every one of the 25 registered probes n in {19,23,25,29,31},
K in {600,900,1200,1800,2400}, and the separate diagnostic (21,522),
lies outside the real span of these analytic weak rows. This statement
makes no claim about sampled residual information, statistical
independence, blindness, or earlier unrecorded experiments.

## Proof of the objective-span claim

For r>0, divide a proposed finite linear relation by the positive
factor r(1+r^2)^(-2), then take its sine-n Fourier coefficient on the
whole circle. Every objective row has angular frequency at most 17,
so its coefficient is zero at the frequency of any listed probe.
The probe contributes t^K>0 for 0<t<1. This contradicts the relation.
An a.e. equality gives the same conclusion for almost every radius;
a distributional equality between these smooth functions implies
pointwise equality. Repeating previously used rows cannot enlarge the
span. The prior accepted candidate016 objective audit binds the earlier
stages and proves that their rows are already in the same list.

The condition 2K+1>=n ensures smoothness at the origin: write
r^(2K+1)sin(n theta) as the degree-n harmonic polynomial times the
even radial power r^(2K+1-n). The rational denominator is smooth and
positive. At infinity phi=O(r^-3) and its gradient is O(r^-4).
The complete weak-distance theorem and its cutoff hypotheses are in
../joint_scaled_factored_weak/PROOF.md. No numerical distance follows
from the span argument alone.

## Proof of the shape and dimension claim

The accepted dependency ../joint_scaled_rank_peer/PROOF.md proves that,
for exactly the c, old quotient basis and 504 functions specified above,
the potential span has dimension 2426 and the density map
chi -> -partial_y Delta chi is injective on this span. Its hypotheses
include separate evenness and smoothness, branch exponents p_j and
p_j-p_k nonintegral, growth exponent 3+gamma<4, and distinct positive
physical radii 25 and 50. These are the same exact data as here.
Its proof separates angular harmonics and fractional branches, then
uses the distinct auxiliary rational poles v=-1/624 and v=-1/2499 to
eliminate the new Legendre coefficients in descending pole order.
Its density argument reduces a kernel element to a separately even
quadratic polynomial by harmonic derivative estimates; fractional
branch separation excludes that polynomial. Both independent exact
witness records and the full analytic proof have been accepted.

The present checker compares all 2426 raw shapes, in order and as a
set, with that accepted abstract list. It also verifies that the first
2174 shapes are exactly candidate016's and that precisely the 252
radius50 tuples are appended. The exact value of c is unchanged.
Therefore the raw candidate's generator space is exactly the space
of the dependency, and its two dimension conclusions apply. No rank
claim is inferred from an approximate numerical matrix.

## Recorded provenance and scope

Compare the immutable coefficient metadata with the complete launch
script, completed log and accepted parent016 audit. Check the actual
parent filename, generator addition setting, row list, 12 steps,
MID16 radial rule, angular count180, pairing weight10^12, and output
hash. Read the optimizer source as text and compare its bytes with the
previously frozen source. This source hash is not a claim that these
bytes were historically executed; the launch, log and final metadata
are the evidence for the recorded analytic objective.

The initial radius50 coefficients are zero in the inspected source;
the final exact candidate coefficients need not be zero. The old
public 25-probe register predates the immutable snapshot. Selection
of a probe after a FLOAT screen is allowed and is not evidence of a
maximum over all probes. Only own verification code is executed.
Independent candidate-specific point, sector and weak checks remain
separate from this exact provenance and shape comparison.
