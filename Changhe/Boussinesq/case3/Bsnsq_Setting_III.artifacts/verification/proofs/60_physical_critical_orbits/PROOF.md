# Physical temperature critical points on escaping trajectories

Date:2026-10-20. Status: CONFIRMED by independent derivation of the physical jet equations.
Actual Opus requests did not provide a written audit; see Section8.
This audits the coordinate-free extension in the lead's audit56 and gives
a further finite-order extension. Both are restricted results, not a full
endpoint and not a statement about nonzero angular extrema at beta>2.

## 1. Setting and exact statements

Let beta>=2 and let a smooth full-plane B2 profile satisfy the prompt,
including the canonical whole-plane relative inverse, sublinear velocity,
x-reflection, the zero-axis temperature and nonzero quadratic center jet.
Put c=beta-2, W=beta X+U-U(0), so

    divW=2beta, -curlW=Omega,
    W.gradTheta=c Theta,
    W.gradOmega+Omega=Theta_x.                           (1)

Assume Omega has one weak sign in x>0. Let O be a complete forward-escaping
trajectory contained in x>0 and suppose gradTheta(Y0)=0 at one point Y0 on O.

Theorem A. On the entire orbit,

    gradTheta=0, D^2Theta=0, Omega=0, gradOmega=0.          (2)

If beta>2, also Theta=0 on O. No condition on the backward limit set is
needed. This is the coordinate-free statement proposed by lead audit56.

Theorem B. Suppose additionally that O converges backward to a single
equilibrium p and DW(p) has no negative eigenvalue. If at one point of O
the temperature has a first nonzero positive-order derivative of finite
order N, then N is odd and N>=3. In particular a local extremum of Theta
at any point of O must be flat relative to its value. Then Theta-Theta(Y0)
and Omega are flat along all of O. For beta>2 the value Theta(Y0) is zero.

Only the following previous inputs are needed. Outward radial flow from
W=beta X+o(|X|) gives completeness and bounded negative semiorbits; all
fixed-order smooth jets are bounded on their compact closures. Packet56
proves that weakly signed nontrivial Omega in the full-plane target forbids
every horizontal forward-escaping orbit in x>0. Its nonzero angular tail
and canonical inverse hypotheses follow for the full target from
packets33,39,40. There is no need to assume a scattering parametrization
for the present proof.

## 2. First derivatives and vorticity zeros

Write X'=W(X), A(t)=DW(X(t)), g(t)=gradTheta(X(t)). Differentiating(1) gives

    g'=(cI-A^T)g.                                        (3)

This is a homogeneous linear ODE on any finite time interval. Since g is
zero once, uniqueness makes it zero for all time, including backwards.
Equation(1) then gives cTheta=0 on O. When c=0, Theta is constant along O;
when c>0, that constant is zero.

The vorticity forcing Theta_x is now zero on O. Thus Omega'+Omega=0.
Boundedness on the negative semiorbit forces Omega=0 throughout O.
Every orbit point lies in the open sign domain x>0, so it is a local
minimum or maximum of the smooth signed Omega. Therefore gradOmega=0
at each of these points.

Differentiating the vorticity equation once gives

    d(gradOmega)/dt+(I+A^T)gradOmega=gradTheta_x.

The left side vanishes identically along O, and hence

    M e1=0, M=D^2Theta(X(t)).                             (4)

Differentiating the already identically zero g along O also gives

    M W=0.                                               (5)

These are identities along the whole orbit, not just at its initial point.

## 3. Hessian vanishing without a backward-limit assumption

If W2 vanished identically on O, that escaping trajectory would be
horizontal, contradicting packet56. There is therefore a time t1 with
W2(X(t1))!=0. At this point e1 and W form a basis of R^2. Equations(4)-(5)
force the linear map M(t1)=0.

Twice differentiating the temperature equation and using g=0 gives

    M'=cM-A^T M-M A.                                     (6)

All terms containing second derivatives of W are contracted with g and
vanish. The homogeneous finite-dimensional ODE(6), starting at M(t1)=0,
gives M=0 on O. This proves Theorem A. It neither uses a nonexistent second
derivative of a C1 angle nor assumes any backward equilibrium type.

## 4. Propagation of vanishing temperature jets

For any n>=1, let T_n=D^nTheta along O. The repeated product rule gives

    T_n'=(cI-sum_slots A^T)T_n
      - sum_{j=2}^n sym(D^jW contracted with T_{n-j+1}).   (7)

Here sym includes the ordinary product-rule multiplicities. In particular,
if all positive-order temperature jets below n vanish on O, T_n solves a
homogeneous linear system. Its vanishing at one time propagates along O.
Starting with(3), induction shows that any initially vanishing block of
positive-order temperature jets stays zero along the complete orbit.
If the first nonzero order at Y0 is N, then T_N is nonzero at EVERY point
of O, since otherwise the homogeneous order-N equation would make it
zero at Y0 as well.

Also differentiating the zero tensor T_{N-1} along O gives

    T_N(W,v2,...,vN)=0                                   (8)

for arbitrary fixed vectors v2,...,vN. This uses symmetry of derivatives.
Since W!=0 on an escaping orbit, a symmetric tensor annihilating W in one
slot is a scalar multiple of ell^{tensor N}, for a nonzero covector ell
annihilating W. Indeed choose a basis containing W; the only surviving
component has all slots in the second basis direction. This elementary
rank-one fact is useful but not required for the basis argument below.

## 5. Backward vorticity jets and even orders

We already know Omega=0 on O; continuity at the backward limit gives
Omega(p)=0. Since -curlW(p)=Omega(p), DW(p) is symmetric. Under the
additional hypothesis its two eigenvalues are nonnegative.

Let J_n=D^nOmega. The exact product rule from packet59, also checked by
independent symbolic multi-index differentiation, gives

    J_n' + L_n(t)J_n = D^nTheta_x + lower Omega jets,
    L_n=I+sum_slots A^T.                                 (9)

Every term in the last group uses only J_m with m<n. If n<=N-2, its
forcing D^nTheta_x vanishes because it has temperature order n+1<N.
For the symmetric limit M=DW(p), the operator L_n(p) on symmetric
n-tensors has eigenvalues1+k lambda1+(n-k)lambda2>=1. Along backward
time tau, a homogeneous J_n solves J_n'=L_n(-tau)J_n, so eventually

    d|J_n|^2/dtau>=|J_n|^2.

The convergence of L_n(-tau) to its symmetric positive limit suffices;
no convergence rate is assumed. Boundedness of every physical jet on
the compact negative semiorbit forces J_n=0. Induction gives
J_0,...,J_{N-2}=0.

If N were even, the leading possible Omega Taylor polynomial of degree
N-1 would be odd. Its weak sign on a neighborhood inside x>0 forces it
zero. Thus J_{N-1}=0 along O too, and(9) at that order gives

    T_N(e1,v2,...,vN)=0.                                 (10)

At a time with W2!=0, equations(8) and(10) annihilate a basis in one slot,
and hence T_N=0. Its homogeneous transport then contradicts the stipulated
nonzero first jet at Y0. This proves that N is odd. Theorem A already
excludes N2, consistently with this argument.

At a local extremum, the first nonzero homogeneous Taylor polynomial,
if any, must have even degree: every nonzero odd polynomial changes sign
under z to -z. Therefore there is no finite first order. The temperature
is flat relative to its value at Y0. Equation(7), order by order, transports
all its positive-order zero jets along O. For every fixed n, the forcing
and lower jets in(9) then vanish, and the same backward growth makes J_n=0.
Thus Omega is flat along O as claimed. No infinite-order norm estimate or
analytic continuation is used.

## 6. Scope checks and saddle limits

At a saddle limit with eigenvalues -nu and2beta+nu, the finite even-order
argument remains valid for N>=4 if nu<1/(N-2). Equality cannot be added by
this proof: packet59 gives exact local coupled weak-sign solutions with
surviving even Omega jets at equality. Those examples extend to general
beta by replacing4 with2beta in W2, but they are not global target profiles.
There is no all-order flatness conclusion from this growth argument at a
fixed saddle nu>0.

For beta>2 an extremum of a nonzero angular amplitude generally is NOT a
physical critical point. If local orbit coordinates satisfy
Theta=e^{ct}H(alpha), then gradTheta=e^{ct}(cH gradt+Hprime gradalpha).
Thus Hprime=0 but H!=0 does not qualify for either theorem. If H=Hprime=0
and the coordinates are C1, it does qualify and Hsecond must vanish, by
the critical-point composite Taylor argument. This is a restricted
zero-level statement.

Theorem B does not exclude an odd-order critical inflection, a flat
extremum or an open plateau. Flat smooth jets along a curve do not imply
zero on a neighborhood. It supplies no complete NO for beta2 or beta>2.

## 7. Provenance and verification

The coordinate-free proposal was read directly in the lead's
astra/audit56/PROOF.md, lines299-319. A local copy and hash accompany
this proof. Theorem A has an independent proof here; Theorem B is the
verifier's own extension of the bounded-jet method. No numerics-lane code
is used. The complete informal proof precedes any formalization, and
formal/README.md records that no Lean/Lake execution is permitted.


## 8. Actual review limitation

The independent verifier reread and checked every displayed transport,
sign and tensor equation in Sections1-6 on2026-10-20. TheoremA does not
require the singleton-limit input, whereas TheoremB does. The previously
completed exact multi-index checks in packet59 also check the product
rule used in TheoremB. There is no formal proof-assistant verification.

Actual Opus requests58 and59 returned model claude-opus-5-5 but no written
audit, stop_reason refusal, after5.064241092 and5.078431171seconds. The raw
responses label the refusal category cyber. This is an availability
limitation, not a mathematical objection or an endorsement. No substitute
model was used. TheoremA is also proposed in lead audit56; the proof here
is independent. TheoremB remains the verifier's independently derived
extension, with its external model review unavailable.
