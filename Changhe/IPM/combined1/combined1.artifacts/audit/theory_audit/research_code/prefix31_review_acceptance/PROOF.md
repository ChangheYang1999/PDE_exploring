# Acceptance of R1-051, the prefix31 composition, and opposite norm orderings

This proof precedes its checker. The frozen review is T1 R1-051 in
review set 48, SHA256
f7a43c40237c554e26a0412e36436a0ff325aee007a135c115d739a3a5b8dcd8.
It accepts the exact finite implications below. It does not repeat a
candidate source integral or enlarge the scope of the accepted source
certificates. The exact frozen source, spaces and dependencies matter.

## Statement and definitions

Fix the complete canonical residuals F007 and F016 of snapshots
C1-N1-007-d2w-j7-e2bal and C1-N1-016-legqs25-quot013. Their generator
convention is rho=-partial_y Delta chi, u=(-chi_xyy,chi_xxy), and
F=(cX+u).grad rho-rho at the common exact
c=4076476460239181/2251799813685248. The canonical local velocity term
is included. These are the exact fields accepted by N4-252 and N4-392,
not sampled grids or truncated nonlinear products. All functions are
real, and all norms use Lebesgue measure on R2. Set

 H(F)=sup{|int F phi|: phi in C_c^infty(R2), ||grad phi||2<=1},
 G0=||F||2, G1=||grad F||2,
 P2=||(1+4r^2)^(2/5)D2F||2,
 E2(F)^2=P2^2+2^14 G1^2+2^18 G0^2+(20/21)2^18 H(F)^2.

The Hessian uses its Euclidean tensor norm. Under the complete source
and integration premises listed below, the prefix31 certificate proves

 0.529469576110 < H(F016) < 0.619651337324093367770781451079,
 608.392385921614 < E2(F016) < 629.296112162914.

Moreover,

 H(F007)-H(F016)>0.015873038675998,
 E2(F016)-E2(F007)>1.572166921614.

The opposite orderings concern these two residual norms only. They
neither compare distances to solutions nor establish an inverse or a
stationary solution. Candidate016 remains excluded in the audited balls.

## Complete prefix and the upper bound

The complete F016 has exactly the 160 odd sine frequencies 1 through319,
from its accepted1360 branches. For F=sum f_n(r)sin(n theta), put
q_n=pi int_0^infinity r^3 f_n(r)^2 dr and R2=||rF||2^2=sum q_n.
The angular right inverse
A=-e_theta r sum f_n(r)cos(n theta)/n has div A=F and
||A||2^2=M2=sum q_n/n^2. Local regularity at the origin and the
square-integrable tangential field justify the whole-plane identity,
as proved in469 and474 and independently accepted477 and481. Thus
H(F)^2<=M2. The source regularity, integrability and parity are retained.

Every omitted frequency after31 is at least33. Since q_n>=0,

 M2 <= R2/1089 + sum_(n=1,3,...,31)(1/n^2-1/1089)q_n.

Let R2 in[RL,RU] and q_n in[l_n,u_n] be the accepted intervals.
Every displayed coefficient is positive, giving the rational upper

 P=RU/1089+sum_(n<=31)(1/n^2-1/1089)u_n.

The prefix sum sum l_n/n^2 is a lower bound for M2. The split upper
Q=sum u_n/n^2+(RU-sum l_n)/1089 satisfies
Q-P=sum(u_n-l_n)/1089>0. No omitted frequency is dropped. The16 intervals
were independently resummed from all484 saved groups in T4-480. This
acceptance uses those results and recomposes both source formulas.

For each accepted deep test psi_n in modes1 and3, define
Z_n=A_(Delta psi_n)-grad psi_n, a_n=||Z_n||2^2 and b_n=<A,Z_n>.
The tests have smooth origin parity, gradients and r Delta in L2, and
valid cutoff limits. Then div Z_n=0. The two different frequencies
are orthogonal. Completing two scalar squares gives
H(F016)^2<=M2-b_1^2/a_1-b_3^2/a_3. The strict accepted improvement
floor is J=59664789113139289718803/250000000000000000000000.
Consequently H(F016)^2<P-J. No same-frequency gains are added.
T4-472 independently checked the exact energies and the650digit
signed pairing archive; T4-477 accepted both Opus domain reviews.

The dual lower square is the accepted sum of strict floors for
(int F psi_n)^2/||grad psi_n||2^2. The two gradient fields are orthogonal.
Cutoff convergence permits these tests in the completion of the compact
test space. Choosing their coefficients proportional to the pairing
divided by gradient energy proves this lower bound. This is the argument
accepted470/472. Insert both H squares and the accepted G0,G1,P2 endpoints
into the positive E2 formula. Every numerical display follows by exact
squaring or rational comparison. T1's repaired E4 to E7 displays are
checked the same way, including seven total-energy tail bounds.

## Opposite norm orderings

Decode N4-252's outward lower ball [m +/- r] for H(F007) as exact
finite decimals. Then H(F007)>=m-r. Subtract the strict rational H(F016)
upper above. The exact difference exceeds0.015873038675998. This is a
comparison of an actual lower bound with a complete upper bound,
including the omitted angular tail. Separately subtract the strict
E2(F007) upper606.820219 from the strict E2(F016) lower608.392385921614.
The difference of those rational endpoints is exactly1.572166921614;
the original strict inequalities make the difference of the actual
norms strictly larger. Their definitions and weights are identical.
This proves N4-412 from the same accepted endpoints.

## Directed displays and a new rounding check

All main bounds in R1-051 and its E4 to E7 corrections are checked
against the exact input endpoints. In particular the corrected
prefix7 no-improvement E2 upper is763.064677, not763.064676.
The total-square interval is[51.061045287604984,51.061045287604985].
The exact width comparison is P-sum l_n/n^2<.000525<RU/1089<.046889.
These are upper bounds, not exact norms or tail sizes.

R1-051 V7 says, under a FLOAT label, that modes1 through31 carry
'at most0.9888' of R2. Test this literal upper separately. Positivity
gives

 (sum l_n)/RU <= (sum q_n)/R2 <= (sum u_n)/RL.

The checker tests whether the left endpoint exceeds.988805 and the
right is below.988806. If both tests pass, the literal 'at most.9888'
is refuted by accepted exact endpoints. The ordinary approximate
four-decimal fraction.9888 remains correct. Use 'about.9888' or the
rigorous upper.988806. This observation does not affect P, H or E2.

The N3 complete Hardy display and narrower H bracket remain consistency
observations conditional on source premises not established here.
A containment or decimal agreement does not certify a source integral.

## Verification boundary

The checker binds the frozen T1 review and program text, its54-check
log, the revised4783-check program and log, N4-410 and412, own accepted
480/481/472 inputs, and the exact007 source. Peer programs are parsed
and never executed. Their source maps are checked against immutable
own-lane copies. Whole-field source construction, positive-pole moment
soundness and outward serialization remain the accepted premises.
No new integration, Lean build, optimizer, remote model or server is
used. Collaboration is through the existing configured Opus5.5 lanes;
actual provider identity is unobservable.
