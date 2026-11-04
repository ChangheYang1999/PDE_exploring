# Backward Bernoulli averages and vortex excursion flux

## Setting and claims

Let U in C2(R3;R3), P in C1 solve the full rotating profile equation, with div U=0, U bounded, 0<c<1/2 and arbitrary finite omega. Write A=cI-omega J, B=Ay+U, Omega=curl U, a=1-2c, b=1+c, q=|U|^2/2 and

    Ht=P+q+(Ay).U.

Let Phi_t be the complete B flow and psi_tau the complete Omega flow. Choose R1>2||U||_infinity/c and set D_t=Phi_t(B_R1). Then the following parts of Theory Agent A C18 hold.

1. Ht(y)=a integral_0^infinity exp(-as)(P-q)(Phi_-s y) ds. If U tends to zero and P tends to p_infinity, then Ht tends to p_infinity and (Ay).U tends to zero. If |P-p_infinity|+q<=C r^-gamma for gamma>0 outside a ball, then

       |Ht-p_infinity|+|(Ay).U|
          <= C'[r^-gamma+r^(-a/c)]

   for gamma unequal to a/c. At equality the bound is C' r^(-a/c)(1+log r). This part only needs C1 velocity.
2. The signed vorticity flux measure on every oriented C1 surface is multiplied by exp(-at) under Phi_t, including separately its positive and negative parts. In particular

       F_t=integral_boundary(D_t) |Omega.n| dS=exp(-at) F_0.

   This part holds for every c>0 if the global bounded-velocity vorticity equation is assumed.
3. The excursion-volume inequality and finite-return flux bound stated below hold. These are geometric consequences of incompressible vorticity flow and part 2, not an exclusion of a profile.

## Carrier geometry and the backward average

The radial component of B is cr+U.n. Thus B has linear growth, its flow is complete, and r increases strictly for r>=R1. Every backward orbit enters the closed R1-ball and remains there. D_s has closure contained in D_t for s<t; the D_t exhaust R3 as t tends to infinity. Solving the radial differential inequalities gives, on boundary(D_t), for t>=0,

    (R1-M/c)e^(ct)+M/c <= r <= (R1+M/c)e^(ct)-M/c,
    M=||U||_infinity.

In particular the lower radius is at least (R1/2)e^(ct). Statements about this expanding shell are for t>=0, not arbitrary negative t.

The exact momentum identity is Omega cross B=-aU-grad Ht. Dot it with B and use U.B=Ht-P+q. For f(s)=Ht(Phi_-s y) and g(s)=(P-q)(Phi_-s y),

    f'=af-ag.

The entire backward trajectory is contained in a compact set depending on y; f and g are bounded there. Multiplying by exp(-as), integrating to T, and sending T to infinity proves the claimed average with absolute convergence. No global pressure bound or normalization is needed.

For the limit and rate, let s0 be the backward entrance time into the R1-ball. For large y, exp(cs0) is comparable to |y| and, for 0<=s<=s0,

    |Phi_-s y| >= (R1/2) exp(c(s0-s)).

The integral after s0 is exp(-as0) times a uniformly bounded compact-core average. The integral before s0 tends to zero after subtracting p_infinity: split at s0-L, bound the first piece by the far-field supremum of |P-p_infinity|+q, and the second by C exp(-a(s0-L)). Take |y| to infinity then L to infinity. For a power bound the relevant convolution is

    integral_0^s0 exp(-as) exp(-c gamma(s0-s)) ds.

Its elementary evaluation gives the two powers, or s0 exp(-as0) at resonance. Finally (Ay).U=Ht-P-q. The pressure limit is an extra hypothesis, not a consequence of boundedness or decay used here.

## Exact signed and unsigned flux

The Cauchy formula is

    Omega(Phi_t x)=exp(-bt) D Phi_t(x) Omega(x),
    det D Phi_t=exp(3ct).

For tangent vectors v,w this gives

    det[Omega(Phi_t x),D Phi_t v,D Phi_t w]
       =exp((3c-b)t) det[Omega(x),v,w].

Therefore Phi_t^*(i_Omega vol)=exp(-at)i_Omega vol. With the transported orientation the multiplier is positive, so the Jordan positive and negative parts of the surface measure scale separately. This proves part 2, including infinite fluxes when relevant. For the compact boundary of D_t all fluxes are finite.

## Excursion-volume inequality

Let N be compact with N contained in D_t and let Z be a Borel set outside closure(D_t). For p on boundary(D_t), let tau_N^plus(p) be the first positive psi-time reaching N, and tau_N^minus its backward analogue; assign infinity if absent. Let Fplus consist of boundary points whose backward trajectory meets N before meeting the boundary again, and let Fminus use the opposite directions. Define

    Tplus_Z(p)=integral_0^tau_N^plus(p) 1_Z(psi_tau p) d tau,
    Tminus_Z(p)=integral_0^tau_N^minus(p) 1_Z(psi_-tau p) d tau.

Let Z_N be the points of Z whose full vortex line meets N. Then

    |Z_N| <= integral_Fplus |Omega.n| Tplus_Z dS
             + integral_Fminus |Omega.n| Tminus_Z dS.        (1)

To prove this, take a point whose backward line meets N, choose its last N-contact before the point, and then the first boundary crossing after that contact. This represents the point as psi_tau p with p in Fplus and 0<tau<tau_N^plus. The opposite-direction construction covers the remaining points. The map (p,tau)->psi_tau p has absolute Jacobian |Omega.n|(p), because psi preserves volume. The area formula gives (1); it only needs a covering and may overcount. Boundary tangencies cause no gap: their flow images have zero three-dimensional measure by the same area formula, first for bounded tau and then by a countable union. Hitting sets and these integral domains are measurable for a continuous complete flow and compact N; bounded time pieces and compact parameter subsets suffice for the area formula.

Suppose, additionally, that an open Phi-invariant basin W is the union of complete vortex lines through a compact invariant set contained in N. If

    V1=|W intersect (D_1\D_0)|>0,

then invariance and constant divergence give |W intersect (D_(t+1)\D_t)|=exp(3ct)V1. Apply (1) to that shell and enlarge the integration sets to the full boundary. It follows that

    integral_boundary(D_t) |Omega.n|(Tplus_Z+Tminus_Z)dS
        >=exp(3ct)V1.

Together with F_t=exp(-at)F_0 this gives a flux-weighted mean at least (V1/F_0)exp(bt). Here F_0>0 follows from the positive shell volume and (1). Infinite occupation averages are allowed. The count does not require a far-field pressure limit or a rate for U.

The commutation identity Phi_t psi_tau=psi_(exp(bt)tau) Phi_t carries this inequality at time zero with core Phi_-t N to the inequality at time t with core N. Flux, occupation time and volume are multiplied by exp(-at), exp(bt) and exp(3ct), respectively, and -a+b=3c. Their exact compatibility shows that this scaling calculation supplies no contradiction.

## Counting returns to a transverse disk

Let Sigma be a compact C1 embedded disk transverse to Omega, with Omega.n_Sigma>0 including its boundary. Its flux measure is mu_Sigma=(Omega.n_Sigma)dS. For t large enough that Sigma is contained in D_t, let E_k(t) be the points whose forward vortex trajectory reaches boundary(D_t), with at most k further Sigma crossings before its first hit. Then

    mu_Sigma(E_k(t)) <= (k+1)F_t
                     = (k+1)exp(-at)F_0.                 (2)

Choose a uniform short flow box Sigma times [0,delta) inside D_t. Its volume over E_k(t) is delta mu_Sigma(E_k(t)). Represent each such point by its first future boundary hit p and its backward time from p. Along the backward trajectory from p, any Sigma crossing belonging to E_k(t) is among the last k+1 Sigma crossings before p. The permitted flow-box pieces thus occupy at most (k+1)delta of backward time for each p. Apply the volume-preserving flow-box Jacobian and divide by delta. As above, tangential-hit images have zero volume and can be discarded. This proves (2). For open disks use compact transverse subdisks and monotone exhaustion.

For a point with unbounded forward vortex trajectory, every sufficiently large D_t is eventually exited. The number of prior Sigma crossings is nondecreasing with t. The sets with that number bounded by k therefore have measure at most the limit of (k+1)exp(-at)F_0, which is zero. Taking all integers k proves divergence of the return count for almost every such point.

## Scope and limitations

The three substantive identities and inequalities in C18 are confirmed with the explicit positive-time shell and compact-transversal qualifications above. The argument only establishes compatibility of the stated flux and volume scalings. It does not prove a universal theorem that every possible use of flux, recurrence, decay or the full curl coupling must fail. No such completeness claim is supported by these estimates. A rate for pressure, a limit of pressure and the basic-attractor basin description remain separate assumptions where invoked.
