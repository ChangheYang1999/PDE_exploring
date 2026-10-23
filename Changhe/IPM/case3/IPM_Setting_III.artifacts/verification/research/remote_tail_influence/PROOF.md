# Quantitative influence of a remote density tail on the core

Verifier result160. Written 2026-10-21 before the supporting exact checks. This addresses the suggestion that outgoing rescaled transport prevents a changing far field from influencing the core. Transport is local along characteristics; its canonical velocity law is not.

## Statement and hypotheses

Let 0<p<1 and R>0. Let h be a real smooth density perturbation on R^2, even in x and odd in y, identically zero for r<=R, and satisfying

    |h(X)|+r|grad h(X)| <= A r^p   for r>=R.

Let delta psi and delta U be its canonical whole-plane stream and velocity. Write

    h(r,theta)=sum_(n positive odd) f_n(r)sin(n theta),
    f_n(r)=1/pi integral_0^(2pi) h(r,theta)sin(n theta)dtheta.

For each even m>=2 set I_m=integral_R^infinity f_(m+1)(s)s^(-m)ds. Then on r<R,

    delta psi(r,theta)=1/2 sum_(m even>=2) I_m r^m sin(m theta).    (1)

The series and every derivative converge on each smaller closed disc. In particular,

    delta c=delta psi_xy(0)=I_2
           =integral_R^infinity f_3(s)s^(-2)ds.                  (2)

With delta=1-p and q=r/R<1,

    |delta c| <= 4A/(pi delta) R^(-delta),
    |delta U(X)| <= 4A/(pi delta) r R^(-delta)/(1-q^2),
    ||D delta U(X)||_op
       <= 4A/(pi delta) R^(-delta)(1+q^2)/(1-q^2)^2.             (3)

Thus a uniform exterior amplitude bound makes remote perturbations small on a fixed core as R tends to infinity. Outward support alone does not imply this. There are smooth compactly supported h_R, with support in R<r<2R, that tend to0 in every local smooth norm while their canonical strain stays exactly1. This is a counterexample to continuity of the canonical inverse for the topology of local smooth convergence alone on the union of the admissible growth classes with unrestricted constants. It is not an exact profile or an instability theorem.

For a pure third-mode tail h=f_3(r)sin(3theta) supported beyondR, if |f_3(r)|<=B r^(2p-1), then

    |delta c| <= B R^(-2delta)/(2delta).                         (4)

The hypotheses in (4) are a uniform tail bound, stronger than merely giving an asymptotic coefficient as r tends to infinity at each fixed time.

## Full-plane inverse inside the empty disc

The angular source g_m of h_x is

    g_m=1/2[f_(m-1)'-(m-1)f_(m-1)/r]
             +1/2[f_(m+1)'+(m+1)f_(m+1)/r].

The canonical radial Green formula, regular at0 and sublinear in velocity at infinity, gives for r<R

    (delta psi)_m(r)=r^m/(2m) integral_R^infinity g_m(s)s^(1-m)ds.

In the first term of this integral the integrand is one half the derivative of s^(1-m)f_(m-1), whose boundary terms vanish. In the second, integration by parts gives m integral_R^infinity f_(m+1)s^(-m). The lower terms vanish since h is identically zero up toR and smooth; the upper ones vanish since f_n=O(s^p) and p+1-m<0 for m>=2. Its derivative and other terms are absolutely integrable by the stated weighted gradient bound. This proves each coefficient in (1).

There is no angular zero sine mode and no odd stream mode. For m=2, r^2 sin(2theta)=2xy, so its stream contribution is I_2 xy and (2) follows. No extra harmonic strain was chosen: this interior harmonic term is determined by the remote density through the canonical whole-plane inverse.

The inverse formula can also be obtained by solving each radial ODE and eliminating the growing homogeneous coefficient at infinity. Uniqueness of the whole-plane canonical velocity follows because the difference is harmonic, sublinear and has the stipulated parities; the mean-value gradient estimate on arbitrarily large balls makes it constant, and parity makes it zero.

## Convergence and core bounds

The coefficient normalization gives

    |f_n(s)| <= (4/pi) A s^p,
    |I_m| <= (4A/pi) R^(p+1-m)/(m-p-1).                          (5)

The geometric factor (r/R)^m in (1) implies absolute convergence with every derivative on r<=eta R for any eta<1. Thus differentiating termwise is justified. A single harmonic stream r^m sin(m theta) has gradient norm m r^(m-1) and Hessian operator norm m(m-1)r^(m-2). With (5),

    |delta U| <= (2A/pi)R^p sum_(m even>=2)
                                  m q^(m-1)/(m-p-1).

For m>=2, m/(m-p-1)<=2/(1-p). Summing q+q^3+... gives the velocity bound in (3). The same inequality reduces the derivative bound to

    sum_(m even>=2) (m-1)q^(m-2)=(1+q^2)/(1-q^2)^2.

Equation (2) and (5) at m=2 give the strain bound. More generally, for a sequence of such perturbations at radii R_j tending to infinity with amplitudes A_j, the sufficient condition A_j R_j^(-delta)->0 makes their velocities converge to0 in C^1 on every fixed compact disc. Higher derivatives follow by the same geometrically convergent series; for derivatives beyond first the estimates decay at least as fast on a fixed disc. This is a sufficient control, not a necessary condition when modes or signs cancel.

## A remote perturbation with fixed strain

Choose any C-infinity nonnegative nonzero f compactly supported in1<s<2, normalized by integral_1^2 f(s)s^(-2)ds=1. Define

    h_R(r,theta)=R f(r/R)sin(3theta).

Each h_R is a smooth compactly supported density with the required parities. It vanishes on every fixed compact set once R is sufficiently large. Yet a change of variable in (2) gives delta c=1 for everyR. In fact (1) has only the m=2 term insideR, so

    delta psi=xy,   delta U=(-x,y)   on r<R.                     (6)

This is an induced interior strain, not an inadmissible added whole-plane harmonic. The velocity outside is generated by the compact source and is sublinear. If a fixed admissible nondegenerate density rho_0 is added to h_R, all its density jets and its local values eventually agree exactly with rho_0, but its canonical strain differs by1. The growth bound for each member holds, but a constant uniform inR at a fixed p<1 does not: the shell amplitude is of orderR, and A_R is of orderR^(1-p). The example therefore does not contradict (3).

The proof uses a smooth bump. Exact polynomial bump tests with finitely smooth extension below verify the integral formula and scaling only; they do not substitute a finite-regularity bump into the smooth theorem.

## Consequences for dynamic rescaling

For fixed C>1, c_x=C c_w and a=rho_y(0) fixed nonzero, slope preservation gives c_w=c_x+c, or c_w=-c/(C-1). Thus (2) changes c_w by -I_2/(C-1) even when the density perturbation is identically zero throughout the core. Outgoing W cannot by itself exclude this change.

A quantitative estimate may still make the effect negligible. For a pure sin(3theta) perturbation satisfying the envelope in (4), integration of r^(2p-3) proves (4). In a family with coefficient bound B(tau) and support outside R(tau), the sufficient condition B(tau)R(tau)^(-2delta)->0 gives vanishing core strain effect. For example, if |B| tends to infinity and R is bounded below by a positive constant times |B|^(1/delta), the bound is O(1/|B|). This is conditional on the support and envelope, and is not a demonstrated transition law for any computed DR trajectory. A fixed-time asymptotic coefficient alone does not supply the required uniform envelope or transition radius.

## Dependencies and verdict

Dependencies: the already independently derived canonical radial Green inverse; elementary Fourier coefficient estimates, integration by parts and geometric series; the audited DR slope relation. The calculation extends result152 to the m=2 strain response and supplies a uniform estimate. CONFIRMED analytic formulas and counterexample after exact support checks; outgoing transport alone as a shielding argument is REFUTED. The size and practical impact of this effect in actual DR trajectories remain OPEN. No principal endpoint follows.
