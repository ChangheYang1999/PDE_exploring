# Candidate 017: independent dual modes and residual replay

## Exact statement and hypotheses

Fix the immutable potential C1-N1-017-legqs50-quot013 with SHA256
7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114,
c=4076476460239181/2251799813685248 and delta=1-1/c. On R2 with
Lebesgue measure put rho=-partial_y Delta chi, U=(-chi_xyy,chi_xxy)
and F=(cX+U).grad rho-rho. Define H(F) as the supremum of |int F phi|
over real smooth compactly supported phi with ||grad phi||2<=1.
The source is the exact finite rational radial and angular representation
specified in ../joint_scaled_factored_weak/PROOF.md. All angular products
that contribute to a requested sine frequency are retained.

For an odd positive frequency n and every saved exact coefficient x_i,
beta_i>3/2 and integer k_i>=-1 with 3+2k_i-n even and nonnegative, set

 psi_n=u_n(r)sin(n theta),
 u_n=sum_i x_i r^3(1+r^2)^(-beta_i)(r^2/(1+r^2))^k_i.

The vectors are exact proposed data in source/N3_dual.json and
source/N3_hres.json. They are checked through the independent formulas
below. No property of a Galerkin solve is required. Write

 d=||grad psi_n||2^2, p=int F psi_n,
 Z=-u_n' sin(n theta)e_r-(r u_n''+u_n')cos(n theta)e_theta/n,
 a=||Z||2^2, b=<A_Fn,Z>, Qn=||r F_n||2^2,
 A_Fn=-r f_n(r)cos(n theta)e_theta/n.

For every accepted trial with d>0,

 H(F)^2 >= sum_n p_n^2/d_n.                               (1)

For a single mode whose Qn is finite, put

 Rn^2=Qn+2n^2(b-p)+n^2(a+d).

Then Rn=||r(F_n+Delta psi_n)||2, and

 max(0,sqrt(d)-Rn/n,|p|/sqrt(d)) <= H(F_n)
                         <= sqrt(d)+Rn/n.                (2)

Every term in (1) must have a different angular frequency. This topic
recomputes all sixteen saved dual trials at n=1,3,...,31. It also checks
the independent residual trials at n=1,3 through (2). It does not claim
independent reproduction of the remaining fourteen residual trials,
all160 Hardy squares, or complete G0,G1,P2 for candidate017. Replaying
the peer's totals as finite interval arithmetic has exactly those source
premises and is labelled conditional arithmetic, not a PDE certificate.

## Proof of admissibility, duality and residual identity

At the origin each trial is smooth because its angular numerator is a
harmonic polynomial times a nonnegative even power of r. At infinity
u,u_y,u_yy=O(r^(3-2 beta_min)), with y=log r. Thus grad psi and r Delta psi
are square integrable. Smooth radial cutoffs approximate psi in gradient
norm: the squared error is O(R^(6-4 beta_min)), tending to zero. Every
pairing integral used below is separately checked for absolute convergence.
Its cutoff integrals therefore converge by dominated convergence.

For finitely many distinct frequencies, cutoff the sum
sum_n(p_n/d_n)psi_n. Orthogonality gives its limiting squared gradient norm
sum_n p_n^2/d_n, and its limiting pairing has the same value. The definition
of H proves (1), including the case H(F)=infinity. Thus the lower bound
needs no unverified complete candidate017 Hardy integral.

For a single mode, div A_Fn=F_n in distributions and
||A_Fn||2=sqrt(Qn)/n. This follows by angular differentiation on annuli;
the radial flux is zero, so no point mass occurs at the origin. The
single-mode Hardy inequality H(G_n)<=||rG_n||2/n follows. The gradient
completion identity H(Delta psi)=||grad psi||2 follows by integration by
parts and approximation. The triangle inequality gives (2), together
with its dual lower bound.

In logarithmic radius, r^2 Delta psi=(u_yy-n^2u)sin(n theta). Integration
by parts in y is valid by the origin and infinity decay. Hence

 ||r Delta psi||2^2
 =pi int[(u_yy)^2+2n^2(u_y)^2+n^4u^2]dy=n^2(a+d).

Also int r^2 F_n Delta psi=n^2(b-p), directly from the definitions of
A_Fn and Z. Expanding the square proves the formula for Rn^2. There is no
subtraction of numerical midpoints: every term is a containing Arb ball.
If cancellation leaves insufficient precision, the computation fails.

## Complete exact radial formulas

Set t=r^2/(1+r^2), v=1-t, b_i=beta_i-1 and
P_b=sum_(i:b_i=b) x_i t^(k_i+1), so u=r sum_b v^b P_b.
Define D_bP=(1-2bt)P+2t(1-t)P'. Then

 d/pi=(1/2)sum_(b,c) int_0^1 v^(b+c-2)
                    [(D_bP_b)(D_cP_c)+n^2P_bP_c]dt,
 a/pi=(1/2)sum_(b,c) int_0^1 v^(b+c-2)
                    [(D_bP_b)(D_cP_c)+(D_b^2P_b)(D_c^2P_c)/n^2]dt.

Expand in v and integrate each monomial as 1/(exponent+1). All exponents
exceed -1. These two quantities are exact rationals. In particular d/pi
must equal the source's complete exact rational, not its shortened text.

Reconstruct the complete projected residual directly from the raw chi:

 f_n=r sum_ell v^(ell delta/2) A_(ell,n)(t).

The own projection algorithm differentiates every potential generator and
retains all compatible velocity-gradient products. Its derivation and
sign folding are in ../joint_scaled_factored_weak/PROOF.md. This is the
previously checked general source algorithm, applied to017. No coefficient
identity with the accepted016 Cartesian field is asserted. The raw017
candidate structure and its earlier independently checked weak records
are dependencies. The new computation records its complete projection hash
and contributing product count. Peer F caches are neither copied nor read.

The pairings are

 p=(pi/2)sum_(ell,b) int_0^1 v^(ell delta/2+b-3)t A_(ell,n)P_b dt,
 b=(pi/(2n^2))sum_(ell,b) int_0^1
                       v^(ell delta/2+b-3)t A_(ell,n)D_b^2P_b dt.

For Qn, retain every ordered branch pair and use

 Qn=(pi/2)sum_(ell,j) int_0^1
                 v^((ell+j)delta/2-4)t^2 A_(ell,n)A_(j,n)dt.

Combine equal exponents before integration. For each complete rational
group, extract its exact zero order q at v=0. Require its resulting
exponent greater than -1. Positive denominator factors1+s v never vanish
on[0,1]. These checks prove absolute convergence for each group.
The own rational-pole moment engine checks exact partial fractions and
returns an outward Arb interval. No quadrature, finite radius, sampled
angular transform, optimizer convergence or basis completeness is used.

## Export, assembly and scope

Use4096bits internally and650digit containing exports of every integral
group. Reparse the exported JSON and require the accumulated absolute
radius below10^-200, at least600bits in each final pairing and square,
and containment of the full internal sum. Endpoint floors and ceilings
are exact rationals, strictly outside the resulting balls. Distinct trial
families are never silently identified: hdual uses the integer beta class
in addition to eight other classes, while hres uses eight classes.

Finite peer-total replay checks source hashes, distinct mode coverage,
nonnegative containing intervals and the formulas for H and
E2^2=P2^2+2^14G1^2+2^18G0^2+(20/21)2^18H^2. It can confirm correct directed
arithmetic from those inputs. It cannot validate an uncomputed integral
merely because another recorded total agrees. The full017 upper bound,
complete017 E2 and the ordering017<007 remain OPEN until all required
source-specific component certificates are independently accepted.

Dependencies include the own radial field and weak projection proofs,
the rational-pole moment proof, the general dual/Hardy proofs accepted
through T4-466/T4-469 and the actual existing Opus reviews, and source-bound
017 structural/weak certificates. Freeze exact input hashes before the
run and recheck afterward. Peer programs are retained as text only.
No inverse, correction distance, nonlinear closure or existence follows.
