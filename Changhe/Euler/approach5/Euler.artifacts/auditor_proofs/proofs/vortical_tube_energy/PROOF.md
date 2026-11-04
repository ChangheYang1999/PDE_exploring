# Vortical tube energy and the critical exponent

## Statements

Let U in C2(R3;R3) be bounded and divergence-free, let P in C2 solve the rotating profile equation, and put A=cI-omega J, B=Ay+U, Omega=curl U. The B-flow Phi is complete. Define Q_t=exp(omega t J) and N_t(a)=exp(-tA) DPhi_t(a). For any bounded open V, eta in C1_c(V), constant v in R3 and t>=0,

exp((3c-1)t) |integral_V eta v.N_t Omega|
 <= exp(ct/2)|v| (integral_V |N_t^{-1}|^2 |grad eta|^2)^(1/2)
                 ||U||_{L2(Phi_t V)}.                         (1)

Assume c>0 and the Dini condition

integral_1^infinity m(r) dr/r < infinity,
 m(r)=sup_{|y|>=r}|DU(y)|.                                    (D)

If |a_0|>2||U||_infinity/c and Omega(a_0)!=0, a sufficiently small ball V about a_0 satisfies

||U||_{L2(Phi_t V)} >= k exp((5c-2)t/2), t>=t_0,               (2)

for constants k>0,t_0 depending on V and the profile.

Finally assume c=2/5 and Hb: U is bounded and U(R .)->0 in distributions as R tends to infinity. Under (D), U=0. In particular this holds for U(y)->0. Every statement holds for arbitrary finite omega, with no symmetry condition.

## Cocycle and distortion

Since div U=0,

det DPhi_t=exp(3ct), det N_t=1,
N_t'=Q_t DU(Phi_t a) Q_t^T N_t,
Omega(Phi_t a)=exp(-t)Q_t^T N_t(a)Omega(a).                    (3)

The last identity is the exact vorticity transport law. If M=||U||_infinity and r(t)=|Phi_t a|, then cr-M<=r'<=cr+M. Fix R_1>2M/c and |a|>R_1. The exterior is forward invariant and

(|a|-M/c)exp(ct)<=r(t)<=(|a|+M/c)exp(ct), r'>=cr/2.

Thus

sup_{|a|>R_1} integral_s^infinity |DU(Phi_t a)|dt
 <= (2/c) integral_{R_1 exp(cs)/2}^infinity m(r)dr/r = delta(s),

where delta(s)->0. Gronwall in (3) and in the inverse equation gives uniform bounds |N_t|,|N_t^{-1}|<=exp(delta(0)), and

|N_t-N_s|<=exp(delta(0))delta(s), t>=s.

Consequently N_t converges uniformly on the exterior to a continuous invertible N_infinity of determinant one.

## Proof of the tube estimate

Use the compactly supported test field

psi_t(y)=eta(Phi_{-t}y) Q_t^T v.

The Euler coupling Omega=curl U gives integral Omega.psi_t=integral U.curl psi_t, without boundary terms. Changing variables by Phi_t and using (3), the left side is exp((3c-1)t) integral_V eta v.N_t Omega. On the right,

grad(eta composed with Phi_{-t})(Phi_t a)
 =exp(-tA^T)N_t(a)^{-T}grad eta(a).

Its norm is at most exp(-ct)|N_t^{-1}||grad eta|. The Jacobian exp(3ct) therefore gives the L2 curl bound in (1), and Cauchy-Schwarz proves (1).

Set v=N_infinity(a_0)Omega(a_0)!=0. Continuity permits a ball V in the exterior on which v.N_infinity(a)Omega(a)>=|v|^2/2. Choose eta>=0 supported in V with positive integral. Uniform convergence gives integral eta v.N_t Omega>=k_0>0 for all large t. The inverse bounds and (1) now imply (2). The ball images lie in a shell with inner radius at least (R_1/2)exp(ct).

## Critical nonexistence

A054, proved independently from the canonical pressure and localized energy equation, implies U in L2(R3) under Hb at c=2/5. If Omega were nonzero at an exterior point, (2) would give a positive lower bound for its tube's L2 norm, whereas that tube escapes to infinity and the L2 tail tends to zero. Thus Omega=0 outside a sufficiently large ball.

Let K_+ be the set of points whose whole forward orbit remains in that ball. Every vortical point lies in K_+, because nonzero vorticity is preserved by the invertible formula (3). But Phi_t K_+ stays in the ball and has volume exp(3ct)|K_+|. Letting t tend to infinity gives |K_+|=0. The open set {Omega!=0} is null and therefore empty. Since U is bounded, curl-free and divergence-free on R3, its components are bounded harmonic functions and are constant. Hb makes that constant zero.

## Dependencies and limits

This audits Theory Agent A C12-C13, in the team records. The Dini condition can be replaced by its local orbit version: each exterior a_0 has a bounded neighborhood V with sup_{a in V} integral_t^infinity |DU(Phi_s a)|ds ->0. On the initial finite time interval, compactness gives the uniform bound needed for Gronwall.

No Dini condition has been deduced from velocity decay alone. For 2/5<c<1/2 the lower bound (2) has exactly the already allowed natural energy exponent, and yields no contradiction. Only the critical exponent is excluded by this argument. The pressure input is entirely A054; the test-field argument itself introduces no pressure normalization.
