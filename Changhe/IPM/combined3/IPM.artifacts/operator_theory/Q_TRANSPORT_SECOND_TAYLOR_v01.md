# Isolating the small fractional transport remainder

Status: proved exact decomposition and analytic bounds in explicit coefficient
norms. Numerical coefficient bounds and the remaining integer divergence-form
energy estimate are separate obligations.

The preferred third-Taylor prefactor is the sharper rational upper
51/1000 proved in the final section. The initial343/2000 bound below
remains valid but is not the strongest available value.

Set q=2+delta=21/10, delta=1/10, h=J^delta g, u=u*, S=Sym Du,
and define the nonunitary Fourier Wiener moment
\(M_s(v)=(2\pi)^{-2}\int|\xi|^s|\widehat v(\xi)|d\xi\).
This is numerically identical to the unitary convention in the finite-rank
agent's source-commutator note. Vector and tensor moments use their joint
Euclidean/Frobenius norm.

The exact second Taylor formula gives
\[
\boxed{[J^q,u\cdot\nabla]g
=-q\operatorname{div}(S\nabla h)
+\frac{q\delta}2\sum_{klj}(\partial_{kl}u_j)
\partial_{klj}J^{\delta-2}g+\mathcal R_{3,u}(\nabla g).}
\tag{1}
\]
In particular the integer divergence-form term is exact, with the correct
coefficient q, rather than an informal replacement of q by2.

To verify (1), the first Taylor term is
\(-q\sum\partial_k u_j\partial_{kj}J^\delta g\).
The second Taylor term is
\(-q\Delta u\cdot\nabla J^\delta g/2
+q\delta\sum\partial_{kl}u_j\partial_{klj}J^{\delta-2}g/2\).
Since div u=0, div S=Delta u/2. The Delta u terms cancel upon putting
the first term into divergence form. The remaining Fourier kernel is the
third Taylor remainder of the symbol m(eta)=J(eta)^q, multiplied by
i eta·uhat(zeta).

The full third directional derivative has bound
\[
\|D^3m(\eta)\|_{trilinear}
\le q\delta[3|\eta|J^{\delta-2}
+(2-\delta)|\eta|³J^{\delta-4}]
\le q\delta(5-\delta)J^{\delta-1}\le\frac{1029}{1000}.
\]
Thus, at fixed input eta, its third Taylor remainder r3 and its output
frequency derivative satisfy
\[
|r3|\le c3|\zeta|³,\quad
|\nabla_\xi r3|\le3c3|\zeta|²,\quad
c3=\frac{q\delta(5-\delta)}6=\frac{343}{2000}.
\]
Weighted Young convolution and ||Wv||<=||v||+2||xv|| therefore prove
\[
\boxed{\|W\mathcal R_{3,u}(\nabla g)\|2
\le c3[M_3(u)+2M_3(xu)+6M_2(u)]\,\|\nabla g\|2.}
\tag{2}
\]
The output frequency derivative acts on uhat or r3 and never differentiates
the input derivative i eta. Hence no hidden fourth moment is needed in (2).

The small local second term in (1) obeys
\[
\left\|W\frac{q\delta}2 D²u:D³J^{\delta-2}g\right\|2
\le\frac{q\delta}2\|W D²u\|infty,F\|J^{q-1}g\|2.
\tag{3}
\]
The exact joint Fourier tensor norm of D³J^(delta-2) is bounded by
J^(1+delta)=J^(q-1), which justifies (3) without summing its components
separately.

## Reuse of the actual source coefficient certificate

Let b=grad rho*. Write B_j=||D^j b||2 and X_j=||D^j(xb)||2.
The joint velocity multiplier has |m_U|<=1 and
\(\||\xi|D_\xi m_U\|_F=1\) away from zero. Consequently
\[
M_2(u)\le\tfrac12\sqrt{B_1B_3},\quad
M_3(u)\le\tfrac12\sqrt{B_2B_4},
\]
\[
\boxed{M_3(xu)\le\tfrac12
\sqrt{[X_2+(\sqrt2+1)B_1][X_4+(\sqrt2+1)B_3]}.}
\tag{4}
\]
Here M_j(v)<=sqrt(||D^jv||2 ||D^(j+2)v||2)/2 is the source agent's
proved homogeneous Wiener inequality. To check the coordinate bound,
xu=U(x rho*)+[x,U]rho*, and the commutator multiplier norm at derivative
order j is at most |xi|^(j-1). Also grad(x rho*)=xb+I rho*, giving
||D^j(x rho*)||<=||D^(j-1)(xb)||+sqrt2||D^(j-1)rho*||.
Apply this for j3,5 and add the commutator bound. All the derivatives in
(4) are precisely those already required for the source certificate.

These homogeneous manipulations are legitimate for the actual growing
background: all displayed derivatives are L2, by the verified finite source
form and gamma=1-1/c>0. Coordinate commutators are understood away from zero
frequency and by the corresponding actual decaying derivatives; polynomial
ambiguities have degree too low to survive these derivatives. Equivalently
one may truncate the coefficient physically and pass to the limit in every
displayed derivative seminorm.

## Outside-ball price

If Q(g)=||WJ^qg||>=M and ||g||<=R, interpolation yields
\[
\frac{|\langle W\mathcal R_{3,u}\nabla g,WJ^qg\rangle|}{Q(g)^2}
\le c3[M3(u)+2M3(xu)+6M2(u)](R/M)^{11/21}.
\]
The local term(3) has analogous rate
\((q\delta/2)\|WD²u\|infty(R/M)^{10/21}\).
These small fractional prices do not bound the first divergence-form term
in(1); its exact weighted integer-order energy still has to be related to
the pointwise principal matrix with an explicit remainder bound.

## Sharper third derivative supplied by the finite-rank agent and audited here

Let z be a unit direction, v=xi/J(xi), and t=v·z. Exact differentiation gives
\[
D³m[z,z,\cdot]=q\delta J^{\delta-1}
[2tz+(1+(\delta-2)t²)v].
\]
Since |v|<=1, its bracket norm² is at most
\[
1+(4+2\delta)t²+(\delta²-4)t^4
\le\frac4{2-\delta}.
\]
The last scalar polynomial is concave in t², attaining its maximum at
t²=1/(2-delta). Thus both the repeated third directional derivative and
the output-gradient Taylor remainder have the common bound
\(2q\delta/\sqrt{2-\delta}\). In(2) and its outside-ball version one may
therefore replace c3 by
\[
\boxed{c3=\frac{q\delta}{3\sqrt{2-\delta}}
<\frac{51}{1000}.}
\]
The strict rational comparison follows by squaring positive quantities:
(7/100)²<(51/1000)²*(19/10). The powers and all profile moment obligations
are unchanged. The two-term fractional transport price is now explicit
once the source derivative certificate and ||W D²u||infty are supplied.

## Passage to the actual growing velocity

The cutoff justification can be made explicit without multiplying an
undefined growing-coefficient transform. The actual u belongs to S^s,
s=1/c<1. For u_R=chi(X/R)u with a fixed smooth radial cutoff,
\[
\|D^j(u_R-u)\|2=O(R^{1+s-j})\quad(j\ge2),
\]
\[
\|D^j[x(u_R-u)]\|2=O(R^{2+s-j})\quad(j\ge3).
\]
Product differentiation proves these estimates on the cutoff annulus;
integration of the exact symbol decay proves the same tail estimates.
Thus M2(u_R-u), M3(u_R-u), and M3(x(u_R-u)) tend to zero by the
homogeneous Wiener lemma at derivative pairs(2,4),(3,5),(3,5).
The remainder estimate(2) itself does not require divergence freeness,
so it passes strongly in weighted L2 to a uniquely defined actual R3
operator.

For Schwartz g the full commutators and each local Taylor term also
converge distributionally, indeed after multiplication by any fixed
polynomial weight: the cutoff coefficient differences multiply rapidly
decaying inputs. The exact divergence-form rewriting for u_R has the
additional term(q/2)grad(div u_R)·grad Jdelta g. Its weighted coefficient
is O(R^(s-1)), hence tends uniformly to zero. The actual u is exactly
divergence free, so the limiting identity is precisely(1). This proves
the growing-coefficient estimate without a residual polynomial transform
ambiguity; the triple Taylor zero kills all possible lower polynomial
terms. The canonical whole-plane velocity convention is independently
identified in `CANONICAL_BACKGROUND_VELOCITY_v01.md`.
