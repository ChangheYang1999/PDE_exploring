# Negative transverse growth on a regular Bernoulli support

Status: independent reconstruction of LIT104, with the focused configured-model review incorporated. The nonzero-velocity hypothesis is kept explicit in Sections1-6 and holds automatically by A464. The geometric lemma and its exact Euler consequences are the subjects of A465-A467.

## 1. Euler theorem at the stated conditional scope

Let 0<c<1/2, omega in R, U in C2(R3;R3) and P in C1 solve the full incompressible rotating Euler profile equation. Assume uniform U=o(|y|) and global U.curl U=0. Define

    A=cI-omega J, B=Ay+U, W=curl U,
    a=1-2c, kappa=1+c, d=3c, D=d+kappa=1+4c,
    H=P+|U|^2/2+(Ay).U, g=U.B.

Suppose mu is a compactly supported, whole-flow-invariant and whole-flow-ergodic probability satisfying

    B!=0, W=0, DW!=0, D(B cross W)=0  mu-almost everywhere.

If U is nowhere zero on S=supp mu, no such measure exists. Carrier equilibria in S are allowed as zero-mass support points. No nonflatness at those equilibria is imposed.

The dependencies A444-A445 give, everywhere on S,

    W=0, g=0, H=h, grad H=-aU,
    grad g=-kappa U, d(BH)=-kappa dH.                  (1)

A449 excludes a nonstationary periodic carrier orbit having these negative-covector data and the stated nonflat vorticity first jet. Sections2-6 prove that the measure must be such a periodic measure. The proof uses neither compactification of a regular surface nor an external singular-flow theorem.

## 2. Projection and exact surface Jacobian

Compactness and U!=0 on S give a positive lower bound for |grad H| there. Choose a relatively compact neighborhood V with grad H nonzero. The level M={H=h} intersect V is a C2 embedded surface, possibly disconnected and noncompact. Set

    Btilde=B-(BH)grad H/|grad H|^2, X=-Btilde.          (2)

The field X is C1 and tangent to M. Since BH=0 on S, it agrees there with -B. The original complete backward carrier trajectories through S solve its equation and stay in S, so uniqueness identifies the two flows on S for all times.

For v in ker dH(x), x in S, differentiating (2) gives

    D Btilde(x)v=DB(x)v,                              (3)

because BH=0 and d(BH)(v)=-kappa dH(v)=0. This implies equality of tangent derivative cocycles, not just their generators: the projected derivative remains tangent to M because H is its first integral, and (3) makes it solve the same linear variational equation as the original derivative with the same initial data.

Write Psi for the original backward flow. Pulling back dH along an orbit in S, (1) gives

    D Psi_t(x)^T grad H(Psi_t x)=exp(kappa t)grad H(x).

Also det D Psi_t=exp(-dt). The codimension-one area formula therefore gives

    J_2(D Psi_t|T_xM)
        =exp(-Dt)|grad H(Psi_t x)|/|grad H(x)|.        (4)

This formula uses the ambient original derivative and its tangent restriction, which by (3) is exactly the projected surface derivative. It is valid even at equilibria. Relative to the positive density dA/|grad H| the surface Jacobian is exp(-Dt).

At a regular x put s(x)=|X(x)|=|B(x)| and let P_x^t be the one-dimensional normal Poincare derivative in T M, orthogonal to X. Since D Psi_t X(x)=X(Psi_t x), an orthonormal frame with first vector X/s gives

    |P_x^t|=exp(-Dt)
        |grad H(Psi_t x)|/|grad H(x)| s(x)/s(Psi_t x).

Parameterize a transverse section at each center y with tangent vector s(y) times a unit normal. The derivative between these normalized section coordinates is

    |P_x^{*,t}|=s(x)/s(Psi_t x) |P_x^t|
        =exp(-Dt)|grad H(Psi_t x)|/|grad H(x)|
                   [s(x)/s(Psi_t x)]^2.              (5)

Both speed factors are present. The first comes from removing the flow direction from the area Jacobian; the second comes from the chosen section coordinates.

## 3. Tempered speed without integrable logarithm

Let f=Psi_1 on S. A derivative bound for the C1 field on a compact neighborhood gives L<infinity with

    exp(-L)<=s(fx)/s(x)<=exp(L)

at every regular x in S. It follows from the variational equation for X along its own trajectories, applied for time1 and time-1. Thus q=log s composed with f minus log s is bounded on the full-measure regular set. Define q arbitrarily on the zero-mass equilibrium set.

The measure-preserving time-one Birkhoff theorem makes

    [log s(f^n x)-log s(x)]/n

converge almost everywhere. No time-one ergodicity is required. The limit is at most zero, since s is bounded above on S. For almost every x, recurrence in one of the sets {s>=1/j} gives a subsequence n with s(f^n x)>=1/j. The limit is therefore zero. Hence log s(f^n x)/n tends to zero almost everywhere. The bounded endpoint factors involving grad H in (5) imply

    lim_n n^(-1)log |P_x^{*,n}|=-D<0                 (6)

almost everywhere. This proves the required normal exponent directly, without integrating log s.

## 4. Uniform finite-time sections near possible equilibria

We prove the local fact needed to use (6). Let X be a C1 vector field on a neighborhood of a compact invariant set K in a C2 surface. Only trajectories through K need be complete. Write f for its time-one map on K. At each regular x choose a short transverse section I_x, parameterized by z with I_x(0)=x and I_x'(0)=s(x)n_x, where n_x is a unit normal to X in the tangent plane.

There are b>0, m>0, C<infinity and a modulus w tending to zero such that the holonomy from I_x to I_(f x), with transit time close to1, has normalized coordinate form F_x defined on (-b,b) and

    F_x(0)=0, m<=|F_x'(0)|<=C,
    |F_x'(z)-F_x'(0)|<=w(|z|).                       (7)

The sections themselves may be larger than this common input interval; F_x need not map (-b,b) into itself. The transit time lies between1/2 and3/2 after b is decreased. The derivative at the center is the normalized Poincare derivative in (5), up to orientation.

Here are the regularity and uniformity details. Work in finitely many C2 surface charts on a compact neighborhood of K, with bounded chart derivatives and uniform moduli of continuity for their derivatives. Sections can be short straight coordinate segments with the specified tangent, transported back to the surface. Thus no geodesic theorem for a C1 metric is needed. At a center p of speed s, rescale spatial chart coordinates by s. In Euclidean coordinates the field becomes

    X_p(z)=X(p+s z)/s, D X_p(z)=DX(p+s z).

Its initial coordinate norm is bounded above and below by fixed positive constants, since the chart norm and surface norm are uniformly comparable. Its derivative has a uniform bound, and its derivative modulus on bounded sets is bounded by a fixed modulus evaluated at a constant times |z-z'|, because s is bounded above on K. The normalized orbit remains in a uniformly bounded region for bounded time by Gronwall. The speed at times between-2 and2 is within fixed positive factors of s, using the forward and inverse variational equations. Thus terminal normalized transversality has a uniform positive lower bound.

For completeness, the uniform implicit-function estimate follows as follows. Choose the finite charts with inner chart domains covering K and a common positive coordinate margin rho0. Let Lam bound the chart and inverse differentials, let L bound the first derivative of each chart field Y, and let om be a common nondecreasing modulus for those derivatives. Let smax=max_K s. The case smax=0 has no regular point and is vacuous. For a regular p with chart coordinate u_p and speed s, put Y_p(z)=Y(u_p+s z)/s. Then

    Lam^(-1)<=|Y_p(0)|<=Lam,
    |DY_p|<=L,
    |DY_p(z)-DY_p(z')|<=om(smax|z-z'|).

Choose an integer k sufficiently large and tau=1/k. Choose z0>0 small so that smax(z0+Lam tau)exp(L tau)<rho0/2. Each rescaled solution starting in |z|<z0 remains in the chart for |t|<=tau, by the integral equation and Gronwall. Its derivative V_t satisfies

    ||V_t||<=exp(L tau),
    ||V_t(z)-V_t(z')||
       <=tau exp(2L tau)om(smax exp(L tau)|z-z'|).

Indeed subtract the two variational equations, use the Lipschitz bound exp(L tau)|z-z'| for the trajectories, and apply variation of constants. These estimates require only C1 regularity. The central speed ratio at the end of the step is bounded above and below by positive constants depending only on Lam,L,tau. A zero of Y_p cannot be within distance1/(Lam L) of the center when L>0; when L=0 no zero is possible in this chart component.

Let q be the terminal center. Express its transverse section in the same rescaled chart as sigma_q(zeta). Its center tangent is (s(q)/s)e_q, where Dphi(e_q) is a unit surface normal to X(q). The hitting equation is

    Phi_t^p(zeta0 e_p)=sigma_q(zeta).

At (zeta0,t,zeta)=(0,tau,0), the two columns of its derivative in (t,zeta) are Y_p(Phi_tau^p0) and -(s(q)/s)e_q. They are perpendicular in the surface metric before chart conversion. The metric distortion bound and the central speed bounds give a fixed positive lower bound gamma0 for their determinant. Their norms and inverse matrix norm are therefore uniformly bounded. All first derivatives of this equation have a common modulus of the form C0[r+om(C0 r)]. Straight coordinate sections have constant coordinate tangent; sections moved through a chart transition obey the same bound because transitions are C2 with bounded second derivatives on these compact chart domains.

To see explicitly that this gives uniform domains, freeze that invertible two-column Jacobian at the center. On a fixed small ball in (t-tau,zeta), its product with the varying derivative differs from the identity by at most1/2, by the common modulus. Newton's map with this frozen matrix is a contraction on that ball for all sufficiently small |zeta0|. This supplies the unique hitting time and target coordinate on a common input interval. Implicit differentiation and the inverse-matrix identity give a common bound C_tau on the holonomy derivative and a common derivative modulus tending to zero. Decrease the interval so the hitting-time error is less than1/(4k).

Compose k such steps to obtain time-one holonomy; the step length was chosen exactly1/k. Intermediate sections may be in different charts, whose changes have the same uniform bounds. A common input interval is obtained by decreasing the step interval by the factor max(1,C_tau)^k. The derivative bound is max(1,C_tau)^k, and a modulus follows by the finite product rule and composition of the step moduli. The sum of the k time errors is less than1/4, so the total time lies in(1/2,3/2). Applying the same construction to the inverse holonomy bounds its center derivative away from zero, giving m in(7). In the Euler application (5) also gives the explicit choice

    m=exp(-D-2L_B) min_S|grad H|/max_S|grad H|,

where L_B=max_S||DB|| controls the central speed ratio for unit time. Choose w nondecreasing, increasing it if necessary. Orientations may vary because only absolute derivatives enter. After choosing the recurrent base point in Section5, choose the section assignment coherently in its one regular chart. All constants are independent of this choice and of the minimum speed visited by the orbit. This proves(7), including visits arbitrarily close to equilibria.

## 5. A recurrent point with negative normalized exponent is periodic

Suppose a regular x in K is recurrent for f and has strictly negative limiting normalized exponent. If chi<0 denotes the limiting exponent, choose exp(chi)<lambda<eta<1 and K0>=1 such that

    A_n:=|P_x^{*,n}|<=K0 lambda^n for all n>=0.

Set x_i=f^i x and a_i=|F_(x_i)'(0)|. In one transverse dimension norms multiply exactly, so A_n=product_(i<n) a_i, with m<=a_i<=C. Choose recurrent integers n tending to infinity with x_n tending to x.

For large such n, the sections at x_n and x lie in one regular flow box around x. Short flow projection gives a closing holonomy C_n from I_(x_n) to I_x. Its center delta_n=C_n(0) tends to zero; its C1 norm, derivative modulus and domain can be chosen uniformly because s(x_n)->s(x)>0. Its small transit time may have either sign.

For this n put

    g_i=A_i/eta^i for 0<=i<n, g_n=1.

Then g_0=1 and 0<g_i<=K0. For i<n-1 define

    Ftilde_i(z)=F_(x_i)(g_i z)/g_(i+1),

and define the final map by

    Ftilde_(n-1)(z)=C_n(F_(x_(n-1))(g_(n-1)z)).

For every nonfinal map, its center derivative has absolute value eta and its derivative variation on [-r,r] is at most

    (eta/m)w(K0 r),                                  (8)

since g_i/g_(i+1)=eta/a_i. For the final map the center derivative is at most

    C_c a_(n-1)g_(n-1)
      =C_c A_n/eta^(n-1)
      <=C_c K0 eta(lambda/eta)^n ->0.

The family C_n composed with F_(x_(n-1)) has a common derivative modulus on a fixed small domain. Multiplication of its argument and derivative by g_(n-1)<=K0 retains a common modulus. Choose eta<eta1<1, then r>0 sufficiently small and finally n sufficiently large so every transformed map is eta1-Lipschitz on [-r,r]. Choose also K0 r<b and shrink r for the final projection's domain. These choices are independent of the large return n.

The nonfinal maps fix zero and map [-r,r] into [-eta1 r,eta1 r]. The final map has center delta_n. For large n, |delta_n|<(1-eta1)r, so it too maps [-r,r] into itself. Thus the whole composition R_n is a strict contraction of that interval. The coordinate scalings telescope because g_0=g_n=1; R_n is the actual flow return obtained by composing all original holonomies and the final projection. It has a fixed point, whose orbit is periodic and regular. Its total transit time is positive: the n block times are each at least1/2, and the final short time is bounded by a constant independent of n.

For this one fixed n, iteration of R_n sends the initial coordinate zero to its fixed point. The associated return-time function is continuous and bounded above and below by positive numbers on the compact interval. Uniform continuous dependence over the intervening bounded time intervals shows that the full forward orbit of x approaches this periodic orbit. Recurrence puts x itself on it. This last argument uses one periodic orbit and never compares reported periods with least periods.

We have proved: a regular recurrent point of a C1 surface flow near a compact invariant set, with negative normalized transverse exponent, is periodic. No hyperbolicity of equilibria, orientability of the entire surface, compact surface completion or shadowing theorem is assumed.

## 6. Application to the exceptional Euler measure

Choose x typical for (6), integer recurrence and whole-flow empirical convergence to mu. Apply Section5 to K=S and X=-Btilde. The point is periodic. Its continuous-time empirical probability is the normalized time measure on that periodic orbit, hence is mu. Therefore S is exactly the orbit.

Projected and original trajectories coincide on S. Choose one point where DW!=0, rank DW=1 and image DW=R B; these hold almost everywhere by A433 in its kappa case. The differentiated Cauchy law on W=0 preserves the rank of DW and transports its image; because D Psi_t B(x)=B(Psi_t x), rank DW=1 and image DW=R B hold around the entire orbit. The covector law already holds everywhere by (1). Thus all hypotheses of A449 hold, and it excludes this orbit. This proves Section1's theorem.

By A464 and A444's pointwise zero restriction, U!=0 on S holds automatically. Hence, with A445, no compactly supported whole-flow-ergodic probability with B!=0,W=0,DW!=0,D(B cross W)=0 almost everywhere exists in the global helicity-free class. Together with A433 this leaves, for nonstationary irrotational measures, either DW=0 almost everywhere or its other nonflat spectrum(a/2,0,-D/2), where D(B cross W) has rank one. This does not treat that other spectrum, first-jet-flat measures, carrier equilibrium atoms, measures not concentrated on W=0, arbitrary helicity sign or the general Gamma_E condition.

## 7. Primary source and verification record

The actual Jiagang Yang manuscript arXiv1502.06179v1 is pinned as in the team records. The normal-cocycle definitions and printed pages6-7 have been read directly from its extracted text. Lemma2.15 and Corollary2.16 assert the corresponding nonnegative-normal-exponent and zero-surface-exponent results for nontrivial ergodic measures; nontrivial excludes equilibrium and periodic-orbit measures. Section3 uses a scaled normal cocycle and a shadowing theorem. Its page7 inference from different reported periods to distinct periodic sinks needs a least-period justification. No refutation of its theorem is claimed. The independent one-dimensional return argument above supplies the exact implication needed here and does not depend on that inference or that source theorem.

The initial and reviewed source snapshots, the primary source, the focused review and this reconstruction are hashed in the team records. The focused review challenged (7) at C1 regularity, its domain near small speeds, the final rescaling, recurrence without time-one ergodicity and the two speed ratios in(5). Its advice was checked independently. The original unspecified short-step subdivision is now made with tau=1/k, and the uniform implicit-function argument is written out. No computation is needed for the proof. Review configuration identifies the primary model; this is configuration evidence, not independent provider attestation.
