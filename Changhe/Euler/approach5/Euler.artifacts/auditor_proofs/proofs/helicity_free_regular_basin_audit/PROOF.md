# Helicity-free regular basins: independent proof and source-scope audit

## 1. Exact theorem

Let 0<c<1/2, omega be any finite real number, J(x1,x2,x3)=(-x2,x1,0), A=cI-omega J, and let U in C2(R3;R3), P in C1(R3) solve

    (1-c)U + (Ay+U).grad U + omega JU + grad P = 0,
    div U=0,
    U(y)->0 as |y|->infinity.

Write B=Ay+U, Omega=curl U, a=1-2c, kappa=1+c, Phi_t for the B flow and Psi_t=Phi_-t. Let Lambda be a compact transitive locally maximal uniformly hyperbolic attractor for Psi, with B and Omega nonzero on Lambda. Use the regular-attractor conclusions proved in A115/A118: its open invariant basin V is the union of complete strong stable leaves through Lambda, and these leaves are complete Omega curves. Suppose U.Omega=0 on V.

Then H=P+|U|2/2+Ay.U is constant on V. In particular

    aU=B cross Omega,   U.B=0,   |U|=|B cross Omega|/a

on V. If such basins cover almost every point of {Omega!=0}, and helicity vanishes on each basin, then U=0. The same conclusion holds if helicity merely has one sign on each basin, with signs allowed to differ.

This is the B26 conclusion and the previously confirmed A291 theorem. It is C2 and retains the regular-basin and helicity hypotheses. It does not use the newer C-infinity coverage theorem. A308 does not automatically supply coverage by regular attractors.

## 2. Independent proof without an arithmetic alternative

The Lamb form gives

    aU+grad H=B cross Omega,
    BH=-a U.B,    Omega H=-a U.Omega.

The last equality makes H constant on every complete strong stable leaf in V. Fix a periodic point p of Lambda with period L. The union of strong stable leaves through the periodic orbit is its weak stable set and is dense in Lambda. The local-product proof is as follows: take a dense forward orbit, first near a prescribed target and later close to p; form the product of its later unstable plaque with p's center-stable plaque, then pull this product point back. Backward contraction along the unstable plaque places it near the target, while it remains in the periodic orbit's weak stable set. Local maximality keeps the product point in Lambda. This is the regular basic-set lemma proved in A267.

On a strong stable leaf through Psi_s p, constancy along the leaf gives

    H(Psi_(t+L)y)=H(Psi_(t+s+L)p)=H(Psi_(t+s)p)=H(Psi_t y).

Continuity and weak stable density give H composed Psi_L=H on Lambda, and the stable-leaf union extends this to V. Differentiate along B to get

    g(Phi_L y)=g(y),    g=U.B.

The energy theorem A052 under the actual decay hypothesis gives E(R)=integral_(|y|<R)|U|2<=C R^beta, with 0<=beta<1, unless U is already zero. At c=2/5 take beta=0; at c>2/5 take beta=5-2/c. Consequently, for every fixed rho>1,

    R^-3 integral_(R<|y|<rho R)|g|
       <= C_rho [R^((beta-1)/2)+R^(beta-3)] ->0.

Here |g|<=||A||rho R |U|+|U|2 and Cauchy-Schwarz supplies the first power. There is no pressure trace or unproved infinity boundary term.

A continuous Phi_L-invariant function on the invariant open V with these vanishing shell means must be zero. To prove this, if |g|>epsilon at one point, its open invariant superlevel contains an escaping ball D. The trapped set is bounded and null because its volume is multiplied by exp(3ct). With M=||U||infinity, radial comparison r'=cr+O(M) places Phi_(nL)D in ratio-five shells of radii rho_n comparable to exp(cnL), and its volume is C_D rho_n3. This gives a fixed positive lower bound for the corresponding normalized shell integral, a contradiction. This is A290's direct proof; only one shell subsequence is needed.

Thus BH=0 on V. H is constant on the periodic orbit, on its stable leaves, on Lambda by density, and on V by the stable-leaf union. The asserted algebraic consequences follow from grad H=0. A265/A266 give U=0 under the separate covering hypothesis. A283 changes the helicity sign assumption to vanishing because each V is open and invariant under the complete recurrent vortex flow.

## 3. The phase-based proof, conditional on its explicit phase premise

Assume the alternative used in B26: in the nonmixing case there is a continuous equivariant phase theta:Lambda->R/TZ whose fibers are closures of synchronized strong stable traces. Constancy of H on those traces gives H=phi(theta). The quotient-map property of theta gives continuity of phi, and the identity phi(theta(x)+t)=H(Psi_t x) gives phi in C1 and phi'=a g on Lambda.

Extend theta to V by the stable-leaf union. It is well-defined because two attractor points on the same leaf have the same phase. Carrier equivariance then gives phi'=a g on all V, with no regularity assertion about the extended phase needed.

If |phi'|>=2a epsilon on a phase interval of length ell>0, choose F_R=V intersect {R<|y|<2R}. A092 supplies |F_R|>=delta R3 for all sufficiently large R. Every phase spends at least ell units of time in the interval during [0,T]. Fubini therefore gives some t_R in [0,T] for which at least an ell/T fraction of F_R has |g(Psi_(t_R)y)|>=2epsilon. Liouville gives an image volume at least exp(-3cT)ell delta R3/T.

For large R, all these images lie in the annulus with radii R exp(-3cT/2) and 2R: use |U|<=M and r>=2M/c in the backward radial equation. On the image, |B|<=(2||A||+1)R after R>=M. Hence |U|>=2epsilon/((2||A||+1)R), and E(2R)>=C epsilon2 R. This contradicts beta<1 or bounded endpoint energy. All Fubini sets are measurable using g composed Psi_t, independently of any measurability concern about the extended phase.

Thus this conditional phase proof is correct. The exact original Bowen/Plante theorem supplying the phase alternative has not been independently obtained here. The existing coordinator answer records later attribution through Day arXiv:2501.15323v1, which is insufficient to certify the original statement at the requested basic-set scope. No successful new web retrieval was made in this audit. The unconditional theorem above does not need that external input. No verdict on an unspecified historical theorem number is inferred.

## 4. Equivalent helicity conditions

On V, the following are equivalent:

1. h=U.Omega=0;
2. H is constant on each vortex line;
3. g=U.B is constant on each vortex line.

The first equivalence is Omega H=-a h. Since [B,Omega]=-kappa Omega,

    Omega(BH)=B(Omega H)+kappa Omega H,
    Omega g=B h+kappa h.

Thus h=0 implies Omega g=0. Conversely Omega g=0 gives h(Psi_t y)=exp(kappa t)h(y). Every such future approaches the compact attractor and remains in a bounded set, where continuous h is bounded. Therefore h(y)=0. The differentiated identity is legitimate: the Lamb gradient is C1 when U is C2, so H is C2 despite only C1 pressure being stated initially.

## 5. Refuted overstatement of the energy input

B26 input I4 and Remark(d) quote Theorem A under boundedness alone. This is false. Fix any nonzero constant vector u. Then

    U(y)=u,
    P(y)=-[(1-c)u+omega Ju].y

is a smooth bounded exact profile for every c and omega, with zero vorticity. Its energy is E(R)=4pi|u|2 R3/3. It violates both the claimed subcritical vanishing and every quoted smaller growth exponent. Its harmonic linear pressure is permitted by the profile equation.

The actual energy theorem requires Hb: U is bounded and U(R.) tends to zero in distributions. Uniform decay implies Hb and is already assumed by B26, so this citation error does not invalidate B26's theorem. The repair is to include Hb in I4 and Remark(d). Do not silently normalize away the linear pressure in the counterexample.

## 6. Evidence and limits

A310 confirms the exact B26 conclusions, its helicity equivalence, and the phase-to-energy deduction conditional on the explicit phase premise. A311 refutes only the bounded-only formulation of the energy input. The immutable submitted file and hash are in the team records. No computation or formal build was used. This argument covers every finite omega but does not establish the helicity premise, general regular-attractor coverage, or the unrestricted Euler conjecture.
