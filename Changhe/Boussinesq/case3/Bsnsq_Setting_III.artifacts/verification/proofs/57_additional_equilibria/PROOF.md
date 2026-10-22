# Additional equilibria for beta greater than two

Date:2026-10-20. Status: CONFIRMED by independent verifier, with actual
second-model reviews48,50,51 and classification follow-up52 checked.
No full endpoint.

## 1. Hypotheses, conventions and dependencies

Let a smooth full-plane B2 profile satisfy the prompt and beta>2. Use its
canonical relative velocity V=U-U(0), W=beta X+V, and the given x-reflection. Explicitly impose Theta(0,y)=0 for every y,
as required in PROMPT.md; this gives Theta_y(0,y)=0, not merely evenness.
Normalize the nonzero quadratic temperature coefficient to a0>0 by the
previously checked signed spatial scaling. The conclusions without sign
language also hold before this normalization. Put

    c=beta-2, d=beta+2, D=3beta+2, E=2beta+1,
    J(v1,v2)=(-v2,v1), Q=J grad Theta.

Thus div W=2beta, -curl W=Omega, W.grad Theta=c Theta and
W.grad Omega+Omega=Theta_x. The source at0 has eigenvalues c/2,D/2.
By packets33,36,40 the full target has the smooth angular limits and bounds

    V=O(r^{1-1/beta}), DV=O(r^{-1/beta}),
    Omega=O(r^{-1/beta}), grad Theta=O(r^{-2/beta}),
    Theta=O(r^{1-2/beta}).

The leading angular vorticity is not zero identically. The flow is complete,
all negative semiorbits from a compact set stay in a common compact ball, and outside a fixed disk its
radial velocity is positive and comparable to r. Every forward orbit is either
bounded or eventually leaves that disk and escapes, so R2=K union E.
Packets05/33 give a C1 scattering diffeomorphism Phi:E->R2 minus{0}; its
angular coordinate is a submersion. In particular open invariant subsets
of E contain an open interval of asymptotic directions. Let Z be its compact zero
set and K its compact bounded-forward-orbit set. Temperature is zero on K
by forward transport and c>0. On the source basin B0, packet04/48 gives
Theta=a0 xi^2, with xi smooth and zero exactly on the invariant axis.
Packet53 Section2 proves that compact alpha/omega limit sets have no regular
point for a planar field of constant nonzero divergence; that elementary
return-loop lemma is used below, including its nonisolated-zero scope.

The statements independently established here are: all such limit sets
are single equilibria; all zeros have real eigenvalues; the source and
saddle alternatives below; vanishing of Theta, gradTheta and Omega on every
source-basin boundary; any additional zero requires an additional axis
zero; the two axis resonances with parity; and, when every zero is
hyperbolic, K is a finite tree and Theta is nonflat at every zero.
These are restricted structural results, not exclusion of the full target.

The audit concerns the exact lead snapshot stored in
review_snapshots/zeros1_20261020T1815/PROOF.md, SHA256
93013825880d953df2d26e4defc64a85a7ea28c385445f672f9b438a83333422,
copied at18:13:52Z. The folder label is only an identifier. The live lead
file may change. Its proof was read in full; none of its conclusions was
accepted from a summary alone.

## 2. Scalar resolvent and commuting vector fields

Integrating the vorticity equation from time -T to0 gives

    Omega(Y)=e^{-T}Omega(phi_{-T}Y)
                    +int_{-T}^0 e^t Theta_x(phi_tY)dt.

The negative orbit stays in a compact ball, so its endpoint tends to0 and
the integral is absolutely convergent. Consequently

    Omega(Y)=int_{-infinity}^0 e^t Theta_x(phi_tY)dt.       (1)

Differentiating W.gradTheta=cTheta gives DQ W=DW Q-dQ. This follows from
J M^T=(tr M)J-M J for a two-by-two matrix M. Therefore

    [W,Q]=-dQ, Dphi_t(Y)Q(Y)=e^{dt}Q(phi_tY).             (2)

The second identity follows by solving the same variational equation on
both sides. In particular a short Q-curve in a compact set has negative
flow images whose lengths are at most C e^{-dt}, since all those images
stay in a common compact ball. No bound on the full inverse derivative
of the flow is being asserted.

## 3. A compact connected equilibrium limit is one point

A bounded semiorbit has a nonempty compact connected limit set L. The
return-loop lemma makes L a subset of Z. Suppose L has several points.
At each p in L, DW(p) has positive trace, hence is nonzero. The implicit
function theorem applied to one scalar component of W puts all nearby
zeros in a C1 embedded curve. Some open subarc of this curve must belong
to L. To prove this without a local-connectedness assumption, choose a
curve rectangle about p which omits another point of L. If the coordinates
of L on its middle curve contain no interval, choose a missing coordinate
on each side of p. A smaller closed rectangle between them has boundary
disjoint from L. Its intersection with L is a nonempty proper relatively
open and closed subset, contradicting connectedness.

Near an interior point of the obtained zero subarc, graph coordinates
(u,v), with u normal to the curve, give

    udot=u A(u,v), vdot=u B(u,v), A>=eta>0, |B|<=C.

Division in the u direction is legitimate even with a C1 curve: write it
as a graph and use the original C1 field's u derivative; A,B are continuous.
The transverse eigenvalue is the positive trace, while the tangent one is0.
In backward time, |u| decays at least e^{-eta t}; tangential variation is
bounded by C|u_initial|/eta. A sufficiently small diamond
|v-v0|+(C/eta)|u|<h is backward invariant. Every point in it converges
backward to one equilibrium. If L is an alpha-limit, a visit to this
neighborhood forces a single backward limit. If L is an omega-limit,
there are visits t_j tending to infinity. Backward invariance places each
fixed earlier orbit point in the diamond, and

    |u(t)|<=e^{-eta(t_j-t)}|u(t_j)| ->0.

Thus the trajectory is an equilibrium. Both cases contradict nonsingleton
L. Every alpha-limit, and every bounded omega-limit, is one zero.

A singleton limit of a bounded semiorbit implies actual convergence, since
otherwise a sequence bounded away from that point supplies another limit.
Hence K consists exactly of Z and connecting orbits between individual zeros.
Moreover K is connected: for a sufficiently large outward disk D_R,

    K=intersection_{t>=0} phi_{-t}(closed D_R).

These are nested compact disks. K has area zero, because it is invariant
and its area is multiplied by e^{2beta t} under the flow.

## 4. Classification and flatness at a degenerate zero

At a zero z, set M=DW(z). Evaluation and first differentiation give

    Theta(z)=0, M^T gradTheta(z)=c gradTheta(z),
    Omega(z)=Theta_x(z).                              (3)

If the gradient is nonzero, M has distinct positive eigenvalues c,d.
If it vanishes, Omega(z)=0, so M is symmetric. All zeros therefore have
real eigenvalues and no nontrivial Jordan block. With trace2beta, they
are hyperbolic sources, hyperbolic saddles, or have eigenvalues0,2beta.
Every zero has a positive eigenvalue and a local strong unstable curve;
no zero is a forward attractor.

At a degenerate zero choose its orthogonal eigen-coordinates. If the first
nonzero homogeneous Taylor term P_N of Theta existed, it would satisfy
(MY).grad P_N=c P_N. The monomial weights are2j beta, j>=0, none equal to
0<c<beta. Induction gives complete flatness of Theta. For Omega the
homogeneous operator is (MY).grad+1, with weights2j beta+1>0; its forcing
and lower terms vanish, so Omega is also flat. This is a jet statement,
not vanishing on a neighborhood.

If Z is finite its total index is1, since on a sufficiently large circle
W is homotopic to beta X through fields with strictly positive radial
part. An isolated degenerate zero has index -1,0 or1: solving the component
with positive derivative reduces its local degree to that of (u,g(v)),
where g has no further zero nearby. Its signs on the two punctured sides
give precisely those three possibilities.

## 5. Saddles, including their first jets

At a saddle use orthogonal coordinates (s,u) with eigenvalues -nu and
mu=2beta+nu, nu>0. On its smooth unstable curve a scalar coordinate r has
rdot=mu r+O(r^2). The smooth correction
rho=r exp(int[mu/w(r)-1/r]dr) satisfies rhodot=mu rho, since the bracket
extends smoothly through0. Temperature on a punctured branch must equal
C |rho|^{c/mu}. As 0<c/mu<1, differentiability at the zero forces C=0.
Transport extends this to the whole unstable manifold.

There gradTheta annihilates W, so Q=fW at regular points. Equation(2)
gives fdot=-df. Smoothness and gradTheta(z)=0 imply |Q|<=C|X-z|,
whereas |W|>=C^{-1}|X-z| on the local unstable curve. Thus f stays bounded
backward and its exponential ODE forces f=0. Formula(1) now gives Omega=0
on the entire unstable manifold as well. Theta also vanishes on the stable
manifold, by bounded forward transport.

At the saddle, the degree-one and degree-two temperature weights are
-nu,mu and -2nu,2beta,2mu. None is c, so gradTheta=D2Theta=0. Differentiating
the vorticity equation gives (M^T+I)gradOmega=0. Hence gradOmega=0 unless
nu=1; in that exception it may be a stable covector. The exact local
coupled example

    W=(-x,(2beta+1)y+alpha x^2), Theta=0, Omega=-2alpha x

has divW=2beta, -curlW=Omega, and both transport equations. It confirms
the exception, but violates the global center normalization and tail.

For completeness, let W_j,P_n,Q_n be homogeneous Taylor pieces of W,
Theta,Omega at the saddle, with W_1=MY and L_M=(MY).grad. Degree matching
in the actual physical derivative x gives

    (L_M-c)P_n=-sum_{j=2}^n W_j.grad P_{n-j+1},
    (L_M+1)Q_n=partial_x P_{n+1}
                         -sum_{j=2}^n W_j.grad Q_{n-j+1},
    div W_j=0 (j>=2), Q_n=-curl W_{n+1}.              (4)

If Theta is nonflat, its first piece is C s^i u^j with i>=2,j>=1 and
j mu-i nu=c. Distinct monomials of a fixed degree have distinct weights.
Vanishing on the stable curve removes j=0, and vanishing of the function
and gradient on the unstable curve removes i=0,1. Straightening those
curves does not change the leading homogeneous piece. At degree3 only
s^2u is possible, with nu=beta+2,mu=3beta+2. No stronger jet exclusion
is inferred from these recurrences.

## 6. Source alternatives and a smooth weak eigenfunction

At a hyperbolic source write the real eigenvalues as0<mu1<=mu2, with
mu1+mu2=2beta. A scalar eigenfunction of weight c that is flat at the
source vanishes on its basin. Indeed the negative flow contracts at any
fixed rate a<mu1 in an adapted norm. Flatness of order N and transport give

    |Theta(Y)|<=C_N e^{(c-Na)t} ->0

for Na>c. If Theta is nonzero there, it has a first nonzero Taylor term.
Since mu2>=beta>c, its weight can only be k mu1=c, k a positive integer,
and its leading term is C times the kth power of a weak left eigenvector.
In particular the two eigenvalues are distinct.

A smooth weak eigenfunction exists without smooth linearization. Translate
the zero to0, write W=MY+N(Y), and let L be a weak left eigenvector and
n=LN. On a small backward-invariant neighborhood set

    zeta(Y)=LY-int_0^infinity e^{mu1 t}n(phi_{-t}Y)dt. (5)

Choose mu1/2<a<mu1. The negative flow and every fixed finite-order initial
point derivative are O(e^{-at}), uniformly on a smaller neighborhood.
For the first derivative this follows from the variational equation in
an adapted norm. Higher derivatives solve the same homogeneous linear
system, with sources consisting of products of at least two lower-order
flow derivatives; convolution proves the same bound by induction. Since
n=O(|Y|^2), Dn=O(|Y|), every derivative of n(phi_{-t}Y) is O(e^{-2at}).
Thus(5) converges in every Ck. It equals the limit of
 e^{mu1 t}L phi_{-t}Y, so W.grad zeta=mu1 zeta and Dzeta(0)=L.

Subtract C zeta^k from Theta to cancel its first term. Any remaining first
term would again have weight c, whose only possible monomial is the already
canceled weak kth power. The difference is flat and hence zero. Extend
zeta to the whole basin by its transport law, using one sufficiently large
negative entrance time locally. The construction is smooth and independent
of the chosen time. The weak eigenfunction with a specified differential
is unique by the same Taylor and flatness argument at weight mu1.

Therefore a source is either live with Theta=C zeta^k, mu1=c/k, C!=0,
or has Theta=Omega=0 on its basin, the latter by(1). At an axis source DW is diagonal by W1 odd and W2 even in x.
The weak direction must be transverse, since otherwise its leading term
would be a nonzero multiple of (y-y_source)^k on the axis, contradicting
the explicit global condition Theta(0,y)=0. Normalize Dzeta=dx. Reflection and uniqueness
make zeta odd in x, hence k is even. For k=2 the eigenvalues are c/2,D/2
and Omega_x=4C/beta. No positivity is imposed on C at an additional source.

A source basin is simply connected and diffeomorphic to the plane: start
with a small outward disk and its boundary flow collar. Backward contraction
makes its forward images an increasing disk exhaustion of the basin; every
outside orbit crosses the original boundary exactly once, giving its
infinite cylinder collar. On a dead basin, curlV=divV=0. Integration of the
closed one-form gives V=grad h with Delta h=0, so W=grad H, Delta H=2beta.
All scalar derivatives vanish at its finite boundary by smoothness. Its
intersection with E is open and nonempty since K has area zero; scattering
there gives an open angular arc where both temperature and vorticity
leading coefficients vanish. This is compatible with nonzero coefficients
elsewhere and is not itself a contradiction.

## 7. Vanishing on every source-basin boundary

Let B be any hyperbolic source basin. Its boundary is invariant under the
complete flow. Suppose a boundary point P has Theta(P)!=0. Then
 det(W,Q)=cTheta is nonzero. The local Q-curve through P is a transversal
to W and contains points of B arbitrarily near P: use the local chart
(t,s)->phi_t(chi_s(P)) and the invariance of B to move a nearby basin point
to t=0. Choose such a point Y on a short segment. Equation(2) makes the
negative images of that segment have lengths at most C e^{-dt}.
Thus phi_{-t}P and phi_{-t}Y converge to the same source. This puts P in
the open basin, a contradiction. Hence Theta=0 on the boundary.

At a boundary zero, a nonzero temperature gradient would by(3) make it
a hyperbolic source. Its open local basin is either contained in B or
disjoint from B, both incompatible with being a boundary point. Thus its
gradient is zero. At a regular boundary point suppose Q!=0. The zero
level condition gives Q=fW and fdot=-df. For t>=0,

    W(phi_{-t}P)=f(P)^{-1}e^{-dt}Q(phi_{-t}P).        (6)

The right side is integrable because the negative orbit is bounded. Its
trajectory converges to a zero z on the boundary. Since Q(z)=0 and Q is
smooth, |Q(X)|<=C|X-z| near z. With
S(T)=sup_{t>=T}|phi_{-t}P-z|, integration of(6) gives
S(T)<=C'e^{-dT}S(T). For large T this implies S(T)=0, impossible for a
regular orbit. Therefore gradTheta=0 everywhere on the boundary, and(1)
gives Omega=0 there. No hyperbolicity of other zeros was used.

On the right part of B0, xi=sqrt(Theta/a0)>0; the preceding vanishing gives
its continuous extension by zero to the finite boundary. Smooth extension
of xi across that boundary is not asserted.

## 8. Why extra zeros require extra axis zeros

Assume the axis has no zero except0. Its two forward branches escape by
the scalar axis equation and the outward far field. Choose a small outward
disk about0. Every off-axis boundary point escapes because its nonzero
Theta on B0 makes it lie outside K. The two axis boundary points also
escape. For a large outward disk D_R containing Z, compactness of the
small boundary and continuity of the flow give one time T at which its
whole image is outside D_R; once outside D_R, it cannot return.

The image of the small disk is a topological disk containing0. Its boundary
misses the connected disk D_R, so D_R is entirely inside it. Every zero is
fixed by the flow, hence a zero in that image already lay in the original
small disk. Only0 did. Thus there are no other zeros. In particular the
origin plus an off-axis reflection pair, even a degenerate pair, is impossible.

## 9. Independent axis resonance and parity audit

Write b(y)=W2(0,y), f(y)=Theta_xx(0,y)/2 and g(y)=Omega_x(0,y). Exact
axis differentiation, using W1_x=2beta-bprime and the parity, gives

    b fprime=(2bprime-D)f,
    b gprime+(E-bprime)g=2f,                          (7)

with bprime(0)=D/2, f(0)=a0>0 and g(0)=4a0/beta>0.
Suppose s>0 is the first additional axis zero and bprime(s)=-nu<0.
The first equation gives f>0 on(0,s) and near s

    f=C_- |y-s|^n F(y), n=2+D/nu, F(s)>0,

where F is smooth, obtained by subtracting the simple pole of1/b in
f=C b^2 exp(-D int1/b). Smoothness and C_-!=0 force integer n and a nonzero
nth jet. Thus f continues nontrivially to the other side with sign(-1)^n.
There is a next zero z>s, since b is negative just beyond s and positive
far above. On(s,z) f never vanishes. If bprime(z)=0, then near z
fprime/f> D/(2|b|), whose integral diverges; |f| would be unbounded.
Thus kappa=bprime(z)>0. Its leading power at z is2-D/kappa, which must be
a nonnegative integer less than2. It is either0 or1. The first case is a
live quadratic source with kappa=D/2; the second is a saddle with
kappa=D and transverse stable exponent beta+2, and f has a simple zero.

The second equation(7), propagated forward from the original source,
gives g>0 on(0,s). Its integrating factor at s has power

    m=1+E/nu.

The coefficient of |y-s|^m is strictly positive: it is a positive initial
value plus a positive forcing integral. The integral converges since
n nu-(E+nu)=nu+beta+1>0. Smoothness forces integer m. On(s,z), g has the
same sign as f near z and then throughout the interval. At a source this
follows from g=4f/beta. At the other possible saddle, g(z)=0 because its
stable exponent beta+2 is not1, and differentiating(7) gives
E gprime(z)=2 fprime(z). Propagation toward s keeps that sign. The same
integrating-factor argument gives a nonzero leading coefficient at s
from this side. Smoothness therefore requires n and m to have the same
parity.

Let ell=n-m. Then ell is a positive even integer and

    (beta+1)/nu=ell-1,
    1/nu=2ell-m-1=:d_integer>0.

Hence nu=1/d_integer and beta=(ell-1)/d_integer-1, with ell-1>3d_integer.
For beta=p/q>2 in lowest terms, d_integer=r q and r(p+q) is odd. Thus p,q
have opposite parity and r is odd. Irrational beta and odd integer beta
are impossible for this nondegenerate first-axis-zero configuration.
If additionally Theta>=0 everywhere, f>=0, so n,m are even; this requires
p even and q odd. The negative-axis proof uses r=-y, btilde=-b(-r),
ftilde=f(-r), gtilde=g(-r); equations(7) remain identical. No horizontal
reflection was used.

These reproduce, in the new notation, the existing packet28/30 restrictions.
The tuples(4,1,16,10),(5/2,1/2,21,13),(8/3,1/3,32,20) are only arithmetic
resonances, not profiles. The middle tuple has a sign change in f.

## 10. The all-hyperbolic tree and propagation of flatness

If every zero is hyperbolic, compactness makes Z finite. Every point has
one zero as its backward limit, so the plane is the disjoint union of
source basins and unstable manifolds of saddles. A bounded forward orbit
outside Z approaches a saddle, hence belongs to a stable branch. Thus K
is the union of the zeros and the two stable branches of each saddle.
Every such branch connects two zeros. Its closure is an embedded arc,
with exponential, finite-length ends. A homoclinic arc or a cycle in the
resulting finite graph would give an invariant Jordan curve, impossible
by area expansion, or by the divergence theorem after deleting tiny
vertex disks. Those additional fluxes tend to0 since W=O(distance).
K is connected by Section3, hence this finite embedded graph is a tree.
With N_s sources and N_h saddles, it has N_s+N_h vertices and2N_h edges,
so N_s-N_h=1, also agreeing with the index count.

A basin boundary is a finite union of selected saddle unstable branches
and saddle vertices. Indeed it is invariant and meets no open source
basin, and each remaining point belongs to one of the finitely many
unstable manifolds. An entire connected branch is selected or excluded
by invariance. Saddle-to-saddle connections are allowed. Not every branch
of a boundary saddle need bound the same basin. Off-axis orbits in B0
escape by Section1: Theta=a0 xi^2 is nonzero there whereas Theta=0 on K.
Thus only its two axis branches can be bounded tree edges from0.

Here is the flatness-propagation lemma with its full hypothesis. If a smooth
F satisfies W.gradF=cF and an orbit converges exponentially to an equilibrium
at either time end, flatness of F at that equilibrium forces flatness at
every point of the orbit. For fixed N, the finite vector of derivatives
of F of orders at most N satisfies a homogeneous linear ODE along the
orbit: differentiation of the transport equation gives

    d/dt partial^alpha F=c partial^alpha F
       -sum_{0<delta<=alpha} binomial(alpha,delta)
          (partial^delta W).grad partial^{alpha-delta}F.

Every derivative of F has order at most |alpha|. On the whole compact closure of the convergent semiorbit
its coefficient matrix is bounded, say by M_N. Exponential orbit convergence
at rate a and flatness give a bound C_{N,L} e^{-La t} for any L, after
reversing time if necessary. The backward fundamental matrix bound is
at most e^{M_N(t-t0)}. Choose La>M_N and let t tend to infinity to force
the jet vector at t0 to vanish; linear uniqueness propagates it throughout.
This proves the lemma for every N.

Each tree edge converges exponentially to both hyperbolic endpoints.
Flatness at one end implies flatness along the edge and then at the
other end by continuity of every derivative. Connectedness propagates it
to0, contradicting Theta_xx(0)=2a0. Therefore Theta is nonflat at every
zero, and no source basin is dead. A configuration in which all additional
sources are dead is impossible. If the axis parity test fails, Sections8-9
force the global-source subclass when all zeros are hyperbolic; they do
not decide existence in that remaining subclass.

## 11. Limitations, counterexamples and audit scope

A dead source with degenerate zeros elsewhere is not excluded. Degenerate
approach can be slower than exponential, precisely the missing hypothesis
in Section10. Flatness cannot be used as an analytic continuation theorem.
For example the linear saddle W=-nu s partial_s+mu u partial_u has the
nontrivial smooth transported scalar

    T=u^{c/mu} exp(-1/(s^2 u^{2nu/mu})) if u>0 and s!=0,
    T=0 otherwise.

It is flat on both axes: on every compact rectangle the exponential
absorbs every inverse power arising from differentiation. The quantity
s u^{nu/mu} is invariant, so W.gradT=cT. This is not a coupled B2 solution,
since curlW=0 whereas its physical temperature derivative is generally
nonzero. It only refutes a transport-only flatness exclusion.

Likewise harmonic continuation from a dead region need not equal the given
smooth exterior field. The beta2 endpoint reflection obstruction used an
extra continued zero-arc mechanism, absent here. The canonical relative
kernel K(Z)=-JZ/(2pi|Z|^2) has the correct negative-curl convention and its
combined difference K(X-Y)-K(-Y) is absolutely integrable against the
O(r^{-1/beta}) tail. Local singularities are integrable; splitting at
|Y|~|X| gives O(r^{1-1/beta}) velocity. Its derivatives have changing signs,
so no unproved coercive constraint on a dead basin is claimed.

Every claim of the lead snapshot, including its local examples, source
normalization, index scope, boundary statement, axis continuation and
all-hyperbolic flatness improvement, has been independently checked above.
The exact state of the unrestricted smooth class remains OPEN. No new
profile or nonexistence endpoint is claimed. No formalization is supplied;
Lean and Lake execution is prohibited. Local stable/unstable manifold
existence and hyperbolic exponential convergence remain explicitly named
standard ODE dependencies, as in the source proof.

Actual second-model audit record: review48 returned a truncated usable Section3
audit only (188.871s, max_tokens). Review49 returned refusal/no text (14.652s).
Review50 (78.213s, end_turn) checked the source construction, and review51
(80.772s, end_turn) checked source boundaries and the hyperbolic tree/flatness
lemma. All returned model identifiers were claude-opus-5-5. Their actual
written suggestions were read, not inferred from summaries. Review50's
complex/Jordan-source suggestion is inapplicable: Section4 proves all spectra
real and semisimple using the coupled equations. A focused follow-up records
that counterargument. Definitions of V, the escape/bounded dichotomy and
the scattering submersion, and the off-axis escape dependency are explicit.
No unavailable or unsupplied portion of an answer counts as confirmation.

Follow-up52 (actual claude-opus-5-5,21.615s,end_turn) withdrew the complex/Jordan
objection. Its answer carelessly wrote zero of V and suggested M=DV; neither
notation is adopted. Throughout this proof z is a zero of W and M=DW(z),
so trM=2beta. Its core two-case linear-algebra check is correct. The source,
saddle and degenerate alternatives were always distinct in Section4.
Exact hyperbolic invariant-manifold source statements were read in the
saved Wiggins Section6 text; see packet53 verification source audit.
