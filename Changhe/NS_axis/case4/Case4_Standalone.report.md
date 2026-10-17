# Case 4: first normalizations for axisymmetric Navier-Stokes singularities with bounded circulation

Status: UNRESOLVED_NOT_ACCEPTED

First missing implication: in the regime $D/M^2\to0$, exclusion of the residual cascade alternative (C) of
Theorem 5 below; equivalently, the existence, at some amplitude-$M$ Euler-scale normalization with retained
$L^2$ oscillation, of a uniform local $L^2$ translation modulus for the physical solution (for instance through the
vorticity bound (VL1) of Theorem 6, for which a bound on one signed part of $\omega^\theta$ suffices by Corollary 6A). When the flat alternative (FLAT) of Proposition 14 fails, a sufficient condition is
a bound, uniform in $n$, on the meridional vorticity mass $\ell_n^{-2}M_n^{-1}\int_{B_{R\ell_n}(x_n)\cap\{r>h\ell_n\}}|\omega^\theta(t)|\,dx$
over the last $A$ Euler times, for all $R,A,h$, at one normalization with the terminal certificate (OSC$_0$) of
Theorem 17 (Proposition 22). Proposition 25 shows that the analogous single-time exterior mass condition is
stronger than compactness for single-time fields, so this sufficient condition may be strictly stronger than the
exclusion of (C); necessity of (EC) in the trajectory class is open. In the weaker topology (ST) of Section 6A the first missing implication is the
exclusion of the alternative (C*) of Corollary 13 (which is contained in (C)), that is, of both the flat alternative
(FLAT) and the defect alternative (C*-D) of Proposition 14; by Proposition 14A, equivalently, of (FLAT$_0$) (historical
BMO norm $o(M)$; by Proposition 14C it can hold only with $\Theta_0\ge cM/\log(E_0M)$) and of (C*)$\cap$(HD) (some admissible normalization has a nonzero Reynolds defect; it then has one
with a constant weak limit, a constant nonzero defect and retained terminal $L^2$ oscillation). Outside (C*), GOAL in (ST) holds with the anchor and the
terminal slice chosen by rules applied to each trajectory, not from the limit (Theorem 17, Corollary 18). In both
topologies the exclusion of the residual alternative would not by itself give a selection rule computed from records
for every trajectory: in (B) the defining conditions concern the rescaled physical solution, in (B*) they concern an
admissible joint subsequential limit, and in both the starting normalization is given only by an existence statement. Explicit rules are
proved under additional conditions, among them (L2LS) of Theorem 5', a ratio condition on level scales (Section 5), a
prescribed modulus (the Remark at the end of Section 6), and (EC) for the outputs of a prescribed rule producing
normalizations with the physical certificate (OSC$_0$) (Proposition 22); the mere existence of some normalization with
both certificates gives the analytic requirements only. The first missing implication is stated within the strategy of
admissible amplitude-$M$ isotropic normalizations: neither (C) nor (C*) is shown to be equivalent to the failure of
every first normalization allowed by Case 4 (for instance, the conditional extractions of Proposition 14B, under its
granted regularity input and the respective record hypotheses, yield nonconstant limits whose global boundedness is not
proved).

## Result

Let $u$ be the maximal smooth solution of the three-dimensional Navier-Stokes equations (unit viscosity) with smooth,
axisymmetric, divergence-free data $u_0\in\bigcap_kH^k(\mathbb R^3)$, energy $E_0=\|u_0\|_2^2$, and circulation
bound $G=\|ru_0^\theta\|_\infty<\infty$, and suppose $u$ blows up at a finite time $T_*$. Write
$M(t)=\sup_{s\le t}\|u(s)\|_\infty$, $D(t)=\sup_{s\le t}\|\nabla u(s)\|_\infty$, $S(t)=\sup_{s\le t}\|u^\theta(s)\|_\infty$,
and $\omega_t(\rho)=\sup_{s\le t}\sup_{x,|h|\le\rho}|u(x+h,s)-u(x,s)|$ (historical modulus).

The goal (GOAL) is a selection rule, computable from records or from a quantitatively specified observable, and a
physically justified first normalization $U_n$ such that along one subsequence $U_n\to U$ strongly locally including
the terminal time $\tau=0$, $\sup|U|<\infty$, $U$ is spatially nonconstant, and $U$ solves a rigorously derived ancient
PDE with the correct pressure class. This report does not achieve GOAL for every singular trajectory.

Convention. Below, "GOAL holds" for a normalization means that the analytic requirements of GOAL (strong convergence
including $\tau=0$, boundedness, spatial nonconstancy, the limit equation with canonical pressure) hold for that
normalization; how the normalization is selected is stated separately in each case. The selection requirement is
met by an explicit rule from records in regime (I) (first crossings, Theorem 2), when (UP) fails (near-maximizers of the
oscillation at a fixed multiple of the Lipschitz scale at which (UP) fails, Theorem 4(c)), under (L2LS) (Theorem 5'),
and by any prescribed rule from physical observables that produces normalizations with the physical certificate
(OSC$_0$), provided its outputs satisfy (EC) (Proposition 22); the existence of some normalization with both
certificates gives the analytic requirements but does not supply such a rule. In alternative
(B) in general the normalization is only shown to exist; it is not chosen from the limit, since its defining
conditions, including the oscillation certificate, concern the rescaled physical solution, but no computable rule
producing it is given. In (B*) the defining conditions (a vanishing defect and a weak limit that is not constant at
some time) concern a joint subsequential limit, so a (B*) normalization is characterized through its limit; Corollary
18 applies rules computed from the trajectory to such a normalization but does not select it. The end-time shift of Theorem 12 is chosen from the weak limit, that is, retrospectively.

What is proved:

1. (Regime split.) Exactly one of (I) $\limsup_{t\uparrow T_*}D/M^2>0$ and (II) $D/M^2\to0$ holds, and (II) is
   equivalent to $S/M\to0$ (Theorem 3).
2. (Regime I.) In regime (I), GOAL holds with the parabolic normalization at first-crossing records of
   $\|\nabla u\|_\infty$; the limit is a bounded ancient mild Navier-Stokes solution with canonical BMO pressure and
   $|\nabla U(0,0)|\ge c>0$ (Theorem 2). No Liouville theorem is needed.
3. (Reduction to a plateau.) In regime (II), GOAL holds with an explicit Euler-scale normalization unless the uniform
   plateau alternative (UP) holds: $\omega_t(RM/D)/M\to0$ for every fixed $R$ (Theorem 4). Under (UP), every
   amplitude-$M$ normalization at the Lipschitz scale $M/D$ has only space-time constant limits.
4. (Main reduction.) GOAL also holds whenever some admissible amplitude-$M$ Euler-scale normalization has a uniform
   local $L^2$ translation modulus (L2M) and retained $L^2$ oscillation (L2-OSC); the limit is a bounded, swirl-free
   weak Euler solution with canonical pressure, axisymmetric about a limiting axis or planar. So GOAL holds unless the
   residual alternative (C) holds: every admissible amplitude-$M$ normalization with retained $L^2$ oscillation
   fails (L2M) (Theorem 5); in (B) the normalization is given by an existence statement. The convergence obtained is in $C([-A,0];L^2_{loc})$ for every $A$ (strong local
   convergence including the terminal trace, not locally uniform). (C) is stated literally; no equivalence with a condition on
   Reynolds defects is proved.
4'. (Observable rule.) A sufficient condition for GOAL in regime (II), stated through an explicit observable, is
   the $L^2$ level-scale condition (L2LS) of Theorem 5': the smallest scale at which the historical local $L^2$
   oscillation reaches a fixed fraction $c$ of $M$ is comparable to the smallest scale at which it reaches every
   smaller fraction. The selection is then the level scale with a near-maximizing center.
4''. (Defect-free reduction.) In regime (II) it suffices that some admissible amplitude-$M$ normalization has a
   vanishing Reynolds defect and a weak limit that is spatially nonconstant at some time (Theorem 12). After an end-time
   shift by a bounded number of Euler times, taken from a full-measure set determined by the weak limit (a
   retrospective choice, which does not meet the selection requirement), the analytic requirements of GOAL then
   hold with strong convergence in $L^2_{loc}$ of space-time and strong $L^2_{loc}$ convergence of the terminal slice
   (topology (ST)), which is weaker than the $C_tL^2_{loc}$ convergence of Theorem 5. No choice from the limit is in
   fact needed: re-anchoring at a maximizer of a weighted oscillation observable and then selecting a terminal slice
   within one Euler time by a threshold rule on translation differences, both computed from each rescaled trajectory,
   gives GOAL in (ST) for the normalization so obtained from the given one; the slices converge strongly there, and the limit there is nonconstant by a relative-energy
   argument (Theorem 17, Corollary 18). In this weaker sense the
   alternatives are (A), (B*) (some admissible joint subsequential limit is defect-free and nonconstant; it contains
   (B)) and (C*) (Corollary 13); GOAL holds in (A), and in (B*) for a normalization given by an existence statement. The remaining alternative (C*) is contained in (C) and
   splits into the flat alternative (FLAT) (at every scale the velocity mollified at a fixed relative resolution has
   oscillation $o(M)$; then every weak limit of an admissible amplitude-$M$ isotropic normalization is constant, $E_0D^3/M^5\to\infty$, and every velocity
   record sits in an approximately uniform jet extending over unboundedly many octaves above the Lipschitz scale;
   every joint limit is one space-time constant $b$ with a Leray-free defect, and, along each joint convergent
   subsequence, the normalizations at fixed multiples of the Lipschitz scale around velocity records converge strongly,
   without defect, to a constant unit vector equal to the limiting normalized record direction) and the defect alternative (C*-D) (Proposition 14). Exact bounded Navier-Stokes families show that neither branch
   can be excluded using the limit equation alone. Re-zooming at a Lebesgue point of a nonzero defect (Proposition 14A)
   shows that (C*) is the disjoint union of (FLAT$_0$), historical BMO norm $o(M)$, in which every admissible
   normalization converges in (ST) along subsequences to constants, and of (C*)$\cap$(HD), where (HD) provides an
   admissible normalization of the same trajectory with a constant weak limit, a constant nonzero defect annihilating
   the azimuthal direction (rank at most two),
   mollified fields converging locally uniformly to that constant and retained terminal $L^2$ oscillation; (C*-D) is
   contained in (HD). This is a reduction, not an exclusion.
4'''. (BMO amplitude.) Write $\Theta_0$ for the historical BMO norm (Proposition 14A). The bound
   $\|\nabla p\|_\infty\le C\|u\|_{BMO}\|\nabla u\|_\infty$ holds at every time, and, granting the quantitative one-scale
   $\epsilon$-regularity theorem, $D\le C_a+C\Theta_0^2$ (Proposition 14B(a)). Ancient Navier-Stokes solutions with bounded
   gradient, bounded BMO norm and the absolutely convergent, curl-free increment pressure are constant if they are
   invariant in one direction or axisymmetric without swirl (Proposition 14B(b)). Consequently, if $D/\Theta_0^2$ does not
   tend to $0$, there are $\delta>0$ and record times with $D(t_n)\ge\delta\Theta_0(t_n)^2$ for which the normalizations at
   gradient records, with amplitude $\Theta_0(t_n)$, length $1/\Theta_0(t_n)$, unit viscosity and the constant Galilean
   frame of the local mean, have a subsequence converging locally with first derivatives through $\tau=0$ to a
   nonconstant ancient solution of this class, whose pressure gradient is exactly the increment pressure; after a
   further constant horizontal boost the limit is axisymmetric about a fixed line, with circulation bounded by $G$ and
   nonzero swirl (Proposition 14B(c)). BMO records with bounded $\kappa_n=\Theta_0(t_n)\rho_n$ give the corresponding
   subsequential limits at length $\rho_n$, with viscosity $1/\kappa$ and circulation bound $G/\kappa$ (Proposition
   14B(d)). These normalizations are computed from records, and their limits have the convergence, nonconstancy and
   limit equation required by GOAL, but at the amplitude $\Theta_0$ rather than $M$, and global boundedness is not
   established: the limits satisfy $|v|\le C_A(1+\log(2+|y|))$ on each slab $-A\le\sigma\le0$. Rigidity with
   swirl in this class is not proved here (it contains the bounded-circulation case of the KNSS conjecture, which the
   sources we read describe as open), and the scalar rates of Remark (ii) after Proposition 14B satisfy both
   $D/\Theta_0^2\to0$ and (FLAT$_0$); so the present arguments exclude neither (FLAT$_0$) nor (C). Finite energy restricts (FLAT$_0$) quantitatively:
   if $\Theta_0\le M/32$, then $D^3\ge c_0E_0^{-1}M^2\Theta_0^32^{3M/(16\Theta_0)}$, and, since $D\le M^2$ near $T_*$ in regime (II),
   $\Theta_0\ge cM/\log(E_0M)$ near $T_*$ without any granted input (Proposition 14C); the scalar rates above satisfy this.
   Following the local mean along its own path shows that, at sufficiently flat dyadic velocity records, a large mean
   persists for a time longer by a factor $e^{c M/\Theta_0}$ than the elementary pressure bound gives, with a lower bound for
   $M(t)^2(T_*-t)$ in terms of the flatness ratio at the next dyadic record, which tends to infinity under (FLAT$_0$)
   (Proposition 14D; that $M^2(T_*-t)\to\infty$ in regime (II) is already Proposition 7(c)); the dissipation this certifies is summable, so it does not exclude (FLAT$_0$).
   At every sufficiently large dyadic velocity record $t_n$ with $h_n\ge h_*$, the signed pressure impulse along the
   backward-diffusing packet, over the age interval $\varsigma_n=KE_0^{2/3}m_n^{-4/3}<t_n$, is at least $m_n/2$. The older averaged
   velocity has norm at most $m_n/4$ (Remark after Proposition 14D). The bound $O(\Theta_0)$ for this impulse that would exclude (FLAT$_0$) is not proved, and the upper bound
   that is proved does not suffice.
5. (Vorticity certificates.) (L2M) holds at any admissible scale $\ell$ at which
   $\int_{B_{R\ell}}|\omega^\theta|\le C_{R,A}M\ell^2$ on every window of $A$ Euler times, for every fixed $R$ and $A$, with
   $C_{R,A}$ independent of $n$ (Theorem 6). By the circulation
   bound $|\int\!\!\int_P\omega^\theta\,dr\,dz|\le M\operatorname{perimeter}(P)$ on meridional rectangles, a bound on one signed part of
   $\omega^\theta$ suffices; so in (C), for every admissible normalization with retained oscillation, there are a radius, a
   subsequence and times in a bounded Euler window at which the meridional vorticity on the corresponding rectangle has both
   signs with unbounded normalized masses that cancel up to a bounded amount (Corollary 6A). For each fixed $h>0$ the
   signed meridional masses on the exterior rectangles $[\max\{h,d_n-R\},d_n+R]\times[-R,R]$ ($d_n$ the rescaled axis
   distance) are, up to $o(1)$, carried by fluid that stayed outside a tube around the axis of normalized radius
   $a_n\to0$ during the preceding $A_n\to\infty$ Euler times (Lemma 26A); this concerns particle paths, not where the
   vorticity was generated, and it bounds neither signed exterior mass. Near the
   axis the bound of Theorem 6 is implied by $\int_{B_{R\ell}}|\omega^\theta/r|\le CM\ell$; the global bound proved here for
   $\|\omega^\theta/r\|_{L^1}$ (Lemma 9, under the additional integrability of the data and of $\omega^\theta/r$ assumed
   there) misses it by the unbounded factor $(E_0M)^{1/2}$. Without that integrability, the accumulated swirl source
   $\int_0^t\|\partial_z(q^2)\|_{L^1}$ up to the observation times $t=t'_n$ in the windows of Corollary 6A exceeds $2\pi M\ell$ times
   their normalized mass up to $o(1)$, and at least half of this lower bound comes from a physical tube around the axis whose radius tends to zero
   but is much larger than $\ell$ (Remark after Lemma 9'); both facts are compatible with the available upper bound and
   do not locate the production within the preceding history. For Navier-Stokes trajectories a
   much weaker certificate suffices. Off the axis the meridional vorticity mass in a ball of fixed radius can grow, over
   a bounded elapsed Euler time $\Delta\tau$, only by transport from the ball enlarged by $\Delta\tau$ plus a collar of fixed
   width $w\in(0,1]$, provided this whole enlarged ball stays at normalized distance at least $d'>0$ from the axis, up to
   the factor $e^{\Delta\tau/d'}$ and an error $O(D/M^2+GD/M^2)$ whose constant depends on the radius, $w$, $\Delta\tau$ and
   $d'$ (Lemma 21); the rescaled swirl source of $\omega^\theta/r$ tends to zero in $W^{-1,1}_{loc}$ and uniformly
   off the axis (Lemma 19). Consequently the exterior certificate (EC), a bound on the meridional vorticity mass over the
   last $A$ Euler times outside every tube $\{r\le h\ell\}$ around the axis, with constants that may blow up as $h\to0$
   (in time-integrated or, equivalently, single-time form), implies (L2M) (Proposition 22). With the terminal
   certificate (OSC$_0$) $O_\epsilon(x_n,s_n,\ell_n)\ge cM_n$ of Theorem 17 (a physical selection, available exactly when
   (FLAT) fails), (EC) gives case (B) of Theorem 5: GOAL in $C([-A,0];L^2_{loc})$ at the physical terminal time, with no
   terminal-slice rule. The time-integrated full-ball bound (VC) of Theorem 6' implies (EC) (Proposition 20); the
   terminal-slice rules of Theorem 17(d) and Proposition 20(b), which give GOAL in (ST) under (VC) or (EC), remain correct
   but are not needed for this conclusion. In (C) every normalization with (OSC$_0$) has $\ell_nD_n/M_n\to\infty$ and
   violates (EC) along every subsequence. A historical bound $O(M)$ for $\|\omega^\theta\|_3$ would give (VC) for every
   admissible normalization and so exclude the part of (C) outside (FLAT); one for $\|\omega^\theta/r\|_{3/2}$ would do so
   given a certified normalization with bounded rescaled axis distance (whose existence is not proved). Neither bound is
   available, and such bounds cannot address (FLAT) (Section 9B, Remarks). Section 9D tests this route: energy makes $\sum_nM_n\ell_n^2$, hence
   the sum $\sum_n\ell_n$ of the scales, finite over certified windows with boundedly overlapping persistence cylinders (Proposition 24), so the local
   budget of Lemma 9' alone gives no uniform bound on the exterior mass along windows approaching $T_*$; for single-time
   fields, failure of the exterior mass bound at every certified scale is compatible with compactness of the certified
   rescalings (Proposition 25), so (EC) may be strictly stronger than what is needed (a strict separation for
   trajectories is not proved); and certified windows approach the axis (Corollary 26).
5'. (Sub-amplitude criterion, conditional.) A normalization at an amplitude $B_n$ with $D_n/B_n^2\to0$ (of interest
   for $B_n=o(M)$) at the Lipschitz scale $B_n/D_n$, in the constant Galilean frame of the observed central velocity,
   gives GOAL with locally uniform convergence through $\tau=0$ provided, with constants $C,c>0$ independent of $n$, it
   is bounded by $C$ on cylinders $B_{R_n}\times[-A_n,0]$ with $R_n,A_n\to\infty$ and $A_n$ at most the rescaled depth
   $s_nD_n$, satisfies $\sup_{B_1}|v_n(\cdot,0)|\ge c$, and has a time-integrated tail
   $\int_{-A_n}^0\int_{|y|>R_n}|v_n|^2|y|^{-4}$ tending to zero (Proposition 15). These hypotheses are not derived from the
   a priori estimates. The time part of the local bound on $B_{\rho_n}\times[-A_n,0]$ follows from the terminal bound on
   the ball of radius $(\rho_n+A_n)e^{A_n}+A_n+1$ if $A_n$ times the rescaled pressure gradient on the cylinder over a
   ball one unit larger tends to zero and $A_n\nu_n^{1/2}\to0$, $\nu_n=D_n/B_n^2$ (Lemma 15', a Lagrangian estimate), but the available a priori bound for the pressure gradient (the increment integral) is
   bounded below by a positive constant in rescaled units at any scale where the terminal oscillation holds, so the
   needed smallness would require cancellation in the pressure integral, and the terminal quiet zone is not given by the present estimates (a
   functional family shows that increment behaviour alone cannot give it).
5''. (Weighted relative energy.) For a smooth bounded Navier-Stokes solution $v$ with canonical pressure and bounded
   $\nabla v$, $\nabla^2v$, $\partial_\tau v$, compared with a bounded $C^1$ Euler solution $V$ with canonical pressure and
   bounded $\nabla V$, $\partial_\tau V$, the relative energy in the weight $(1+|y|^2/L^2)^{-\alpha/2}$, $3<\alpha<5$, satisfies
   a Gronwall inequality (Lemma 16, Proposition 16(a)). Hence strong
   convergence on earlier slices propagates to $\tau=0$ whenever the limit is classical on a terminal interval
   (classical regularity of the unknown limit is not derived), and a limit that is constant at a slice of strong
   convergence stays constant at later times, which is the nonconstancy argument of Theorem 17. Under (FLAT)
   the weighted defect energy $e_1$ of Proposition 16(c) satisfies $e_1(t)\le C_\alpha(1+t-a)^\alpha e_1(a)$ for $a<t$ in a set of
   full measure, so it can decrease backward in time at most polynomially, and exact swirl-free pipe flows carry
   stationary defects, so this estimate does not exclude a defect.
6. (Dynamics under (UP).) Under (UP), $\|\nabla p(t)\|_\infty=o(M(t)D(t))$ and $M(t-A/D(t))/M(t)\to1$ for every fixed
   $A>0$: the velocity record is frozen over bounded multiples of the Lipschitz-scale Euler time $1/D(t)$ (Proposition 7); in particular the temporal certificate of Section 5 (a drop of the velocity record within a fixed multiple of the time $1/D$) fails under (UP). In regime
   (II), $M(t)^2(T_*-t)\to\infty$, so (C) can occur only for velocity Type II blow-up; Type I is not assumed anywhere,
   it is excluded from regime (II) by a short argument (Proposition 7(c)).
7. (Single-time test.) An explicit one-dimensional profile (Proposition 10) satisfies, uniformly in a parameter $N$,
   amplitude and Lipschitz normalizations, the plateau modulus of (UP) (after a dilation into the regime
   $D/M^2\to0$), retained $L^2$ oscillation at the energy scale, and failure of (L2M) at the energy scale and on every
   interval of length $2\pi4^{-j}$ where $L^2$ oscillation is retained. Its three-dimensional transfer (Proposition 10')
   is a family of smooth, compactly supported, divergence-free, axisymmetric, swirl-free fields of fixed energy with
   $M,D\to\infty$, $D/M^2\to0$, the plateau modulus of (UP) and $L^2$ oscillation at a scale comparable to the energy
   length, for which every amplitude-normalized window that retains $L^2$ oscillation, at any centre and any scale,
   fails the $L^2$ translation modulus. So the single-time inequalities used in this report do not by themselves
   exclude (C)-type behaviour, in one or in three dimensions. This is a single-time test: the fields are not a
   Navier-Stokes trajectory, and it does not show that no single-time argument using other information about
   three-dimensional finite-energy fields could succeed.

No genuine fixed-data counterexample is claimed. The single-time test profiles (Section 10, Proposition 25) and the
kinematic and functional families of Sections 6, 6A, 8 and 9 are not Navier-Stokes solutions; the exact Navier-Stokes families of
Section 6A (Remark after Proposition 14) and of Section 9 (after Proposition 16) are bounded infinite-energy solutions that are not rescalings of one
solution, used only to show what the limit equation alone cannot decide. The shears of the Remark at the end of Section 6 are
stationary Euler solutions of infinite energy.

## Method

The historical records at reference times $t_n$ supply the
amplitudes and the scale bounds; the terminal times $s_n\le t_n$ of the rescalings are record times in Theorem 2 and may
be other past times elsewhere (Theorems 4, 5', 12). The rescalings preserve the Navier-Stokes coefficients up to an explicitly computed viscosity $\nu_n$. The main tools are:
first-crossing records and the maximum principle at a record; the circulation maximum principle; an exact increment
formula for the pressure gradient with an explicit constant; the KNSS smoothing estimates for bounded mild solutions;
compactness under a uniform modulus in $C^0$ or in local $L^2$, with identification of the canonical BMO pressure by
duality with the Hardy space; canonical-pressure rigidity of spatially constant solutions; the KNSS Liouville
theorems in dimension two and for swirl-free axisymmetric flows, and their analogues for ancient solutions with bounded
gradient and bounded BMO norm in a constant Galilean frame; one-cylinder $\epsilon$-regularity in such a frame; a div-curl translation estimate for the meridional
velocity; a weighted relative-energy inequality for bounded solutions with canonical pressure; a selection of
terminal slices by a rule applied to each rescaled trajectory; and lacunary Fourier series (moment computations,
Paley-Zygmund) for the functional test.

### Setting and standing facts

$u$ is axisymmetric for all $t<T_*$, $u\in C([0,T_*);H^k)$ for all $k$, so $u(t)$ and all its derivatives lie in
$C_0(\mathbb R^3)$. The pressure is $p=R_iR_j(u_iu_j)=\Phi*\partial_iu_j\partial_ju_i$, $\Phi(z)=(4\pi|z|)^{-1}$. The
energy identity gives $\|u(t)\|_2^2+2\int_0^t\|\nabla u\|_2^2=E_0$. Leray's lower bound gives $\|u(t)\|_\infty\to\infty$
and the Beale-Kato-Majda criterion gives $\int_0^{T_*}\|\nabla u\|_\infty=\infty$, so $M,D\to\infty$. The circulation
$\Gamma=ru^\theta$ satisfies $\|\Gamma(t)\|_\infty\le G$. Duhamel's formula holds with the Oseen kernel
$|\mathcal K_\tau(x)|\le C(|x|+\sqrt\tau)^{-4}$.

For a continuous nondecreasing $Q(t)=\sup_{s\le t}q(s)$ and a level $\lambda>q(0)$ that is reached, the first
crossing $t_\lambda=\min\{s:q(s)=\lambda\}$ has $q(t_\lambda)=\lambda>q(s)$ for $s<t_\lambda$, and every value of $Q$
above $q(0)$ is attained at a first crossing.

## Findings

### 1. Swirl and energy inequalities

**Lemma 1 (record identity and swirl bounds).** (a) At a first crossing $t_\lambda$ of $\sigma(s)=\|u^\theta(s)\|_\infty$
and a point $x_\lambda$ with $\epsilon u^\theta(x_\lambda,t_\lambda)=\lambda$ ($\epsilon=\pm1$): $r_\lambda=r(x_\lambda)>0$ and
$-r_\lambda u^r(x_\lambda,t_\lambda)\ge1$. (b) $S(t)\le\max(\sigma(0),GM(t))$. (c) $\|u^\theta(s)\|_\infty^2\le
G\|\nabla u(s)\|_\infty$, hence $S^2\le GD$.

Proof. (a) $u^\theta=0$ on the axis, so $r_\lambda>0$. With $v=\epsilon u^\theta$, $\partial_tv\ge0$ at the record
(first crossing, $u$ is $C^1$ in time), $\partial_rv=\partial_zv=0$ and $\partial_{rr}v+\partial_{zz}v\le0$ at the
spatial maximum. The swirl equation $\partial_tu^\theta+u^r\partial_ru^\theta+u^z\partial_zu^\theta+u^ru^\theta/r=
(\partial_{rr}+r^{-1}\partial_r+\partial_{zz}-r^{-2})u^\theta$ then gives $u^r\lambda/r_\lambda\le-\lambda/r_\lambda^2$.
(b) If $S(t)=\lambda>\sigma(0)$ is attained at a first crossing $t_\lambda\le t$, (a) gives $1\le r_\lambda M(t)$, and
$r_\lambda\lambda\le G$. (c) Along a ray $\rho\mapsto(\rho\cos\theta,\rho\sin\theta,z)$ the derivative of $u^\theta$ is
$e_\theta\cdot(e_r\cdot\nabla)u$, so $|u^\theta|\le r\|\nabla u\|_\infty$; multiply by $|u^\theta|\le G/r$. $\square$

**Lemma 2 (energy).** $M(t)^5\le\frac{24}\pi E_0D(t)^3$. Put $L_E(t)=(6E_0/(\pi M(t)^2))^{1/3}$. If $s\le t$ and
$|u(x_*,s)|=M(t)$, then $\operatorname{osc}_{B_{L_E}(x_*)}u(s)\ge M(t)/2$.

Proof. $|u(\cdot,s)|\ge M/2$ on $B_{M/(2D)}(x_*)$, so $E_0\ge\frac{M^2}4\frac{4\pi}3\frac{M^3}{8D^3}$. If $|u(\cdot,s)|\ge
M/2$ on all of $B_{L_E}(x_*)$, then $E_0\ge\frac{M^2}4\frac{4\pi}3L_E^3=2E_0$. $\square$

### 2. Pressure

**Lemma 3 (increment formula).** For divergence-free $v\in C^1$ with $v,\nabla v$ bounded and $\nabla v\in L^2$,
$q=\Phi*\partial_iv_j\partial_jv_i$ satisfies
$$\partial_kq(x)=\int K_{kij}(z)\,w_i(z)w_j(z)\,dz,\quad w(z)=v(x-z)-v(x),\quad
K_{kij}=\frac{3}{4\pi|z|^4}(\delta_{ij}n_k+\delta_{ik}n_j+\delta_{jk}n_i-5n_in_jn_k),$$
$n=z/|z|$, and $\|\nabla q\|_\infty\le24\|v\|_\infty\|\nabla v\|_{\infty}$. In particular
$\|\nabla p(s)\|_\infty\le24M(t)D(t)$ for $s\le t$.

Proof. With $W=v-v(x)$, divergence freeness gives $\partial_iv_j\partial_jv_i=\partial_i\partial_j(W_iW_j)$. Integrate by
parts twice on $\{\epsilon<|y-x|<R\}$; inner boundary terms are $O(\epsilon)$; outer ones vanish along a sequence
$R_m\to\infty$ because $\nabla v\in L^2$ and $v$ is bounded. The integrand is bounded by
$C\min(\|\nabla v\|_\infty^2|z|^{-2},4\|v\|_\infty^2|z|^{-4})$. For the constant: $K_{\cdot ij}w_iw_j=\frac{3}{4\pi|z|^4}
[2(n\cdot w)w+n(|w|^2-5(n\cdot w)^2)]$ and the bracket has squared norm $|w|^4(1-2q+5q^2)\le4|w|^4$,
$q=(n\cdot w)^2/|w|^2$; with $|w|\le\min(L|z|,2M)$, $|\nabla q|\le6\int_0^\infty\min(L^2,4M^2\rho^{-2})d\rho=24ML$.
$\square$

For a bounded field $F$, $R_iR_jF_{ij}\in BMO$ is defined by duality with the Hardy space $\mathcal H^1$. If $F_n\to F$
weak-* in $L^\infty$, then $R_iR_jF_{n,ij}\to R_iR_jF_{ij}$ weak-* in $BMO$ and the gradients converge in $\mathcal D'$
(test with $R_iR_j\operatorname{div}\phi\in L^1$). If the fields are moreover uniformly Lipschitz and converge locally
uniformly, the pointwise functionals $\Pi[U_n]=\int K_{\cdot ij}w_iw_j$ converge locally uniformly, and the BMO pressure
gradient equals $\Pi[U]$ (the difference of two BMO solutions of the same Poisson equation is harmonic and BMO, hence
constant). A spatially constant field $U=b(\tau)$ has $\nabla R_iR_j(b_ib_j)=0$: no free uniform pressure force
$-a(\tau)\cdot y$ can appear in a limit with canonical pressure.

### 3. Regime I: parabolic extraction at gradient records

**Lemma (smoothing; KNSS, Acta Math. 203 (2009), Prop. 4.1, (4.6)).** There are absolute $C_{k,l}$ with
$\|\nabla^k\partial_t^lu(t)\|_\infty\le C_{k,l}M(t)^{1+k+2l}$ whenever $t\ge1/(2M(t)^2)$ (restart a time $\delta M^{-2}$
earlier; the classical solution is the unique bounded mild solution from the restarted datum). Consequently
$\limsup D/M^2\le C_{1,0}$.

**Theorem 2 (regime I).** Assume $\limsup D/M^2=2c>0$. Let $s_n$ be first crossings of $\|\nabla u\|_\infty$ at levels
$\lambda_n\to\infty$ with $D(s_n)\ge cM(s_n)^2$ (they exist: the first crossing of the level $D(t)$ at a time $t$ with
$D(t)\ge cM(t)^2$ inherits the inequality), $x_n$ with $|\nabla u(x_n,s_n)|=D(s_n)$, $M_n=M(s_n)$, and
$U_n(y,\tau)=M_n^{-1}u(x_n+y/M_n,s_n+\tau/M_n^2)$. Along a subsequence $U_n\to U$ in $C^k_{loc}(\mathbb R^3\times
(-\infty,0])$ for every $k$, where $U$ is a bounded ancient mild Navier-Stokes solution, $\|U\|_\infty\le1$, with
pressure $R_iR_j(U_iU_j)$, $\nabla P=\Pi[U]$, and $|\nabla U(0,0)|\ge c$. So GOAL holds.

Proof. $|U_n|\le1$ on the whole rescaled past; the smoothing lemma (with the fixed upper bound $M_n$ for the restarted
datum) gives $|\nabla^k\partial^l_\tau U_n|\le C_{k,l}$ for $\tau\ge-s_nM_n^2+\frac12$, and $s_nM_n^2\to\infty$.
Arzela-Ascoli and a diagonal argument give $C^k_{loc}$ convergence including $\tau=0$; $|\nabla U_n(0,0)|=D(s_n)/M_n^2\ge
c$ passes to the limit. The Duhamel identity passes to the limit by dominated convergence with the integrable majorant
$C(|y-z|+\sqrt{\tau-\sigma})^{-4}$, so $U$ is mild on $(a,0]$ for every $a$. The pressure is identified as in Section 2.
$\square$

### 4. The equivalence of $D/M^2\to0$ and $S/M\to0$

**Theorem 3.** $D/M^2\to0$ if and only if $S/M\to0$.

Proof. If $D/M^2\to0$, Lemma 1(c) gives $S/M\le\max(\sigma(0)/M,(GD/M^2)^{1/2})\to0$. Conversely, assume $S/M\to0$
and $\limsup D/M^2>0$, and take the limit $U$ of Theorem 2. Its swirl component vanishes. If the rescaled axis distance
$d_n=M_nr(x_n)$ has a bounded subsequence, extract convergence of the horizontal displacement vector to the rescaled axis;
rotations about the rescaled axis pass to the limit, so $U$ is axisymmetric and swirl free about the limiting axis, and
by KNSS Theorem 5.2 (bounded ancient weak solutions, axisymmetric without swirl, are $(0,0,b_3(t))$) and Remark 6.1
(mild implies $b$ constant) $U$ is constant, contradicting $|\nabla U(0,0)|\ge c$. If $d_n\to\infty$, rotating by the
angle $s/d_n$ shows $U(y+se)=U(y)$ for $e=\lim e_\theta(x_n)$, and $U\cdot e=0$; testing the weak formulation with
$(\psi_1\eta(y_e),0,\psi_2\eta(y_e))$, $\int\eta=1$, reduces it to the planar weak equation, KNSS Theorem 5.1 gives
$U=b(\tau)$, and mildness gives $b$ constant. Contradiction. $\square$

Remark. If $\limsup S/M>0$, swirl first crossings with $S_n\ge cM$ satisfy $c\le r_nS_n\le G$ (Lemma 1), and the
rescaling with length $r_n$, time $r_n/S_n$, amplitude $S_n$ has viscosity in $[1/G,1/c]$ and gives a bounded,
nonconstant, axisymmetric ancient mild Navier-Stokes limit with positive viscosity. This case is contained in
regime (I) by Lemma 1(c).

### 5. Regime II: Euler-scale compactness and the plateau alternative

Assume $D/M^2\to0$. For $t_n\uparrow T_*$, $M_n=M(t_n)$, $D_n=D(t_n)$, a scale $\ell_n\ge cM_n/D_n$, centers $x_n$,
times $s_n\le t_n$ with $s_nM_n/\ell_n\to\infty$, put
$$U_n(y,\tau)=M_n^{-1}u(x_n+\ell_ny,\,s_n+\tau\ell_n/M_n).$$
Then $U_n$ solves Navier-Stokes with unit nonlinear coefficient and viscosity $\nu_n=1/(M_n\ell_n)\le D_n/(cM_n^2)\to0$,
and $|U_n|\le1$. Call this an admissible isotropic normalization. Globally bounded rescalings must have amplitude
at least comparable to $M(s_n)$: if $U_n=B_n^{-1}(u(x_n+\ell_ny+V_nT_n\tau,s_n+T_n\tau)-V_n)$ with a constant Galilean
frame $V_n$, then $\sup|U_n|\ge M(s_n)/(2B_n)$, since $U_n\to-V_n/B_n$ at spatial infinity. This is only a lower bound
on $B_n$; if $B_n/M(s_n)\to\infty$, every limit is a constant, since the oscillation of $U_n$ is at most $2M(s_n)/B_n$ (the
constant is zero if $|V_n|=O(M(s_n))$, and may be nonzero: $V_n=B_ne_3$ gives $-e_3$), so a nonconstant limit needs $B_n$
comparable to $M(s_n)$. It
does not exclude bounded local limits of rescalings whose global bounds diverge (Section 9).

**Theorem 4 (uniform modulus; reduction to (UP)).** (a) If
$\bar\mu(\delta)=\limsup_n\omega_{t_n}(\delta\ell_n)/M_n\to0$ as $\delta\to0$ (automatic when $\ell_n=M_n/D_n$), then
along a subsequence $U_n\to U$ locally uniformly on $\mathbb R^3\times(-\infty,0]$, $\|U\|_\infty\le1$, and $U$ is a
weak Euler solution with canonical pressure $P=R_iR_j(U_iU_j)$, the time-integrated identity holding up to $\tau=0$.
For $\ell_n=M_n/D_n$, $U$ is Lipschitz and $\nabla P=\Pi[U]$. The swirl vanishes, and $U$ is axisymmetric about a limiting
axis (if $r(x_n)/\ell_n$ stays bounded) or planar (if it diverges).
(b) (Rigidity.) If such a limit is spatially constant at every time of an interval $I$, it is constant on $I$.
(c) (Reduction.) If there are $R,c>0$, times $s_n\le t_n$ and points with $\operatorname{osc}_{B_{RM_n/D_n}(x_n)}u(s_n)\ge
cM_n$, GOAL holds with $\ell_n=M_n/D_n$ centered at $(x_n,s_n)$. Hence GOAL holds unless
$$\text{(UP)}\qquad D/M^2\to0\quad\text{and}\quad\omega_t(RM(t)/D(t))/M(t)\to0\ \text{ for every }R<\infty,$$
and under (UP) every subsequential limit with $\ell_n=M_n/D_n$ is a space-time constant.

Proof. (a) With a mollifier $\rho_\epsilon$, $\partial_\tau(U_n*\rho_\epsilon)=-(U_n\otimes U_n)*\nabla\rho_\epsilon
-k_\epsilon*(U_n\otimes U_n)+\nu_nU_n*\Delta\rho_\epsilon$, where $k_\epsilon=\nabla R_iR_j\rho_\epsilon$ has
$\int k_\epsilon=0$ and $\|k_\epsilon\|_1\le C/\epsilon$. Hence $|U_n(y,\tau)-U_n(y,\tau')|\le2\hat\mu(\epsilon)+
C|\tau-\tau'|(\epsilon^{-1}+\nu_*\epsilon^{-2})$ with $\hat\mu=\sup_n\mu_n\to0$ and $\nu_*=\sup\nu_n$; choosing
$\epsilon=|\tau-\tau'|^{1/3}$ gives a uniform time modulus. Arzela-Ascoli and the pressure stability of Section 2 give
the limit equation; the viscous term vanishes. The swirl part is $o(1)$ by Theorem 3; the axis dichotomy is proved as in
Theorem 3 using only $C^0$ convergence. (b) For $U=b(\tau)$ both the flux divergence and the canonical pressure gradient
vanish, so $b'=0$. (c) $\|u(s_n)\|_\infty\ge cM_n/2$ forces $s_n\to T_*$ and depth $s_nD_n\to\infty$; the
oscillation passes to the limit at $\tau=0$ on $\bar B_R$. If (UP) fails in regime (II), the oscillation hypothesis holds,
since $\omega_t(\rho)\le2\sup_{s\le t,x}\operatorname{osc}_{B_\rho(x)}u(s)$. Under (UP) the limits have zero oscillation on every ball. $\square$

Two record certificates follow from (c): an energy certificate (if $D^3/M^5$ stays bounded along a subsequence of
velocity first crossings, Lemma 2 gives oscillation $M/2$ at a bounded number of Lipschitz lengths), and a temporal
certificate (if $M(t_n-A/D(t_n))\le\kappa M(t_n)$, $0<\kappa<1$, along velocity first crossings, the limit has
$|U(0,0)|=1>\kappa\ge\sup|U(\cdot,-A)|$, hence is nonconstant by (b)). Under (UP) both fail (Proposition 7). The
alternatives GOAL and (UP) are not proved to be mutually exclusive: under (UP) a normalization at a larger scale may
succeed.

**Level scales.** For $c\in(0,\frac12]$ let $\ell_c(t)=\min\{\rho:\omega_t(\rho)=cM(t)\}\in[cM/D,L_E]$. GOAL holds by
(a) with $\ell_n=\ell_c(t_n)$ and centers at near-maximizing increments, whenever $\liminf_n\ell_{c'}(t_n)/\ell_c(t_n)>0$
for every $c'<c$ (admissibility holds since $\ell_c\ge cM/D$ gives $\nu_n\to0$, and an increment at $(x_n,s_n)$ within a factor $1-o(1)$ of the maximal one
forces $\|u(s_n)\|_\infty\ge cM_n/4$ for large $n$, hence $s_n\to T_*$, so $\ell_c\le L_E$ gives depth $s_nM_n/\ell_n\to\infty$; given $c'<c$ there is $\delta'>0$ with
$\ell_{c'}(t_n)\ge\delta'\ell_c(t_n)$ for large $n$, and $\omega_{t_n}(\rho)<c'M_n$ for $\rho<\ell_{c'}(t_n)$, so $\bar\mu(\delta)\le c'$ for
$\delta<\delta'$; hence $\bar\mu(\delta)\to0$, which is the hypothesis of (a)); conversely, an admissible
normalization with the modulus hypothesis of Theorem 4(a) and sup oscillation $c$ on a ball $B_R$ forces this condition
at every level $\gamma<\min(c,\frac12)$. In regime (II), if for no sequence $t_n\to T_*$, no $c\in(0,\frac12]$ and no subsequence
the condition holds for every $c'<c$ (a sup-norm cascade: the historical modulus climbs through every fixed fraction of
$M$ across unboundedly many octaves of scale), then (UP) holds: otherwise there are $R$, $c\le\frac12$ and $t_n\to T_*$ with
$\omega_{t_n}(RM_n/D_n)\ge cM_n$, so $\ell_c(t_n)\le RM_n/D_n$ while $\ell_{c'}(t_n)\ge c'M_n/D_n$.

### 6. The $L^2$ reduction and the residual alternative

**Theorem 5 (main reduction).** (a) Let an admissible isotropic normalization satisfy, for all $R,A$,
$$\text{(L2M)}\qquad\lim_{\delta\to0}\limsup_n\sup_{-A\le\tau\le0}\sup_{|h|\le\delta}\int_{B_R}|U_n(y+h,\tau)-U_n(y,\tau)|^2dy=0.$$
Then along a subsequence $U_n\to U$ in $C([-A,0];L^2(B_R))$ for all $A,R$, $\|U\|_\infty\le1$, $U$ is a weak Euler
solution on $\mathbb R^3\times(-\infty,0]$ with canonical pressure, rigidity (Theorem 4(b)) applies, and the swirl and axis
dichotomy holds. If moreover, for some $R>0$ and $c>0$,
$$\text{(L2-OSC)}\qquad\liminf_n\int_{B_R}|U_n(y,0)-(U_n)_{B_R}(0)|^2dy\ge c>0,$$
then $U(\cdot,0)$ is nonconstant and GOAL holds.
(b) For every admissible isotropic normalization, along a subsequence $U_n\rightharpoonup^*\bar U$,
$U_n\otimes U_n\rightharpoonup^*\bar U\otimes\bar U+\mathcal R$, $\mathcal R\ge0$, and $(\bar U,\mathcal R)$ solves the
Euler-Reynolds system with pressure $R_iR_j(\bar U_i\bar U_j+\mathcal R_{ij})$; the convergence is strong in
$L^2_{loc}$ of space-time if and only if $\mathcal R=0$.
(c) Consequently, for every singular trajectory at least one of the following holds:
(A) regime (I), and GOAL holds with a nonconstant bounded ancient mild Navier-Stokes limit (Theorem 2);
(B) regime (II), and some admissible isotropic normalization satisfies (L2M) and (L2-OSC); GOAL holds with a bounded
nonconstant swirl-free ancient weak Euler limit with canonical pressure;
(C) regime (II), and every admissible isotropic normalization with (L2-OSC) fails (L2M).
The three cases are exhaustive and mutually exclusive ((C) is literally the negation of (B) within regime (II); it
holds vacuously if no admissible normalization retains $L^2$ oscillation).

Proof. (a) The pointwise bound on $\partial_\tau(U_n*\rho_\epsilon)$ uses only $|U_n|\le1$, and Minkowski's inequality
bounds $\|U_n-U_n*\rho_\epsilon\|_{L^2(B_R)}$ by the translation modulus on $B_{R+1}$. So the family is equicontinuous in
$C([-A,0];L^2(B_R))$ and pointwise precompact by the Riesz-Frechet-Kolmogorov theorem. Strong $L^2_{loc}$ convergence
and $|U_n|\le1$ give $U_n\otimes U_n\to U\otimes U$ in $L^1_{loc}$, hence (with the uniform bound, truncating test
functions) weak-* in $L^\infty$, and the pressure passes to the limit. The limit equation holds in time-integrated form
on $[a,b]$, $b\le0$, with endpoint terms converging by the $C_tL^2_{loc}$ convergence; rigidity holds because the local
variance is continuous in $\tau$. (b) On each compact subset of $\mathbb R^3\times(-\infty,0]$, which lies in the domain of $U_n$ for large $n$, bounded
sets of $L^\infty$ are weak-* compact; a diagonal subsequence gives $U_n\rightharpoonup^*\bar U$ and
$U_n\otimes U_n\rightharpoonup^*\bar U\otimes\bar U+\mathcal R$. For $\xi\in\mathbb R^3$ and $0\le\phi\in C_c$,
$\int\phi|U_n\cdot\xi|^2=\int\phi|\bar U\cdot\xi|^2+2\int\phi(\bar U\cdot\xi)((U_n-\bar U)\cdot\xi)+\int\phi|(U_n-\bar U)\cdot\xi|^2$, and the
middle term tends to $0$, so $\mathcal R\ge0$. In the weak form of the equation for $U_n$ against a test field
$\varphi\in C_c^\infty$, the terms $\int U_n\cdot\partial_\tau\varphi$ and $\int U_n\otimes U_n:\nabla\varphi$ pass to the weak-* limit,
$\nu_n\int U_n\cdot\Delta\varphi\to0$, and the pressure term is $\int R_iR_j(U_n^iU_n^j)\operatorname{div}\varphi=\int U_n^iU_n^jR_iR_j(\operatorname{div}\varphi)$, where
$\operatorname{div}\varphi(\cdot,\tau)$ lies in the Hardy space $\mathcal H^1$, which the Riesz transforms preserve, so
$R_iR_j(\operatorname{div}\varphi)\in L^1$ and this term also passes to the limit. This gives the Euler-Reynolds system with
pressure $R_iR_j(\bar U_i\bar U_j+\mathcal R_{ij})$. Finally, for $0\le\phi\in C_c$, $\int\phi|U_n-\bar U|^2=\int\phi|U_n|^2-2\int\phi U_n\cdot\bar U+\int\phi|\bar U|^2\to\int\phi\operatorname{tr}\mathcal R$,
and since $\mathcal R\ge0$ the convergence is strong in $L^2_{loc}$ if and only if $\mathcal R=0$. (c) Theorem 3 and (a). $\square$

Remarks. (i) For general bounded divergence-free families, strong space-time convergence need not determine the
terminal trace: $W_n=\chi(n\tau)\sin(ny_2)e_1$, with $\chi(0)=1$ and $\chi$ supported near $0$, converges strongly to
$0$ in $L^2_{loc}$ of space-time, retains terminal oscillation, and fails (L2M). This family is not an admissible
Navier-Stokes normalization (its time cutoff does not solve the heat equation). For admissible normalizations,
Proposition 14A(a) proves terminal strong convergence when the joint limit is defect-free and its weak limit is a
space-time constant; the corresponding terminal conclusion for a general nonconstant defect-free weak limit is not
established here (Theorem 12 obtains it only after a retrospective shift of the terminal time). No equivalence between
failure of (L2M) and a condition on Reynolds defects is proved for the fixed-trajectory class. Separately, a nonzero
divergence-free defect does not prevent the weak limit from solving Euler ($\cos(nr)e_z$ is a stationary Euler
sequence with defect $\frac12e_z\otimes e_z$). (ii) In (B) the center time need not be a
first crossing; (B) as stated is an existence statement, and Theorem 5' gives an explicit sufficient rule defined from
an observable. Throughout the Findings, "GOAL holds" in (B), (B*) and in Theorem 12 is meant in the sense of the
Convention in the Result: the analytic requirements hold, while the normalization is given existentially (or, in
Theorem 12, the end-time shift retrospectively).

**Theorem 5' ($L^2$ level-scale selection).** For $s<T_*$, $x\in\mathbb R^3$, $\rho>0$ let
$O(x,s,\rho)=\big(\fint_{B_\rho(x)}|u(y,s)-(u(s))_{B_\rho(x)}|^2dy\big)^{1/2}$ and $\Omega_t(\rho)=\sup_{s\le t}\sup_xO(x,s,\rho)$.
Then $\Omega_t$ is continuous, $\Omega_t(\rho)\le\min(M(t),2D(t)\rho)$, and for $\gamma\in(0,1]$ such that $\Omega_t$ reaches
$\gamma M(t)$ the level scale $\lambda_\gamma(t)=\min\{\rho>0:\Omega_t(\rho)=\gamma M(t)\}$ satisfies
$\gamma M/(2D)\le\lambda_\gamma\le(3E_0/(4\pi\gamma^2M^2))^{1/3}$ and $\Omega_t<\gamma M(t)$ on $(0,\lambda_\gamma)$. Assume regime (II)
and

(L2LS) there are $c\in(0,1]$ and $t_n\uparrow T_*$ such that $\lambda_c(t_n)$ is defined and
$\liminf_n\lambda_{c'}(t_n)/\lambda_c(t_n)>0$ for every $c'\in(0,c)$.

Let $\ell_n=\lambda_c(t_n)$ and choose $s_n\le t_n$ and $x_n$ with $O(x_n,s_n,\ell_n)\ge(1-\frac1n)cM(t_n)$. Then
$U_n(y,\tau)=M_n^{-1}u(x_n+\ell_ny,s_n+\tau\ell_n/M_n)$ is an admissible isotropic normalization satisfying (L2M) and
(L2-OSC) on $B_1$, so GOAL holds as in Theorem 5(a).

Proof. Bounds: $|u-(u)_B|\le2D\rho$ on $B_\rho$ and $\fint|u-(u)_B|^2=\fint|u|^2-|(u)_B|^2\le M^2$. Continuity: from
$\frac d{d\rho}\fint_{B_\rho}f=\frac3\rho(\fint_{\partial B_\rho}f-\fint_{B_\rho}f)$, $|\partial_\rho O^2|\le CM^2/\rho$ uniformly in $(x,s)$, and
$\Omega_t\le2D\rho$ near $0$. If $O(x,s,\rho)\ge\gamma M$ then $\|u(s)\|_\infty\ge\gamma M$ and
$E_0\ge\int_{B_\rho}|u(s)|^2\ge\frac{4\pi}3\rho^3\gamma^2M^2$. Translation bound: covering $B_r(z)$ by $C(r/|h|)^3$ balls
$B_{|h|}(z_i)$ and using $\int_{B_{|h|}(z_i)}|u(y+h)-u(y)|^2\le4\int_{B_{2|h|}(z_i)}|u-m_i|^2$ ($m_i$ the mean), one gets for
$|h|\le r$ and $s\le t$: $\fint_{B_r(z)}|u(y+h,s)-u(y,s)|^2dy\le C_0\Omega_t^*(2|h|)^2$, $\Omega^*_t(\rho)=\max_{\rho'\le\rho}\Omega_t(\rho')$
(a maximal $|h|$-separated set of centers has at most $27(r/|h|)^3$ points, so $C_0=864$ works). Now $\|u(s_n)\|_\infty\ge cM_n/2$ gives
$s_n\to T_*$; $\ell_n\le CM_n^{-2/3}$ gives depth $s_nM_n/\ell_n\to\infty$; $\ell_nD_n/M_n\ge c/2$ gives $\nu_n\to0$; (L2-OSC)
holds with constant $c^2(1-o(1))$. For (L2M), all physical times are $\le t_n$; given $c'<c$ and
$\kappa<\liminf\lambda_{c'}/\lambda_c$, for $|h|\le\delta<\kappa/2$ and $n$ large $2\delta\ell_n<\lambda_{c'}(t_n)$, hence
$\fint_{B_R}|U_n(y+h,\tau)-U_n(y,\tau)|^2dy\le C_0c'^2$; let $c'\to0$. $\square$

The rule is explicit in terms of the observable $O(x,s,\rho)$: the scale comes from $\Omega_t$ and $M(t)$, the center and
time from a near-maximizer of $O$ (the function $\Omega_t$ alone does not determine the center, since axial translates
of the solution have the same $\Omega_t$). It is defined without reference to any limit; it is not claimed to be
algorithmically computable with certified errors, and (L2LS), an asymptotic condition, cannot be certified from finitely
many observations. (L2LS) is sufficient for (B); it is not known to be necessary, because $\Omega_t$ is a supremum over all windows and past
times, so small-scale structures anywhere in the flow can make $\lambda_{c'}/\lambda_c\to0$ even if a good window exists
elsewhere. The sup-norm level-scale condition of Section 5 also implies (B). The split (A)/(II) is an asymptotic
predicate on the trajectory.

Remark (rules in (B)). (i) A rule exists once a modulus is fixed. Fix $\gamma>0$, $R_0$, an enumeration $j\leftrightarrow(k,R,A)$
of $\mathbb N^3$, and numbers $\mu_j\in[0,1]$ with $\mu_{j(k,R,A)}\to0$ as $k\to\infty$ for fixed $R,A$. For a datum $\zeta$
(a terminal time $s\le t$, a center and a scale, normalized with $M(t)$) let $e_j(\zeta)=m_\zeta(2^{-k};R,A)/(4|B_R|)\in[0,1]$, where
$m_\zeta(\delta;R,A)$ is the quantity in (L2M) for the single rescaling $\zeta$, if $[-A,0]$ lies in its time domain, and
$e_j(\zeta)=1$ otherwise; let $J(\zeta)=\sup_j2^{-j}(e_j(\zeta)-\mu_j)_++\min(1,\nu_\zeta)+(1+d_\zeta)^{-1}$ with $\nu_\zeta$ the viscosity and
$d_\zeta$ the depth, and let $e(t)$ be the infimum of $J$ over data at $t$ with terminal oscillation at least $\gamma$ on
$B_{R_0}$. If an admissible sequence at times $t_n$ has terminal oscillation at least $\gamma$ on $B_{R_0}$ and
$\limsup_ne_j\le\mu_j$ for every $j$, then $e(t_n)\to0$, since each term tends to $0$ and the terms with $j\ge N$ are at most
$2^{-N}$. Conversely, data $\zeta'_n$ at times $t'_n\uparrow T_*$ with that oscillation and $J(\zeta'_n)\to0$ are admissible
($\nu\to0$, depth $\to\infty$, and $\sigma=\ell D/M$ is bounded below, since $|\nabla U(\cdot,0)|\le\sigma$ gives
$\gamma\le\int_{B_{R_0}}|U(y,0)-U(0,0)|^2dy\le\frac35|B_{R_0}|R_0^2\sigma^2$), have $\limsup_ne_j(\zeta'_n)\le\mu_j$, hence (L2M) by monotonicity of $m$ in $\delta,R,A$, and
(L2-OSC). So near-minimizers of the explicit observable $J$ give GOAL whenever (B) holds with a modulus dominated by
$(\mu_j)$; what (B) does not supply is the modulus. (ii) No fixed countable list of moduli dominates all moduli up to
constants: given moduli $\mu^{(i)}$, choose $\delta_j\downarrow0$ with $\max_{i\le j}\mu^{(i)}(\delta_j)<j^{-2}$ and let $\mu=1/j$ on
$(\delta_{j+1},\delta_j]$; then $\mu(\delta_j)>j\mu^{(i)}(\delta_j)$ for $j\ge i$. (iii) (L2LS) cannot be localized by taking suprema over
small balls in a window: with a cutoff $\chi$ ($0\le\chi\le1$, $\chi=1$ on $[-1,1]$, supported in $[-2,2]$) and
$\epsilon_n\to0$, the shears $F_n=[\frac12\sin y_2+\frac18\chi(y_2/\epsilon_n)\sin(y_2/\epsilon_n^2)]e_1$ (stationary Euler solutions, not
rescalings of one Navier-Stokes solution) satisfy $m_{F_n}(\delta;R,A)\le C_R(\delta^2+\epsilon_n)$, so (L2M) holds with
terminal oscillation, while the standard deviation on balls $B_r(a)$, $a\in B_1$, is at most $r/2+\frac18$ for every $r$
and exceeds $\frac1{32}$ at $a=0$, $r=\pi\epsilon_n^2$ for large $n$ (there $\chi=1$, the mean is $0$, both sines have the sign
of $y_2$, and the ball average of $\sin^2(y_2/\epsilon_n^2)$ is $\frac12+\frac3{8\pi^2}$, so the standard deviation is at least
$\frac18(\frac12+\frac3{8\pi^2})^{1/2}$); since the standard deviation is continuous in $r$ and tends to $0$ as $r\to0$, the smallest radius with standard deviation $\frac1{32}$ on some
such ball is at most $\pi\epsilon_n^2$, and the smallest radius with standard deviation $\frac14$ is at least $\frac14$.
Whether a rule without a modulus parameter exists in (B) is open.

### 6A. Defect-free normalizations and the flat alternative

This subsection weakens the sufficient condition of Theorem 5(a), at the price of a weaker topology and of an end-time
shift. Let
$$\text{(ST)}\qquad U_n\to U\ \text{in }L^2(B_R\times(-A,0))\ \text{for all }R,A,\quad\text{and}\quad U_n(\cdot,0)\to U(\cdot,0)\ \text{in }L^2(B_R)\ \text{for all }R .$$
Fix a radial mollifier $\rho\in C_c^\infty(B_1)$ ($\rho\ge0$, $\int\rho=1$), $\rho_\epsilon=\epsilon^{-3}\rho(\cdot/\epsilon)$, $f^\epsilon=f*\rho_\epsilon$ (in space).

**Lemma 11 (weak limits at every time).** Let $(U_n)$ be an admissible isotropic normalization. Along a subsequence,
$U_n\rightharpoonup^*\bar U$ in $L^\infty(\mathbb R^3\times(-\infty,0))$, and for every $\tau\le0$, $U_n(\cdot,\tau)\rightharpoonup^*W(\tau)$
in $L^\infty(\mathbb R^3)$, where $W(\tau)=\bar U(\cdot,\tau)$ for a.e. $\tau$, $\tau\mapsto\int W(\tau)\cdot\phi$ is continuous for every
$\phi\in L^1(\mathbb R^3)$, and $U_n^\epsilon\to W^\epsilon$ locally uniformly on $\mathbb R^3\times(-\infty,0]$ for every $\epsilon>0$.
If for some $\epsilon,R,c>0$ and $\tau_n\in[-A,0]$
$$\text{(W-OSC)}\qquad\liminf_n\int_{B_R}|U_n^\epsilon(y,\tau_n)-(U_n^\epsilon(\tau_n))_{B_R}|^2dy\ge c,$$
then $W(\tau_*)$ is not a.e. constant for some $\tau_*\in[-A,0]$.

Proof. By the proof of Theorem 4(a), which uses only $|U_n|\le1$ and the canonical pressure, $|U_n^\epsilon|\le1$,
$|\nabla U_n^\epsilon|\le C/\epsilon$ and $|\partial_\tau U_n^\epsilon|\le C(\epsilon^{-1}+\nu_*\epsilon^{-2})$. Arzela-Ascoli and a diagonal
argument give a subsequence with $U_n^{1/k}\to V^{1/k}$ locally uniformly for every $k$, and $U_n\rightharpoonup^*\bar U$. For
$\phi\in C_c^\infty$, $|\int(U_n(\tau)-U_n^{1/k}(\tau))\cdot\phi|\le\|\phi-\phi*\rho_{1/k}\|_1=:e_k(\phi)\to0$ uniformly in $n,\tau$, so
$\int U_n(\tau)\cdot\phi$ is Cauchy for every $\tau$; by density and $|U_n|\le1$ this defines $W(\tau)$ with
$U_n(\tau)\rightharpoonup^*W(\tau)$. Then $W(\tau)^{1/k}=V^{1/k}(\tau)$, and $\int W(\tau)\cdot\phi$ is the uniform limit of the continuous
functions $\int V^{1/k}(\tau)\cdot\phi$. Testing with $\chi(\tau)\phi(y)$ and dominated convergence in $\tau$ gives $W=\bar U$ a.e.
For general $\epsilon$ the equicontinuous sequence $U_n^\epsilon$ can only have the limit $W^\epsilon$, so it converges. Under
(W-OSC) take $\tau_n\to\tau_*$; by equicontinuity $\int_{B_R}|W^\epsilon(\tau_*)-(W^\epsilon(\tau_*))_{B_R}|^2\ge c$, so $W(\tau_*)$ is
not a.e. constant. $\square$

We write $\bar U(\tau)$ for $W(\tau)$ at every $\tau$, and $\mathcal R$ for the Reynolds defect of Theorem 5(b).

**Theorem 12 (defect-free reduction).** Assume regime (II), let $(U_n)$ be admissible with a joint subsequence on which
the conclusions of Lemma 11 and of Theorem 5(b) both hold, and suppose $\mathcal R=0$ and $\bar U(\tau_*)$ is not a.e. constant for some $\tau_*\le0$. Then there are
an open interval $J\subset(-\infty,0)$, a set $E\subset J$ of full measure and a further subsequence such that for every
$\tau_0\in E$ the shifted normalization $U'_n(y,\tau)=U_n(y,\tau+\tau_0)$ (terminal time $s_n'=s_n+\tau_0\ell_n/M_n$; same
$t_n,x_n,\ell_n$) is admissible and $U'_n\to U'=\bar U(\cdot+\tau_0)$ in the sense (ST); $|U'|\le1$; $U'(\cdot,0)$ is not a.e.
constant; $U'$ is a weak Euler solution on $\mathbb R^3\times(-\infty,0]$ with canonical pressure $P'=R_iR_j(U'_iU'_j)$ in the
time-integrated form with endpoint terms at every $a<b\le0$; and the swirl and axis dichotomy of Theorem 4(a) holds.
So the analytic requirements of GOAL hold in the topology (ST) with the terminal time $s'_n$; since $\tau_0$ is chosen
from the weak limit, this extraction does not by itself meet the selection requirement (see after the proof).

Proof. By Theorem 5(b), $\mathcal R=0$ gives strong convergence on $B_R\times(-A,-\delta)$ for every $\delta>0$; since
$|U_n-\bar U|\le2$, the strip contributes $\int_{-\delta}^0\int_{B_R}|U_n-\bar U|^2\le4|B_R|\delta$, so
$\int_{-A}^0\|U_n(\tau)-\bar U(\tau)\|_{L^2(B_R)}^2d\tau\to0$ for all $R,A$. Choose $n_j$ with
$\int_{-j}^0\|U_{n_j}(\tau)-\bar U(\tau)\|_{L^2(B_j)}^2d\tau\le4^{-j}$; for each $k$, $\|U_{n_j}(\tau)-\bar U(\tau)\|_{L^2(B_k)}\to0$ for a.e.
$\tau\in(-k,0)$ (summability); let $E_0$ be the full-measure set where this holds for all $k$. The limit equation: in the
integrated identity for $U_n$ the endpoint terms converge by Lemma 11, $U_n\otimes U_n\to\bar U\otimes\bar U$ in $L^1_{loc}$, the
pressure term $\int\!\!\int(U_n\otimes U_n):R_iR_j(\nabla\cdot\phi)$ converges by weak-* convergence because
$R_iR_j\nabla\cdot\phi\in L^1$ ($\nabla\cdot\phi(\tau)$ lies in the Hardy space $\mathcal H^1$), and the viscous term is $O(\nu_n)$. The set
$N=\{\tau:\bar U(\tau)\text{ not a.e. constant}\}=\bigcup_{\psi,j}\{\tau:\int\bar U(\tau)\cdot\partial_j\psi\ne0\}$ is relatively open by
weak continuity, and nonempty, so it contains an open interval $J\subset(-\infty,0)$. For $\tau_0\in E=E_0\cap J$:
admissibility holds since $s'_n\le s_n$ and $s'_nM_n/\ell_n=s_nM_n/\ell_n+\tau_0\to\infty$; the space-time convergence is the
shifted $L^2$ convergence; the terminal slice converges in $L^2(B_k)$ for all $k$ because $\tau_0\in E_0$; $\bar U(\tau_0)$ is
nonconstant because $\tau_0\in N$. The swirl part is $\le S(t_n)/M_n\to0$ and the axis dichotomy passes in $L^2_{loc}$. $\square$

The shift $\tau_0$ is chosen after the subsequence and the weak limit are known (from a full-measure subset of an
interval determined by the weak limit, any element of which works), and the terminal time is no longer the time at
which oscillation was recorded. This is a genuine weakening relative to Theorem 5(a). Theorem 17 and Corollary 18 in
Section 9A replace this choice, and the anchor, by rules applied to each trajectory. A hypothesis of Theorem 5(a) and
(L2-OSC) imply those of Theorem 12. In the defect-free case $\mathcal R=0$, if $\bar U$ is spatially constant at every time, it is a space-time
constant: with $\bar U(\tau)=b(\tau)$, the identity tested with $\chi(\tau)\psi(y)$ gives $b'=0$, since the flux and the
canonical pressure of a constant field are constant. With a nonzero bounded defect the same conclusion follows instead
from the large-ball argument of Proposition 14(e).

**Corollary 13 (refined residual alternative).** In regime (II), GOAL in the sense of Theorem 12 holds unless
(C*): for every admissible isotropic normalization and every joint subsequence as in Theorem 12, either $\bar U(\tau)$ is
a.e. constant for every $\tau$, or $\mathcal R$ is not a.e. zero. (C*) implies alternative (C) of Theorem 5. The exhaustive
and mutually exclusive alternatives in this weaker sense are (A); (B*): regime (II) and some admissible joint
subsequential limit has $\mathcal R=0$ and $\bar U(\tau_*)$ not a.e. constant for some $\tau_*$; and (C*). GOAL holds in (A),
and in the sense of Theorem 12 in (B*); alternative (B) of Theorem 5 implies (B*). One may not keep (B) and replace only
(C) by (C*), since a trajectory in (C) but not in (C*) is not excluded; it belongs to (B*). "Smaller" means
containment; strict containment for actual singular trajectories is not established. By Corollary 18, GOAL holds in (B*)
in the topology (ST) also with re-anchoring and terminal-time rules applied to each trajectory, without the
retrospective shift; these rules start from a (B*) normalization that is itself only shown to exist.

Proof. If (C*) fails, some admissible joint subsequential limit has $\mathcal R=0$ and a weak limit not a.e. constant at
some time, which is (B*), and Theorem 12 applies. If (B) holds, the normalization of (B) has, by Theorem 5(a), strong
convergence, hence $\mathcal R=0$, and a nonconstant limit by (L2-OSC), so (C*) fails. $\square$

**Proposition 14 (the flat alternative).** For $\epsilon\in(0,1]$ let
$O_\epsilon(x,s,\rho)=(\fint_{B_\rho(x)}|u^{\epsilon\rho}(s)-(u^{\epsilon\rho}(s))_{B_\rho(x)}|^2)^{1/2}$, $\Theta_\epsilon(t)=\sup\{O_\epsilon(x,s,\rho):s\le t,x,\rho>0\}$, and
$$\text{(FLAT)}\qquad\Theta_\epsilon(t)/M(t)\to0\ \text{ as }t\uparrow T_*,\ \text{ for every }\epsilon\in(0,1].$$
(a) (FLAT) holds iff every admissible isotropic normalization has only weak limits $\bar U$ that are a.e. constant at
every time. Hence (C*) is the disjoint union of (FLAT) and (C*-D): (FLAT) fails, and every joint subsequential limit
with a weak limit that is nonconstant at some time has $\mathcal R$ not a.e. zero.
(b) $\omega_t(RM/D)/M\le CR^{3/5}(\Theta_{\epsilon/2}(t)/M(t))^{2/5}+2\epsilon R$; so (FLAT) implies (UP).
(c) $\Theta_\epsilon(t)\le C\sup_{s\le t}\|u(s)\|_{BMO}$; so historical BMO $=o(M)$ implies (FLAT).
(d) Let $\delta(t)=M(t)^{-1}\sup\{|(u(s))_{B_\rho(x)}-(u(s))_{B_{2\rho}(x)}|:s\le t,x,\rho>0\}$. Then
$\delta(t)\le\sqrt8\,\Theta_\epsilon(t)/M(t)+6\epsilon$ for every $\epsilon$, and
$\frac1{2\delta(t)}-1\le\frac13\log_2\big(768E_0D(t)^3/(\pi M(t)^5)\big)$. At a velocity record $|u(x_*,t)|=M(t)$ the means
$m_k$ of $u(t)$ over $B_{r_k}(x_*)$, $r_k=2^kM/(4D)$, satisfy $|m_k-u(x_*,t)|\le M/4+k\delta M$. Under (FLAT), therefore,
$E_0D^3/M^5\to\infty$, and at every velocity record the mean velocity stays within $M/2$ of the record value on all balls
of radius up to $2^{1/(4\delta)}M/(4D)$: the plateau extends over a number of octaves above the Lipschitz scale that
tends to infinity.
(e) Under (FLAT), for every admissible isotropic normalization and every joint subsequence as in Theorem 5(b) and
Lemma 11, there is one vector $b$, $|b|\le1$, with $W(\tau)=b$ for every $\tau\le0$ and $\bar U=b$; the defect
$\mathcal R=\operatorname{w*lim}(U_n-b)\otimes(U_n-b)$ satisfies $\nabla\cdot\mathcal R+\nabla R_iR_j\mathcal R_{ij}=0$, i.e.
$\iint\mathcal R:\nabla\varphi=0$ for every divergence-free test field $\varphi$. If $s_n=t_n$ is a record time,
$|u(x_n,t_n)|=M_n$ and $\ell_n=\lambda M_n/D_n$ with $\lambda>0$ fixed, then $u(x_n,t_n)/M_n\to b$, so $|b|=1$, and moreover
$\mathcal R=0$ and $U_n(\tau)\to b$ strongly in $L^2_{loc}$ for every $\tau\le0$: under (FLAT) the record-centred normalizations
at fixed multiples of the gradient scale converge strongly to a constant (a trivial limit). If
$\operatorname{dist}(x_n,\text{axis})/\ell_n\to0$ (any admissible normalization), then $b\parallel e_z$. Nonconstant
defects are compatible with these constraints: with $V$ the Beltrami (ABC) field
$3^{-1/2}(\sin z_3+\cos z_2,\sin z_1+\cos z_3,\sin z_2+\cos z_1)$ and $\theta\in C_c^\infty$, the bounded divergence-free fields
$Z_n=\nabla\times(\theta n^{-1}V(ny))$ converge weakly to $0$ with $Z_n\otimes Z_n\rightharpoonup^*\frac13\theta^2I$, and
$\nabla\cdot(\frac13\theta^2I)$ is a gradient (a kinematic example, not a Navier-Stokes trajectory).

Proof. (a) If (FLAT) fails there are $\epsilon,c>0$, $t_n\uparrow T_*$, $s_n\le t_n$, $x_n$, $\rho_n$ with $O_\epsilon(x_n,s_n,\rho_n)\ge cM_n$.
Since $O_\epsilon\le\min(2D\rho,\|u(s)\|_\infty)$: $\rho_n\ge cM_n/(2D_n)$, $\|u(s_n)\|_\infty\ge cM_n$, so $s_n\to T_*$; by Jensen
$c^2M_n^2|B_{\rho_n}|\le E_0$, so $\rho_n\to0$ and the depth diverges. The normalization at $(t_n,s_n,x_n,\rho_n)$ is admissible
and satisfies (W-OSC) at $\tau=0$ with $R=1$, because $U_n^\epsilon(y,0)=M_n^{-1}u^{\epsilon\rho_n}(x_n+\rho_ny,s_n)$; Lemma 11 applies.
Conversely, under (FLAT), for any admissible $(U_n)$, $\epsilon\in(0,1]$ and $R\ge1$ (so that $\epsilon/R\in(0,1]$), $\fint_{B_R}|U_n^\epsilon(\tau)-(U_n^\epsilon(\tau))_{B_R}|^2=
O_{\epsilon/R}(x_n,s_n+\tau\ell_n/M_n,R\ell_n)^2/M_n^2\to0$ uniformly in $\tau\in[-A,0]$, so every $W^\epsilon(\tau)$ is constant on every
ball, and $W(\tau)=\lim_{\epsilon\to0}W^\epsilon(\tau)$ in $L^1_{loc}$ is constant. (b) Put $\rho=RM/D$, $\delta=\epsilon\rho$, $v=u^\delta(s)$.
Then $|u(s)-v|\le D\delta=\epsilon RM$, and for $|h|\le\rho$, $\theta=|v(x+h)-v(x)|\le D\rho$. With $m$ the mean of $v$ on
$B_{2\rho}(x)$, one of $p\in\{x,x+h\}$ has $|v(p)-m|\ge\theta/2$, hence $|v-m|\ge\theta/4$ on $B_{\theta/(4D)}(p)\subset B_{2\rho}(x)$, so
$O_{\epsilon/2}(x,s,2\rho)^2\ge(\theta/4)^2(\theta/(8D\rho))^3$; that is $\theta\le C(D\rho)^{3/5}\Theta_{\epsilon/2}^{2/5}$, and
$|u(x+h,s)-u(x,s)|\le\theta+2\epsilon RM$. (c) For $\delta\le\rho$, Jensen gives $\fint_{B_\rho}|u^\delta-m|^2\le8\fint_{B_{2\rho}}|u-m|^2$;
take $m=(u)_{B_{2\rho}}$ and use the John-Nirenberg inequality. (d) With $v=u(s)*\rho_{2\epsilon\rho}$:
$|(v)_{B_\rho}-(v)_{B_{2\rho}}|\le(\fint_{B_\rho}|v-(v)_{B_{2\rho}}|^2)^{1/2}\le\sqrt8\,O_\epsilon(x,s,2\rho)$, and for $r\in\{\rho,2\rho\}$,
$|(v)_{B_r}-(u)_{B_r}|\le\|u(s)\|_\infty\sup_{|z|\le2\epsilon\rho}|B_r(x-z)\triangle B_r(x)|/|B_r|\le3\epsilon M$, using
$|B_r(a)\triangle B_r(b)|\le2\pi r^2|a-b|$. At a record time, $|u-u(x_*,t)|\le Dr_0=M/4$ on $B_{r_0}(x_*)$, which gives the bound on
$m_k$; for $k\le K=\lceil1/(2\delta)\rceil-1$ it gives $|m_k|\ge M/4$, while $|m_k|^2\le\fint_{B_{r_k}}|u|^2\le3E_0/(4\pi r_k^3)$, so
$r_K^3\le12E_0/(\pi M^2)$, i.e. $2^{3K}\le768E_0D^3/(\pi M^5)$ ($\delta>0$, since otherwise all ball means vanish and $u\equiv0$). For a
general $t$ use the last record time $t'\le t$, where $M(t')=M(t)$, $D(t')\le D(t)$, $\delta(t')\le\delta(t)$. For a non-dyadic
radius $r\le2^qr_0$, $q=1/(4\delta)$: $\fint_{B_a(x_*)}|u-u(x_*,t)|\le\frac34Da$ gives
$|m(r)-u(x_*,t)|/M\le\frac3{16}2^{q-j}+j\delta$ for every integer $j\ge0$, and $j=0$ ($q\le1$), $j=1$ ($1\le q\le2$), $j=\lceil q\rceil$
($q\ge2$) make this at most $1/2$ (by convexity in $q$, respectively in $j-q\in[0,1)$, with $\delta\le1/8$). (e) By (a), $W(\tau)=b(\tau)$ is a.e. constant in space, and $b$ is
continuous in $\tau$ by Lemma 11. Then $\bar U\otimes\bar U$ and $R_iR_j(\bar U_i\bar U_j)$ do not depend on $y$, and the
Euler-Reynolds system reads $\partial_\tau b+\nabla\cdot\mathcal R+\nabla R_iR_j\mathcal R_{ij}=0$. Test with $\chi(\tau)\psi(y/L)$:
the left side gives $-L^3\int b\chi'\,d\tau\cdot\int\psi$, while $\|\nabla(\psi(\cdot/L))\|_{L^1}=L^2\|\nabla\psi\|_{L^1}$ and, as Riesz
transforms commute with dilations, $\|R_iR_j\nabla\cdot(\psi(\cdot/L))\|_{L^1}=L^2\|R_iR_j\nabla\cdot\psi\|_{L^1}$; with $|\mathcal R|\le4$ the
defect and pressure terms are $O(L^2)$. Letting $L\to\infty$ gives $b'=0$. Conversely, if $\iint\mathcal R:\nabla\varphi=0$ for
divergence-free $\varphi$, then for $A=\int\chi\mathcal R\,d\tau$ the field $F=\nabla\cdot A+\nabla R_iR_jA_{ij}$ is curl free (test with
$\chi\nabla\times\zeta$) and divergence free ($\Delta R_iR_j=-\partial_i\partial_j$), hence harmonic; averaging over balls of radius $L$
with a radial mollifier and the same $L^1$ scaling give $|F|\le C\|A\|_\infty/L$, so $F=0$. In the record-centred case, fix
$\eta\in(0,1]$ and chain the means over $B_{2^{-j}\ell_n}(x_n)$, $0\le j\le J=\max(0,\lceil\log_2(\lambda/\eta)\rceil)$: the innermost is within
$\eta M_n$ of $u(x_n,t_n)$ by the Lipschitz bound, consecutive ones differ by at most $\delta(t_n)M_n$, where $\delta(t_n)\to0$ by (d),
and $(U_n(0))_{B_1}\to b$ by Lemma 11 (weak convergence at the fixed time $\tau=0$). So $U_n(0,0)\to b$, $|b|=1$. As $|U_n|\le1$
on the window, $1+\operatorname{tr}\mathcal R=\operatorname{w*lim}|U_n|^2\le1$, so $\mathcal R=0$, and
$\int_B|U_n(\tau)-b|^2\le\int_B(2-2b\cdot U_n(\tau))\to0$ for every ball $B$ and every $\tau\le0$. Near the axis, the
horizontal part of an axisymmetric field has zero mean on balls centred on the axis, and moving the centre by $d$
changes a mean over $B_\ell$ by at most $\frac32(d/\ell)\|u\|_\infty$. $\square$

(FLAT) says that at every scale the velocity resolved at a fixed relative resolution has oscillation $o(M)$, so that no
band of boundedly many octaves carries amplitude-$M$ structure; by (d) a flat singularity would carry, at every velocity
record, an approximately uniform jet over unboundedly many octaves, with the mean drifting by $o(M)$ per octave (a
logarithmic profile). The Gaussian lacunary profile of Section 10 is a candidate single-time model of this behaviour; that it satisfies
the single-time form of (FLAT) uniformly over all windows has not been proved.

**Remark (a defect is not excluded by the limit equation).** Let $\nu_n\to0$, $A>0$, $k_n\to\infty$ with $\nu_nk_n^2A\to0$,
$\chi\in C_c^\infty$, $0\le\chi\le1$, $\chi\not\equiv0$. (i) $U_n=(f_n(y_2,\tau),0,0)$, with $f_n$ the heat flow at viscosity $\nu_n$ on $[-A,0]$ of
$\tanh y_2+\frac12\chi(y_2)\sin(k_ny_2)$, is an exact Navier-Stokes solution with zero pressure ($(U_n\cdot\nabla)U_n=0$),
$|U_n|\le\frac32$ and $\|f_n(\tau)-f_n(-A)\|_\infty\le C_\chi\nu_nA(1+k_n^2)\to0$; its weak limit $(\tanh y_2,0,0)$ is nonconstant and its defect
$\mathcal R_{11}=\frac18\chi(y_2)^2$ is nonzero. (ii) The swirl-free axisymmetric pipe flows $U_n=w_n(r,\tau)e_z$, $w_n$ the
two-dimensional heat flow of $\chi(r)\cos(k_nr)$ ($\chi$ supported in $1<r<2$), have zero pressure, weak limit $0$ and
$\mathcal R_{zz}=\frac12\chi(r)^2$. So boundedness, the limit equation with canonical pressure and vanishing viscosity do not
exclude either branch of (C*); information specific to the singular trajectory is needed. These families have infinite
energy and are not rescalings of one solution; they are not counterexamples.

**Proposition 14A (homogeneous defect tangents and the unmollified flat alternative).** Assume regime (II). Let
$O_0(x,s,\rho)=(\fint_{B_\rho(x)}|u(s)-(u(s))_{B_\rho(x)}|^2)^{1/2}$ (no mollification) and
$\Theta_0(t)=\sup\{O_0(x,s,\rho):s\le t,x,\rho>0\}$; by the John-Nirenberg inequality $\Theta_0(t)$ is comparable to
$\sup_{s\le t}\|u(s)\|_{BMO}$. Let
$$\text{(FLAT}_0)\qquad\Theta_0(t)/M(t)\to0\ \text{ as }t\uparrow T_*,$$
and let (HD) be the statement that some admissible isotropic normalization has a joint subsequence (as in Theorem 12)
with $\mathcal R$ not a.e. zero.
(a) For every admissible isotropic normalization, every $0\le\chi\in C_c^\infty(\mathbb R^3)$ and every constant vector
$b$ with $|b|\le1$, the function $e_n(\tau)=\int\chi|U_n(y,\tau)-b|^2dy$ satisfies $e_n'\le C_\chi$ on its interval of
definition for all large $n$, with $C_\chi$ independent of $n$, $b$ and $\tau$. Consequently, if a joint subsequence has
$\mathcal R=0$ and $\bar U\equiv b$, then $U_n(\cdot,0)\to b$ in $L^2_{loc}$, so $U_n\to b$ in (ST).
(b) If a joint subsequence of an admissible normalization has $\mathcal R$ not a.e. zero, then $\sigma_n=\ell_nD_n/M_n\to\infty$
along it, and there are $(y_0,\tau_0)$ with $\tau_0<0$, $\delta_j\downarrow0$ and indices $n_j\uparrow\infty$ such that
$V_j(y,\tau)=U_{n_j}(y_0+\delta_jy,\tau_0+\delta_j\tau)$, which is the admissible isotropic normalization of the same
solution with the same $t_{n_j}$ and $M_{n_j}$, center $x_{n_j}+\ell_{n_j}y_0$, scale $\delta_j\ell_{n_j}$ and terminal time
$s_{n_j}+\tau_0\ell_{n_j}/M_{n_j}$, has the following properties: $V_j\rightharpoonup^*b$ and
$V_j\otimes V_j\rightharpoonup^*b\otimes b+R_0$ with a constant vector $b$ and a constant matrix $R_0\ge0$, $R_0\ne0$,
$|b|^2+\operatorname{tr}R_0\le1$; for every $\tau\le0$ and $R>0$, $V_j(\cdot,\tau)\rightharpoonup^*b$ and
$\int_{B_R}|V_j(y,\tau)-(V_j(\tau))_{B_R}|^2dy\to|B_R|\operatorname{tr}R_0$, so $(V_j)$ satisfies (L2-OSC), fails (L2M), and has
no subsequence converging in (ST); $V_j^\epsilon\to b$ locally uniformly on $\mathbb R^3\times(-\infty,0]$ for every $\epsilon>0$;
the rescaled distance of the new centers from the axis tends to infinity; and in a limiting frame $(e_1,e_2,e_3)$, with
$e_1$ a limit of the radial directions at the new centers and $e_3=e_z$, one has $b\cdot e_2=0$ and $R_0e_2=0$.
(c) (C*) is the disjoint union of (FLAT$_0$) and of (C*)$\cap$(HD). (FLAT$_0$) holds if and only if every joint
subsequential limit of every admissible isotropic normalization has $\mathcal R=0$ and $\bar U$ equal to a space-time
constant; then no admissible normalization satisfies (L2-OSC), and (C) holds vacuously. (FLAT$_0$) implies (FLAT),
(C*-D) is contained in (HD), and within (C*), (HD) holds if and only if $\limsup_{t\uparrow T_*}\Theta_0(t)/M(t)>0$.

Proof. (a) Put $z=U_n-b$. Since $b$ is constant, $\partial_\tau z+U_n\cdot\nabla z+\nabla P_n=\nu_n\Delta z$ and
$\operatorname{div}z=0$, with the canonical pressure $P_n=R_iR_j(U_{n,i}U_{n,j})$. Multiplying by $2\chi z$ and integrating by
parts gives, for every function $c(\tau)$,
$e_n'=\int|z|^2U_n\cdot\nabla\chi+2\int(P_n-c)z\cdot\nabla\chi+\nu_n\int|z|^2\Delta\chi-2\nu_n\int\chi|\nabla U_n|^2$, since
$\int z\cdot\nabla\chi=0$. As $|U_n|\le1$, $\|P_n(\tau)\|_{BMO}\le C$, so $\|P_n(\tau)-c(\tau)\|_{L^2(\operatorname{supp}\chi)}\le C_\chi$ for
$c(\tau)$ the mean of $P_n(\tau)$ over a fixed ball containing $\operatorname{supp}\chi$ (John-Nirenberg); with $|z|\le2$ and $\nu_n\le1$ the first three terms are at most $C_\chi$ and the last is nonpositive.
Hence $e_n(\tau')\le e_n(\tau)+C_\chi(\tau'-\tau)$ for $\tau<\tau'$, and for $h>0$
$$\frac1h\int_\tau^{\tau+h}e_n-\frac{C_\chi h}2\le e_n(\tau)\le\frac1h\int_{\tau-h}^\tau e_n+\frac{C_\chi h}2,$$
the left inequality whenever $\tau+h$ lies in the interval of definition. If $\mathcal R=0$ and $\bar U\equiv b$, the first
step of the proof of Theorem 12 gives $\int_{-A}^0e_n\to0$ for every $A$, and the right inequality at $\tau=0$ gives
$\limsup_ne_n(0)\le C_\chi h/2$ for every $h>0$.
(b) If $\sigma_n\le C$ along a further subsequence, then $|\nabla U_n|\le C$ and $|U_n-U_n^\epsilon|\le C\epsilon$; with the bounds
on $U_n^\epsilon$ from the proof of Lemma 11 the sequence is equicontinuous on compact subsets of
$\mathbb R^3\times(-\infty,0]$ up to $C\epsilon$, for every $\epsilon$, so a further subsequence converges locally uniformly,
$U_n\otimes U_n\to\bar U\otimes\bar U$ in $L^1_{loc}$, and $\mathcal R=0$, a contradiction. Pass to a subsequence along which the
rescaled axes $\mathcal A_n=\{y:x_n+\ell_ny\in\text{axis}\}$ converge to a vertical line $\mathcal A$ or leave every compact
set. With $Q=\operatorname{w*lim}U_n\otimes U_n$, $\operatorname{tr}\mathcal R>0$ on a set of positive measure in
$\mathbb R^3\times(-\infty,0)$ and $\mathcal A\times\mathbb R$ is a null set, so there is a common Lebesgue point $(y_0,\tau_0)$ of
$\bar U$ and $Q$ (for Euclidean balls in $\mathbb R^4$) with $\tau_0<0$, $y_0\notin\mathcal A$ and $\operatorname{tr}R_0>0$, where
$b=\bar U(y_0,\tau_0)$ and $R_0=Q(y_0,\tau_0)-b\otimes b$. Fix a countable dense set $\{\phi_k\}$ in $C_c(\mathbb R^3\times\mathbb R)$,
choose $\delta_j\downarrow0$ with $\tau_0+\delta_j\tau<\tau_0/2$ on the supports of $\phi_1,\dots,\phi_j$, and then $n_j>n_{j-1}$ with
$\delta_j\sigma_{n_j}\ge j$, $\nu_{n_j}\le\delta_j/j$, $s_{n_j}M_{n_j}/\ell_{n_j}\ge j-\tau_0$, and such that for $k\le j$ the pairings
of $U_{n_j}-\bar U$ and of $U_{n_j}\otimes U_{n_j}-Q$ with the fixed $L^1$ functions
$\delta_j^{-4}\phi_k((Y-y_0)/\delta_j,(T-\tau_0)/\delta_j)$ are at most $1/j$ in absolute value. The new normalization has
$\ell'_jD_{n_j}/M_{n_j}=\delta_j\sigma_{n_j}\ge j$, viscosity $\nu_{n_j}/\delta_j\le1/j$, terminal time at most $s_{n_j}\le t_{n_j}$ and
depth $(s_{n_j}M_{n_j}/\ell_{n_j}+\tau_0)/\delta_j\ge j$, so it is admissible. The Lebesgue point property gives
$\int\bar U(y_0+\delta_jy,\tau_0+\delta_j\tau)\phi_k\to b\int\phi_k$ and the same for $Q$; with the choice of $n_j$, density and
$|V_j|\le1$ this gives the two weak-* limits. The fields $V_j$ are defined for $\tau\le-\tau_0/\delta_j\to\infty$ (physical
times up to $s_{n_j}$), with $|V_j|\le1$ there. By the proof of Lemma 11, $V_j^\epsilon$ is equicontinuous and each of its
locally uniform limits is $b$, so $V_j^\epsilon\to b$ locally uniformly, which gives $V_j(\cdot,\tau)\rightharpoonup^*b$ for every
$\tau$. The proof of (a) uses only $|V_j|\le1$, the equation and the canonical pressure, so the two-sided inequality of (a)
holds for $e_j(\tau)=\int\chi|V_j(\tau)-b|^2$, with both sides available at every $\tau\le0$ for large $j$. Since
$e_j\rightharpoonup^*\operatorname{tr}R_0\int\chi$ in $L^\infty_{loc}$ of time, letting $j\to\infty$ and then $h\to0$ gives
$e_j(\tau)\to\operatorname{tr}R_0\int\chi$ for every $\tau$. Approximating $1_{B_R}$ by such $\chi$ and using
$\int_{B_R}|V_j-(V_j)_{B_R}|^2=\int_{B_R}|V_j-b|^2-|B_R||(V_j)_{B_R}-b|^2$ gives the oscillation limit; (L2M) would give strong
convergence and $R_0=0$. The rescaled axis distance of the new centers is $\operatorname{dist}(y_0,\mathcal A_{n_j})/\delta_j\to\infty$.
On $B_R$ the azimuthal direction then differs from a fixed horizontal unit vector $e_2^{(j)}$ by $o(1)$, so
$|V_j\cdot e_2^{(j)}|\le S(t_{n_j})/M_{n_j}+o(1)\to0$ uniformly on compact sets (Section 4). Along a subsequence
$e_2^{(j)}\to e_2$, whence $b\cdot e_2=0$ and $e_2\cdot R_0e_2=0$, and $R_0\ge0$ gives $R_0e_2=0$; $|b|^2+\operatorname{tr}R_0\le1$
because $\operatorname{w*lim}|V_j|^2\le1$.
(c) If (FLAT$_0$) holds, then for every admissible normalization and $R\ge1$,
$\sup_{-s_nM_n/\ell_n\le\tau\le0}\int_{B_R}|U_n(\tau)-(U_n(\tau))_{B_R}|^2\le|B_R|(\Theta_0(t_n)/M_n)^2\to0$, and the means over $B_R$ and $B_1$
differ by $o(1)$; along a joint subsequence $(U_n(\tau))_{B_1}\to(\bar U(\tau))_{B_1}$ for every $\tau$ (Lemma 11), so $U_n(\tau)$
converges in $L^2_{loc}$ for every $\tau$ to a spatial constant, $\mathcal R=0$, and $\bar U$ is a space-time constant (the
remark after Theorem 12). Conversely this property implies (C*) and excludes (HD). If (FLAT$_0$) fails, there are $c>0$,
$t_n\uparrow T_*$, $s_n\le t_n$, $x_n$, $\rho_n$ with $O_0(x_n,s_n,\rho_n)\ge cM_n$. Since $O_0(x,s,\rho)\le\min\{D(s)\rho,\|u(s)\|_\infty\}$,
$\rho_n\ge cM_n/D_n$ and $s_n\to T_*$; by Jensen $c^2M_n^2|B_{\rho_n}|\le E_0$, so $\rho_n\to0$ and the depth diverges; the
normalization at $(t_n,s_n,x_n,\rho_n)$ is admissible and satisfies (L2-OSC) on $B_1$. Along a joint subsequence either
$\mathcal R$ is not a.e. zero, which is (HD), or $\mathcal R=0$; in the latter case, under (C*), $\bar U(\tau)$ is a.e. constant
for every $\tau$, hence $\bar U$ is a space-time constant, and (a) contradicts (L2-OSC). This proves the decomposition
and the last equivalence. (FLAT$_0$) implies (FLAT) since $\Theta_\epsilon\le\sqrt8\,\Theta_0$ (proof of Proposition 14(c)),
so (C*-D) $\subset$ (C*) $\setminus$ (FLAT$_0$) $\subset$ (HD). Under (FLAT$_0$) a normalization with (L2-OSC) would, along a joint
subsequence, converge at $\tau=0$ strongly to a constant by (a), which is impossible. $\square$

Proposition 14A is a reduction, not an exclusion. In (ST) both branches of (C*) reduce to flat configurations: either
the historical BMO norm is $o(M)$, or some admissible normalization of the same trajectory has a constant weak limit with
a constant nonzero defect $R_0$ supported on $\operatorname{span}\{e_1,e_3\}$ (rank at most two), mollified fields converging
locally uniformly to that constant (so it has neither (W-OSC) nor (OSC$_0$); for the second option of (OSC$_0$), $\tilde O/M$
is a sum of fixed-resolution normalized oscillations with weights $2^{-m}$, each at most $1$ and tending to $0$), retained
terminal $L^2$ oscillation and failure of (L2M). Since a trajectory in (C*) is in (C), Corollary 6A(c) applies to this
tangent and supplies divergent cancelling signed meridional vorticity masses along a subsequence of bounded rescaled time
windows. The dimensional scenario of Limitations 1' postulates (FLAT$_0$). The tangent of (b) does not retain the
nonconstant weak mean of a (C*-D) witness: the construction proves (C*-D) $\subset$ (HD), but it neither proves the
converse nor excludes (HD) together with (B*) through different normalizations of one trajectory, and no strict
containment or coexistence example for actual singular trajectories is given. The point $(y_0,\tau_0)$ is chosen from the
weak limit (a retrospective choice, not a rule computed from the physical records). The exact heat shears
$U_n=(\beta+ae^{-\nu_nk_n^2(\tau+A_n)}\sin(k_ny_3),0,0)$ on $\tau\ge-A_n$, with $a>0$, $|\beta|+a\le1$, $k_n=n$, $A_n=n$,
$\nu_n=n^{-4}$, have zero pressure and $(U_n\cdot\nabla)U_n=0$, and on every bounded window weak limit $\beta e_1$ and defect
$\frac{a^2}2e_1\otimes e_1$, which annihilates $e_2$; so the limit equation does not exclude the configuration of (b). They
have infinite energy and are not normalizations of a singular trajectory. Excluding (HD) within (C*) requires an
estimate on the fixed trajectory. At the tangent, with $\lambda_j=\delta_j\ell_{n_j}$ and $d_j$ the rescaled axis distance,
terminal (L2-OSC) and disjoint rotated copies of the certified ball give $(1+d_j)M_{n_j}^2\lambda_j^3\le CE_0$ (the argument
of Remark (iii) of Section 9B). With $A_0=\|\eta_0\|_\infty$, the maximum principle bounds the datum contribution to the
rescaled $\eta$ by $A_0\lambda_j^2/M_{n_j}$, and that to the rescaled meridional vorticity on $B_R$ by
$A_0(d_j+R)\lambda_j^2/M_{n_j}\le C_RA_0E_0/(M_{n_j}^3\lambda_j)$; both tend to $0$, since $M_{n_j}\lambda_j\to\infty$. Lemma 19 and
$d_j\to\infty$ make the local swirl sources tend to $0$ uniformly on bounded windows. Thus, up to a locally uniformly
vanishing datum contribution, the rescaled meridional vorticity at the tangent is the accumulated source component. Its
local forcing vanishes on bounded tangent windows, but these estimates do not quantify the earlier production,
transport, diffusion or survival of that component; controlling it is the missing estimate of Limitations 6.

**Proposition 14B (normalizations at the BMO amplitude).** Let $\theta_0(s)=\sup_{x,\rho}O_0(x,s,\rho)$, so that
$\Theta_0(t)=\sup_{s\le t}\theta_0(s)$ (Proposition 14A). For a Lipschitz divergence-free field $f$ on $\mathbb R^3$ with
$\theta_0[f]=\sup_{x,\rho}(\fint_{B_\rho(x)}|f-(f)_{B_\rho(x)}|^2)^{1/2}<\infty$ put $\Pi[f](x)=\int K_{\cdot ij}(z)w_i(z)w_j(z)\,dz$,
$w(z)=f(x-z)-f(x)$, with $K$ as in Lemma 3. A BMO-class ancient solution with viscosity $\nu>0$ is a classical solution
of $\partial_\sigma v+v\cdot\nabla v+\Pi[v]=\nu\Delta v$, $\operatorname{div}v=0$ on $\mathbb R^3\times(-\infty,0]$ with
$\sup\|\nabla v\|_\infty<\infty$, $\sup_\sigma\theta_0[v(\sigma)]<\infty$ and $\operatorname{curl}\Pi[v(\sigma)]=0$ in the sense of
distributions for every $\sigma$ (this holds for rescaled physical fields, where $\Pi$ is a pressure gradient by Lemma 3,
and passes to the locally uniform limits used below). This class is invariant under translations,
rotations and constant Galilean transformations $v\mapsto v(y+c\sigma,\sigma)-c$, since $\Pi$ depends only on increments
and is covariant under rotations.
Fix a radial smooth probability density $\phi$ supported in $B_1$ and put $\phi_\rho=\rho^{-3}\phi(\cdot/\rho)$.
(a) For $f$ as above, with $\beta=\theta_0[f]$ and $d=\|\nabla f\|_\infty$: if $\beta d=0$, $f$ is constant and $\Pi[f]=0$;
otherwise $|f(x)-f(y)|\le C\beta(1+\log^+(d|x-y|/\beta))$, so
$\Pi[f]$ converges absolutely and $\|\Pi[f]\|_\infty\le C\beta d$. Since $\Pi[u(s)]=\nabla p(s)$, $\|\nabla p(s)\|_\infty\le
C\theta_0(s)\|\nabla u(s)\|_\infty$. Granting the quantitative one-scale $\epsilon$-regularity theorem quoted in the proof, for every
$a\in(0,T_*)$ there is $C_a$ with $D(t)\le C_a+C\Theta_0(t)^2$ for $a\le t<T_*$; consequently $\Theta_0(t)\to\infty$ as
$t\uparrow T_*$.
(b) (Liouville theorems in the BMO class.) A BMO-class ancient solution that is invariant under the translations in one
fixed direction, or that is axisymmetric about a fixed line with zero swirl about it, is constant.
(c) (Gradient records.) Assume the conclusion of (a), and suppose that $D(t_n)\ge\delta\Theta_n^2$, $\Theta_n=\Theta_0(t_n)$,
along a sequence $t_n\uparrow T_*$, for some $\delta>0$. Choose $s_n\le t_n$ and $x_n$ with $|\nabla u(x_n,s_n)|\ge D(t_n)/2$,
rotated about the axis into the half-plane $\{x_2=0,\,x_1\ge0\}$, let $V_n=\int\phi_{1/\Theta_n}(x-x_n)u(x,s_n)\,dx$ and
$$v_n(y,\sigma)=\Theta_n^{-1}\bigl[u(x_n+\Theta_n^{-1}y+\Theta_n^{-2}V_n\sigma,\ s_n+\Theta_n^{-2}\sigma)-V_n\bigr],\qquad
-s_n\Theta_n^2\le\sigma\le0 .$$
Then $a_n=\Theta_n\operatorname{dist}(x_n,\text{axis})$ is bounded, and along a subsequence $a_n\to a$, $v_n\to v$ and
$\nabla v_n\to\nabla v$ locally uniformly on $\mathbb R^3\times(-\infty,0]$, where $v$ is a BMO-class ancient solution
with viscosity $1$, $\sup_\sigma\theta_0[v(\sigma)]\le1$, $\|\nabla v\|_\infty\le C$, $|\nabla v(0,0)|\ge\delta/2$ and
$|v(y,\sigma)|\le C_A(1+\log(2+|y|))$ for $-A\le\sigma\le0$. For a constant horizontal vector $w$ the field
$\tilde v(y,\sigma)=v(y-w\sigma,\sigma)+w$ is axisymmetric about the vertical line through $(-a,0,0)$, with circulation
$|r\tilde v^\theta|\le G$ and swirl $|\tilde v^\theta|\le CG^{1/2}$ about that line, and $\tilde v^\theta\not\equiv0$.
(d) (BMO records.) Assume the conclusion of (a), and let $t_n\uparrow T_*$, $s_n\le t_n$, $x_n$ (rotated as in (c)) and
$\rho_n$ satisfy $O_0(x_n,s_n,\rho_n)\ge\Theta_n/2$ and $\kappa_n=\Theta_n\rho_n\le K$. With $T_n=\rho_n/\Theta_n$,
$V_n=\int\phi_{\rho_n}(x-x_n)u(x,s_n)\,dx$ and
$v_n(y,\sigma)=\Theta_n^{-1}[u(x_n+\rho_ny+T_nV_n\sigma,\,s_n+T_n\sigma)-V_n]$, one has $\kappa_n\ge c>0$,
$\operatorname{dist}(x_n,\text{axis})/\rho_n$ is bounded, and along a subsequence $\kappa_n\to\kappa$ and $v_n\to v$ as in
(c), with viscosity $1/\kappa$, $\|\nabla v\|_\infty\le CK$, circulation bound $G/\kappa$, and the terminal oscillation
$\fint_{B_1}|v(y,0)-(v(0))_{B_1}|^2dy\ge\frac14$ in place of the lower bound for $|\nabla v(0,0)|$; again $\tilde v^\theta\not\equiv0$.

Proof. (a) Let $h=\beta/d$ and $|x-y|=R\ge h$ (for $R<h$, $|f(x)-f(y)|\le dR<\beta$). Then $|f(x)-(f)_{B_h(x)}|\le dh=\beta$,
means over concentric balls with radii $\rho$ and $2\rho$ differ by at most $\sqrt8\,\beta$, and $B_{2^kh}(y)\subset B_{2^{k+1}h}(x)$
when $2^kh\ge R$; chaining from $B_h(x)$ and from $B_h(y)$ up to radius $2^kh$, $k\le\log_2(4R/h)$, gives the
logarithmic bound. With $|K_{kij}(z)|\le C|z|^{-4}$ and $|w(z)|\le\min\{d|z|,C\beta(1+\log^+(|z|/h))\}$, splitting at $|z|=h$
gives $|\Pi[f]|\le C(d^2h+\beta^2/h)=C\beta d$. For $f=u(s)$, Lemma 3 identifies the integral with $\nabla p(s)$.
For the bound on $D$ fix $s\in[a,t]$, $x_0$, an absolute $\epsilon_0>0$ to be chosen, $r=\min\{\epsilon_0/\Theta_0(t),\sqrt a/2\}$,
$V=\int\phi_r(x-x_0)u(x,s)\,dx$, and the constant Galilean transform $\tilde u(x,\tau)=u(x+V(\tau-s),\tau)-V$,
$\tilde p(x,\tau)=p(x+V(\tau-s),\tau)$, a smooth solution on $Q_r=B_r(x_0)\times(s-r^2,s]$. For every fixed $1<q<\infty$ and each $\tau$,
$(\fint_{B_r(x_0)}|\tilde p(\tau)-c(\tau)|^q)^{1/q}\le C_q\theta_0(\tau)^2$ for a suitable $c(\tau)$: with
$w=u(\tau)-(u(\tau))_{B_{2r}}$ (balls centred at $x_0+V(\tau-s)$), $p=R_iR_j(w_iw_j)$ up to a constant because
$\operatorname{div}u=0$; the part of $w_iw_j$ on $B_{4r}$ is handled by the $L^q$ bound for $R_iR_j$ and the John-Nirenberg
inequality, and the rest by the kernel difference bound $Cr|y|^{-4}$ on the dyadic annuli together with
$\fint_{B_{2^kr}}|w|^2\le C(k+1)^2\theta_0^2$. Let $h(\tau)=\int\phi_r(x-x_0)\tilde u(x,\tau)\,dx$ and $z=\tilde u-h$. Testing the
equation with $\phi_r(\cdot-x_0)$ and using $\int\partial_j\phi_r\,z_j=0$ (since $\operatorname{div}z=0$), the
John-Nirenberg inequality and the pressure bound, $|h'|\le C(\Theta/r^2+\Theta^2/r+\Theta|h|/r)$ with $\Theta=\Theta_0(t)$; as
$h(s)=0$ and $r\Theta\le\epsilon_0$, $|h|\le C\Theta$ on $[s-r^2,s]$. Hence
$r^{-2}\int_{Q_r}(|\tilde u|^3+|\tilde p-c(\tau)|^{3/2})\le C(r\Theta)^3\le C\epsilon_0^3$. The $\epsilon$-regularity theorem of
Caffarelli, Kohn and Nirenberg in the form with $L^3$ velocity and $L^{3/2}$ pressure on one cylinder (F.-H. Lin, Comm.
Pure Appl. Math. 51 (1998), Theorem 3.1; O. A. Ladyzhenskaya and G. A. Seregin, J. Math. Fluid Mech. 1 (1999); restated as
Theorem 1.1 of C. Guevara and N. C. Phuc, arXiv 1702.00449), in its quantitative form (a bound for the velocity on the
half cylinder), applied to the smooth, hence suitable, rescaling $U(X,S)=r\tilde u(x_0+rX,s+r^2S)$,
$P=r^2(\tilde p-c)(x_0+rX,s+r^2S)$ on $B_1\times(-1,0]$, for which $\int(|U|^3+|P|^{3/2})\le C\epsilon_0^3$, together with the
interior estimates for spatial derivatives of bounded suitable weak solutions on a smaller backward cylinder, gives $|\nabla u(x_0,s)|=|\nabla\tilde u(x_0,s)|\le C/r^2$ for $\epsilon_0$ small. This is the
step granted in the statement. So $D(t)\le\max\{D(a),C\Theta_0(t)^2+C/a\}$. If $\Theta_0$ stayed bounded, $D$ and then, by
Lemma 2, $M$ would stay bounded, which is impossible.
(b) Common facts. Let $v_k$ be members of the class with viscosities in a compact subset of $(0,\infty)$, or smooth solutions
of $\partial_\sigma v_k+v_k\cdot\nabla v_k+\Pi[v_k]=\nu_k\Delta v_k$ on $\mathbb R^3\times[-A_k,0]$ with $A_k\to\infty$ and $\operatorname{curl}\Pi[v_k]=0$, with
$\theta_0[v_k(\sigma)]\le\beta$, $\|\nabla v_k\|_\infty\le L$ and $|\int\phi\,v_k(y,0)\,dy|\le C_0$. The weighted means
$h_k(\sigma)=\int\phi\,v_k(y,\sigma)\,dy$ satisfy, by the computation in (a) with $r=1$ and the bound of (a) for $\Pi$,
$|h_k'|\le C(\nu_k\beta+\beta^2+\beta L+\beta|h_k|)$, so with (a), $|v_k(y,\sigma)|\le C_A(1+\log(2+|y|))$ on $[-A,0]$. On each
bounded cylinder $\partial_\sigma v_k-\nu_k\Delta v_k=-v_k\cdot\nabla v_k-\Pi[v_k]$ is then bounded, so interior $W^{2,1}_p$
estimates ($p>5$) bound $\nabla v_k$ in a parabolic H\"older norm; the vorticity equation
$\partial_\sigma\omega_i-\nu_k\Delta\omega_i=\partial_j(v_{k,i}\omega_j-\omega_iv_{k,j})$, obtained with $\operatorname{curl}\Pi[v_k]=0$, contains no pressure, and
bootstrapping in it, with $\Delta v_k=-\operatorname{curl}\omega$, bounds all spatial derivatives of $v_k$ locally, uniformly in
$k$. A subsequence converges locally uniformly with these derivatives on $\mathbb R^3\times(-\infty,0]$, and
$\Pi[v_k]\to\Pi[v_\infty]$ locally uniformly by dominated convergence (the integrands are bounded by
$C|z|^{-4}\min\{L^2|z|^2,\beta^2(1+\log^+(L|z|/\beta))^2\}$), so the limit is in the class (curl-freeness of $\Pi$ passes to the limit), with the same bounds. Applied to the
Galilean translates $v(y_k+y+W_k\sigma,\sigma_k+\sigma)-W_k$ of one member, with $|W_k-\int\phi(y-y_k)v(y,\sigma_k)dy|\le C_0$, this
gives compactness of translates; applied at every point it bounds $\nabla^2v$. A member that is curl-free at a time
$\sigma$ has harmonic components with bounded gradient at that time, so $v(\sigma)$ is affine, and $\theta_0<\infty$ forces it
to be constant (a linear field $Ly$ has $O_0(0,0,\rho)=\rho|L|/\sqrt5$, $|L|$ the Frobenius norm). A spatially constant
member $c(\sigma)$ has $\Pi[c]=0$, hence $c'=0$.
Invariant direction. Rotate so that $\partial_2v=0$. With $\Phi(z)=(4\pi|z|)^{-1}$ one has $K_{kij}=\partial_i\partial_j\partial_k\Phi$, and
every term of $\Pi[v]$ with an index equal to $2$ vanishes: its increments do not depend on $z_2$, the integral is
absolutely convergent, and $\int_{\mathbb R}\partial_2g\,dz_2=0$ for $g$ a second derivative of $\Phi$ and $(z_1,z_3)\ne0$. In
particular $\Pi_2[v]=0$. The component $\omega=\partial_3v_1-\partial_1v_3$ of the vorticity along $e_2$ is bounded by $2L$ and,
as the stretching term $\omega_1\partial_1v_2+\omega_3\partial_3v_2=-\partial_3v_2\partial_1v_2+\partial_1v_2\partial_3v_2$ vanishes, solves
$\partial_\sigma\omega+v\cdot\nabla\omega=\nu\Delta\omega$. Suppose $S=\sup\omega>0$ and take $(y_k,\sigma_k)$ with $\omega(y_k,\sigma_k)\to S$.
A limit of translates as above is invariant in $e_2$, and its vorticity component $\omega_\infty\le S$ attains $S$ at $(0,0)$;
the strong maximum principle for $S-\omega_\infty\ge0$ (smooth locally bounded drift) gives $\omega_\infty\equiv S$ on
$\mathbb R^3\times(-\infty,0]$. Then $(v_{\infty,1},v_{\infty,3})-\frac S2(y_3,-y_1)$ is, in the variables $(y_1,y_3)$, divergence-free and
curl-free with bounded gradient, hence affine, so $(v_{\infty,1},v_{\infty,3})$ is affine with a nonzero antisymmetric part, and
$O_0(0,\sigma,\rho)\ge c\rho S$ for all $\rho$, a contradiction. Hence $\omega\le0$, likewise $\omega\ge0$, and $(v_1,v_3)$ is, as above,
a function $c(\sigma)$ of time alone. The remaining terms of $\Pi_1,\Pi_3$ contain only increments of $v_2$ and so
vanish, and $c'=0$. With $\Pi_2=0$, $f(y,\sigma)=v_2(y+c\sigma,\sigma)$ solves $\partial_\sigma f=\nu\Delta f$ on
$\mathbb R^3\times(-\infty,0]$ with bounded gradient; each $\partial_if$ is a bounded ancient solution of the heat equation, and the
representation from time $\sigma-A$ gives $|\nabla\partial_if|\le C(\nu A)^{-1/2}\|\partial_if\|_\infty$, so $\nabla f$ is constant,
$f=b\cdot y+g(\sigma)$ with $g'=0$, and $\theta_0<\infty$ forces $b=0$. So $v$ is constant.
Axisymmetric without swirl. Take the axis to be $\{y_1=y_2=0\}$, $v=v^re_r+v^ze_z$, and $\eta=\omega^\theta/r$, which solves
$\partial_\sigma\eta+v^r\partial_r\eta+v^z\partial_z\eta=\nu(\partial_r^2+3r^{-1}\partial_r+\partial_z^2)\eta$ and is bounded: $|\eta|\le2L/r$ for $r\ge1$,
and $|\eta|\le C\sup|\nabla^2v|$ for $r\le1$ because $\omega^\theta$ vanishes on the axis. Suppose $S=\sup\eta>0$ and take
$(y_k,\sigma_k)$ with $\eta(y_k,\sigma_k)\to S$; after discarding finitely many terms, $r(y_k)\le\max\{1,4L/S\}$. Translate along the axis to the height of $y_k$ and in
time, and subtract the weighted mean over the unit ball centred at the axis point at that height, which is axial
because $\phi$ is radial; it differs from the mean at $y_k$ by at most $L(1+\max\{1,4L/S\})$. The
translates stay axisymmetric about the same axis without swirl, and a limit has $\eta_\infty\le S$ with equality at a point
with $r\le\max\{1,4L/S\}$ and $\sigma=0$. Lifted to $\mathbb R^4\times\mathbb R$ with $r=|Y|$, the $\eta$ equation is
$\partial_\sigma\eta+\tilde b\cdot\nabla\eta=\nu\Delta_5\eta$ with the smooth locally bounded drift $\tilde b=(v^rY/r,v^z)$ (smooth because
$v^r/r$ is a smooth function of $r^2$ and $z$), so the strong maximum principle gives $\eta_\infty\equiv S$ and
$|\omega^\theta_\infty|=Sr$ is unbounded, contradicting $\|\nabla v_\infty\|_\infty\le L$. Hence $\eta\le0$, likewise $\eta\ge0$, so
$\operatorname{curl}v=\omega^\theta e_\theta=0$ and $v$ is constant.
(c) For physical times $s\le s_n$, $\theta_0[v_n(\sigma)]=\theta_0(s)/\Theta_n\le1$ and $\|\nabla v_n(\sigma)\|_\infty\le D(t_n)/\Theta_n^2\le C$ for
large $n$ by (a); the viscosity is $1$, and $\Pi[v_n]$ is the rescaled pressure gradient by Lemma 3 and the invariance of
$\Pi$. Since $|\nabla u(x_n,s_n)|\to\infty$, $s_n\to T_*$ and the depth $s_n\Theta_n^2$ tends to infinity. By the choice of
$V_n$, $\int\phi\,v_n(y,0)\,dy=0$. The common facts of (b) give the subsequence and the limit with the stated bounds, and
$|\nabla v(0,0)|\ge\delta/2$ because $|\nabla v_n(0,0)|\ge D(t_n)/(2\Theta_n^2)$. For the geometry let $x_n^a=(0,0,x_{n,3})$ and
$V_n^a=\int\phi_{1/\Theta_n}(x-x_n^a)u(x,s_n)\,dx$, which is vertical because $\phi$ is radial and $u$ is axisymmetric. The chain
of means in (a) gives $|V_n-V_n^a|\le C(1+\log(2+a_n))\Theta_n$, so the horizontal part $W_n'$ of $W_n=V_n/\Theta_n$ satisfies
$|W_n'|\le C(1+\log(2+a_n))$. Put $U_n(z,\sigma)=\Theta_n^{-1}u(x_n+\Theta_n^{-1}z,s_n+\Theta_n^{-2}\sigma)$, so that
$v_n(y,\sigma)=U_n(y+W_n\sigma,\sigma)-W_n$ and $U_n$ is axisymmetric about the vertical line through $(-a_n,0,0)$. Differentiating
the rotation covariance gives $(Y^\perp\cdot\nabla)U_n=JU_n$, with $Y=(z_1+a_n,z_2,0)$, $Y^\perp=(-Y_2,Y_1,0)$ and
$J(c_1,c_2,c_3)=(-c_2,c_1,0)$. If $a_n\to\infty$ along a subsequence, then for $(y,\sigma)\in B_R\times[-A,0]$ and
$z=y+W_n\sigma$, $|Y-a_ne_1|\le R+CA(1+\log(2+a_n))=o(a_n)$ and
$|(Y^\perp/|Y|)\cdot\nabla v_n(y,\sigma)|=|J(v_n(y,\sigma)+W_n)|/|Y|\le(C_{A,R}+C\log(2+a_n))/(a_n/2)\to0$; since $Y^\perp/|Y|\to e_2$
uniformly there and $\nabla v_n$ is bounded, $\partial_2v_n\to0$ locally uniformly, the limit is invariant in $e_2$, and
(b) makes it constant, contradicting $|\nabla v(0,0)|\ge\delta/2$. So $a_n$ is bounded; along a subsequence $a_n\to a$ and
$W_n'\to w$. The fields $\tilde U_n(z,\sigma)=U_n(z+W_{n,3}e_3\sigma,\sigma)-W_{n,3}e_3$ are axisymmetric about the same line as
$U_n$, with the same swirl, and $\tilde U_n(z,\sigma)=v_n(z-W_n'\sigma,\sigma)+W_n'\to v(z-w\sigma,\sigma)+w=\tilde v(z,\sigma)$ locally
uniformly. So $\tilde v$ is axisymmetric about the line through $(-a,0,0)$, and its swirl is the limit of the values of
$\Theta_n^{-1}u^\theta$ at the corresponding points; the circulation bound and Lemma 1(c) give $|r\tilde v^\theta|\le G$ and
$|\tilde v^\theta|\le\limsup(GD(t_n))^{1/2}/\Theta_n\le CG^{1/2}$. $\tilde v$ is in the class; if $\tilde v^\theta\equiv0$, (b) makes $\tilde v$,
and hence $v$, constant, a contradiction.
(d) Since $O_0(x,s,\rho)\le(3/5)^{1/2}D(s)\rho$, $\Theta_n\le2D(t_n)\rho_n$ and $\kappa_n\ge\Theta_n^2/(2D(t_n))\ge c$ by (a). Since
$O_0(x_n,s_n,\rho_n)\le\|u(s_n)\|_\infty$, $s_n\to T_*$, and the depth $s_n/T_n\ge s_n\Theta_n^2/K$ tends to infinity. The
viscosity is $T_n/\rho_n^2=1/\kappa_n\in[1/K,1/c]$, $\theta_0[v_n]\le1$, $\|\nabla v_n\|_\infty\le\rho_nD(t_n)/\Theta_n=\kappa_nD(t_n)/\Theta_n^2\le CK$,
and the terminal oscillation of $v_n$ on $B_1$ is $O_0(x_n,s_n,\rho_n)/\Theta_n\ge\frac12$ and passes to the limit. The rest is
the proof of (c), with $a_n=\operatorname{dist}(x_n,\text{axis})/\rho_n$, circulation $\Gamma/\kappa_n$ for $\tilde U_n$, swirl bounded
by $(GD(t_n))^{1/2}/\Theta_n$, and the terminal oscillation in place of $|\nabla v(0,0)|$. $\square$

**Remark (scope of Proposition 14B).** (i) The normalizations of (c) and (d) are computed from records of the trajectory
(a near-maximizer of $|\nabla u|$ or of $O_0$, with the local weighted mean as constant Galilean frame), and along subsequences they
converge locally uniformly with first derivatives through $\tau=0$ to limits that are spatially nonconstant and solve the
Navier-Stokes equations with the pressure gradient $\Pi[v]$, which for bounded fields is the gradient of the
canonical BMO pressure (Section 2). They are not admissible amplitude-$M$ normalizations, and the limits are not shown to
be bounded: only $|v|\le C_A(1+\log(2+|y|))$ on each slab $-A\le\sigma\le0$ is proved. No uniform force $F(\sigma)$ appears
in the limit equation, because the full increment integrals converge. Under (FLAT$_0$), $\Theta_n=o(M_n)$, and since $u(s)\in C_0$,
$\sup_{x,\,s\le s_n}|u(x,s)-V|\ge M(s_n)/2$ for every constant vector $V$, so the supremum of $|v_n|$ over its whole domain
is at least $M(s_n)/(2\Theta_n)$. If a limit $v$ in (c) or (d) were bounded, its constant horizontal Galilean transform $\tilde v$
would be a nonconstant bounded ancient Navier-Stokes solution, axisymmetric about a fixed line, with bounded circulation
and nonzero swirl. Proposition 14B does not give GOAL.
(ii) The hypothesis of (c) is not derived. In the complementary case $D/\Theta_0^2\to0$, every sequence as in (d) without
the bound $K$ has $\kappa_n\ge\Theta_n^2/(2D(t_n))\to\infty$: the viscosity of the BMO-scale rescaling tends to zero and (d) does
not apply. The scalar rates $M=\tau^{-3/4}$, $\Theta_0=M\ell^{-1/2}$, $D=\Theta_0^2\ell^{-1}$, with $\tau=T_*-t$ and $\ell=\log(e/\tau)$,
satisfy $D/M^2\to0$, (FLAT$_0$), $D/\Theta_0^2\to0$, the bound $M'\le C\Theta_0D$ that follows from (a) and the maximum principle
for $|u|$ ($M'/(\Theta_0D)=\frac34\tau^{1/2}\ell^{5/2}$), Lemma 2 ($M^5/D^3=\tau^{3/4}\ell^6$), $M^2\tau\to\infty$ and
$\int^{T_*}D=\int^{T_*}\Theta_0^2=\infty$; they are rates, not a solution.
(iii) Among the axisymmetric limits of (c) and (d), the case left open by (b) is the one with swirl. If every BMO-class ancient solution that is
axisymmetric about a fixed line with bounded circulation were constant, (c) and (d) would give $D(t)/\Theta_0(t)^2\to0$ and
$\kappa_n\to\infty$ along every sequence as in (d) without the bound $K$; by (ii) this would exclude neither (FLAT$_0$) nor (C).
That hypothesis contains the Liouville problem for bounded ancient axisymmetric mild solutions with bounded
circulation (by the KNSS smoothing estimates such solutions have bounded gradients and canonical pressure), for which
the theorems known to us need further hypotheses: $r|v|\le C$ (Koch, Nadirashvili, Seregin and Sverak, Theorem 5.3),
$\Gamma\in L^\infty_tL^p_x$ for some $1\le p<\infty$, or $\Gamma\to0$ as $r\to\infty$ uniformly (Lei, Zhang and Zhao, arXiv 1701.00868,
Theorem 1.3 and Remark 1.4), or a BMO stream potential (Lei and Zhang,
arXiv 1011.5066). Q. S. Zhang's survey (arXiv 2101.04905v2, Section 3) states the KNSS conjecture that bounded mild
ancient axisymmetric solutions are constant, notes that bounded circulation can be added to it without much loss of
generality since $\Gamma$ is scale invariant and obeys the maximum principle, and describes the case in which $\Gamma$ does not
decay at radial infinity as the remaining and most difficult one, with partial results under axial periodicity or a rate
of convergence of $\Gamma^2$ to its upper limit at radial infinity. So proving the universal hypothesis of this remark would
in particular settle the bounded-circulation case of the KNSS conjecture described as open in these sources. A rigidity
statement for the smaller class of limits actually extracted from these trajectories need not classify every bounded
ancient solution; none is proved here. Decay of $\Gamma$ uniform in height and time, $\lim_{R\to\infty}\sup\{|\Gamma(r,z,\sigma)|:r\ge R,\ z\in\mathbb R,
\ \sigma\le0\}=0$, would suffice: as $|\Gamma|\le Lr^2$, a
positive supremum of $\Gamma$ would be approached at radii bounded above and below, the compactness of (b) with axial
boosts would give a limit attaining it at a finite positive radius, and the strong maximum principle for
$\partial_\sigma\Gamma+v^r\partial_r\Gamma+v^z\partial_z\Gamma=\nu(\partial_r^2-r^{-1}\partial_r+\partial_z^2)\Gamma$ on $\{r>0\}$ would make the limit constant
there, contradicting $\Gamma=0$ on the axis; so $\Gamma\le0$, likewise $\Gamma\ge0$, and with $\Gamma\equiv0$, (b) applies. This decay is
not derived. The bounds defining the class do not imply the scale-invariant bound $r|v|\le C$ used by KNSS, even after
subtraction of a constant: $\log(1+r^2)e_z$ is divergence-free with bounded gradient and finite $\theta_0$. It is a
stationary Euler field, not an ancient Navier-Stokes solution, so it tests only the functional bounds.

**Proposition 14C (energy bound on BMO flatness).** (a) Let $f\in L^2(\mathbb R^3;\mathbb R^3)$ be Lipschitz, with
$m=\|f\|_\infty>0$, $d=\|\nabla f\|_\infty$, $\beta=\theta_0[f]$ (as in Proposition 14B) and $\beta\le m/32$, and let $k$ be the
largest integer with $(1+8k)\beta\le m/2$. Then $k\ge1$, $k\ge m/(16\beta)-9/8$, and
$$\|f\|_2^2\ge\frac\pi3\,m^2\Bigl(\frac\beta d\Bigr)^38^k\ge c_0\,m^2\Bigl(\frac\beta d\Bigr)^32^{3m/(16\beta)},\qquad c_0=\frac\pi3\,8^{-9/8}.$$
(b) For every $t<T_*$ with $\Theta_0(t)\le M(t)/32$,
$$D(t)^3\ge c_0E_0^{-1}M(t)^2\,\Theta_0(t)^3\,2^{3M(t)/(16\Theta_0(t))}.$$
In particular, with $x=M(t)/\Theta_0(t)\ge32$, $D(t)/M(t)\ge c_0^{1/3}(M(t)^2/E_0)^{1/3}2^{x/16}/x$; the ratio of this bound to
the bound $D/M\ge(\pi M^2/(24E_0))^{1/3}$ of Lemma 2 is $2^{-1/8}2^{x/16}/x$, which is less than $1$ near $x=32$ and grows
exponentially as $x\to\infty$, so under (FLAT$_0$) the new bound is eventually the stronger one.
(c) In regime (II) there is $t_0<T_*$ such that for $t_0\le t<T_*$
$$\frac{M(t)}{\Theta_0(t)}\le\max\Bigl\{256,\ \frac{32}3\log_2\bigl(c_0^{-1}E_0M(t)\bigr)\Bigr\}.$$
So (FLAT$_0$), if it holds, holds at most at a logarithmic rate: $\Theta_0(t)\ge cM(t)/\log(E_0M(t))$ near $T_*$. Granting the
regularity input of Proposition 14B(a) gives the same conclusion with $\frac{16}3\log_2(CE_0M)$.

Proof. (a) A Lipschitz function in $L^2$ tends to $0$ at infinity, so $|f(x_*)|=m$ for some $x_*$; $d>0$ and $\beta>0$, since
otherwise $f$ would be constant, hence $0$. From $\beta\le m/32$, $(m/(2\beta)-1)/8\ge15/8$, so $k\ge1$, and
$k\ge(m/(2\beta)-1)/8-1=m/(16\beta)-9/8$. Put $\ell=\beta/d$ and write $(f)_r$ for the mean of $f$ on $B_r(x_*)$. On $B_\ell(x_*)$,
$|f-f(x_*)|\le d\ell=\beta$, so $|(f)_\ell-f(x_*)|\le\beta$. For $r>0$,
$$|(f)_r-(f)_{2r}|\le\fint_{B_r(x_*)}|f-(f)_{2r}|\le8\fint_{B_{2r}(x_*)}|f-(f)_{2r}|\le8\,O_0[f](x_*,2r)\le8\beta,$$
by the Cauchy-Schwarz inequality. Hence $|(f)_{2^k\ell}-f(x_*)|\le(1+8k)\beta\le m/2$ and $|(f)_\rho|\ge m/2$ for $\rho=2^k\ell$. By
the Cauchy-Schwarz inequality again, $\|f\|_2^2\ge\int_{B_\rho(x_*)}|f|^2\ge|B_\rho||(f)_\rho|^2\ge\frac{4\pi}3\rho^3\frac{m^2}4$, which is
the first inequality; the second follows from $8^k\ge8^{-9/8}2^{3m/(16\beta)}$.
(b) Since $s\mapsto\|u(s)\|_\infty$ is continuous on $[0,t]$, there is $s_*\le t$ with $\|u(s_*)\|_\infty=M(t)$. Apply (a) to
$f=u(s_*)$, with $\|f\|_2^2\le E_0$ by the energy inequality, $d\le D(t)$ and $\beta=\theta_0(s_*)\le\Theta_0(t)\le M(t)/32$. The
function $g(\beta)=\beta^32^{3m/(16\beta)}$ has $g'/g=3/\beta-3m\log2/(16\beta^2)<0$ for $0<\beta<m\log2/16$, and $1/32<\log2/16$, so
$g(\theta_0(s_*))\ge g(\Theta_0(t))$ with $m=M(t)$. Under (FLAT$_0$), $\Theta_0(t)\le M(t)/32$ for $t$ near $T_*$; take cube roots.
(c) In regime (II), $D(t)\le M(t)^2$ for $t$ near $T_*$. If $x=M(t)/\Theta_0(t)\ge256$, (b) gives
$M^6\ge D^3\ge c_0E_0^{-1}M^2(M/x)^32^{3x/16}$, that is $2^{3x/16}\le c_0^{-1}E_0Mx^3$; and $x^3\le2^{3x/32}$ for $x\ge256$, since
$\log_2x\le x/32$ there, so $2^{3x/32}\le c_0^{-1}E_0M$. With the granted input instead, $\Theta_0(t)\to\infty$ and
$D(t)\le C_a+C\Theta_0(t)^2\le2C\Theta_0(t)^2$ near $T_*$, and for $x\ge32$ (b) gives $8C^3\Theta_0^6\ge c_0E_0^{-1}M^2\Theta_0^32^{3x/16}$, that is
$2^{3x/16}\le8C^3c_0^{-1}E_0M/x^3\le8C^3c_0^{-1}E_0M$. $\square$

**Remark.** The exponential dependence on $m/\beta$ in (a) is sharp up to the constant in the exponent. For
$f=m\,e\max\{0,1-L^{-1}\log(1+|x|/a)\}$, $e$ a unit vector, $a>0$ and $L$ large, one has $d=m/(La)$; $\beta\le C_1m/L$, since
$t\mapsto\max\{0,1-t\}$ is $1$-Lipschitz and the mean minimizes the $L^2$ deviation, so $\theta_0[f]\le(m/L)\theta_0[\log(1+|\cdot|)]$;
$\beta\ge c_1m/L$, from the oscillation of the logarithm on $B_{ae^{L/2}}(0)$; and $\|f\|_2^2\le\frac{4\pi}3m^2a^3e^{3L}$. Hence
$\|f\|_2^2\le Cm^2(\beta/d)^3e^{3C_1m/\beta}$. This field is not divergence-free, and (a) does not use the divergence
condition, but the same holds for smooth, compactly supported, divergence-free fields that are axisymmetric without swirl:
with $b>0$, $0<8a<\mathcal R$, $L=\log(\mathcal R/a)$, $\chi$ smooth, supported in $[a,\mathcal R]$, equal to $1$ on $[2a,\mathcal R/2]$, with
$|\chi'(q)|\le C/q$, and $F(q)=b\int_q^\infty\chi(\varsigma)\varsigma^{-1}d\varsigma$, the field
$f=\operatorname{curl}(\frac12F(|x|)\,e_z\times x)=F(|x|)e_z+\frac{F'(|x|)}{2|x|}(|x|^2e_z-x_3x)$ is constant on $B_a$, has
$\|f\|_\infty=bL+O(b)$, $d\le Cb/a$, $cb\le\theta_0[f]\le Cb$ and $\|f\|_2^2\le Cb^2\mathcal R^3=Cb^2a^3e^{3L}$, hence again
$\|f\|_2^2\le Cm^2(\beta/d)^3e^{Cm/\beta}$. (The terms other than $F e_z$ are bounded by $Cb$ and $F$ is within $Cb$ of
$b\min\{L,\log^+(\mathcal R/|x|)\}$, which gives the upper bounds; the horizontal component $\frac{b\chi(|x|)x_3}{2|x|^2}(x_1,x_2)$ has
zero mean on balls centred at the origin and modulus at least $b/16$ on a fixed fraction of $B_{\mathcal R/2}$, which gives the
lower bound for $\theta_0$.) Part (c) does not exclude (FLAT$_0$): the scalar rates of Remark (ii) after Proposition 14B have
$M/\Theta_0=\ell^{1/2}$ and $\log M=\frac34\log(1/\tau)$, within the bound. Under (FLAT$_0$), the proof of (b) also shows that the ball
$B_\rho(x_*)$ of (a) at time $s_*$, on which the mean velocity has modulus at least $M/2$, has radius $\rho\ge(\Theta_0/(3D))2^{M/(16\Theta_0)}$,
which is larger than the Lipschitz length $M/D$ by a factor that grows exponentially in $M/\Theta_0$ (this uses $\beta\le\Theta_0$ and
the monotonicity of $\beta\,2^{m/(16\beta)}$ for $\beta<m\log2/16$). These are admissible scales: along $t_n\uparrow T_*$, Jensen gives
$\rho_n^3\le3E_0/(\pi M_n^2)$, so $\rho_n\to0$, and $s_{*,n}\to T_*$ since $\|u(s_{*,n})\|_\infty=M_n\to\infty$, so the depth $s_{*,n}M_n/\rho_n$
diverges, while $\rho_nD_n/M_n\to\infty$. The amplitude-$M$ normalizations at such scales have constant limits, as Proposition
14A(c) requires; the ball carries a large mean and small relative $L^2$ oscillation, not a pointwise plateau.

**Proposition 14D (persistence of large means).** Let $\phi$ be as in Proposition 14B, $R>0$, $t<T_*$, $\Theta=\Theta_0(t)$,
$x_0\in\mathbb R^3$, and let $X$ solve $X'(s)=b(s)=\int\phi_R(y)u(X(s)+y,s)\,dy$ on $[0,t]$ with $X(t)=x_0$.
(a) For $0\le s\le t$, $|b'(s)|\le C_1\Theta(1+\Theta R)R^{-2}$ and $\|\nabla u(s)\|_2^2\ge c_1R|b(s)|^2$.
(b) Let $m_0>\|u_0\|_\infty$, $m_n=2^nm_0$, let $t_n$ be the first time with $\|u(t_n)\|_\infty=m_n$, and put $B_n=\Theta_0(t_n)$,
$d_n=D(t_n)$, $h_n=m_n/B_n$, $R_n=2^{\lfloor h_n/64\rfloor}B_n/d_n$. There are absolute $h_*,c>0$ such that, whenever $h_n\ge h_*$,
$$t_n-t_{n-1}\ge\delta_n=\frac{m_nR_n^2}{8C_1B_n(1+B_nR_n)},\qquad
\int_{t_n-\delta_n}^{t_n}\|\nabla u(s)\|_2^2\,ds\ge c\,\frac{m_n^3R_n^3}{B_n(1+B_nR_n)},$$
and the intervals $[t_n-\delta_n,t_n]$ are disjoint, so the sum of the right-hand sides over such $n$ is at most $E_0/2$.
(c) In regime (II), $\delta_n\ge c\,e^{\kappa h_n}/(h_nm_n^2)$, $\kappa=(\log2)/64$, for large $n$ with $h_n\ge h_*$. Consequently,
$M(t)^2(T_*-t)\ge c\,e^{\kappa h_{n+1}}/h_{n+1}$ for $t_{n-1}\le t<t_n$, $n$ large, whenever $h_{n+1}\ge h_*$.

Proof. (a) $X$ exists and is unique on $[0,t]$ since $b$ is bounded and Lipschitz in $X$ there. Put $w(y,s)=u(X(s)+y,s)-b(s)$
and let $c(s)$ be the constant of the pressure estimate in the proof of Proposition 14B(a), for the ball $B_R(X(s))$ and
$q=2$ (its proof applies to balls of any radius), so that $(\fint_{B_R}|p(X(s)+\cdot,s)-c(s)|^2)^{1/2}\le C\theta_0(s)^2$; that
estimate does not use the granted input. Since
$X'=b$, the equation gives $b_i'=\int\Delta\phi_R\,w_i+\int\partial_j\phi_R\,w_iw_j+\int\partial_i\phi_R\,(p(X+\cdot)-c)$, where
$\int\phi_R\,w_j\partial_jw_i=-\int\partial_j\phi_R\,w_iw_j$ because $\operatorname{div}w=0$. As $|b-(u)_{B_R(X)}|\le C\fint_{B_R(X)}|u-(u)_{B_R(X)}|\le C\Theta$,
$\int_{B_R}|w|^2\le C\Theta^2R^3$, and the three terms are at most $C\Theta/R^2$, $C\Theta^2/R$ and $C\Theta^2/R$. For the second
inequality let $\psi=\Phi*\phi_R$, $\Phi(x)=(4\pi|x|)^{-1}$, so $-\Delta\psi=\phi_R$ and $\|\nabla\psi\|_2^2=R^{-1}\|\nabla(\Phi*\phi)\|_2^2$.
For a unit vector $e$, $\int\phi_R(y)u(X+y,s)\cdot e\,dy=\int\nabla\psi\cdot\nabla(u\cdot e)(X+\cdot,s)$: the boundary terms on spheres
$\partial B_\varrho$ are bounded by $C|\varrho^{-2}\int_{\partial B_\varrho}u\cdot e|$ for large $\varrho$, and this tends to $0$ along a sequence
$\varrho\to\infty$ since $u(s)\in L^2$. Choosing $e$ parallel to $b(s)$ gives $|b(s)|\le CR^{-1/2}\|\nabla u(s)\|_2$.
(b) At $t_n$, $\|u(t_n)\|_\infty=M(t_n)=m_n$ is attained at some $x_*$ (as in Proposition 14C(a)). With $a=B_n/d_n$, $k=\lfloor h_n/64\rfloor$
and $h_n\ge64$, the dyadic comparison in the proof of Proposition 14C(a) gives $|(u(t_n))_{B_{R_n}(x_*)}-u(x_*,t_n)|\le(1+8k)B_n\le
B_n+m_n/8$, and the weighted mean differs from the ball mean by at most $C_\phi B_n$. Take $x_0=x_*$, $R=R_n$, $t=t_n$ in (a); for
$h_n\ge h_*=\max\{64,8(1+C_\phi)\}$, $|b(t_n)|\ge3m_n/4$. By (a), $|b(s)|\ge5m_n/8>m_{n-1}$ for $s\in[t_n-\delta_n,t_n]\cap[0,t_n]$.
Since $|b(s)|\le\|u(s)\|_\infty$, and $\|u(s)\|_\infty\le m_{n-1}$ for $s\le t_{n-1}$ (with $m_{n-1}\ge m_0>\|u_0\|_\infty$ for $n=1$), the
interval $[t_n-\delta_n,t_n]$ lies in $(t_{n-1},t_n]$. On it, (a) gives $\|\nabla u(s)\|_2^2\ge c_1R_n(5m_n/8)^2$; integrate over the
interval and use $\int_0^{T_*}\|\nabla u\|_2^2\le E_0/2$.
(c) $R_n\ge\frac12e^{\kappa h_n}B_n/d_n$, and $d_n\le m_n^2$ for large $n$. If $B_nR_n\ge1$, $\delta_n\ge m_nR_n/(16C_1B_n^2)\ge
m_ne^{\kappa h_n}/(32C_1B_nd_n)\ge h_ne^{\kappa h_n}/(32C_1m_n^2)$; if $B_nR_n<1$, $\delta_n\ge m_nR_n^2/(16C_1B_n)\ge
m_nB_ne^{2\kappa h_n}/(64C_1d_n^2)\ge e^{2\kappa h_n}/(64C_1h_nm_n^2)$. For $t_{n-1}\le t<t_n$ with $n$ large,
$M(t)\ge m_{n-1}=m_{n+1}/4$ and $T_*-t\ge t_{n+1}-t_n\ge\delta_{n+1}$, so $M(t)^2(T_*-t)\ge c\,e^{\kappa h_{n+1}}/(16h_{n+1})$. $\square$

**Remark.** (i) This sharpens the persistence from Proposition 7(b) and $\|\nabla p\|_\infty\le C\Theta_0D$, which gives only
$M/(C\Theta_0D)$, by the factor $e^{\kappa h}$ when $\Theta_0R\ge1$: the frame moving with the local mean removes the
self-advection term. Under (FLAT$_0$) in regime (II) this case occurs eventually, since $B_nR_n\ge\frac12e^{\kappa h_n}B_n^2/d_n\ge
\frac12e^{\kappa h_n}/h_n^2$. A moving frame driven by a mollified velocity with prescribed terminal point is used by J. Yang
(Ann. Inst. H. Poincare Anal. Non Lineaire 39 (2022), as reported by the second-model audit; not read); I do not know a
source for the estimate in (b), (c). That $M(t)^2(T_*-t)\to\infty$ in regime (II) is already Proposition 7(c), with the bound
$M(t)^2(T_*-t)\ge(48\sup_{[t,T_*)}D/M^2)^{-1}$; part (c) bounds the same quantity below, for $t_{n-1}\le t<t_n$, in terms of the
flatness $h_{n+1}=m_{n+1}/\Theta_0(t_{n+1})$ of the next dyadic record instead, by a quantity that tends to infinity under (FLAT$_0$). The scalar rates of Remark (ii) after Proposition 14B have
$M^2\tau=\tau^{-1/2}$, $h=\ell^{1/2}$ and satisfy both bounds, with $\delta\asymp\tau^{3/2}\ell^{5/2}e^{\kappa\sqrt\ell}=o(\tau)$ and $\Theta_0R\ge1$.
(ii) The dissipation bound in (b) gives no contradiction by itself: when $B_nR_n\ge1$ its right side is at most
$Cm_n^3R_n^2/B_n^2$, and since $m_n^2R_n^3\le CE_0$ (Jensen on $B_{R_n}$), this is at most $CE_0^{2/3}h_n^2m_n^{-1/3}$, which is summable
over the geometric sequence $m_n$ because $h_n\le C\log(E_0m_n)$ (Proposition 14C(c)); when $B_nR_n<1$ it is at most
$m_n^3R_n^3/B_n<m_n^3/B_n^4=h_n^4/m_n$, also summable. So these bounds do not force divergence of the certified dissipation. A nonsummable lower bound for
$\int_{t_{n-1}}^{t_n}\|\nabla u\|_2^2$, for example $cE_0\log(m_n/m_{n-1})$, would give a contradiction with the energy inequality, but
no such bound is proved here.

**Remark (pressure impulse at flat records).** Let $t_n$, $x_n=x_*$, $R_n$ and $b=b(t_n)$ be as in the proof of Proposition
14D(b), write $v(x,\sigma)=u(x,t_n-\sigma)$, and consider only $n$ so large that $h_n\ge h_*$ (under (FLAT$_0$) this holds
eventually; large $n$ alone does not imply it). Then $|b|\ge3m_n/4$, so $e=b/|b|$ is defined. For $0\le\sigma\le\varsigma<t_n$ let
$q(\cdot,\sigma)$ be the law of $X_\sigma$, where $dX_\sigma=-v(X_\sigma,\sigma)\,d\sigma+\sqrt2\,dW_\sigma$ and $X_0$ has density
$\phi_{R_n}(\cdot-x_n)$. The drift is smooth, bounded and Lipschitz, $q$ solves $\partial_\sigma q=\Delta q+v\cdot\nabla q$, $q(\sigma)$ is a
probability density (for each Brownian path the flow preserves volume because $\operatorname{div}v=0$), and $q$ is nonnegative at
$\sigma=0$ and positive for $\sigma>0$.

(i) Impulse identity. In the backward age, $\partial_\sigma v=-\Delta v+(v\cdot\nabla)v+\nabla p$. Multiply
$\partial_\sigma(qv_i)$ by a cutoff $\chi_H$ equal to $1$ on $B_H(x_n)$, supported in $B_{2H}(x_n)$, with
$|\nabla\chi_H|\le C/H$ and $|\nabla^2\chi_H|\le C/H^2$, and integrate by parts. The diffusion terms cancel and the transport
terms combine to $\int\chi_Hv\cdot\nabla(qv_i)$, so that only cutoff errors of size $C(m_nH^{-2}+d_nH^{-1}+m_n^2H^{-1})$ remain
(since $\int q=1$), while $\nabla p$ is bounded by Lemma 3. Letting $H\to\infty$,
$I(\sigma):=\int q(x,\sigma)v(x,\sigma)\,dx=b+\int_0^\sigma F$, where $F(\sigma):=\int q(x,\sigma)\nabla p(x,t_n-\sigma)\,dx$. This is the
expectation of Ito's formula for $v$ along $X$. Related stochastic Lagrangian representations of Navier-Stokes are due to
Constantin and Iyer (Comm. Pure Appl. Math. 61 (2008), 330-345) and to Delbaen, Qiu and Tang (arXiv:1303.5329). I have not checked
these sources myself, and they do not contain the upper bound in (iii).

(ii) Lower bound. The same cutoff argument applied to $q^2$ gives $\frac{d}{d\sigma}\|q\|_2^2=-2\|\nabla q\|_2^2$. With Nash's
inequality $\|q\|_2^{10/3}\le C\|q\|_1^{4/3}\|\nabla q\|_2^2$ and $\|q\|_1=1$, this gives $\|q(\sigma)\|_2\le C\sigma^{-3/4}$ independently
of $v$. Hence $|I(\varsigma)|\le CE_0^{1/2}\varsigma^{-3/4}\le m_n/4$ for $\varsigma=\varsigma_n=KE_0^{2/3}m_n^{-4/3}$, with $K$ absolute.
Since $\varsigma_n\to0$ and $t_n\to T_*>0$, eventually $\varsigma_n<t_n$. Therefore
$$J_n:=-\int_0^{\varsigma_n}e\cdot F(\sigma)\,d\sigma=|b|-e\cdot I(\varsigma_n)\ge\frac{m_n}2,\qquad b=I(\varsigma_n)-\int_0^{\varsigma_n}F,\quad|I(\varsigma_n)|\le\frac{m_n}4.$$
So at a flat record the signed pressure impulse $J_n$ along the backward-diffusing packet, over the last $\varsigma_n$ units of
time, is at least $m_n/2$. The part of the mean carried from older data has norm at most $m_n/4$; it is not shown to vanish.

(iii) Upper bound. Write $m=m_n$, $B=B_n$, $d=d_n$, $w(x,z)=v(x-z)-v(x)$, $a=B/d$ and $V=\|\nabla q\|_1$, all at age $\sigma$.
Because $|K(z):w\otimes w|\le C|z|^{-4}\min(d^2|z|^2,4m^2)$, the integrals $\iint q(x)|K(z):w\otimes w|$ and
$\iint q(x-z)|K(z):w\otimes w|$ are at most $Cmd$. The substitution $(x,z)\mapsto(x-z,-z)$ reverses the sign of the odd kernel $K$
of Lemma 3 and preserves $w\otimes w$, so averaging gives
$F_k=\frac12\iint[q(x)-q(x-z)]K_{kij}(z)w_i(x,z)w_j(x,z)\,dz\,dx$. The increment bound in the proof of Proposition 14B(a) (dyadic
comparison of ball means, starting at radius $a$) gives $|w(x,z)|\le C\min\{d|z|,B[1+\log_+(|z|/a)]\}$. Together with
$\|q-q(\cdot-z)\|_1\le\min\{2,|z|V\}$, this gives
$|F|\le C\int_0^\infty\min\{2,rV\}\min\{d^2r^2,B^2[1+\log_+(r/a)]^2\}r^{-2}\,dr$.
If $aV\le1$, split at $a$ and $1/V$; if $aV>1$, split at $a$ and use $Bd<B^2V$. This yields
$|F|\le CB^2V[1+\log_+^3(d/(BV))]$.
Let $H(q)=\int q\log q$ and $\mathcal I(q)=\int|\nabla q|^2/q$. With $\beta_\varepsilon(r)=(r+\varepsilon)\log(r+\varepsilon)-\varepsilon\log\varepsilon$,
cutoffs at fixed $\varepsilon$ and then $\varepsilon\downarrow0$ (monotone convergence for the dissipation, domination by $|q\log q|+Cq$ at
the endpoints), we get $H(q(\varsigma))+\int_0^\varsigma\mathcal I(q)\,d\sigma=H(q(0))=H(\phi)-3\log R_n$. From the stochastic equation and the
$L^2$ triangle inequality, $Q(\sigma)^{1/2}:=(\int|x-x_n|^2q)^{1/2}\le R_n+m\sigma+\sqrt{6\sigma}$. Comparison with the Gaussian of the
same second moment gives $H(q)\ge-\frac32\log(2\pi eQ/3)$. Hence $\int_0^\varsigma\mathcal I\le C_\phi L_n$, with
$L_n=1+\log(1+(m\varsigma+\varsigma^{1/2})/R_n)$. Since $V^2\le\mathcal I$ (Cauchy-Schwarz with $\int q=1$),
$\int_0^\varsigma V\le C_\phi(\varsigma L_n)^{1/2}$.
The map $V\mapsto V[1+\log_+^3(d/(BV))]$ is not monotone, so the average bound cannot simply be inserted. Instead put
$\lambda=d\varsigma^{1/2}/B$ and $z=\varsigma^{1/2}V$. Using $\log_+(\lambda/z)\le\log_+\lambda+\log(1/z)$ and $z\log^3(1/z)\le27e^{-3}$ for
$z<1$, we get $z[1+\log_+^3(\lambda/z)]\le C[1+\log_+^3\lambda](1+z)$. Hence
$\int_0^\varsigma V[1+\log_+^3(d/(BV))]\,d\sigma\le C[1+\log_+^3\lambda](\varsigma^{1/2}+\int_0^\varsigma V)$, and with $\varsigma=\varsigma_n$
$$J_n\le CB_n^2\varsigma_n^{1/2}[1+\log_+^3(d_n\varsigma_n^{1/2}/B_n)]L_n^{1/2}.$$
The regularizations are indicated rather than written in full. The upper bound is used only to show that this route gives
no contradiction. The displayed upper and lower bounds are compatible. In regime (II), the right-hand side of the upper
bound divided by $m_n$ tends to infinity: by Proposition 14C(c), $B_n\ge cm_n/\log(E_0m_n)$, so
$B_n^2\varsigma_n^{1/2}/m_n\ge cK^{1/2}E_0^{1/3}m_n^{1/3}/\log^2(E_0m_n)\to\infty$. This does not show that $J_n/m_n$ itself diverges.
A bound $J_n\le CB_n$ on an infinite subsequence, with $C$ depending only on the datum, would give $h_n\le2C$ there and so exclude
(FLAT$_0$). It is not proved. The argument establishes the signed, time-integrated lower bound in (ii), but no pointwise sign for
the antisymmetrized kernel integrand and no decorrelation estimate sufficient to obtain that stronger upper bound.

### 7. Consequences of the plateau alternative

**Proposition 7.** Put $\epsilon_t(R)=\omega_t(RM/D)/M$. (a) For $s\le t$ and every $R>0$,
$\|\nabla p(s)\|_\infty\le(12\epsilon_t(R)+24/R)M(t)D(t)$. (b) $M(b)-M(a)\le\int_a^b\|\nabla p(s)\|_\infty ds$. Hence under
(UP), $M(t-A/D(t))/M(t)\to1$ for every fixed $A$, and the temporal certificate fails.

Proof. (a) In Lemma 3, $|K_{\cdot ij}w_iw_j|\le\frac3{2\pi}|w|^2|z|^{-4}$ and $\sup_{|z|=r}|w|\le\min(Dr,\omega_t(r),2M)$;
split the radial integral at $\omega_t(\rho)/D$ and at $\rho=RM/D$. (b) At a spatial maximum of $|u|^2$,
$u\cdot(u\cdot\nabla)u=0$ and $u\cdot\Delta u\le0$, so $\partial_t\frac12|u|^2\le\|u\|_\infty\|\nabla p\|_\infty$ there;
the upper right Dini derivative of $\|u(s)\|_\infty$ is at most $\|\nabla p(s)\|_\infty$. $\square$

**Proposition 7(c) (regime (II) is velocity Type II).** In regime (II), $M(t)^2(T_*-t)\to\infty$.

Proof. By (b) and $\|\nabla p\|_\infty\le24\|u\|_\infty\|\nabla u\|_\infty$ (Lemma 3), $0\le M(v)-M(u)\le\int_u^v24MD$ for
$u<v<T_*$, so $M\in AC_{loc}([0,T_*))$ with $0\le M'\le24MD$ a.e., and $\frac d{dt}M^{-2}\ge-48D/M^2$. Integrating on
$[t,b]$, $M(t)^{-2}\le M(b)^{-2}+48\int_t^bD/M^2$; let $b\uparrow T_*$ ($M(b)\to\infty$):
$M(t)^{-2}\le48(T_*-t)\sup_{[t,T_*)}D/M^2=o(T_*-t)$. $\square$

So a singularity with $\limsup M^2(T_*-t)<\infty$ lies in regime (I), where GOAL holds; this is a consequence, not an
assumption.

**Proposition 8 (Hessian at gradient records).** At a first crossing $(x_d,t_d)$ of $\|\nabla u\|_\infty$,
$|\nabla^2u|^2\le D^3+D|\nabla^2p|\le CD^3(1+\log^+(MH/D^2))$, $H$ the historical sup of $|\nabla^2u|$.

Proof. Let $A_{ij}=\partial_ju_i$, so $|\nabla^2u|=|\nabla A|$ and $M,D,H$ bound $|u|,|A|,|\nabla A|$ on $\mathbb R^3\times[0,t_d]$. Differentiating
the equation, $\frac12(\partial_t+u\cdot\nabla-\Delta)|A|^2=-A_{ij}A_{ik}A_{kj}-A_{ij}\partial_i\partial_jp-|\nabla A|^2$. At the first crossing
$|A|^2$ has a maximum over $\mathbb R^3\times[0,t_d]$ at $(x_d,t_d)$, so $\partial_t|A|^2\ge0$, $\nabla|A|^2=0$, $\Delta|A|^2\le0$ there, and
$|\nabla A|^2\le|A|^3+|A||\nabla^2p|=D^3+D|\nabla^2p|$. For the pressure, $-\Delta p=f:=\partial_iu_j\partial_ju_i=\partial_i\partial_j(u_iu_j)$, with $|f|\le D^2$,
$|\nabla f|\le2DH$ and $f\in L^1$. Hence $\partial_k\partial_lp(x)=c_0\delta_{kl}f(x)+\mathrm{p.v.}\int K(z)f(x-z)\,dz$ with $|c_0|\le1$ and a kernel $K=K_{kl}$
homogeneous of degree $-3$ with mean zero on spheres, so $|\partial^\beta K(z)|\le C|z|^{-3-|\beta|}$ for $|\beta|\le2$. Let $\rho=M/D$ and
$\epsilon=\min(\rho,D/H)$. On $\{|z|<\epsilon\}$ the mean-zero property gives $|\int K(z)(f(x-z)-f(x))dz|\le C\int_{|z|<\epsilon}|z|^{-3}2DH|z|\,dz\le CDH\epsilon\le CD^2$.
On $\{\epsilon<|z|<\rho\}$ the integral is at most $CD^2\log(\rho/\epsilon)=CD^2\log^+(MH/D^2)$. On $\{\rho<|z|<R\}$ write $f(x-z)=\partial_{z_i}\partial_{z_j}g_{ij}(z)$,
$g_{ij}(z)=(u_iu_j)(x-z)$, $|g|\le M^2$, $|\nabla g|\le2MD$, and integrate by parts twice: the volume term is at most
$C\int_{|z|>\rho}|z|^{-5}M^2dz=CM^2\rho^{-2}=CD^2$, the sphere terms on $|z|=\rho$ are at most $C\rho^{-3}MD\rho^2+C\rho^{-4}M^2\rho^2=CD^2$, and those on
$|z|=R$ are at most $C(MD/R+M^2/R^2)\to0$ as $R\to\infty$, while $\int_{|z|>R}|K||f|\le CR^{-3}\|f\|_1\to0$. So
$\|\nabla^2p\|_\infty\le CD^2(1+\log^+(MH/D^2))$ at every time $\le t_d$, and the claim follows. $\square$

None of these statements contradicts (UP); they show it is dynamically self-consistent over bounded Euler times.

### 8. A vorticity certificate for (L2M)

**Lemma (div-curl translation modulus).** If $V\in C^1(B_{4R})$, $\operatorname{div}V=0$, $|V|\le1$,
$\int_{B_{4R}}|\operatorname{curl}V|\le K$, then for $|h|\le R/2$:
$\int_{B_R}|V(y+h)-V(y)|^2\le C_R(1+K)|h|(1+\log(R/|h|))$.

Proof. Write $V=W+H$ with $W=\operatorname{curl}(\Phi*(\phi\operatorname{curl}V))$ for a cutoff $\phi$; $H$ is harmonic in
$B_{2R}$ with $\int_{B_{2R}}|H|\le C(R^3+RK)$, so its gradient is bounded on $B_{3R/2}$; $W$ is a convolution of a measure of
mass $K$ with $\nabla\Phi$, whose $L^1$ translation modulus on balls is $C|h|(1+\log(R/|h|))$. Use $|V|\le1$ to pass from
$L^1$ to $L^2$. $\square$

**Theorem 6 (vorticity certificate).** Let an admissible isotropic normalization satisfy
$$\text{(VL1)}\qquad\sup_n\sup_{-A\le\tau\le0}\frac{1}{M_n\ell_n^2}\int_{B_{R\ell_n}(x_n)}|\omega^\theta(x,s_n+\tau\ell_n/M_n)|dx<\infty$$
for all $R,A$. Then (L2M) holds, and with (L2-OSC) GOAL holds. If $r(x_n)/\ell_n$ is bounded, (VL1) follows from
$\int_{B_{R\ell_n}(x_n)}|\eta|\le C_{R,A}M_n\ell_n$, $\eta=\omega^\theta/r$.

Proof. The meridional field $u^{mer}=u^re_r+u^ze_z$ is divergence free with curl $\omega^\theta e_\theta$; apply the lemma to
its rescaling, and note that the swirl part is uniformly $o(1)$ (Theorem 3). $\square$

**Corollary 6A (one-sided vorticity certificate).** For an admissible isotropic normalization write $\varrho_n=r(x_n)$,
$z_n=x_{n,3}$, and for $R>0$ let $P_{n,R}=\{(r,z):r\ge0,\ |r-\varrho_n|\le R\ell_n,\ |z-z_n|\le R\ell_n\}$ in the meridional
half-plane. For $t\le t_n$ put $N^\pm_{n,R}(t)=(M_n\ell_n)^{-1}\int\!\!\int_{P_{n,R}}(\omega^\theta)_\pm(r,z,t)\,dr\,dz$. Then:
(a) $|N^+_{n,R}(t)-N^-_{n,R}(t)|\le8R$ and
$(M_n\ell_n^2)^{-1}\int_{B_{R\ell_n}(x_n)}|\omega^\theta(x,t)|\,dx\le16\pi R^2+4\pi R\min\{N^+_{n,R}(t),N^-_{n,R}(t)\}$.
(b) Hence (VL1), and so (L2M), holds if for all $R,A$ one has
$\sup_n\sup_{-A\le\tau\le0}\min\{N^+_{n,R},N^-_{n,R}\}(s_n+\tau\ell_n/M_n)<\infty$, in particular if one signed part of $\omega^\theta$
has bounded normalized meridional mass. If $\varrho_n\ge2R\ell_n$, then
$N^\pm_{n,R}(t)\le(RM_n\ell_n^2)^{-1}\int_{B_{3R\ell_n}(x_n)}(\omega^\theta)_\pm dx$; if $\varrho_n\le2R\ell_n$, then
$N^\pm_{n,R}(t)\le(2\pi M_n\ell_n)^{-1}\int_{B_{6R\ell_n}(x_n)}\eta_\pm\,dx$ with $\eta=\omega^\theta/r$.
(c) Consequently, in alternative (C) of Theorem 5, for every admissible isotropic normalization with (L2-OSC) there are
$R,A$, a subsequence and times $\tau_k\in[-A,0]$ at which $N^+_{n_k,R}$ and $N^-_{n_k,R}$ both tend to infinity while
their difference stays bounded by $8R$: on such windows the meridional vorticity has both signs, with normalized masses
that are unbounded and cancel up to $O(R)$.

Proof. (a) For $t<T_*$ the functions $u^r,u^z$ are smooth on $[0,\infty)\times\mathbb R$, and Green's theorem on the
rectangle $P=P_{n,R}$ gives $\int\!\!\int_P\omega^\theta\,dr\,dz=-\oint_{\partial P}(u^r\,dr+u^z\,dz)$; the perimeter of $P$ is at most
$8R\ell_n$ and $|u^r|^2+|u^z|^2\le M_n^2$ for $t\le t_n$, which gives the first claim. In cylindrical coordinates
$\int_{B_{R\ell_n}(x_n)}|\omega^\theta|\,dx=\int\!\!\int|\omega^\theta(r,z)|L(r,z)\,dr\,dz$, where $L(r,z)$ is the length of the part of the
horizontal circle of radius $r$ about the axis at height $z$ that lies in the ball; $L>0$ only on $P$. The ball meets that
plane in a disk of radius $\rho'\le R\ell_n$; if $r\le\rho'$ then $L\le2\pi r\le2\pi\rho'$, and if $r>\rho'$ the circle meets the disk in
one arc of angle $2\alpha$ with $\alpha\le\pi/2$ (the disk contains no two antipodal points of the circle) and $r\sin\alpha\le\rho'$,
so $L=2r\alpha\le\pi\rho'$. Hence the left side of the second claim is at most $2\pi R(N^++N^-)$, and
$N^++N^-\le2\min\{N^+,N^-\}+8R$. (b) The first sentence follows from (a) and Theorem 6. If $\varrho_n\ge2R\ell_n$, the wedge
$\{(r,\theta,z):(r,z)\in P,\ |\theta-\theta_n|\le R\ell_n/\varrho_n\}$ ($\theta_n$ the angle of $x_n$) lies in $B_{3R\ell_n}(x_n)$, since its points
have horizontal distance at most $R\ell_n+(\varrho_n+R\ell_n)R\ell_n/\varrho_n\le\frac52R\ell_n$ and vertical distance at most $R\ell_n$ from $x_n$,
and its integral of $(\omega^\theta)_\pm$ is at least $(\varrho_n-R\ell_n)\cdot2R\ell_n\varrho_n^{-1}\int\!\!\int_P(\omega^\theta)_\pm\ge R\ell_n\int\!\!\int_P(\omega^\theta)_\pm$. If
$\varrho_n\le2R\ell_n$, then $P\subset[0,3R\ell_n]\times[z_n-R\ell_n,z_n+R\ell_n]$, whose solid of revolution lies in $B_{6R\ell_n}(x_n)$, and
$\int\!\!\int(\omega^\theta)_\pm\,dr\,dz=(2\pi)^{-1}\int\eta_\pm\,dx$ over it. (c) If (C) holds, (L2M) fails, so (VL1) fails by Theorem 6 for
some $R,A$; by (a) the minimum in (b) is unbounded, and the difference is bounded by (a). $\square$

The cancellation in (c) is what the single-time test fields of Section 10 exhibit: on the core of Proposition 10',
$\omega^\theta=rF_N'(x_3)$ changes sign on every period of every mode. The swirl source $\partial_z(q^2)$ of $\eta$ is a
$z$-derivative, so on each line $r=\mathrm{const}$ where it does not vanish identically it takes both signs; no one-sided bound is derived in this report.

**Theorem 6' (time-integrated vorticity certificate).** Assume regime (II) and let an admissible isotropic
normalization satisfy, for all $R,A$,
$$\text{(VC)}\qquad\limsup_{n\to\infty}\ \ell_n^{-3}\int_{s_n-A\ell_n/M_n}^{s_n}\int_{B_{R\ell_n}(x_n)}|\omega^\theta(x,t)|\,dx\,dt<\infty$$
(for large $n$ the window lies in $[0,s_n]$, since the depth tends to infinity).
Then every joint subsequential limit has $\mathcal R=0$ (strong $L^2_{loc}$ convergence on $\mathbb R^3\times(-\infty,0)$), and the
limit is axisymmetric without swirl about a limiting axis if $r(x_n)/\ell_n$ stays bounded, and planar (invariant along a
limiting angular direction $e$, with no component along $e$) if $r(x_n)/\ell_n\to\infty$. If (W-OSC) of Lemma 11 also holds,
GOAL holds in the sense of Theorem 12 above, with an end-time shift chosen after the limit is known; this argument gives
no compactness of the terminal slices at the original $\tau=0$ (for trajectories Proposition 22 does: (VC) implies (L2M)). If the selection satisfies the terminal certificate
(OSC$_0$) of Theorem 17, an explicit rule computed from the meridional vorticity on the last Euler time gives GOAL in the
topology (ST) (Theorem 17(d)). If
$r(x_n)/\ell_n$ is bounded, (VC) follows from $\int_{s_n-A\ell_n/M_n}^{s_n}\int|\omega^\theta|r^{-2}dx\,dt\le C_A\ell_n$.

Proof. The left side of (VC) equals $\int_{-A}^0\int_{B_R}|\operatorname{curl}V_n|\,dy\,d\tau$ for the rescaled meridional field $V_n$.
The bound of the Lemma is linear in $K$, so integrating it in $\tau$ gives a space-time $L^2$ translation modulus for $V_n$,
hence for $U_n$ (the swirl part is uniformly $o(1)$). Then $\|U_n-U_n^\delta\|_{L^2(Q)}$ is small uniformly in $n$ as $\delta\to0$,
while $U_n^\delta$ converges locally uniformly for each $\delta$ (Lemma 11, after refining the given joint subsequence to one
along which Lemma 11 applies), so $U_n$ converges strongly in $L^2(Q)$ for every bounded cylinder $Q$ along the refinement.
This identifies the weak-* limit of $U_n\otimes U_n$ as $U\otimes U$, so $\mathcal R=0$, and strong convergence holds along the
original subsequence by Theorem 5(b). The symmetry passes to the limit as in the proof of Theorem 3. Apply Theorem 12. Near the axis use $|\omega^\theta|\le(r(x_n)/\ell_n+R)^2\ell_n^2|\omega^\theta|r^{-2}$
on $B_{R\ell_n}(x_n)$. $\square$

The selection here is physical (triples with $O_\epsilon(x_n,s_n,\ell_n)\ge cM_n$ for fixed $\epsilon,c$, which exist whenever
(FLAT) of Proposition 14 fails); (VC) is the extra hypothesis. The only global information available,
$\int_0^{T_*}\int|\omega^\theta|r^{-2}dx\,dt<\infty$ under $\|\omega^\theta_0\|_1<\infty$, makes the window integrals tend to zero
but gives no rate relative to $\ell_n$. The terminal limitation of the argument above is real at the functional level (for
Navier-Stokes trajectories it is removed by Lemma 21 and Proposition 22): the divergence-free fields
$Z_n=\frac12(\sin y_2+\chi(n\tau)\sin(ny_2))e_1$ with $\chi\in C_c^\infty(-1,1)$, $0\le\chi\le1$, $\chi(0)=1$, are bounded by $1$, have
bounded space-time $L^1_{loc}$ curl, convergent fixed mollifications, and a strong space-time limit $\frac12\sin y_2\,e_1$, while
their terminal slices have no strongly convergent subsequence in $L^2(B_1)$.

**Lemma 9 (global growth of $\|\eta\|_{L^1}$).** Assume in addition $\eta_0\in L^1$, $\omega_0\in L^2$, and that
$\eta(t)\in L^1$ with $\sup_{[0,t]}\|\eta\|_{L^1}<\infty$ for $t<T_*$. Then
$\|\eta(t)\|_{L^1}\le\|\eta_0\|_{L^1}+(E_0\|\omega_0\|_2^2)^{1/2}+E_0D(t)^{1/2}$.

Proof. $\eta$ solves $(\partial_t+u\cdot\nabla)\eta=(\Delta+\frac2r\partial_r)\eta+\partial_z(q^2)$, $q=u^\theta/r$. Testing with
a cutoff times a smoothed sign, the transport and diffusion parts do not increase $\|\eta\|_{L^1}$ (the $\frac2r\partial_r$
term contributes $-4\pi\int\phi_\epsilon(\eta(0,z))dz\le0$ in the meridional variables), so
$\|\eta(t)\|_1\le\|\eta_0\|_1+2\int_0^t\|q\|_2\|\partial_zq\|_2$. The axisymmetric Hardy identity
$|\nabla v|^2\ge(v^\theta/r)^2$ gives $\|q\|_2\le\|\nabla u\|_2$, $\|\partial_zq\|_2\le\|\nabla\omega\|_2$, and the enstrophy
inequality gives $\int_0^t\|\nabla\omega\|_2^2\le\frac12\|\omega_0\|_2^2+\frac12E_0D(t)$. $\square$

Near the axis Theorem 6 needs $\int_{B_{R\ell}}|\eta|\le CM\ell$ with $M\ell\le ML_E=(6E_0M/\pi)^{1/3}$, while Lemma 9 and
Lemma 2 give only $E_0D^{1/2}\ge cE_0^{5/6}M^{5/6}$: the deficit is the factor $(E_0M)^{1/2}\to\infty$ (both quantities
are dimensionless). Since $\|\eta\|_{L^1}$ is invariant under the Navier-Stokes scaling while $M\ell\to\infty$ at every
scale with retained oscillation in regime (II), if (C) holds then every such normalization with bounded rescaled axis
distance has, for some $R,A$, an unbounded ratio $\sup_\tau\int_{B_{R\ell_n}}|\eta|/(M_n\ell_n)$. This is a consequence of
(C) for each such normalization, not an unconditional growth statement.

**Lemma 9' (an a priori $L^1$ bound with swirl).** Let $w=\omega^\theta$ and $\phi\in C_c^\infty$, $0\le\phi\le1$. For $t<T_*$,
$$\int\phi|w(t)|+\int_0^t\!\!\int\phi\frac{|w|}{r^2}\le\int\phi|w_0|+\frac{E_0}2+\|\nabla\phi\|_\infty E_0(t/2)^{1/2}+\|\Delta\phi\|_2(tE_0/2)^{1/2};$$
if $\|w_0\|_1<\infty$, then $\|w(t)\|_1+\int_0^t\int|w|r^{-2}\le\|w_0\|_1+E_0/2=:K$ and $\int_0^{T_*}\|\eta\|_1^2dt\le K^2$.

Proof. $w=\partial_zu^r-\partial_ru^z$ solves $(\partial_t+b\cdot\nabla)w=(\Delta-r^{-2})w+(u^r/r)w+2q\partial_zu^\theta$. Test with
$\phi$ times a smoothed sign, first on $\{r>\delta\}$ and then $\delta\to0$ ($w=O(r)$ at the axis, so the boundary terms vanish
and $|w|/r^2$ is locally integrable).
The axisymmetric identity for $|\nabla v|^2$ gives $\|u^r/r\|_2\le\|\nabla b\|_2=\|w\|_2$ ($b=u^re_r+u^ze_z$),
$\|q\|_2^2+\|\partial_zu^\theta\|_2^2\le\|\nabla(u^\theta e_\theta)\|_2^2$, and $\|\nabla u\|_2^2=\|\nabla b\|_2^2+\|\nabla(u^\theta e_\theta)\|_2^2$;
so the reaction terms are bounded by $\|\nabla u\|_2^2$, whose time integral is $\le E_0/2$. The cutoff terms are bounded
by $\|\nabla\phi\|_\infty\|u\|_2\|w\|_2+\|\Delta\phi\|_2\|w\|_2$, with $\int_0^t\|w\|_2\le(tE_0/2)^{1/2}$. For the global form take
$\phi_R=\chi(\cdot/R)$: $\|\nabla\phi_R\|_\infty=O(R^{-1})$, $\|\Delta\phi_R\|_2=O(R^{-1/2})$, and use Fatou. Finally
$\|\eta\|_1^2\le\|w\|_1\int|w|r^{-2}$. $\square$

This bound is supercritical: $\int\phi|w|$ and $\int\!\int|w|r^{-2}$ have the dimension of a length. At a scale $\ell$
with retained oscillation the rescaled meridional vorticity (the curl of the rescaled meridional field $b/M$, which is
what Theorem 6 uses; the full rescaled curl also contains the swirl vorticity and is not controlled by this bound)
satisfies $\int_{B_R}|\operatorname{curl}V_n|\le K/(M\ell^2)$ with $M\ell^2\le CE_0^{2/3}M^{-1/3}\to0$. Near the axis a window
average of $\int|w|r^{-2}$ of size $O(M)$ (a critical requirement that integrability on $[0,T_*)$ does not provide) would
give the time-integrated certificate (VC) of Theorem 6', hence a vanishing Reynolds defect and, with (W-OSC), GOAL
in the sense of Theorem 12; it would not give the supremum in time that (VL1) requires.

**Remark (accumulated swirl source in (C)).** Write $F=\partial_z(q^2)$ and $\mathcal I(t)=\int_0^t\!\int|F|\,dx\,ds$. In alternative
(C), take an admissible isotropic normalization with (L2-OSC) and $R$, a subsequence and times $t'_n=s_n+\tau_n\ell_n/M_n$,
$\tau_n\in[-A,0]$, as in Corollary 6A(c), so that $m_n=N^+_{n,R}(t'_n)+N^-_{n,R}(t'_n)\to\infty$. Then there are $e_n\to0$ with
$\mathcal I(t'_n)\ge2\pi M_n\ell_n(m_n-e_n)$, and with $J_n=M_n\ell_n(m_n-e_n)$ and $\rho_n=E_0/(2\pi J_n)\to0$,
$$\int_0^{t'_n}\!\!\int_{\{r<\rho_n\}}|F|\,dx\,ds\ge\pi J_n\to\infty.$$
No integrability of $\eta_0$ is assumed.

Proof. Split $\eta=\eta^d+Z$, where $\eta^d$ solves the homogeneous equation $(\partial_t+u\cdot\nabla)\eta^d=(\Delta+\frac2r\partial_r)\eta^d$
with datum $\eta_0$ and $Z$ solves the equation of $\eta$ with zero datum. The datum $\eta_0=\omega_0^\theta/r$ is bounded
($\omega_0^\theta$ is smooth and vanishes on the axis), so $|\eta^d|\le C_0:=\|\eta_0\|_\infty$ by the maximum principle. The
homogeneous propagator is positive and contracts $L^1(dx)$ (the computation in the proof of Lemma 9, for compactly
supported data, and density), and $\|F(t)\|_1\le2\|q\|_2\|\partial_zq\|_2$ is integrable on $[0,t]$ for $t<T_*$; so Duhamel's
formula gives $\|Z(t)\|_1\le\mathcal I(t)$. Let $E_n$ be the solid of revolution of $P_{n,R}$ and $d_n=\varrho_n/\ell_n$. Exactly,
$\int_{E_n}|\eta(t'_n)|\,dx=2\pi\int\!\!\int_{P_{n,R}}|\omega^\theta|\,dr\,dz=2\pi M_n\ell_nm_n$, and $|E_n|\le8\pi R^2(d_n+R)\ell_n^3$. By (L2-OSC)
at radius $R'$, eventually $\int_{B_{R'\ell_n}(x_n)}|u(s_n)|^2\ge\frac c2M_n^2\ell_n^3$, and the same holds on each rotated copy of this
ball about the axis; disjoint copies and energy give $(1+d_n)M_n^2\ell_n^3\le C_{R'}E_0/c$. Hence
$e_n:=C_0|E_n|/(2\pi M_n\ell_n)\le C_{R,R'}C_0E_0/(cM_n^3\ell_n)\to0$, and $\mathcal I(t'_n)\ge\int_{E_n}|Z(t'_n)|\,dx\ge2\pi M_n\ell_n(m_n-e_n)$.
Next $r|F|=2|q||\partial_zu^\theta|\le|\nabla(u^\theta e_\theta)|^2\le|\nabla u|^2$ (the identities in the proof of Lemma 9'), so
$\int_0^{T_*}\!\int r|F|\,dx\,dt\le E_0/2$ and the part of $\mathcal I(t'_n)$ in $\{r\ge\rho\}$ is at most $E_0/(2\rho)$; take $\rho=\rho_n$. $\square$

This is a necessary condition, not a contradiction. The source part of Lemma 9 gives, without integrability of $\eta_0$,
$\mathcal I(t)\le(E_0\|\omega_0\|_2^2+E_0^2D(t))^{1/2}$, while $|\omega^\theta|\le\sqrt2D$ gives $J_n\le M_n\ell_nm_n\le4\sqrt2R^2\ell_n^2D(t'_n)$, so
$J_n/(E_0^2D(t'_n))^{1/2}\le C_RD_n^{1/2}\ell_n^2/E_0\le C_RM_n\ell_n^2/E_0\to0$ (certification gives $M_n\ell_n^2\le CE_0^{2/3}M_n^{-1/3}$): the
required production is far below the ceiling. The tube is coarse: $\rho_n/\ell_n\ge cE_0/(D_n\ell_n^3)\to\infty$.
The production is accumulated over the whole history and is not assigned to the window: the same source may feed many
windows, and diffusion moves vorticity between particle labels, so Lemma 26A (which concerns labels) does not locate it.

### 9. Other normalization classes

Every rescaling $U_n=B_n^{-1}(u(x_n+\ell_ny+V_nT_n\tau,s_n+T_n\tau)-V_n)$ with a constant Galilean frame has
$\sup|U_n|\ge M(s_n)/(2B_n)$ over the available past ($u\in C_0$ gives the value $-V_n/B_n$ at infinity, and a historical
maximum gives $(M(s_n)-|V_n|)/B_n$). If $B_n/M(s_n)\to\infty$, convergent globally bounded sequences have constant
(possibly nonzero) limits, so nonconstant limits need $B_n\asymp M(s_n)$. Rescalings with $B_n=o(M(s_n))$
(local-amplitude rescalings) are globally unbounded. If $|u-V|\le CB$ only on a ball of $Q$ rescaled radii, split the
pressure source with a cutoff fixed in the source variable: the far part of the rescaled pressure gradient on $B_R$ is
$\int_{|z|>Q}K(y-z)v(z)\otimes v(z)dz$, $v=(u-V)/B$, with $|K|\lesssim|z|^{-4}$, so it is spatially uniform up to
$C|y|(M/B)^2/Q^2$ and has size at most $C(M/B)^2/Q$. A quiet zone $Q\gg(M/B)^2$ is thus sufficient (not necessary) for
the far field to disappear; identifying the limit pressure as canonical still requires compactness of the quadratic
source (e.g. (L2M)), and a nonvanishing uniform part has a limit only if it converges, which the tail bounds do not give. Otherwise limits may carry a uniform force $a(\tau)$, i.e. a parasitic
pressure $-a(\tau)\cdot y$, for which spatially constant time-dependent fields are solutions and rigidity fails; removing
it requires the accelerating frame $W=U(y+X)-X'$, $X''=a$, which is excluded (and has bounded frame velocity only if $a$
has a bounded primitive). Nothing in the a priori estimates produces quiet zones. Equal-amplitude
anisotropic rescalings (in regime (II), with a spatial modulus holding over the whole physical history) whose limits
oscillate in the thin variable reduce to isotropic ones at the thin scale (the isotropic rescaling inherits the modulus
and the oscillation, and is admissible); limits independent of the thin variable lead to a
singular hydrostatic-type balance for which no physical certificate was found.

**Proposition 15 (boosted Lipschitz-scale criterion; conditional).** Let $t_n\uparrow T_*$, $s_n\le t_n$, $D_n=D(t_n)$,
$B_n>0$ with $D_n/B_n^2\to0$, $s_nD_n\to\infty$, $\ell_n=B_n/D_n$, $V_n=u(x_n,s_n)$, and
$v_n(y,\tau)=B_n^{-1}(u(x_n+\ell_ny+V_n\tau/D_n,s_n+\tau/D_n)-V_n)$. If for constants $C$, $c>0$ and sequences
$R_n,A_n\to\infty$ ($A_n\le s_nD_n$), $\varepsilon_n\to0$,
$$\sup_{B_{R_n}\times[-A_n,0]}|v_n|\le C,\qquad\sup_{B_1}|v_n(\cdot,0)|\ge c,\qquad
\int_{-A_n}^0\!\!\int_{|y|>R_n}|v_n|^2|y|^{-4}\,dy\,d\tau\le\varepsilon_n,$$
then a subsequence converges locally uniformly on $\mathbb R^3\times(-\infty,0]$ to a field $v$ with $|v|\le C$ everywhere,
$\operatorname{Lip}_yv\le1$, $v(0,0)=0$, $\sup_{B_1}|v(\cdot,0)|\ge c$, solving the Euler equations with canonical pressure; so GOAL
holds. None of the three hypotheses is derived here, and (FLAT), which concerns amplitude $M$ only, neither implies
nor excludes them at amplitudes $B_n=o(M)$.

Proof. The constant boost is an exact symmetry ($\beta_n=1$, $\nu_n=D_n/B_n^2$, pressure $p/B_n^2$, no inertial term), and
the cross terms $R_iR_j(V_iv_j)$ and $R_iR_j(V_iV_j)$ are constants because $\nabla\cdot v_n=0$, so the pressure is canonical for
$v_n$. Physical times are $\le t_n$, so $|\nabla_yv_n|\le1$. Split the pressure source with a cutoff equal to $1$ on $B_{Q/2}$;
on $B_{Q/4}$ the far part of $\nabla P_n$ has kernel $O(|y-z|^{-4})$, and by the first and third hypotheses its
$L^1([-A_0,0];L^\infty(B_{Q/4}))$ norm is $O(C^2A_0/Q+\varepsilon_n)$. The near part is bounded in $L^\infty_\tau L^2_y$. Hence spatial
mollifications $v_n^\delta$ (with $|v_n-v_n^\delta|\le\delta$) are asymptotically equicontinuous in time on compact sets, and the
Arzela-Ascoli theorem with a diagonal argument gives local uniform convergence through $\tau=0$. The bounds pass to the
limit, the nonlinearity converges uniformly, $\nu_n\to0$, the near pressure converges by stability of $R_iR_j$ under
bounded weak-* convergence, and the far parts vanish as $Q\to\infty$. $\square$

The sequence $v_n$ is not globally bounded when $|V_n|/B_n\to\infty$; the third hypothesis is the weighted far-tail
control that replaces global boundedness. Since $|v_n|\le(|u|+|V_n|)/B_n\le2M(t_n)/B_n$ on the whole available past,
the third hypothesis holds, with some $\varepsilon_n\to0$, as soon as $R_n\gg A_n(M(t_n)/B_n)^2$.
The hypotheses are tests on the physical velocity over prescribed windows, so a selection by them is not
retrospective.

**Lemma 15' (Lagrangian time control; what it does not give).** In the setting of Proposition 15 let $A,\rho\ge1$,
$R_1=(\rho+A)e^A+A+1$, $C_0=\|\nabla\rho_1\|_{L^1}$ for a fixed mollifier $\rho_1$ supported in $B_1$, $C_0\nu_n\le1$, and
$\kappa=2(C_0\nu_n)^{1/2}(1+A)+A\pi$. If $|v_n(\cdot,0)|\le C$ on $B_{R_1}$, $|\nabla P_n|\le\pi$ on $B_{R_1+1}\times[-A,0]$ and
$\kappa\le1$, then $|v_n|\le C+1$ on $B_\rho\times[-A,0]$.

Proof. With $\delta=(C_0\nu_n)^{1/2}$ and $v^\delta=\rho_\delta*v_n$, along a trajectory $Y'=v_n(Y,\sigma)$ one has
$\frac d{d\sigma}v^\delta(Y,\sigma)=[v_n\cdot\nabla v^\delta-(v_n\cdot\nabla v_n)^\delta]-\nabla P_n^\delta+\nu_n\Delta v^\delta$; the commutator is
$\int\rho_\delta(Y-z)((v_n(Y)-v_n(z))\cdot\nabla)v_n(z)dz$, of size $\le\delta$, and $|\nu_n\Delta v^\delta|\le C_0\nu_n/\delta$. With
$|v_n-v^\delta|\le\delta$, the velocity changes by at most $\kappa$ along any trajectory that stays in $B_{R_1}$ during
$[-A,0]$. The trajectory through $(0,0)$ then has speed $\le1$ and stays in $B_A$; any trajectory through
$(y,\tau)\in B_\rho\times[-A,0]$ stays within $(\rho+A)e^A$ of it by the Lipschitz bound and Gronwall, hence in $B_{R_1}$,
and $|v_n(y,\tau)|\le|v_n(Y(0),0)|+\kappa\le C+1$. $\square$

So the time part of the first hypothesis of Proposition 15 follows from its $\tau=0$ part on a ball of radius
$\ge(\rho_n+A_n)e^{A_n}+A_n+1$ if $A_n\sup|\nabla P_n|\to0$ there and $A_n\nu_n^{1/2}\to0$. Then the third hypothesis is not
needed: the limit solves $\partial_\tau v+\nabla\cdot(v\otimes v)=0$, and its canonical pressure is a harmonic BMO function,
hence constant. This reduction is not useful a priori: under the second hypothesis with constant $c$ the increment
integral $\int|u(x_n-z)-u(x_n)|^2|z|^{-4}dz$ that bounds $|\nabla p(x_n)|$ is at least $\frac{\pi c^5}{384}B_nD_n$, hence bounded below by a positive constant
in rescaled units, so smallness of $\nabla P_n$ would need cancellation in the pressure integral that nothing here
provides (it does occur for exact shear flows). The $\tau=0$ part (a quiet zone around a Lipschitz-saturated
oscillation) is not given by the present estimates, and increment behaviour alone cannot give it. For the divergence-free
functional field $f_K=\sum_{k=0}^Kb^{-ks}\cos(b^kx_1)e_2$ ($0<s<1$, $b$ an integer with $b^s\ge8$, $h_K=b^{-K}$; infinite energy, not
axisymmetric, not an NS trajectory) one has $|f_K(x+h)-f_K(x)|\le C|h|^s$ for $|h|\le1$, and $\operatorname{osc}_If_K\ge c|I|^s$ for every
interval $I$ in the $x_1$ direction with $2\pi h_K\le|I|\le1$ (constants depending on $b,s$). For the lower bound choose $q\le K$ with
$2\pi b^{-q}\le|I|<2\pi b^{1-q}$ and an extremum $x_*$ of $\cos(b^qx_1)$ with $x_*\pm h\in I$, $h=\pi/(2b^q)$; in the centred second
difference at $x_*$ the mode $q$ contributes $2b^{-qs}$, the modes $k<q$ at most $\frac{\pi^2}{4(b^{2-s}-1)}b^{-qs}$ and the modes $k>q$ at most
$\frac4{b^s-1}b^{-qs}$, together less than $b^{-qs}$, and a second difference is at most twice the oscillation. Hence
$D_K=\sup|\nabla f_K|\ge ch_K^{s-1}$ and $|\nabla^2f_K|\le Ch_K^{s-2}$. If $x_K$, $B_K\le C$, $\ell_K=B_K/D_K$ satisfied the second
hypothesis of Proposition 15 and the $\tau=0$ part of the first on radii $R_K\to\infty$ (with $f_K$ in place of the velocity), then
$B_K\le C\ell_K^s$; if $\ell_K\ge c'h_K$, the oscillation on the interval of length $\min(2R_K\ell_K,1)$ around $x_K$ is
$\ge c\min(R_K,\ell_K^{-1})^sB_K$; if $\ell_K/h_K\to0$, Taylor's formula gives $|\partial_1f_K|\ge cD_K/4$ with a fixed sign on an interval
of radius $c'h_K$ around $x_K$, and the normalized increment over the radius $\min(R_K\ell_K,c'h_K)$ is $\ge c\min(R_K,c'h_K/\ell_K)$. In
both cases the normalized amplitude on $B_{R_K}$ is unbounded. This obstructs only arguments based on the increment behaviour.

**Weighted relative energy.** Fix $3<\alpha<5$ and $w_L(y)=(1+|y|^2/L^2)^{-\alpha/2}$; then $|\nabla w_L|\le C_\alpha w_L/L$,
$|\Delta w_L|\le C_\alpha w_L/L^2$, $\int w_L=c_\alpha L^3$, and $w_1\le w_L\le L^\alpha w_1$ for $L\ge1$.

**Lemma 16 (weighted canonical pressure).** For bounded $F$, $R_iR_jF_{ij}$ has a representative $q$ with
$\|q\|_{L^2(w_L)}\le C_\alpha\|F\|_{L^2(w_L)}$. In particular a harmonic canonical pressure of a bounded tensor is constant.

Proof. Take $L=1$ and a scalar input $f$ for $T=R_iR_j$ (kernel $K(z)=(3z_iz_j-\delta_{ij}|z|^2)/(4\pi|z|^5)$ off the origin, plus a
multiple of $\delta_0$; multiplier of modulus $\le1$). With $\chi$ a cutoff equal to $1$ on $B_1$ and supported in $B_2$, put
$T_0f=Tf-\int K(-z)(1-\chi(z))f(z)dz$. Decompose $f=\sum_jf_j$ dyadically ($f_j$ supported where $|z|\sim2^j$), use output annuli
$A_k$ ($|y|\sim2^k$) and $a_j=2^{-\alpha j/2}\|f_j\|_2$. For $|k-j|\le3$ the $L^2$ bound gives $2^{-\alpha k/2}\|T_0f_j\|_{L^2(A_k)}\le Ca_j$;
for $k\ge j+4$, $|Tf_j|\le C2^{-3k}2^{3j/2}\|f_j\|_2$ and the constant is $\le C2^{-3j/2}\|f_j\|_2$, giving $C2^{-(\alpha-3)(k-j)/2}a_j$;
for $j\ge k+4$, $|K(y-z)-K(-z)|\le C2^k2^{-4j}$ gives $C2^{-(5-\alpha)(j-k)/2}a_j$. Young's inequality for the summable kernel in
$k-j$ gives $\|T_0f\|_{L^2(w_1)}\le C\|f\|_{L^2(w_1)}$. For bounded $f$ the truncations converge in $L^2(w_1)$ and, tested against
mean-zero $\psi\in C_c^\infty$ (for which $T\psi=O(|y|^{-4})$), the limit represents $R_iR_jf$. A harmonic representative satisfies
$|\nabla q(x)|\le CR^{-5/2}\|q\|_{L^2(B_R(x))}\le C_xR^{(\alpha-5)/2}\|q\|_{L^2(w_1)}\to0$. $\square$

**Proposition 16 (relative energy and its consequences).** (a) Let $v$ be a smooth solution on $\mathbb R^3\times[a,b]$ of the
Navier-Stokes equations with viscosity $\nu\ge0$ and canonical pressure, with $|v|\le K$ ($K\ge1$) and $v$, $\nabla v$, $\nabla^2v$,
$\partial_\tau v$ bounded, and let $V\in C^1$ be a divergence-free solution of the Euler equations with canonical pressure, $|V|\le K$, with
$\nabla V,\partial_\tau V$ bounded, $H(\tau)=\|\nabla V(\tau)\|_\infty$. Then $E_L=\int w_L|v-V|^2$ satisfies
$E_L'\le C_\alpha(H+K/L+\nu/L^2)E_L+C_\alpha\nu L^3H^2$.
(b) If an admissible isotropic normalization satisfies $\int_{-A}^{-A/2}\|U_n-V\|^2_{L^2(B_R)}\to0$ for all $R$, for such a $V$ with $K=1$
on $[-A,0]$, then $\sup_{[-A/2,0]}\|U_n-V\|_{L^2(B_R)}\to0$, in particular at $\tau=0$; and a classical $V$ that is constant at one time is
constant. Hence, if the defect-free limit of Theorem 6' or Theorem 12 is classical on a terminal interval $[-A,0]$, the end-time shift is
unnecessary and, with the physical selection $O_\epsilon(x_n,s_n,\ell_n)\ge cM_n$, the limit is nonconstant at $\tau=0$; the convergence is
then (ST) together with uniform-in-time $L^2_{loc}$ convergence on $[-A/2,0]$ only. This hypothesis
concerns the unknown limit and is not a certificate on the physical records. (Theorem 17 removes the retrospective
shift without it, at the price of a terminal slice within one Euler time before $s_n$.)
(c) Under (FLAT), with $\mathcal R$ the defect of a joint limit and $e_L(\tau)=\int w_L\operatorname{tr}\mathcal R(\tau)$,
$e_1(t)\le C_\alpha(1+t-a)^\alpha e_1(a)$ for all $a<t$ in a set of full measure in $(-\infty,0)$: a defect cannot vanish on a
past interval and reappear.

Proof. (a) $z=v-V$ solves $\partial_\tau z+v\cdot\nabla z+z\cdot\nabla V+\nabla q=\nu\Delta z+\nu\Delta V$ with $q=R_iR_j(v_iv_j-V_iV_j)$, and
$\|q\|_{L^2(w_L)}\le2C_\alpha KE_L^{1/2}$ by Lemma 16. Testing with $w_L\chi(\cdot/R)z$, keeping both viscous terms integrated by parts once (so no second
derivative of $V$ enters), and letting $R\to\infty$ (the terms containing $\nabla\chi(\cdot/R)$, among them
$-\nu\int w_Lz_i\partial_jV_i\partial_j\chi(\cdot/R)$, are bounded by
$C\int_{R<|y|<2R}w_L(|z|^2(K+1)+|q||z|+\nu(|\nabla z|+|\nabla V|)|z|)R^{-1}$ and vanish since $z$, $\nabla z$, $\nabla V$ are bounded, $w_L$
is integrable and $q\in L^2(w_L)$; the remaining $-\frac\nu2\int\nabla|z|^2\cdot\nabla w_L$ is integrated by parts without cutoff; the
pressure pairing is the $BMO$-$\mathcal H^1$ pairing with a compactly
supported mean-zero function, so constants do not matter) gives
$\frac12E_L'+\nu\int w_L|\nabla z|^2=\frac12\int|z|^2v\cdot\nabla w_L-\int w_Lz_iz_j\partial_jV_i+\int qz\cdot\nabla w_L-\nu\int w_L\nabla z:\nabla V+\frac\nu2\int|z|^2\Delta w_L-\nu\int z_i\partial_jV_i\partial_jw_L$,
and each term is bounded as claimed, the gradient term being absorbed. (b) $\int_{-A}^{-A/2}E_{n,1}\to0$ by the uniform bound and the
integrable weight, so $E_{n,1}(a_n)\to0$ for some $a_n\in[-A,-A/2]$, and Gronwall with $\nu_n\to0$ gives $\sup_{[a_n,0]}E_{n,1}\to0$.
For constancy apply (a) with $\nu=0$ to the time-reversed solution $-V(-\sigma)$ and a constant. (c) Under (FLAT), by Proposition 14(e), the joint
limit is $\bar U=b$ for a constant $b$, $|b|\le1$, and $\operatorname{tr}\mathcal R=\operatorname{w*lim}|U_n-b|^2$ in $L^\infty(\mathbb R^3\times(-\infty,0))$; $\mathcal R$
is positive semidefinite, so $\operatorname{tr}\mathcal R\ge0$, and $e_L(\tau)$ is defined for a.e. $\tau$ by Fubini. Each $U_n$ is a rescaling of the
smooth solution on $[0,s_n]$, so it is smooth with bounded $\nabla U_n,\nabla^2U_n,\partial_\tau U_n$ on its window, and $V=b$ is a
classical Euler solution with constant canonical pressure and $H=0$. By (a) with $K=1$, $E_{n,L}(\tau)=\int w_L|U_n(\tau)-b|^2$ satisfies
$E_{n,L}'\le\lambda_{n,L}E_{n,L}$ with $\lambda_{n,L}=C_\alpha(L^{-1}+\nu_nL^{-2})$, so $f_n=e^{-\lambda_{n,L}\tau}E_{n,L}$ is nonincreasing on the window
and $\int f_n\chi'\,d\tau\ge0$ for every $\chi\in C_c^\infty((-\infty,0))$ with $\chi\ge0$, once the window contains the support of $\chi$.
Since $e^{-\lambda_{n,L}\tau}\chi'\to e^{-\lambda_L\tau}\chi'$ uniformly, $\lambda_L=C_\alpha/L$, $0\le E_{n,L}\le4\int w_L$, and $\int E_{n,L}g\,d\tau\to\int e_Lg\,d\tau$ for
$g\in L^1$ (test the weak-* convergence with $g(\tau)w_L(y)$), the limit gives $\int e^{-\lambda_L\tau}e_L\chi'\,d\tau\ge0$. So the
distributional derivative of $f=e^{-\lambda_L\tau}e_L$ is $\le0$; its mollifications are nonincreasing and converge to $f$ at
the Lebesgue points of $e_L$, so $f$ is nonincreasing on the set $E_L$ of these points, which has full measure. Put
$E=\bigcap_{k\ge0}E_{2^k}$. For $a<t$ in $E$ choose $L=2^k$ with $1+t-a\le L<2(1+t-a)$; since $w_1\le w_L\le L^\alpha w_1$,
$e_1(t)\le e_L(t)\le e^{C_\alpha(t-a)/L}e_L(a)\le e^{C_\alpha}2^\alpha(1+t-a)^\alpha e_1(a)$, which is the claim with the constant of the statement renamed. If $e_1=0$ a.e. on an interval $(a_1,a_2)$,
choosing $a\in E\cap(a_1,a_2)$ with $e_1(a)=0$, arbitrarily close to $a_1$, gives $e_1(t)=0$ for every $t\in E$, $t>a$; as $w_1>0$ and
$\mathcal R\ge0$, $\mathcal R=0$ a.e. on $\mathbb R^3\times(a_1,0)$. $\square$

The inequality in (c) is a genuine restriction beyond the Euler-Reynolds equation (the constant-mean triple with
$\mathcal R=\frac{\epsilon^2}2e^{2\tau}e_3\otimes e_3$ violates it), but it excludes neither (FLAT) nor stationary defects: the exact axisymmetric
swirl-free solutions $v_n=[e^{\nu_n(\tau+n)\Delta_{x'}}(c_0\cos r+c_1\cos nr)]e_3$, $\nu_n=n^{-4}$, $\tau\in[-n,0]$, have constant canonical
pressure, converge weakly to the nonconstant classical mean $c_0\cos r\,e_3$ and carry the stationary defect $\frac{c_1^2}2e_3\otimes e_3$.

### 9A. Terminal slices and anchors selected from each trajectory

Theorem 12 and Theorem 6' obtain strong convergence of a terminal slice only after an end-time shift taken from a
full-measure set that is determined by the weak limit. Here that choice is replaced by rules that are
applied to each rescaled trajectory $U_n$ separately: a threshold rule for the terminal slice (Theorem 17) and a
maximization rule for the anchor (Corollary 18). The nonconstancy of the limit at the selected slice is proved instead of
being selected for. Write $T_n=\ell_n/M_n$ and, for $f\in L^\infty(\mathbb R^3)$, $R\ge1$, $\rho>0$,
$$m_R(f;\rho)=\sup_{|h|\le\rho}\int_{B_R}|f(y+h)-f(y)|^2dy ,$$
for a normalization defined on $\mathbb R^3\times[-2,0]$
$$\varpi_{n,R}(\rho)=\sup_{|k|\le\rho}\int_{-2}^0\int_{B_R}|U_n(y+k,\tau)-U_n(y,\tau)|^2dy\,d\tau ,$$
and $\tilde O(x,s,\rho)=\sum_{m\ge0}2^{-m}O_{2^{-m}}(x,s,\rho)$ with $O_\epsilon$ as in Proposition 14. Since
$O_\epsilon(x,s,\rho)\le\|u(s)\|_\infty$, $\tilde O(x,s,\rho)\le2M(s)$. Both $m_R(f;\cdot)$ and $\varpi_{n,R}$ are nondecreasing.

**Lemma 17 (supremum of translation differences).** For $f\in L^\infty(\mathbb R^3)$, $R\ge1$ and $0<\rho\le1$,
$$m_R(f;\rho)\le256\fint_{B_{2\rho}}\int_{B_{R+1}}|f(y+k)-f(y)|^2dy\,dk .$$

Proof. Let $g(v)=\|f(\cdot+v)-f\|_{L^2(B_{R+1})}$. For $|h|\le\rho$ and $k\in B_\rho$,
$\|f(\cdot+h)-f\|_{L^2(B_R)}\le\|f(\cdot+h)-f(\cdot+k)\|_{L^2(B_R)}+\|f(\cdot+k)-f\|_{L^2(B_R)}\le g(h-k)+g(k)$, since
$\int_{B_R}|f(y+h)-f(y+k)|^2dy=\int_{B_R(k)}|f(z+h-k)-f(z)|^2dz$ and $B_R(k)\subset B_{R+1}$. Average over $k\in B_\rho$:
$\{h-k:k\in B_\rho\}=B_\rho(h)\subset B_{2\rho}$ and $B_\rho\subset B_{2\rho}$, so both averages are at most
$(|B_{2\rho}|/|B_\rho|)\fint_{B_{2\rho}}g=8\fint_{B_{2\rho}}g$. Hence $\|f(\cdot+h)-f\|_{L^2(B_R)}\le16\fint_{B_{2\rho}}g\le16(\fint_{B_{2\rho}}g^2)^{1/2}$;
square and take the supremum over $h$. $\square$

**Theorem 17 (terminal selection by a rule on each trajectory).** Assume regime (II). Let
$(t_n,s_n,x_n,\ell_n)$ be an admissible isotropic normalization with the terminal certificate
$$\text{(OSC}_0)\qquad O_\epsilon(x_n,s_n,\ell_n)\ge cM_n\ \text{ for all }n\quad\text{or}\quad\tilde O(x_n,s_n,\ell_n)\ge cM_n\ \text{ for all }n,$$
for fixed $\epsilon\in(0,1]$, $c>0$, and let a joint subsequence $\Lambda$ as in Theorem 12 have $\mathcal R=0$ a.e. Restrict to
indices with $2T_n\le s_n$.
(a) (Rule.) For $j\ge1$ let $\varrho_{n,j}$ be the largest $2^{-i}$, $i\ge0$ an integer, with $\varpi_{n,R+1}(2^{1-i})\le8^{-j}$ for all
$R\le j$, and put
$$k_n(\tau)=\sum_{j\ge1}\sum_{R=1}^{j}\frac{4^j}{256\,j^2}\,m_R\big(U_n(\cdot,\tau);\varrho_{n,j}\big),\qquad
\theta_n=\min\{\theta\in[0,1]:k_n(-\theta)\le2\}.$$
Then $\varrho_{n,j}$ and $\theta_n$ are well defined, and they are functions of $U_n$ on $\mathbb R^3\times[-2,0]$ alone.
(b) (Uniform modulus along $\Lambda$.) For every $R$, $\varpi_R(\rho):=\sup_{n\in\Lambda}\varpi_{n,R}(\rho)\to0$ as $\rho\to0$. Hence
there is a largest $\varrho_j=2^{-i}$ with $\varpi_{R+1}(2^{1-i})\le8^{-j}$ for all $R\le j$, and $\varrho_{n,j}\ge\varrho_j$ for $n\in\Lambda$.
(c) (Conclusion.) Let $s'_n=s_n-\theta_nT_n$ and $U'_n(y,\tau)=U_n(y,\tau-\theta_n)=M_n^{-1}u(x_n+\ell_ny,s'_n+T_n\tau)$, an
admissible isotropic normalization with the same $t_n,x_n,\ell_n$. Along a further subsequence of $\Lambda$, $\theta_n\to\theta\in[0,1]$
and: $U'_n\to U':=\bar U(\cdot,\cdot-\theta)$ in the sense (ST); $|U'|\le1$; $U'(\cdot,0)$ is not a.e. constant; $U'$ is a weak Euler
solution on $\mathbb R^3\times(-\infty,0]$ with canonical pressure in the time-integrated form of Theorem 12, and has the swirl and
axis dichotomy of Theorem 12. Hence GOAL holds for this normalization in the topology (ST), with terminal time $s'_n$.
(d) (Explicit rule under (VC).) If (VC) of Theorem 6' holds, let $V_n$ be the rescaled meridional field of the proof of
Theorem 6',
$$Q_{n,R}(\tau)=\int_{B_{4R}}|\operatorname{curl}V_n(y,\tau)|dy=\frac1{M_n\ell_n^2}\int_{B_{4R\ell_n}(x_n)}|\omega^\theta(x,s_n+T_n\tau)|dx,
\qquad A_{n,R}=\int_{-1}^0Q_{n,R}(\tau)\,d\tau,$$
$$\kappa_n(\tau)=\sum_{R\ge1}\frac{2^{-R}\,Q_{n,R}(\tau)}{1+A_{n,R}},\qquad\theta_n=\min\{\theta\in[0,1]:\kappa_n(-\theta)\le2\}.$$
Then all conclusions of (c) hold, and $\theta_n$ is computed from the meridional vorticity of the physical solution on the
time interval $[s_n-T_n,s_n]$ alone ((VC) enters only the proof).

Proof. (a) For fixed $n$, $|U_n(y+k,\tau)-U_n(y,\tau)|\le\|\nabla U_n\|_{L^\infty(\mathbb R^3\times[-2,0])}|k|$ with
$\|\nabla U_n\|_\infty\le\ell_nD_n/M_n<\infty$, so $\varpi_{n,R}(\rho)\le2|B_R|\|\nabla U_n\|_\infty^2\rho^2\to0$. Since $\varpi_{n,R}$ is
nondecreasing, the integers $i$ satisfying the condition form a nonempty set closed under $i\mapsto i+1$, and $\varrho_{n,j}$ is
$2^{-i}$ for its least element. Each $U_n$ is smooth and bounded with bounded derivatives on $\mathbb R^3\times[-2,0]$, so
$(h,\tau)\mapsto\int_{B_R}|U_n(y+h,\tau)-U_n(y,\tau)|^2dy$ is continuous and $\tau\mapsto m_R(U_n(\tau);\rho)$ is continuous
(supremum over a compact set). Thus $k_n$ is lower semicontinuous with values in $[0,\infty]$ and
$\{\theta\in[0,1]:k_n(-\theta)\le2\}$ is closed. By Lemma 17 ($\varrho_{n,j}\le1$) and Fubini,
$\int_{-1}^0m_R(U_n(\tau);\varrho_{n,j})d\tau\le256\,\varpi_{n,R+1}(2\varrho_{n,j})\le256\cdot8^{-j}$ for $R\le j$, hence
$\int_{-1}^0k_n\le\sum_jj\cdot j^{-2}2^{-j}\le1$, and $\{\theta\in[0,1]:k_n(-\theta)\le2\}$ has measure at least $1/2$; it is nonempty.
(b) By the first part of the proof of Theorem 12, $U_n\to\bar U$ in $L^2(B_{R}\times(-2,0))$ along $\Lambda$. Given $\delta>0$ take $N$ with
$\|U_n-\bar U\|_{L^2(B_{R+1}\times(-2,0))}<\delta$ for $n\ge N$ in $\Lambda$. For $|k|\le1$ the translate of $U_n-\bar U$ restricted to
$B_R$ is controlled by its norm on $B_{R+1}$, so for such $n$ the space-time translation difference of $U_n$ on $B_R\times(-2,0)$ is,
in $L^2$, at most $2\delta$ plus that of $\bar U$; the finitely many $U_n$ with $n<N$, and $\bar U$, are bounded functions on a
bounded set, whose translation differences tend to $0$ with $|k|$. Hence $\limsup_{\rho\to0}\varpi_R(\rho)\le4\delta^2$ for every
$\delta$. The existence of $\varrho_j$ follows as in (a), and every $i$ admissible for $\varpi$ is admissible for $\varpi_n\le\varpi$, so
$\varrho_{n,j}\ge\varrho_j$.
(c) Step 1 (compact terminal slices). Let $f_n=U_n(\cdot,-\theta_n)$, $n\in\Lambda$. From $k_n(-\theta_n)\le2$,
$m_R(f_n;\varrho_{n,j})\le512\,j^24^{-j}$ for $R\le j$, hence by (b) and monotonicity $m_R(f_n;\varrho_j)\le512\,j^24^{-j}$, and
$\sup_{n\in\Lambda}m_R(f_n;\rho)\to0$ as $\rho\to0$ for every $R$. By Minkowski's inequality
$\|f_n-f_n^\delta\|_{L^2(B_R)}\le m_R(f_n;\delta)^{1/2}$ for $\delta\le1$, uniformly small in $n$; the mollified functions $f_n^\delta$ are
bounded by $1$ with gradients bounded by $C/\delta$, hence precompact in $C(\bar B_R)$. So $(f_n)$ is totally bounded in $L^2(B_R)$ for
every $R$, and a diagonal subsequence converges in $L^2_{loc}$ to some $f$; pass also to $\theta_n\to\theta$.
Step 2 (identification). By Lemma 11, $U_n^\delta\to W^\delta$ locally uniformly on $\mathbb R^3\times(-\infty,0]$ and $W^\delta$ is
continuous, so $f_n^\delta=U_n^\delta(\cdot,-\theta_n)\to W^\delta(-\theta)$ locally uniformly; also $f_n^\delta\to f^\delta$. Hence
$f^\delta=W^\delta(-\theta)$ for every $\delta$, and $f=W(-\theta)=\bar U(-\theta)$ a.e.
Step 3 (space-time convergence). For $R,A$:
$\|U'_n-U'\|_{L^2(B_R\times(-A,0))}\le\|U_n-\bar U\|_{L^2(B_R\times(-A-1,0))}+\|\bar U(\cdot,\cdot-\theta_n)-\bar U(\cdot,\cdot-\theta)\|_{L^2(B_R\times(-A,0))}$.
The first term tends to $0$ by the first part of the proof of Theorem 12; the second by continuity of time translations in $L^2(B_R\times(-A-2,0))$ for the
bounded function $\bar U$. With Steps 1 and 2, $U'_n\to U'$ in the sense (ST).
Step 4 (nonconstancy). Suppose $\bar U(-\theta)=b$ a.e. for a constant $b$, $|b|\le1$. Since $|U_n-b|\le2$, $w_1$ is integrable and
$f_n\to b$ in $L^2_{loc}$, $E_n:=\int w_1|f_n-b|^2\to0$. If $\theta_n>0$, apply Proposition 16(a) on $[-\theta_n,0]$ with $v=U_n$
($\nu=\nu_n$, $K=1$; the regularity hypotheses hold for each $n$, as noted in (a)), $V\equiv b$ ($H=0$) and $L=1$:
$E_1'\le C_\alpha(1+\nu_n)E_1$, so $\int w_1|U_n(\cdot,0)-b|^2\le e^{C_\alpha(1+\nu_n)}E_n\to0$ (trivially if $\theta_n=0$). Since
$w_1\ge c>0$ on $B_2$ and, for $|y|\le1$, $|U_n^{\epsilon'}(y,0)-b|\le\|\rho_{\epsilon'}\|_{L^2}\|U_n(\cdot,0)-b\|_{L^2(B_{\epsilon'}(y))}$ with
$B_{\epsilon'}(y)\subset B_2$, $U_n^{\epsilon'}(\cdot,0)\to b$ uniformly on $B_1$ for every $\epsilon'\in(0,1]$. By scaling,
$O_{\epsilon'}(x_n,s_n,\ell_n)/M_n=\big(\fint_{B_1}|U_n^{\epsilon'}(y,0)-(U_n^{\epsilon'}(\cdot,0))_{B_1}|^2dy\big)^{1/2}\to0$ for every such
$\epsilon'$, and $\tilde O(x_n,s_n,\ell_n)/M_n\to0$ by dominated convergence of the series (its terms are at most $2^{-m}$). Either form of
(OSC$_0$) is contradicted. So $U'(0)=\bar U(-\theta)$ is not a.e. constant. Quantitatively, with $E_n(\tau;b)=\int w_1|U_n(\tau)-b|^2$:
for $|b|\le1$ and $0<\epsilon'\le1$, Jensen's inequality, the minimizing property of the mean and $w_1\ge5^{-\alpha/2}$ on $B_2$ give
$O_{\epsilon'}(x_n,s_n,\ell_n)/M_n\le C_\alpha E_n(0;b)^{1/2}$ and $\tilde O(x_n,s_n,\ell_n)/M_n\le2C_\alpha E_n(0;b)^{1/2}$; with
$E_n(0;b)\le e^{C_\alpha(1+\nu_n)}E_n(-\theta_n;b)$ and $\nu_n\le1$, (OSC$_0$) gives $\inf_{|b|\le1}\int w_1|f_n-b|^2\ge c_*>0$ ($c_*$ depending
only on $c,\alpha$), and in the limit $\int w_1|U'(0)-b|^2\ge c_*$ for every $|b|\le1$.
Step 5 (equation and symmetry). $U'$ is the time translate of $\bar U$, so the limit equation and the symmetry argument in the proof of Theorem 12
apply (they use only $\mathcal R=0$ and $S(t_n)/M_n\to0$). Admissibility of $U'_n$: $s'_n\le s_n\le t_n$, $s'_n/T_n\ge s_n/T_n-1\to\infty$.
(d) Theorem 6' gives $\mathcal R=0$ along every joint subsequence. For each $n$, $Q_{n,R}$ is continuous and $A_{n,R}<\infty$, so
$\kappa_n$ is lower semicontinuous, and $\int_{-1}^0\kappa_n=\sum_R2^{-R}A_{n,R}/(1+A_{n,R})\le1$; so $\theta_n$ is well defined. By the
Jacobians of the proof of Theorem 6', $A_{n,R}=\ell_n^{-3}\int_{s_n-T_n}^{s_n}\int_{B_{4R\ell_n}(x_n)}|\omega^\theta|dx\,dt$, so (VC) with
$A=1$ and radius $4R$ gives $C_R:=\sup_nA_{n,R}<\infty$. At $\tau=-\theta_n$, $Q_{n,R}(-\theta_n)\le2^{R+1}(1+A_{n,R})\le2^{R+1}(1+C_R)$ for
every $R$, and the Lemma of Section 8 gives $m_R(V_n(-\theta_n);\rho)\le C_R'\rho(1+\log(R/\rho))$ for $\rho\le R/2$, uniformly in $n$ (the bound is
increasing in $|h|$ on $(0,R/2]$). As $|U_n-V_n|\le S(t_n)/M_n\to0$ uniformly,
$m_R(U_n(-\theta_n);\rho)\le2m_R(V_n(-\theta_n);\rho)+8|B_R|S(t_n)^2/M_n^2$; total boundedness in Step 1 of (c) holds with this
vanishing error (finitely many $n$ are handled individually). Steps 2 to 5 of (c) apply verbatim. $\square$

**Corollary 18 (anchor selection by a rule; GOAL in (ST) in alternative (B*)).** Assume regime (II), let
$(t_n,s_n,x_n,\ell_n)$ be an admissible isotropic normalization, and let a joint subsequence $\Lambda$ as in Theorem 12 have
$\mathcal R=0$ a.e. and $W(\tau_*)$ not a.e. constant for some $\tau_*\le0$. For $n$ with $4T_n\le s_n$ let $(y_n,\tau_n)$ be the
maximizer of
$$\Psi_n(y,\tau)=e^{-|y|-|\tau|}\,\tilde O(x_n+\ell_ny,\,s_n+T_n\tau,\,\ell_n)/M_n\qquad\text{over }y\in\mathbb R^3,\ -s_n/(2T_n)\le\tau\le0$$
singled out by a tie-break fixed in advance: among all maximizers take the least $\tau$, then successively the least $y_1$, $y_2$, $y_3$
($(0,0)$ if $\Psi_n\equiv0$). Then $|y_n|+|\tau_n|$ is bounded for large $n\in\Lambda$; the re-anchored normalization
$(t_n,\ s_n+\tau_nT_n,\ x_n+\ell_ny_n,\ \ell_n)$ is admissible (along the whole sequence), satisfies (OSC$_0$) in the $\tilde O$ form for large $n\in\Lambda$, and has
a joint subsequence with $\mathcal R=0$; Theorem 17 applies to it. Hence GOAL holds in the topology (ST) for the normalization
obtained from $(t_n,s_n,x_n,\ell_n)$ by two rules, the maximization above and the threshold rule of Theorem 17(a), neither of
which uses the limit.

Proof. $\tilde O(x,s,\ell_n)$ is continuous in $(x,s)\in\mathbb R^3\times[0,t_n]$ ($u$ is bounded and uniformly continuous there, and
the series converges uniformly), and $\Psi_n\le2e^{-|y|-|\tau|}$; so if $\sup\Psi_n>0$ it is attained on the compact set where
$2e^{-|y|-|\tau|}\ge\sup\Psi_n/2$; the set of maximizers is then nonempty and compact, and the successive minimizations of the
continuous functions $\tau,y_1,y_2,y_3$ over it are attained on nonempty compact sets, which determines $(y_n,\tau_n)$. Lower bound: $W(\tau_*)$ is not a.e. constant on some unit ball $B_1(y_0)$ (a function that is a.e.
constant on every unit ball is a.e. constant), and since $W^{2^{-m}}(\tau_*)\to W(\tau_*)$ in $L^2(B_1(y_0))$, $W^{2^{-m}}(\tau_*)$ is not
constant on $B_1(y_0)$ for some $m$. By Lemma 11 and scaling,
$O_{2^{-m}}(x_n+\ell_ny_0,s_n+T_n\tau_*,\ell_n)/M_n=\big(\fint_{B_1(y_0)}|U_n^{2^{-m}}(y,\tau_*)-(U_n^{2^{-m}}(\tau_*))_{B_1(y_0)}|^2\big)^{1/2}\to a>0$
along $\Lambda$, so $\Psi_n(y_0,\tau_*)\ge c_1:=2^{-m-1}ae^{-|y_0|-|\tau_*|}$ for large $n\in\Lambda$ (the depth tends to infinity, so
$|\tau_*|\le s_n/(2T_n)$ and $(y_0,\tau_*)$ is in the domain for large $n$). Then $2e^{-|y_n|-|\tau_n|}\ge\Psi_n(y_n,\tau_n)\ge c_1$, so $|y_n|+|\tau_n|\le K:=\log(2/c_1)$, and
$\tilde O(x_n+\ell_ny_n,s_n+T_n\tau_n,\ell_n)\ge e^{|y_n|+|\tau_n|}\Psi_n(y_n,\tau_n)M_n\ge c_1M_n$. Pass to $\Lambda'\subset\Lambda$ with
$(y_n,\tau_n)\to(y_\#,\tau_\#)$ and put $U^\#_n(y,\tau)=U_n(y+y_n,\tau+\tau_n)$. Admissibility, for every $n$ with $4T_n\le s_n$ and not only along $\Lambda$: same $t_n,\ell_n$; the terminal time
$s_n+\tau_nT_n\le s_n\le t_n$, and by the constraint on $\tau$, $(s_n+\tau_nT_n)/T_n\ge s_n/(2T_n)\to\infty$ and $2T_n\le s_n+\tau_nT_n$.
Convergence along $\Lambda'$: $\|U^\#_n-\bar U(\cdot+y_\#,\cdot+\tau_\#)\|_{L^2(B_R\times(-A,0))}\le\|U_n-\bar U\|_{L^2(B_{R+K}\times(-A-K,0))}
+\|\bar U(\cdot+y_n,\cdot+\tau_n)-\bar U(\cdot+y_\#,\cdot+\tau_\#)\|_{L^2(B_R\times(-A,0))}\to0$ (the first part of the proof of Theorem 12, and continuity of
translations of the bounded function $\bar U$; all times involved are $\le0$). The mollified fields
$U^{\#,\delta}_n(y,\tau)=U_n^\delta(y+y_n,\tau+\tau_n)$ converge locally uniformly to $W^\delta(y+y_\#,\tau+\tau_\#)$ (locally uniform
convergence and uniform continuity of $W^\delta$ on compact sets), which with $|U_n|\le1$ and $\|\phi-\phi*\rho_\delta\|_1\to0$ gives
$U^\#_n(\tau)\rightharpoonup^*W(\tau+\tau_\#)(\cdot+y_\#)$ for every $\tau\le0$; the strong convergence gives convergence of the velocity
tensor with $\mathcal R^\#=0$. So $\Lambda'$ is a joint subsequence as in Theorem 12 for $U^\#_n$, with $\mathcal R^\#=0$, and
(OSC$_0$) holds with $\tilde O$ and $c=c_1$ for large $n\in\Lambda'$. Apply Theorem 17. $\square$

Remarks. (i) Combined with the physical selection in the paragraph after Theorem 6' (record times $t_n$ and triples with
$O_\epsilon(x_n,s_n,\ell_n)\ge cM_n$, which exist if (FLAT) fails), Theorem 17(d) gives: (OSC$_0$) and (VC) together imply GOAL in the topology (ST) ((VC) alone allows constant
limits), with the terminal time placed within one Euler time before $s_n$ by an explicit rule computed from the meridional
vorticity of the physical solution on that Euler time and from nothing else. The rule of (a) is equally explicit but less transparent physically. Neither shift is chosen from the
limit or chosen to avoid a trivial limit; nonconstancy is a consequence of (OSC$_0$) and the relative-energy inequality (a limit
that is constant at a strongly converging slice stays constant later). The two weaknesses of Theorem 6' recorded in its
statement are therefore removed. Proposition 22 gives more: (VC) implies (L2M), so (VC) and (OSC$_0$) give GOAL in
$C([-A,0];L^2_{loc})$ at the original terminal time $s_n$, with no terminal-slice rule (Proposition 22(c)). What remains is
that (VC) is a hypothesis on the selected physical normalizations. The family $Z_n$ of Section 8 is consistent with this: the
local $L^1$ norm of its curl at time $\tau$ is at least $c_Rn\chi(n\tau)-C_R$, so the rule of (d) selects slices at which its high
mode has amplitude $O(1/n)$.
(ii) The sequence $(\varrho_j)$ of (b) enters only the proof; the rule of (a) uses each $U_n$ on $\mathbb R^3\times[-2,0]$ and nothing
else, and the rule of (d) uses the meridional vorticity of each $U_n$ on $\mathbb R^3\times[-1,0]$ and nothing else. The constants $\epsilon$ (or the series $\tilde O$) and $c$ of (OSC$_0$) enter only the hypothesis.
(iii) By Corollary 18, in alternative (B*) of Corollary 13 GOAL holds in the topology (ST) for a normalization obtained from the
(B*) normalization by rules computed from the physical solution: the end-time shift of Theorem 12 and the anchor are no longer
taken from the limit. The (B*) normalization itself remains existential, as in alternative (B) of Theorem 5,
but membership in (B*) is characterized through a joint subsequential limit. The trichotomy (A)/(B*)/(C*) is unchanged, and so is the first missing implication (exclusion of (C*)).

### 9B. The swirl source and an exterior vorticity certificate

For an admissible isotropic normalization $(t_n,s_n,x_n,\ell_n)$ the physical axis becomes the line $\mathcal A_n$ parallel to
$e_3$ at distance $d_n=r(x_n)/\ell_n$ from $0$; write $r_n(y)=r(x_n+\ell_ny)/\ell_n=\operatorname{dist}(y,\mathcal A_n)$ and
$\partial_{r_n}$ for the radial derivative about $\mathcal A_n$. With $q=u^\theta/r$, $\eta=\omega^\theta/r$, put
$q_n=(\ell_n/M_n)q(x_n+\ell_ny,s_n+T_n\tau)$, $\eta_n=(\ell_n^2/M_n)\eta(x_n+\ell_ny,s_n+T_n\tau)$ and
$$\sigma_n=\frac{\ell_nD_n}{M_n},\qquad g_n=\frac G{M_n\ell_n},\qquad\delta_n=\sigma_ng_n=\frac{GD_n}{M_n^2}.$$
Admissibility gives $\sigma_n\ge c$; in regime (II) $\delta_n\to0$. $V_n$ denotes the rescaled meridional field,
$\operatorname{curl}V_n=(\ell_n/M_n)\omega^\theta e_\theta=r_n\eta_ne_\theta$.

**Lemma 19 (the rescaled swirl source).** Assume regime (II) and let the normalization be admissible. For
$-s_n/T_n\le\tau\le0$:
(a) $\partial_\tau\eta_n+V_n\cdot\nabla\eta_n=\nu_n(\Delta+2r_n^{-1}\partial_{r_n})\eta_n+\partial_{y_3}(q_n^2)$;
(b) $|q_n|\le\min(\sigma_n,g_nr_n^{-2})$ and $|\partial_{y_3}q_n|\le\sigma_nr_n^{-1}$;
(c) for every ball $B_R(y_0)$ and $h>0$: $\int_{B_R(y_0)}q_n^2\le4\pi R\delta_n$, $|\partial_{y_3}(q_n^2)|\le2\delta_nr_n^{-3}$,
$\int_{B_R(y_0)\cap\{r_n\ge h\}}|\partial_{y_3}(q_n^2)|\le8\pi R\delta_n/h$, and $\int_{B_R(y_0)}|\partial_{y_3}(q_n^2)|\le16\pi R\sigma_n\delta_n^{1/2}$.
Hence, uniformly in $\tau$, $q_n^2\to0$ in $L^1_{loc}$, the source $\partial_{y_3}(q_n^2)$ tends to $0$ in $W^{-1,1}_{loc}$ and uniformly
on $\{r_n\ge h\}$; these estimates do not give a uniform bound for its total variation. The rescaled swirl core radius
$(G/D_n)^{1/2}/\ell_n$ is at most $c^{-1}(GD_n)^{1/2}/M_n\to0$. If $G=0$, then $q_n=0$ and everything is trivial.

Proof. (a) The physical equation is $\partial_t\eta+u^{mer}\cdot\nabla\eta=(\Delta+\frac2r\partial_r)\eta+\partial_z(q^2)$; after the change
of variables each of its four terms is multiplied by the same factor $\ell_n^3/M_n^2$. (b) Since $u^\theta$ vanishes on the axis
and $|\nabla u|\le D_n$ on $[0,t_n]$, $|u^\theta|\le D_nr$; the circulation maximum principle gives $|q|\le G/r^2$; and
$|\partial_zu^\theta|\le D_n$ gives $|\partial_zq|\le D_n/r$. Multiply by $\ell_n/M_n$, resp. $\ell_n^2/M_n$, and use $r=\ell_nr_n$.
(c) A ball of radius $R$ lies in a slab of thickness $2R$, so $\int_{B_R(y_0)}F(r_n)\le4\pi R\int_0^\infty F(\lambda)\lambda\,d\lambda$ for
$F\ge0$. With $a^2=g_n/\sigma_n$: $\int_0^\infty\min(\sigma_n^2,g_n^2\lambda^{-4})\lambda\,d\lambda=\sigma_n^2a^2/2+g_n^2/(2a^2)=\delta_n$;
$|\partial_{y_3}(q_n^2)|\le2\sigma_n\lambda^{-1}\min(\sigma_n,g_n\lambda^{-2})\le2\delta_n\lambda^{-3}$ at $r_n=\lambda$; $\int_h^\infty2\delta_n\lambda^{-2}d\lambda=2\delta_n/h$;
and $\int_0^\infty2\sigma_n\min(\sigma_n,g_n\lambda^{-2})d\lambda=4\sigma_n\delta_n^{1/2}$. The $W^{-1,1}$ statement follows by integrating by
parts in $y_3$, and the core bound from $\ell_n\ge cM_n/D_n$. $\square$

**Proposition 20 (exterior vorticity certificate).** Assume regime (II) and let an admissible isotropic normalization satisfy,
for all $R,A,h>0$,
$$\text{(EC)}\qquad\limsup_{n\to\infty}\ \ell_n^{-3}\int_{s_n-AT_n}^{s_n}\int_{B_{R\ell_n}(x_n)\cap\{r>h\ell_n\}}|\omega^\theta(x,t)|\,dx\,dt<\infty .$$
(a) Along every joint subsequence as in Theorem 12, $\mathcal R=0$, with the symmetry of Theorem 6'. With (OSC$_0$),
Theorem 17(a)-(c) applies: GOAL holds in the topology (ST).
(b) With $Q^e_{n,R}(\tau)=\int_{B_{4R}\cap\{r_n>1/R\}}|\operatorname{curl}V_n(\tau)|$, $A^e_{n,R}=\int_{-1}^0Q^e_{n,R}$,
$\kappa^e_n=\sum_{R\ge1}2^{-R}Q^e_{n,R}/(1+A^e_{n,R})$ and $\theta_n=\min\{\theta\in[0,1]:\kappa^e_n(-\theta)\le2\}$, (EC) and (OSC$_0$) give
all conclusions of Theorem 17(c); this rule uses only the meridional vorticity in $\{r>\ell_n/R\}$ on $[s_n-T_n,s_n]$.
(c) (VC) implies (EC), and they coincide when $d_n\to\infty$; the constants in (EC) may blow up as $h\to0$, and nothing is
assumed in the tubes $\{r\le h\ell_n\}$.
(d) If (C*) holds, every admissible isotropic normalization with (OSC$_0$) has $\sigma_n\to\infty$, and (EC) fails along each
of its subsequences; in (C*-D) such normalizations exist.

Proof. Scaling the Lemma of Section 8 (with $R=1$) by $y=y_0+\rho y'$ preserves $|V|\le1$ and $\operatorname{div}V=0$ and multiplies the
curl integral by $\rho^{-2}$; so if $\int_{B_{4\rho}(y_0)}|\operatorname{curl}V|\le K$, then
$\int_{B_\rho(y_0)}|V(y+k)-V(y)|^2dy\le C_1(\rho^2+K)|k|(1+\log(\rho/|k|))$ for $|k|\le\rho/2$. (a) Refine a joint subsequence so that
Lemma 11 holds and either $d_n\to\infty$ (put $\mathcal A=\emptyset$) or $\mathcal A_n$ converges to a vertical line $\mathcal A$. Fix
$R\ge1$, $A>0$, $h\in(0,1]$, $K=\bar B_R\cap\{\operatorname{dist}(\cdot,\mathcal A)\ge h\}$, and cover $K$ by $m$ balls $B_\rho(y_i)$, $y_i\in K$,
$\rho=h/16$. For large $n$, $B_{4\rho}(y_i)\subset B_{R+1}\cap\{r_n>h/2\}$, whose time-integrated curl over $(-A,0)$ is the (EC) quantity
with radius $R+1$ and $h/2$. Summing the scaled estimate over $i$ and integrating in time gives a space-time translation
modulus of $V_n$ on $K\times(-A,0)$, uniform in large $n$; since the swirl part is uniformly $o(1)$, the argument of
Theorem 6' (Minkowski for $U_n-U_n^\delta$, locally uniform convergence of $U_n^\delta$ by Lemma 11) gives $U_n\to\bar U$ in
$L^2(K\times(-A,0))$. The tube $B_R\cap\{\operatorname{dist}(\cdot,\mathcal A)<h\}$ has volume at most $2\pi Rh^2$ and $|U_n-\bar U|\le2$, so
$\limsup\|U_n-\bar U\|^2_{L^2(B_R\times(-A,0))}\le8\pi ARh^2$ for every $h$: $U_n\to\bar U$ strongly and $\mathcal R=0$. Theorem 17(a)-(c)
needs only this and (OSC$_0$). (b) Discard finitely many indices so that $s_n\ge2T_n$. As in Theorem 17(d), $\int_{-1}^0\kappa^e_n\le1$, $\theta_n$ is well defined, and (EC) with $A=1$, radius $4R$
and $h=1/R$ gives $C_R=\sup_nA^e_{n,R}<\infty$, so $Q^e_{n,R}(-\theta_n)\le2^{R+1}(1+C_R)$. For the slices $f_n=U_n(-\theta_n)$, the scaled
estimate on the balls of (a) (with $R'\ge\max(R+1,2/h)$, so that $B_{4\rho}(y_i)\subset B_{4R'}\cap\{r_n>1/R'\}$) gives a translation
modulus on $K$ uniform in large $n$, hence total boundedness of the restrictions to $K$; on the tube,
$\|f_n-f_m\|^2_{L^2}\le8\pi Rh^2$. So $(f_n)$ is totally bounded in $L^2(B_R)$, and the remaining steps of the proof of Theorem 17(c)
apply verbatim. (c) The region in (EC) is contained in that of (VC), with equality once $d_n>R+h$. (d) Since
$|\omega|\le\sqrt2|\nabla u|$, $|\operatorname{curl}V_n|\le\sqrt2\sigma_n$, and the (VC) quantity is at most $\sqrt2(4\pi/3)AR^3\sigma_n$; so bounded
$\sigma_n$ along a subsequence gives (VC), hence (EC), along it. By (a) and Theorem 17(c), (EC) along a subsequence of a normalization
with (OSC$_0$) produces a joint subsequence with $\mathcal R=0$ and a limit nonconstant at some time, contradicting (C*). If (FLAT)
fails, normalizations with (OSC$_0$) exist (paragraph after Theorem 6'). $\square$

Remarks. (i) Critical norms. $\|\eta(t)\|_{L^{3/2}}/M_n$ and $\|\omega^\theta(t)\|_{L^3}/M_n$ are the corresponding norms of the rescaled
fields, independent of $\ell_n$. By Hoelder, a historical bound $\sup_{s\le t}\|\omega^\theta(s)\|_3\le CM(t)$ would give (VC) for every
admissible normalization and so, by Proposition 20(d), exclude (C*-D) (not (FLAT)); $\sup_{s\le t}\|\eta(s)\|_{3/2}\le CM(t)$ would do
the same for normalizations with $d_n$ bounded. Neither bound is known. The elementary estimates (the forcing bound
$\|\partial_z(q^2)\|_{3/2}\le C\|\nabla q\|_2^2$ with $|\nabla q|\le C|\nabla^2u|$, and the enstrophy inequality) give at best
$\|\eta_0\|_{3/2}+C\|\omega_0\|_2^2+CE_0D$ and $C[D(\|\omega_0\|_2^2+E_0D)]^{1/3}$, larger than $M$ by factors at least $c(E_0M)^{2/3}$ and
$c(E_0M)^{1/9}$ (Lemma 2); these are sizes of upper bounds, not of the norms (the first also uses the $L^{3/2}$ contraction of
the homogeneous $\eta$ propagator, which follows by interpolation from its $L^1$ contraction in the Remark after Lemma 9' and
the maximum principle; this auxiliary upper estimate is used in no proof). Also $\eta_0\in L^{3/2}$ does not follow from
$u_0\in\bigcap_kH^k$ (the swirl-free field with stream function $\phi(r)(1+z^2)^{-\alpha/2}$, $\phi\in C_c^\infty((1,2))$ nonzero,
$\frac12<\alpha\le\frac23$, has $|\eta|\ge c|z|^{-\alpha}$ for large $|z|$ on a radial interval).
(ii) Critical norms cannot address (FLAT): the swirl-free fields $b_N$ with stream function $\frac12r^2f_N(|x|)$,
$f_N(s)=h_N(-\log s)$, $h_N$ a mollified $N^{-1}\min\{N,\max\{0,\cdot\}\}$, satisfy $b_N=f_Ne_z+O(1/N)$, $\|\nabla b_N\|_\infty\asymp e^N/N$,
$\|b_N\|_2^2\asymp N^{-2}$, $\|\eta[b_N]\|_{3/2}\le CN^{-1/3}$, $\|\omega[b_N]\|_3\le CN^{-2/3}$, and every resolved oscillation at most $C/N$
(on balls with $|x|\ge2\rho$ the oscillation of $\log|x|$ is bounded; otherwise compare with $h_N(-\log\rho)$). Rescaled to fixed energy
with amplitude $e^{6N}$ they have $D/M^2\to0$, both critical ratios $\to0$ and all resolved oscillations $o(M)$. These are
single-time fields, not trajectories.
(iii) Production and inheritance. Under (OSC$_0$), Jensen and energy give $\ell_n^3\le3E_0/(\pi c^2M_n^2)$, so $\ell_n^2/M_n\to0$ and the
contribution of the datum to $\eta_n$ tends to $0$ uniformly (maximum principle; the homogeneous operator is transport plus the
Laplacian of $\mathbb R^5$ in the variables $(r,z)$); for $\operatorname{curl}V_n=r_n\eta_ne_\theta$ with $d_n\to\infty$ one also uses
$(1+d_n)M_n^2\ell_n^3\le C_cE_0$, obtained by placing order $d_n$ disjoint rotated copies of the certified ball around the axis.
Without (OSC$_0$) the upper bound for the datum contribution need not tend to $0$. So on certified normalizations the meridional vorticity of a window is produced by
the swirl source (quantitatively, the Remark after Lemma 9'), but over the whole history of $s_n/T_n\to\infty$ Euler times; in the Duhamel formula, pairing with a test
function needs the derivative of the transported test function, which involves $\nabla V_n$, bounded only by $\sigma_n$, and
$\sigma_n\to\infty$ on certified normalizations in (C*). The energy bound for $\int\!\!\int q_n^2$ over the whole history is at least of
order $(E_0M_n)^{1/3}$ at certified scales, and the instantaneous envelopes of Lemma 19(b) do not bound the total variation of the
source (an envelope example, not a solution). In (C*-D) the exterior vorticity that defeats (EC) on every certified normalization
is therefore, by Lemma 21 below, present at earlier times in larger balls as long as these stay off the axis, and otherwise
comes out of the tubes around the axis; no estimate of it is available. Bounding it on one certified normalization is a
sufficient route, not a proved equivalent of the missing implication.

### 9C. Lagrangian localization of the meridional vorticity; (EC) implies (L2M)

Notation as in Section 9B, and $w_n(y,\tau)=(\ell_n/M_n)\,\omega^\theta(x_n+\ell_ny,s_n+T_n\tau)$, so that $\operatorname{curl}V_n=w_ne_\theta$,
$w_n=r_n\eta_n$, and $|w_n|\le\sqrt2\,\sigma_n$ for $\tau\le0$ (since $|\omega|\le\sqrt2|\nabla u|$). Note $\nu_n\sigma_n=D_n/M_n^2$. Fix
$\psi\in C^\infty(\mathbb R)$ nonincreasing with $\psi=1$ on $(-\infty,0]$, $\psi=0$ on $[1,\infty)$, and put $C_\psi=\|\psi'\|_\infty+\|\psi''\|_\infty$.

**Lemma 21 (Lagrangian localization).** Let the normalization be admissible, $-s_n/T_n\le\tau_1<\tau_2\le0$,
$\Delta\tau=\tau_2-\tau_1$, $\rho>0$, $w\in(0,1]$, $y_0\in\mathbb R^3$, $\rho_1=\rho+\Delta\tau+w$, and assume
$d':=\inf\{r_n(y):y\in B_{\rho_1}(y_0)\}>0$. Then
$$\int_{B_\rho(y_0)}|w_n(\tau_2)|\le e^{\Delta\tau/d'}\Big[\int_{B_{\rho_1}(y_0)}|w_n(\tau_1)|+\Delta\tau\,E_n\Big],\qquad
E_n=|B_{\rho_1}|\Big(3C_\psi\big(w^{-2}+(w\rho)^{-1}\big)\frac{D_n}{M_n^2}+\frac{2\delta_n}{d'^2}\Big),$$
and
$$\int_{B_\rho(y_0)}|\eta_n(\tau_2)|\le\int_{B_{\rho_1}(y_0)}|\eta_n(\tau_1)|+\Delta\tau\,E''_n,\qquad
E''_n=|B_{\rho_1}|\Big(3C_\psi\big(w^{-2}+(w\rho)^{-1}+(wd')^{-1}\big)\frac{D_n}{M_n^2d'}+\frac{2\delta_n}{d'^3}\Big).$$
In regime (II) $E_n,E''_n\to0$ for fixed $\rho,w,\Delta\tau,d'$. So, away from the axis, the meridional vorticity mass in a
ball at a later time is bounded by the mass at an earlier time in the ball enlarged by the elapsed Euler time plus $w$,
up to a bounded factor and an error tending to $0$, for fixed $\rho,w,\Delta\tau$ and a lower bound on $d'$.

Proof. Away from the axis the physical equation is
$\partial_t\omega^\theta+u^{mer}\cdot\nabla\omega^\theta=(\Delta-r^{-2})\omega^\theta+(u^r/r)\omega^\theta+\partial_z((u^\theta)^2)/r$: it follows from
the $\eta$-equation of Lemma 19(a) with $\omega^\theta=r\eta$, since $u^{mer}\cdot\nabla r=u^r$, $\Delta(1/r)=r^{-3}$ and $\nabla(1/r)=-r^{-2}e_r$
give $r(\Delta+\frac2r\partial_r)(\omega^\theta/r)=(\Delta-r^{-2})\omega^\theta$, and $r\partial_z(q^2)=\partial_z((u^\theta)^2)/r$. Every term scales by
$\ell_n^2/M_n^2$, so on $\{r_n>0\}$
$$\partial_\tau w_n+V_n\cdot\nabla w_n=\nu_n(\Delta-r_n^{-2})w_n+\frac{V_n^r}{r_n}w_n+F_n,\qquad F_n=r_n\partial_{y_3}(q_n^2),\quad|F_n|\le2\delta_nr_n^{-2}$$
(Lemma 19(c)), with $|V_n|\le1$ and $\operatorname{div}V_n=0$. For $\tau\in[\tau_1,\tau_2]$ let $\phi(y,\tau)=\psi((|y-y_0|-\rho-(\tau_2-\tau))/w)$. It is
smooth (constant near $y_0$), $0\le\phi\le1$, $\phi(\cdot,\tau_2)=1$ on $B_\rho(y_0)$, $\operatorname{supp}\phi(\cdot,\tau)\subset\bar B_{\rho_1}(y_0)$, and
$\partial_\tau\phi+V_n\cdot\nabla\phi=w^{-1}\psi'(\cdot)(1+V_n\cdot e)\le0$ with $e=(y-y_0)/|y-y_0|$; on the support of $\psi'(\cdot)$, $|y-y_0|\ge\rho$, so
$|\Delta\phi|\le C_\psi(w^{-2}+2(w\rho)^{-1})$ and $|\nabla\phi|\le C_\psi/w$. Let $j_\epsilon(s)=(s^2+\epsilon^2)^{1/2}$ and $X_\epsilon=\int j_\epsilon(w_n)\phi$; $w_n$ is
smooth on $\bar B_{\rho_1}(y_0)\subset\{r_n\ge d'\}$ for $t<T_*$. Transport gives $\int j_\epsilon(w_n)V_n\cdot\nabla\phi$ ($\operatorname{div}V_n=0$); diffusion gives
at most $\nu_n\int j_\epsilon(w_n)\Delta\phi$ (convexity of $j_\epsilon$) and the term $-\nu_n\int j'_\epsilon(w_n)w_n\phi r_n^{-2}\le0$; stretching gives at most
$X_\epsilon/d'$; the source at most $2\delta_n|B_{\rho_1}|/d'^2$. With $j_\epsilon(w_n)\le\sqrt2\sigma_n+\epsilon$, $\nu_n\sigma_n=D_n/M_n^2$ and $2\sqrt2<3$,
$X'_\epsilon\le X_\epsilon/d'+E_n+\epsilon\nu_nC_\psi(w^{-2}+2(w\rho)^{-1})|B_{\rho_1}|$; Gronwall and $\epsilon\to0$ give the first estimate. For the second
use the same $\phi$ with the $\eta$-equation, which has no zero-order term. Off the axis $\operatorname{div}(r_n^{-1}e_{r_n})=0$, so
$\int\phi\,2r_n^{-1}\partial_{r_n}j_\epsilon(\eta_n)=-\int j_\epsilon(\eta_n)\,2r_n^{-1}\partial_{r_n}\phi$, at most $2(|\eta_n|+\epsilon)C_\psi/(wd')$ integrated over
$B_{\rho_1}(y_0)$. On $\operatorname{supp}\phi$, $|\eta_n|\le\sqrt2\sigma_n/d'$ and $|\partial_{y_3}(q_n^2)|\le2\delta_n/d'^3$; integrate in $\tau$ and let $\epsilon\to0$. $\square$

**Proposition 22 ((EC) implies (L2M)).** Assume regime (II).
(a) Every admissible isotropic normalization with (EC) of Proposition 20 satisfies (L2M) of Theorem 5. Moreover (EC) is
equivalent to its single-time form: $\limsup_n\sup_{-A\le\tau\le0}\int_{B_R\cap\{r_n>h\}}|w_n(y,\tau)|\,dy<\infty$ for all $R,A,h>0$.
(b) (OSC$_0$) of Theorem 17 implies (L2-OSC) of Theorem 5 on $B_2$: $\int_{B_2}|U_n(0)-(U_n(0))_{B_2}|^2\ge|B_1|c^2$ in the single-$\epsilon$
form, and $\ge|B_1|c^2/4$ in the series form, for all $n$.
(c) Hence an admissible isotropic normalization with (EC) and (OSC$_0$), in particular one with (VC) and (OSC$_0$), is in
case (B) of Theorem 5(c), and GOAL holds for it at its own terminal time $s_n$ in the sense of Theorem 5(a): along a
subsequence $U_n\to U$ in $C([-A,0];L^2(B_R))$ for all $A,R$, $|U|\le1$, $U(\cdot,0)$ not a.e. constant, $U$ a weak Euler solution with
canonical pressure, with the swirl and axis dichotomy. No terminal-slice rule is needed.
(d) If alternative (C) of Theorem 5 holds, every admissible isotropic normalization with (OSC$_0$) has $\sigma_n\to\infty$ and fails
(EC) (equivalently its single-time form) along each of its subsequences. If (FLAT) fails, such normalizations exist.

Proof. (a) Fix $R\ge1$, $A>0$, $h\in(0,1]$, and consider indices with $(A+1)T_n\le s_n$. Put $\rho=h/16$, $K_n=\bar B_R\cap\{r_n\ge h\}$,
and fix a finite set $Y\subset\bar B_R$, $m=\#Y$, with $\bar B_R\subset\bigcup_{z\in Y}B_{\rho/2}(z)$; for each $z$ with $B_{\rho/2}(z)\cap K_n\neq\emptyset$ pick
$y_i$ in this set. Then $K_n\subset\bigcup_iB_\rho(y_i)$ with at most $m$ balls and $r_n(y_i)\ge h$. Apply the first estimate of Lemma 21
with target ball $B_{4\rho}(y_i)=B_{h/4}(y_i)$, $w=h/16$ and $\Delta\tau\le\theta:=h/16$: then $\rho_1\le3h/8$, $B_{3h/8}(y_i)\subset B_{R+1}\cap\{r_n\ge5h/8\}$,
$d'\ge5h/8$, $\Delta\tau/d'\le1/10$. Let $\mathcal K_n=\int_{-A-1}^0\int_{B_{R+1}\cap\{r_n>h/2\}}|w_n|$; it is the (EC) quantity with radius $R+1$, window $A+1$ and
$h/2$ (the Jacobian of the proof of Theorem 6'), so $\limsup_n\mathcal K_n<\infty$. For $\tau\in[-A,0]$ the continuous function
$\tau'\mapsto\int_{B_{3h/8}(y_i)}|w_n(\tau')|$ has integral at most $\mathcal K_n$ over $[\tau-\theta,\tau]$, so it is at most $\mathcal K_n/\theta$ at some
$\tau_1\in[\tau-\theta,\tau]$, and Lemma 21 gives $\int_{B_{4\rho}(y_i)}|w_n(\tau)|\le e^{1/10}(16\mathcal K_n/h+E_n)=:\mathcal K'_n$ for all $\tau\in[-A,0]$, with
$\limsup_n\mathcal K'_n<\infty$. Summing over $i$ proves the single-time form (the converse is integration in $\tau$). The scaled form
of the Lemma of Section 8 (proof of Proposition 20) on each $B_\rho(y_i)$ at time $\tau$ gives
$\int_{K_n}|V_n(y+k,\tau)-V_n(y,\tau)|^2dy\le mC_1(\rho^2+\mathcal K'_n)|k|(1+\log(\rho/|k|))$ for $|k|\le\rho/2$. The set $B_R\setminus K_n$ lies in a cylinder of
radius $h$ and height $2R$ about $\mathcal A_n$, of volume at most $2\pi Rh^2$, where $|U_n(y+k)-U_n(y)|\le2$ since $|U_n|\le1$. On $K_n$,
$|U_n-V_n|\le S(t_n)/M_n$ gives $|U_n(y+k)-U_n(y)|^2\le2|V_n(y+k)-V_n(y)|^2+8S(t_n)^2/M_n^2$. Hence
$$\sup_{-A\le\tau\le0}\sup_{|k|\le\delta}\int_{B_R}|U_n(y+k,\tau)-U_n(y,\tau)|^2dy\le2mC_1(\rho^2+\mathcal K'_n)\delta(1+\log(\rho/\delta))+8\pi Rh^2+8|B_R|\frac{S(t_n)^2}{M_n^2}$$
for $\delta\le\rho/2$. Take $\limsup_n$ (Theorem 3), then $\delta\to0$, then $h\to0$.
(b) In rescaled variables $O_\epsilon(x_n,s_n,\ell_n)/M_n=(\fint_{B_1}|f^\epsilon-(f^\epsilon)_{B_1}|^2)^{1/2}$ with $f=U_n(\cdot,0)$, and the mollifier is nonnegative
with integral $1$ and support in $B_\epsilon$. For $b\in\mathbb R^3$, Jensen and Fubini give
$\int_{B_1}|f^\epsilon-(f^\epsilon)_{B_1}|^2\le\int_{B_1}|(f-b)^\epsilon|^2\le\int_{B_1}(|f-b|^2)^\epsilon\le\int_{B_2}|f-b|^2$; take $b=(f)_{B_2}$. So $O_\epsilon/M_n\le\Theta_n$,
$\Theta_n^2=|B_1|^{-1}\int_{B_2}|f-(f)_{B_2}|^2$, for every $\epsilon\in(0,1]$, and the series form is at most $2\Theta_n$.
(c) By (a), (b) and Theorem 5(a); (VC) implies (EC) by Proposition 20(c).
(d) A subsequence of a normalization with (OSC$_0$) is again one; (EC) along it would give case (B), which is excluded by (C).
If $\sigma_n\le C$ along a subsequence, (EC) holds along it (Proposition 20(d)); so $\sigma_n\to\infty$. Existence: paragraph after
Theorem 6' (if the horizons $t_n$ are not record times, replace $t_n$ by the first time at which $M$ reaches $2M(t_n)$; the
certificate survives with $c/2$, and admissibility and depth are kept). $\square$

Remarks. (i) The family $Z_n$ after Theorem 6' satisfies the time-integrated curl bound and fails (L2M); it is not a
Navier-Stokes trajectory, and Lemma 21 is what excludes this behaviour for trajectories: curl mass of order $n$ appearing
within Euler time $O(1/n)$ is incompatible with transport at unit speed up to $o(1)$. So for trajectories the time-integrated
certificates of Theorem 6' and Proposition 20 control the terminal slice, and the terminal-slice rules of Theorem 17(d) and
Proposition 20(b) are not needed for GOAL (they remain correct).
(ii) Lemma 21 propagates a bound on mass that is already present; it gives no bound by itself. Combined with the
enstrophy inequality it gives, at a fixed time and for large $n$, $\ell_n^{-2}M_n^{-1}\int_{B_\lambda}|\omega^\theta|\le C(\lambda/\ell_n)^{3/2}(E_0D_n\ell_n^{-1}/M_n^2)^{1/2}$,
an upper bound that tends to infinity at certified scales; enlarging the ball makes it larger. The first missing
implication is unchanged: exclusion of (C). Where (FLAT) fails, a sufficient form is a bound, uniform in $n$, on
$\ell_n^{-2}M_n^{-1}\int_{B_{R\ell_n}(x_n)\cap\{r>h\ell_n\}}|\omega^\theta(t)|\,dx$ for $t\in[s_n-AT_n,s_n]$ (or on its integral in rescaled Euler time, the physical time integral divided by $T_n$),
for all $R,A,h$, at one normalization with (OSC$_0$).
(iii) Near the axis no localization is used: the tubes $\{r_n<h\}$ enter only through their volume. The second estimate of
Lemma 21 gives, with $r_0=r_n(y_0)>\rho_1$, $\int_{B_\rho(y_0)}|w_n(\tau_2)|\le\frac{r_0+\rho}{r_0-\rho_1}\int_{B_{\rho_1}(y_0)}|w_n(\tau_1)|+(r_0+\rho)\Delta\tau E''_n$, whose
geometric factor tends to $1$ when $d_n\to\infty$ with $y_0$, $\rho$, $\rho_1$ fixed (not for centres that move with the axis).
(iv) If $d_n\to\infty$, (EC) is unchanged by bounded changes of the window ($s'_n=s_n-\theta_nT_n$, $x'_n=x_n+\ell_ny_n$, $\ell'_n=\lambda_n\ell_n$,
$0\le\theta_n\le B$, $|y_n|\le B$, $c\le\lambda_n\le C$, same amplitude): (EC) is then the full-ball bound, bounded shifts and comparable
scales change $R,A$ and the prefactor by bounded factors, and the times in $[-\theta_n,0]$ are reached from $[-\theta_n-1,-\theta_n]$ by
Lemma 21 as in (a). So in the axis-escaping case, if (EC) fails along a given subsequence, no bounded change of the window
along that same subsequence makes it hold (in (C), part (d) gives failure along every subsequence).

### 9D. Window budgets, scale selection and the axis

This section tests three ways of proving (EC) at a certified normalization. Notation
of Proposition 22; for $R,A,h>0$ let $K_n(R,A,h)=\int_{-A}^0\int_{B_R\cap\{r_n>h\}}|w_n|\,dy\,d\tau$ (the time-integrated (EC) quantity) and let
$Q_n$ be the physical region $\{(x_n+\ell_ny,s_n+T_n\tau):|y|<R,\ r_n(y)>h,\ -A\le\tau\le0\}$.

**Lemma 23 (budget weights).** $K_n=\ell_n^{-3}\int_{Q_n}|\omega^\theta|\,dx\,dt$ and $\int_{Q_n}|\omega^\theta|r^{-2}\,dx\,dt=\ell_n\int\!\int|w_n|r_n^{-2}\,dy\,d\tau\ge\ell_n(d_n+R)^{-2}K_n$.
So if the regions $Q_n$, $n\in\mathcal N$, lie in $\{\phi=1\}\times[0,T_*)$ for a cutoff $\phi$ of Lemma 9' and overlap at most $N$
times, then $\sum_{n\in\mathcal N}\ell_n(d_n+R)^{-2}K_n\le NC_\phi$, with $C_\phi$ the right side of Lemma 9' at $t=T_*$, and
$\inf_{n\in\mathcal N}K_n\le NC_\phi/W$, $W=\sum_{n\in\mathcal N}\ell_n(d_n+R)^{-2}$.

Proof. $dx\,dt=\ell_n^3T_n\,dy\,d\tau$, $\omega^\theta=(M_n/\ell_n)w_n$, $r=\ell_nr_n$, $T_n=\ell_n/M_n$, $r_n\le d_n+R$ on $B_R$; then Lemma 9' and monotone
convergence as $t\uparrow T_*$. $\square$

If certified windows of divergent total weight $W$ existed, the fixed budget would give $\inf K_n=0$ for that triple
$(R,A,h)$ (one triple only, not yet (EC)). Energy forbids divergent weight for families whose full persistence cylinders
overlap boundedly.

**Proposition 24 (energy forbids a divergent weighted supply).** Assume regime (II) and fix $\epsilon\in(0,1]$, $c>0$. There are
$a,c_2>0$ depending on $c,\epsilon$ such that every admissible isotropic normalization with $O_\epsilon(x_n,s_n,\ell_n)\ge cM_n$ satisfies,
whenever $aT_n\le s_n$ and $\nu_n\le1$,
$$\int_{s_n-aT_n}^{s_n}\int_{B_{2\ell_n}(x_n)}|\nabla u|^2\,dx\,dt\ge c_2M_n\ell_n^2 .$$
Hence, for fixed $c,\epsilon$, any family of such normalizations of one solution, with indices in $I=\{n:aT_n\le s_n,\ \nu_n\le1\}$,
whose persistence cylinders $C_n=B_{2\ell_n}(x_n)\times[s_n-aT_n,s_n]$ overlap at most $N$ times has $\sum M_n\ell_n^2\le NE_0/(2c_2)$,
so $\sum\ell_n\le\sum M_n\ell_n^2<\infty$ (as $M_n\ell_n=1/\nu_n\ge1$), and $W<\infty$ in Lemma 23 (bounded overlap of the regions $Q_n$
alone does not give bounded overlap of the $C_n$). A finite $W$ still gives $\inf K_n\le NC_\phi/W$; the budget alone gives no
uniform bound on $K_n$ along windows approaching $T_*$ (weights $2^{-n}$ with $K_n=n$ are consistent with it).

Proof. Let $\mathrm{osc}(g)=(\fint_{B_1}|g-(g)_{B_1}|^2)^{1/2}$, a seminorm bounded by $\sup_{B_1}|g|$; then
$O_\epsilon(x_n,s_n+T_n\tau,\ell_n)/M_n=\mathrm{osc}(U_n(\tau)*\rho_\epsilon)$. By the formula for $\partial_\tau(U_n*\rho_\epsilon)$ in the proof of Theorem 4(a)
(canonical pressure, $\|k_\epsilon\|_1\le C/\epsilon$), $|U_n|\le1$ and $\nu_n\le1$ give $|\partial_\tau(U_n*\rho_\epsilon)|\le C_\epsilon=C(\epsilon^{-1}+\epsilon^{-2})$, so the
oscillation is at least $c/2$ for $-a\le\tau\le0$, $a=c/(2C_\epsilon)$. At each such time, with $b$ the mean of $u$ over $B_{2\ell_n}(x_n)$,
the Jensen and Fubini chain of Proposition 22(b) and the Poincare inequality give
$|B_{\ell_n}|c^2M_n^2/4\le\int_{B_{2\ell_n}(x_n)}|u-b|^2\le C_P\ell_n^2\int_{B_{2\ell_n}(x_n)}|\nabla u|^2$. Integrate over the time interval of length
$a\ell_n/M_n$: $c_2=a|B_1|c^2/(4C_P)$. The sum bound is the energy inequality $2\int_0^{T_*}\|\nabla u\|_2^2\le E_0$. $\square$

Remarks. (i) A budget argument would have to compare two quantities that both tend to $0$, the budget remaining after a
time $t$ and the weight of the certified windows after $t$; nothing gives a rate for their ratio. Exponent bookkeeping
(not a solution) is consistent with all the listed bounds while $K_n\to\infty$: $M=(T_*-t)^{-4/7}$, $D=M^{15/8}$, one certified
window per dyadic level of $M$ with $\ell=M^{-3/4}$ and $K=M^{1/8}$ gives $D/M^2\to0$, $\sigma=M^{1/8}$, $M'\le24MD$, $M^5\le D^3$, window
energy $M^{-1/4}$, weighted expenditure $\ell K=M^{-5/8}$ and window dissipation $M\ell^2K^2=M^{-1/4}$, all summable over the levels.
(ii) Since $|w_n|\le\sqrt2|\nabla U_n|$, Cauchy-Schwarz gives $K_n\le(2A|B_R|Z_n(R,A))^{1/2}$ with the window enstrophy
$Z_n(R,A)=(M_n\ell_n^2)^{-1}\int_{s_n-AT_n}^{s_n}\int_{B_{R\ell_n}(x_n)}|\nabla u|^2$, and Proposition 24 gives $Z_n(R,A)\ge c_2$ for $R\ge2$, $A\ge a$. So (EC) would
follow if one certified normalization had $\limsup_nZ_n(R,A)<\infty$ for every fixed $R,A$ (the dissipation of every fixed
rescaled window of the order of its minimum $M_n\ell_n^2$); in (C) this family of bounds fails at every certified
normalization, which does not show divergence on the minimal window $B_2\times[-a,0]$.
(iii) Lemma 21 cannot be iterated through unboundedly many Euler times without re-estimating its errors, and for bounded
$d_n$ the backward cone from a fixed exterior ball reaches the axis after boundedly many Euler times.

**Proposition 25 (single-time obstruction to scale selection).** There are smooth, compactly supported, divergence-free,
axisymmetric, swirl-free fields $v_j$ with $\|v_j\|_2\to0$, $M_j=\|v_j\|_\infty\to\infty$, $D_j=\|\nabla v_j\|_\infty$, $D_j/M_j^2\to0$, and numbers
$\kappa>0$, $A_j\to\infty$, such that: (a) some pair $(x_j,\ell_j)$ has $O_\epsilon(x_j,\ell_j)[v_j]\ge c_*M_j$ for all $\epsilon\in(0,1]$ and large $j$
($O_\epsilon$ computed for the field $v_j$); (b) for every $c>0$, $\epsilon\in(0,1]$ there are $R,h,c'>0$ such that for large $j$ every pair with
$O_\epsilon(x,\ell)[v_j]\ge cM_j$ has $\ell D_j/M_j\ge c'A_j^\kappa$ and $M_j^{-1}\ell^{-2}\int_{B_{R\ell}(x)\cap\{r>h\ell\}}|\omega^\theta[v_j]|\ge c'A_j^\kappa$; (c) the rescalings
$M_j^{-1}v_j(x_j+\ell_j\cdot)$ along any such pairs have locally uniformly convergent subsequences; (d) given $\alpha>1$, $\gamma>2$, one
can also have $|v_j|\le Cr^{-\alpha}$ and $|\omega^\theta[v_j]|\le Cr^{-\gamma}$ everywhere.

Proof. For axisymmetric $\Psi(r,z)$ supported off the axis, $B[\Psi]=-r^{-1}\partial_z\Psi\,e_r+r^{-1}\partial_r\Psi\,e_z$ is smooth, swirl-free and
divergence free. Let $\chi_0\in C_c^\infty(\{\frac12<r<6,|z|<3\})$ equal $1$ on $\{1\le r\le5,|z|\le2\}$ and $B=B[\frac12r^2z\chi_0]$; there
$B=(-x_1/2,-x_2/2,x_3)$, affine and curl free. Let $\chi_1\in C_c^\infty(\{2<r<4,|z|<1\})$ equal $1$ on $Q=\{\frac52\le r\le\frac72,|z|\le\frac12\}$ and
$B_j=B[\frac12r^2z\chi_0+(a_j/k_j)\chi_1\sin(k_jr)]$ with $a_j\to0$, $a_jk_j\to\infty$. Then $\|B_j-B\|_\infty\le C_1a_j$, $\|\nabla(B_j-B)\|_\infty\le C_1a_jk_j$
(with a matching lower bound), and on $Q$, $\omega^\theta[B_j]=a_jk_jr^{-1}\sin(k_jr)+a_jr^{-2}\cos(k_jr)$, so $\int_Q|\omega^\theta[B_j]|\ge a_jk_j$ for large $j$
(since $\int_{5/2}^{7/2}|\sin k_jr|\,dr\to2/\pi$). Take $\frac23<\beta<1$, $0<\kappa<1-\beta$, $L_j=A_j^{-\beta}$, $a_j=A_j^{-\kappa}$, $k_j=A_j^{2\kappa}$,
$v_j=A_jB_j(\cdot/L_j)$. Then $M_j=A_j\|B_j\|_\infty$, $D_j\asymp A_j^{1+\beta+\kappa}$, $\|v_j\|_2^2\asymp A_j^{2-3\beta}\to0$, $D_j/M_j^2\asymp A_j^{\beta+\kappa-1}\to0$.
(a) $x_j=L_j(3,0,0)$, $\ell_j=L_j$: the radial mollifier fixes the affine field on $B_1((3,0,0))$, whose oscillation there is $\sqrt{3/10}$;
the perturbation changes the oscillation by at most $C_1a_j$. (b) With $x=L_jX$, $\ell=L_j\lambda$, $O_\epsilon(x,\ell)[v_j]=A_jO_\epsilon(X,\lambda)[B_j]$, and
certification gives $O_\epsilon(X,\lambda)[B_j]\ge c\|B\|_\infty/2$. The mollified $B$ is $\|\nabla B\|_\infty$-Lipschitz, so $\lambda\ge\lambda_->0$; the bound
$O_\epsilon(X,\lambda)[B_j]\le(\|B_j\|_2^2/|B_\lambda|)^{1/2}$ gives $\lambda\le\lambda_+$; the support gives $|X|\le X_+$. With $R=(X_++4)/\lambda_-$ and $h=2/\lambda_+$,
$Q\subset B_{R\lambda}(X)\cap\{r>h\lambda\}$, and changing variables, $M_j^{-1}\ell^{-2}\int_{B_{R\ell}(x)\cap\{r>h\ell\}}|\omega^\theta[v_j]|\ge a_jk_j/(2\|B\|_\infty\lambda_+^2)$, while
$\ell D_j/M_j\ge\lambda_-\|\nabla B_j\|_\infty/\|B_j\|_\infty\ge c'a_jk_j$; and $a_jk_j=A_j^\kappa$. (c) $(X_j,\lambda_j)$ ranges in a compact set and $B_j\to B$
uniformly. (d) The support lies in $\{L_j/2<r<6L_j\}$, where $|v_j|\le CA_j$, $|\omega^\theta[v_j]|\le CA_j^{1+\beta+\kappa}$; choose
$\max\{\frac23,\frac1\alpha,\frac1{\gamma-1}\}<\beta<1$ and $0<\kappa<\min\{1-\beta,(\gamma-1)\beta-1\}$. $\square$

So, for single-time fields, failure of the exterior mass bound at every certified scale is compatible with compactness
of the certified rescalings: no choice of scale based on the bound $\int_{B_R}|w|\le\sqrt2|B_R|\sigma$ can find a certified scale with bounded
exterior mass, and the sufficient form of the first missing implication (Proposition 22, Remark (ii)) may be strictly
stronger than the exclusion of (C); a strict separation for trajectories is not proved. Spatial power bounds of the type
in (d), with $\alpha>1$, $\gamma>2$, do not help either; the restriction $\gamma>2$ is essential, since a bound $|\omega^\theta|\le Cr^{-2}$
on the windows gives $|w_n|\le C\nu_nr_n^{-2}$, hence $K_n\le CA|B_R|h^{-2}\nu_n\to0$. The fields are not Navier-Stokes trajectories
and do not model (C).

**Corollary 26 (certified windows approach the axis).** Under (OSC$_0$) with constant $c$, in either form,
$r(x_n)\le C_cE_0/(M_n^2\ell_n^2)\le4C_cc^{-2}E_0(D_n/M_n^2)^2\to0$.

Proof. $r(x_n)=d_n\ell_n$, $(1+d_n)M_n^2\ell_n^3\le C_cE_0$ (Section 9B, Remark (iii)), and $\ell_n\ge cM_n/(2D_n)$ since $O_\epsilon(x_n,s_n,\ell_n)\le D_n\ell_n$ and $\tilde O(x_n,s_n,\ell_n)\le2D_n\ell_n$. $\square$

So off-axis regularity in its qualitative form (the Caffarelli-Kohn-Nirenberg theorem with axisymmetry puts all singular
points at $T_*$ on the axis) gives nothing uniform on certified windows. The corollary proves approach to the physical
axis, not bounded rescaled axis distance $d_n$.

Remark. In (C) the alternative (UP) of Theorem 4 holds (otherwise Theorem 4(c) gives a normalization with $\ell_n=M_n/D_n$
satisfying (L2M) and (L2-OSC), i.e. case (B)). Since $u^r$ and $u^\theta$ vanish on the axis, $|u^r(x,t)|+|u^\theta(x,t)|\le2\omega_t(r(x))$. So
in (C), within any fixed number of Lipschitz lengths $M/D$ of the axis the velocity is $u^ze_z+o(M)$, with $u^z$ within $o(M)$ of
its value on the axis at the same height, and all certified oscillation lives at scales with $\ell D/M\to\infty$
(Proposition 22(d)).

**Lemma 26A (recent export from the axis).** Let $U$ be smooth, axisymmetric about a fixed vertical axis and divergence
free on $\mathbb R^3\times[\tau-A,\tau]$, with $|U|\le1$ and $\|\nabla U\|_\infty\le\sigma$, and let $\mathcal V_{a,A}(\tau)$ be the set of $y$ whose
particle path through $(y,\tau)$ meets $\{r\le a\}$ during $[\tau-A,\tau]$. Then $|\mathcal V_{a,A}(\tau)\cap\{|y_3-z_0|\le R\}|\le2\pi e^2(R+A)a^2(2+A\sigma)$
for every $z_0$. Proof: $|U^r|\le\sigma r$, since the horizontal velocity vanishes on the axis, so along a path radii at times
at most $1/\sigma$ apart differ by a factor at most $e$; split $[\tau-A,\tau]$ into $k=\max\{1,\lceil A\sigma\rceil\}$ equal intervals (of length at most $1/\sigma$, read as $\infty$ if $\sigma=0$;
at most $A\sigma+2$ endpoints); a path visiting $\{r\le a\}$ lies in $C=\{r\le ea,\ |y_3-z_0|\le R+A\}$ at a neighbouring endpoint (as $|U^z|\le1$), and
the images of $C$ under the volume-preserving flow have volume $|C|=2\pi e^2a^2(R+A)$. $\square$

Here $G>0$: for $G=0$ the solution has no swirl and is globally regular (Ukhovskii-Yudovich, Ladyzhenskaya), so there is no
singular time. Applied to $U_n$ with $|w_n|\le\sqrt2\sigma_n$, $a_n=\delta_n^{-1/8}(g_n/\sigma_n)^{1/2}$ (physical radius $\delta_n^{-1/8}(G/D_n)^{1/2}$, which is $\delta_n^{3/8}M_n/D_n$)
and $A_n=\min\{\delta_n^{-1/8},\frac12(s_n/T_n)^{1/2}\}$, one gets $\sigma_na_n^2=\delta_n^{-1/4}g_n$ and, for $\sigma_n\ge c>0$ and fixed $R,B$,
$\sup_{-B\le\tau\le0}\int_{\mathcal V_{a_n,A_n}(\tau)\cap\{|y_3|\le R\}}|w_n(\tau)|\,dy\le C_{R,c}\delta_n^{1/2}\to0$. So the quantity $K_n(R,B,h)$ of Section 9D, and
each signed meridional mass on exterior rectangles $[\max\{h,d_n-R\},d_n+R]\times[-R,R]$ (whose difference is at most $8R$, as in
Corollary 6A), change by $o(1)$ when the vorticity on particles that visited the tube $\{r_n\le a_n\}$ during the preceding $A_n$
Euler times is removed. In (C), for a normalization with (L2-OSC), Proposition 22(a) forces failure of (EC), so some fixed exterior window
carries divergent cancelling masses along a subsequence; these masses are therefore carried, up to $o(1)$, by particles that
stayed outside that tube for $A_n\to\infty$ Euler times. Diffusion moves vorticity between particle labels, so this says nothing
about where the vorticity was generated, and it gives no bound on the mass carried by those particles.

### 10. Single-time functional test of alternative (C)

The following is a function of one variable, not a Navier-Stokes solution and not a counterexample. Let
$g_N(z)=N^{-1/2}\sum_{k=1}^N\sin(4^kz)$, $F_N=\tanh g_N$, $\Lambda_N=N^{-1/2}(4^{N+1}-4)/3$, $h_m=\frac{2\pi}34^{-m}$,
averages over a period.

**Proposition 10.** With $c_0=\tanh(\frac12)^2/12$ and $c_1=\frac32(1-\frac3{4\sqrt2})\operatorname{sech}^4(2)$:
(i) $\tanh(2^{-1/2})\le\sup|F_N|<1$, $\operatorname{Lip}F_N=\Lambda_N$;
(ii) for $R\ge1$, $\sup_{|h|\le R/\Lambda_N}|F_N(\cdot+h)-F_N|\le N^{-1/2}(2\log_4(RN^{1/2})+4)\to0$;
(iii) $\mathbb EF_N=0$, $\mathbb EF_N^2\ge c_0$;
(iv) $\mathbb E|F_N(z+h_m)-F_N(z)|^2\ge c_1(N-m+1)/N$ for $1\le m\le N$;
(v) for every $c>0$ there are $N_0(c)$, $c_2(c)>0$, $C(c)$ such that for $N\ge N_0(c)$, every integer $j\ge0$ and
every interval $I$ of length $2\pi4^{-j}$ with $\operatorname{Var}_IF_N\ge c$: $N-j\ge cN-1$, and for $1\le m'\le N-j$,
$\mathbb E_I|F_N(z+h_{j+m'})-F_N(z)|^2\ge c_2(c)(N-j-m'+1)/N-C(c)N^{-1/2}$.

Proof. (i) $\mathbb Eg_N^2=\frac12$, and $|F'|\le|g'|\le\Lambda_N$ with equality at $0$. (ii) $|g(z+h)-g(z)|\le
N^{-1/2}\sum_k\min(2,4^k|h|)$, and at most $\log_4(RN^{1/2})+1$ indices have $4^k|h|>1$. (iii) A signed sum of four powers
of 4 vanishes only in cancelling pairs (uniqueness of base-4 digits), so any $Y=\sum r_k\sin(4^kz+\theta_k)$ has
$\mathbb EY^4\le3(\mathbb EY^2)^2$; Paley-Zygmund gives $P(g^2>\frac14)\ge\frac1{12}$. (iv) The increment of $g$ is a
lacunary sum with $r_k^2=2N^{-1}(1-\cos4^kh_m)$, and $4^kh_m\equiv\frac{2\pi}3$ mod $2\pi$ for $k\ge m$ because
$4^n\equiv1$ mod 3, so its mean square is $\ge\frac32(N-m+1)/N$; on $\{|g(z)|,|g(z+h_m)|\le2\}$, $|F(z+h)-F(z)|\ge
\operatorname{sech}^2(2)|g(z+h)-g(z)|$, and the complement has $\mathbb E[Y^21_{A^c}]\le(\mathbb EY^4)^{1/2}P(A^c)^{1/2}\le
\frac3{4\sqrt2}\mathbb EY^2$ ($P(A^c)\le2\mathbb Eg^4/16$). (v) Note $c<1$, as $|F_N|<1$. If $j=0$, $I$ is a full period of every mode and the claim
follows from (iv), since $c_2(c)\le c_1$. If $j>N$, every mode has $k<j$, and the bound on the variation of $L$ below gives
$\operatorname{Var}_IF_N\le\operatorname{Var}_Ig_N\le9/N<c$, so this case does not occur. Let $1\le j\le N$. The modes $k\ge j$ are $|I|$-periodic, so on $I$ averages of
polynomials in them are full-period averages, the fourth-moment bound of (iii) holds for lacunary sums over $k\ge j$, and
translates of such sums have the same distribution on $I$. Write $g_N=L+H$ with $L$ the sum over $k<j$, which varies on
$I$ by at most $N^{-1/2}\sum_{k<j}4^k|I|\le3N^{-1/2}$, and $\mathbb E_IH^2=(N-j+1)/(2N)\le\frac12$. Since $\tanh$ is $1$-Lipschitz,
$\operatorname{Var}_IF_N\le\operatorname{Var}_Ig_N$, so $c^{1/2}\le3N^{-1/2}+((N-j+1)/(2N))^{1/2}$, which gives $N-j+1\ge cN$ once
$3N^{-1/2}\le(1-2^{-1/2})c^{1/2}$. Let $N\ge9$ and let $L_0$ be the value of $L$ at the midpoint of $I$; by symmetry let
$L_0\ge0$. On $\{|H|\le L_0/2\}$, $F_N\ge\tanh(L_0/2-1)$, and $P_I(|H|>L_0/2)\le16\,\mathbb E_IH^4/L_0^4\le12/L_0^4$, so
$c\le\operatorname{Var}_IF_N\le\mathbb E_I|F_N-1|^2\le(1-\tanh(L_0/2-1))^2+48/L_0^4$, which forces $L_0<K_0(c)$ for a number $K_0(c)$
depending only on $c$. Let $K=K_0+4$ and $h=h_{j+m'}$. The increment of $L$ at $h$ is at most
$N^{-1/2}\sum_{k<j}4^kh\le\epsilon:=\frac{2\pi}9N^{-1/2}4^{-m'}\le1$, so $|L|\le K_0+2$ at $z$ and at $z+h$ for $z\in I$, and
$Y=H(\cdot+h)-H$ satisfies $\frac32(N-j-m'+1)/N\le\mathbb E_IY^2\le2$ as in (iv). On $A=\{|g_N(z)|,|g_N(z+h)|\le K\}$,
$|F_N(z+h)-F_N(z)|\ge\operatorname{sech}^2(K)(|Y|-\epsilon)_+$; off $A$ one of $|H(z)|,|H(z+h)|$ exceeds $2$, so $P_I(A^c)\le\frac3{32}$
and $\mathbb E_I[Y^21_{A^c}]\le\frac3{4\sqrt2}\mathbb E_IY^2$ as in (iv). With $(|Y|-\epsilon)_+^2\ge Y^2-2\epsilon|Y|$ and $\mathbb E_I|Y|\le\sqrt2$,
$\mathbb E_I|F_N(z+h)-F_N(z)|^2\ge\operatorname{sech}^4(K)\big((1-\frac3{4\sqrt2})\mathbb E_IY^2-2\sqrt2\epsilon\big)$, which is the claim with
$c_2(c)=\frac32(1-\frac3{4\sqrt2})\operatorname{sech}^4(K_0(c)+4)$, $C(c)=1$ and $N_0(c)=\max(9,9(1-2^{-1/2})^{-2}c^{-1})$. $\square$

With $M=\sup|F_N|$, $D=\Lambda_N$: (ii) is the plateau modulus of (UP) at a single time; it is invariant under
dilations $Mf(x/L)$, while regime (II) needs a dilation with $\Lambda_N/(ML)\to0$ (the undilated profile has
$D/M^2\to\infty$). (iii) is $L^2$ oscillation at the unit (energy) scale, and (iv), (v) show that (L2M) fails at the
unit scale and on every interval of length $2\pi4^{-j}$ retaining $L^2$ oscillation (take $m'\le(N-j)/2$, so the right side of (v) stays
above a positive constant while the shift tends to $0$ relative to the window). A direct numerical evaluation on
a grid of $48\cdot4^N$ points for $N=3,\dots,8$ was consistent with (i), (iii), (iv) at the sampled points ($\mathbb EF_N^2\approx0.28$, finite-difference
Lipschitz estimate within $0.6\%$ of $\Lambda_N$; the bound in (ii) is $O_R((1+\log N)/\sqrt N)$, and these small-$N$ checks do not verify its asymptotic decay).

**Proposition 10' (three-dimensional transfer).** Fix an axisymmetric $\chi\in C_c^\infty(\mathbb R^3)$, $0\le\chi\le1$,
with $\chi=1$ on the core $Q=\{|x_h|\le4,\ |x_3|\le4\pi\}$ ($x_h=(x_1,x_2)$), independent of $N$. Let
$G_N(z)=-\int_0^zF_N$, $v_N=\operatorname{curl}\big(\chi\,G_N(x_3)(-x_2,x_1,0)\big)$, $m_N=\|v_N\|_\infty$, $d_N=\operatorname{Lip}v_N$,
$E_N=\int|v_N|^2$, $\operatorname{Var}_Bv=\fint_B|v-(v)_B|^2$, $\beta=\frac{3\pi}8(1-\frac{\pi^2}{16})$, and let $C_\chi$ denote constants
depending only on $\chi$. Then $v_N$ is smooth, compactly supported, divergence free, axisymmetric and swirl free, and:
(i') $|G_N|\le\gamma_N:=\min\{\frac\pi4,\frac\pi{4\sqrt N}(1+\lceil\log_4\sqrt N\rceil)\}\to0$; $4\tanh(\sqrt{3N}/2)\le m_N\le C_\chi$;
$4\Lambda_N\le d_N\le C_\chi\Lambda_N$; $1024\pi^2c_0\le E_N\le C_\chi$;
(ii') for $R\ge1$, $\omega_{v_N}(R/\Lambda_N)\le C_\chi\big(N^{-1/2}(2\log_4(RN^{1/2})+4)+R/\Lambda_N\big)\to0$;
(iii') $\operatorname{Var}_{B_1(x)}v_N\ge\beta c_0$ whenever $1\le|x_h|\le3$ and $|x_3|\le4\pi-2$;
(iv') for such $x$ and $1\le m\le N$, $\fint_{B_1(x)}|v_N(y+h_me_3)-v_N(y)|^2dy\ge\beta c_1(N-m+1)/N$;
(v') if $c>0$, $N_k\to\infty$ and $\operatorname{Var}_{B_{\rho_k}(x_k)}v_{N_k}\ge c$ for some balls (any centres and radii), then
$(\rho_k)$ is bounded, and along a subsequence there are $t_k$ with $t_k/\rho_k\to0$ and
$\liminf_k\fint_{B_{\rho_k}(x_k)}|v_{N_k}(y+t_ke_3)-v_{N_k}(y)|^2dy>0$;
(vi') with $\lambda_N=d_N/m_N$, $e_N=E_N/m_N^2$ and $E_*>0$, the fields $u_N(x)=a_Nm_N^{-1}v_N(x/L_N)$, $a_N=\lambda_N^6$,
$L_N=(E_*/e_N)^{1/3}\lambda_N^{-4}$, have $\int|u_N|^2=E_*$, $M_N:=\|u_N\|_\infty=a_N\to\infty$, $D_N:=\operatorname{Lip}u_N=(e_N/E_*)^{1/3}\lambda_N^{11}\to\infty$,
$D_N/M_N^2=(e_N/E_*)^{1/3}\lambda_N^{-1}\to0$ and $\omega_{u_N}(RM_N/D_N)/M_N\to0$ for every $R>0$; under dilation of balls and
shifts by $L_N$, variances and averaged squared increments are multiplied by $(M_N/m_N)^2$, so (iii') and (iv') hold for $u_N$
with their lower bounds multiplied by this factor, and (v') holds in normalized form: if
$M_{N_k}^{-2}\operatorname{Var}_{B_{\rho_k}(x_k)}u_{N_k}\ge c>0$, then $\rho_k/L_{N_k}$ is bounded and along a subsequence there are $t_k$ with
$t_k/\rho_k\to0$ and $\liminf_kM_{N_k}^{-2}\fint_{B_{\rho_k}(x_k)}|u_{N_k}(y+t_ke_3)-u_{N_k}(y)|^2dy>0$ (without the factor $M_N^{-2}$ this
would be false: $u_N$ is nearly linear on small balls).
Consequently, for every choice of centres $x_N$ and scales $\ell_N$ (no lower bound on $\ell_N$ is needed), the
amplitude-normalized fields $W_N(y)=M_N^{-1}u_N(x_N+\ell_Ny)$ that retain $L^2$ oscillation on some $B_R$ fail the $L^2$
translation modulus at $\tau=0$, since $\int_{B_R}|W_N-(W_N)_{B_R}|^2=|B_R|M_N^{-2}\operatorname{Var}_{B_{R\ell_N}(x_N)}u_N$ and the same
identity holds for increments, with physical shifts divided by $\ell_N$; this includes windows near the axis and near the
edge of the support of $\chi$. Retained oscillation occurs at the scale $L_N$, comparable to the energy length
$(6E_*/(\pi M_N^2))^{1/3}$, by (iii'). These are single fields, not a Navier-Stokes trajectory: no evolution, record
condition, temporal admissibility or energy identity is involved.

Proof. Put $P=\frac\pi2$, $A=(\chi x_1,\chi x_2,0)$, $B=(-x_1\partial_3\chi,-x_2\partial_3\chi,2\chi+x_h\cdot\nabla_h\chi)$. The potential is smooth,
and the Cartesian curl with $G_N'=-F_N$ gives $v_N=A\,F_N(x_3)+B\,G_N(x_3)$; so $v_N$ is smooth, compactly supported (in
$\operatorname{supp}\chi$) and divergence free; its horizontal part is parallel to $x_h$ and its coefficients are rotation invariant, so
it is axisymmetric and swirl free. On $Q$, $v_N=(x_1F_N,x_2F_N,2G_N)$; the only nonzero entries of $\nabla v_N$ are $F_N,F_N,-2F_N$
on the diagonal and $x_1F_N',x_2F_N'$ in the last column. (i') $F_N$ is odd and $P$-periodic with mean zero, so $G_N$ is even and
$P$-periodic, and $|G_N|\le P/2$. Let $K=1+\lceil\log_4\sqrt N\rceil$ and $H=N^{-1/2}\sum_{K\le k\le N}\sin(4^kz)$. The function $\tanh H$ is
odd with period $T=2\pi4^{-K}$, so its primitive vanishing at $0$ is even and $T$-periodic and bounded by $T/2\le\frac\pi{4\sqrt N}$;
since $|F_N-\tanh H|\le|g_N-H|\le(K-1)N^{-1/2}$, for $|z|\le P/2$ one gets $|G_N(z)|\le\frac\pi4(K-1)N^{-1/2}+\pi4^{-K}\le\gamma_N$. With
$u=F_N^2$ and $F_N'=(1-u)g_N'$, on $Q$: $|\nabla v_N|^2=6u+|x_h|^2F_N'^2\le6u+16\Lambda_N^2(1-u)\le16\Lambda_N^2$ (Frobenius norm, as
$16\Lambda_N^2\ge6$), with equality at $(4,0,0)$, where $\nabla v_N$ has rank one, so $4\Lambda_N$ is attained for the operator norm
too; off $Q$, $|\nabla v_N|\le\|A\|_\infty\Lambda_N+\|\nabla A\|_\infty+\|B\|_\infty+\|\nabla B\|_\infty\gamma_N$. Next $g_N(\frac{2\pi}3)=\frac{\sqrt{3N}}2$
($4^k\equiv1$ mod $3$) and $|v_N(4,0,z)|\ge4|F_N(z)|$ give the lower bound for $m_N$, and $m_N\le\|A\|_\infty+\|B\|_\infty\gamma_N$. Finally
$E_N\ge\int_Q|v_N|^2=1024\pi^2\mathbb E_PF_N^2+512\pi^2\mathbb E_PG_N^2\ge1024\pi^2c_0$ by (iii) (the core has height $16P$, and
$\int_{|x_h|\le4}|x_h|^2dx_h=128\pi$), and $E_N\le2\|A\|_2^2+2\gamma_N^2\|B\|_2^2$. (ii') $\omega_{v_N}(t)\le\|A\|_\infty\omega_{F_N}(t)+(\|\nabla A\|_\infty+\|B\|_\infty+\frac\pi4\|\nabla B\|_\infty)t$,
using $|F_N|\le1$ and $|G_N'|\le1$; apply (ii).

Ball averages. For a ball $B_\rho(x)$ with $r_0=|x_h|$ and $a=x_3$, the normalized vertical marginal is
$w(z)=\frac3{4\rho}(1-(z-a)^2/\rho^2)_+$, and conditionally on $y_3=z$ the horizontal variable is uniform on the disk of radius
$(\rho^2-(z-a)^2)^{1/2}$ centred at $x_h$. Writing $\mathbb E_w$, $\operatorname{Var}_w$ for this weight, for balls in $Q$
$$\operatorname{Var}_{B_\rho(x)}v_N=r_0^2\operatorname{Var}_wF_N+\tfrac12\mathbb E_w[(\rho^2-(z-a)^2)F_N^2]+4\operatorname{Var}_wG_N,\qquad
\fint_{B_\rho(x)}|v_N(y+he_3)-v_N(y)|^2\ge r_0^2\,\mathbb E_w|F_N(z+h)-F_N(z)|^2$$
(the second when the translated ball also lies in $Q$). (iii'), (iv'): for $\rho=1$, $w\ge\frac34(1-\frac{\pi^2}{16})$ on the interval of
length $P$ centred at $a$, so $\mathbb E_wf\ge\beta\,\mathbb E_Pf$ for nonnegative $P$-periodic $f$. Apply this to $|F_N-b|^2$ (infimum over $b$;
$\mathbb E_PF_N=0$ and (iii)) and to $|F_N(\cdot+h_m)-F_N|^2$ ((iv)), with $r_0\ge1$; the balls and their translates by $h_m<1$ lie in $Q$.

Weighted averages of periodic functions. If $f\ge0$ is $T$-periodic and $\eta=3T/(2\rho)$, then
$(1-\eta)\mathbb E_Tf\le\mathbb E_wf\le(1+\eta)\mathbb E_Tf$: indeed $\int fw=\int_0^Tf(u)\sum_{\ell\in\mathbb Z}w(u+\ell T)\,du$ and
$|T\sum_\ell w(u+\ell T)-1|\le T\|w'\|_1=3T/(2\rho)$. 

Scalar lemma. Let $4^{-j-1}<\rho\le4^{-j}$ with $j\ge0$, $s=5$ (so $4^s\ge192\pi$), $K=j+s$, $g_N=L+H$ with $L$ the modes $k<K$ and $H$
the modes $K\le k\le N$ ($H=0$ if $K>N$), $n=N-K+1$, $T=2\pi4^{-K}$, so that $\eta\le12\pi4^{-s}\le\frac1{16}$. For $1\le m'\le N-j$ and
$h=h_{j+m'}$, $L$ varies on $[a-\rho,a+\rho]$ by at most $d=N^{-1/2}4^K\rho/3\le4^sN^{-1/2}/3$ and $|L(z+h)-L(z)|\le e:=\frac{2\pi}9N^{-1/2}4^{s-m'}$.
(a) Let $q\in(0,1]$, $K_0(q)=\max\{2+\frac12\log(8/q),(102/q)^{1/4}\}$ and $N\ge4^{2s+1}/(9q)$, so that $d\le\sqrt q/2$ and $d+e\le1$.
If $\operatorname{Var}_wF_N\ge q$, then $n\ge\frac{8q}{17}N$ and $|L(a)|\le K_0(q)$. Indeed, $\tanh$ is $1$-Lipschitz and standard deviations
are subadditive, so $\sqrt q\le d+(\mathbb E_wH^2)^{1/2}$; if $K>N$, then $H=0$ and $\sqrt q\le d\le\sqrt q/2$, which is impossible, so
$K\le N$, $n\ge1$, and $\sqrt q\le d+((1+\eta)n/(2N))^{1/2}$, which gives the first claim. For the second, let $L_0=L(a)>K_0$ (the case $L_0<-K_0$ is symmetric, with $F_N+1$ in place of $F_N-1$). By the fourth-moment bound
of (iii) and the averaging inequality, $\mathbb E_wH^4\le\frac{17}{16}\cdot\frac34$; on $\{|H|\le L_0/2\}$, $g_N\ge L_0/2-1>0$, so
$q\le\mathbb E_w|F_N-1|^2\le(1-\tanh(L_0/2-1))^2+4\cdot16\,\mathbb E_wH^4/L_0^4\le4e^{-2(L_0-2)}+51L_0^{-4}<q$, a contradiction.
(b) If $|L(a)|\le K_1$ and $d+e\le1$, then
$\mathbb E_w|F_N(z+h)-F_N(z)|^2\ge\operatorname{sech}^4(K_1+5)\big[\frac98(N-j-\max(s,m')+1)/N-\frac{2\pi}3N^{-1/2}4^{s-m'}\big]$. Indeed,
$Y=H(\cdot+h)-H$ is a lacunary sum of period $T$ with $J=\mathbb E_TY^2\in[\frac32(N-\max(K,j+m')+1)/N,\,2]$ (as in (iv)) and
$\mathbb E_TY^4\le3J^2$. On $\mathcal A=\{|H(z)|,|H(z+h)|\le4\}$, $|g_N|\le K_1+5$ at $z$ and $z+h$, so
$|F_N(z+h)-F_N(z)|\ge\operatorname{sech}^2(K_1+5)(|Y|-e)_+$. The averaging inequality gives $P_w(\mathcal A^c)\le3(1+\eta)/512$,
$\mathbb E_w[Y^21_{\mathcal A^c}]\le(1+\eta)\frac3{16\sqrt2}J$, $\mathbb E_wY^2\ge(1-\eta)J$ and $\mathbb E_w|Y|\le(2(1+\eta))^{1/2}<\frac32$; with
$(|Y|-e)_+^2\ge Y^2-2e|Y|$ and $1-\eta-(1+\eta)\frac3{16\sqrt2}\ge\frac34$ this gives at least $\operatorname{sech}^4(K_1+5)(\frac34J-3e)$.

(v') Since $c\le\fint_{B_{\rho_k}(x_k)}|v_{N_k}|^2\le E_{N_k}/|B_{\rho_k}|$, $\rho_k$ is bounded, and the balls meet $\operatorname{supp}\chi$, so the centres
are bounded; pass to $x_k\to x$, $\rho_k\to\rho\in[0,\infty)$, and write $N=N_k$. If $\rho=0$: on the ball,
$v_N=A(x_k)F_N(y_3)+R_k$ with $|R_k|\le\|\nabla A\|_\infty\rho_k+\|B\|_\infty\gamma_N\to0$; as the standard deviation is the $L^2$ distance to
constants, $\sqrt c\le|A(x_k)|(\operatorname{Var}_wF_N)^{1/2}+o(1)$, so eventually $|A(x_k)|\ge\sqrt c/2$ and $\operatorname{Var}_wF_N\ge q:=\min\{1,c/(4\|A\|_\infty^2)\}$.
By (a) and (b) with $m'=\lfloor(N-j)/2\rfloor\ge\frac{4q}{17}N-1$ and $t_k=h_{j+m'}$: $t_k/\rho_k<\frac{8\pi}34^{-m'}\to0$ and
$\liminf\mathbb E_w|F_N(z+t_k)-F_N(z)|^2\ge\operatorname{sech}^4(K_0(q)+5)\frac{9q}{34}$. Since $v_N(y+t_ke_3)-v_N(y)=A(x_k)(F_N(y_3+t_k)-F_N(y_3))+R'_k$
with $|R'_k|\le\|\nabla A\|_\infty(2\rho_k+t_k)+2\|B\|_\infty\gamma_N\to0$, the reverse triangle inequality in $L^2$ gives the claim. If $\rho>0$:
$A$ does not vanish identically on $B_\rho(x)$, for otherwise $|v_N|\le\|B\|_\infty\gamma_N$ there, and since $|v_N|\le C_\chi$ and
$|B_{\rho_k}(x_k)\triangle B_\rho(x)|\to0$, $\fint_{B_{\rho_k}(x_k)}|v_N|^2\to0$. Choose a ball $B_\delta(y_*)\Subset B_\rho(x)$, $\delta\le1$, on which $|A|\ge a_0>0$; it
lies in $B_{\rho_k}(x_k)$ for large $k$. For this fixed ball (with its $j$ and weight), $|L|\le(j+s)N^{-1/2}\le1$ once $N\ge(j+s)^2$, so (b)
applies with $K_1=1$ and $m'=\lfloor N/2\rfloor-j$, giving $\liminf\mathbb E_w|F_N(z+h_{\lfloor N/2\rfloor})-F_N(z)|^2\ge\frac9{16}\operatorname{sech}^4(6)$. As before,
$v_N(y+h e_3)-v_N(y)=A(y)(F_N(y_3+h)-F_N(y_3))+O(\|\nabla A\|_\infty h+\|B\|_\infty\gamma_N)$ with $|A|\ge a_0$ on $B_\delta(y_*)$, so the average
over $B_\delta(y_*)$ stays positive, and the average over $B_{\rho_k}(x_k)$ is at least $|B_\delta|/|B_{\rho_k}|$ times it; $h_{\lfloor N/2\rfloor}/\rho_k\to0$.
(vi') Dilations give $\|u_N\|_\infty=a_N$, $\operatorname{Lip}u_N=a_N\lambda_N/L_N$, $\int|u_N|^2=a_N^2L_N^3e_N$, which with the stated $a_N,L_N$ are the
formulas claimed; $\lambda_N\asymp_\chi\Lambda_N\to\infty$ and $e_N\asymp_\chi1$ by (i'). Also $\omega_{u_N}(RM_N/D_N)/M_N=\omega_{v_N}(Rm_N/d_N)/m_N\to0$ by (ii')
and (i') ($m_N/d_N\le C_\chi/\Lambda_N$), and, since $u_N=(M_N/m_N)v_N(\cdot/L_N)$, $M_N^{-2}$ times the variance, or the average squared increment with shift $tL_N$, of $u_N$
on $B_{\rho L_N}(L_Nx)$ equals $m_N^{-2}$ times the corresponding quantity of $v_N$ on $B_\rho(x)$ with shift $t$, where $m_N\asymp_\chi1$. $\square$

So in three dimensions, where unlike the periodic profile of Proposition 10 the energy is finite and fixed, the
single-time conditions used in this report (fixed energy, amplitude and
Lipschitz normalizations with $D/M^2\to0$, the plateau modulus of (UP), $L^2$ oscillation retained at a scale comparable
to the energy length) are compatible with the failure of (L2M) at $\tau=0$ for every amplitude-normalized window that
retains $L^2$ oscillation, at every centre and scale. An exclusion of (C) must use the evolution or single-time
information beyond the conditions tested here. The constants of
Proposition 10' are not optimized.

## Limitations / Open Questions

1. Within the strategy of admissible amplitude-$M$ isotropic normalizations, the first missing implication is the
   exclusion of (C) for the actual fixed-data trajectory, i.e. a uniform local
   $L^2$ translation modulus (L2M) with retained $L^2$ oscillation at $\tau=0$ at some admissible amplitude-$M$ scale.
   Sufficient conditions: the local vorticity bound (VL1) or its one-sided form (Corollary 6A), the sup-norm
   level-scale condition, or (L2LS). Vanishing
   of a Reynolds defect alone is not the retained-oscillation, uniform-in-time compactness criterion required in (B); no
   equivalent defect criterion for the exclusion of (C) is proved here (Section 6, Remark (i)). Section 10 shows that the
   one-dimensional forms of the single-time conditions used here (amplitude and Lipschitz normalizations, the plateau
   modulus after a dilation, retained oscillation at the energy scale) do not give it, for a one-dimensional model
   profile and, by Proposition 10', for a family of three-dimensional divergence-free axisymmetric swirl-free fields of
   fixed energy on which every retained-oscillation window fails (L2M); so the exclusion of (C) has to use the
   evolution (or single-time information not used here). By Proposition 7(c), only
   velocity Type II singularities can fall into (C).
1'. In the weaker sense of Section 6A the missing implication is the exclusion of (C*) = (FLAT) or (C*-D), by
   Proposition 14A equivalently of (FLAT$_0$) and of (C*)$\cap$(HD). A
   dimensional scenario was tested against the scalar bounds given by the energy, the energy ball, $M'\le24MD$, velocity
   Type II, the Beale-Kato-Majda criterion and the swirl bounds $S^2\le CGD$ (a scalar consistency check, not a
   construction and not a verification of compatibility with the full system): $M\sim h^{-3/5}$,
   $D\sim h^{-11/10}$ ($h=T_*-t$), a logarithmic jet with amplitude $o(M)$ per octave, a strain at the Lipschitz scale
   of the sub-amplitude structures and a swirl tube of core $D^{-1/2}$. Its exponent bookkeeping was checked
   symbolically; it postulates historical BMO $=o(M)$, which is (FLAT$_0$) of Proposition 14A and gives (FLAT) by
   Proposition 14(c), and it was not found to contradict the published
   regularity criteria for axisymmetric flows with swirl that were checked (as reported by the second-model
   consultation; the original statements were not all re-read). The meridional vorticity budget
   $\|\eta(t)\|_1\le\|\eta_0\|_1+\int_0^t\|\partial_z(q^2)\|_1$ requires an axial modulation of the swirl in that scenario. This
   is heuristic evidence that (FLAT) cannot be excluded by the a priori bounds used here; it is not a construction
   and not a counterexample. In such a flat scenario every weak limit of an admissible amplitude-$M$ isotropic normalization is constant; heuristically, sub-amplitude limits
   with a constant Galilean boost are logarithmically unbounded or carry a uniform far-field pressure force, and the
   boundedness requirement of GOAL, rather than compactness, appears to be the obstruction. Subject to the quantitative regularity input granted
   in Proposition 14B(a), Proposition 14B(c) makes part of this precise: if $D/\Theta_0^2$ does not tend to $0$, gradient records along a sequence with
   $D(t_n)\ge\delta\Theta_0(t_n)^2$ give, along a subsequence, a nonconstant ancient limit at the BMO amplitude whose
   pressure gradient is exactly the increment pressure (no uniform force survives); after a constant horizontal boost it
   is axisymmetric about a fixed line with nonzero swirl; it grows at most logarithmically on each finite time slab, and
   its global boundedness is not proved. Finite energy limits the flatness itself: by Proposition 14C, unconditionally in
   regime (II), $\Theta_0\ge cM/\log(E_0M)$ near $T_*$, so (FLAT$_0$) can hold only at a logarithmic rate. This estimate permits (FLAT$_0$), and the arguments given here
   do not exclude it; a dynamical argument could exclude it without sharpening this estimate, and none is given.
   Proposition 14D adds that a large mean persists along its own path for a time $\delta_n\ge ce^{\kappa h_n}/(h_nm_n^2)$ between
   dyadic records and, for $t_{n-1}\le t<t_n$, bounds $M(t)^2(T_*-t)$ below by $ce^{\kappa h_{n+1}}/h_{n+1}$ in terms of the flatness
   ratio $h_{n+1}=M(t_{n+1})/\Theta_0(t_{n+1})$ of the next dyadic record (whenever $h_{n+1}\ge h_*$); under (FLAT$_0$) this
   bound tends to infinity, but the dissipation certified by the proposition is summable. By the Remark on the pressure
   impulse after Proposition 14D: at every sufficiently large dyadic record with $h_n\ge h_*$, the signed pressure impulse
   $J_n$ along a backward-diffusing packet, over the age interval $\varsigma_n=KE_0^{2/3}m_n^{-4/3}$, is at least $m_n/2$, and the
   older averaged velocity has norm at most $m_n/4$. A bound $J_n\le C(u_0)\Theta_0(t_n)$ on an infinite subsequence would exclude
   (FLAT$_0$); no such bound is proved.
1''. For general bounded divergence-free families a time-integrated curl bound gives no compactness of the terminal
   slice at the original terminal time (an explicit family with a uniformly bounded time-integrated curl has terminal
   slices that converge only weakly, Section 8). For Navier-Stokes trajectories this gap is closed by Lemma 21: (EC), and
   hence (VC), implies (L2M), so with (OSC$_0$) GOAL holds in $C_tL^2_{loc}$ at the physical terminal time (Proposition 22);
   the rules of Theorem 17 and Proposition 20(b) remain correct but are not needed for this conclusion. Theorem 17 shows that this is not an obstruction to GOAL in the
   topology (ST): for an admissible normalization with (OSC$_0$) and a joint subsequence on which $\mathcal R=0$, an
   explicit rule selects a slice within one Euler time before $s_n$; along a further subsequence the slices converge
   strongly there and the terminal limit is nonconstant. For a certified normalization what remains
   open is (EC) (or (VC)) itself on the physical records; the gap between (ST) and the $C_tL^2_{loc}$ convergence of
   Theorem 5 remains only for defect-free normalizations without such a vorticity certificate. Proposition 16(b)
   gives convergence at the original terminal time when the limit is classical near $\tau=0$; a certificate for this on
   the physical records is missing. Proposition 15
   needs a terminal quiet zone and a far-tail bound at amplitude $o(M)$ that are not derived; the available far-field
   bound for the time-integrated tail is $16\pi A_nW_n^2/R_n$ with $W_n=M(t_n)/B_n$, and no estimate relates these quantities.
   Proposition 20 weakens (VC) to the exterior bound (EC). On the (C*-D) side a sufficient route (not a proved
   equivalent) is (EC) for one certified normalization, that is, a bound on the meridional vorticity at distance at least $h\ell_n$ from the axis that
   is inherited from earlier times or carried out of the swirl core; the swirl source itself is negligible there
   (Lemma 19), and nothing controls this inherited vorticity (Section 9B, Remark (iii)); by Lemma 26A it is carried, up to $o(1)$, by fluid
   that did not visit the tube $\{r_n\le a_n\}$, $a_n\to0$, during the last $A_n\to\infty$ Euler times, which neither locates its
   generation (diffusion moves vorticity between particles) nor bounds it; Lemma 21 propagates such a bound
   forward over bounded Euler times but does not create one. By Proposition 25, for single-time fields the failure of
   the exterior mass bound at every certified scale is compatible with compactness of the certified rescalings, so (EC)
   may be strictly stronger than the exclusion of (C) (a strict separation for trajectories is not proved), and (EC)
   cannot follow from the single-time constraints tested there alone. Bounds of order $M_n\ell_n^2$ on the dissipation of
   every fixed rescaled window of one certified normalization would give (EC) (Section 9D, Remark (ii)); they are not proved.
2. Approaches that were tried and fail, with the reason:
   the global bound on $\|\omega^\theta\|_1+\int\!\!\int|\omega^\theta|/r^2$ off the axis (it gives the vorticity
   certificate only at axis distances $r_0\gtrsim K/(M\ell)$, while a size-$M$ structure of scale $\ell$ at distance $r_0$
   has energy $\sim M^2\ell^2r_0$, forcing $r_0\lesssim E_0/(M^2\ell^2)\ll K/(M\ell)$);
   the centrifugal reformulation (the meridional field solves swirl-free Navier-Stokes with a forcing
   $(u^\theta)^2/r\,e_r$ whose rescaled local $L^1$ norm is $O(GD/M^2)\to0$; vanishing forcing gives no compactness) and
   backward inheritance of fine-scale vorticity along the meridional flow;
   Kolmogorov-scale normalizations (local limits such as a Burgers vortex in a strain are unbounded);
   amplitude-$M$ gradient-record normalization at length $M/D$ in regime (II) (only constant limits under (UP));
   energy and temporal certificates (fail under (UP), Proposition 7);
   the energy-scale normalization (bounded energy and total dissipation do not exclude a Reynolds defect; frozen
   laminated shear layers are stationary for Euler);
   local-amplitude rescalings (the far-field pressure is not controlled; without a sufficient tail estimate such as a
   quiet zone a spatially uniform force may survive);
   Galilean $\epsilon$-regularity at the BMO amplitude and the BMO-class Liouville route (Proposition 14B: subject to the quantitative
   regularity input granted in (a), it gives only $D\le C_a+C\Theta_0^2$ and, along sequences with $D(t_n)\ge\delta\Theta_0(t_n)^2$, subsequential nonconstant ancient limits,
   axisymmetric with nonzero swirl after a constant boost, that are not shown to be bounded; the axisymmetric Liouville
   case with swirl remains and contains the bounded-circulation case of the KNSS conjecture, open in the literature we
   read (Remark (iii) after Proposition 14B), and its positive resolution would force $D/\Theta_0^2\to0$ but leave (FLAT$_0$) open);
   backward uniqueness for the limits of Proposition 14B(c) (if such a limit $v$ had $\operatorname{curl}v(\cdot,0)=0$ outside a ball,
   then $v(\cdot,0)$ would be the Biot-Savart field of a bounded compactly supported vorticity plus an entire harmonic field of
   logarithmic growth, hence bounded; the bound would extend to every finite backward slab (the common facts of
   Proposition 14B(b) bound $\nabla^2v$ and part (a) bounds $\Pi[v]$, and integrating $dv/d\sigma=\Delta v-\Pi[v]$ along the
   material curves of the globally Lipschitz field $v$ gives $\|v(\sigma)\|_\infty\le\|v(0)\|_\infty+C|\sigma|$), and the exterior backward
   uniqueness and unique continuation theorems of Escauriaza, Seregin and Sverak, in versions reported by the second model
   and not read by us, would make $v$ constant; but nothing gives exterior vanishing of the terminal normalized vorticity
   $\Theta_n^{-2}\omega(x_n+\Theta_n^{-1}y,s_n)$ on the physical records, and, under the input granted in Proposition 14B(a),
   such a rigidity conclusion for every sequence covered by 14B(c) would give $D/\Theta_0^2\to0$, and hence
   $\kappa_n\to\infty$ for the sequences of Remark (ii) after Proposition 14B, which still leaves (FLAT$_0$) open);
   a Gaussian frequency for $q=u^\theta/r$ (with $q$ lifted radially to $\mathbb R^4\times\mathbb R$, $X_0$ fixed on the axis,
   $F(\xi,s)=q(X_0+\sqrt{T_*-t}\,\xi,t)$, $s=-\log(T_*-t)$ and $d\mu=(4\pi)^{-5/2}e^{-|\xi|^2/4}d\xi$ on $\mathbb R^5$, the quotient
   $N=\|\nabla F\|_{L^2(\mu)}^2/\|F\|_{L^2(\mu)}^2$, defined where $\|F\|_{L^2(\mu)}>0$, satisfies
   $dN/ds\le(T_*-t)M^2N+4(T_*-t)^2D^2$, and at the scalar rates of Remark (ii) after Proposition 14B neither coefficient is
   integrable in $s$; centring on an axial material curve bounds the remaining drift by $C(T_*-t)D|\xi|$, an available
   bound whose prefactor also diverges at those rates, so the inequality gives no uniform frequency control there; and a
   bound on $N$ alone would not give oscillation of the velocity at amplitude $M$);
   the Hessian at gradient records (controls a point, not a neighbourhood);
   the global $L^1$ bound for $\eta$ (deficit $(E_0M)^{1/2}$) and the a priori $L^1$ bound for $\omega^\theta$ with
   swirl (Lemma 9', supercritical);
   Euler Liouville arguments (false: the steady jet $e^{-r^2}e_z$, whose canonical pressure is constant, and, in the
   laboratory frame, the uniformly translating spherical vortex of M. J. M. Hill (Phil. Trans. R. Soc. Lond. A 185
   (1894)), a Lipschitz weak solution with velocity $O(|x|^{-3})$ at infinity, are nonconstant bounded ancient swirl-free
   Euler solutions with canonical pressure; the second is classical and was not re-derived here);
   dissipation budgets (they exclude actively dissipating cascades, not frozen ones);
   viscous cancellation of the two signed masses of Corollary 6A (the cancellation rate $2\nu\int_{\{w=0\}}|\nabla w|\,d\mathcal H^1$
   at the sign changes of the normalized meridional vorticity $w$ admits no lower bound of the alternating-layer form
   $c\nu m^3$, $m$ the smaller signed mass on a fixed rectangle: exact swirl-free pipe flows $f(r,t)e_z$ (independent of $z$, hence of infinite energy, and changing with $k$), with $f$ solving
   the radial heat equation from $f(r,0)=\chi(r)F(\pi kr^2)$, where $F(\theta)=\frac98\cos\theta-\frac18\cos3\theta$ has flat extrema
   ($F'=-\frac32\sin^3\theta$) and the cutoff $\chi$ equals $1$ near $[1,\sqrt2]$ and vanishes near $r=0$, keep both signed masses of
   order $k$ on $[1,\sqrt2]\times[0,1]$ for $k^{1/4}$ Euler times at normalized viscosity $k^{-13/4}$, while their total, the
   meridional mass $\int_1^{\sqrt2}|\partial_rf|\,dr=2k$ of that rectangle, decreases only by $O(k^{-1})$: at heat time $\nu t=k^{-3}$
   the exact radial heat flow multiplies the modes $e^{\pm i\pi kr^2}$ and $e^{\pm3i\pi kr^2}$ by $e^{-x}$ and $e^{-9x}$, $x=4\pi^2r^2/k$,
   up to perturbations $O(k^{-2})$ in sup norm, the cutoff contributes $O(e^{-ck^3})$ in $C^1$ on $[1,\sqrt2]$, and at the $k+1$
   points where $\pi kr^2\in\pi\mathbb Z$ the values $\pm1$ change by $\frac98(1-e^{-x})-\frac18(1-e^{-9x})+O(k^{-2})=\frac92x^2+O(k^{-2})$,
   so the variation through these points, which bounds the mass from below, is $2k-O(k^{-1})$; the flat extrema matter,
   since for $F=\cos$ the values change by $1-e^{-x}\approx x$ and the loss tends to $12\pi^2$);
   concentration-cancellation with record freezing (window weak limits solve the Euler-Reynolds system with a nonnegative
   defect, which vanishes exactly when the convergence is strong; with $\epsilon^p_n=\sup_{s\le t_n}\|\nabla p(s)\|_\infty/(M_nD_n)$,
   which tends to $0$ under (UP) by Proposition 7(a), Proposition 7(b) bounds the relative record increase over $A$ window
   Euler times $\ell_n/M_n$ only by $A\epsilon^p_n\sigma_n$, $\sigma_n=\ell_nD_n/M_n$, and $\sigma_n\to\infty$ in (C) for
   normalizations with (OSC$_0$) (Proposition 22(d)), so this bound does not show that the record is frozen; and even a frozen record does
   not force a window mean to be saturated: stationary Euler pipe flows $f_n(r)e_z$ with a plateau at the axis and an
   oscillating annulus have frozen records, vanishing subscale flux and a positive defect);
   a near-axis cancellation functional (with $D_t=\partial_t+u^r\partial_r+u^z\partial_z$, $\Delta_5=\partial_r^2+3r^{-1}\partial_r+\partial_z^2$,
   gradients taken in $(r,z)$ and expressions on the axis read through the smooth axisymmetric extension, $q=u^\theta/r$, $Q=\partial_zq$ and $\phi=\psi/r$, where $b=\operatorname{curl}(\psi e_\theta)$, so that $-\Delta_5\phi=\eta$, $H=\frac12(Q^2+\eta^2)$ satisfies
   $(D_t-\Delta_5)H=-|\nabla Q|^2-|\nabla\eta|^2+Q\mathcal E$ with $\mathcal E=-2q(\phi_{rr}+3\phi_r/r)+rq_r\phi_{zz}-r\phi_{rz}Q$, and on
   the axis $Q\mathcal E=-8qQ\phi_{rr}$, which has no sign; for data with $\phi=A+cr^2$, $q=q_0+q_1z$ near a point of the axis, $c<0<q_0,q_1$,
   one gets $D_tH=-16cq_1q>0$ there at the initial time while $\nabla Q=\nabla\eta=0$);
   selection by production events (the source records $\max_{s\le t}\|\partial_z(q^2)(s)\|_\infty$ are physical events and, in (C),
   grow faster than $D$ along the times of Corollary 6A, but a source maximum does not force retained velocity oscillation:
   in a smooth compactly supported single-time family, a jet $n^{24}e_z$ on a ball of radius $n^{-16}$ contains a swirl packet
   of amplitude $n^{18}$ and radius $n^{-24}$ that carries the source maximum $x_*$, and a remote packet of amplitude $n^{21}$
   and radius $n^{-21}$ fixes $S\asymp n^{21}$, with $M\asymp n^{24}$, $D\asymp n^{42}$; for every $B\in[S,M]$ the rescaling
   $(u(x_*+(B/D)y)-n^{24}e_z)/B$ is $O(n^{-3})$ on bounded sets; the budget of the Remark after Lemma 9' is compatible with
   the available upper bound and is not assigned to windows);
   finite-energy closure of pipes and an energy charge for record increases (proposed constructions, not established
   here: for smooth compactly supported radial $f_0$ with $\int_0^\infty rf_0\,dr=0$, the solution $f$ of
   $f_t=\nu(f_{rr}+r^{-1}f_r)$, $f(\cdot,0)=f_0$, $a=r^{-1}\int_0^r\rho f\,d\rho$ and an axial cutoff $\chi\in C_c^\infty(\mathbb R)$ equal to
   $1$ near $0$, the field $V_L=(-L^{-1}a\chi'(z/L),0,f\chi(z/L))$ in cylindrical components $(r,\theta,z)$ is divergence
   free, has finite energy and solves Navier-Stokes with zero pressure up to a residual of order $L^{-1/2}$ in $H^s$ on a
   fixed time interval; applied to the profiles of the item on viscous cancellation this suggests exact finite-energy
   solutions with changing data, $D/M^2\to0$ and windows with (L2-OSC) but without (L2M), but a stability estimate with
   its dependence on $L$, on $k$ and on the divergent number of Euler times, the diagonal choice of the parameters and
   the verification of the historical record properties after rescaling are not carried out here; separately, a suitably
   positioned remote packet can have a canonical-pressure contribution that accelerates a constant core $e_z$ carrying the
   speed maximum (the sign depends on the position of the packet as well as on the distribution of its kinetic energy),
   and for a fixed smooth profile at amplitude $M$ and scale $\ell$ the dissipation over one Euler time is of order $(M\ell)^{-1}$
   times the energy, the ratio of the viscous cost $M\ell^2$ of an Euler window to its energy $M^2\ell^3$; using this for an
   exact-solution family needs control of its normalized enstrophy over that time; these observations suggest that
   record increases need not be charged by dissipation, but neither this nor a fixed-factor increase of the global
   record of an actual solution within one Euler time is established; neither proposal is used as a counterexample, and
   neither involves swirl);
   pigeonhole over certified windows with the local budget of Lemma 9' (the total weight of certified windows with boundedly
   overlapping persistence cylinders is finite by energy, Proposition 24, and absolute continuity of the budget gives no rate);
   choice of scale at a certified point using the bound $\int_{B_R}|w|\le\sqrt2|B_R|\sigma$ (single-time obstruction,
   Proposition 25);
   the Lagrangian form of the swirl source (for Euler, with labels $a=(r_0,z_0)$, $r_0>0$, at time $t_1$ and the meridional flow
   map $X$, Cauchy's formula gives $(\det D_aX)\,\omega^\theta(X(a,t),t)=\omega^\theta(a,t_1)+\frac12\{\Gamma(t_1)^2,\rho\}_a$, where
   $\{f,g\}=f_rg_z-f_zg_r$ and $\rho=\int_{t_1}^tr(X(a,s),s)^{-2}ds$, so for a compact label set $E\subset\{r_0>0\}$, with
   $\Phi=(\Gamma(t_1)^2,\rho)$ and $N_E(\xi)$ the number of points of $E$ mapped to $\xi$, the area formula gives the unweighted
   meridional mass of the net source contribution $\omega^\theta(X(a,t),t)-(\det D_aX)^{-1}\omega^\theta(a,t_1)$ on $X(E,t)$ as
   $\frac12\int_{\mathbb R^2}N_E(\xi)\,d\xi\le\frac12|\Phi(E)|\operatorname{ess\,sup}N_E$ (this does not control the time integral of the
   absolute source); no bound on $N_E$, and none on the viscous remainders of the Navier-Stokes version, which contain
   brackets with $\rho$, is proved, and the kinematic information alone gives none: if the meridional velocity vanishes
   on an annular region, then $\rho=(t-t_1)/r_0^2$ there, and a swirl whose square runs $k$ times through the same range in
   $z_0$ gives $N_E=k$ almost everywhere on the image; such prescribed fields are not Euler solutions, so this does not
   exclude a bound that uses the dynamics; iterating over blocks of Euler times returns to the history problem of Section 9B);
   quantitative Liouville theorems across scales and backward propagation of concentration (in viscous units
   $v_n(X,t)=M_n^{-1}u(x_n+X/M_n,s_n+t/M_n^2)$ the Euler window has radius $L_n=M_n\ell_n\to\infty$ and, on windows with retained
   oscillation, the history has depth $s_nM_n^2$, much larger than $L_n^2$, so time depth is not the obstruction; but the maximum-principle lemma behind the
   Liouville theorem of Koch, Nadirashvili, Seregin and Sverak has constants that depend on the domain and the drift
   bound and degenerate with the radius: $w=\tanh(Y_5/2)$ solves $w_t-w\,\partial_5w-\Delta w=0$ in $\mathbb R^5$ with drift of size
   at most $1$, its supremum on $B_{2R}$ is $\tanh R$, its value at $(R/2)e_5$ is smaller only by the factor
   $1-\tanh(R/4)/\tanh R=2e^{-R/2}(1+o(1))$, and it vanishes at the centre; this drift is not a Navier-Stokes velocity, so the
   example only shows that a scale-uniform version needs further structure; the swirl source, of size $O(\epsilon)$ when
   the normalized swirl is $\epsilon$ and three derivatives are bounded, costs an error $O(\epsilon R^2)$ over viscous time $R^2$; the
   Holder estimate of Lei and Zhang (arXiv 1011.5066) for $\Gamma$ at the axis depends on a scale-invariant drift quantity
   which, at radii comparable to $R$, is at least of order $R$ on the exact pipe flows
   $\frac{R^2}{2R^2+t}e^{-r^2/(4(2R^2+t))}e_z$, $-R^2\le t\le0$, which are bounded by $1$; and the Liouville theorem of Lei, Zhang and
   Zhao (arXiv 1701.00868) for solutions with swirl assumes $\Gamma\in L^\infty_tL^p_x$, a norm multiplied by $M_n^{3/p}$ under
   this rescaling; on the other hand, failure of (L2M) at shifts $\rho_n$ with $M_n^2/D_n\ll\rho_n\ll L_n$ in these units gives
   $\int_{B_{(R+2)L_n}}|\omega_n|^2\ge c_RL_n^3/\rho_n^2$ at the failing time, but the coefficients of the vorticity equation
   rescaled to that shift, of sizes $\rho_n$ and $\rho_n^2D_n/M_n^2$, diverge, and the backward enstrophy charge this gives
   over the last $M_n^2/D_n$ units of viscous time is $o(M_nE_0)$, below the available dissipation budget; the critical $L^3$
   bound used in Tao's quantitative argument for the Escauriaza-Seregin-Sverak theorem is not supplied by energy);
   normalization at records of $r|u^{mer}|$, with $u^{mer}=u^re_r+u^ze_z$ the meridional velocity and $r$ the distance to the
   axis (a singular solution cannot satisfy $|u|\le C/r$ on $[0,T_*)$, by results of Koch, Nadirashvili, Seregin and Sverak
   and of Chen, Strain, Tsai and Yau, not re-checked here, and $r|u^\theta|\le G$, so $\sup_{0\le s<T_*}\|r\,u^{mer}(s)\|_\infty=\infty$;
   this may hold already at $s=0$, since the data class does not bound $\|r\,u^{mer}(0)\|_\infty$, so finite attained records
   are not established; if a finite positive record $\sup_{0\le s\le s_A}\|r\,u^{mer}(s)\|_\infty=r_AA\in(0,\infty)$ is attained at a point $x_A$ at time
   $s_A$, with $r_A=r(x_A)>0$ and $A=|u^{mer}(x_A,s_A)|>0$, the rescaling $U(y,\tau)=A^{-1}u^{mer}(x_A+r_Ay,s_A+r_A\tau/A)$ satisfies
   $|U(0,0)|=1$ and $|U(y,\tau)|\le r_A/r(x_A+r_Ay)$ for $-s_AA/r_A\le\tau\le0$ and $r(x_A+r_Ay)>0$, so it is bounded away from the rescaled axis,
   but neither the existence of such records with $s_A\uparrow T_*$ nor the divergence of the backward depth $s_AA/r_A$ is
   proved, $U$ is not shown to be bounded near the rescaled axis, its gradient $r_AA^{-1}\nabla u^{mer}$ is not shown to be
   bounded, and with amplitude $M(s_A)$ in place of $A$ the retained value $A/M(s_A)$ is not shown to stay away from $0$;
   for the two fields $f$ of the Remark after Proposition 14C, which are single-time fields and not solutions, with
   $m=\|f\|_\infty$ and the parameters $a$, $L$ of that Remark, a point $x_A$ where $r|f|$ is maximal lies, for large $L$, at
   distance $r_A=r(x_A)$ comparable to the outer radius $ae^L$, $|f(x_A)|$ is comparable to $m/L$, and
   $r_A\|\nabla f\|_\infty/|f(x_A)|$ is of order $e^L$, since $\|\nabla f\|_\infty$ is of order $m/(La)$);
   Holder regularity near the axis as possible input for the Euler-length bounds of Constantin, Ignatova and Vicol
   (Limitations 6) (fix $0<t<T_*$, put $D=D(t)>0$ and $q=u^\theta/r$, and choose $\rho>0$ with $\rho^2\le t$; smoothness at
   the axis and the gradient bound give $|q|\le D$, hence $|\Gamma|\le Dr^2$ for $\Gamma=ru^\theta$, throughout the preceding
   history; the radial lift of $\eta=\omega^\theta/r$ to $\mathbb R^4\times\mathbb R$ solves
   $(\partial_\sigma+\tilde b\cdot\nabla-\Delta_5)\eta=\partial_z(q^2)$ with $\tilde b=(u^rY/r,u^z)$ and
   $\Delta_5=\partial_r^2+3r^{-1}\partial_r+\partial_z^2$; with $a'(\sigma)=u^z(0,a(\sigma),\sigma)$, $r_y=|y'|$ and
   $\sigma_s=t+\rho^2s$, the function $h(y,s)=(\rho/D)\eta(\rho r_y,a(\sigma_s)+\rho y_5,\sigma_s)$ on $B^5_1\times[-1,0]$ solves
   $h_s+\mathcal B\cdot\nabla h-\Delta_5h=\operatorname{div}_yF$, where $\mathcal B$ is $\rho$ times the lifted velocity increment from the
   moving axis point and $F=(\rho^2/D)q^2e_5$, so that $\|\mathcal B\|_\infty+\|\operatorname{div}_y\mathcal B\|_\infty+\|F\|_\infty\le CD\rho^2$ (the
   lifted drift is not divergence free, $\operatorname{div}_y\mathcal B=2\rho^2u^r/r$), while $|h|\le2/r_y$ from $|\omega^\theta|\le2D$ is
   locally square integrable in five dimensions; for $D\rho^2\le c_0$ interior De Giorgi-Nash-Moser estimates bound $h$
   and its parabolic Holder seminorm on the half cylinder, and multiplication by $r\le\rho/2$ gives
   $\sup_{t-\rho^2/4\le\sigma\le t}\rho^\alpha[\omega^\theta(\cdot,\sigma)]_{C^\alpha(B_{\rho/2}((0,0,a(\sigma))))}\le CD$ with $0<\alpha<1$
   and $C$ independent of $t$, $\rho$ and the axis point; this argument gives uniform normalized control only at lengths
   $\rho\lesssim D^{-1/2}$, which at the scalar rates of Remark (ii) after Proposition 14B, with $\tau=T_*-t$ and
   $L=\log(e/\tau)$, is $D^{-1/2}=\tau^{3/4}L=o(\sqrt\tau)$, whereas the Euler length $\ell(t)$ of that criterion satisfies
   $\sqrt\tau=o(\ell(t))$ by definition and, if its velocity bound holds on the whole space, $\ell(t)\ge c\tau\|u(t)\|_\infty$,
   hence $\ell(t)\ge c\tau^{1/4}$ at global velocity records at those rates; these comparisons concern scalar rates, not a
   constructed solution, and the argument does not establish the hypotheses of that criterion at its Euler length;
   worked out with a second-model research answer and checked by hand, in the form requested by a second-model audit);
   spatial power bounds $|u|\le Cr^{-\alpha}$, $|\omega^\theta|\le Cr^{-\gamma}$ with $\alpha>1$, $\gamma>2$ used as single-time bounds (Proposition 25(d)), and
   qualitative off-axis regularity (certified windows approach the axis, Corollary 26).
3. In alternative (B) the selection is an existence statement for a scale; Theorem 5' gives an explicit sufficient
   rule defined from an observable, and whether (B) implies (L2LS) is open. The same holds in (B*): Corollary 18
   replaces the retrospective end-time shift of Theorem 12 and the anchor by rules computed from the trajectory, but it
   starts from a (B*) normalization that is itself only shown to exist. So the exclusion of (C), or of (C*), would give
   the analytic requirements of GOAL for an existentially selected normalization; a selection rule from records for
   every trajectory needs in addition a criterion such as (L2LS), or (EC) for the outputs of a prescribed rule producing (OSC$_0$) normalizations
   (the Remark at the end of Section 6 states what is known about rules in (B)). The regime split is an asymptotic predicate of the trajectory.
   Normalization classes other than those of Sections 5 to 9 (componentwise amplitudes,
   non-ball windows) are not exhausted.
4. Off-axis singular points are excluded by the Caffarelli-Kohn-Nirenberg partial regularity theorem together with
   axisymmetry. This qualitative fact is discussed above (Corollary 26 and Limitations 2), but no proof here depends on
   it; the epsilon-regularity criterion of the same theory enters only through the input granted in Proposition 14B(a).
5. The results are proved for the Sobolev class $u_0\in\bigcap_kH^k$; Lemma 9 needs the extra integrability stated.
6. Possible routes not yet completed: a local, scale-critical bound on the vorticity produced by the swirl source
   $\partial_z(q^2)$ of $\eta$ (after rescaling, $q_n^2\to0$ in $L^1_{loc}$ and the source tends to $0$ in $W^{-1,1}_{loc}$ and
   uniformly away from every fixed normalized tube around the axis, Lemma 19; $(G/D)^{1/2}=o(M/D)$ is the crossover radius
   of the pointwise envelope of $q$, and no concentration of the absolute source within a multiple of that radius is
   proved), whose accumulated effect over the history is not controlled; concentration-cancellation methods for
   swirl-free axisymmetric flows (the published strong-compactness theorems for vanishing-viscosity limits without
   swirl, e.g. Jiu, Wu and Yang (Math. Methods Appl. Sci., DOI 10.1002/mma.3087), Nobili and Seis (Math. Ann. 382
   (2022)) and Chae and Imanuvilov (EJDE 1998, no. 26), assume uniform integrability of the relative vorticity
   $\omega^\theta/r$ in $L^1\cap L^p$, $p>1$, or $L\log^\alpha L$, for which the required uniform bounds have not been
   established here; Corollary 6A(c) rules out uniform local $L^1$ control of the normalized relative vorticity on its
   retained-oscillation witness windows in (C) when the normalized axis distance is bounded, and does not establish this
   obstruction for axis-escaping windows or for time-integrated bounds);
   time-integrated or Lagrangian arguments using that the rescaled limit must be an Euler-Reynolds solution with a
   nonnegative defect; and the heat depth of the history: on every admissible normalization with retained $L^2$ oscillation
   (L2-OSC) the normalized heat time of the history, $\nu_ns_nM_n/\ell_n=s_n/\ell_n^2$, tends to infinity, since retained
   oscillation gives $\ell_n^3\le CE_0/M_n^2$ and $s_n\to T_*>0$ (without (L2-OSC) this fails: $\ell_n=1$ is admissible in
   regime (II) and has heat depth $s_n$); a whole-space solution of the heat equation bounded by $1$ over heat time $T$ has
   gradient at most $CT^{-1/2}$ at its end, so the exact Navier-Stokes shear and pipe comparisons of this report that reduce to
   heat flow can fail (L2M) only along subsequences whose heat age at the failing times tends to zero (they model recently
   created structure, which a changing datum can supply); heuristically, on a fixed trajectory the fine structure of a window in (C) at relative
   scale $\delta$ must be produced or maintained by the nonlinear terms against diffusion, which alone would damp it within about
   $\delta^2M_n\ell_n$ Euler times. Two quantitative forms of this, the stationary example below and the heat-depth
   bound for the avoidance interval of Lemma 26A were checked by hand and then audited (the audit added the
   specification of the cutoff in (i) and corrected the alternative in (ii)); none of them gives a contradiction or
   excludes (C). (i) If a failing increment of (L2M) has physical shift $\rho_n=\alpha_n\ell_n$ with $\alpha_n\to0$,
   then with $H_a=I-\chi(aD_x)$, $D_x=-i\nabla$, where $\chi\in C_c^\infty(\mathbb R^3;\mathbb R)$ is even,
   $0\le\chi\le1$, $\chi=1$ on $B_1$ and $\chi=0$ outside $B_2$, and $a_n=L\rho_n$ for a large fixed $L$, one has
   $\|H_{a_n}u\|_2^2\ge cM_n^2\ell_n^3$ at the failing time; the identity
   $\frac12\frac d{dt}\|H_au\|_2^2+\|\nabla H_au\|_2^2=-\int H_a^2u\cdot(u\cdot\nabla u)\,dx$, the bound
   $M_na\|\nabla u\|_2^2$ for its right side and $\|\nabla H_au\|_2\ge a^{-1}\|H_au\|_2$ then force, during the
   preceding physical time $K\ell_n^2+O(\ell_n^2\log M_n)\to0$, a dissipation
   $\int\|\nabla u\|_2^2\,dt\ge cM_n\ell_n^2/\alpha_n$; but (UP) gives $\rho_nD_n/M_n\to\infty$, so this charge is
   $o(D_n\ell_n^3)$ and tends to zero, and energy gives no rate contradicting it. (ii) Let $P$ be a meridional
   rectangle of side at most $2R\ell_n$ in $\{r\ge h\ell_n\}$ and
   $N_n=(M_n\ell_n)^{-1}\int\!\!\int_P|\omega^\theta|\,dr\,dz$ at a time $b_n=s_n+\tau_n\ell_n/M_n$, with
   $-A\le\tau_n\le0$ for a fixed $A$, of the retained-oscillation normalization. If this normalized mass stays at
   least $N_n/2$ during the preceding physical time $K\ell_n^2$, the pointwise bound
   $|\nabla u|^2\ge\frac12|\omega^\theta|^2$ and Cauchy-Schwarz on $P$ give
   $\int\|\nabla u\|_2^2\,dt\ge\frac{\pi h}{16R^2}KM_n^2\ell_n^3N_n^2$ over that time; since $b_n\to T_*$ and
   $K\ell_n^2\to0$, the dissipation over that time tends to zero, so along any sequence on which this persistence
   holds, $KM_n^2\ell_n^3N_n^2\to0$. If instead the displayed dissipation lower bound fails, persistence fails at some
   time of the interval. Writing $\mathfrak Z_n$ for the physical dissipation on the interval and $E_n=M_n^2\ell_n^3$,
   the accumulated normalized absolute swirl source then satisfies
   $S_n\le\frac{4RG}{\sqrt{2\pi}h^{5/2}}\sqrt{K\mathfrak Z_n/E_n}<\frac{GKN_n}{\sqrt2h^2}$, by Cauchy-Schwarz and the
   bound of Lemma 19 on the swirl source, and for fixed $0<K\le h^2/(2\sqrt2G)$ Kato's inequality for the conservative
   equation of $\omega^\theta$ in the meridional plane forces an integrated positive inward boundary flux, by
   transport or diffusion, greater than $N_n/4$ in these units during the interval. Its physical length $K\ell_n^2$ is
   $KM_n\ell_n\to\infty$ Euler times, and no upper bound on this influx is proved. A local inequality bounding the Kato cancellation
   of interleaved signed masses below by $c\nu\min\{N^+,N^-\}^3$ per unit Euler time fails, whatever the elapsed heat depth of the observation interval, for the exact
   stationary Navier-Stokes flows $(0,f_k(x,z),\frac12)$ on the half-space $z>0$ with $p=0$,
   $f_k=\frac a8[9e^{\lambda_1z}\cos kx-e^{\lambda_3z}\cos3kx]$, $a=\frac14$, $\nu=k^{-4}$, where $\lambda_j<0$ solves
   $\nu\lambda^2-\frac12\lambda-\nu j^2k^2=0$: the vorticity component $\partial_xf_k$ has sign changes at $x\in\pi\mathbb Z/k$, masses of order
   $k$ on $(0,2\pi)\times(1,2)$, circulations bounded by $\frac{5a}4$ times the perimeter, and gradient $O(\nu k^4)$ at its zero
   lines, so the ratio of cancellation to the cubic quantity is $O(k^{-2})$; the layers are renewed by inflow, and the flow is
   neither axisymmetric nor defined on the whole space, so this excludes only a local scalar closure (particles reach $1<z<2$ from the inflow boundary within a few Euler times, so it does not test an estimate requiring old incoming material). The avoidance
   interval of Lemma 26A has heat depth $\nu_nA_n\le C\nu_n^{7/8}\to0$, so it does not certify thermal age. What is missing
   is a bound on the high-frequency transfer in (i), or on the influx in (ii), that is small compared with the displayed
   charges. The Euler-scaling Type II scenarios of Seregin (arXiv 2402.13229 v3, 2507.08733 v2,
   2606.29468 v1) extract ancient Euler limits under scale-wise energy bounds with an exponent $m<1$ (or a slowly
   varying function in place of a power) and a concentration hypothesis; these are additional rate hypotheses (for $m=1$
   they are scale-invariant Type I bounds), not consequences of finite energy and bounded circulation, and the amplitude
   is a prescribed power of the length rather than $M$. Under those energy bounds the parabolic concentration condition
   $r^{-2m_0}\int_{Q_r}|v|^3\ge c_1$, $m_0=2m/(3-m)$, is impossible (after the rescaling it equals the $L^3$ norm of the rescaled
   field over a cylinder of radius tending to $0$, which the uniform $L^{10/3}$ bound makes small), and under the physical
   bound on $\partial_tv$ assumed in the axisymmetric Liouville statements the rescaled time derivative tends to $0$, so every
   extracted limit is stationary and the all-scale bounds make it zero (both calculations were checked by hand under the
   hypotheses as printed in the parts of the preprints listed in Verification; they are given here only in outline). The partial
   Type I theorem of Q. S. Zhang (arXiv 2604.07785, Theorem 1.1: an axisymmetric Leray-Hopf solution with bounded
   initial circulation and $u^r\ge-c/\sqrt{T-t}$ stays regular through $T$) gives at a singular time only
   $\limsup_{t\uparrow T_*}\sqrt{T_*-t}\,\|(u^r)_-(t)\|_\infty=\infty$. With $h=T_*-t$, the functions $M=h^{-1}$, $D=h^{-9/5}$,
   $\|(u^r)_-\|_\infty=h^{-3/5}$ satisfy $M^5\le CE_0D^3$, $M'\le24MD$, $D/M^2\to0$ and this conclusion while
   $\|(u^r)_-\|_\infty/M\to0$ (exponent bookkeeping, not a solution). A radial velocity of size $cM$ within $KM/D$ of the axis
   would contradict (C) (Section 9D, Remark after Corollary 26); Zhang's theorem does not supply one. The September
   2026 revision of a preprint of Shahmurov (arXiv 2604.21213 v3, 3 September 2026; only the abstract was read here)
   announces, for smooth axisymmetric flows with swirl, an exact $L^p$ balance for $r^du^\theta$, $-1\le d<1$, with a
   signed radial-compression action, continuation under finite $L^p$ mass and bounded signed action for $p\ge3/(1-d)$,
   the needed mass on the critical diagonal $d=1-3/p$ for every finite $p\ge2$ from $H^1$ data and bounded
   circulation, and a sliding Petrovskii displacement criterion with endpoint coefficient $2$ and an iterated-log
   correction. The precise statements, in particular the form of the sliding-interval inequality, have not been
   verified against the text, and the second-model consultation that had reported them withdrew its claim to have read
   the text. For $p=3$ the following calculation is independent of that attribution: with $Z=\|u^\theta\|_3^3>0$ and
   $\chi_{0,3}=Z^{-1}\int(u^r/r)|u^\theta|^3\,dx$, multiplying the swirl equation by $3u^\theta|u^\theta|$ gives
   $Z'+\frac83\|\nabla|u^\theta|^{3/2}\|_2^2+3\int|u^\theta|^3r^{-2}\,dx=-3\chi_{0,3}Z$, so an upper bound on the
   signed action $A(t)=-\int_{t_0}^t\chi_{0,3}\,ds$ bounds $|u^\theta|^{3/2}$ in
   $L^\infty_tL^2_x\cap L^2_t\dot H^1_x$, hence $u^\theta$ in $L^4_tL^6_x$, and the criterion of Chen, Fang and Zhang
   (Discrete Contin. Dyn. Syst. 37 (2017), Theorem 1.1: $r^du^\theta\in L^a_tL^b_x$ with $0\le d<1$,
   $\frac2a+\frac3b\le1-d$, $b>\frac3{1-d}$, $a\ge\frac2{1-d}$; in the form reported by the consultation, not checked
   against the source) then gives continuation. Thus, conditional on that criterion,
   $\limsup_{t\uparrow T_*}A(t)=+\infty$ at a first singular time (if $Z$ vanishes at some earlier time the solution
   has no swirl afterwards and stays regular). This does not locate the compression in the windows of (C) or give a
   radial velocity comparable with $M$, so it does not exclude (C), and the unverified sliding criterion supplies no
   established further conclusion here. The other recent items are literature leads reported by the consultation, not
   checked against the sources, and their applicability has not been established; the following remarks only explain
   why none of them is expected to apply directly. A stationary Liouville theorem, such as those attributed to Wang
   and Yang (arXiv 2608.06040), cannot be invoked without proving stationarity and its spatial hypotheses for the
   limits here. Nonzero purely azimuthal axisymmetric vorticity on a complete azimuthal orbit cannot satisfy
   $|\omega\cdot e|\ge c|\omega|$ for a fixed unit vector $e$ and $c>0$, since $e_\theta\cdot e$ vanishes somewhere on
   the orbit; this does not exclude a cone condition restricted to a small off-axis window, and the exact geometric
   hypothesis of Lei, Ren and Tian (arXiv 2501.08976) is unverified here. The quantitative weak $L^3$ bounds of
   Ozanski and Palasek (Ann. PDE 9 (2023)) need a bound that energy and $M$ give only as
   $\|u\|_{L^{3,\infty}}\le CE_0^{1/3}M^{1/3}$. The abstract of Bae, Chen and Kim (arXiv 2610.06385, 5 October 2026,
   abstract read here) states global energy compactness in $C_tL^2_x$ of regular approximate swirl-free axisymmetric
   Euler flows with relative vorticity in $L^1\cap L^p$ ($p\ge4/3$, and below $4/3$ under control of the absolute
   impulse); its exact hypotheses are unverified. Corollary 6A excludes bounds on
   $\eta_n=(\ell_n^2/M_n)\,\omega^\theta/r$ that are uniform in $n$ in $L^\infty_\tau(L^1_{loc}\cap L^p_{loc})$,
   $p\ge1$, on its witness windows at bounded normalized distance from the axis, since the normalized $L^1$ norm of
   $\eta_n$ over the solid of revolution of its rectangle is $2\pi(N_n^++N_n^-)\to\infty$; it does not exclude
   membership of each $\eta_n$, membership of a weak limit, time-integrated bounds, or bounds on windows whose
   normalized distance from the axis tends to infinity. The abstract of a preprint of Constantin, Ignatova and Vicol
   (arXiv 2609.20762 v2, 29 September 2026; only the abstract was read here) states local regularity for axisymmetric
   suitable weak solutions, smooth before the terminal time $0$, with $|u(\cdot,t)|\le C\ell(t)/(-t)$ and
   $|\nabla^2u(\cdot,t)|\le C/((-t)\ell(t))$ for an Euler length $\ell$ (non-increasing, doubling, $\ell(t)\to0$ and
   $(-t)/\ell(t)^2\to0$), the Hessian bound being replaceable by a Holder bound on the azimuthal vorticity and a bound
   on its potential vorticity. These are a priori pointwise bounds at a prescribed scale, which the problem does not
   allow one to assume. If they held on the whole space with $M$ comparable
   with $\ell(t)/(-t)$, interpolation would give $D\le C/(-t)$ and hence $D/M^2\le C(-t)/\ell(t)^2\to0$, so that class
   lies in regime (II). Neither of these bounds at a prescribed Euler length is derived here from fixed data, from
   $D/M^2\to0$ or from (FLAT$_0$).
   Two further necessary conditions on the meridional mass were derived by hand and audited once (the audit found two
   defects, repaired below: the weighted identity had been stated for all $0<k<4$, and the compatibility of the two
   bounds in (i) had been given a wrong reason). Put
   $Q(t)=\int\!\!\int|\omega^\theta|\,dr\,dz=(2\pi)^{-1}\|\eta(t)\|_{L^1}$, which is invariant under the Navier-Stokes
   scaling, and $S_Q=(2\pi)^{-1}\|\partial_z(q^2)\|_{L^1}$. The proof of Lemma 9 gives
   $Q(t_2)\le Q(t_1)+\int_{t_1}^{t_2}S_Q$ for $t_1\le t_2<T_*$ whenever $Q(t_1)<\infty$ ($Q(0)<\infty$ is an
   assumption on the datum, not implied by $u_0\in\bigcap_kH^k$), and at the witness times $t'_n$ of Corollary 6A(c),
   at any axis distance, $Q(t'_n)\ge N_nM_n\ell_n$ with $N_n=(N^+_{n,R}+N^-_{n,R})(t'_n)\to\infty$. (i) For
   $\Gamma=ru^\theta$ and $2\le k<4$ (for $0<k<2$ the same identity holds under additional weighted integrability at
   infinity, which finite energy does not give),
   $\frac d{dt}\int\Gamma^2r^{-k}=-2\int|\nabla\Gamma|^2r^{-k}+k(k-2)\int\Gamma^2r^{-k-2}-k\int\Gamma^2u^rr^{-k-1}$;
   with the radial Hardy inequality $\int\Gamma^2r^{-5}\le\frac49\int(\partial_r\Gamma)^2r^{-3}$ the case $k=3$ gives
   $\frac d{dt}\int\Gamma^2r^{-3}+\frac23\int|\nabla\Gamma|^2r^{-3}\le3\int(u^\theta)^2(u^r)_-r^{-2}$, and
   Cauchy-Schwarz with the same Hardy inequality gives $S_Q\le(3\pi)^{-1}\int|\nabla\Gamma|^2r^{-3}$. Hence, if
   $Q(0)<\infty$ ($\int(u_0^\theta)^2r^{-1}<\infty$ holds for the data considered), in (C) the compression action
   $\int_0^{t'_n}\!\int(u^\theta)^2(u^r)_-r^{-2}$ is at least $\frac{2\pi}3N_nM_n\ell_n-C(u_0)$,
   $C(u_0)=\frac13\int(u_0^\theta)^2r^{-1}+\frac{2\pi}3Q(0)$. It is also at most $M(t'_n)E_0/2$, since
   $\int(u^\theta)^2r^{-2}\le\|\nabla u\|_2^2$. The two bounds are compatible:
   $N_nM_n\ell_n\le\int\!\!\int_{P_{n,R}}|\omega^\theta(t'_n)|\,dr\,dz\le4\sqrt2R^2D(t'_n)\ell_n^2$, so the ratio of
   the lower bound to the upper one is at most $C_R(D(t'_n)/M(t'_n)^2)M_n\ell_n^2/E_0\to0$, by regime (II) and
   $M_n^2\ell_n^3\le CE_0$. (ii) If $\|\omega_0^\theta\|_1<\infty$, Lemma 9' and
   $\|\eta\|_1\le(\int|\omega^\theta|r^{-2})^{1/2}\|\omega^\theta\|_1^{1/2}$ give
   $\int_0^{T_*}Q^2\,dt\le K^2/(4\pi^2)$ with $K=\|\omega_0^\theta\|_1+E_0/2$ (so $Q<\infty$ for almost every time);
   hence at every time $t$ with $0<Q(t)<\infty$ and $\Delta(t)=2K^2/(\pi^2Q(t)^2)\le t$ one has
   $\int_{t-\Delta(t)}^tS_Q>Q(t)/2$: the accumulated absolute swirl source over the preceding physical time
   $\Delta(t)$ exceeds half the current meridional mass (this does not locate the source or identify which of it
   survives). At the witness times of (C) this time is at most $2K^2/(\pi^2N_n^2M_n^2\ell_n^2)$, which may still
   contain many Euler times of the window since $M_n\ell_n^3\le CE_0/M_n$; the production may take place anywhere
   along the axis. The envelopes $|\partial_z\Gamma|\le Dr$ and $|\Gamma|\le\min\{G,Dr^2\}$ give only
   $\int_0^\infty|\partial_z(q^2)|\,r\,dr\le4G^{1/2}D^{3/2}$ at each height, a bound per unit axial length of the
   swirling core whose axial extent is not controlled, and the global bounds of $S_Q$ by
   $\pi^{-1}\|\nabla u\|_2\|\nabla\omega\|_2$ or by the weighted dissipation above are not controlled at a single
   time. (iii) Two second-model consultations, whose derivations were checked by hand, add the following. The equation
   $\partial_tq+b\cdot\nabla q=(\Delta+2r^{-1}\partial_r)q-2(u^r/r)q$, tested against $q$ with a time cutoff, gives
   $\int_{t-d}^tS_Q\le\pi^{-1}e(t,d)\,(\frac1{2d}+2D(t))^{1/2}$ for $2d\le t$, where $e(t,d)=\int_{t-2d}^t\|q\|_2^2$;
   under the additional hypothesis $\|\omega^\theta_0\|_1<\infty$ of (ii), combining this estimate with (ii) and
   $\int_0^{T_*}\|q\|_2^2\le E_0/2$ gives $Q(t_k)/D(t_k)^{1/2}\to0$ along every sequence $t_k\to T_*$
   with $Q(t_k)\to\infty$. This does not conflict with the witness bound of (C), since by (i)
   $N_nM_n\ell_n\le4\sqrt2R^2D(t'_n)\ell_n^2\le C_RD(t'_n)(E_0/M_n^2)^{2/3}=o(D(t'_n)^{1/2})$, where
   $C_R$ depends also on the fixed (L2-OSC) constant, using $D(t'_n)\le D(t_n)\le M_n^2$ for large $n$. Energy bounds the
   axial length of strong swirl, $|\{z:\sup_r|u^\theta(r,z,t)|\ge\kappa(GD(t))^{1/2}\}|\le64E_0/(\pi\kappa^4G^2)$ for
   $0<\kappa\le1$ (at such a height $|u^\theta|\ge v_0/2$ on a radial interval of length $v_0/D$ in $r\ge v_0/(2D)$,
   $v_0\ge\kappa(GD)^{1/2}/2$), but not that of weak swirl, and a smooth swirling field supported in $r\le2a$,
   $|z|\le2a^{-2}$ with bounded Lipschitz constant and enstrophy, circulation $O(a^2)$, energy $O(a^2)$ and no
   meridional vorticity has $S_Q\ge c/a$, so $S_Q$ is not bounded at one time by these quantities. Since
   $|\omega^\theta|\le\sqrt2D$, the part of the witness rectangle $P_{n,R}$ with $r\le cN_nM_n/D(t'_n)$ carries at
   most half of its mass for a small $c=c(R)>0$, so the cancelling mass lies beyond the Lipschitz length by an
   unbounded factor, and the region $r\le C(G/D)^{1/2}$ carries $o(M_n\ell_n)$ of it. The envelope rate
   $4G^{1/2}D^{3/2}$ per unit axial length is attained up to a constant factor by smooth profiles at radius
   $(G/D)^{1/2}$, and at this rate an axial length $O(\ell_n)$ would supply an absolute source budget equal to the
   witness mass in a time much shorter than $\ell_n^2$, while the deadline of (ii) computed from the witness mass
   alone is much longer than $\ell_n^2$. Scalar bookkeeping (exponents only, not a field) is consistent with all the
   inequalities in (i)-(iii), with the energy, enstrophy and Lemma 9' budgets and with regime (II), while $Q\to\infty$
   and $Q/(M\ell)\to\infty$. None of these conditions excludes (C); what is missing is control of the export and
   survival of the produced signed vorticity. (iv) A third second-model consultation, whose derivations were checked
   by hand, gives a necessary condition for regime (II) itself. Split $\eta=\eta^d+\eta^s$ with the same drift,
   $\eta^d(0)=\eta_0$, $\eta^s(0)=0$, and $\eta^s$ forced by $\partial_z(q^2)$. Testing with $\eta^s$ and integrating the
   source by parts in $z$ gives $\|\eta^s(t)\|_2^2\le\int_0^t\|q(s)\|_4^4ds\le\int_0^tD(s)^2\|q(s)\|_2^2ds=o(D(t)^2)$ (norms in $L^p(dx)$; there is no
   positive axis boundary term, and the little-o follows from $\int_0^{T_*}\|q\|_2^2\le E_0/2$ and $D(t)\to\infty$). The
   meridional velocity $b$ satisfies $b=e^{\rho^2\Delta}b+k_\rho*\times(\omega^\theta e_\theta)$ with
   $k_\rho=\int_0^{\rho^2}\nabla g_s\,ds$, $g_s$ the heat kernel, $|k_\rho(z)|\le C|z|^{-2}e^{-c|z|^2/\rho^2}$; splitting
   $\omega^\theta=r\eta^d+r\eta^s$ only on $|x-y|\ge a$, using $|\omega^\theta|\le\sqrt2D$ for the total vorticity on $|x-y|<a$,
   $\|\eta^d\|_\infty\le\|\eta_0\|_\infty$, $r(y)\le r(x)+|x-y|$ and Cauchy-Schwarz, and choosing $a=(r(x)\|\eta^s\|_2/D)^{2/3}$,
   one gets
   $|b(x)|\le C[E_0^{1/2}\rho^{-3/2}+\|\eta_0\|_\infty(r(x)\rho+\rho^2)+D^{1/3}(r(x)\|\eta^s\|_2)^{2/3}+\|\eta^s\|_2\rho^{1/2}]$.
   At a velocity record $|u(x_n,t_n)|=M_n$ one has $|b(x_n)|\ge M_n-S(t_n)$ and, from the energy of a solid torus around
   the axis, $r(x_n)\le CE_0D_n^2M_n^{-4}$; with $\rho=LE_0^{1/3}M_n^{-2/3}$ this gives, at all large velocity records in
   regime (II), $\|\eta^s(t_n)\|_2^2\ge cE_0^{-2}M_n^{11}D_n^{-5}$ (and $\ge cE_0^{-1/3}M_n^{8/3}$ for a record on the axis). The two
   bounds are compatible with the upper bound $o(D^2)$, since $M^{11}D^{-7}\le CE_0^{7/3}M^{-2/3}$ by the energy-ball
   inequality; for $M=h^{-3/5}$, $D=h^{-11/10}$ the general lower scale is $h^{-11/10}$, the axis scale $h^{-8/5}$ and
   $D^2=h^{-11/5}$ (scalar bookkeeping, not a field). A rate
   $\int_0^{t_n}\|q\|_4^4=o(E_0^{-2}M_n^{11}D_n^{-5})$ along the velocity records would exclude regime (II); it is not available.
7. Context from the literature (as reported by the second-model literature check; not re-read): the classical
   parabolic blow-up rescaling of Koch, Nadirashvili, Seregin and Sverak gives a bounded nonzero ancient mild solution
   that may be constant, and in regime (II) it is constant since its gradient is at most $D/M^2$; a structure theorem
   of Lei and Zhang (Pacific J. Math. 254 (2011)), under the stronger hypothesis $\|ru_0\|_\infty<\infty$, says that the
   parabolic rescaling at an almost historical maximum $Q_0$ of $|u|$, attained at distance $r_0$ from the axis, with
   $r_0Q_0$ large is close to a nonzero constant (their $Q_0$ is a velocity, not the meridional mass $Q$ of
   Limitations 6). Where the
   published numerical and computer-assisted singularity scenarios (Hou and Huang; Hou; Luo and Hou; Chen and Hou;
   Elgindi; Elgindi, Ghoul and Masmoudi, all for Euler, with a boundary, or non-rigorous) allow a ratio $D/M^2$ to be
   read off, it does not tend to zero, i.e. they would fall in regime (I), where Theorem 2 applies to Navier-Stokes.
   No scenario in regime (II) is known to us beyond dimensional ones.

## Verification

Proofs. Every numbered statement in the Findings is accompanied by a proof in this report, conditional on an
explicitly granted input where the statement says so (Proposition 14B). Some proofs refer to
standard arguments (Arzela-Ascoli, Riesz-Frechet-Kolmogorov, Hardy space and BMO duality, Calderon-Zygmund estimates)
or reuse steps of an earlier proof instead of repeating them (the symmetry and pressure identifications in Theorems 2,
4(a) and 6', and the steps reused in Theorem 17(d) and Proposition 20(b)). Several proofs are abbreviated, among them the localized div-curl and kernel translation
estimate in Section 8, the passage from the pressure tail to time equicontinuity in Proposition 15 and the dyadic
weighted pressure estimates of Lemma 16; this list is not exhaustive. Passages labelled heuristic, dimensional or
exponent bookkeeping are not proofs and are not used as such. The proofs were written and checked by hand; no proof
assistant was used. The constant $24$ of Lemma 3 and the exponent bookkeeping of the dimensional scenario in
Limitations 1' were also checked by symbolic computation; the other exponent bookkeeping (after Proposition 24 and in
Limitations 6) and the constants of Proposition 10 were checked by the author by hand (the audits of Limitations 6(iii)
and 6(iv) additionally report exact rational arithmetic). The profile of Proposition 10 was in
addition evaluated numerically on a grid for $3\le N\le8$; this gives consistency checks on sampled amplitudes,
finite-difference derivative estimates, increments and window variances, and does not prove the statements for these $N$ or verify the
constants of the proof.

Independent audits. A second model (GPT-6 "astra", run through Codex) acted as a hostile referee on frozen copies of
parts of the report and as a research consultant. Its output was treated as a list of claims: every reported defect and
proof was checked by hand before it was used, and no result of this report rests on its assertion alone; literature
statements reported by it have the verification status stated below (checked against the original texts only where so
stated, otherwise reported as context or used conditionally). The criterion of Proposition 15, the
relative-energy argument of Proposition 16, Lemma 26A with its application, the Remark on the accumulated swirl source
after Lemma 9' and parts of the Remark at the end of Section 6 were proposed in these consultations; the proof of Proposition 10' was developed in a consultation from an embedding
proposed by the author of this report. Each of these was then checked by hand line by line. The audited parts were Sections 1 to 5; Sections 6 to 10; Theorem 5', Proposition 7(c), the pressure Hessian
bound, Lemma 9' and Section 9; Lemma 11, Theorem 12, Corollary 13 and Proposition 14; Theorem 6' and Proposition 15;
Lemma 15', Lemma 16, Proposition 16 and Section 9A; Sections 9B, 9C and 9D separately; the whole report, four times as listed here (two later whole-report audits are
described below)
(internal consistency, the selection requirement, forbidden assumptions, presentation; the second time with spot checks
of Lemma 26A, Corollary 6A, Lemma 21 and Proposition 22, the third with spot checks of Theorem 6, Proposition 24 and
Theorem 17(d), the fourth with spot checks of Lemma 11, Theorem 12, Corollary 13, Proposition 14(a) to (e), Proposition
7(c), Lemma 26A and Proposition 14A including the paragraph after its proof, and found no failing step in these proofs); and, five times, the repairs made after the preceding audit (the third of these also covered the
written-out proof of Proposition 16(c); the fourth re-audited the repairs made after the second whole-report audit; the
fifth also covered the Remark on the accumulated swirl source after Lemma 9' and four items of Limitations 2); and Proposition 10' together with the passages of the Result, the
Limitations and this section that describe it. The defects found were of these kinds, and the text was revised in response to each: implications stated as equivalences (failure of (L2M) versus a nonzero
Reynolds defect; several "if and only if" statements in Section 9); missing quantifiers or hypotheses (the time
modulus in Theorem 4(a), joint subsequences in Corollary 13, index ranges and subsequence scopes in Sections 9A to 9D,
the hypotheses of Propositions 15 and 16(a) in the Result); constants computed from the whole sequence instead of each
record (Theorem 17(d)); an invalid step in an auxiliary example after Lemma 15' (replaced by a second-difference
argument); a wrong zero-limit statement for large-amplitude Galilean rescalings (the limit is a constant); incomplete
displayed proofs (Proposition 8, Theorem 5(b), Proposition 10(v)); a criterion stated as a selection rule although it
is a condition on a given normalization (Proposition 22); an unrestricted index range (Proposition 10(v), now $j\ge0$); a dilation statement without its amplitude factor
(Proposition 10'(vi')); a conclusion stated more strongly than proved (that an exclusion of (C) must use the
evolution); a misreported numerical tolerance (Section 10); a hypothesis of Lemma 21 omitted in the Result, and later its collar width; a transfer of Lemma 26A to
rectangles meeting the axis (now restricted to exterior rectangles); the scope of the temporal
certificate and the description of (B*) overstated in the Result; the degenerate cases $\sigma=0$, $G=0$ of Lemma 26A; a localization of the swirl source in the swirl core
not implied by Lemma 19; two constructions described as exact solutions without the needed stability and record-growth
arguments; undefined operators in a displayed identity; and statements of GOAL for normalizations whose selection is retrospective
(Theorem 12) or existential (alternatives (B), (B*)), now qualified as such; in the fourth whole-report audit, a
functional (non Navier-Stokes) example used to assert a non-equivalence for the trajectory class (Section 6, Remark (i),
now restricted), a blanket claim that the rescaled sequences lack the vorticity integrability assumed in the no-swirl
compactness literature (Limitations 6, now restricted to what Corollary 6A(c) proves), and missing scope qualifiers in
Result 6, the rigidity remark after Theorem 12, Theorem 5(a) and Limitations 6(iii). These repairs were made after
the fourth whole-report audit; the later whole-report audits and their stated coverage are described below, and they
did not individually recheck every earlier repair. No audit found a use of a forbidden
assumption (the shape inequality $MH\le CD^2$, Type I bounds, $H^2$ compactness, a bounded stream potential, BMO
smallness, self-similarity, affine background subtraction, time-dependent Galilean frames, ancient finite energy, a free
pressure gradient).

Literature. Re-read in the original texts for this report: arXiv 2402.13229 (pages 1 to 4), 2507.08733 (Theorems 2.1
and 3.1, and the step of the proof of Theorem 2.1 where the threshold is used), 2606.29468 (Theorem 3.1) and 2604.07785
(Theorem 1.1). Cited as reported by the second model's literature checks, without re-reading: the
Koch-Nadirashvili-Seregin-Sverak statements used (Liouville Theorems 5.1 and 5.2, Remark 6.1, Proposition 4.1); the
no-swirl compactness theorems of Limitations 6; the theorem of Lei and Zhang and the numerical and computer-assisted
scenarios of Limitations 7; the regularity criteria compared with the dimensional scenario of Limitations 1'; and the
remaining statements of the four preprints above (Theorem 5.1 of 2507.08733, the Liouville propositions, the boundary
Holder estimate used by Zhang). Of the preprint of Constantin, Ignatova and Vicol only the abstract (v2) was read here.
The October 2026 literature additions in Limitations 6 (Shahmurov, Chen-Fang-Zhang, Wang-Yang, Lei-Ren-Tian,
Ozanski-Palasek, Bae-Chen-Kim) require primary-source verification. The second-model literature consultation that
reported them states in its final form that it retrieved no original paper or abstract and withdraws its earlier
claims of verification, and the auditor of that passage could not retrieve the sources either. Here the abstracts
of arXiv 2604.21213 v3 and 2610.06385 were read (twice, the second time to check the wording of Limitations 6
against them); the $p=3$ identity, the signed integrating-factor argument, the interpolation and the weak-$L^3$
estimate were checked by hand and then audited, and continuation uses the Chen-Fang-Zhang criterion conditionally
on its hypotheses as reported.
Standard facts (the Leray-Hopf energy inequality, the circulation maximum principle, the Beale-Kato-Majda criterion, the
Caffarelli-Kohn-Nirenberg theorem, global regularity without swirl) are used as known.

Further checks and remaining verification limits. That the Gaussian lacunary profile of
Section 10 satisfies the single-time form of (FLAT) uniformly over all windows is not proved. The proof of Proposition 10' (the
three-dimensional transfer) was developed by the second model from an embedding proposed by the author, checked by hand
and then audited; the repairs made in
response to that audit (the normalized form of (vi'), the case $K>N$ in the scalar lemma, the wording of the closing
paragraph of Section 10 and two numerical descriptions) were audited again together with Corollary 6A, and the only
defect found (the description of the decay rate in (ii)) was corrected. Lemma 26A and its application were checked by hand and spot-checked
in the second whole-report audit, which found no mathematical defect beyond the degenerate cases now treated; the
re-audit of those repairs confirmed the degenerate cases and led to the restriction of the summary in the Result to
exterior rectangles. The Remark on the accumulated swirl source after Lemma 9' and the four items of Limitations 2 on viscous
cancellation, concentration-cancellation with record freezing, the near-axis cancellation functional and selection by
production events were checked by hand and then audited; the audit confirmed every formula and power and found three
defects of wording (the time localization of the source bound in the Result, a stale description of the $L^{3/2}$
contraction, and the reference in this sentence) and one missing specification (the flat-extremum profile of the pipe
flow example), all repaired. The two proposals in the Limitations 2 item on finite-energy closure of pipes and an
energy charge for record increases arose in a consultation; the divergence identity and the residual were checked by hand,
while the sign of the pressure force depends on the packet geometry and the dissipation scaling is a fixed-profile
calculation; neither supplies the missing exact-solution or record-growth argument. An audit found two omissions in an earlier wording
(the decay hypotheses on $f_0$ and $\chi$, without which $V_L$ can have infinite energy, and the diagonal choice of the
cutoff length), and the third whole-report audit found that the stability, parameter-selection and record-growth
arguments needed to establish exact-solution families are not supplied; the item now states them as provisional. That
audit also led to the repairs in Limitations 6 (no localization of the source in the swirl core), in the items of
Limitations 2 on near-axis cancellation (definitions of $D_t$ and $\Delta_5$), on the Lagrangian form of the swirl source
(the multiplicity) and on viscous cancellation (the energy class and the estimate of the loss), and to clarifications
in Section 5 (level scales), Section 9A, Result 5 and Limitations 1'; these repairs were audited once, and the two
further defects found (the packet geometry in the closure item and an overstatement in the numerical sentence below)
were repaired. The remark on the heat depth of the history in Limitations 6 and the item of Limitations 2 on
quantitative Liouville theorems and backward propagation were checked by hand and audited once; the audit confirmed the
scalings, the examples and the enstrophy bound of the second (and the statements of Lei and Zhang, Theorem 1.1, and of Lei,
Zhang and Zhao, Theorem 1.3, in the auditor's copies of the primary texts; only the abstracts were read here), and found a
quantifier error in the first, which had claimed divergence of the heat depth on every admissible normalization; it is
now restricted to normalizations with retained oscillation (the hand check had missed this error). The two
quantitative forms (i) and (ii) of the age argument added to that remark, the stationary half-space example there
and the heat-depth bound for the interval of Lemma 26A were proposed in a consultation, checked by hand (the
threshold on $K$ that removes the source term in (ii) was added here) and then audited. The audit confirmed the
scaling powers, the persistence constant, the source threshold, the stationary inflow example and the heat-depth
exponent; it required an explicit real even cutoff with $0\le\chi\le1$ in (i), and a correction in (ii): the
quarter-mass influx conclusion follows when the displayed dissipation bound fails, not merely when half-mass
persistence fails, and the vanishing of the persistence charge is conditional on persistence. Both repairs were
made, and a second audit found the repaired text correct. A numerical evaluation of the exact heat flow of the uncut profiles of the viscous-cancellation item
was consistent with its $O(k^{-1})$ estimate for the flat profile and with the limit for $F=\cos$: $k$ times the
flat-profile loss approached $336\pi^4\approx3.27\cdot10^4$, the sum of the changes $\frac92x_j^2$ of the values at the points
$\pi kr^2\in\pi\mathbb Z$ with interior weights $2$ and endpoint weights $1$, and the cosine loss approached $12\pi^2$. Identifying $336\pi^4$ as the
exact asymptotic constant would also need control of the shifted extrema, and the numerical evaluation is a
consistency check, not that proof.
The paragraph of Limitations 6 on two necessary conditions for the meridional mass $Q$ (the weighted identity for
$\Gamma$ with $k=3$, the bound of $S_Q$ by the weighted dissipation, and the $L^2$-in-time bound for $Q$ with its
recent-production consequence) was derived and checked by hand; the weighted identity for
$k=1,\frac52,3$, the Hardy constant and the bound of the production by the weighted dissipation were also checked by
numerical quadrature on one test field with a divergence-free drift (smooth in the meridional variables with the
vanishing at the axis used in the integrations, but without the parity of a smooth Cartesian field; a consistency check
of the integrations only). An audit confirmed the constants, the $L^2$-in-time bound and its consequence, and found
the two defects stated in that paragraph, which were repaired after that audit; the repaired paragraph was not the
subject of a further dedicated audit.
Item (iii) of that paragraph summarizes two second-model research answers; I rederived the $q$ identity and the
time-cutoff bound, the strong-swirl length bound, the functional swirl example, the witness-mass localization, the
comparison of the three times and the exponent arithmetic of the scalar bookkeeping by hand. One second-model audit of
item (iii) confirmed each estimate and the scalar arithmetic (the auditor reports exact rational arithmetic), with the
qualifications stated there: the consequence $Q/D^{1/2}\to0$ and the deadline of (ii) assume
$\|\omega_0^\theta\|_1<\infty$, the comparison of times gives a necessary duration for an absolute source budget and
says nothing about actual production, export or survival, and the bookkeeping is a scalar consistency test, not a
field. It asked that the dependence of $C_R$ on the oscillation constant be stated; this was done.
Item (iv) of that paragraph summarizes a third second-model research answer; I rederived the energy inequality for
$\eta^s$, the kernel bounds, the solid-torus bound and the exponent chain by hand. One second-model audit of item (iv)
confirmed the energy inequality, the kernel bound, the velocity bound (it supplied the near and far split now stated),
the solid-torus bound, both lower bounds and the exponents (the auditor reports exact rational arithmetic), as a necessary
condition and scalar compatibility only.
Proposition 14A (Section 6A) was obtained from a second-model research answer (re-zooming at a Lebesgue point of the
weak limit and its defect, and the one-sided local energy bound for the terminal slice) and rewritten here; I
rederived each step by hand. One second-model audit confirmed (a), (b) and (c) step by step, including the extension
of the tangent to positive rescaled times on which the energy limit at $\tau=0$ rests; it found that the paragraph after
the proof claimed more than was proved (that (HD) does not characterize (C*-D), and that the vorticity at the tangent is
carried in), and that paragraph was rewritten to state only what is proved; the fourth whole-report audit checked the
rewritten paragraph and Proposition 14A(a) to (c) again and found them correct.
Proposition 14B was derived by hand (part (b), and the extraction of (d) in a form that controlled only the azimuthal
part of the boost) and in a second-model research answer, which proved the Liouville statements of (b) independently
by the same maximum-principle arguments, pointed out that with the record mean subtracted the axis moves with the
horizontal part of the boost (now handled by the comparison with the axis-centred mean in (c)), and proposed the
unit-viscosity gradient-record extraction of (c) and the scalar rates of Remark (ii); I checked each step by hand. Part
(a) was first derived using the cited $\epsilon$-regularity theorem and interior derivative estimates without re-reading
their sources. I later read the statement and attributions of the restatement as Theorem 1.1 of Guevara and Phuc,
arXiv 1702.00449; I did not re-read the original regularity proofs or the interior derivative estimates, and the
quantitative regularity step remains explicitly granted in Proposition 14B(a). Of the literature statements in Remark (iii),
I read Theorem 1.3 and Remark 1.4 of Lei, Zhang and Zhao (arXiv 1701.00868) and Section 3 of Zhang's survey (arXiv
2101.04905v2) in the original; the statements attributed to Koch, Nadirashvili, Seregin and Sverak and to Lei and Zhang
are as reported in the second-model research answers. The constructions in the first of these answers of nonconstant
bounded solutions of scalar transport-diffusion equations with smooth bounded divergence-free drifts are not used.
A second-model audit of the frozen text checked the BMO increment and pressure estimates, the Galilean drift
calculation, the applicability of the one-cylinder $L^3$-$L^{3/2}$ criterion (through that restatement), the two Liouville arguments, the
convergence of the increment pressure and both record extractions, and found that the limiting pressure gradient is
exactly $\Pi[v]$. It identified the constant-field case of (a), the curl-freeness of $\Pi[v]$ for unbounded members (now
part of the definition of the class), a sign in the vorticity equation, and qualifications concerning subsequences,
the constant horizontal boost, the uniformity of the decay of $\Gamma$ in Remark (iii) and the scope of the logarithmic
example; I checked these by hand and repaired the text. A later whole-report audit of the repaired text spot-checked parts
(a) to (d) again and found no failing step, subject to the regularity input granted in (a); it could not retrieve primary
sources. It also found two stale or undefined passages elsewhere (a remark after Theorem 17 that predated Proposition 22,
and an undefined symbol in the record-freezing item of Limitations 2) and two places where the granted input was not
carried into a summary; these were repaired by hand.

Proposition 14C was derived by hand from Lemma 2's argument, the dyadic comparison of ball means and the
Cauchy-Schwarz inequality; part (c) uses only $D\le M^2$ near $T_*$ (regime (II)), and its second form the granted bound
of Proposition 14B(a). I checked the constants, the
monotonicity step in (b), the logarithmic example of the Remark and the consistency with the scalar rates by hand. A
second-model audit of a frozen text, in which (c) was still stated under the granted bound, found (a), (b), the conditional
(c), the Remark and the plateau radius correct, supplied the admissibility check for the plateau balls now noted in the
Remark, and independently derived the unconditional form of (c) from $D\le M^2$ with the same constants. It found one
overstatement (that excluding (FLAT$_0$) would require improving the logarithm), a misstated comparison with Lemma 2 in
(b), a missing range $1\le p<\infty$ in the citation of Lei, Zhang and Zhao, and an overly broad necessity claim in
Remark (iii) after Proposition 14B; I checked each by hand and repaired the text. That audit could not retrieve sources
and worked from the extracted texts of the two papers read in the original.

Proposition 14D and the divergence-free example in the Remark after Proposition 14C were first proposed in a second-model
research answer (route question on (FLAT$_0$)), which also identified the summability of the certified dissipation. I
rederived the moving-frame identity for $b'$, the three bounds, the enstrophy bound (including the boundary terms, which
the answer did not treat), the disjointness of the intervals, both cases in (c) and the passage from dyadic records to all
$t$, and the curl formula, the constant core and the bounds for the example, by hand. A second-model audit of a frozen text
(without second-model consultation inside the audit, and with web access) found (a) to (c), both Remarks' estimates and
the example correct, and pointed out that the divergence of $M^2(T_*-t)$, then presented as a consequence of (c), is
already Proposition 7(c); that the necessity sentence in Remark (ii) overstated (nonsummability is sufficient, not
necessary); that $\Theta_0R\ge1$ holds eventually under (FLAT$_0$); and that $b>0$ should be stated in the example. I
checked these by hand and repaired the text.

A later whole-report audit of a frozen text containing these repairs (without second-model consultation inside the
audit) compared every item of the Result and the Limitations with the Findings and spot-checked Propositions 14A to
14D and 22, finding no failing step (14B subject to its granted input) and no em or en dashes. It found one unsupported
inference in summaries of Proposition 14D: the lower bound for $M(t)^2(T_*-t)$ uses the flatness ratio of the next
dyadic record, not the current ratio $h(t)=M(t)/\Theta_0(t)$; monotonicity gives $h_{n+1}\le4h(t)$ but not the lower
comparison needed to replace the next-record ratio by the current one in this estimate. It
also asked for missing subsequence and hypothesis qualifiers in Result 4'' and Limitations 1'', amplitude and scope
qualifiers in two items of Limitations 2 and in Limitations 4, the exponent range in the pressure estimate of
Proposition 14B, a symbol clash ($\Gamma$ for the Newtonian kernel), corrections of three audit-status sentences in this
section, and the statement that the first missing implication is precise within the strategy of admissible
amplitude-$M$ isotropic normalizations. I checked each point against the text and made these repairs by hand; they
have not been re-audited.

The Remark on the pressure impulse after Proposition 14D was proposed in a second-model research answer (route question
on (FLAT$_0$)). I rederived the impulse identity, the Nash decay, the choice of $\varsigma_n$, the lower bound $J_n\ge m_n/2$, the
antisymmetrized kernel formula, the bound of $|F|$ by $\|\nabla q\|_1$ with the cubic logarithm, the entropy, moment and
Gaussian bounds and the resulting upper bound by hand. A hostile second-model audit (A66) of that version found
the identity, the decay, the lower bound, the kernel formula and the comparison with Proposition 14C correct. It reported
gaps in the presentation: the flat-record quantifier, the construction of $q$, the cutoff justification of the identity and
the kernel substitution, the attribution of the identity, and above all the unwritten time-logarithm step of the upper bound.
It also asked that the impulse be stated as a signed quantity with the older contribution retained, and that the
comparison of $h_{n+1}$ with $h(t)$ be corrected as above. The Remark now writes these steps, following the audit's
reconstruction, which I checked by hand. A second hostile audit of the revised Remark (A67) found no false displayed
estimate and asked for three scope repairs: the record quantifier in Result 4''', the restriction of the comparison with
Proposition 14C(c) to regime (II), and a more precise closing sentence. I made these by hand; they have not been
re-audited. The cited sources were not checked by me.

Three items of Limitations 2 were checked as follows: the normalization at records of $r|u^{mer}|$ (immediately before the
Holder-regularity item), and backward uniqueness for the limits of Proposition 14B(c) and the Gaussian frequency of $q$
(just after the BMO-class Liouville route). The first, with its
test on the two fields of the Remark after Proposition 14C, was worked out by hand. The other two come from a
second-model research answer (route question on (FLAT$_0$)); I rederived the single-time Biot-Savart step, the
frequency identity $dN/ds=-2\|Z\|^2/H+2\langle Z,\mathscr R\rangle/H$ with $Z=(A-N)F$, $A=-\Delta_\xi+\frac12\xi\cdot\nabla_\xi$,
$H=\|F\|^2_{L^2(\mu)}$ and $\mathscr R$ the transport and stretching remainder, the resulting inequality and the scalar-rate
exponents by hand. The exterior backward uniqueness and unique continuation theorems of Escauriaza, Seregin and Sverak
enter only that Limitations item, in the versions reported by the answer, which were not read. A hostile
second-model audit of a frozen text containing the three items (without second-model consultation inside the audit,
and without access to the sources) found the field estimates, the internal backward-uniqueness argument and the
frequency inequality correct. It found that the divergence of the weighted supremum does not give finite attained
records (the data class does not bound $\|r\,u^{mer}(0)\|_\infty$; it gave an explicit smooth finite-energy swirl-free
datum, which I checked) and that the bound for that rescaling holds only on the available time interval; it asked for
the definitions of the lift and of the Gaussian measure, for a description of the divergent transport term as a
divergent available bound, and for the consequence $\kappa_n\to\infty$ in the backward-uniqueness item. It also asked
for qualifier repairs: the conditional status of Proposition 14B in the opening paragraph, the label of Result 4',
the quantifier "every weak limit of an admissible amplitude-$M$ isotropic normalization" in Result 4'' and Limitations
1', the rigidity and scalar-rate wording in Result 4''', the quantifiers of Theorem 6 in Result 5, the description of
the pressure lower bound in Result 5' and after Lemma 15' (a lower bound for the majorizing increment integral, not for
the pressure gradient), the defect-energy summary in Result 5'', the scope of the dimensional scenario in Limitations
1', the constant of the tail bound in Limitations 1'' and two sentences at the opening of this section. It found the
status label and the statement of the first missing implication consistent with the Findings. I checked each point
against the text and made these repairs by hand. A second-model literature check of
post-2021 results on axisymmetric solutions found no theorem whose hypotheses follow from fixed data and which
excludes (FLAT$_0$) or yields a bounded nonconstant ancient limit; its statements were not re-read here, except that
the abstract of arXiv 2609.20762 v2 was read and the corresponding sentence of Limitations 6 was made precise. A
focused second-model re-audit of these repairs, of that sentence and of this section found them correct except for
three points (positivity and domain conditions in the rescaling at records of $r|u^{mer}|$, an unproved converse in
the sentence on that preprint, and a wrong item number in this paragraph), which I repaired as it proposed. It again found the status label and the first missing implication honest. A
last focused second-model audit found these three repairs correct and the status label and first missing implication
unchanged; for the Limitations 2 item on Holder regularity near the axis (added after the re-audit) it confirmed the
local estimate and the exponents but asked for the time, domain and history conditions and for the qualification that
the lower bound for the Euler length by $\tau\|u(t)\|_\infty$ needs the velocity bound on the whole space, and it found
one stale locator in this paragraph; I made both changes in the form it proposed, and these final edits have not been
audited again.
