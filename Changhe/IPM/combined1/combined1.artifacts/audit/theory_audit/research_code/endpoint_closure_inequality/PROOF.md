# Moment budget and the reach of the endpoint closure inequality

## Statement and hypotheses

This independently audits R2 and R3 of T2 the review of T4-335. Let c>1,
gamma=1/c, delta=1-gamma, q=gamma-4, and use all hypotheses (5) of
../moment_resolved_tail/PROOF.md: a real C1 S1 reference R with its
specified canonical velocity, angular data A and Theta, positive
epsilon,eta, finite nonnegative V,G,E_F,E_R, and R0>=2. All growth,
residual and differentiated profile bounds there hold for r>=R0.
Put P=gamma cos(2theta)Theta+sin(2theta)Theta' and
B=dist_L2(circle)(A,span_R P)/(4c). Assume B>0. Arc length is dtheta.
For a real S1 C1 function h define

    H_q(h)=max(sup_X (1+|X|)^(-q)|h|,
                 sup_X (1+|X|)^(1-q)|grad h|).

Suppose H_q(h)<=H<infinity, ||h||2<=beta and R+h is stationary at
this same c, with velocity U_R+U[h]. Let E=E_q be the proved constant
in the neighboring theorem, D_x=1-c(q-x), and

    mu=8/[(-q-1)(-q-2)(-q-3)].

Then H>=B/sqrt(2pi), the absolutely convergent moment m=integral y h
satisfies |m|<=mu H, and for every R1>=R0 one necessarily has

    beta^2 >= integral_(R1)^infinity r^(2q+1)
                         [B-sqrt(2pi) ehat(r;H)]_+^2 dr,       (CI)

where [z]_+=max(z,0) and

    ehat = E_F r^(-epsilon)/D_epsilon
         + mu H E_R r^(-eta)/(pi D_eta)
         + H(V+E G) r^(-delta)/D_delta
         + mu H^2 r^(-4)/(pi D_4)
         + E H^2 r^(q-1)/D_(1-q).

If G>0, define r_sep=(E G/D_delta)^(1/delta). The square root of
(CI)'s right side, for every admissible H and R1, is at most

    beta_cap=B r_sep^(q+1)/sqrt(-2q-2).                        (1)

This is an upper bound on what this particular necessary test can
certify. It is not an upper bound on a correction or on the distance
to a stationary solution. The theorem retains the hypotheses (5).

## Proof

S1 and the density bound give absolute moment convergence. In polar
coordinates,

    |m| <= H integral_0^(2pi)|sin theta| dtheta
                integral_0^infinity r^2(1+r)^q dr
         =4H B(3,-q-3)=mu H.

Here -4<q<-3, so the Beta integral converges at both ends. Evaluating
it by two integrations by parts gives the displayed rational mu.
Replacing |m| by mu H in the already audited endpoint error estimate
(7) proves |e(r,theta)|<=r^q ehat(r;H). Its leading angular profile
is (A+(m/pi)P)/(4c), whose circle L2 norm is at least B for every
real m. Uniform convergence of r^(-q)h to this profile implies

    H_q(h)>=||[A+(m/pi)P]/(4c)||infinity>=B/sqrt(2pi).

The first inequality follows directly from (1+r)^(-q)>=r^(-q).
Taking the L2(circle) triangle inequality at each r>=R0, retaining
a nonnegative lower bound, and integrating with the polar measure
r dr proves (CI). Every integral is finite because q<-1 and its
integrand is bounded by B^2 r^(2q+1).

All five terms of ehat are nonnegative. Since H>=B/sqrt(2pi),

    sqrt(2pi) ehat(r;H)>=B E G r^(-delta)/D_delta.

Consequently the positive part in (CI) is zero for r<=r_sep. Beyond
that radius it is at most B. Enlarging its integration domain to
(r_sep,infinity) gives

    RHS(CI)<=B^2 integral_(r_sep)^infinity r^(2q+1)dr
            =B^2 r_sep^(2q+2)/(-2q-2),

which proves (1). If R0 or the other errors force a larger starting
radius, the upper bound only decreases. For larger H, the support
threshold is at least (sqrt(2pi)H/B)^(1/delta) r_sep. Without any
upper H budget this tends to infinity, and the same upper bound on
the test tends to zero. A pure L2 budget therefore supplies no
positive exclusion from this family by itself.

## Exact campaign specialization

Use c=4076476460239181/2251799813685248 and the exact angular data
of007,013,014 in data/. These are the pairs for any reference that
preserves their stated leading profile and endpoint residual, and
also satisfies all hypotheses (5). The original references have
additional slower residual sectors; this section does not claim
they satisfy (5). The independently reviewed three-cutoff application
has its own acceptance status.

The finite rational and directed interval checker must verify

    mu<504423/100000, E>133,
    B<85020, B/sqrt(2pi)>33917,
    Theta'(0)>285227/10000.

The last inequality bounds G from below without a maximization.
Indeed divide the gradient expansion in (5) by r^(gamma-1), set
theta=0 and let r tend to infinity. S1 implies Theta(0)=0, so
G>=|Theta'(0)|. The exact leading profile is the same in all three
inputs. Thus r_sep exceeds

    r_low=(133*(285227/10000)/D_delta)^(1/delta).

Since q+1<0, (1) is strictly less than

    85020 r_low^(q+1)/sqrt(-2q-2).

The checker encloses this expression with Arb and tests the rational
upper bound 928/10^13. Acceptance requires that strict comparison.
This makes the stated limitation rigorous without using the peer's
FLOAT angular grid or its FLOAT radius. The artificial E=10,1,1/2
rows remain hypothetical and are not asserted as valid velocity
constants. This audit provides no PDE inverse or existence result.

## Dependencies and evidence

The analytic dependency is the complete moment-resolved theorem335,
now AUDITED through350, including its domain addendum. The finite
angular data and their exact projection were independently confirmed
there. This checker reconstructs the projection again from exact
JSON and evaluates only the new constants. Its inputs, proof, source
review, results and actual completion time are hashed. No publisher
or other-lane code is executed.
