# Candidate 023: two-scale dimension and recorded probe history

## Exact statement and notation

Fix c=4076476460239181/2251799813685248, gamma=1/c, delta=1-gamma,
p_j=(3+gamma-j delta)/2, S=1+x^2+y^2, r=sqrt(x^2+y^2),
v=1/S and H_m=Re(x+iy)^(2m). The accepted old quotient space has
1922 basis potentials H_m S^(p_j-m) P(t), where t=1-v, P is a
polynomial and j is in {0,...,7}. Its basis and independence are the
dependency ../optimizer_quotient_audit/PROOF.md. Adjoin, for each
R in {25,100}, j in {1,2,3}, m in {9,...,15} and N in {0,...,11},

 G_RjmN = H_m S^(p_j-m) [R^2/(R^2+r^2)]^4
                         P_N(2r^2/(R^2+r^2)-1),

where P_N is the Legendre polynomial with P_N(1)=1. The resulting
2426 potentials are linearly independent, and the density map
D chi=-partial_y Delta chi is injective on their real span.

The immutable candidate is C1-N1-023-legqs25p100-quot013, raw SHA256
d67bdd9ff05917736e686af5f834a2e12afede891098ccf8f9de8a6e2d7a71df.
Its full ordered shape list must match precisely this basis. Its
phase-one raw hash is
637ae589e19d01a4bb355c2935cae1883c718b0d1e467d5151e8ce2482635ceb,
and that phase starts from candidate 016, raw hash
a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42.
The phase-one addition is exactly the 252 radius-100 functions above.

For odd n>0 and integer K>=(n-1)/2, define
phi_(n,K)=r S^(-2) (r^2/S)^K sin(n theta).
The two recorded 023 stages have exactly the same 67 analytic weak
objective rows as 016: 27 first-mode K values

 0,1,2,3,4,5,6,7,8,12,16,24,32,48,64,96,128,192,256,384,512,
 768,1024,1536,2048,3072,4096,

and 40 rows n=3,5,...,17, K=(n-1)/2+s, s in {0,8,32,128,512}.
The 25 publicly registered pairs n in {19,23,25,29,31},
K in {600,900,1200,1800,2400}, and the 35 diagnostic pairs
n=19,21,...,31, K=(n-1)/2+s, lie outside their real analytic span.
Historical scope is the recorded chain 007 -> 013 -> exact quotient
-> 016 -> 023 phase one -> 023 phase two. No earlier, unrecorded,
statistically independent or blinded history is asserted.

## Potential independence

Angular orthogonality separates cos(2m theta). At a fixed m, a relation
is a sum of v^(-p_j) Q_j(v), with rational Q_j analytic at zero. The
eight p_j and their 28 pairwise differences are nonintegers, as exact
rational checks verify. A nonzero Q_j has a finite integer vanishing
order e_j. The exponents e_j-p_j are pairwise distinct. Division by
the smallest power and the limit v down to zero leaves exactly one
nonzero coefficient, a contradiction. Each rational branch vanishes
separately. The same proof separates these branches from an integer
Laurent polynomial; its order may be negative but is still integral.

Set a_R=R^2-1 and L_R=1+a_R v. Within a branch the scaled radial
factor, including t^m, is

 A_RmN(v)=R^8 v^4 (1-v)^m
           P_N(2(1-v)/L_R-1)/L_R^4.

Rodrigues' formula gives Legendre leading coefficient
2^(-N) binom(2N,N). Thus at v_R=-1/a_R the pole order is exactly
4+N, with nonzero leading Laurent coefficient

 C_RmN=R^8 v_R^4 binom(2N,N)(1-v_R)^(m+N)/a_R^(4+N).

The old polynomial is analytic there. The other scale is analytic
there too, because a_25=624, a_100=9999 and
L_R'(v_R)=1-a_R'/a_R is nonzero. At either pole, the largest N in a
nontrivial relation has a highest pole that cannot cancel. Descending
induction removes all its scaled terms, and then those at the other
pole. Accepted old independence removes the rest. The total dimension
is 1922+2*3*7*12=2426. This uses rational identities at auxiliary
negative poles, without extending a physical noninteger S power there.

## Injectivity of the density map

Every generator is smooth and separately even in x and y. Its finite
formula and differentiation show
|D^k chi|=O(r^(3+gamma-k)) for 0<=k<=4 at infinity. The scaled envelope
adds eight powers of decay. Since d=3+gamma<4, fourth derivatives tend
to zero. If partial_y Delta chi=0, smoothness gives Delta chi=f(x).
For fixed x, f''(x)=partial_xx Delta chi tends to zero as |y| tends
to infinity; hence f''=0. Evenness makes f a constant K0.
Then h=chi-K0 r^2/4 is entire harmonic with growth O(1+r^d).
The harmonic interior estimate on a radius-L disk at any fixed point
gives |D^4 h|<=C L^(-4) sup|h|=O(L^(d-4)); L tending to infinity
makes D^4 h=0. Thus h has degree at most three. Separate evenness and
harmonicity reduce h to A+B(x^2-y^2). Consequently chi is a separately
even quadratic polynomial. Its angular radial coefficients are integer
Laurent polynomials in v. Separation from the noninteger branches
proved above makes every coefficient zero. Therefore chi=0, and D is
injective. This standard harmonic estimate is an analytic dependency,
not something established by the finite arithmetic program.

## Probe separation and history

For r>0 divide a proposed dependence by r S^(-2)>0 and take its full
circle sine-n coefficient at n>=19. Every objective row has n<=17
and contributes zero, while the proposed probe gives t^K>0 for 0<t<1.
This is a contradiction. Each probe is smooth at the origin because
r^(2K+1) sin(n theta) equals Im(x+iy)^n times
(r^2)^(K-(n-1)/2), an integer nonnegative power. Equality almost
everywhere or in distributions between these continuous functions
implies pointwise equality, so the same conclusion holds there.
The accepted 016 history gives the earlier part of the recorded chain.

The checker binds the exact full phase-one and final shape lists,
all 67 rows, angular order 180, middle order 16, weights 26214400,
3000000 and 10^12, penalty mode, and all logged 12 then 28 iterations.
Iteration counts include rejected trials, and do not mean 40 accepted
updates. Literal shell parameters are inspected without executing the
publisher's shell or Python. The immutable manifest's generic d2
parent names broad lineage; it does not replace the actual saved inputs.
Its truncated description does not supply the missing phase details.
The public 25-pair register predates the recorded 08:46Z launch. The
08:47Z announcement and 09:13:13Z record postdate launch and are not
preregistrations. The diagnostic 35-probe list is not given a new
preregistration claim.

## Verification and scope

The program rehashes accepted old rank and density dependencies and the
accepted 25/50 two-pole proof as background. It constructs a fresh
25/100 instance and checks all 168 distinct Laurent coefficients by
actual rational generator expansion as well as the displayed formula.
The 25/50 peer result is not asserted to be an independent audit of
this new 25/100 instance. The latter remains OPEN pending peer review.

No conditioning bound, sampled-matrix rank, optimizer minimum, full-plane
norm or existence result follows. The separate point, origin and exact
sector checks use ../generator_sector_audit/PROOF.md and
PROOF_CANDIDATES.md. A weak-distance evaluation must use all hypotheses
and the whole-plane argument in ../joint_scaled_factored_weak/PROOF.md,
including the same fixed c, canonical velocity, real S1 correction
class and distributional stationary equation. Probe separation alone
is neither a residual estimate nor an exclusion certificate.
