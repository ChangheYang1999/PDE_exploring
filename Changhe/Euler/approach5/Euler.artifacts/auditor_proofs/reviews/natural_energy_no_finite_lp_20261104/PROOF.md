# Natural ball energy without a finite velocity norm

## 1. Exact object and theorem

The source is LIT372 at SHA256
88da79a97f1237343552cc2ab2e8160051369b620939d84fab21bc053586d1f9.
All seven sections, thirty-six manual checks and the formal-source note
were read. Exact copies and the author's reading record are retained
in verification. No numerical computation is involved.

For every 0<beta<1 and L>0 the construction below gives a smooth
bounded divergence-free U on R3, tending uniformly to zero, such that
for every fixed a in R3,

    E_a(R)=integral_{|y-a|<R}|U(y)|^2
          =L R^beta+O_a(R^(beta-1)/log R).

For every finite p>0, both integral |U|^p and
sup_{lambda>0} lambda^p measure{|U|>lambda} are infinite.
There is a smooth Poisson pressure P0 with
-Delta P0=tr((DU)^2). Nevertheless no real c, omega and C1 pressure
P make this U a full rotating Euler profile.

The constants in the construction may depend on beta,L and the fixed
smooth cutoff functions. The energy remainder constant may also depend
on a; the weak-norm bound may depend on p. There is no assertion of
uniformly bounded derivatives at infinity. The countertest concerns
kinematic and Poisson implications, not the remaining momentum equation.

## 2. Exact baseline and orthogonal bump

Write J(y1,y2,y3)=(-y2,y1,0), K0=8pi/3,

    s=(beta-5)/2,  b=sqrt(beta L/K0).

Choose a smooth 0<=chi0<=1 vanishing on [0,1] and equal to one on
[2,infinity). The field b chi0(r) r^s Jy is smooth, since its scalar
coefficient vanishes near zero. Its energy inside radius2 is strictly
less than L2^beta: the corresponding integral is
beta L integral_0^2 chi0(r)^2 r^(beta-1)dr.
Choose a nonzero smooth eta0 supported in (1/4,1/2). Adding t0 eta0
to the scalar coefficient, where

    t0^2=(L2^beta-E_pre(2))/(K0 integral r^4 eta0(r)^2 dr),

fills the positive deficit exactly. The two scalar terms have disjoint
supports. Call the resulting scalar f0 and the field U0=f0(r)Jy.
It is smooth and divergence-free, its squared magnitude is even, and
for r>=2 its surface energy is

    T0(r)=K0 r^4 f0(r)^2=beta L r^(beta-1).

Hence E0(R)=LR^beta for all R>=2, with no integration constant.
Also |U0|<=C r^((beta-3)/2) at infinity.

For t<1 put psi(t)=exp(-1/(1-t)), and for t>=1 put psi(t)=0.
Then psi(|x|^2) is smooth and supported in the closed unit ball.
Let W=curl(psi(|x|^2)Jx). Direct differentiation gives

    W=(-2x1 x3 psi',-2x2 x3 psi',2psi+2(x1^2+x2^2)psi').

Thus W is smooth, compactly supported, divergence-free and nonzero at
zero. Its horizontal part is radial, so W.Jx=0 pointwise. Put
Kp=integral |W|^p, a positive finite number for every p>0.

## 3. Scales and exact compensation

Take a smooth chi>=0 supported in (2,3) with integral chi=1, and fix
0<eta<=beta L/(4||chi||_infinity). For positive integers n set

    Rn=10n,  an=1/log(Rn+e),
    en=eta Rn^(beta-1)/log(Rn+e),
    epsilon_n^3=en/(K2 an^2)
                =(eta/K2)Rn^(beta-1)log(Rn+e).

Since beta<1, epsilon_n tends to zero. Restrict to n>=n0 so that
Rn>=3 and epsilon_n<1/4. Define

    Wn(y)=an W((y-Rn e3)/epsilon_n).

The supports are disjoint balls and integral |Wn|^2=en. Because the
translation is along the axis, Jy=epsilon_n Jx at y=Rn e3+epsilon_n x;
therefore Wn.Jy=0. This verifies orthogonality after translation, not
just for the unshifted bump.

For r>2 set g(r)=sum_n en chi(r-Rn)/T0(r), and set g=0 for r<=2.
The intervals supporting this locally finite sum are disjoint. On one
such interval r/Rn<=2 and log(Rn+e)>=1, so

    0<=g(r)<=2eta||chi||_infinity/(beta L)<=1/2.

The scalar f=f0 sqrt(1-g) is smooth. Define

    U=f(r)Jy+sum_n Wn.

Every term is divergence-free. Orthogonality and disjointness give

    |U|^2=f(r)^2|Jy|^2+sum_n |Wn|^2,
    integral_{|y|=r}f(r)^2|Jy|^2
      =T0(r)-sum_n en chi(r-Rn)  for r>=2.

Thus the compensation removes exactly en after bump n is fully inside
the centered ball and before the next bump begins. No signed energy
or square-root ambiguity is used.

## 4. Centered and translated energy; uniform decay

For R>=2 let Fn(R)=integral_{B_R}|Wn|^2 and
Cn(R)=integral_0^R chi(r-Rn)dr. Then exactly

    E(R)=LR^beta+sum_n [Fn(R)-en Cn(R)].

Each bracket is zero before Rn-epsilon_n, rises to en during the bump,
remains en until Rn+2, decreases to zero by Rn+3 and remains zero.
The active intervals are disjoint. Therefore

    0<=E(R)-LR^beta<=C R^(beta-1)/log R.

The sum never retains offsets from completed bumps.

For a fixed center a, first consider only F0=|U0|^2. With
G(a)=integral_{B_R}F0(y+a)dy, the divergence theorem gives

    partial_i G(a)=integral_{partial B_R} F0(y+a)n_i,
    partial_j partial_i G(a)
      =integral_{partial B_R} partial_j F0(y+a)n_i.

Evenness gives grad G(0)=0. On all boundary points needed for the
segment from0 to a, when R>2|a|+4 the exact tail formula applies and
|grad F0|<=C R^(beta-4). Hence |D^2G|<=C R^(beta-2), and Taylor's
theorem yields

    integral_{B_R(a)}|U0|^2=LR^beta+O_a(R^(beta-2)).

The nth signed correction density is
|Wn|^2-f0(r)^2[en chi(r-Rn)/T0(r)]|Jy|^2.
Its positive and negative masses are each en, and its full integral
is zero. Its support lies in Rn-1/4<=|y|<=Rn+3.
If this radial region lies entirely inside B_R(a), or entirely
outside it, the correction contributes zero. Consequently only

    R-|a|-3<=Rn<=R+|a|+1/4

can contribute. There are O_a(1) such indices because Rn=10n;
each contribution has absolute value at most en. Their sum is
O_a(R^(beta-1)/log R). The smaller baseline error is absorbed, since
R^(beta-2)=o(R^(beta-1)/log R). This proves the all-center statement
without assuming translation invariance of the profile equation.

The supports accumulate only at infinity, and all cutoffs are smooth
across their boundaries, so U is smooth at every finite point.
The azimuthal term is bounded by |U0| and the nth bump by
an||W||_infinity. Both tend uniformly to zero at infinity. Thus U is
bounded and uniformly decaying; dominated convergence against a
compactly supported test also gives U(R.) tending to zero in
distributions. The single point x=0 has no effect on this argument.

## 5. Divergence of every strong and weak finite norm

On a bump support, |U|>=|Wn|. For fixed p>0, disjointness gives

    integral |U|^p
      >=(Kp/K2)eta sum_n Rn^(beta-1)log(Rn+e)^(1-p).

For p<=1 the logarithmic factor is eventually at least one. For p>1,
log(Rn+e)^(p-1)<=Rn^(beta/2) eventually, so the terms dominate a
positive multiple of Rn^(beta/2-1). Both comparison series diverge,
since Rn=10n and beta>0. This uses no norm inequalities for p<1.

Choose a positive-measure set A inside the unit ball and w0>0 with
|W|>=w0 on A, possible by continuity at zero. For large N set
lambda_N=w0/[2log(20N+e)]. For N<=n<=2N, on the disjoint sets
Rn e3+epsilon_n A one has |U|>=an w0>=2lambda_N. Their combined
volume is at least

    (|A|eta/K2)sum_{n=N}^{2N}Rn^(beta-1)log(Rn+e)
      >=C N^beta log N.

Therefore lambda_N^p measure{|U|>lambda_N}
is at least C_p N^beta(log N)^(1-p), which tends to infinity for
every fixed finite p>0. This is the asserted weak-Lp failure.
The thresholds tend to zero, so boundedness is not contradicted.

## 6. Poisson pressure, including the distributional limit

Let Gamma(z)=1/(4pi|z|), so -Delta Gamma=delta0. The distributional
second derivative is

    partial_i partial_j Gamma
      =(1/(4pi))PV[(3z_i z_j-|z|^2 delta_ij)/|z|^5]
        -(delta_ij/3)delta0.

Convolving with U_i U_j gives exactly

    P0(y)=-|U(y)|^2/3
      +(1/(4pi))PV integral
       [(3z_i z_j-|z|^2 delta_ij)/|z|^5]
       U_i(y-z)U_j(y-z) dz,

with repeated indices summed. Near zero, subtracting the smooth
value U_i(y)U_j(y) uses the kernel's zero spherical mean; the
remaining integrand is O(|z|^(-2)), locally integrable in R3.
For y in any fixed compact set, the far annulus of scale R has
absolute bound C R^(-3)E_y(2R)<=C R^(beta-3). Dyadic summation
converges. Derivatives of order m of the far kernel gain R^(-m),
so they also converge locally uniformly.

To justify smoothness without tail bounds on DU, separate the density
U_i U_j by a smooth cutoff in the original integration variable which
is one near the compact set of observation points. Its local part is
smooth and compactly supported; convolution with the distributional
kernel is smooth. All observation derivatives of the remaining part
fall on the smooth far kernel and are justified by the preceding
bounds. Thus P0 is smooth.

For the equation, first truncate U_i U_j by compact smooth cutoffs
which exhaust space. The resulting smooth pressures obey
-Delta P_R=partial_i partial_j(chi_R U_i U_j). Their kernel tails
converge locally, as just proved, to P0. The right sides converge in
distributions to partial_i partial_j(U_i U_j), since every test is
compactly supported. Passing to the limit gives

    -Delta P0=partial_i partial_j(U_i U_j)=tr((DU)^2).

The last identity follows by differentiating and using div U=0.
No global integrability of q or of derivatives of U was assumed.

## 7. Full momentum fails for every c and omega

On every shell Rn+4<|y|<Rn+8, all bumps and compensations vanish and
U=h(r)Jy with h=b r^s. These are nonempty open shells. Directly,

    (Jy.grad)U=JU,
    (U.grad)U=-h^2(y1,y2,0),
    (1-c)U+c(y.grad)U=(1+cs)U.

The two rotation terms therefore cancel for every omega. The angular
component of the full equation would require

    partial_theta P=-(1+cs)h(r)(y1^2+y2^2).

On any circle at fixed positive cylindrical radius and height within
the shell, this right side is constant. Integrating a single-valued
C1 pressure around the circle forces 1+cs=0. If that relation holds,
the remaining equation is

    grad P=h(r)^2(y1,y2,0).

The z derivative of the first component is
2s b^2 r^(2s-2)y1 z, nonzero at suitable points in the shell, whereas
the first derivative of its zero third component is zero. The proposed
gradient has nonzero distributional curl, impossible for a C1 scalar.
This treats both possibilities for c, and is independent of omega or
which harmonic addition is made to the Poisson pressure.

For the campaign exponent c=2/(5-beta), one has exactly 1+cs=0;
it is the curl obstruction that excludes the construction in this
case. The exponent is in (2/5,1/2), and the error in Section 4 is
little-o(R^(beta-1)), matching the precise energy law without
satisfying the full equation.

## 8. Status and dependency boundary

The construction and each limiting argument have been independently
reconstructed from the complete source. The only distributional
input is the displayed Newtonian kernel identity. LIT370 motivates
the compensation method but no lemma from it is needed here.
No numerical experiment or formal build is needed.

The exact implication challenged is from smooth divergence-free
uniform decay, Hb, the all-center energy asymptotic and a smooth
Poisson pressure to some finite strong or weak velocity Lp norm.
The implication from the full rotating equation is still open.
No counterexample to the Euler conjecture, bounded derivative claim,
velocity-integrability theorem or novelty assertion follows.
The complete existing-agent comparison in the team records, all eight
section checks and remarks V1-V3, was read and independently checked.
Sections 9-10 record the analytical refinements. Its scripts, numerical
threshold checks and execution claims are not certified. The comparison
is from the configured model agent; actual provider execution remains
independently unattested.


## 9. Radial-swirl obstruction and unbounded derivatives

The shell calculation has a useful precise extension. Suppose on an open
spherical shell 0<r_a<|y|<r_b a C1 field is U=h(|y|)Jy with h C1, and
there is a single-valued C1 pressure solving the full profile equation.
Its pressure-free residual is

    (h+c r h')Jy-h^2(y1,y2,0),

independently of omega. For each radius in the shell one may choose a
horizontal circle there with positive cylindrical radius. The pressure
integral on that circle forces h+c r h'=0. For c=0 this gives h=0.
For c!=0 the ODE gives h=b r^(-1/c) throughout the connected interval.
The remaining proposed gradient has component derivative

    partial_3[h^2 y1]=-(2/c)b^2 r^(-2/c-2)y1 y3.

A point with y1 y3!=0 exists at every positive spherical radius. Equality
of mixed pressure derivatives therefore forces b=0. The ODE has made the
proposed gradient smooth, so this argument is valid even when the original
pressure was only C1. Thus no nonzero purely radial coefficient times Jy
can solve the full equation on such a shell for any real c and omega.
This observation does not exclude a general swirling field or nonradial
coefficient.

For the construction in Sections 2-7,

    an/epsilon_n=(K2/eta)^(1/3) Rn^((1-beta)/3)
                    log(Rn+e)^(-4/3) -> infinity.

Choose a fixed point inside the unit ball where DW is nonzero. On the
corresponding point of bump n, the compensation is absent and the
baseline derivative tends to zero. The scaled bump derivative therefore
shows that DU is unbounded. There is also a point where curl W is nonzero:
otherwise compactly supported divergence-free and curl-free W would have
harmonic components and vanish, contrary to W(0)!=0. The same argument
shows unbounded curl U. This is a direct property of this construction;
no general equivalence of bounded gradient and bounded curl is used.

## 10. What an additional bounded gradient would imply

Let a C1 vector field V on R3 be bounded and have bounded gradient outside
a fixed ball. Assume

    integral_(B_R)|V|^2=L R^beta+O(R^(beta-1)),
    L>0, 0<beta<1.

No divergence condition is needed for this paragraph. The constants may
depend on V,L,beta and the gradient bound. Subtracting the energy values
at R+1 and R-1 gives a shell bound C R^(beta-1), using only values of the
remainder. Choose H at least1, the exterior supremum of |V| and the
exterior supremum of |DV|_op. If |V(y0)|=delta and |y0|=R is sufficiently
large, then |V|>=delta/2 on B_(delta/(2H))(y0). This ball lies in
R-1<|y|<R+1 and is within the region of the gradient bound. Its energy is
at least a fixed positive constant times delta^5/H^3. Consequently

    |V(y)|<=C |y|^((beta-1)/5)

at large distance. For p>2, the integral of |V|^p over each unit shell
k<=|y|<k+1 is at most its energy times the supremum of |V|^(p-2), hence
at most C k^((beta-1)(p+3)/5). The sum converges whenever

    p>(2+3beta)/(1-beta).

The right side is greater than2, so the use of p-2 was justified. Local
C1 regularity handles the remaining compact ball. Thus V belongs to every
such Lp space. In particular the all-p countertest cannot have bounded
gradient, consistently with Section 9. At beta=5-2/c this threshold is
(17c-6)/(2-4c). This is a kinematic estimate, not the stronger natural
pointwise decay estimate for full profiles mentioned in the comparison.
That earlier full-profile theorem is not re-audited here.

The kinematic conclusions also agree with the previously confirmed source
identities: the constructed E=o(R) is infinite in the limit, so an eventual
lower bound on rN-E would contradict the cumulative-source criterion;
the finite positive quadratic-source moment criterion would contradict
its infinite energy. These observations do not supply any missing full
momentum equation or imply that an actual profile has infinite Lp norms.
