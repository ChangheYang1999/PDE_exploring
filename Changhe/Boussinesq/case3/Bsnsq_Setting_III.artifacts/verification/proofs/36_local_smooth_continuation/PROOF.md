# Local propagation of all spatial derivatives and uniform polar corrections

Date:2026-10-20. Status: CONFIRMED by the independent verifier.
External-review availability is recorded in verification/audit.json.
No nonexistence or existence endpoint is claimed.

## 1. Local regularity lemma

Let D be an open subset of R2. On D times[t0,0), suppose u,omega,theta are
smooth and solve

    omega_t+u.grad omega=theta_x, theta_t+u.grad theta=0,
    div u=0, partial_2 u1-partial_1 u2=omega.              (1)

Assume that on each compact subset of D, uniformly as t approaches0,

    |u|, |Du|, |theta|, |grad theta| and |omega|
                       are uniformly bounded.           (2)

and that u,omega,theta converge locally uniformly at t=0 to u0,omega0,theta0.
Then all three limits are smooth on D and the convergence holds in every
C^j norm on every compact subset, for each finite integer j>=0.
In particular every spatial derivative remains locally bounded up to0.
No global norms or boundary values on partial D are assumed.

The external functional-analytic input is the whole-plane Lq div-curl
estimate for compactly supported smooth vector fields F:

    ||D^k F||_Lq <= C_{k,q}(||D^{k-1}div F||_Lq
                      +||D^{k-1}(partial_2 F1-partial_1 F2)||_Lq),   (3)

for integers k>=1 and 1<q<infinity. It follows by the Fourier div-curl
identity and the classical Lq boundedness of the second-order Riesz
transforms. We use it only after compactly supporting F within D.
Local Sobolev embedding, Hölder, Young and Gronwall inequalities are also
used. These standard analytic tools are the dependencies of the lemma.

## 2. Inductive objective and shrinking cutoff

We prove by induction on k>=1 that on compact subsets, uniformly up to0,

    u,theta bounded in W^{k,p}, omega in W^{k-1,p}
                           for every finite p>2.        (4)

The case k=1 follows from(2) on compact sets, with omega in Lp.
Suppose(4) holds at k-1, with k>=2, and fix q>2.
The induction hypothesis holds for every finite p, including2q. This is
needed for the intermediate derivative products below.

Fix z0 in D and a ball B(z0,R) with closure in D. All norms of previously
controlled derivatives on this ball are bounded. In particular choose M
larger than a uniform bound on |u| there. Restrict to a sufficiently late
interval [t1,0), with t1<0, so that M|t1|<R/8. Choose a smooth decreasing
function eta of one real variable with 0<=eta<=1, eta=1 for r<=R/2 and
eta=0 for r>=3R/4. Define

    chi(t,z)=eta(|z-z0|+M(t-t1)).                         (5)

This is smooth, including at z0 since it is constant near the center.
It is supported in B(z0,3R/4), equals1 on B(z0,3R/8) through t=0, and
all spatial derivatives needed at this induction step are uniformly
bounded. Wherever its gradient is nonzero,

    (partial_t+u.grad)chi
       =eta'(|z-z0|+M(t-t1))[M+u.(z-z0)/|z-z0|] <=0.    (6)

Thus the cutoff contributes a favorable nonpositive term to transport
energies. No uncontrolled factor grad chi/chi needs to be divided out.
The initial time t1 is before the endpoint, so every required high-order
norm on the compact support is finite at t1.

## 3. A weighted elliptic estimate with only lower-order errors

Apply(3) to F=chi u extended by zero outside D. Product differentiation
and(1) give

    div(chi u)=grad chi.u,
    partial_2(chi u1)-partial_1(chi u2)
       =chi omega+(partial_2 chi)u1-(partial_1 chi)u2.

Every term in D^k(chi u)-chi D^k u contains at most k-1 derivatives of u.
In D^{k-1}(chi omega), only chi D^{k-1}omega is not a previously bounded
quantity; every other term has at most k-2 derivatives of omega.
All derivatives of grad chi.u have at most k-1 derivatives of u.
Consequently, with constants uniform on [t1,0),

    ||chi D^k u||_Lq <= C ||chi D^{k-1}omega||_Lq+C0.     (7)

The constant C0 depends on the already controlled local W^{k-1,q}
norm of u and W^{k-2,q} norm of omega, and derivatives of chi.
Crucially, the leading vorticity term has exactly the same cutoff chi
as the left side. Thus no larger-domain high-order norm is required
at the current induction step. Lower-order norms are available on the
fixed larger ball from the previous step.

## 4. Coupled transport energies

Set A=D^{k-1}omega and B=D^k theta, understood as the finite arrays of
all indicated partial derivatives. Differentiating(1) gives

    (partial_t+u.grad)A=D^{k-1}theta_x
                                  -[D^{k-1},u.grad]omega,
    (partial_t+u.grad)B=-[D^k,u.grad]theta.               (8)

In the first commutator the terms with one derivative on u are bounded
by C||Du||_infinity |A|. For terms with j>=2 derivatives on u, the factors
have orders j<=k-1 on u and k-j<=k-2 on omega. Both are controlled in
L^{2q} by the induction hypothesis, so their product is bounded in Lq.
The source D^{k-1}theta_x is a component of B.

In the second commutator, the terms with one derivative on u are
bounded by C||Du||_infinity |B|. The terms with all k derivatives on u
are bounded by C|D^k u| ||grad theta||_infinity. For each intermediate
2<=j<=k-1, the factors have j<=k-1 derivatives on u and k+1-j<=k-1
on theta; Hölder with L^{2q} bounds their product in Lq. The needed
Du and grad theta sup norms are part of(2), uniformly on the support
of chi. At the first induction step k=2, both intermediate sums are
empty: the vorticity commutator is Du times Domega, and the temperature
commutator contains only Du times D2theta and D2u times grad theta.
Thus the weighted elliptic estimate closes that base step directly.
The L2q product argument is first needed at k=3.

Multiply the component equations by chi^q |A|^{q-2}A and
chi^q |B|^{q-2}B, sum, and integrate over the plane. Compact support
and div u=0 remove the flux at infinity. By(6), differentiating the
weight has nonpositive contribution. With

    E(t)=||chi A||_Lq^q+||chi B||_Lq^q,

Hölder and Young give

    E'(t) <= C E(t)+C
       +C ||chi D^k u||_Lq ||chi B||_Lq^{q-1}
       <= C' E(t)+C',                                   (9)

where the last step is(7) and Young's inequality. All constants are
finite and independent of t in[t1,0). The lower-order products carry
chi on both sides of the energy pairing; their weighted Lq norm is
bounded by their unweighted local Lq norm, since0<=chi<=1.
For noninteger q the displayed energy derivative is justified by
regularizing |A|^q and |B|^q at zero and taking the regularization to
zero. No regularization of the PDE or endpoint is needed.

Gronwall bounds E through0. Since chi=1 on B(z0,3R/8), this proves the
new omega W^{k-1,q} and theta W^{k,q} bounds there. Equation(7), with
local lower-order bounds, gives u W^{k,q} there as well. Arbitrary
compact sets are covered by finitely many such smaller balls.
Since q>2 was arbitrary, the induction closes for every finite p>2.

## 5. Smooth limits and convergence

For any compact K inside D choose a slightly larger compact set and
apply(4) for arbitrarily high k. Sobolev embedding gives uniform bounds
in every C^{j+1} norm on K. Along any sequence t_n approaching0,
Arzela-Ascoli on a slightly larger compact set gives a subsequence
converging in C^j(K). Its uniform limit is the already specified
u0,omega0,theta0, so the derivative limits are their derivatives.
This proves that the limits are C^j and that the full sequence, hence
the full time limit, converges in C^j. Since j is arbitrary, the
limits are smooth and all local spatial derivatives converge.

This is spatial smoothness through the endpoint. The argument does
not bound or assert any time derivative of u.

## 6. Application to exact class A B2 profiles

The confirmed class A estimates of33 give

    V=O(r^(1-s)), DV=O(r^-s), Omega=O(r^-s),
    Theta=O(r^(1-2s)), grad Theta=O(r^-2s), s=1/beta.

The uniform angular limits for Omega and Theta are provided by33
and14; the canonical inverse gives local uniform convergence of
velocity by dominated convergence, as explicitly proved in35 section3.
For the physical fields

    u_tau(z)=tau^(beta-1)V(tau^-beta z),
    omega_tau(z)=tau^-1 Omega(tau^-beta z),
    theta_tau(z)=tau^(beta-2)Theta(tau^-beta z),

the displayed estimates give(2) directly on each compact annulus:
Du_tau=tau^-1 DV(tau^-beta z) and
grad theta_tau=tau^-2 grad Theta(tau^-beta z) are uniformly bounded.
The other fields are uniformly bounded there by the same scaling.
Their exact physical transport and div-curl equations hold
on D=R2 minus{0}, beta>=2. Therefore the local lemma applies without any external local
continuation theorem. Its
limits u0,omega0,theta0 are the homogeneous functions defined in35.
Consequently their angular coefficients a,h are C-infinity, and

    u_tau->u0, omega_tau->omega0, theta_tau->theta0

in every spatial C^j norm on every compact annulus.
The exact equations in tau read

    partial_tau omega_tau=u_tau.grad omega_tau-partial_x theta_tau,
    partial_tau theta_tau=u_tau.grad theta_tau.

Their right sides converge in every C^j norm, because spatial
convergence is available at j+1. Integration from0 to tau, first
integrating from epsilon>0 and then taking epsilon->0, gives

    omega_tau=omega0+tau omega1+o_{C^j}(tau),
    theta_tau=theta0+tau theta1+o_{C^j}(tau),
    omega1=u0.grad omega0-partial_x theta0,
    theta1=u0.grad theta0.                              (10)

Restricting to the unit circle and using tau=r^-s, s=1/beta,
m=1-2s, proves for every finite angular derivative order j

    Omega(r e)=r^-s a+r^-2s b+o_{C^j(S1)}(r^-2s),
    Theta(r e)=r^m h+r^(m-s)d+o_{C^j(S1)}(r^(m-s)),       (11)

where b=omega1|S1 and d=theta1|S1 are exactly the coefficients in35.
Thus the vorticity correction is now uniform, with all fixed angular
derivatives. All source and velocity far-field derivative bounds
also follow from the annular scaling, for each integer j>=0:

    |D^j Omega(X)|<=C_j r^(-s-j),
    |D^j Theta(X)|<=C_j r^(m-j),
    |D^j V(X)|<=C_j r^(1-s-j).                          (12)

Each estimate concerns r sufficiently large. The smooth profiles
remain unconstrained by such estimates on the limiting point z=0
in physical coordinates. No finite-energy or bounded-data blowup
claim is implied. A velocity second term or an all-orders time
expansion requires additional inverse analysis and is not asserted.

## 7. Audit record

The verifier checked the k=2 starting case and the k=3 case explicitly: D^2u times Dtheta or
Domega, and D^2u times D^2theta, are controlled by the prior local
L^{2q} norms. The same-cutoff highest-order elliptic estimate eliminates
the usual loss to an uncontrolled larger-domain high-order norm.
Every induction stage may shorten the late time interval, which is
permitted for each fixed derivative order. This proves spatial, not
uniform-in-order or analytic, regularity. Two direct Opus5.5 requests
returned stop_reason=refusal with no written audit; they supply no
endorsement. The preceding local W2q and Lq second-term argument35 did
receive an actual written Opus5.5 audit, independently checked against
the primary theorem. Lead review of the new local lemma remains welcome
through the shared files and is not presumed completed.

The final proof strengthens the original local lemma: the original
W2p starting hypothesis is replaced by the direct first-derivative
sup bounds(2), and the same energy argument starts at k=2. These
bounds are already consequences of33 after physical scaling, so the
Chae-Wolf theorem is no longer a dependency of this result. The exact
primary theorem audit in35 remains valid as a separate route to its
weaker W1q angular conclusion. Neither unavailable external request
24 nor25 reviewed this final simplified starting step.

Actual Opus27 returned a written audit of the final k=2 starting step on 2026-10-20 at16:29:09Z (claude-opus-5-5,46.644273s). It found no substantive gap and identified the finite-q range, uniform cutoff derivatives, nonnegative transport weight and finite initial high-order norms, all explicitly present above. Its unrelated 3D aside is not used. The verifier checked the response; requests24/25 remain recorded as unavailable audits.
