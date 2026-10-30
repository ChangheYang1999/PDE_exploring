# Scope and exact constants in the T2 final summary

## Statement and dependencies

This is an audit of the frozen the T2 final summary dated 17:15 UTC and
T2's bs_draft55_errata_check.py, read as text. It is not a new existence
theorem. The claims concern fixed-c, real whole-plane S1 corrections in
the registered norm completions, with Lebesgue L2 norm. The high norms
control sqrt(W2) times that L2 norm. The independent proofs T4-454,
T4-462, T4-468 and T4-473 are dependencies. In particular no estimate for
a new inverse, new localized domain, actual solution distance or changed
c is inferred. The frozen full theory draft55 and original theory_v01
permit exact verification of T2's numbered excerpts. Selected lines of
our append-only verification ledger are frozen independently.

The three summary findings are as follows.

1. The seven scalar families in T4-454 have common strict necessary L2
budget below 3.7930e-6. The smaller 3.79e-6 in summary section6 is not a
valid uniform upper bound derived from these scalar inequalities.
A TB-sharp scalar example satisfies all the displayed rate, contraction,
slope and self-map inequalities while its radius permits L2 budget
3.791e-6. This refutes that budget deduction, not a theorem that all
actual stationary corrections lie below 3.79e-6.

2. The exact relaxation scaling factor in summary section0 is
sqrt(k/K) u/v, with the exact definitions below. It lies strictly between
0.99998312568 and 0.99998312569. Thus 0.99998313 is a correct nearest
eight-decimal approximation, but is not the exact factor.

3. The accepted weak lower bounds do not determine which candidate has
the smallest actual fixed-c L2 correction distance. The phrase "closest
candidate" needs a separate ordering proof. That ordering is OPEN here.
It can be replaced by a precise description of 007's accepted evidence.

We also accept T2's draft55 source and arithmetic corrections within
the scope stated below. None changes a candidate exclusion.

## Proof of the scalar budget correction

Write mu=297/1000, C=402, cU=8/5, sqrt(W2)=512, s=1/4096,
b=3791/10^9 and r=512b. The high rate is

 beta = mu - C s - cU r/sqrt(s).

All parameters are positive rationals and sqrt(s)=1/64. Exact rational
comparison gives beta>0 and beta r>1e-7. Hence forcing eta=1e-7 satisfies
the scalar self-map condition eta<=beta r. For the scalar normalization
constant c_s=1/(2 sqrt(pi s(1+s))), pi>3 gives

 (c_s r)^2 < 1024 r^2/[3(1+s)] < (36/1000)^2.

Consequently 7/10-c_s r>0, betaL=19/5-c_s r>0 and
c_s r/betaL < (36/1000)/(19/5-36/1000)<1. Also 0<s<=1/1024.
Thus these scalar conditions admit b=3.791e-6>3.79e-6. This construction
supplies parameters, not a reference profile, inverse or stationary
correction. Those separate PDE hypotheses are not asserted.

For every mu,C,cU,W2>0, positivity of the high rate implies

 ||h||2 <= r/sqrt(W2)
          < (mu-C s)sqrt(s)/(cU sqrt(W2))
          <= (2mu/3)sqrt(mu/(3C))/(cU sqrt(W2)).

The last step maximizes mu t-C t^3 over t=sqrt(s)>0. Its derivative
mu-3C t^2 vanishes at the unique positive maximum. Squaring the last
expression gives 4mu^3/(27C cU^2 W2). For the seven registered tuples,
T4-454's exact rational square comparisons certify the common upper
3.7930e-6, and place the TB-sharp value between3.7929e-6 and3.7930e-6.
We check those comparisons again from their small exact parameter file.

The original graded estimate is bG=50/(651 sqrt(28248)), with
bG<4.5717e-4. The older coarse upper 25/54684 is slightly larger than
4.5717e-4, so the displayed equality 25/54684=4.5717e-4 is approximate.
The sharper accepted estimate nevertheless proves the summary's graded
upper bound directly. These are distinct issues.

## Proof of the relaxation factor

Let sigma=1/1024, M=sqrt(pi)Gamma((1-sigma)/2)/2,
W=8sqrt(5)6^(-3/5)/5, k1=M+8/5, cr=3M/2+32/15,
c8=1+3pi W/4, dtop=1+pi W/2 and

 K=2dtop+6c8+24(cr+2k1)+32k1.

Put q0=1/(2sqrt(pi)), ps=2^sigma sqrt(1+sigma)/(2sqrt(pi)),
P0=ps(1+WM sigma)+WM sigma/(2sqrt(pi)) and

 v=(4/5)q0+q0(1+4WM sigma)+(19/5)P0,
 k=39068/100, u=15871/10000.

The relaxed squared objective is proportional to 1/(K v^2), all other
variables fixed. Its supremum therefore scales by k u^2/(K v^2), and
the positive square root by sqrt(k/K)u/v. Directed Arb evaluation of
these explicit formulas bounds that factor by the strict rational
interval stated above, within the accepted T4-473 enclosure. The whole
interval is below0.99998313 and within half5e-9 of it. Exact equality is
therefore false while nearest rounding is correct. No attainability of
the relaxed supremum in the complete PDE prescription follows.

## Draft55 corrections and their limits

T2's numbered draft55 excerpt must agree at every line with the frozen
complete draft55, not only with a producer-supplied excerpt hash. Its
T4-175,290,328,485 excerpts must agree with our ledger. The original
sector excerpt is also compared with the complete original theory_v01.

The beta=2 WU3 estimate is for T2-R3. The beta=11/4 estimate is for the
T2-R1 TB-sharp matrix with E0 as one component. They are different norm
families; draft55 section2.8 already distinguishes them correctly.
The registered floors are1/2 and9/10. "Fixed state131 floors" is
misleading because hypothetical improved state131 floors are separate
parameter rows. Neither all-weight statement assumes those improvements.

T4-290 already accepts T2's localization extension under unchanged
high-row margin and norm-domination hypotheses. It does not establish
those hypotheses for a newly localized PDE framework. A general
unqualified promotion of other claims in handoffAK2 does not follow.

A complete scalar closure checklist must include beta>0 and
7/10-c_s r>0 together with eta<=beta r and the low contraction. Their
omission from a short summary is a scope clarification. It does not
refute the full theorem, which supplies them separately.

The T4ALT residual maximum depends on the defect data. At fixed s,
let mu=1/10-4800s, A=5/sqrt(s), m>=0 and B>=0. Under mu-Am-B>0,
completion of the square in the reviewed defect inequality gives

 eps_max=((mu-Am-B)^2-4ABm)/(4A),
 r_star=(mu+Am-B)/(2A).

The displayed1.8938e-7 refers to s=2^-18,m=2^-17,B=1/100.
The second box s=2^-18,m=2^-16,B=1/200 has a different maximum,
approximately6.1967e-8. Both decimals are checked as nearest five-digit
roundings of the exact expressions, not substituted as exact maxima.
Other defect data must use their own formula. The necessary domain,
hyperplane, background and low-contraction hypotheses remain those of
the reviewed theorem.

At the selected sharp and sharpw radii, exact rates are respectively
12551327/121000000 and63092119/405000000. Their reciprocal upper
bounds9.6432 and6.4226 are valid. The intermediate quotients10000/1037
and10000/1557 are strictly larger than those decimals, so an equality
between each quotient and its decimal is false. Comparison with the
actual exact rates, not the rounded rate lower bounds alone, proves the
valid final upper bounds.

The T4-175 floor6091157959/250000000000 exceeds0.02436463 but is less
than0.024364634. It cannot independently certify T2's higher printed
floor. Its ratio to0.01625064 rounds to1.50. Finally the old exponent
labels gamma-h delta-2k, gamma=1-delta, become1-l delta-2q under
l=h+1,q=k. Thus old labels(1,0),(2,0),(3,0) are exactly new labels
(2,0),(3,0),(4,0). The automatic new(1,0) cancellation is separate.
All these conclusions retain the hypotheses of their accepted proofs.

## Why lower bounds cannot rank actual distance

A distance lower bound a<d does not supply an upper bound on d. Given
bounds a<d1 and b<d2, choose d1=max(a,b)+2,d2=max(a,b)+1 or reverse
them. Both assignments obey both bounds and give opposite orderings.
Actual admissible sets might also be empty, giving infinite distance.
Thus lower-bound comparisons alone cannot establish "closest". This
logical observation does not assert either assignment is realized by
these PDE candidates. The candidate ordering remains OPEN.
