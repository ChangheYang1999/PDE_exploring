# Candidate016 registered assembly, conditional on the component enclosures

## Exact statement and the remaining condition

Fix candidate C1-N1-016-legqs25-quot013, raw SHA256
a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42,
at c=4076476460239181/2251799813685248. Its whole-plane residual is
F=(cX+U[rho]).grad rho-rho for the exact finite generator sum.
All norms below use Lebesgue measure on R^2 and the ordered Cartesian
Hessian. Let omega=(1+4|X|^2)^(2/5), J=(1-Delta)^(1/2), and set

 G0=||F||2, G1=||DF||2, P2=||omega D^2F||2, R=|| |X|F ||2,
 H=||(-Delta)^(-1/2)F||2,
 E_w^2=P2^2+w1 G1^2+w2 G0^2,
 E_* = E_(2^14,2^18), E_2^2=E_*^2+2^18(20/21)H^2,
 N_s(F)=E_2(J^s F), X_(s,w)(F)=E_w(J^s F).

Assume the four positive component norms G0,G1,P2,R belong to the
outer intervals of the complete N3 component record frozen in
../candidate016_scaled_norm_peer/source/MANIFEST_v02.json. This is an
explicit numerical hypothesis, not independently established by this
assembly check. Its independent whole-plane integrations are running.

Subject to that hypothesis, the directed rational bounds in the result
file enclose E_*, E_2 and all listed lower comparison expressions. The
four Ns and five XSW instances use the exact s, weights and sufficient
thresholds in source/parameters.json. The legacy X3 instance uses exact
threshold1/163840. Every listed sufficient smallness test fails under
the hypothesis. This does not prove absence of a stationary correction;
that requires the separate accepted weak-distance theorem.

## Parity Hardy bound and its limited meaning

F is odd in y and even in x. For a compact smooth test phi write its
odd-in-y part as phi_o=(phi(x,y)-phi(x,-y))/2. Then the pairing with F
is unchanged and ||grad phi_o||2<=||grad phi||2. On each centered circle
phi_o has zero angular mean. The unit-circle Fourier Poincare inequality
therefore gives

 ||phi_o/r||2 <= ||r^(-1) partial_theta phi_o||2 <= ||grad phi||2.

The first inequality follows by expanding in nonzero integer Fourier
modes, whose squared frequencies are at least1, and integrating in r.
Cauchy-Schwarz now bounds |integral F phi| by R ||grad phi||2.
By density and the Fourier description of the homogeneous Sobolev dual,
H is finite and0<=H<=R. This proves a proxy upper bound, not H=R and
not a positive lower bound for H. Consequently

 E_* <= E_2 <= sqrt(E_*^2+2^18(20/21)R^2).

All functions here are smooth finite generator sums. If an indicated
fractional norm is infinite, its lower comparison still holds in the
extended sense, but no finite upper claim is made for it.

## Registered norm comparisons

The accepted Analysis II comparison, fully reproduced in
../negative_norm_forcing_assembly/PROOF.md, gives

 N_s(F)>=(1-34s)E_2, 0<s<1/34.

Its argument is as follows. Put T F=(omega D^2F,128DF,512F,
512sqrt(20/21)(-Delta)^(-1/2)F). Then ||TF||2=E_2. The accepted
Bessel commutator estimate ||[J^s,omega]v||2<=34s||v||2, and the fact
that every other entry commutes with J^s, give
||J^s TF||2<=N_s(F)+34sE_2. The Fourier multiplier of J^s is at least1,
so E_2<=||J^s TF||2. This proves the comparison. The same argument
with the last entry removed gives the legacy X3 lower comparison.

The sharper accepted T2-R3/T4-042 comparison, used in N4-181 and
frozen theory_v03 section NORM-T-XSW-v1, is

 X_(s,w)(F)>=(1-(48/25)s)E_w.

Only the five registered small positive s values are used. Its
commutator argument is the same with the accepted constant48/25.
No new commutator estimate or inverse theorem is asserted here.
Both sources also give interpolation upper bounds involving
Q3=||omega D^3F||2. No Q3 input is available in this component record,
so all those fractional upper bounds remain OPEN. A finite E_2 upper
bound alone does not supply a finite numerical Ns upper bound.

For the graded components gamma0=||J^sF||2, gamma1=||DJ^sF||2 and
gammaH=||(-Delta)^(-1/2)J^sF||2, the Bessel multiplier is at least1,
which gives gamma0>=G0, gamma1>=G1 and gammaH>=H. For0<=s<=1,
concavity gives (1+t^2)^(s/2)<=1+s(sqrt(1+t^2)-1)<=1+st.
The triangle inequality and Plancherel therefore give

 gamma0<=G0+sG1, gamma1<=G1+s||D^2F||2<=G1+sP2,
 gammaH<=H+sG0<=R+sG0.

These elementary comparisons use only the assumed component bounds.
The three saved graded rows are checked as arithmetic against their
stated decimal boxes; this does not revise any box or its hypotheses.
Gamma2 upper bounds still require missing higher regularity data.

## Outward arithmetic and exact threshold transcription

Every serialized component endpoint is a containing ball. Its outer
lower or upper endpoint supplies the monotone input. Positive weighted
sums, square roots and the positive comparison factors preserve order.
The checker evaluates them at1536bits and accepts a printed decimal
lower bound only below the entire independent expression, and a
printed decimal upper bound only above it. It also records coarser
strict rational enclosures, verified directly without float proposals.
These are conditional scalar calculations, not new spatial integrations.

The rebalanced exact threshold is3/327680=0.0000091552734375. The
legacy N3 code uses0.0000091553 instead, exceeding it by17/640000000000.
A ratio to that larger denominator is a conservative lower estimate of
the ratio to the exact threshold, but is not the exact source ratio.
For legacy X3 the source threshold is1/163840=0.000006103515625;
the code uses0.0000061035, smaller by1/64000000000. Its printed ratio
to that smaller denominator is not the ratio to the source threshold
and is not justified as a lower bound by the cited comparison alone.
The checker recomputes both exact source ratios. This finding concerns
transcription and the supporting calculation; it does not assert that
the unknown true fractional norm is below the displayed ratio.

All source texts are read and bound, never executed. This audit accepts
only the conditional scalar assembly and the elementary/registered
comparisons stated above. The original four full-plane numerical
hypotheses, an actual H enclosure, Q3, a compatible inverse and a
nonlinear existence closure remain separate tasks.
