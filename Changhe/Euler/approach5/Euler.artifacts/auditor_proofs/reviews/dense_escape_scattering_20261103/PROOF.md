# Dense escaping points force nonvanishing tail arcs and a stronger rate gap

Status: CONFIRMED in A516-A518 after complete independent reconstruction and full postread. This includes a target-range pressure proof independent of the auditor/LIT131 kernel split.

## 1. Exact settings and conclusions

Let U in C2(R3;R3),P in C1(R3) solve

    div U=0, LU+(DU)(Ay+U)+grad P=0,
    A=cI-omega J, L=(1-c)I+omega J,
    J(y1,y2,y3)=(-y2,y1,0).

Write B=Ay+U,W=curl U,a=1-2c,kappa=1+c,H=P+|U|^2/2+(Ay).U and g=U.B. Assume global zero helicity U.W=0. Let p0 be a vortical carrier equilibrium with real covector rate rho<-a, where A496 supplies rho<=-a generally. On its connected regular vortical H-level Sigma the confirmed A509 identities give a C1 function f with

    B cross W=f grad H, aU=(f-1)grad H,
    Bf=mu f, Wf=0, mu=-a-rho>0,
    dg=-(rho/a)dH, g=0.

The set Sigma^*=Sigma intersect {f!=0} is a nonempty C2 surface, and both B and W preserve it for finite flow times. A510 supplies its escape-versus-compact-critical-limit dichotomy. Its bounded alternative has unbounded full W-saturation.

There are two scopes:

(A) U=o(r) uniformly,0<c<1/2,every finite omega. Then the escaping points form an open dense subset of Sigma^*.

(B) U->0 uniformly,DU=O(sqrt r),1/3<c<1/2,every finite omega. In addition, the A210 tails V,W_* give E=-aV+Ay cross W_*. Every escaping point of Sigma^* has a limiting direction w with

    E(w)=0, V(w)!=0, Aw cross W_*(w)=aV(w)!=0,

and these directions contain a regular C1 arc tangent to the nonzero sphere field Y defined in Section6. If moreover 2/5<c<1/2, then rho<=-2(1-c). Thus in this strict target interval every vortical carrier equilibrium has rho=-a or rho<=-2(1-c).

A conditional consequence in scope(B) is that if Z_E={w in S2:E(w)=0} contains no regular C1 arc tangent to Y with Y nonzero, every vortical carrier equilibrium has rho=-a. This includes totally disconnected Z_E and Y=0 on Z_E. No global nonexistence, irrotational-equilibrium exclusion or periodic-witness exclusion follows.

## 2. Target-range pressure by exact vanished moments

This section does not use zero helicity or any equilibrium. For full C2/C1 profiles with U->0, DU=O(sqrt r), and 2/5<c<1/2, A498,A492,A476,A477,A210 give the uniform natural estimates

    |U|<=C(1+r)^(1-1/c), |DU|<=C(1+r)^(-1/c).

Set beta=2/c. In the strict target interval 4<beta<5. The full pressure equation is

    Delta P=h=-tr((DU)^2)=-D_ij(U_iU_j),
    |h(y)|<=C(1+|y|)^(-beta).

Thus h is continuous, integrable and has finite first absolute moments. Its zeroth and first moments vanish. To see this, test the last distributional identity against chi(y/R) and y_k chi(y/R). The constant and affine derivatives vanish inside the cutoff ball; the remaining terms are supported on its annulus and bounded respectively by

    C R^-2 integral_annulus |U|^2=O(R^(3-beta)),
    C R^-1 integral_annulus |U|^2=O(R^(4-beta)).

Both tend to zero. Dominated convergence on the h side yields integral h=0 and integral y_k h=0 for k=1,2,3.

Let N=-1/(4pi|x|). The absolutely convergent N*h is continuous and tends uniformly to zero. For example, split its integral into a fixed compact core, the ball of radius r/2 about an evaluation point |y|=r, and the remaining tail. The core is O(1/r); the near part is O(r^(2-beta)); the remaining tail is bounded by its vanishing L1 mass times a bounded separated kernel. Local boundedness of h handles the kernel singularity. Distributionally Delta(N*h)=h. A508 gives P->Hinf uniformly, so the entire harmonic function P-Hinf-N*h tends to zero and vanishes. Consequently

    grad P=grad N*h.

This gradient integral also converges absolutely, using the locally integrable |x|^-2 kernel and bounded h near each point.

For |y|=r large, split into I={|z|<r/2}, II={|z-y|<r/2}, and their complement. On I subtract the constant and linear Taylor terms of grad N(y-z). Their full h moments are zero; their omitted tails cost at most

    C r^-2 integral_(|z|>=r/2)|h|=O(r^(1-beta)),
    C r^-3 integral_(|z|>=r/2)|z h|=O(r^(1-beta)).

The Taylor remainder costs

    C r^-4 integral_(|z|<r/2)|z|^2|h(z)|dz
          <=C r^-4 r^(5-beta)=C r^(1-beta).

On II, |h|<=Cr^-beta and the gradient kernel integrates to Cr, giving the same bound. On the remaining region the kernel is at most Cr^-2 and the h mass is at most Cr^(3-beta), again the same. Hence

    grad P=O(r^(1-2/c)), P-Hinf=O(r^(2-2/c)).           (1)

The pressure rate follows by integration along rays and the known common limit. The exact linear-drift integration in the team records then gives

    U-V=O(r^(1-2/c)),
    H-Hinf-(Ay).V=O(r^(2-2/c)).                         (2)

The moment proof and the earlier proportional-radius kernel proof agree. The moments are justified directly; none is inferred merely from pressure decay.

## 3. A Baire argument makes escape open and dense

Work only in scope(A). Uniform sublinearity implies y.B>=c|y|^2/2 outside a fixed sphere. An unbounded forward orbit must enter this exterior and then escapes with increasing radius. By continuous dependence, this property is open in Sigma^*.

Suppose some nonempty relatively open O in Sigma^* consists of forward-bounded orbits. For each positive integer m let

    O_m={x in O:|Phi_t x|<=m for every t>=0}.

Each O_m is relatively closed, by continuity of each Phi_t, and their union is O. A surface is locally compact and hence Baire, as is its open subset O. Some O_m therefore has nonempty relative interior O'. Choose x0 in O' and s0>0 so that Gamma_s x0 belongs to O' for |s|<=s0. The W-flow is complete by A048 and preserves Sigma^* because WH=Wf=0 and regularity is preserved by its flow.

The exact flow commutation gives

    Gamma_s(Phi_t x0)=Phi_t(Gamma_(exp(-kappa t)s)x0).

For t>=0 and |s|<=exp(kappa t)s0, the right side has norm at most m. If k is any point of the compact omega-limit set K of x0, choose t_n tending to infinity with Phi_(t_n)x0->k. For each fixed real s, the displayed bound holds for all sufficiently large n, and continuity of the complete W-flow gives |Gamma_s k|<=m. Thus the full W-saturation of K is bounded. This contradicts A510 for x0 in Sigma^* with bounded forward orbit. No such O exists, proving density.

This argument uses no velocity decay, derivative bound, far-field pressure or local geometry of the entire unstable surface. It does not say that every point escapes.

## 4. Scattering of the flow and its derivative

Return to scope(B). Write Q_t=exp(omega tJ). For an escaping initial point x let y_t=Phi_t x. The natural velocity estimate gives

    d/dt log|y_t|=c+O(|y_t|^(-1/c)).

The preliminary exterior exponential lower bound makes the error time-integrable. Integrating therefore gives two-sided |y_t| asymp exp(ct). It follows that

    v_t=exp(-tA)y_t,
    v_t'=exp(-tA)U(y_t)=O(exp(-t)).

Thus v_t->v(x), v(x)!=0, with error O(exp(-t)). For

    M_t=exp(-tA)DPhi_t(x)

one has

    M_t'=exp(-tA)DU(y_t)exp(tA)M_t,
    ||exp(-tA)DU(y_t)exp(tA)||=O(exp(-t)).

Gronwall gives a bounded M_t converging at rate O(exp(-t)) to M. Liouville's formula gives det M_t=1 exactly, so det M=1 and M is invertible. These estimates are locally uniform on the open escaping set: nearby initial points enter the exterior at a common finite time, and the finite-time flow derivatives and exterior constants are uniformly controlled on a small compact neighborhood. Uniform convergence of the maps and derivatives implies v is C1 and Dv=M there.

Flow invariance of B and the bracket [B,W]=-kappa W give

    DPhi_t B(x)=B(y_t), DPhi_t W(x)=exp(kappa t)W(y_t).

Taking the scattering limits and using A210 yields

    M B(x)=Av(x), M W(x)=W_*(v(x)).                      (3)

For the second identity, exp(t)Q_t W(y_t) equals W_*(v_t)+o(1), by twisted homogeneity and the uniform vorticity tail. Since det M=1, (Ma) cross (Mb)=M^(-T)(a cross b), and hence

    Av cross W_*(v)=M^(-T)(B cross W)(x).                (4)

At finite time the same calculation gives the exact identity

    exp((1-c)t)Q_t(B cross W)(y_t)
                           =M_t^(-T)(B cross W)(x).     (5)

## 5. The transported Bernoulli gradient and its sharp remainder

Let Z(t)=exp((1-c)t)Q_t grad H(y_t). The Lamb identity and(5), together with the A210 velocity tail, show in the full scope(B) that

    Z(t)->-aV(v)+M^(-T)(B cross W)(x)=E(v).              (6)

In the strict target interval one also has |Z(t)-E(v)|<=C exp(-t). To prove this without assuming a derivative of the tail remainder, differentiate BH=-ag. Since DB^T=cI+omega J+DU^T and H-g=P-|U|^2/2, direct differentiation gives

    Z'(t)=a exp((1-c)t)Q_t grad(P-|U|^2/2)(y_t)
                               -Q_t DU(y_t)^T Q_t^T Z(t).

By(1) and the natural bounds, the first term is O(exp(-t)); the matrix coefficient of Z is also O(exp(-t)). The limit(6) already bounds Z. Therefore Z'=O(exp(-t)), and integration to infinity proves

    |Z(t)-E(v)|<=C exp(-t).                             (7)

No pointwise gradient asymptotic for V or pressure is used in this estimate.

## 6. Nonzero zero-set arcs, with exact projection

Take any escaping q in Sigma^*, whose existence follows from Section3. Along its orbit f(y_t)=exp(mu t)f(q). Since aU=(f-1)grad H and mu>0,

    |Z(t)|=a exp((1-c)t)|U(y_t)|/|exp(mu t)f(q)-1|
                        ->0.

The numerator is bounded and tends to a|V(v)|. Thus E(v)=0 by(6). Furthermore (B cross W)(q)=f(q)grad H(q)!=0. Equation(4) implies Av cross W_*(v)!=0, and E(v)=0 then yields aV(v)=Av cross W_*(v)!=0. In particular |V(v)| is strictly positive; this is the additional lower information absent from an upper-rate argument alone.

For y!=0 define sigma(y)=log|y|/c, pi(y)=exp(-sigma(y)A)y in S2. For w in S2 let

    Y(w)=W_*(w)-[(w.W_*(w))/c]Aw.

This is tangent to S2, and Dpi(w)h=h-[(w.h)/c]Aw. Let w=pi(v). Twisted homogeneity turns the preceding identities into E(w)=0 and aV(w)=Aw cross W_*(w)!=0, so Y(w)!=0.

For small s, Gamma_s q stays in Sigma^* and in the open escaping set. Therefore w(s)=pi(v(Gamma_s q)) lies in Z_E and obeys the same nonvanishing conditions. It is C1 because v is C1. At any such s, with eta=sigma(v(Gamma_s q)), equation(3) and projection homogeneity give

    w'(s)=Dpi(v)W_*(v)=exp(-(1+c)eta)Y(w(s))!=0.

It traces a regular C1 arc tangent to Y, after an optional positive reparametrization. Only continuity of Y is required; uniqueness for its integral curves is not assumed.

## 7. The stronger rate gap

In the strict target interval, the same escaping q satisfies |V(v)|>0. The exact expression for |Z(t)| in Section6 therefore supplies a constant C_q>0 and a sufficiently large time such that

    |Z(t)|>=C_q exp(-mu t).

But E(v)=0 and(7) give |Z(t)|<=C exp(-t). If mu<1 the two estimates contradict each other as t tends to infinity. Therefore mu>=1, equivalently rho<=-2(1-c).

Combining with A496, every vortical equilibrium either has rho=-a or has the stronger lower rate. No assumption that its own equilibrium vortex half-line escapes is needed: Section3 supplies escaping points on Sigma^*. Bounded orbits may still exist. They do not prevent this necessary rate conclusion.

## 8. Dependencies, independent comparison and limits

The geometry uses A048,A413,A468,A478,A496,A508-A510 and the exact bracket and Lamb identities. The far field uses the confirmed A498/A492/A476/A477/A210 chain. Section2 is an independent moment proof of the same target pressure and velocity remainder found in the auditor/LIT131 proportional-radius argument. The whole revised Theory Agent C C36 was read and compared step by step; its author is configured as model, with provider identity not independently attested. No computation was needed.

The former C36 singleton-component statement is retained in its pinned A512 version. This new proof supplies additional nonvanishing escape information, so its totally-disconnected criterion no longer needs A512's separate no-common-zero premise. That strengthening follows from Sections3-6, not by deleting a hypothesis from A512.

The source's extra estimates for c<=2/5 and its next-order cancellation discussion are outside this entry unless separately audited. In particular its suggestion that a leading pressure-gradient limit requires DU-DV convergence is not adopted here. No general E=0 tail, irrotational equilibrium, periodic flat witness, or unrestricted profile is excluded by the present result.
