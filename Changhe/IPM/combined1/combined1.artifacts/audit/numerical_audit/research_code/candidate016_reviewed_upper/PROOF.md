# Reviewed complete upper bound for candidate016

## Exact statement, hypotheses and notation

Fix C1-N1-016-legqs25-quot013, raw SHA256
a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42,
and c=4076476460239181/2251799813685248. The exact generator convention
and its complete rational source are those accepted in N4-392, with
rho=-partial_y Delta chi, u=(-chi_xyy,chi_xxy) and
F=(cX+u).grad rho-rho, including the canonical local velocity term.
All functions and tests are real; norms use Lebesgue measure on R2.
Define H(F)=sup{|int F phi|:phi in C_c^infty(R2),||grad phi||2<=1}.
The complete source has1360 branches and exactly the160 odd sine
frequencies1 through319. Define G0=||F||2, G1=||grad F||2 and
P2=||(1+4r^2)^(2/5)D2F||2, with the Euclidean Hessian norm, and
E2^2=P2^2+2^14 G1^2+2^18 G0^2+(20/21)2^18 H(F)^2.
The exact polynomial representation is regular at the origin. Every
positive-pole denominator is positive on the compact radial interval.
The accepted complete392 integrals establish rF,G0,G1,P2 in L2.

The candidate's H and E2 satisfy the strict bounds

 0.529469576110 < H(F) < 0.619652,
 608.392385921614 < E2(F) < 629.296113.

At the same definition and weights E2(007)<606.820219, hence
E2(016)-E2(007)>1.572166921614. Sharper exact rational endpoints
are retained in the bound assembly. These are bounds, not exact norms.

## Complete informal proof

Write F=sum f_n(r)sin(n theta). Let q_n=pi int r^3 f_n(r)^2dr,
R2=||rF||2^2=sum q_n and
A=-e_theta r sum f_n(r)cos(n theta)/n. Angular orthogonality gives
||A||2^2=M2=sum q_n/n^2<=R2. Angular integration by parts on annuli
shows div A=F. The origin limit follows from local regularity of F
and L2 of A; no radial flux is present. Thus H(F)<=||A||2.
For N=31 and m=33, every omitted n>=m. Nonnegativity gives

 M2 <= R2/m^2+sum_(n<=N)(1/n^2-1/m^2)q_n.

All coefficients are positive. The accepted complete R2 upper and
upper endpoints of the16 complete source integrals therefore give a
rational upper U_M, even though144 modes have no individual integral
in this prefix certificate. This proves the tail step directly. N4-409
checks it against the source-bound650digit groups; N4-407 separately
reconstructs the same general tail reasoning and reciprocates T4-476.

For the accepted smooth single-mode tests psi_1,psi_3, all663 exact
labels have beta>3/2, k>=-1,3+2k>=n and even difference. The tests
are smooth at the origin, their gradients and r Delta are L2, and
radial cutoffs converge in gradient norm. For
Z_n=A_(Delta psi_n)-grad psi_n, div Z_n=0, a_n=||Z_n||2^2>0 and
b_n=<A,Z_n>. Distinct frequencies make Z_1 and Z_3 orthogonal.
For every compact test the divergence-free correction changes no
pairing. Cauchy-Schwarz and completing two scalar squares give

 H(F)^2 <= M2-b_1^2/a_1-b_3^2/a_3.

The accepted398 exact denominators and399 complete650digit signed
pairings give a strict rational improvement lower J. Thus H(F)^2
<U_M-J. The domain, distributional signs and polar formulas are
independently reviewed by T2 and T1 in404/408, and all candidate labels
and integrability conditions are checked in396/398/399/408. This
explicit composition discharges the earlier saved numerical result's
general analytic-review condition. The additional T1 R1-050 tail
review is still pending at preparation; it is not represented as
completed here. The displayed finite tail inequality is proved above,
with its independent T4 review and own exact arithmetic already bound.

For the lower bound set p_n=int Fpsi_n and d_n=||grad psi_n||2^2.
Cutoff convergence and angular Hardy pass these pairings to the dual
norm. The gradient norm squared and F pairing of
sum(p_n/d_n)psi_n both equal sum p_n^2/d_n. This gives
H(F)^2>=sum p_n^2/d_n, with strict rational quotient floors supplying
L_H^2. Insert the same accepted G0,G1,P2 endpoints into the positive
E2 square for lower and upper bounds. Check every displayed rational
by exact squaring and the energy gap by exact subtraction.

## Dependencies, finite verification and scope

Bind396,398,399,392,404,407,408 and prefix31 result409, including their
source and proof hashes. Recompute U_M from the saved individual q
upper dyadic endpoints and complete R2 upper as exact rationals.
Verify all16 frequencies and the complete source identity, select only
the two distinct accepted improvements, reconstruct both H squares
and both E2 squares, and check strict displayed endpoints. Hash checks
preserve identity; accepted source moments and the proved identities
are the mathematical premises. No overlap test is a proof premise.
No peer code, quadrature, new moment or optimizer is executed.

This result accepts its own upper, not N3's narrower display or an
017 norm. It orders the registered energy only, not correction
distances. It proves no inverse, nonlinear contraction or stationary
solution and changes no exclusion. Peer configuration is
us.anthropic.claude-opus-5-5, with actual provider response identity
unobservable. No substitute model or remote client is used.
