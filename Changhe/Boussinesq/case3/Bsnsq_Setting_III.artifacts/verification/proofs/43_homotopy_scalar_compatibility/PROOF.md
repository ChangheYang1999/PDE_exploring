# The scalar compatibility condition in the forced continuation

Date:2026-10-20. Verdict: CONFIRMED as a conditional functional-analytic
statement. Whether it causes the measured numerical stalls is OPEN.
Source audited: numerics astra/stall1/homotopy/PROOF.md, read independently
2026-10-20. This is not a profile existence theorem.

## Statement and hypotheses

Fix beta>2 and c=1+beta/2. Let E be a real Banach space of admissible
vorticities and ell:E->R a bounded nonzero linear center-strain functional.
Set H={q:ell(q)=c}, E0=ker ell. Suppose an open subset of H carries a
well-defined continuously Frechet differentiable transport map S:H->E.
For source s in H, S(s) is the vorticity obtained from the temperature
with coefficient a0=1 in W=beta X+B s, where B is the canonical relative
inverse. All profile, whole-plane weighted, basin and differentiability
requirements are assumptions here, not conclusions of finite samples.
Let e in H be the fixed external source and s_epsilon(q)=(1-epsilon)e+
epsilon q. The fixed-amplitude forced equation is q=S(s_epsilon(q)).
For epsilon>0 the nonzero quadratic temperature jet forces ell(q)=c:
ell(s_epsilon(q))=c and ell(e)=c imply epsilon(ell(q)-c)=0.

Choose d in E with ell(d)=1 and let Qv=v-ell(v)d,
Pv=v+(c-ell(v))d. If q0=S(e) belongs to H, then the projected equation
q=P S(s_epsilon(q)) has a unique nearby C1 solution curve q(epsilon).
The curve solves the actual forced equation precisely where

    m(epsilon)=ell S(s_epsilon(q(epsilon)))-c=0.

Writing A=DS(e):E0->E, its first derivatives are

    q'(0)=Q A(q0-e), m'(0)=ell A(q0-e).                (1)

If m'(0)!=0, no nearby true branch exists for small positive epsilon.
If m'(0)=0 this argument decides nothing. If ell S(e)!=c, no continuous
fixed-amplitude branch can approach the passive output S(e) as
epsilon decreases to0.

Alternatively suppose L0=ell S(e)>0. Allow a>0 and solve

    q=a S(s_epsilon(q)), q in H.                     (2)

There is a unique nearby C1 branch starting at
a*=c/L0, q*=a*S(e). It can equivalently be written

    q=[c/ell S(s_epsilon(q))]S(s_epsilon(q)).          (3)

This assertion only concerns sufficiently small epsilon and the assumed
C1 map. It gives no continuation guarantee to epsilon1.

## Proof

In the affine chart H=q0+E0, the derivative with respect to q of the
projected residual q-P S(s_epsilon(q)) equals
I-epsilon Q DS(s_epsilon(q))|E0. It is I at epsilon0, so the Banach
implicit-function theorem applies. Differentiating the source at0 gives
q0-e because the epsilon q' term vanishes. This proves(1). Subtracting
the projected equation from the original one shows that their difference
is exactly the scalar m times d. If m'(0)!=0, C1 continuity and m(0)=0
give m(epsilon)=epsilon m'(0)+o(epsilon), with constant nonzero sign
for small positive epsilon. Every nearby true solution must lie on the
unique projected branch and would contradict this scalar condition.
An O(epsilon^2) remainder is not justified by C1 alone. If L0!=c, continuity
and ell(q(epsilon))=c contradict q(epsilon)->S(e).

For(2), its derivative with respect to (q,a) at(epsilon0,q*,a*) is

    (h,alpha)->h-alpha S(e), h in E0.

For arbitrary z in E its unique preimage is
alpha=-ell(z)/L0 and h=z-[ell(z)/L0]S(e). Both operations are bounded,
and ell(h)=0. This proves invertibility and the local C1 branch by IFT.
Positivity persists by continuity. Applying ell to(2) solves for a and
establishes(3). The transported temperature and vorticity must both be
multiplied by a; adding a strain projection only to vorticity does not
give(2).

## Endpoint normalization and exact limitations

If an admissible branch reaches epsilon1 at finite a>0, it solves the
actual B2 equations with temperature jet a x^2. The exact spatial scaling

    Omega_tilde(X)=Omega(X/a),
    Theta_tilde(X)=a Theta(X/a), U_tilde(X)=a U(X/a)

gives coefficient1, unchanged beta and strain c. The kernel homogeneity
and the subtraction at0 give the stated relative velocity; chain rule
substitution gives both PDEs. Thus allowing amplitude in the forced
problem does not remove an epsilon1 branch from the normalized target.
At epsilon<1 the fixed external source breaks this scaling symmetry.

At epsilon1, q_lambda(X)=q(lambda X), a_lambda=lambda a is a symmetry
of(2), with Theta_lambda=lambda^-1 Theta(lambda X) and
U_lambda=lambda^-1 U(lambda X). If its infinitesimal generator belongs
to the differentiability domain, (X.grad q,a) is a kernel vector of the
endpoint equation. This is an exact symmetry, not by itself a fold.
Neither this kernel statement nor equation counting in a discretization
proves a Fredholm index, a cokernel dimension, discrete admissible beta,
or nonexistence at a fixed beta. A scale condition plus free-beta search
is a reasonable computational design, not a theorem of overdetermination.

The scalar ell A(q0-e) has not been independently evaluated for the
reported production state. The C1 whole-plane transport hypothesis is
also unproved there. Therefore the claim that this argument exactly
explains the observed O(1) residual floor is unsupported. It identifies
a possible compatibility defect and rigorously explains why affine
projection alone is insufficient. Tests of the revised continuation
must still measure true PDE residuals, amplitude, basin changes, tail
and inverse errors, and possible loss of nontriviality.

Dependencies: the B2 center jet, a bounded linear strain functional,
explicitly assumed Banach C1 transport map, Banach IFT, and elementary
kernel homogeneity. No production solver code was reused or run.

## A finite-dimensional counterexample to the kernel-to-count inference

Let E=R^2, ell(x,y)=x, c>0, H={(c,y):y>0}, e=(c,1), and
S(c,y)=(c/y,1). This map is smooth. In q=a S((1-epsilon)e+epsilon q),
write q=(c,y), a>0. The two scalar equations are

    y=a,  c=ac/[(1-epsilon)+epsilon y].

The denominator is positive, so these equations are equivalent to

    y=a,  (1-epsilon)(y-1)=0.

Thus for 0<=epsilon<1 there is exactly one solution q=e,a=1; at
epsilon1 all q=(c,y),a=y solve. Define the linear map
R_lambda(x,y)=(x,lambda y), lambda>0. Direct substitution gives
S(R_lambda q)=lambda^{-1}R_lambda S(q). Consequently the endpoint
equation has the scaling symmetry (q,a)->(R_lambda q,lambda a),
and differentiating yields a nonzero kernel direction. Nevertheless
the amplitude-one branch persists through the endpoint. One may
append a parameter beta on which S does not depend; normalized solutions
then exist for every beta. The kernel alone says nothing about a
cokernel or discrete beta. This is an exact counterexample to that
abstract inference, not a counterexample or solution of the B2 PDE.
A specifically declared discretization may have an independent count;
that would require its own analysis, absent from the challenged claim.

The actual Opus33 call returned no audit text (stop reason refusal),
so it supplies no endorsement. This algebra was derived and checked
independently. The follow-up Opus34 also returned no audit text (stop
reason refusal, actual claude-opus-5-5,7.980720s); it is not an endorsement.
