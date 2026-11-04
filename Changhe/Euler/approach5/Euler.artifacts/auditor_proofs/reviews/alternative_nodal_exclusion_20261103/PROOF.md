# Alternative nodal exclusions and the closure repair

Status: CONFIRMED at the actual-profile scope below. The proposed weaker parallel criterion needs an additional closure premise and is not certified as stated.

## 1. Exact hypotheses and inputs

Fix 2/5<c<1/2 and omega in R. Let Jx=(-x2,x1,0), A=cI-omega J, a=1-2c, kappa=1+c and p=(1-c)/c. Suppose U in C2(R3;R3), P in C1(R3) satisfy

    div U=0,
    (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0,
    |U(x)|<=C(1+|x|)^(-p),
    |DU(x)|<=C(1+|x|)^(-p-1).

Set B=Ax+U, Omega=curl U and E=sym DU. Normalize by the actual pressure limit Pinf, and write

    H=P-Pinf+|U|^2/2+(Ax).U,
    Q=P-Pinf-|U|^2/2, g=U.B=H-Q, N=grad H.

These scalar functions are C2 by the equation. The B and Omega flows Phi and Gamma are complete. The first field has linear growth; the second is bounded and C1. Let K be the compact forward-bounded B core, let K_Omega consist of complete vortex lines contained in K, and put O=R3 minus K_Omega. The actual transported scalar L is C1 on O, not assumed defined on all R3.

Suppose M is a nonempty connected component of {L=0,dL!=0,Omega!=0}. The previously proved sheet theorem gives H=Q=g=0, dH=dL and dQ=0 on M, and

    U=bN, B cross Omega=fN, f=1+ab,

with one nonzero spatial constant b. Let nu be the two-form on M obtained by contracting Euclidean volume with N/|N|^2. Vorticity preserves nu. Pressure flatness A878-A881 gives D2Q=0 on the ambient closure of M and

    U.curl Omega=2|E|^2, U!=0 there.

The parallel case has b=-1/a, B=tau Omega, Omega.tau=kappa and the connected embedded curve P0={B=0} in M. The nonparallel case has the annular coordinates described in Section 5. The arguments below do not use A896 compactness or A897 exclusion as premises.

## 2. A weighted regular-zero area lemma

For any C2 scalar F on a neighborhood of a compact ball D,

    integral_({F=0,grad F!=0} intersect D)|grad F|dA<infinity.

Choose a nonnegative smooth cutoff chi equal to one on D with compact support in that neighborhood. Set psi_e(s)=sqrt(s^2+e^2). Integration by parts gives

    integral chi psi_e''(F)|grad F|^2
      =integral psi_e(F)Delta chi
       -integral chi psi_e'(F)Delta F.

The nonnegative left side is uniformly bounded for 0<e<=1. Indeed |psi_e'|<=1 and psi_e(F)<=|F|+e, while the other factors are bounded on a fixed compact set. On any compact portion of the regular zero surface, use F as a transverse coordinate. Since psi_e''(s)ds tends to twice the Dirac mass at zero, the local limiting measure is 2chi|grad F|dA. Exhaust the regular surface by compact patches and use the uniform bound, or equivalently use nonnegative compact test functions and monotone exhaustion. This proves the assertion even when the regular zero set is not proper.

This lemma gives an independent proof that a parallel M has an escaping point, without first assuming pressure flatness. Local regular H coordinates and the vortical rank identity give Q=phi(H), with one common C2 germ along M. Thus for a finite constant lambda,

    2|E|^2=U.curl Omega-lambda|N|^2 on M.

If M were contained in K, then U=-N/a and the area lemma would imply integral_M |U|^2|nu|<infinity. Take a compact arc sigma(r) in P0 and j(r,s)=Gamma_s sigma(r). Since tau=kappa s, this is an injective immersion; nu invariance gives j*nu=F0(r)dr wedge ds with F0 nowhere zero. Fubini yields a vortex line for which integral_1^infinity |U(j(r0,s))|^2 ds is finite.

On this line, compactness of K and B=kappa s Omega give Omega=O(1/s) and |d_s U|<=C/s. If |U| exceeded a fixed epsilon at arbitrarily large s, the derivative bound would keep it above epsilon/2 on intervals [s,(1+delta)s] of growing length, contradicting its finite square integral. Thus U tends to zero. The displayed pressure identity, N=-aU and bounded curl Omega imply E tends to zero; Omega tends to zero as well, so DU tends to zero.

The reparametrization y(t)=j(r0,exp(kappa t)) is a bounded nonconstant B orbit. Variation of constants and ||exp(-tA)||=exp(-ct) give

    y(t)=-integral_t^infinity exp((t-s)A)U(y(s))ds ->0.

Therefore U(0)=DU(0)=0. Near zero, |U(y)|<=c|y|/2, giving d_t|y|^2>=c|y|^2. A nonconstant forward orbit cannot approach zero under this inequality. This contradiction proves M is not contained in K. It is an alternative to the stronger already confirmed two-sided escape theorem.

## 3. The parallel tangent identity

On the parallel sheet put alpha=Omega.flat restricted to TM and R=U.curl Omega. Define

    Y=Omega cross U,
    T=Y+(2omega/kappa)U3 Omega.

The contraction and exterior derivative formulas are

    i_Y nu=b alpha, d alpha=(R/b)nu, div_nu Y=R.

Since U.flat restricts to zero on TM and B=tau Omega,

    (Ax).flat restricted to TM=tau alpha.

Its exterior derivative is -2omega(U3/b)nu. Thus

    Y tau+tau R=-2omega U3,
    T tau=-tau R,
    div_nu T=R+(2omega/kappa)Omega(U3).

On P0, tau=0, so T is tangent to P0. It is nonzero there since Y!=0 and Y is perpendicular to Omega. Also Omega tau=kappa. Hence [T,Omega]tau=kappa R on P0, and the Omega coefficient of that bracket in the basis (T,Omega) is R. Using nu(T,Omega)=b|Omega|^2 in the Lie derivative of nu gives

    T log|Omega|^2=2R+(2omega/kappa)Omega(U3).

The stated regularity suffices: the fields are C1, R=2|E|^2 is C1 on M, and T tau=-tau R and Omega tau=kappa are C1. The commutator identity holds distributionally for C1 tau and C1 fields and has continuous representatives here; no second derivative of Omega is needed.

At B=0, vorticity transport gives DU Omega=(I+omega J)Omega, so Omega(U3)=Omega3. With pressure flatness this becomes

    T log|Omega|^2=4|E|^2+(2omega/kappa)Omega3.       (1)

For the pointwise algebra choose the positively oriented orthonormal basis e1=Omega/|Omega|, e3=U/|U| and e2=e3 cross e1. Write d for the fixed rotation axis in this basis and o=|Omega|. The identities DB e1=kappa e1, (DB)^T e3=-a e3, tr DB=3c and curl B=Omega-2omega e_axis give

    DB=[[kappa,2omega d3,-2omega d2],
        [0,0,2omega d1-o],
        [0,0,-a]].

Consequently, for m_c=1+c^2+(1-c)^2,

    |E|^2=m_c+|Omega-2omega e_axis|^2/2.

Substitution into (1) and completion of the square give

    T log|Omega|^2
      =4m_c+2|Omega-(2-1/(2kappa))omega e_axis|^2
       +(8kappa-1)omega^2/(2kappa^2)
      >=4m_c>0.                                  (2)

This holds for every real omega, including zero.

## 4. A maximum argument repairs the domain issue

Because B=0 on P0, c|y|<=|Ay|=|U(y)| there. Thus its ambient closure C0 is compact. The relative-closure conclusion of A894, Section 2 of its proof, says

    q in C0 and Omega(q)!=0 imply q in P0.          (3)

This conclusion did not use compactness of P0 or the final regular-node exclusion. Its proof is worth recalling. The full vortex line through q stays in closure M. A bounded sign half, with covector rate -a, would have a first-order-flat endpoint by A658-A659. Pressure flatness on closure M excludes such an endpoint. Thus q belongs to O. Only now may continuity of L and dL be used to put q back in the same regular nodal component and hence P0.

The continuous function |Omega|^2 attains a positive maximum on C0, since it is positive somewhere on P0. A maximizing point q has Omega(q)!=0 and therefore belongs to P0 by (3). At this interior point of the curve its derivative along the tangent T must vanish. This contradicts (2). The parallel sheet is excluded.

This proof needs neither compactness of P0 nor completeness of the auxiliary T flow. The submitted referee instead used a finite-exit argument and took continuity of L at an ambient limit before establishing that the point belonged to O. That step was incomplete. Formula (3), or the maximum argument above, supplies the missing premise.

## 5. Annular circulation with explicit vortex-time cuts

For the nonparallel sheet use global coordinates j(theta,zeta), theta modulo T0, zeta real, with

    j_theta=B-kappa zeta Omega, j_zeta=Omega,
    j*nu=f dtheta wedge dzeta, f!=0.

Pressure flatness gives d alpha=(2|E|^2/b)nu. Let

    I(zeta)=integral_0^T0 Omega(j).j_theta dtheta.

Stokes on the compact cylinder segment gives

    (2f/b) integral_0^T0 integral_-R^R |E(j)|^2 dzeta dtheta
       =I(-R)-I(R).

The actual scattering map satisfies |Xi(y)-y|<=||U||_infinity/c. Scaling from the two compact zeta=+1,-1 circles gives |j(theta,+R)| and |j(theta,-R)| comparable to R^(c/kappa), uniformly in theta. Put r equal to either end radius. Natural decay yields |Omega|<=C r^(-1/c), while

    |j_theta|<=|B|+kappa R|Omega|<=C r.

Thus |I(+R)|+|I(-R)|<=C r^(-p), tending to zero. The nonnegative increasing strain integral must vanish; E=0 on M. On its periodic B cycle, however, the scalar vorticity equation gives

    integral_0^T0 e.Ee dt=T0, e=Omega/|Omega|.

This is impossible. More quantitatively, trace-free symmetry gives |e.Ee|<=sqrt(2/3)|E|, hence integral_cycle |E|^2 dt>=3T0/2.

There is also a convergent full-cylinder identity:

    2 integral Omega.E Omega dtheta dzeta
       =(1-c) integral |Omega|^2 dtheta dzeta>0.

Indeed B=partial_theta+kappa zeta partial_zeta and B|Omega|^2=2Omega.EOmega-2|Omega|^2. Integrating by parts gives coefficient 2-kappa=1-c. The ends vanish because |Omega|=O(|zeta|^(-1/kappa)) and 2/kappa>1.

## 6. Weaker sign premises and unresolved scope

For an annulus with the same geometry and vanishing end circulation, Delta Q>=0 on M suffices: d alpha=(2|E|^2+Delta Q)nu/b has one sign, and Stokes forces E=0. This is a valid conditional variant.

For the parallel branch the local identity becomes

    T log|Omega|^2=4|E|^2+2Delta Q+(2omega/kappa)Omega3.

Thus Delta Q>=0 on P0 gives the same local strict monotonicity. But the submitted statement that this sign premise alone supplies a weaker global exclusion omits the relative-closure or flow-completeness input. The repair (3) used pressure flatness on the entire closure M, not merely a sign on P0. The weaker parallel criterion is confirmed only if one separately assumes (3), compactness of P0, or completeness of the tangent flow within P0 with the necessary boundedness. Without such a premise it remains OPEN in this audit.

The pointwise triangular matrix is a consistent first jet. It is not a construction of a local helicity-free profile germ on an equilibrium arc. No actual critical-node exclusion follows. The full bare-decay conjecture remains OPEN.
