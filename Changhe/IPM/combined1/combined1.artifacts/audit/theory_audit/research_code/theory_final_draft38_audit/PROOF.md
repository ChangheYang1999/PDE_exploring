# Independent audit of theory draft 38

## Object and inherited hypotheses

This audit concerns the frozen 1810-line THEORY_FINAL draft 38, SHA256
ccaa8623477ffdffbb977e866e669cffc9546a657eade246d053941ea0162a02,
published at 12:57Z on 29 October 2026. The preceding accepted draft 34
has SHA256 febf6c09e19a2e6b585c5263348250017d4af86fca9aa731db89fbc6d6106b40.
The entire word comparison, 124 changed blocks in 743 lines, was read.
The separate 914-line unified diff was not read completely. The word
comparison ignores whitespace alone and covers every changed word.

All unchanged conditional closure results retain the exact reference,
operator-domain, fixed-c, canonical velocity and normalization hypotheses
of the accepted draft 34 audit and its predecessors. In particular,
X_(s,w)(h)=E_w(J^s h), J=(1-Delta)^(1/2), with

 E_w(g)^2 = ||omega D^2 g||_2^2 + w1 ||Dg||_2^2 + w2 ||g||_2^2,
 omega=(1+4r^2)^(2/5).

The reference exponent is fixed, c[h]=0, and the leading far-field
profile is fixed. A correction direction with a nonintegrable scaling
or angular tail is not admitted by an L2 chart. Conditional rate and
contraction arithmetic do not establish the missing reference
hypotheses or a high inverse. The proof of draft 34 remains a named
source dependency, rather than an unstated appeal to earlier agreement.

## 1. Conditional closure and the expanded exclusion table

The sharpw data are mu=97/250, C=397, s=1/5184, cU=8/5,
w2=2^20, r=1351/10^6, eta=4207/(2*10^7), betaL=2. Direct substitution
gives the exact high rate

 beta=mu-C*s-cU*r/sqrt(s)=63092119/405000000>1557/10000.

The conservative self-map slack is r-eta/(1557/10000)=7/1557000000>0;
using the exact beta also gives 1/beta<6.4226. The contraction coefficient
r/(2 betaL sqrt(pi*s*(1+s))) is below 0.0137200. These are precisely
conditional implications in the named chart. Their hypotheses are not
supplied by the arithmetic.

The necessary sharpw L2 family ceiling

 b=(2mu/3)*sqrt(mu/(3C))/(cU sqrt(w2))

is below 2.8496e-6. The analogous conservative scalar and original graded
ceilings used in the table are 3.7930e-6 and 25/54684. For an established
distance D>d and a necessary radius ceiling B<=b, exact d/b>q implies
D/B>q. Recompute all 21 six-column rows, including 023 and 024, with
these exact ceilings. This division orders the displayed lower bounds
only. It does not order different candidates' actual correction distances.

The profile-specific coefficient 93/250 and the radial caps are now
AUDITED through T4-434. The lower obstruction N(z)/G(z)>0.3714757 for 007
concerns that complete angular inequality. It does not prove the same
lower obstruction for every estimate using the stationary equation.
The full 410 remainder, 425 radial average and their scope are accepted
through 424 and 432. No new inverse theorem has been added in draft 38.

## 2. The new two-endpoint dyadic implication for 016

Let c=4076476460239181/2251799813685248, S=1+r^2 and
F=(cX+U[rho]).grad rho-rho for the exact 016 reference. For a>=0 put

 J(a)^2=sum_(n=1,3) integral_R2 S^(2-a) |Delta Pi_n F|^2 dX,
 N_a(F)=||S^((2-a)/2) Delta F||_2,

where Pi_n is full-circle sine projection normalized by 1/pi.
Orthogonality gives J(a)<=N_a(F), including infinite N_a(F), and positivity
of the integrand makes J nonincreasing.

Assume all registered NC-T-ORIGIN-INV hypotheses: the exact origin slope
a0>=5c-4, strain 1-c, canonical realization, input hyperplane, dyadic
partition, plateau and absorption assumptions of its accepted theorem.
They supply 0<s<c-1, M>=1/(c-1-s), beta<=1+c-ca and C_U>=1. Under
these assumptions the scalar necessary inequality for 0<a<Astar=1+1/c is

 5^((a-2)/2) N_a(F) < H(c-1) (1+c-ca)/(1+a),
 H(d)=max_(0<s<d) (d-s)sqrt(4*pi*s*(1+s)).                 (1)

For d=c-1, the unique maximum occurs at
sstar=(2d-3+sqrt((2d-3)^2+16d))/8. Indeed the derivative of
(d-s)^2*s*(1+s) is (d-s)[d+(2d-3)s-4s^2]. The bracket has one positive
root in (0,d), while both endpoint values vanish. This proves the formula
without numerical optimization.

Partition (0,Astar) at 0,1/4,1/2,3/4,1,5/4,3/2,Astar. Since
3/2<Astar<7/4, choose e=1/4 on the first cell and e=7/4 on every other
cell. For a in [l,h], e>=h and

 5^((a-2)/2) N_a(F) >= 5^((l-2)/2) J(e),
 H(d)(1+c-ca)/(1+a) <= H(d)(1+c-cl)/(1+l).

The first factor increases with a; the last rational factor has derivative
-(1+2c)/(1+a)^2<0. Thus seven positive gaps computed from only these two
endpoint norms contradict (1) on all cells. For Astar<=a<2 the separate
nonpositive far-field rate excludes the registered scheme. The minimum
cell ratio is strictly above 1.253908386497.

The endpoint numerical inputs are N4's independently reproduced complete
moments, which agree with the containing N3 displays. This audit binds
those results and recalculates the seven inequalities. It does not claim
a third integration of the candidate or reproduction of five unused N3
endpoints. The complete projection algorithm is analytically consistent:
for f=r*v^z*P(t)*sin(n theta), t=r^2/S and v=1/S, put
T_z P=(1-2zt)P+2t(1-t)P'. Then

 Delta f = r*v^(z+1) [T_z(T_z P)-n^2 P]/t * sin(n theta).

This follows from r*partial_r and the polar Laplacian. Squaring,
using r dr=dt/(2v^2), and factoring each exact vanishing order gives
N4's exponent a+(ell+k)*delta/2+q_ell+q_k-3. Positive denominator factors
and all endpoint exponents above -1 justify its complete ordinary
integrals. No principal-value or contact convention is introduced.

## 3. Repairs required in the frozen draft

1. Section 3.4 writes lambda=1/2+5*2^(1-q)=109.6024. The final equality
is false. The exact expression is strictly above 109.6024. Replace the
last equality by an approximate sign or the proved strict inequality.
Here q=1/c-4; the difference is recomputed with outward Arb arithmetic.

2. Section 9 again states J(r)>=lambda*H*(5/r)^delta on all of
[L0,18860]. The cited derivation uses this formula for r>=max(L0,5)
and J(r)>=lambda*H for L0<=r<5. Section 3.4 already has the correct
piecewise statement. Repeat it, or state only the valid uniform
consequence J(r)>2.74*H on [L0,18860]. This audit does not refute the
stronger formula; its application below 5 is OPEN from that derivation.
The same current tail list and its positive delta term remain required.

3. Section 10 writes N_1>=13.758676 for 007 from modes 1 and 3.
Those modes give J(1)=13.758675979450936...<13.758676. The rounded value
is therefore not a proved lower bound from these data. Write
N_1>13.75867597, or label 13.758676 as an approximation to J(1).
This refutes the stated inference, not the possibility that additional
modes make the full N_1 larger than that decimal.

4. The historical sentence saying 023's distance is 5.763 times the
graded ceiling should say it exceeds that ceiling by a factor greater
than 5.763. The exact lower ratio is not equal to the rounded display.

5. The factor above 4.34 in the outer-only radial averaging paragraph
is the comparison without the universal fallback. The fallback version
is the separately stated Eeff>0.79303648 comparison. Add this qualification
to avoid combining the stronger factor with the broader fallback class.

6. Keep exclusions scoped to registered scalar and original graded balls,
with dyadic exclusions listed separately. Only 016 has been added to the
dyadic list here. Do not infer a dyadic exclusion for 023 or 024 from an
unweighted L2 distance. Later 025 results and N4's later completion of the
six 016 probes are publication updates, not retroactive errors in this
12:57Z snapshot.

7. Treat the suggested exponent near 1.05 and the much smaller inner
amplitude as FLOAT diagnostics for the specified replacement tail model.
They are not necessary exponents for every stationary-specific method.
The fixed tail input is what blocks the current sufficient certificate.

## Verdict and evidence

CONFIRMED: the changed conditional mathematics, 21 exclusion-table rows,
the two-endpoint dyadic implication under its exact hypotheses, and the
accepted profile and radial-average dependencies. REFUTED: the exact
109.6024 equality and the inference of the upward-rounded 13.758676
lower bound from the two projections. OPEN: the unqualified small-radius
intermediate formula and all missing inverse or stationary-only inputs.
The other listed changes clarify scope or current status. No existence
closure or nonexistence of the profile problem follows.

The checker binds the frozen source and comparisons, repeats exact closure
arithmetic and seven Arb cell inequalities, and verifies the indicated
rounding and piecewise consequences. No foreign code is executed and no
large candidate moment is repeated. Unseen later edits are outside scope.
