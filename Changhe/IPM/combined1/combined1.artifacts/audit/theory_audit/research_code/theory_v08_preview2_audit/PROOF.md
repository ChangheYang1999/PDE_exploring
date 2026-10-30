# Independent audit of theory_v08 preview 2

## Exact object and hypotheses

The object is the 868-line preview generated at 2026-10-29T13:55:03Z,
SHA256 5940b948c623aab0e744375d26100c99356f6bdc6acb46d915822e8b86d70158.
Its 127 changed word blocks are compared with the accepted preview1,
SHA256 d8c8e8ba4d36e281381c0f7c55447c9636fc39977e6350a00d805c765725cf06.
This proof is written before its checker. The task is to verify the
changes and the newly reported factor bounds. Unchanged claims retain
the exact hypotheses and separate verdicts of T4-445 and its dependencies.
This audit does not replace the planned full matrix falsification.

All correction statements fix c=4076476460239181/2251799813685248 and the
leading far-field profile. S1 means real, even in x and odd in y. Velocity
is U[h]=(partial_xy,-partial_xx)Delta^(-1)h with the local term (0,-h/2).
The symbol DK is the derivative of its kernel; it is not multiplication
by D below. In the fixed-c tangent chart c[h]=0. Normalization and the
realization of the inverse retain their stated domains. Nonintegrable
scaling and leading angular modes do not belong to the L2 correction chart.
For the endpoint arguments put

 q=1/c-4, d=1-1/c, D=5c-1, a=-2q-2, e=d/(-q-1),
 H_q(h)=max(sup (1+|X|)^(-q)|h|, sup (1+|X|)^(1-q)|grad h|).

Here h is C1, centrally odd and has finite H_q. The endpoint statements
assume the stationary tail identities, canonical velocity, finite moments
and error estimates specified by T4-335, T4-351, T4-414 and T4-425. They
are statements about those certificates, not every stationary solution.
The scalar chart is the completion under
X_(s,w)(h)=E_w((1-Delta)^(s/2)h), where
E_w(g)^2=||omega D2g||2^2+w1||Dg||2^2+w2||g||2^2 and
omega=(1+4|X|^2)^(2/5). Every use of its inverse keeps its normalization,
operator domain, range and reference hypotheses.

## Exact target arithmetic

For a specified quantity Q and threshold T>0, p<=Q and T<=t imply
Q/T>=p/t. Rounding p/t downward is therefore valid. This implication does
not convert a sufficient forcing test into a necessary condition for
existence. The 24 printed rows are unchanged from the corrected table
accepted in T4-445. In particular S2 has numerator 516.9717852723 and
factor 6782715.40. We reparse every row and repeat the rational divisions.

To check the additional radius-dependent factors, use the exact finite
sine polynomials A=F12 and P in each frozen endpoint JSON. Set

 B=sqrt(pi*(sum A_n^2-(sum A_n P_n)^2/sum P_n^2))/(4c),
 g0=sum n Theta0_n,
 Phi=|q*(A P'-A' P)|/(4c*sqrt(q^2 P^2+(P')^2))

at the exact angle in data/reach_parameters.json. The accepted endpoint
bounds supply H>=H0, where H0 is 999775, 999745 and 999748 for 007,013,014,
and separately H>=Phi. The denominator and B are strictly positive.
For V>=0 the complete retained-shape integral has the critical coefficient

 C_shape(beta,H)=D B/(sqrt(2*pi) H g0)*(B sqrt(S)/beta)^e,
 S=2*d^2/[a*(a+d)*(a+2*d)].

The crude expression C_crude replaces sqrt(S) by 1/sqrt(a). These formulas
follow by substituting the exact constant-coefficient radial integral into
the necessary condition of T4-414. Equivalently, integrate
(B-C*r^(-d))_+^2 r^(2q+1) from its positive root to infinity: the three
terms give S=1/a-2/(a+d)+1/(a+2*d). All constants are positive, so each
critical coefficient is decreasing in beta and in H. Positive V would
subtract V/g0 and only strengthen these upper bounds.

T4-454 proves the exact sharpw ceiling belongs to
(28495/10^10,28496/10^10), the exact TB-sharp ceiling to
(37929/10^10,37930/10^10), and the exact graded ceiling
50/(651 sqrt(28248)) to (45697/10^8,25/54684). These are proved brackets,
not assumptions about the direction of decimal rounding. Write them
(beta_lo,beta_hi). Evaluating C at beta_lo gives a valid upper bound at
the exact ceiling. The printed p of R2 and R3 bounds a chosen remainder
majorant at beta_hi. Its dependence through r_beta is beta^e, so at the
exact ceiling it remains at least p*(beta_lo/beta_hi)^e. Dividing this
lower bound by an upper bound for the positive room C_shape-93/250 proves
the following lower factors at 007:

| row | factor at the exact ceiling, at least |
|---|---|
| U2 | 1.1629 |
| U3 | 1.2253 |
| U4 | 2.9432 |
| P1 | 2.0544 |
| P2 | 2.0515 |
| P4 | 1.2721 |
| P5 | 1.3404 |
| R2 | 46.0752 |
| R3 | 66.5677 |

The R2 and R3 rooms here use H>=Phi. With only H>=H0 the corresponding
factors at 007 are at least 46.0750 and 66.5674. At the exact fixed sharpw
radius 1351/1024000000 the R1 factor with only H>=H0 is at least 22.1948.
We check the stated rounded upper thresholds from the independently
accepted T4-443 source, then divide them independently. The U4 factor
listed here is the 007 factor, as the table header says. The independent
three-candidate critical coefficients also show that every U test still
fails for each of 007,013,014. K2/K3 are left at their printed targets;
no value below those targets is asserted. For D rows an upper radius is
already the conservative direction.

## Scope repairs and later evidence

All seven repairs required by T4-445 are present. Scalar and original
graded exclusions are separated from dyadic exclusions; 025 and 026 are
RULED OUT in the named families; the two-projection test promises no
verdict when its lower bound fails to refute the necessary inequality;
S and N1 are tied to their sharp/sharpw certificates; section 7 cites
T4-443; the erratum says no candidate exclusion changes; DK is defined.
At 009 a two-mode test can fail while the complete norm excludes the
cell, so inconclusiveness is the correct logical alternative.

The new 026 statements are supported by T4-446 to T4-450 with raw hash
2978faab0e8b4a1da1ec06991ebaf03eb9bfa7ed388b0dbbae9d955ca3a095f3.
Their accepted weak distance floor is strictly 0.001355907204057457,
above the common scalar ceiling 3.7930e-6 and the original graded ceiling
25/54684. This uses the fixed-c real S1 weak identity with L2 correction
and its regularity hypotheses. It neither orders different candidates
by distance nor proves a dyadic exclusion. The frozen preview calls
N4's reciprocal acceptance pending; N4-377 to N4-379 have since completed
it, so the published successor should update that historical status.

The 016 low-order forcing statement agrees with T4-451. For s>=0,
Plancherel gives ||(1-Delta)^(s/2)f||2>=||f||2 for f in L2, also in the
extended sense. If F is H1, its accepted strict lower G0 and G1 bounds
therefore give X_(s,w)(F)>sqrt(w1*ell1^2+w2*ell0^2). This proves failure
of the specified sufficient forcing tests. It does not require P2 or a
negative homogeneous norm. No inverse or distance theorem follows.

The endpoint wording correctly separates a constant-coefficient cap
below 1.421e-7 from the variable-envelope integral cap below 1.43912e-7.
The extra V>=v0 condition gives the latter class a cap below 1.14141e-7
at the translation target. The currently chosen list gives a cap below
2.66323e-8. At the two small Db targets an improved admissible universal
constant remains OPEN. A lower bound on all valid constants constructs
no admissible constant. Exact TB-rebal rounding has since been corrected
to the upper bound 3.5126e-7 by T4-454. No common-ceiling exclusion changes.

## Verdict and evidence boundary

CONFIRMED: the changed mathematical statements with their specified
certificate scope, all 24 printed-target factor divisions, and the nine
new exact-ceiling factors and three H0-only remainder factors above.
The bracket assumptions of T2 BB2 and BE2 are discharged by T4-454.
The 026 and 016 additions follow from the separately accepted results.
Historical source hashes identify the frozen preview, not current mutable
reports. Matching immutable appendix files are frozen and checked; changed
live reports are explicitly recorded without declaring them hash matches.

Before publication update the reciprocal 026 status, cite T4-451 and
T4-454 where their independent acceptance matters, and use 3.5126e-7 for
the TB-rebal upper ceiling. These are successor updates to this frozen
13:55 object. The later theory final draft and the complete matrix are
separate audit objects. No existence theorem, sharp inverse or unrestricted
nonexistence statement is proved here. All finite arithmetic uses exact
JSON inputs and Arb balls; no spatial integral or peer code is executed.
