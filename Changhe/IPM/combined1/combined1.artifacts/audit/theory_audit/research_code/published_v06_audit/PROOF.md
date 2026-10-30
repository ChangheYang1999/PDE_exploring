# Audit of published theory_v06 and the second annular-moment review

## Statement, sources and scope

This audits the frozen 988-line theory_v06, SHA256
493549a9b49ac3eb0fd2c115c90c4ac8e5e9513305c38eb3f41598c31801b6bb,
read in full. The unchanged mathematics is covered by T4-312,328-330,336,
341,347,352,358. New status records are compared with T4-360 through372.
The frozen R1-037 is T1 review set 34, SHA256
d25fa09bf5783e9a55b10a2a6057e70747cf61750be3f576d3eed0d7ba70eea4.
Current copies of THEORY_FINAL and NUMERICS_FINAL in source are separate
snapshots, not the documents certified by this statement.

The publication correctly repairs the unchecked hypotheses (A),(B0n),
H3,H4 for007, the two dependencies of the third-cutoff endpoint theorem,
the angular-band lower-bound qualification and the fixed-c exclusion
scope through020. It correctly keeps all new norms apart from an inverse,
and the endpoint tail coefficient apart from a whole-plane L2 distance.
All51 table ratios are conservative against the displayed rounded-up
family ceilings. The closure inequalities and commutator requirement of
T4-358 are unchanged. The source constants and inequalities are checked
again in code/check.py. No existence conclusion follows.

## The scaled-generator index

The publication fixes the sector convention e(l,q)=1-l delta-2q. Its
T4-360 to362 summary says both scaled blocks enter only at l>=4. This
uses the wrong index. The exact expansion in T4-362 is

    R^(2Q) z^Q (1+z)^(p_j-m)
      sum_k b_k (1+R^2 z)^(-w-Q-k),   z=r^-2, Q=4.

Thus they enter at q>=4, while j=1,2,3 corresponds to l=j+1=2,3,4.
For n=0 the leading potential coefficient is R^8 and is nonzero.
For j=1,m=9 its degree d=2p_1-8 is noninteger and its density coefficient
in mode19 is -R^8(d^2-18^2)(d-20)/2, which is nonzero. It occurs at
(l,q)=(2,4). This supplies an exact counterexample to l>=4. The accepted
sixteen-sector prefix is unchanged, because it uses q<=2.

## R1-037 remarks (a), (b), (c)

Use the compact smooth S1 function f=eta(r)sin(theta) of T4-359, with
support 1<r<2 and integral y f=1. Set h_R=m R^-3 f(X/R), R>=1. Here
X is the fixed sharpw high norm, and

    H_q(h)=sup_X ((1+|X|)^(-q)|h(X)|
                 +(1+|X|)^(1-q)|grad h(X)|).

The audited construction gives X(h_R)<=C_X |m| R^-2 and
H_q(h_R)>=c_q |m| R^(-q-3), with positive constants independent of R.
Hence H_q(h_R)/X(h_R)>=c R^(-q-1), proving no bounded embedding X->H_q
on compact smooth S1 functions for any q<-1, as R1-037(a) claims.
For a sequence with X tending to zero and H_q tending to infinity,
choose m=R^alpha with q+3<alpha<2. Its support remains away from the
origin, its velocity is zero there and c[h_R]=0. A fixed nonzero moment
also has X cost tending to zero. No weighted a priori budget follows.

For any compact smooth S1 correction h, its mass and x first moment
vanish. Taylor expansion of the logarithmic Newton kernel outside twice
the support radius gives

    U[h]=m_y(cos(3theta),sin(3theta))/(pi r^3)+O(r^-4).

The differentiated remainder is valid because h is smooth and compact.
If grad rho=r^(gamma-1)(gamma Theta e_r+Theta' e_theta)
+O(r^(gamma-1-epsilon)), epsilon>0, then outside the support the entire
residual change is U[h].grad rho. Its endpoint coefficient is therefore
(m_y/pi)P, P=gamma cos(2theta)Theta+sin(2theta)Theta'. This confirms
R1-037(b): the part orthogonal to P is invariant under compact changes.
The existing exact projection audit supplies the three candidate values.

If support(h) is in the disk of radius A, Cauchy-Schwarz and
integral_disk y^2=pi A^4/4 give ||h||2>=2|m_y|/(sqrt(pi)A^2).
Putting A=2R confirms R1-037(c)'s optimal power R^-2.

## R1-037 remark (d): the drift term cannot be dropped

Fix m!=0 and c>0. Assume the reference satisfies the growth hypotheses
of T4-359: |U[rho]|<=V r^gamma and |grad rho|<=G r^(gamma-1) on r>=1,
with gamma<1. Put A_c=||(c X.grad-1)f||2, and let A_v,A_g,A_n be the
finite constants defined there. The exact residual expansion and reverse
triangle inequality give

    abs(||F(rho+h_R)-F(rho)||2-|m|A_c R^-2)
      <= |m|(V A_v+G A_g)R^(gamma-3)+m^2 A_n R^-6.       (1)

Indeed the drift contribution has exactly the norm |m|A_c R^-2;
the three remaining terms satisfy the displayed error bound. Moreover
integration by parts on the compact support gives

    <(c X.grad-1)f,f>=-(c+1)||f||2^2,

so A_c>0. Since gamma<1, (1) proves

    ||F(rho+h_R)-F(rho)||2 ~ |m|A_c R^-2.

R1-037(d)'s O(R^(gamma-3)) claim for the complete residual change is
therefore false. Its correct power is R^-2. The upper estimate was
already correct in the main review, item8 and the stated theorem.
This also clarifies T4-371's concern: the drift contribution gives the
leading norm as R tends to infinity, but a lower bound at every finite R
requires the error terms in (1). The background constants are not
certified for the candidates. For L2 residual norms, the reverse triangle
inequality bounds the change by the norm in (1). Transfer of other
weighted residual norms needs estimates in those norms, not (1).
Fixed-c distance exclusions transfer only with the explicit triangle
inequality margin exceeding ||h_R||2, as already stated in theory_v06.

## Remaining documentary points

R3 item9 cites the specialized annular ceiling 2.839272409e-6 from
T4-278. Its hypotheses must remain explicit: globally H2 corrections
supported in20<=r<=32 with only sine frequencies n>=19. The number is
valid under those hypotheses. It is not the unrestricted sharpw ceiling
(2mu0/3)sqrt(mu0/(3C'))/((8/5)1024)=2.849577738...e-6, with
mu0=97/250 and C'=397. These are different bounds for different classes,
not different estimates for the same envelope. Replace the bare phrase
annular corrections by the exact support and angular hypotheses, or use
the unrestricted ceiling. This scope clarification changes no exclusion.

The phrase 'pre-registered runs' for021,022 should follow the coordinator's
09:01Z and09:27Z qualification: the 08:33Z declaration follows the08:32Z
launch. The older25-probe register and analytic span separation are the
supported evidence. This is a provenance limitation, not a weakening of
a certified necessary weak test.

The publication's OPEN labels for359 and369 were correct at its ledger
cutoff. T4-370 now accepts359's independent review; T4-369 confirms the
abstract higher-angular rank, with actual future snapshot binding still
separate. T4-371 confirms weighted-budget moment interpolation. T4-372's
new sharp amplitude constant is still OPEN independent review.

## Verification

Exact fractions check the table, sector counterexample, scaling powers,
closure rate, self-map slack and same-family commutator cap. Directed Arb
evaluation encloses the positive square roots. Source and dependency
hashes, runtime and UTC are in verification/result.json. No publisher
code is executed. This audit supplies neither an inverse nor existence.
