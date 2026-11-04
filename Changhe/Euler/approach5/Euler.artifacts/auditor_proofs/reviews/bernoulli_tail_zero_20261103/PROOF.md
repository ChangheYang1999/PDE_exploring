# A necessary zero of the leading Bernoulli gradient tail

Status: CONFIRMED in A509 after complete independent reconstruction and full postread of the configured-model source. This is a conditional restriction on vortical equilibria, not a nonexistence theorem.

## 1. Exact setting and conclusions

Fix 1/3<c<1/2 and any finite real omega. Let U in C2(R3;R3),P in C1(R3) satisfy

    div U=0, ((1-c)I+omega J)U+DU(Ay+U)+grad P=0,
    A=cI-omega J, J(y1,y2,y3)=(-y2,y1,0),
    U(y)->0 uniformly, |DU(y)|<=C0(1+|y|)^(1/2),
    U.curl U=0 everywhere.                                  (1)

Set B=Ay+U,W=curl U,a=1-2c,kappa=1+c,

    H=P+|U|^2/2+(Ay).U, g=U.B.

A498(B), A476 and A492 imply the Dini derivative condition. The exact A210 scattering theorem, with its checked distributional zero-background premise supplied by U->0, gives continuous V,W_* off zero with

    curl V=W_* in distributions,
    V(exp(sA)y)=exp(-(1-c)s)Q_s^T V(y),
    W_*(exp(sA)y)=exp(-s)Q_s^T W_*(y), Q_s=exp(omega sJ),
    U=V+o(r^(1-1/c)), W=W_*+o(r^(-1/c))                     (2)

uniformly at infinity. Define

    k(y)=(Ay).V(y), E(y)=-aV(y)+Ay cross W_*(y),
    pi(y)=exp(-(log|y|/c)A)y in S2,
    Z_E={w in S2:E(w)=0}.                                  (3)

Then k is C1 off zero, grad k=E, and there is a real Hinf with

    grad H=E+o(r^(1-1/c)),
    H-Hinf=k+o(r^(2-1/c)), P-Hinf=o(r^(2-1/c)).             (4)

For h=k restricted to S2, E(w)=0 is equivalent to h(w)=0 and grad_S2 h(w)=0. In particular Z_E is compact, and Z_E empty is equivalent to a bound |grad H(y)|>=epsilon r^(1-1/c) for all sufficiently large r and some epsilon>0.

Let p be a vortical carrier equilibrium, B(p)=0,W(p)!=0. A468 provides the real parameter rho with spec DB(p)={rho,kappa,-a-rho}. If rho!=-a, then

    H(p)=Hinf, P(p)-Hinf=|Ap|^2/2, Z_E is nonempty.         (5)

There is a more precise orbit dichotomy in Section5. Thus the additional hypothesis Z_E empty excludes both bad vortical-equilibrium ranges by forcing rho=-a. It does not exclude irrotational equilibria, flat periodic orbits or general profiles. Constants and error moduli need not be uniform in omega.

## 2. Regular level geometry, with exact dependencies

The following geometry holds under the wider hypotheses c in (0,1/2), global C2/C1 regularity, uniform U=o(r), and global U.W=0, without (1)'s derivative bound. We use the confirmed A413 rank identity dH wedge dg=0 on {W!=0}, A468 equilibrium spectrum and A478 irrotational neighborhood at any zero-velocity equilibrium.

At p, U(p)=-Ap!=0 and grad H(p)=-aU(p)!=0. Let Sigma be the connected component through p of {H=H(p),grad H!=0,W!=0}. In a regular chart, rank writes g=G(H) with G in C2. Hence on Sigma,

    g=0, dg=-(rho/a)dH.                                    (6)

The coefficient is constant along the connected regular level, evaluated at p. By scalar uniqueness for H'=-aG(H), transport of dH at rate rho and the nonvanishing-vorticity transport law, the complete B flow preserves Sigma for every finite time. This is the finite-continuation argument of A508, not an assertion that Sigma is closed.

The W flow is complete by A048. Its proof compresses any finite vortex time by a sufficiently long negative B time into a fixed small local vortex interval in a fixed compact ball containing the relevant backward B orbits, using Phi_t Gamma_s=Gamma_(exp(kappa t)s) Phi_t. It needs neither bounded DW nor bounded complete vortex orbits. Since WH=0, it preserves dH and {W!=0}; connectedness of each orbit therefore makes Sigma W-invariant too.

On Sigma put f=(B cross W).grad H/|grad H|^2. Both fields are tangent, so

    B cross W=f grad H, aU=(f-1)grad H,
    Bf=mu f, mu=-a-rho, Wf=0.                             (7)

The first two equations follow from tangency and grad H=-aU+B cross W. For the derivatives choose a local C1 vector field X with dH(X)=1. Then f=vol(X,B,W). Since div B=3c, [B,W]=-kappa W and dH([B,X])=-rho from (6), differentiation gives Bf=(3c-rho-kappa)f. Similarly div W=0, [W,B]=kappa W and dH([W,X])=0 give Wf=0: the bracket term is tangent to the level and its volume with B,W vanishes, including their dependent points.

If mu!=0, f is nonzero arbitrarily close to p on Sigma. Indeed DB(p) acts on T_p Sigma/span(W(p)) by mu. For any tangent v independent of W(p), DB(p)v-mu v is parallel to W(p), so

    D_v(B cross W)(p)=mu v cross W(p)

has nonzero normal component. This quotient argument does not require the two tangent eigenvalues mu,kappa to be distinct. By A496, rho<=-a always, so the case relevant to (5) has mu>0.

## 3. The leading scalar tail requires only continuous V and curl V

Differentiate (2)'s homogeneity distributionally. With X(y)=Ay,

    (X.grad)V=-(1-c)V-omega JV.

For a continuous vector field with distributional curl W_*, the elementary product identity gives

    grad(X.V)=A^T V+(DV)^T X
             =A^T V+(DV)X+X cross W_*.

It is valid in distributions since X is smooth and linear. As A^T=cI+omega J, substitution gives grad k=-aV+X cross W_*=E. The right side is continuous. Mollify on an arbitrary compact ball away from zero: the mollified gradients converge uniformly to E and the scalar functions to k, so the line-segment fundamental theorem implies k in C1 and grad k=E there. This supplies the claimed regularity without assuming derivatives of the angular tail.

Homogeneity and rotation covariance give

    k(exp(sA)y)=exp(-as)k(y), (Ay).E(y)=-a k(y),
    E(exp(sA)y)=exp(-(1-c)s)Q_s^T E(y),
    |E(y)|=r^(1-1/c)|E(pi(y))|.                            (8)

The exact Lamb identity and (2) show

    grad H-E=-a(U-V)+Ay cross(W-W_*)+U cross W
            =o(r^(1-1/c)).                                (9)

The last term has size O(r^(1-2/c)), which is smaller by r^(-1/c). Since 1-1/c<-1, the radial integral of the error is o(r^(2-1/c)), uniformly in direction. Great-circle arcs on a sphere have length at most pi r, so their oscillation tends to zero as well. Thus H-k tends to a unique constant Hinf with the stated error. Since k=O(r^(2-1/c)) tends to zero, H tends to the same constant. Subtracting k=(Ay).V from the definition of H gives

    P-Hinf=(H-Hinf-k)-(Ay).(U-V)-|U|^2/2
           =o(r^(2-1/c)).

This uses the actual pressure; no gauge is imposed.

For w in S2, Aw=cw-omega Jw. If E(w)=0, (8) gives h(w)=0 and its tangential gradient is zero. Conversely, if h(w)=0 and its tangential gradient vanishes, E(w) is radial, and (Aw).E(w)=c w.E(w)=0, so E(w)=0. Compactness and (8)-(9) prove the equivalence between Z_E empty and the exterior lower gradient bound. For the reverse implication, a zero w of E would make the ratio |grad H|/r^(1-1/c) tend to zero on exp(sA)w, contradicting that lower bound.

## 4. The bounded critical-saturation obstruction

We use the exact A508 consequence of A118: a nonempty compact subset of Crit(H), invariant under both complete B and W flows and avoiding zero, is impossible in the global helicity-free uniformly sublinear class. The reduction is short. Its W-zero subset and its B cross W-zero subset are B-invariant; there U=0 and the orbit is y'=Ay. Compact full invariance leaves only the origin, excluded by assumption. Thus the set lies in {B cross W!=0} and contains a full two-dimensional B/W plaque. A118, valid at C2 by A380, thickens this plaque by local stable curves into positive three-dimensional volume of forward bounded B orbits. Such volume is impossible when div B=3c>0. No local maximality is assumed.

If zero is critical, the identity grad H(0)=-aU(0)+U(0) cross W(0) implies U(0)=0 by scalar product with U(0). A478 then supplies an irrotational neighborhood of zero. Every nonzero-W orbit and its saturation avoid that fixed neighborhood. This is the origin-exclusion step needed below.

## 5. Exact orbit dichotomy and the zero-tail condition

Assume (1),rho!=-a, so mu>0 by A496. Choose q in Sigma with f(q)!=0, and let q_t=Phi_t q. Equations (2) and (7), with compact continuity inside a ball, give

    |grad H(q_t)|=|B cross W|(q_t)/|f(q_t)|
       <=C exp(-mu t)(1+|q_t|)^(1-1/c).                    (10)

Outside a sufficiently large ball y.B>=(c/2)|y|^2. Hence the forward orbit either escapes to infinity or remains bounded.

If it escapes, variation of constants gives a vector v with exp(-tA)q_t->v and

    |q_t-exp(tA)v|<=c^(-1) sup_(s>=t)|U(q_s)|->0.

The integral defining v converges since |exp(-sA)|=exp(-cs) and U is bounded. If v=0, this displayed bound would give q_t->0, contradicting escape; hence v!=0. Since pi is invariant under exp(tA) and continuous off zero, pi(q_t)->pi(v). Constancy of H on Sigma and H->Hinf give H(p)=Hinf. Divide (10) and (9) by |q_t|^(1-1/c) and use (8). It follows that |E(pi(q_t))|->0, so pi(v) belongs to Z_E.

If it remains bounded, its omega-limit set K is nonempty, compact and invariant under every finite B time. Equation (10) and (6) imply K is contained in Crit(H) intersect Crit(g) intersect {H=H(p)}. If W vanished at a point of K, transport and the critical Lamb identity would make its complete orbit satisfy U=0,y'=Ay. Compactness would force that point to be zero, excluded by Section4's irrotational neighborhood. Thus W!=0 on K and K avoids zero.

Let N be the full W-saturation of K. Both H and g are W-first integrals: WH=0 and -aWg=W(BH)=[W,B]H+B(WH)=0. Their differentials are preserved by the W flow. Thus N lies in Crit(H) intersect Crit(g) intersect {H=H(p)}, consists of vortical points and is B-invariant by conjugacy. If N were bounded, its closure would be compact and invariant under both flows. It avoids zero by Section4 when zero is critical, and by closedness of Crit(H) otherwise. Section4 gives a contradiction. Therefore N is unbounded.

For every sequence x_n in N with |x_n|->infinity, H(x_n)=H(p) and grad H(x_n)=0. The limits (4),(9) imply H(p)=Hinf and |E(pi(x_n))|->0. Every accumulating twisted direction belongs to Z_E, and the compact sphere supplies at least one such direction. Finally B(p)=0 gives U(p)=-Ap and H(p)=P(p)-|Ap|^2/2, proving (5).

## 6. Scope of the asymptotic conclusions

All directions above are pi(y), which compensates for rotation. Ordinary radial directions need not converge when omega is nonzero. On an escaping orbit, (10) and |q_t| comparable to exp(ct) also give

    |grad H(q_t)|=O(|q_t|^(1-(1+mu)/c)).

This faster upper bound alone is consistent with a zero of E. It does not close the escaping case. A further contradiction would need a specified nonvanishing lower term, a rigidity implication, or a different compatibility condition. Merely supplying an upper rate for the next term is insufficient.

For any vortex line in Sigma, f is a constant f0. If it has points x_n escaping to infinity and pi(x_n)->w, equations (2),(7),(9) give

    f0 aV(w)=(f0-1)(Aw cross W_*(w)).

In particular f0=0 forces W_*(w) parallel to Aw, and f0=1 forces V(w)=0. These are necessary tail identities, not existence assertions. Global helicity also gives V.W_*=0 by scaling (2). Consequently on k=0 where Aw cross W_*!=0, aV is a scalar multiple ell(Aw cross W_*), and E=(1-ell)(Aw cross W_*). This describes the zero set but supplies no reason it must be empty.

Dependencies are exactly A048, A118/A380, A210, A413, A468, A476, A478, A492, A496, A498 and A508, at their recorded scopes. The full Theory Agent C configured-model source and its comparison to A508 were read; configuration is not independent provider attestation. All displayed identities here are checked analytically. No computation, formal build, new model client, or numerical inference was used.
