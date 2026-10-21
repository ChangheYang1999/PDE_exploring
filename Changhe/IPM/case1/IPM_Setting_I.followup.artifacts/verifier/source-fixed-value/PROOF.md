# A fixed source value restores a critical estimate for source perturbations

Date: 2026-10-20. Status: complete informal proof, independent review pending. This is a conditional estimate for compatible axis functions.

## Statement and hypotheses

Fix A>2, beta=2/A, L>0, and a smooth compatible pair w_0,g_0 satisfying

    w_0 g_0'=(w_0'-A)g_0,  g_0/x^2 -> 1 at zero,
    w_0'(0)=-A,  w_0'(L)=A,
    w_0<0 on (0,L),  g_0>0 on (0,L],
    w_0(0)=w_0(L)=0,  g_0(L)=g_*=2A-2.

Assume w_0 is odd analytic near zero and g_0 is smooth up to L. Use the finite part B and the definitions Q,m,W in ../source-exception/PROOF.md, equation (1), in the physical x coordinate. Choose sufficiently small fixed d_0>0 with d_0<min(1,L/2).

Let v be any smooth function compactly supported in (L-d_0,L). Rebuild the positive normalized g_v from w_v=w_0+v, and suppose

    g_v(L)=g_* exactly.                                      (1)

For delta=L-x put

    epsilon(v)=max_(i=0,1,2) sup_(0<delta<d_0)
                      delta^(i-3+beta)|v^(i)(L-delta)|.

There are constants epsilon_0,C>0, depending only on the fixed base and d_0, such that

    epsilon(v)<=epsilon_0  implies
    |B[w_0+v]-B[w_0]|<=C epsilon(v).                         (2)

In particular this is an estimate by C||v||_(C^(2,1-beta)[0,L]) under the same support and exact source-value constraint. It is a bound relative to this fixed base, not a claim of a Lipschitz map between arbitrary pairs in a larger class. No estimate with an approximate version of (1) is asserted.

## Uniform normalization and the source condition

Write w=w_0, g=g_0 and eta=log(g_v/g). Since |w| is comparable to delta on the source segment, |v/w|<=C epsilon delta^(2-beta), so small epsilon preserves negativity. Normalization of the first equation gives exactly

    eta=log(1+v/w)-A integral_0^x [1/(w+v)-1/w] du.

Condition (1) means eta(L)=0. Subtracting the formula at L therefore gives the useful endpoint-normalized identity

    eta=log(1+v/w)+A integral_x^L [1/(w+v)-1/w] du.           (3)

The integrand has modulus at most C epsilon delta^(1-beta), which is integrable. Consequently, throughout the source segment,

    |eta|<=C epsilon delta^(2-beta),
    eta'= -v'/(A delta)+O(epsilon delta^(2-beta))
                            +O(epsilon^2 delta^(3-2beta)).   (4)

For the derivative, use the exact relation

    eta'=v'/(w+v)+(A-w')v/[w(w+v)],

together with w=-A delta+O(delta^2), w'=A+O(delta). No third derivative of v is needed. Constants are independent of the position, number and length of the support components.

Before the support, eta=0 by center normalization. After the support, eta=0 by (1). Thus the perturbed density is the original density near both endpoints. In particular Q_v(L)=Q_0(L), with no source-constant subtraction error.

## Integrable remainder after the critical cancellation

Let G=g'/(2g^3), V=-w''/(2g^3). Exact algebra gives

    Q_v=e^(-2eta)G+e^(-3eta)V
           +e^(-2eta)eta'/(2g^2)-e^(-3eta)v''/(2g^3),
    W_v/W_0=(1+v/w)^(beta-2)e^(-(beta-1)eta),
    W_0=A^(beta-2)g_*^(1-beta)delta^(beta-2)(1+O(delta)).

It follows that

    (Q_v-Q_0(L))W_v-(Q_0-Q_0(L))W_0
      =-A^(beta-2)/(2g_*^(beta+2))
           [v''+(g_*/A)v'/delta]delta^(beta-2)+E(delta),
    |E(delta)|<=C epsilon+C epsilon^2 delta^(1-beta).         (5)

Here is the error accounting. The changes in the smooth G and V terms are O(epsilon delta^(2-beta)), which become O(epsilon) after multiplication by W_0. The errors in eta' in (4) become O(epsilon)+O(epsilon^2 delta^(1-beta)). Replacing g(x) and W_0 by their leading source values in the displayed v terms introduces a relative O(delta) and hence O(epsilon). The relative change of W is O(epsilon delta^(2-beta)); multiplied by the v terms, it is O(epsilon^2 delta^(1-beta)), and multiplied by Q_0-Q_0(L)=O(delta) it is O(epsilon delta). These are bounded by the right side of (5) for d_0<1. There is no change of a constant density multiplier at L: it equals one exactly by (1). In particular the nonintegrable epsilon^2/delta error present without that constraint is absent.

Both terms in the error bound of (5) are integrable, uniformly over v. The integrand difference vanishes before the source segment, including a full neighborhood of zero. The difference of finite parts is thus an ordinary integral with no remaining center term. Multiplying (5) by (beta-1)A^(1-beta)/3 yields

    B[w+v]-B[w]
      =(1-beta)/(6A g_*^(beta+2))
         integral_0^d_0 [d_delta^2 v-(g_*/A)d_delta v/delta]
                              delta^(beta-2)d_delta
                      +O(epsilon+epsilon^2).                 (6)

The leading integral is exactly

    (3-beta)(2-beta-g_*/A)
                   integral_0^d_0 v delta^(beta-4)d_delta.

Two integrations by parts for the second derivative and one for the first derivative prove this identity. For each individual v all integrals are ordinary and all boundary terms vanish, since v is compactly supported in the open source segment. At g_*=2A-2 and beta=2/A, its prefactor is zero. Therefore (6) proves (2) after reducing epsilon_0 if necessary.

## Relation to the ordinary critical Holder norm

Let alpha=1-beta. Since v and v' and v'' vanish near L, the Holder seminorm of v'' gives

    |v''(L-delta)|<=||v||_(C^(2,alpha)) delta^alpha.

Integration from L gives the bounds for v' and v with powers delta^(1+alpha) and delta^(2+alpha). These prove epsilon(v)<=C||v||_(C^(2,alpha)), so (2) implies the asserted ordinary-norm estimate. This direction uses no uniform higher derivative bound.

The constraint (1) is nonvacuous. For two nonnegative nonzero smooth functions h_1,h_2 with disjoint compact supports in the source segment, define

    F(t,a)=integral_0^L [1/(w+t h_1+a h_2)-1/w]dx.

It is smooth near (0,0), F(0,0)=0, and partial_a F(0,0)=-integral h_2/w^2<0. The scalar implicit function theorem gives a smooth a(t) with a(0)=0 and F(t,a(t))=0. Formula (3) before imposing its endpoint value shows that v=t h_1+a(t)h_2 then satisfies (1). These perturbations are nonzero for t!=0 because the supports are disjoint, and their critical norms tend to zero.

## Dependencies and scope

The proof uses the normalized axis ODE, the finite-part identity with its explicit endpoint convention, the displayed source expansions, ordinary integrations by parts and a scalar implicit function theorem only for the nonvacuity example. It does not depend on numerical quadrature or a PDE implicit function theorem.

This estimate explains why the exceptional construction in ../source-exception/PROOF.md changes g(L): imposing (1) exactly cancels its leading source mechanism. The estimate concerns source-supported perturbations at one exceptional base. It makes no claim about arbitrary interior or origin perturbations, the full fixed-g(L) manifold, coupled two-dimensional profiles, or either strong-setting endpoint.
