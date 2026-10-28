# Stronger finite-cost comparison between Holder exponents

## Statement and hypotheses

Let mu be a finite real signed measure of total mass zero on a compact
metric space of diameter at most d, where d>=1. Its positive and negative
Jordan measures have the same mass M. For 0<t<1 define

    W_t(mu) = inf_pi integral distance(x,y)^t d pi(x,y),

where pi ranges over couplings of the Jordan measures. For M=0 set W_t=0.
For 0<a<b<1 and any m>=M>0,

    d^(a-b) W_b <= W_a <= m^(1-a/b) W_b^(a/b),             (1)
    m^(1-b/a) W_a^(b/a) <= W_b <= d^(b-a) W_a.             (2)

These are finite transport-cost comparisons. They do not identify
optimal couplings for different exponents.

Here is their application to the real whole-plane norms C_alpha and
D_alpha=||R_1^2|| of ../../../01_setup/PROOF.md. Fix

    0<a<alpha0<b<1, 0<epsilon<1/2, R>1,

and let E be any upper bound for Ebar in ../PROOF.md on [a,b]. Let

    m_C = (2/pi) log((R+1/2)/epsilon), m_D=m_C+1/2, d=2R.

Suppose C_alpha0<=U and D_alpha0>=V with V>E. Set

    U0=U+E, V0=V-E,
    H_C=max(log d, log(m_C/U0)/alpha0, 0),
    H_D=max(log d, log(m_D/V0)/alpha0, 0).

An upper bound may replace m_C in H_C and m_D in H_D. If rho>0 and
[alpha0-rho,alpha0+rho] is contained in [a,b], then throughout this closed
interval

    C_alpha <= E+U0 exp(H_C rho),
    D_alpha >= -E+V0 exp(-H_D rho),
    D_alpha-C_alpha >= V0 exp(-H_D rho)-U0 exp(H_C rho)-2E. (3)

In particular a strictly positive right side in (3) certifies strict
separation on the entire interval. Unlike the direct uniform Lipschitz
cost bound, these estimates do not contain a factor d^b multiplying rho.
No claim that the resulting interval is maximal is made.

## Proof of the finite transport comparisons

For every pair at distance r in [0,d], r^b<=d^(b-a) r^a.
Integrate against any coupling, then take the infimum. This proves the
right inequality of (2), equivalently the left one of (1).

For any coupling pi, pi/M is a probability measure. Concavity of
s->s^(a/b) on [0,infinity) gives Jensen's inequality

    integral r^a d pi
       <= M^(1-a/b) (integral r^b d pi)^(a/b).

Take a sequence of couplings whose b-cost tends to W_b. Since W_a is
at most the a-cost of each such coupling, continuity of the nonnegative
power proves the upper inequality in (1) with M. Replacing M by m can
only increase its right side. Rearranging that upper inequality gives
the lower inequality of (2) with M; the exponent 1-b/a is negative, so
replacing M by its upper bound m can only decrease this lower bound.
Zero costs are included by continuity. When M=0 all costs are zero and
the applicable unrearranged inequalities are immediate.

## Transfer to operator norms

The fixed measures mu_phi and mu_phi^D in ../PROOF.md have support in
the disk of radius R. Their Jordan masses are bounded by m_C and m_D,
respectively. Write their phase-supremum costs as C^tr_alpha and
D^tr_alpha. The already accepted truncation theorem gives

    |C_alpha-C^tr_alpha|<=E, |D_alpha-D^tr_alpha|<=E

uniformly on [a,b]. In particular C^tr_alpha0<=U0 and
D^tr_alpha0>=V0>0.

For alpha>=alpha0 put s=alpha-alpha0. Inequality (2), phase by phase,
gives

    C^tr_alpha <= d^s U0,
    D^tr_alpha >= m_D^(-s/alpha0) V0^(1+s/alpha0).

For the second statement choose phases approaching the supremum at
alpha0, apply (2), and pass to the limit. A maximizing phase need not
exist. The expression is increasing in its positive cost argument.

For alpha<=alpha0 put s=alpha0-alpha. Inequality (1) instead gives

    C^tr_alpha <= m_C^(s/alpha0) U0^(1-s/alpha0),
    D^tr_alpha >= d^(-s) V0.

The same supremum argument justifies the lower statement. Thus for
both signs and 0<=s<=rho,

    C^tr_alpha <= U0 exp(H_C rho),
    D^tr_alpha >= V0 exp(-H_D rho).

Adding the two adverse truncation errors proves (3). Every constant
used is finite, and the lemma uses only finite measures. Infinite
variation of the untruncated singular kernel is never treated as a
finite Jordan mass.

## Dependencies and verification status

The only operator dependency is the accepted truncation and mass
bound in ../PROOF.md, which in turn uses ../../PROOF.md. The new step is
the elementary finite-measure Jensen comparison proved here. Numerical
applications require directed enclosures of E, H_C and H_D and a positive
lower endpoint for (3). They must record exact U,V,cutoffs and radius.
Status at creation: OPEN pending independent lead cross-read.
