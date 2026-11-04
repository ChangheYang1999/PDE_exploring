# Physical concentration sets for failure of derivative decay

Status: CONFIRMED at A605; the broader pointwise interpretation is OPEN at A606. Independent reconstruction of Theory Agent A C45. The global nonemptiness conclusions and the claims at an individual point are kept separate.

## 1. Statement and exact physical variables

Fix 0<c<1, any finite real omega, and T in R. Let J(x1,x2,x3)=(-x2,x1,0), A=cI-omega J, Q_s=exp(omega sJ) and T_s=exp(sA). Suppose U in C2(R3;R3), P in C1(R3) solve

    div U=0, (1-c)U+DU(Ay+U)+omega JU+grad P=0,
    U(y)->0 uniformly as |y|->infinity.

For t<T set q=T-t, s=-log q and

    y=T_s x, u(x,t)=q^(c-1)Q_s U(y),
    D_x u=q^-1 Q_s DU(y)Q_s^T,
    omega_phys(x,t)=curl_x u=q^-1 Q_s W(y), W=curl U.

All matrix norms below are operator norms. All limits defining sets are JOINT limits (x,t)->(x_*,T), t<T, with x_*!=0. Define

    Sigma_I={x_*: limsup q|D_x u|>0},
    Sigma_beta={x_*: limsup q^beta|D_x u|=infinity}, beta>=1.

Then each Sigma_beta is closed relative to R3 minus0, invariant under every T_sigma, and Sigma_beta is contained in Sigma_1, which is contained in Sigma_I. With beta0=1+c/2,

    DU fails to tend uniformly to0
      iff Sigma_I is nonempty
      iff Sigma_1 is nonempty
      iff Sigma_beta0 is nonempty.                    (1)

These are equivalences of NONEMPTINESS, not equalities of the sets.

If additionally, for some 0<alpha<1, N>=0 and finite C,

    [W]_(C^alpha(B(y,3)))<=C(1+|y|)^N for every y,

define Theta={x_*: limsup q^beta0 log(1/q)|omega_phys(x,t)|=infinity}, using only sufficiently late times q<1. Then Theta is also closed and invariant under every T_sigma, and

    Sigma_beta0 is contained in Theta,
    Theta is contained in Sigma_1,
    Theta is nonempty iff the conditions in(1) hold.   (2)

No statement says that every point of Sigma_I belongs to Sigma_beta0 or Theta. The divergence of a normalized limsup does not give a fixed additional power of time. The result is conditional on a hypothetical exact profile, not the construction or exclusion of a physical singularity.

## 2. Scaling and closedness of the sets

For any fixed real sigma set

    x'=T_(-sigma)x, q'=exp(-sigma)q, t'=T-q'.

Then s'=s+sigma and T_(s')x'=T_s x. Orthogonality gives

    |D_x u(x',t')|=exp(sigma)|D_x u(x,t)|,
    (q')^beta|D_x u(x',t')|
       =exp((1-beta)sigma)q^beta|D_x u(x,t)|.

The space-time map is a homeomorphism extending at t=T to x_*'=T_(-sigma)x_*. Multiplication by the fixed positive factor preserves an infinite limsup. This proves invariance for Sigma_beta. For Theta the extra logarithmic ratio is (log(1/q)+sigma)/log(1/q), which tends to1; the same argument applies.

An infinite joint limsup means that every sufficiently small space-time neighborhood has arbitrarily large values. If x_j in Sigma_beta tends to x_*!=0, choose in a 1/j neighborhood of (x_j,T) a point with q^beta|D_x u|>j. These points tend to (x_*,T), proving x_* is in Sigma_beta. The same diagonal argument proves closedness of Theta. For beta>=1 and q<1, q|D_x u|>=q^beta|D_x u|, which gives the inclusions in Section1. No closedness of Sigma_I is needed or asserted.

## 3. The nonemptiness equivalences

If DU->0, the physical formula gives q|D_x u|=|DU(T_s x)|->0 near each nonzero x_*, since |T_s x|=q^-c|x|->infinity. Thus Sigma_I is empty. Conversely if |DU(y_n)|>=epsilon>0 along |y_n|=r_n->infinity, choose

    s_n=log r_n/c, q_n=exp(-s_n), x_n=T_(-s_n)y_n.

Then |x_n|=1. Pass to a subsequence tending to x_* in S2. The corresponding joint normalized gradient is at least epsilon, so x_* lies in Sigma_I. This proves the first equivalence by scaling alone.

If DU fails to tend to0, the contrapositive of A498(B), with the stated uniform U->0 premise, says that no finite bound |DU(y)|<=C0(1+|y|)^(1/2) holds. Compact continuity therefore supplies r_n->infinity with

    r_n^-1/2 |DU(y_n)|->infinity.

Choose s_n,q_n,x_n as above. At these points

    q_n^beta0 |D_x u(x_n,T-q_n)|
       =q_n^(c/2)|DU(y_n)|=r_n^-1/2|DU(y_n)|.

After extracting a limiting point on S2, Sigma_beta0 is nonempty. The elementary inclusions Sigma_beta0 subset Sigma_1 subset Sigma_I give all of(1). A492 gives the same middle implication through global bounded-gradient exclusion but is not needed in this short proof. Nothing here puts the concentration supplied by A498 at a previously fixed point of Sigma_I.

## 4. The logarithmic local estimate and the vorticity set

Put w(y)=sup_(B(y,3))|W|, H(y)=[W]_(C^alpha(B(y,3))) and M_3(y)=sup_(B(y,3))|U|. The confirmed local div-curl estimate from A580 gives

    |DU(y)|<=C_alpha[M_3+w(1+log^+(H/w))],             (3)

with the zero-w term interpreted as0. Here is its analytic content. For a cutoff chi equal1 on B(y,2), supported in B(y,3), define V=curl(Gamma*(chi W)), Gamma=1/(4pi|x|). Then U-V is harmonic on B(y,2): its divergence is0, and its curl is the negative gradient of the harmonic function Gamma*(grad chi.W). Its derivative at y is bounded by C(M_3+w). The singular integral for DV has a degree-minus-three mean-zero kernel plus a bounded local term. Splitting at radius delta<=1 gives C_alpha H delta^alpha inside and C w log(3/delta) outside. Choosing delta^alpha=min(1,w/H) proves(3). This uses actual div U=0 and the actual identity W=curl U, not a global integrability assumption.

The polynomial bound on H and boundedness of U imply, for r=|y|>=2,

    |DU(y)|<=C[1+w(y)log(2+r)].                      (4)

If w>=r^-1 this follows from log^+(H/w)<=C+(N+1)log(2+r). If 0<w<r^-1, use w log^+(H/w)<=w log^+H+w log(1/w), with w log(1/w)<=1/e. This also proves(4); w=0 is immediate.

Let x_* belong to Sigma_beta0 and choose a sequence (x_n,t_n)->(x_*,T) on which q_n^beta0|D_x u| tends to infinity. Put y_n=T_(s_n)x_n and r_n=|y_n|=q_n^-c|x_n|. The factor |x_n| stays bounded above and below. Thus r_n^-1/2|DU(y_n)| tends to infinity, and(4) implies

    r_n^-1/2 log(2+r_n)w(y_n)->infinity.

Choose z_n in B(y_n,3) with |W(z_n)|>=w(y_n)/2. At the SAME times t_n set x_n'=T_(-s_n)z_n. Then |x_n'-x_n|<=3q_n^c->0, so x_n' tends to the same x_*. The physical vorticity formula and log r_n=c log(1/q_n)+O(1) prove x_* belongs to Theta. This is the first inclusion in(2), pointwise with its stated hypotheses.

For the other inclusion use |W|<=2|DU|. Since beta0>1,

    q|D_x u| >= (1/2)q^(1-beta0)
                [q^beta0 log(1/q)|omega_phys|]/log(1/q).

The factor q^(1-beta0)/log(1/q) tends to infinity. A sequence giving an infinite bracketed term therefore places the same point in Sigma_1. This proves Theta subset Sigma_1. Combining with(1) gives the nonemptiness equivalence. It does not give the reverse pointwise inclusion Theta subset Sigma_beta0; the logarithm prevents that inference from the curl bound alone.

## 5. What the physical interpretation does and does not establish

Since U->0, the normalized physical velocity q^(1-c)|u| tends to0 uniformly near every nonzero final point. If derivative decay fails, Section3 produces SOME nonzero point with an unbounded coefficient relative to q^(-1-c/2). Under the polynomial Holder premise Section4 also produces vorticity whose joint limsup exceeds q^(-1-c/2)/log(1/q) by unbounded factors. In particular its ratio to q^-1 is unbounded. No extra positive power beyond the displayed rates has been proved.

For an escaping B-orbit y(s), the physical particle path X(t)=T_(-s)y(s) has a nonzero vector limit v, by the bounded-velocity scattering formula; differentiating gives dX/dt=u(X,t). A profile ball of radius rho corresponds exactly to a physical ball of radius rho q^c. If DU is unbounded along this ONE orbit, v is in Sigma_1. If DU merely fails to decay along it, v is in Sigma_I; the global A498 argument may put its stronger concentration elsewhere. Thus a pointwise claim that every gradient concentration is never type I is not justified by the proved nonemptiness statements or the global A492 theorem.

If W=0 on B(y(s),rho) for a fixed rho>0 along an escaping orbit, div U=0 makes U harmonic there. The confirmed estimate A583 gives |DU(y(s))|<=3 sup_(B(y(s),rho))|U|/rho->0. Hence derivative growth on fixed-radius profile balls cannot stay wholly irrotational. This is a local mean-value argument, not a claim that an orbit without such irrotational neighborhoods must already exhibit a prescribed vorticity singularity rate.

The exact irrotational local example A582 with |DU|=2Y0 exp(cs) on an axial orbit converts to |D_x u|=2Y0 q^(-1-c). A profile tube of radius m/(4Y0 exp(cs)) has physical radius m q^(2c)/(4Y0). This narrow-tube local example has no globally decaying extension supplied and does not contradict Section3. Source remarks recalling other Euler blow-up constructions from memory are outside this audit and are not used as evidence.

Dependencies: A498(B), the confirmed local estimate underlying A580, A583 and the physical scaling identities. Every use keeps global C2/C1, 0<c<1, uniform velocity decay and the separate polynomial Holder premise where needed. No numerical computation is used.
