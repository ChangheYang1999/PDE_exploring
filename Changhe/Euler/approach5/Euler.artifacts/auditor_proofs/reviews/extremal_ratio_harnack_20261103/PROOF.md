# Extremal localization of global bounded-ratio rigidity

## 1. Exact setting

Fix 2/5<c<1/2 and any finite real omega. Let Jx=e3 cross x, A=cI-omega J, X(x)=Ax, a=1-2c, b=2(1-c), eta=a/b, m=1/c, tau=(m-2)/2 and theta=1/2-eta. Let V,S be smooth on D=R3 minus{0}, with div V=0, DV X=-((1-c)I+omega J)V, X.grad S=-bS, X.V=0 and curl V.grad S=0. Suppose |V|^2<=r_+|S| on the sphere for one finite r_+>0. Scaling carries this bound to D. Write N={V!=0} and R=|V|^2/|S| on N.

There is a global C1 potential phi with grad phi=|S|^(-eta)V, extended by zero on S=0, and X.grad phi=0. If V is nonzero, both extremal sets of phi have nonempty boundaries in D. At every point z of either boundary V(z)=S(z)=0, N accumulates, and the integral of R^(-tau) over N intersect B_rho(z) is infinite for every ball contained in D. Hence liminf of R through N at z is zero. A lower comparison in a neighborhood of the common zero set alone therefore forces V=0. If the pressure Poisson equation also holds with S=P2-|V|^2/2, it forces S=0. Smoothness, the global upper comparison and the stated transport identities are explicit extra hypotheses.

## 2. Removal using only the upper comparison

Put gamma=1-2eta=2theta. For beta_e=(S^2+e^2)^(-eta/2)V the differentiated first term is dominated componentwise by r_+^eta |V_i|^(-2eta)|D V_i|, and the second by eta sqrt(r_+)|S|^(theta-1)|DS|. The signed gamma roots of V_i and the theta root of |S| have locally integrable derivatives, indeed in L^t for 1<=t<1/(1-theta)=2(1-c)/(2-3c). This is the previously audited Ghisi-Gobbino smooth-root theorem; the complete removal proof in the team records was reread. On zero sets the classical derivatives vanish almost everywhere. Thus these bounds dominate D beta_e uniformly, and dominated convergence gives the weak derivative of the continuous limit beta; |beta|<=sqrt(r_+)|S|^theta also proves its continuity. No lower comparison has been used.

The identity grad(X.V)=-aV+X cross W, W=curl V, gives X cross W=aV. Triple products and the scalar transport give grad S cross V=(b/a)S W. Consequently curl beta_e=e^2(S^2+e^2)^(-eta/2-1)W. It tends to zero almost everywhere, including almost every point of S=0 where W=0. The derivative majorant gives convergence in L1 on compact sets. Hence beta is distributionally closed. Local mollified primitives and simple connectivity of punctured R3 give a global C1 primitive. Since X.grad phi=0, phi is constant on every complete linear-flow orbit; each orbit meets the unit sphere exactly once. Therefore its maximum M and minimum L are attained and are global.

On N direct exponent calculation gives V=q|grad phi|^(m-2)grad phi with q=R^(-tau). On its complement define q=r_+^(-tau). Then q>=r_+^(-tau)>0 and the same equality holds everywhere. Its flux is exactly the smooth vector field V even when q itself is not locally integrable. Thus its divergence is zero in distributions.

## 3. Elementary integrable-weight Harnack lemma

Let p>2, u nonnegative and C1 on B_(3rho) in R3, q>0 almost everywhere, q in L1 and q^(-1) in L^t, with t>2/(p-2), allowing t=infinity. Suppose div(q|Du|^(p-2)Du)=0. Then

    sup_(B_rho) u <= exp(C_(p,t) [mean(q) (mean(q^(-t)))^(1/t)]^(1/p)) inf_(B_rho) u,

where both means are on B_(3rho), and for t=infinity the second factor means ess sup q^(-1).

Choose a cutoff chi equal to one on B_(2rho), supported in B_(3rho), with |Dchi|<=C/rho. Test with chi^p(u+e)^(1-p). Tests are justified by approximation: q is integrable and u and its derivatives are bounded on the compact support. Young's inequality yields

    integral q chi^p |D log(u+e)|^p <= (p/(p-1))^p integral q |Dchi|^p.

For r=pt/(t+1)>2, weighted Holder gives

    ||D log(u+e)||_(L^r(B_2rho))
       <= C rho^(-1) (integral q)^(1/p) (integral q^(-t))^(1/(pt)).

For t=infinity take r=p with the evident supremum factor. Coarea selects sigma in(rho,2rho) whose sphere gradient L^r integral is at most rho^(-1) times the ball integral. The two-dimensional sphere Morrey inequality gives oscillation of log(u+e) on that sphere at most C rho^(1-3/r) times the displayed L^r norm. Since 3/r=3/p+3/(pt), the powers of rho cancel when integrals become means, giving precisely the stated dimensionless bound.

The weak maximum and minimum principles carry the sphere oscillation into B_sigma. For example test with (u-K)_+, with K slightly above the boundary maximum, so the test has compact support. It gives integral q|D(u-K)_+|^p=0; positivity of q makes the positive part constant and its boundary value makes it zero. The lower bound is identical. Approximation is dominated by q on a compact set, so coefficient regularity is unnecessary. Let K tend to the boundary maximum, then e tend to zero. This proves the lemma, including the conclusion u=0 on B_rho if it has an interior zero there.

## 4. Extremal boundary and infinite ratio integral

If V is not zero, grad phi is not identically zero, so M>L. The nonempty closed sets E_+={phi=M}, E_-={phi=L} are proper and invariant under every linear-flow map. Connectedness of D makes their boundaries nonempty; invariance of a set under a homeomorphism also preserves its boundary.

Let z be on the boundary of E_+. Since phi is differentiable and attains a maximum there, grad phi(z)=0, hence V(z)=0. If S(z)!=0, near z the equation is div(|S|^eta grad phi)=0 with a smooth positive coefficient. Its strong maximum principle makes z interior to E_+, a contradiction. Thus S(z)=0. If N missed some ball about z, grad phi would vanish on that ball and phi would be constant there, again a contradiction.

If integral_(B_rho(z) intersect N) R^(-tau) were finite, the extended q would be integrable on the whole ball and q^(-1)<=r_+^tau. Apply Section3 with t=infinity to the nonnegative solution M-phi. Its zero at z forces it zero on a smaller ball, contradicting boundary membership. The integral is therefore infinite at every scale. A positive lower bound on R near z through N would make that integral finite, so liminf R=0. Apply the same argument to phi-L at E_-.

## 5. Corollaries and pressure

Local integrability near every point of either extremal boundary contradicts Section4 if V is nonzero. In particular a lower comparison r_-|S|<=|V|^2 in a neighborhood of {V=S=0}, for one positive r_-, makes q bounded there and forces V=0. No lower comparison elsewhere is used.

With the Poisson equation, V=0 makes S=P2 harmonic. Twisted homogeneity gives |S(x)|<=C|x|^(-d), d=b/c in(2,3). Its Kelvin transform H(y)=|y|^(-1)S(y/|y|^2) is harmonic off zero and bounded by C|y|^(d-1). Its zero singularity is removable. On the entire space this is subquadratic growth, so the harmonic second derivative estimate on arbitrarily large balls makes D2H=0. Hence H is affine. The same bound at zero has order greater than one, forcing its constant and linear coefficients to vanish. Thus H=S=0. Without Poisson, V=0,S=-|x|^(-b/c) is an exact countertest to scalar vanishing under the reduced hypotheses.

## 6. Dependencies and limits

All three submitted sections and this six-section proof were read fully. The entire earlier bounded-ratio proof was reread, including its scalar-root input and topology. The new Harnack argument is proved above from Holder, the sphere Morrey inequality and weak testing; it does not invoke an unverified subsolution theorem. No numerical computation or formal build was used.

This does not derive the global upper comparison, k=0 or W.grad S=0, does not settle continuation at an arbitrary single flat point, and does not remove smoothness. The natural-regularity Poisson root removal previously used a lower comparison and cannot automatically be substituted here. Every finite omega is covered at the stated scope. Bare-decay nonexistence remains open.
