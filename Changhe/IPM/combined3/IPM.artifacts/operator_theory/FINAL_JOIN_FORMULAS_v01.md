# Exact formulas used by the final scalar consumer

Status: analytic assembly formula. Numerical PASS is withheld until every
actual certificate is complete and bound to its unchanged source/code.

The consumer is `assemble_fixed_parameter_closure_v01.py`. It fixes
\[
c=4076476460239181/2251799813685248,\quad q=21/10,\quad\delta=1/10,
\quad W²=1+4r²,\quad\beta=7/10,
\]
\[
R=381377/10^{12},\quad\beta_2=2087491/10^6,
\quad f_2=7961207/10^{13},\quad n=759/100000.
\]
The completed direct L2 certificate gives beta_actual>beta2 and the exact
rational check gives R beta2>f2. The forcing certificate gives ||F||2<=f2,
Q(F)<=n. The remaining actual matrix/local/source constants enter below.

Let K1,K0 be the local correction uppers from the exact local identity,
Wu2=sup W|D²u|F, H1=sup W|Db|F, and A2,Aq the source commutator moment
constants. Let Bj=||D^j b||2, Xj=||D^j(xb)||2. Define
\[
U_2=\tfrac12\sqrt{B_1B_3},\quad
U_3=\tfrac12\sqrt{B_2B_4},
\]
\[
XU_3=\tfrac12\sqrt{[X_2+(\sqrt2+1)B_1]
[X_4+(\sqrt2+1)B_3]},
\quad T_3=\frac{51}{1000}(U_3+2XU_3+6U_2).
\]
These are containing velocity-moment bounds, not new independently
sampled profile norms.

For Rb equal to10000,30000 or100000, the source envelope certificate gives
a0>=sup|b| and a1>=sup_(r<=2Rb) r|b|, while the actual far source
certificate gives Bfar>=sup_(r>=Rb)|b|. Put
\[
Bnear=\sqrt{a0²+4a1²},\qquad
e_f=\frac{3Bfar²}{4(c+1-\beta)}.
\]
The first bounds W|b| on the needed near region. The second consumes only
the explicit negative weighted-f allowance in the local identity; all
other auxiliary near/far commutator prices are absent from this branch.

For a trial M in(0,1/2], let r=R/M, cq=q(q-1)/2. The exact exterior
background loss used by the consumer is
\[
\boxed{\begin{aligned}
e_{bg}={}&e_f+(K1+Bnear)r^{20/21}+K0r^{40/21}\\
&+\frac{q\delta}2Wu2\,r^{10/21}+T_3r^{11/21}\\
&+qH1r^{10/21}+cqA2r^{20/21}+cqAq\,r.
\end{aligned}}
\]
Each exponent is positive, so interpolation proves this bound uniformly
for every test with ||g||<=R and Q(g)>=M. Add the independently reviewed
nonlinear loss LQ(R,M), without changing its outside-ball scope, and put
\[
b=\beta-e_{bg}-LQ(R,M).
\]
The actual strict scalar checks are
\[
b>0,\qquad bM²-nM>0,\qquad
\frac{5M}{\beta_2\sqrt{11\pi}}<1.
\]
Together with the completed actual input certificates, these are exactly
the hypotheses of the forced-evolution bridge. That bridge proves a whole
actual frozen inverse/self-map and an L2 contraction; it does not infer a
high inverse merely from a formal energy estimate.

## An equivalent global background Garding pair

List each nonconstant background rate as ai r^ei and put ti=ei/2. All ti
lie strictly between zero and one. For any actual g, weighted AM-GM (or
the tangent to z^ti at z=(R/M)²) gives
\[
ai\|g\|^{ei}Q(g)^{2-ei}
\le(1-ti)ai r^{ei}Q(g)²+ti ai r^{ei-2}\|g\|².
\]
Consequently the certified global background form has
\[
\epsilon=e_f+\sum_i(1-ti)ai r^{ei},\qquad
C=\sum_i ti ai r^{ei-2},
\]
\[
E_*(g)\le-(\beta-\epsilon)Q(g)²+C\|g\|².
\]
At the stipulated trial radii the scalar margin is identical:
\[
(\beta-\epsilon-LQ)M²-nM-CR²=bM²-nM.
\]
The consumer additionally rounds epsilon and C upward to explicit rational
numbers, verifies both outward comparisons in Arb, and checks the rounded
margin remains strictly positive. This supplies a conventional global
background high-energy pair if desired, without using it to justify an
unproved generator domain or a global nonlinear dissipation claim.

## Certificate discipline

The consumer checks exact source hashes; all current producer/evaluator
bindings; complete base-panel and adaptive-leaf coverage; the actual L2
used-chunk and far-cache hashes; the independent L2 replay; and the exact
forcing arithmetic. Wu2 is reconstructed from saved Hu leaves with their
exact rational geometry and from the proved endpoint bounds. Missing or
invalid data cannot produce PASS. Its current incomplete status is not a
stationary existence claim. After complete numerical PASS and independent
consumer review, the listed analytic proofs yield the concrete fixed-c
stationary theorem, including derived origin strain and actual Darcy
velocity/pressure.
