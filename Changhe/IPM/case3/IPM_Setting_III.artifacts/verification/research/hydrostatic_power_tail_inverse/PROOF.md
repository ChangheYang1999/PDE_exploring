# A power change of variable for the complete hydrostatic inverse

Result221, written 2026-10-21T12:44:06.601775+00:00 before code. This concerns the auxiliary hydrostatic operator, not the elliptic full-plane IPM inverse. Letg be a smooth finite Q density with even-x/odd-y parity, sublinear exponent0<p<1, and the formula and derivative bounds proved in [the independent hydrostatic evaluator](../independent_hydrostatic_evaluator/PROOF.md). For each fixedx its vertical tail obeysg_x(x,t)=O_x(t^(p-2)) andg_xx(x,t)=O_x(t^(p-2)), t->infinity. These statements follow by its smooth angular expansion at the vertical axis: evenness supplies the extra factorx/t in g_x, and differentiating twice gives the displayed Hessian decay. Gaussian manufactures below satisfy these bounds for every suchp.

For y>=0 define

 Phi(x,y)=int_0^y t*g_x(x,t)dt+y*int_y^infinity g_x(x,t)dt,
 V1=-int_y^infinity g_x(x,t)dt,
 V2=int_0^y t*g_xx(x,t)dt+y*int_y^infinity g_xx(x,t)dt.       (1)

Both tails converge sincep-2<-1. Differentiating the first formula, justified by smoothness and locally uniform tail bounds, givesPhi_y=int_y^infinity g_x, Phi_x=V2 and-Phi_yy=g_x. HenceV=(-Phi_y,Phi_x) is divergence free and is the canonical hydrostatic velocity. It hasPhi(x,0)=0 andPhi_y(x,y)->0 asy->infinity. For fixedx these conditions uniquely determinePhi: the difference of two solutions of-Phi_yy=g_x isA(x)y+B(x), and the two conditions forceB=A=0. Extension by parity gives the whole plane; in particularV1 is odd inx/even iny andV2 even inx/odd iny. This boundary normalization is specific to the hydrostatic auxiliary inverse, and must not be described as an independent wall condition in the original IPM problem.

LetP=1/(1-p), R>0. ForF equal tog_x org_xx, the change of variablet=R/u^P gives the exact identity

 int_R^infinity F(t)dt=P*R*int_0^1 F(R/u^P)*u^(-P-1)du.    (2)

Under the stated tail bound the new integrand is bounded nearzero, sinceP*(2-p)-P-1=P*(1-p)-1=0. It is absolutely integrable, so the substitution is justified by finite substitutions followed by dominated convergence. For finite Q densities, the map variablew is of ordert^(-1/P), so its tail expansion becomes an expansion in integer powers ofu; geometric corrections at fixedx occur in powersu^(2P). In the casesP=3/2 andP=2 used here,2P is an integer. This explains why(2) can be easier to integrate numerically than a linear reciprocal substitution, without asserting a rigorous error bound for a finite quadrature rule.

The implementation keeps the finite physical composite Gauss-Legendre cells of the earlier independent evaluator and integrates(2) with ordinary Gauss-Legendre nodes on(0,1). It does not cut off infinity, change the density, or add a linear velocity. SplitR, finite order and tail order are varied. Each finite approximation is empirical; the change of variables itself is exact.

## Manufactured comparisons

For g=y*(1+x²+y²)^b, b=(p-1)/2, putB=1+x². Direct differentiation gives

 gx=2b*x*y*(B+y²)^(b-1),
 gxx=2b*y*(B+y²)^(b-1)+4b*(b-1)*x²*y*(B+y²)^(b-2).

Integrating these derivatives in(1) yields

 V1=x*(B+y²)^b,
 V2=-int_0^y (B+t²)^b dt-2b*x²*int_0^y (B+t²)^(b-1)dt,    (3)

and int_0^infinity gxx(0,t)dt=-1. Formula(3) can be checked by differentiating iny and evaluating atzero. Its finite integrals are evaluated independently at high precision; this does not share the tail quadrature.

For g=y*exp(-x²-y²), (1) givesV1=x*exp(-x²-y²) andV2=(x²-1/2)*sqrt(pi)*exp(-x²)*erf(y). For g=x²*y*exp(-x²-y²), it givesV1=-x*(1-x²)*exp(-x²-y²) andV2=(1/2-5x²/2+x^4)*sqrt(pi)*exp(-x²)*erf(y). Differentiate the density twice inx and use int_0^y t²exp(-t²)dt+y*int_y^infinity texp(-t²)dt=sqrt(pi)*erf(y)/4 to obtain both formulas. The latter includes a nonzero angular harmonic and the first has a nonzero origin slope.

The tests use exact-axis and off-axis points, all sign parities, multiplep and both split/order changes. Agreement validates the implemented finite calculations at those points. It does not prove a uniform numerical error, an exact trial solution or either SettingIII endpoint.
