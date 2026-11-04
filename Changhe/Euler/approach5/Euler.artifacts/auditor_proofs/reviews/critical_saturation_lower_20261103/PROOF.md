# Compact critical carrier sets and the nonrotating restriction

Status: CONFIRMED in A511 after the complete independent proof and focused source comparison were postread. Only the compact critical-set package is treated here.

## 1. Exact hypotheses and conclusions

Let U in C2(R3;R3) and P in C1(R3) solve

    div U=0, ((1-c)I+omega J)U+DU(Ay+U)+grad P=0,
    A=cI-omega J, J(y1,y2,y3)=(-y2,y1,0), 0<c<1/2.

Assume omega is any finite real number, U=o(|y|) uniformly, and U.W=0 globally for W=curl U. Set B=Ay+U,a=1-2c,kappa=1+c,H=P+|U|^2/2+(Ay).U,g=U.B. Suppose K is a nonempty compact set invariant under the complete B flow for all real times, contained in Crit(H), and B cross W is nonzero on K. Then its full W-saturation N is unbounded. The additional premise K contained in Crit(g) is unnecessary for this assertion.

If omega=0, no such K exists at all. This second assertion requires only g=0 on K and B nonzero on K, together with compact full B invariance; it does not use helicity, the W flow, or hyperbolicity.

Consequently, in the helicity-free setting above, let p be a vortical carrier equilibrium with rho<-a as in A468. On the regular level component Sigma of A508 through p, any q with f(q)!=0 has an escaping forward B orbit when omega=0. Here f=(B cross W).grad H/|grad H|^2. For nonzero omega, the alternative of a bounded B orbit with unbounded critical W-saturation is not excluded. No bound on DU or decay of U is needed for these conclusions.

## 2. Completeness and the saturation

Uniform sublinearity bounds |B| by C(1+|y|), so the C1 carrier field has a complete two-sided flow Phi_t. The exact bracket [B,W]=-kappa W and the backward confinement furnished by uniform sublinearity imply completeness of W by A048. With Gamma_s its flow,

    Phi_t Gamma_s=Gamma_(exp(kappa t)s) Phi_t.

The Lamb identity and helicity imply WH=0. Therefore Gamma_s pulls back dH to itself and preserves Crit(H). It follows that N=union_(s in R) Gamma_s(K) lies in Crit(H), is W-invariant, and is B-invariant by the conjugacy. Every point of N has nonzero W by uniqueness, since this is true initially on K.

Suppose N were bounded. Its closure M would be compact and invariant under both complete flows. It avoids zero. Indeed, if zero is not critical this follows from M contained in the closed Crit(H). If zero is critical, the scalar product of grad H(0)=-aU(0)+U(0) cross W(0) with U(0) forces U(0)=0. The confirmed A478 origin theorem gives an irrotational neighborhood of zero. The nonzero-W set N, and hence its closure, avoid a smaller such neighborhood.

Thus M contradicts the compact critical-set obstruction A508/A510. For completeness, its reduction to A118 is: on Crit(H), aU=B cross W. The subset of M where B cross W=0 is compact and B-invariant by the exact transport of the two fields. There U=0, hence B=Ay, and a nonzero forward orbit has radius exp(ct)|y|. Compactness leaves only zero, already excluded. Therefore M is a compact full-B-invariant subset of Reg={B cross W!=0}. Its W invariance supplies a two-dimensional B/W plaque. A118 forbids such a plaque in a compact regular invariant set: local stable curves thicken it to an open set of bounded forward orbits, whereas div B=3c>0 forces every bounded-forward-orbit set to have zero volume. The complete product-box proof and exact C2 scope are in A508/A510. This contradiction proves N unbounded.

## 3. The exact radial identity and omega=0

On Crit(H), taking the scalar product of aU=B cross W with B gives g=0. More generally, on any point where g=0,

    |B|^2=(Ay).B=c y.B-omega(Jy).B,
    B(|y|^2)=(2/c)(|B|^2+omega(Jy).B).                 (1)

For omega=0, continuous nonvanishing of B on compact K gives b0=min_K |B|>0. Integrating (1) on the complete forward orbit of any point in K yields

    |Phi_t q|^2 >= |q|^2+(2/c)b0^2 t, t>=0.

This contradicts boundedness of K. No asymptotic boundary terms or pressure normalization enter this argument.

For omega!=0 the last term in (1) has no fixed sign. The algebraic illustration from the source is accurate: on y(t)=R(cos(omega t),-sin(omega t),0), take B=-omega Jy,U=-cy,W=(ac/omega)e3. Then B=Ay+U,g=0 and B cross W=aU. These are only values prescribed on a curve. They do not enforce W=curl U in a neighborhood, exact momentum, or the transport equation, so they are not an Euler counterexample.

## 4. Consequence for a lower vortical equilibrium

For rho<-a, the complete rank and transport argument of A510 supplies Sigma and f with Bf=(-a-rho)f. Every q in Sigma with f(q)!=0 either escapes forward or has a compact critical limit set K contained in Reg, with unbounded full W-saturation. This uses the uniform exterior inequality y.B>=(c/2)|y|^2 and the growth of f on a bounded orbit. At omega=0, Section3 rules out the compact alternative, so such q escapes. This is a conditional geometric statement, not nonexistence.

The source formulates a narrower application to S=W^u(p) minus a particular vortex line. This entry does not separately certify its global assertion that S is embedded and that f has exactly one complete vortex-line fiber at each value. Any point of S already known to belong to Sigma with f!=0 is covered by the result just proved. The source's escaping area law, properness theorem, polynomial jets and exact local existence question have separate scopes and are not audited here.

## 5. Dependencies and collaboration

Inputs are A048, A118, A413, A468, A478 and A508-A510 at their recorded scopes. The complete 113-line compact-critical-set source, full 74-line coordinator check, entire source question and the answer through its Q1 proof and radial example were read. The configured-model coordinator independently verified both submitted claims. The originating the external referee (a second model) of a second model failed and is not counted. No computation or formal build was used.
