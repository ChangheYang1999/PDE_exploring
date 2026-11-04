# The planar frequency identity and its continuation scope

Recorded: 2026-11-03T16:44:16.005276+00:00. Verdicts A1709-A1713. The actual 23-page manuscript of Yi Ru-Ya Zhang, *An Almgren-type formula for planar p-harmonic functions*, arXiv:2608.30847v1, was read in full. This is a verification of its displayed algebra and the scope of the cited continuation mechanism. It does not certify the external planar hodograph representation theorem anew.

## 1. Statement, notation and dependencies

Let 1<p<infinity and let u be a real p-harmonic function near x0 in R^n, n>=2. Put v=u-u(x0), A=|Du|^(p-2), D(r)=integral_Br |Du|^p, H(r)=integral_dBr A v^2, G(r)=integral_dBr A u_r^2 and K(r)=integral_dBr v^2 A_r. Whenever H>0 put N=rD/H and Theta=K/H-(p-2)(N-1)/r.

For the calculations below, assume the boundary flux, stationarity identity and derivative of H are justified at the radii in question. One sufficient local class is a smooth noncritical solution on the entire ball. Another is a punctured smooth solution with the nondegenerate quantitative homogeneous tangent specified in Section 3. The underlying p-harmonic equation is unweighted. The planar theorem additionally invokes the classical structure theorem quoted as Theorem 2.2 of the source.

## 2. Exact identity, with boundary terms accounted for

The flux identity is D=integral_dBr A v u_r. Stationarity gives D'=(n-p)D/r+pG. Differentiation of the sphere integral gives H'=(n-1)H/r+2D+K. Therefore

    N'/N = (2-p)/r+pG/D-2N/r-K/H.

Adding Theta gives N'+Theta N=pN(G/D-N/r). On expanding a square and using the flux identity, this equals

    (pr/H) integral_dBr A (u_r-Nv/r)^2.

The dimension has cancelled exactly. Multiplication by exp(integral_a^r Theta) gives a nondecreasing corrected frequency on any admissible annulus. Integrability of Theta down to zero is a further estimate needed for a finite, nonvanishing gauge at the center; it is not a consequence of writing this square.

For a critical homogeneous tangent of degree lambda>1, the inner flux at radius epsilon is O(epsilon^[p(lambda-1)+n]). The same exponent controls the inner stationary boundary terms. It is positive. Thus the punctured-ball derivation has no missing inner boundary term in the class of Section 3. At a noncritical center the calculation is classical. No such inner-boundary conclusion is silently asserted for an arbitrary degenerate weighted equation.

## 3. What proves the gauge estimate

Assume that a nonzero homogeneous p-harmonic function P of degree lambda>1 satisfies inf_S |DP|>0 and, uniformly on the unit sphere,

    |D^j v(r theta)-D^j P(r theta)| <= C r^(lambda-j+delta), j=0,1,2,

for some delta>0. Set alpha=p(lambda-1)+n>0. Polar integration gives D=D0 r^alpha(1+O(r^delta)) and H=H0 r^(alpha+1)(1+O(r^delta)), where D0,H0>0. These integrated estimates remain valid where P itself vanishes, because the error terms are estimated before integration. The homogeneous flux identity gives D0=lambda H0. Hence N=lambda+O(r^delta).

Moreover the gradient magnitude has the logarithmic derivative

    partial_r log|Du| = Du.D^2u theta/|Du|^2
                         = (lambda-1)/r+O(r^(-1+delta)).

Nondegeneracy of DP justifies division. Thus K/H=(p-2)(lambda-1)/r+O(r^(-1+delta)), and the two leading terms in Theta cancel. Consequently Theta=O(r^(-1+delta)) is integrable. This independently verifies the conditional higher-dimensional Theorem 5.3. Its Remark 5.4 can instead assume the corresponding C1 asymptotics plus the displayed weighted logarithmic-gradient estimate; that estimate remains an additional hypothesis.

In the plane, the source obtains these asymptotics, including the logarithmic derivative, from its quoted classical hodograph structure theorem. Its finite-order and unique-continuation corollaries use that same prior structure. The frequency calculation therefore does not supply an independent proof of finite order without this input. At a noncritical center, Taylor expansion gives N=1+O(r) and Theta=O(1).

## 4. Quantitative annular pinching

Let 0<a<b, Gamma_a(r)=exp(integral_a^r Theta), N_a=Gamma_a N, and suppose integral_a^b |Theta|<=eta, N_a(b)-N_a(a)<=epsilon. Integrating Section 2 gives the exact equality

    N_a(b)-N_a(a)
      = p integral_a^b Gamma_a(r) (r/H(r)) integral_dBr A(u_r-N(r)v/r)^2 dr.

Let R(a,b) be this integral without Gamma_a or p. Since exp(-eta)<=Gamma_a<=exp(eta), R<=exp(eta)epsilon/p. If N(a)<=Lambda, monotonicity and division by Gamma_a imply

    sup_[a,b] |N(r)-N(a)| <= exp(eta)epsilon+Lambda(exp(eta)-1).

For lambda=N(a), splitting u_r-lambda v/r into u_r-N(r)v/r and (N(r)-lambda)v/r, and applying (s+t)^2<=2s^2+2t^2, gives

    R_lambda(a,b) <= 2exp(eta)epsilon/p
       +2log(b/a)[exp(eta)epsilon+Lambda(exp(eta)-1)]^2.

This proves the source's annular estimate under its exact premises. None of these premises controls an unrelated unweighted logarithmic ratio energy.

## 5. The small positivity repair

The noncritical half of source Lemma 2.5 argues only that v cannot vanish on all small circles. The stated conclusion is positivity on each sufficiently small circle. It follows directly from Taylor expansion: if Du(x0)!=0, then v(r theta)=r Du(x0).theta+O(r^2), so v is not identically zero on any small sphere, while A is positive and bounded there. Alternatively, zero boundary values on any such ball and uniqueness of the p-Dirichlet minimizer force v=0 inside, contradicting the nonzero derivative. The critical case uses the already assumed isolated critical-point structure and the same Dirichlet uniqueness. This is a harmless proof repair, not a new counterexample to the frequency theorem.

## 6. Euler comparison and verdicts

The pending Euler question A1502 involves a coupled system whose scalar conductivity includes a variable ratio and geometric coefficients. The necessary nonzero finite-degree tangent or logarithmic-gradient estimate at a common flat orbit has not been established. The unweighted planar p-harmonic theorem does not cover this arbitrary coefficient. Importing its critical-point expansion would assume the sought finite-order conclusion.

A1709 CONFIRMED: exact flux-frequency identity and vanishing inner boundaries in the explicitly specified class, Section 2. A1710 CONFIRMED: conditional tangent-to-gauge implication and accurate external dependency scope, Section 3. A1711 CONFIRMED: annular pinching with its constants, Section 4. A1712 CONFIRMED: repaired positivity argument, Section 5. A1713 OPEN: any continuation conclusion for the actual coupled flat Euler system, Section 6.

All rotation rates remain admissible in the campaign's question, but this source supplies no new rotating-profile theorem. No computation, flow-completeness assumption, pressure normalization or formal build is used in this audit.
