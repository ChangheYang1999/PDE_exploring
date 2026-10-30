# A uniform tail bound for the first-mode separated weak test

## Exact reference, notation and scope

Fix the exact candidate007 and c=4076476460239181/2251799813685248,
delta=1-1/c. Its canonical potential, density rho, divergence-free velocity
u and full residual F=(cX+u).grad rho-rho are those in
../far_pairing_audit/PROOF.md. The canonical source has SHA256
153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316.
Put t=r^2/(1+r^2), v=1-t and, for integers K>=0,

    phi_K=r v^2 t^K sin(theta), I_K=int_(R^2) F phi_K,
    A_K=||(2c+1)phi_K+cX.grad phi_K||_2.

Consider the separated weak-distance quantity

    m_K=2|I_K|/[D_K+sqrt(D_K^2+4H_K|I_K|)],              (1)

where D_K>=A_K and H_K>=0. This includes N1's full separated denominator
A_K+Benv_K+Cenv_K when those nonnegative norms are exact. No assumption
that its floating extrapolations are containing intervals is made. It
does not include every combined M_K+C_K denominator, since the norm of
a sum can be less than A_K. The result is an upper bound for the value
of this specified necessary test, not an upper bound on the distance to
a solution. It does not locate a maximizer or exclude other probes.

The complete first-sine projection has the exact finite form

    Pi_1 F=r sum_ell v^(ell delta/2) P_ell(t) sin(theta).

Write Q_ell(v)=P_ell(1-v)=sum_j q_ell,j v^j and
beta_ell,j=ell delta/2+j. For every nonzero q_ell,j this computation must
verify beta_ell,j>4/3 exactly. This hypothesis is checked coefficientwise;
being true of a displayed finite far-field table alone is insufficient.
For an integer K0>=0 define the positive finite sum

    U(K0)=sqrt(pi/2)/(c+1) (2K0+3)
           sum_(ell,j) |q_ell,j| B(beta_ell,j,K0+2).      (2)

Then, for every integer K>=K0 and every D_K,H_K as above,

    0<=m_K<=U(K0).                                      (3)

Every source coefficient is read from the shared exact projection
interface. Numerical claims about (2) use outward Arb intervals and
strict rational upper bounds, recorded in JSON. Until independently
reviewed these new numerical upper bounds remain OPEN.

## Whole-plane pairing and a coercive elementary denominator

The previously independently audited projection identity and polar
integration give the exact finite formula

    I_K=(pi/2) sum_(ell,j) q_ell,j B(beta_ell,j,K+2).

All parameters are positive, so the sum of absolute coefficients gives
an upper bound for |I_K|. There is no omitted expansion remainder and
no artificial continuation of a homogeneous model through the origin.

The probe is smooth at zero and decays as r^-3 at infinity. Its squared
norm and the scalar product with its drift expression are

    ||phi_K||_2^2=pi/[2(2K+2)(2K+3)],
    <phi_K,(2c+1)phi_K+cX.grad phi_K>
                         =(c+1)||phi_K||_2^2.

The first formula follows by angular integration and the Beta integral.
For the second, integrate X.grad(phi_K^2)/2 and use div X=2. Both
boundary terms vanish by the stated origin and infinity behavior.
Cauchy-Schwarz and c+1>0 therefore imply

    A_K >= (c+1)||phi_K||_2
         > (c+1)sqrt(pi/2)/(2K+3).

Since the denominator in (1) is at least2D_K>=2A_K,

    m_K <= |I_K|/A_K
        <= sqrt(pi/2)/(c+1) (2K+3)
               sum |q_ell,j| B(beta_ell,j,K+2)=U(K).

The strict denominator comparison is not used to manufacture a strict
numerical result; each reported rational ceiling is independently
checked to exceed the containing interval for U(K0).

## Uniformity over the unbounded integer set

For each beta>4/3 and K>=0, the positive Gamma recurrence gives

  [(2K+5)B(beta,K+3)]/[(2K+3)B(beta,K+2)]
       =[(2K+5)(K+2)]/[(2K+3)(K+2+beta)] < 1.

Indeed this inequality is equivalent to
(2K+3)(beta-1)>1, which follows from beta>4/3. Every summand in (2)
is positive and decreases at every integer step. The finite sum therefore
satisfies U(K)<=U(K0) for every integer K>=K0, proving (3). This argument
has no sampled tail or untested interval between indices.

The existence of a numerical ceiling below a specified incumbent proves
only that this separated test family cannot beat that incumbent for
K>=K0. It does not prove that the incumbent is attained or that all
smaller integer indices were tested. In particular a maximum over a
finite logarithmic mesh must still be labelled as a sampled maximum.

## Independent checks and dependencies

Check exact composition Q(1-t)=P(t), every nonzero exponent, canonical
and projection hashes, and the prior full residual assembly binding.
At each reported K0, evaluate the signed sum and require agreement with
the independently confirmed N4-209/221 whole-plane pairing when present.
Evaluate (2) by both the direct positive Beta sum and its recurrence,
require more than150relative bits, and test a simple rational ceiling.
Store a separate monotonicity flag and the exact minimum beta.

No own or foreign optimizer is executed. The core dependence is the
independently confirmed complete residual projection, not the finite
asymptotic model. This proof is written before implementing the check.
