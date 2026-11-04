# C1 convergence of natural rotating tails from a local derivative estimate

Status: CONFIRMED, A538. Independent complete reconstruction of LIT136, compared with the full existing configured-model Theory Agent C review.

## 1. Exact statement and scope

Let 2/5<c<1/2, omega be any finite real number, p=(1-c)/c, A=cI-omega J, L=(1-c)I+omega J, Q_s=exp(omega sJ), where J(x1,x2,x3)=(-x2,x1,0). Suppose U in C2(R3;R3), P in C1(R3), and

    div U=0, LU+DU(Ax+U)+grad P=0,
    |U(x)|<=C(1+|x|)^(-p),
    |DU(x)|<=C(1+|x|)^(-p-1).                       (1)

Let V be the actual locally uniform leading tail supplied by A210:

    u_s(x)=exp((1-c)s)Q_s U(exp(sA)x) -> V(x)

on D=R3 minus{0}. Then, for every finite q>3 and every compact K contained in D, the family u_s is uniformly bounded in W^(2,q) on a neighborhood of K for all sufficiently large s. The limit V belongs locally to W^(2,q) for every such q, and

    u_s -> V in C^(1,alpha)loc(D) for every 0<alpha<1.       (2)

In particular the actual vorticity tail is curl V and is locally Holder for every exponent below1. No C2 convergence is asserted. No helicity or symmetry is used. The prescribed natural full-gradient bound in(1) is essential to the proof; it is not inferred here from U->0. The confirmed A498/A476/A477 chain supplies(1) when U->0 and DU=O(sqrt r) in the target range. Constants may depend on c,omega, the compact set and finite preterminal C2 norms.

The proof below reconstructs LIT136 with a moving cutoff. It avoids both a time-dependent spatial dilation and any imported local Chae-Wolf continuation theorem.

## 2. Local Euler continuation with bounded velocity and full gradient

Here is the precise local lemma. Let v be a classical incompressible Euler solution on B(x0,R) times(t_*,T), with pressure C1 and with v continuous into W^(2,q) on every compact preterminal subinterval, where 1<q<infinity. Assume

    sup_(B(x0,R) times(t_*,T)) (|v|+|Dv|)<=M0<infinity.    (3)

Then v has a uniform W^(2,q) bound on B(x0,R/4) for all sufficiently late times. More generally every compact spatial subset of the open original ball has such a bound by a finite cover. The bound may depend on one finite preterminal W^(2,q) norm and on R,q,M0. This lemma only concerns a strictly interior region, so it assumes no boundary condition for the pressure or velocity.

Translate x0=0 and set M=1+M0. Choose a smooth nonnegative nonincreasing function eta of one real variable, with eta=1 on(-infinity,1/2] and eta=0 on[3/4,infinity). Choose t0<T so late that

    M(T-t0)<=R/8,

and put

    chi(x,t)=eta((|x|+M(t-t0))/R), t0<=t<T.               (4)

This is spatially smooth, including at x=0: near zero its argument remains below1/2, so it is constant there. It is supported in B(0,3R/4), equals1 on B(0,R/4), and its first two spatial derivatives are uniformly bounded independently of t. On its transition region,

    (partial_t+v.grad)chi
       =eta'((|x|+M(t-t0))/R)(M+v.x/|x|)/R <=0,          (5)

because M>|v| and eta'<=0. The same inequality is trivial where chi is constant. Thus localization contributes a favorable sign to the transport energy.

Write w=curl v and Z_i=partial_i w. In distributions, the usual Euler vorticity equation and its derivative are

    w_t+(v.grad)w=(w.grad)v,
    (Z_i)_t+(v.grad)Z_i
       =(Z_i.grad)v+(w.grad)partial_i v
                         -((partial_i v).grad)w.         (6)

The last term is the differentiated transport commutator and cannot be dropped. All terms on the second right side lie locally in Lq on a compact preterminal time interval. Let

    Y(t)=integral chi(x,t)^q |Dw(x,t)|^q dx.

Multiply the second equation in(6) by the components of chi^q |Dw|^(q-2)Dw and sum. Since div v=0, integration of the transport term, combined with differentiation of chi, gives the term

    integral (partial_t+v.grad)(chi^q) |Dw|^q dx,

which is nonpositive by(5). The first and third terms on the right in(6) are bounded by Cq ||Dv||infinity Y. The middle term is bounded by Holder's inequality. Consequently

    Y' <= Cq ||Dv||infinity Y
          +Cq ||w||infinity ||chi D2v||q Y^((q-1)/q).     (7)

The constants absorb the finite-dimensional summation of the tensor components. Both ||Dv||infinity and ||w||infinity are bounded by(3).

## 3. The cutoff elliptic estimate closes at the same norm

Set F=chi v and extend it by zero outside B(0,R). Its support stays strictly inside that ball. For a compactly supported W^(2,q) vector field, the whole-space second Riesz-transform estimate and the identity

    -Delta F=curl curl F-grad div F

give

    ||D2F||q <= Cq(||D curl F||q+||D div F||q).            (8)

Here no weighted singular-integral theorem is used. This is the ordinary estimate ||D2F||q<=Cq||Delta F||q, valid for1<q<infinity. Expand

    curl(chi v)=chi w+grad chi cross v,
    div(chi v)=grad chi.v.

All differentiated cutoff terms contain at most v or Dv, and fixed first or second spatial derivatives of chi. Their Lq norms are uniformly bounded by(3),(4). It follows that

    ||D2(chi v)||q <= Cq ||chi Dw||q+C,
    ||chi D2v||q <= Cq Y^(1/q)+C.                        (9)

The second line follows by expanding D2(chi v); the additional terms again contain only v,Dv and derivatives of chi. There is no unknown D2v norm on a larger ball in(9). Substituting into(7) gives

    Y'<=C(Y+Y^((q-1)/q))<=C(1+Y).                       (10)

The initial value Y(t0) is finite by the assumed preterminal regularity. Gronwall on the finite interval[t0,T) bounds Y uniformly. Equation(9), chi=1 on B(0,R/4), and(3) give the claimed W^(2,q) bound there. A finite cover proves the assertion on arbitrary compact spatial subsets.

The computation does not assume classical third spatial derivatives. On each compact preterminal interval, v is locally Lipschitz and Dw is continuous into Lq. Spatial mollification inside a slightly larger compact ball justifies the transport equation for the mollified tensor. The commutator between mollification and v.grad tends to zero in Lq: it is uniformly bounded by C||Dv||infinity||Dw||q; it tends to zero for smooth tensors by direct differentiation; approximation of Dw by smooth tensors and continuity of translations give the general statement. The compact preterminal bounds permit time integration and passage to the limit. Regularizing the norm by (|Dw|^2+epsilon)^(q/2) justifies the power test at zeros. Passing the two regularizations gives the integrated form of(7), which suffices for(10) and Gronwall. This also explains why no derivative of the pressure enters the local lemma.

## 4. Application to the actual rotating profile

Set physical time tau=1-exp(-s) and

    v(x,tau)=u_s(x),
    pi(x,tau)=exp(2(1-c)s)P(exp(sA)x).                    (11)

A time-dependent additive pressure constant is immaterial. Direct differentiation of(11), using the full profile equation, gives

    partial_tau v+(v.grad)v+grad pi=0, div v=0.

The full derivative transformation is exactly

    D_xv=exp(s)Q_s DU(exp(sA)x)Q_s^T.                    (12)

On a fixed compact annulus, the natural bounds(1) and c(p+1)=1 give uniform bounds for both v and Dv as tau tends to1. On every preterminal compact cylinder the explicit C2 profile scaling gives continuity into W^(2,q) for every finite q. The pressure is C1 and the velocity is classical there. Thus all assumptions of the local lemma hold on every ball whose closure avoids zero. A finite cover proves uniform W^(2,q) bounds on a neighborhood of any prescribed compact K contained in D.

Choose q>3. Morrey's inequality bounds u_s uniformly in C^(1,gamma) on smaller balls, gamma=1-3/q. For every alpha<gamma, compact embedding gives subsequential convergence in C^(1,alpha). The already known locally uniform velocity limit is V, so every such derivative limit is DV. It follows that the entire family converges in C^(1,alpha), since a sequence violating convergence would have a convergent subsequence with that same limit. Given any alpha<1, choose q>3/(1-alpha). Weak W^(2,q) compactness also puts V in that Sobolev space. This proves(2) at the stated scope.

## 5. Comparison and limitations

LIT136 uses F(y,t)=v((1+sqrt(-t))y,t) and a fixed cutoff, making its modified carrier outward on the transition annulus. Its differentiated vorticity equation has two copies of the dilation rate; both are needed. Its favorable term is (2q-3)hY for q>3. The moving cutoff in(4) instead gives the favorable transport sign directly and introduces no dilation terms. The same ordinary elliptic estimate(9) closes both arguments. I checked the source's differentiated commutator, pressure-free curl step, cutoff signs and powers; they agree with this independent derivation.

The shorter source observation from the already confirmed A477 proof also gives C1 convergence with a positive Holder exponent, because that proof bounds the physical vorticity Holder norm and the interior full-gradient Holder norm. The local lemma above supplies every finite q and every alpha<1 under the explicit natural bound. Neither route establishes a C2 limit, a differentiated first-remainder expansion, nor natural derivative control from mere velocity decay.

Dependencies: A210 for the existing C0 limit; the explicitly proved local continuation lemma; the ordinary whole-space Lq second Riesz-transform estimate; Gronwall; Morrey and compact embedding. No Chae-Wolf or weighted Harnack theorem is used. No computation was necessary. The complete source is pinned in the team records. The complete existing Theory Agent C focused review, configured with the primary model, was read and compared. It independently rederives the cutoff sign, differentiated transport, elliptic closure, scaling and compactness. Its open-ball precision point is incorporated. Provider runtime is not independently attested.
