# Topic95: explicit finite bound for an auxiliary source inverse

Read PROOF.md, ADDENDUM.md, AUDIT_METHOD.md and CLOSURE_NOTES.md together.
The final authority is evidence/verdict.json after its finalizer passes.

The exact normalized modal_v2 trial has the certified source P=(p,0),
delta=33/2000, M_V<0.2972 and M_rho<0.5059 on B_(3delta)(P).
Choose the explicit compact C4 cutoff in PROOF, equal1 on B_(2delta),
supported inside radius23delta/8, with delta|grad theta|<=1472/819<2.
Set w=theta(V-DV(P)(X-P)), q=theta(grad rho-(0,rho_y(P))).
For every s in[3.05,3.1], on its maximal distributional Hs transport
domain, the auxiliary operator

 A_s u=(DV(P)(X-P)+w).grad u-u-rho_y(P) M u+q.U[u]

is invertible, with ||A_s^-1||<1.2e35 uniformly. Sharper proved ceilings
at the three named orders are2.672e34,3.518e34,1.068e35 respectively.
All figures are strict rational outward ceilings.

Two independent enclosure methods cover seven full original spline spans
and all261 modes. Arb512 uses Bernstein polynomial ranges, exact scalar
ODE endpoint majorants and complex derivative ladders. mpmath.iv180 uses
absolute monomial ranges, Gronwall envelopes and Cartesian recursions.
Each computes11004 polynomial derivative envelopes and3654 moment
whole-span envelopes. The common conservative Frobenius ceilings are

 ||D^3rho||<505, ||D^4rho||<24381, ||D^5rho||<3758450,
 ||D^3U||<6376, ||D^4U||<87933.

Together with the exact cutoff derivatives these give finite H4 bounds
for w and q and explicit Wiener commutator bounds. The complete producing
run took49.93 seconds. A fresh output audit used Arb1536/iv250,1344 exact
mixed Cartesian identities and a monotone argument for all s in the
interval, rather than interpolation of sampled parameter values.

The canonical moment boxes and topics84,85,89,78,92 are imported checked
dependencies. This is not a second whole-plane canonical integration.
The cutoff is generally C4, not C5. The physical rank-one strain term is
omitted. The result supplies a finite number for this particular auxiliary
inverse; it does not establish a global IPM inverse or close the proposed
nonlinear estimates. A large upper bound is not a lower bound on the true
inverse norm. No decisive endpoint has been reached.
