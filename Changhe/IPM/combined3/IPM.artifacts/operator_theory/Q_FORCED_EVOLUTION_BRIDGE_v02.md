# The forced-evolution bridge: no conditional high inverse is required

Status: proved analytic implication. The actual L2 rate, forcing bounds,
complete exterior-energy bound, and scalar inequality are numerical inputs
which must be certified before the existence conclusion is invoked.

This is the preferred bridge for the local Q-energy proof. It supersedes the
old-N Garding/matrix-margin lifting step in `Q_NORM_OPERATOR_BRIDGE_v01.md`.
It does not require any inherited compact-operator estimate, old high graph
witness, or separate frozen high-matrix certificate.

Fix a>0, q=21/10 and W_a=sqrt(1+a²r²). Put Q(g)=||W_aJ^qg||2 and
\[
\mathcal B=\{k\text{ real S1}:\|k\|2\le R,\ Q(k)\le M\}.
\]
The ball has no origin-strain hyperplane constraint. For each k define
\[
A_k=(cX+u_*+U[k])\cdot\nabla-1+b_*\cdot U,
\quad b_*=\nabla\rho_*.
\]
Assume the actual maximal L2 generator, as constructed from the complete
flow and bounded source perturbation, has
\[
\|e^{tA_k}\|_{L2S1\to L2S1}\le e^{-\beta_2t}
\quad(k\in\mathcal B),\qquad\beta_2>0.
\tag{1}
\]
This is precisely the independent actual L2 coercivity obligation. In
particular A_k has the actual inverse
\(-A_k^{-1}F=\int_0^\infty e^{tA_k}Fdt\) in L2.

Let ||F||2<=f2, Q(F)<=n, choose R>=f2/beta2, M>0, and suppose uniform
constants b>0,C>=0 have been proved such that, for every Schwartz k in B
and every Schwartz real S1 test g satisfying ||g||2<=R and Q(g)>=M,
\[
\Re\langle W_aJ^q A_kg,W_aJ^qg\rangle
\le-bQ(g)²+C\|g\|2².
\tag{2}
\]
The sufficient invariant-ball inequality is
\[
\boxed{bM²\ge nM+CR².}
\tag{3}
\]
The new local identity normally gives C=0 after its interpolation terms
are incorporated into b. The version here also permits explicit weak
prices to be kept separately.

## 1. Qualitative finite-time Q evolution for a smooth frozen input

The space Q is equivalent to the coordinate Sobolev space
\(\{g:g,xg,yg\in H^q\}\). The exact identity
\[
x_jJ^qg=J^q(x_jg)+q\partial_jJ^{q-2}g
\]
proves equivalence in one direction and its converse. Equivalently use the
smooth bounded frame (1,ax,ay)/W_a and integer H²/H³ product estimates,
followed by interpolation. No numerical norm-conversion constant is used.

For a Schwartz k the drift V_k=cX+u_*+U[k] is C-infinity, globally
Lipschitz, has at-most-linear growth, and has bounded derivatives of every
positive order. Its complete smooth flow Phi_t gives the transport group
\(S_tg=e^{-t}g\circ\Phi_t\). On each bounded time interval, Phi_t and its
inverse are bi-Lipschitz, their higher derivatives are bounded, and
W_a(X)/W_a(Phi_t(X)) and all needed derivatives are bounded. Integer
weighted H²/H³ chain/product rules and interpolation therefore give a
strongly continuous group on Q.

The source operator b_*·U is bounded on Q. Indeed the proved joint S1
velocity estimate, applied to Jqg, gives
\(Q(Ug)\le\sqrt3Q(g)\).
Multiplication by b_* is bounded on the coordinate Hq space, since b_*
and all of its derivatives are bounded. The component parities sum to S1.
Thus the bounded perturbation theorem produces a C0 semigroup on Q with
generator A_k. Its transport flow and source operator coincide with their
actual L2 versions, so the Dyson expansion identifies the Q semigroup with
the restriction of the actual L2 semigroup on every finite time interval.

Smooth compactly supported S1 functions form a Q-generator core. For the
transport generator this can be seen without a pseudodifferential domain
claim: the dense compactly supported smooth space is flow-invariant.
Apply a resolvent with real lambda larger than the group growth rate,
approximate its input by that space, and truncate its time integral. Each
truncated integral has compact support and is smooth; its graph error is
the exponentially vanishing terminal orbit. The bounded source perturbation
preserves the generator domain and this core. In particular the real
quadratic energy extends from the core in its Q graph norm.

## 2. The forced trajectory stays inside the ball

For smooth k in B set
\[
g(t)=\int_0^t e^{sA_k}F\,ds.
\]
Since F belongs to Q and the semigroup is C0 there, g(t) belongs to the Q
generator domain, is C1 as a Q-valued map, and solves
\(\partial_tg=A_kg+F,\ g(0)=0\).
The actual L2 bound(1) gives
\[
\|g(t)\|2\le(f2/\beta_2)(1-e^{-\beta_2t})<R
\quad(t<\infty),
\]
unless f2=R=0, in which case g=0 and there is nothing to prove.

On any open interval where Q(g(t))>M, approximate g(t) in the Q generator
graph norm by core functions. The strict inequalities Q>M and ||g||<R
hold eventually for these approximants, so(2) passes to g(t). Hence
\[
\frac12\frac d{dt}Q(g(t))²
\le-bQ(g(t))²+nQ(g(t))+CR²<0.
\]
The final strict sign for Q>M follows from(3), since the upward quadratic
bz²-nz-CR² has its nonnegative root at most M. Continuity and the initial
value zero now prevent a first crossing of M. Thus
\[
\boxed{Q(g(t))\le M\quad\text{for every finite }t.}
\tag{4}
\]
This is a direct evolution barrier. It does not assume beforehand that
the stationary L2 inverse has high regularity.

The same trajectory converges in L2, by(1), to the actual
\(z_k=-A_k^{-1}F\).
Weak compactness of W_aJqg(t) and distributional identification of its
limit give Q(z_k)<=M. Thus the actual full frozen inverse maps every smooth
input in B into B.

## 3. Rough frozen inputs and completeness

Every k in B has in-ball Schwartz real S1 approximants. Approximate Jqk
in L2(W_a²dX), apply J^-q, symmetrize, and scale by
min(1,R/||k_n||2,M/Q(k_n)). These factors tend to one. This gives convergence
in Q and Hq, hence uniform convergence of U[k_n] and their first
derivatives. No strain functional needs to be subtracted.

Let z_n be the just-constructed actual inverses for k_n. In distributions,
\[
A_kz_n=-F+(U[k]-U[k_n])\cdot\nabla z_n\in L2.
\]
The actual maximal L2 domain therefore applies. Since ||grad z_n||2<=M,
\[
\|z_n-z_k\|2\le\beta_2^{-1}
\|U[k_n]-U[k]\|infty\,M\longrightarrow0.
\]
Weak compactness and the distributional identity again give Q(z_k)<=M.
This proves the self-map for the whole ball and establishes actual high
inverse regularity uniformly there.

The ball is complete in the L2 metric: an L2-Cauchy sequence has an L2
limit; weak compactness of its bounded W_aJq images identifies the limit's
weighted derivative and preserves the Q radius. Real S1 symmetry and the
L2 radius are closed as well.

## 4. Contraction and the fixed exponent

The exact Fourier gradient embedding is
\[
\|\nabla z\|infty\le S_1\|J^qz\|2\le S_1Q(z),
\quad S_1=5/\sqrt{11\pi}<6/7.
\]
For T(k)=-A_k^-1F, the actual L2 inverse and difference equation give
\[
\|T(k)-T(l)\|2\le\frac{S_1M}{\beta_2}\|k-l\|2.
\tag{5}
\]
If S1M<beta2, Banach's theorem supplies the unique fixed point in B.
For example M<=1/2 and beta2>=7/4 give contraction factor below12/49.
The stationary equation for rho=rho*+k is then the actual whole-plane
IPM equation at the original exact rational c.

The origin strain is derived at the fixed point. Actual exact source
structure gives c+partial_y(u*)2(0)=1 and a0=partial_y rho*(0)>1.
For M<=1/2 the total density slope is positive because
|partial_yk(0)|<=S1M<3/7. The parity gives V(0)=rho(0)=0. The first-order
origin expansion of the continuous stationary equation therefore yields
\(\ell(k)(a0+\partial_yk(0))=0\), with
ell(k)=partial_y U2[k](0). Thus ell(k)=0 automatically. No invariant
origin hyperplane was assumed for nonfixed inputs.

Finally, the coordinate Sobolev equivalence shows that this solution has
the original weighted Hq regularity, even if the auxiliary a differs from2.
The exact fixed exponent and the unchanged center are not replaced by
limiting parameters. Numerical fulfillment of(1)--(3), the stated forcing
bounds, and the contraction inequality is still essential to an existence
claim; this bridge is not itself their verification.
