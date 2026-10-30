# Independent audit of the proposed theory_v08 failure factors

## Exact object and inherited hypotheses

This audit concerns the 24 rows in T1's note v47 and its accompanying
v08_factors_007.py, frozen in source/. It checks arithmetic, the
direction and meaning of each bound, and the logical scope of the
conclusion. It does not derive new inverse estimates or repeat the
already independently accepted full-plane integrations.

The reference is C1-N1-007-d2w-j7-e2bal at
c=4076476460239181/2251799813685248. Functions are real on R2 and
have S1 symmetry, even in x and odd in y. The correction chart fixes c
and the leading far-field profile. U=(-R1 R2,R1^2) is the canonical
IPM velocity, including its contact term. The normalized high balls
have c[h]=partial_y U2[h](0)=0. No row replaces the separate reference,
maximal-domain, high inverse, or nonlinear hypotheses of its framework.

The inherited sharp and sharpw spaces are the completions of smooth
compact S1 functions in

 X_(s,w)(f)^2=||omega D2 J^s f||2^2
               +w1||D J^s f||2^2+w2||J^s f||2^2,
 J=(1-Delta)^(1/2), omega=(1+4r^2)^(2/5).

Ordered Cartesian derivative tensors are used. Sharp has
(s,w1,w2)=(1/7744,2^14,2^18) and eta=76219/10^9.
Sharpw has (1/5184,2^15,2^20) and eta=4207/(2*10^7).
These are different norms, at different fractional orders.
Their containing residual bounds were accepted in the frozen
norms_ACCEPTANCE.md after independent component integration.

## 1. Quotient principle and correction of S2

For exact positive quantities Q,T and rational p,t satisfying
Q>=p>0 and 0<T<=t, one has Q/T>=p/t. For a chosen number k of
decimal places the rational displayed lower factor is

 d=10^(-k) floor(10^k p/t).

This is not literally floor(p/t). A division program can verify d<=p/t
and p/t>1 but cannot verify Q>=p unless its mathematical source is
checked. The checker reads the frozen peer program as syntax, extracts
its literal data without executing it, and verifies every quotient
independently with rational arithmetic.

Let E_w be the same norm before applying J^s. The audited comparison is

 (1-48s/25)E_w(F) <= X_(s,w)(F)
 <= E_w(F)^(1-s)(2Q3^2+C_w E_w(F)^2)^(s/2)+(48s/25)E_w(F),

with Q3=||omega D3 F||2 and the registered positive C_w.
The source containing balls certify for sharp

 516.9717852723 < X_(1/7744,(2^14,2^18))(F) < 517.5527701453,

and for sharpw

 756.5312630768 < X_(1/5184,(2^15,2^20))(F).

Every displayed strict inequality is checked against the full ball.
In S2 T1 reuses the sharpw lower bound 756.5312630768 for sharp.
That proposed bound exceeds even the sharp upper comparison.
Consequently S2's source assertion is REFUTED. Replace its numerator
by 516.9717852723. Its exact ratio to 7.6219e-5 is
5169717852723/762190, and the downward display is 6782715.40.
The old 9925756.87 factor is not justified for the sharp norm.
Both corrected S rows still fail their respective sufficient tests.

## 2. Distance, origin and universal rows

D1 to D5 use the independently accepted strict whole-plane weak
distance floor d=4769166867/10^12. A stationary correction with all
hypotheses of the weak identity must have ||h||2>d. The thresholds
are upper ceilings of specified framework L2 radii, or the exact
fixed sharpw radius (1351/10^6)/1024. The sharp and sharpw family
ceilings are independently checked from

 b=(2mu/3)*sqrt(mu/(3C))/[(8/5)sqrt(w2)].

This formula belongs to the stated scalar high estimate. The TB and
graded ceilings are the accepted bounds 3.7930e-6 and 25/54684.
Failure rules out the corresponding correction balls, under the
weak-test hypotheses, and does not rule out larger or different balls.

O1 uses all seven cells of the accepted origin inverse test. Each
saved ratio is greater than 1.23427738878510651005, including the
minimum attained in the first cell. The original output's OPEN status
was superseded by independent acceptance of R1-017. Cite that accepted
result, not the initial computation alone. The statement concerns the
specified dyadic inverse criterion and all its hypotheses.

For the endpoint rows put q=1/c-4, delta=1-1/c, kappa=1-q, D=5c-1,
and

 H_q(h)=max(sup(1+r)^(-q)|h|,sup(1+r)^(1-q)|grad h|).

The accepted universal class estimate
|U[h](X)+DK(X)M[h]|<=E H_q(h)|X|^q for a common exterior radius
requires E>=Emin=(-q-1)/[2(-q)(-q-3)].
The exact rational value of Emin is checked from c. Its lower display
0.793036506422514088 is valid. The normalized smooth fractional-class
extension is accepted separately in T4-397/409; the unrestricted
test is in source/universal_PROOF.md. Neither theorem says that every
stationary-only estimate has this lower bound.

U1 to U4 compare this necessary universal coefficient with optimistic
CI targets at the fixed sharpw, sharpw family, TB and graded radii.
The full endpoint stationary and tail hypotheses, H_q<infinity and
the reference gradient lower bound are retained. Every quoted target
is larger than the independently accepted containing upper expression
for 007. Thus their numerical factors are conservative in this scope.

## 3. Profile and remainder rows

Let A,P,Theta0 be the exact endpoint profiles for 007,
B=dist_L2(A,span(P))/(4c), and g0=Theta0'(0)>0.
At the accepted angle let Phi be the pointwise lower bound for H_q.
The profile coefficient E controls the compensated homogeneous
velocity through N(z)<=E G(z) for every real z=(z1,z2), where
f_z=z1 A+100000 z2 P,
N(z)=sup_theta |V_q[f_z](theta)| and
G(z)=sup_theta sqrt(q^2 f_z(theta)^2+f_z'(theta)^2).
The complete definition of V_q is in source/profile_PROOF.md.
Its accepted lower obstruction is
E>0.3714757. It is a lower bound for this N/G certificate over the
two-dimensional angular family, not for every use of the stationary
equation.

The constants 93/250 and 583/1000 are *chosen proved upper
coefficients*. P1 and P3 to P5 test the CI obtained with those chosen
coefficients. They are not lower bounds on the optimal coefficient.
In particular the improvement from 0.583 to 0.372 demonstrates why
failure at 0.583 cannot exclude every profile estimate. P2 does give
the stated N/G-family obstruction at the graded target. For each row
the critical E upper display is checked against the full ball from
the independently accepted cap calculation.

R1 to R3 compare a lower bound on the specified T4-410 error majorant
J/H with the positive room Ecrit(Phi)-93/250. The full T4-335 tail
list, including its strictly positive delta term, is required, and
forces 0<epsilon<=delta. The lower estimate applies for the stated
admissible start radii through r_beta. At larger starts or for
radius-dependent use, T4-425/432 supplies the separate obstruction.
These rows bound the size of an upper-bound formula, not the actual
error of a stationary correction.

A1 retains the full majorant class in source/average_PROOF.md:
T4-410 constructions, uniform envelopes and valid universal fallbacks.
It uses the correct positive Green average

 Eeff(r)=kappa r^kappa integral_r^infinity E(s)s^(-kappa-1)ds.

Its accepted lower bound exceeds 0.79303 through every relevant
target cutoff. No stationary-only improvement or different remainder
construction is included in this class.

K1 to K3 retain the optimistic outer-only amplitude, the current
delta-tail input, Eprof=93/250, and the allowed relaxed universal
fallback in source/outer_PROOF.md. The current bracket obeys
lambda=1/2+5*2^(1-q)>109.6024. The accepted hypothetical necessary
thresholds for a replacement bracket Lambda are less than 14.41,
8.647 and 7.287. These thresholds are necessary only in this model.
The displayed lambda is not a lower bound for every possible kernel
estimate, and passing a hypothetical threshold would not prove closure.

## 4. Verdict and remaining open work

After correcting S2, all 24 exact rational comparisons exceed one,
with the separate meanings above. All other displayed numerators and
threshold directions are confirmed against their accepted sources.
The global label "all inequalities needed for closure" is too broad.
Use "failed tests for the specified certificates", followed by the
scope of each group. An unresolved inequality and a proved obstruction
to a chosen estimate are different statuses.

The high inverse, background conditions not yet verified, localized
inverse and nonlinear bounds, a stationary H_q upper bound, and a
complete subcritical tail-coordinate framework remain OPEN.
The approximate tail exponent 1.05 from a FLOAT model is not a
universal necessary exponent; a new remainder argument could change
that requirement. No result here proves or disproves existence near
007 outside the stated correction balls and certificate families.

The exact inputs, containing source results and full informal source
proofs are bound in data/manifest.json. Only the new checker is
executed. Arb inequalities are evaluated at 512 bits; a decimal
midpoint or an overlap is never used as proof of an outward bound.
