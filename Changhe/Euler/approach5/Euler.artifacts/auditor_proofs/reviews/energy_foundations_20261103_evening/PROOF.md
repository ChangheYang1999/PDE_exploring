# Repeated energy and pressure foundation audit

Status: CONFIRMED for the classical profile statements below. The separate weak-defect theorem retains its previously audited dependency and is not newly reproved here. Literature priority claims are outside this repeated mathematical verification.

## 1. Exact hypotheses and pressure gradient

Let 0<c<1, omega be any finite real number, Jx=(-x2,x1,0), A=cI-omega J, B=Ax+U. Assume U in C1(R3;R3), P in C1(R3),

    div U=0,  (1-c)U+DU B+omega JU+grad P=0,
    M0=sup|U|<infinity,  U(R.) tends to 0 in distributions.

The last two requirements are Hb; uniform velocity decay implies them. Put E(R)=integral_(|x|<R)|U|^2, alpha=5-2/c, g(R)=R^-alpha E(R), epsilon(R)=sup_(|x|>=R)|U(x)|. No derivative decay, pressure bound or pressure normalization is assumed.

With Gamma(x)=1/(4pi|x|) and T_ij=partial_i partial_j(-Delta)^-1, define the canonical pressure gradient by

    <G_k,phi>=-sum_ij integral U_i U_j T_ij(partial_k phi).

For a compactly supported smooth test, T_ij partial_k phi is locally L2 and has tail O(|x|^-4), hence is L1. Thus G is a well-defined distribution. The two rotational divergence terms cancel exactly, giving -Delta P=partial_i partial_j(U_iU_j); therefore each component of grad P-G is harmonic.

Set U_R(z)=U(Rz). Rescaled momentum gives

    grad P(Rz)=-(1-c)U_R-omega JU_R-(Az.grad)U_R-R^-1 div(U_R tensor U_R).

On a fixed test the last term and G(R.) are O(R^-1). The other pairings tend to zero by Hb. The same is true on translated tests phi(. - x/R), since their transformed tests converge in L1 and boundedness upgrades distributional convergence to convergence on every L1 test. The harmonic mean-value identity now forces (grad P-G)(x)=0 for every x. This eliminates nonconstant harmonic pressure ambiguity without an L-infinity estimate for a Riesz transform. An additive pressure constant remains harmless.

## 2. Annular decomposition and local energy equality

For A_R={R<|x|<2R}, split F_ij=U_iU_j at radii R/2 and4R. The local and inner pressures are T_ij applied to those compactly supported pieces. The exterior pressure is

    Pi3(x)=sum_ij integral_(|z|>=4R) [K_ij(x-z)-K_ij(-z)] U_i(z)U_j(z) dz,
    K_ij(w)=(3w_iw_j-delta_ij|w|^2)/(4pi|w|^5).

The difference kernel has an integrable |z|^-4 tail. Equality of pressure gradients gives P=p_R+Pi1+Pi2+Pi3 on B_(2R). Plancherel and the degree-minus-three and degree-minus-four kernel bounds give

    ||Pi1||2<=epsilon(R/2) E(4R)^1/2,
    sup_(A_R)|Pi2|<=(4/pi)R^-3 E(R/2),
    sup_(B_2R)|Pi3|<=(192/pi)R I(R),
    I(R)=integral_(|z|>=4R)|z|^-4|U(z)|^2
         <=4 integral_(4R)^infinity r^-5 E(r) dr.

The last integration by parts has a vanishing outer boundary because E(r)<=C M0^2 r^3; its inner boundary has the favorable sign.

Dot momentum with U. The Coriolis term vanishes, div B=3c and div U=0, so with q=|U|^2/2,

    (1-5c/2)|U|^2+div(qB+PU)=0.

On a sphere Jx is tangent. Consequently

    (cR/2)E'(R)+(1-5c/2)E(R)=-integral_(|x|=R)(q+P-p)U.n.

Every constant p cancels by divergence freedom, so it may be chosen independently on each annulus. Multiplying by the integrating factor yields

    g(R2)-g(R1)=-(2/c) integral_(R1<|x|<R2)
                  |x|^(-1-alpha)(q+P-p)U.(x/|x|).

No flux at infinity is discarded at this stage.

## 3. Finite energy-growth iteration

Write Phi(R)=integral_(A_R)|q+P-p_R||U|. Cauchy-Schwarz and the preceding pressure decomposition give

    Phi(R)<=epsilon(R)E(2R)/2+epsilon(R/2)E(4R)
      +C R^(3/2)E(2R)^1/2 [R^-3 E(R/2)+R I(R)].

If E(r)<=K r^mu for r>=1 with0<=mu<=3, this is at most C(M0 K+K^(3/2))R^mu. The last power before simplification is R^((3mu-3)/2), at most R^mu because mu<=3. Hence on any subinterval of [R,2R],

    |g(R2)-g(R1)|<=C R^(mu-1-alpha).

Summing inward dyadic shells when beta=mu-1-alpha>0 improves E(R) to O(R^(mu-1)); at beta=0 it gives O(R^(mu-1)(1+log R)); when beta<0, outward summation gives a finite limit L of g with error O(R^beta). Intermediate constants depend on K and mu. The final constants depend on c,M0,E(4), and do not require a bound on omega.

Start with mu=3, supplied by boundedness. If alpha<0, the finite reductions3,2,1,0, followed by the applicable dyadic case at0, force E(R) to tend to zero. Monotonicity gives U=0. If alpha>0, lower mu until mu-1<alpha; at equality absorb the logarithm in R^(1/4) first. The negative-beta case supplies L. Reapplying it with mu=alpha gives

    |R^-alpha E(R)-L|<=C/R,  L>=0.

If L=0, reapply with mu=alpha-1, then alpha-2 whenever nonnegative. A finite number of steps makes the energy exponent negative, hence U=0. Thus L>0 for a nonzero field.

Under uniform decay, the unsimplified flux bound with E=O(R^alpha) gives the stronger error

    |g(R)-L|<=C[epsilon(R/2)/R+R^((alpha-5)/2)]=o(R^-1).

In the target2/5<c<1/2, alpha lies in(0,1), so E(R)-L R^alpha tends to zero. Positive L still allows infinite total energy. This is not a contradiction or an unrestricted nonexistence proof.

## 4. The endpoint c=2/5

Here alpha=0. The iterations3,2,1 give E(R)=O(1+log R), then O(R^(1/4)); negative-beta summation makes E converge. A final mu=0 step yields the tail Tl(R)=integral_(|x|>R)|U|^2=O(R^-1).

Reusing the annular decomposition with exterior energy in the local and velocity factors gives

    Tl(R)<=C R^-1 Tl(R/2)+C R^(-5/2) Tl(R)^1/2.

The inner pressure uses total finite energy and the shell velocity norm; the exterior pressure uses I(R)<=(4R)^-4 Tl(4R). The dyadic sums converge absolutely. If Tl=O(R^-tau), this inequality improves tau to min(tau+1,(5+tau)/2). Four steps from tau=0 give tau=4. Young's inequality absorbs half of Tl on the right and leaves O(R^-5). This proves the stated endpoint without assuming finite energy at the start.

## 5. Shell, Lorentz and vorticity conclusions

Assume2/5<c<1 and let p*=3c/(1-c), so p*>2 and3(1-2/p*)=alpha. The energy limit gives

    R^-alpha [E(2R)-E(R)] tends to (2^alpha-1)L.

Consequently a zero liminf of the normalized shell energy implies U=0. The weak-Lp estimate integral_E |f|^2<=p*/(p*-2)|E|^(1-2/p*)||f||_(p*,infinity)^2 gives the weak-shell criterion. If U lies in L^(p*,q) for0<q<infinity, its exterior Lorentz norm tends to zero, giving this criterion. The same reasoning and Holder give vanishing for U in Lp,0<p<=p*; boundedness handles p<2.

Integrating r^-alpha dE(r) gives

    integral_(1<|x|<R)|U|^2 |x|^-alpha=alpha L log R+O(1).

Thus the borderline weighted integral forces L=0, whereas every additional positive power in the weight is integrable. A nonzero profile also has a positive multiple of R^(-(1-c)/c) as a lower bound for the supremum on every sufficiently large dyadic shell.

For the vorticity version assume Omega=curl U belongs to L^(3c,q),1<=q<infinity. To identify U with its Biot-Savart integral, split weak-L^(3c) Omega into its large and small values, which lie in Lp1 and Lp2 for1<p1<3c<p2<3. Hardy-Littlewood-Sobolev gives the two potentials in finite Lebesgue spaces. Their difference from U is harmonic; the same large radial average and Hb remove that harmonic remainder. O'Neil's convolution theorem then gives U in L^(p*,q), proving vanishing. The lower bound q>=1 in this vorticity statement is retained.

A power tail r^(-(1-c)/c) belongs to weak-Lp* but no finite-second-index L^(p*,q); the analogous vorticity model has power r^-1/c. These are function-space examples and linear tails, not constructed nonlinear profiles. Little-o pointwise critical decay implies the shell tests, but is incomparable with global finite-q Lorentz membership. The exact homogeneous-tail interior-energy matching C0=0 follows from the refined error only when c<3/5, as the current text now states.

## 6. Bounded background normalization

For a bounded classical profile without Hb, the divergence form of momentum makes grad P-G a tempered harmonic distribution, hence a polynomial. Rescaled momentum is bounded on every fixed test and G(R.) is O(R^-1), so that polynomial is constant, say g0. Every weak-star subsequential dilation limit v solves

    Mv+(Az.grad)v+g0=0,  M=(1-c)I+omega J.

Set b=-M^-1 g0 and w=v-b. Transport by the linear complete flow gives w(e^(tA)z)=e^(-tM)w(z). Since e^(-tM)=e^(-(1-c)t)e^(-omega tJ), essential suprema satisfy ||w||infinity=e^(-(1-c)t)||w||infinity, forcing w=0. Thus the full dilation limit is the unique constant b, not necessarily zero.

With z0=-A^-1 b, define W(y)=U(y+z0)-b and Ptilde(y)=P(y+z0)+(Mb).y. Substitution shows their carrier is Ay+W and they solve the same equation. Translation of L1 tests proves W satisfies Hb, so all preceding energy statements apply to W. If U decays, b=0. The subtraction and translation cannot be omitted for merely bounded profiles; nonzero constant solutions are otherwise immediate counterexamples.

## 7. Scope of this repeated check

All483 current Section2A lines and its full51-line difference from the previously read476-line section were read. The changes correctly distinguish intermediate constants, pointwise-to-shell implications, the restricted c<3/5 matching range and the already separately audited bounded endpoint caveat in Chae-Tsai. The canonical-pressure proof was reread in full this pass. The bounded-background argument is reproduced above and the current assembled version was fully read.

The weak-profile theorem W is a statement here with its separate previously confirmed proof A176-A177. Its zero-defect, nonnegative-defect and endpoint conclusions must retain their respective assumptions. This repeated audit does not manufacture a new proof of W or certify every literature priority statement in Section2.9. Named external inputs for the classical conclusions are Weyl's lemma, L2 multiplier bounds, Hardy-Littlewood-Sobolev and the stated O'Neil Lorentz inequality; all are used in their stated ranges.

The current classical pressure/energy proof and its corrections are confirmed. No global L2 bound is inferred in the target interval from uniform decay alone. Whole-assembly approval, derivation of extra tail or helicity conditions, and unrestricted nonexistence remain OPEN. No new computation or external-model execution was used.
