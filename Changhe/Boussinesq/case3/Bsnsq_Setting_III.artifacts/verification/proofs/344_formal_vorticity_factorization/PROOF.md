# Formal vorticity factorization at the beta=2 simple endpoint

Prepared 2026-10-22T10:42:00.445894+00:00 before this packet's computations. This result is algebraic and conditional on the verified formal solution of P321 and normalized temperature root of P331. It gives no convergent series, actual off-axis curve, smooth local Boussinesq solution, or full-plane profile. The general B2 question remains OPEN.

## Exact statement and notation
Work in the complete real formal power-series ring R[[r,u]], with r=x^2. Assign ordinary total degree one to each of r and u. Let C,k be nonzero real numbers, and let the formal solution of P321 have beta=2, B(u)=u+ku^2-Cku^13/260 and H_0=-k^7/231. Write W_1=x a(r,u), W_2=sum_{j>=0} v_j(u)r^j, with signed u=y_*-y. Its derivation on R[[r,u]] is

V=2r a(r,u) partial_r - W_2(r,u) partial_u.

Here a(0,0)=5 and V has linear part 10r partial_r+(kr-u) partial_u. The thermal equation is VTheta=0 and the vorticity equation is VOmega+Omega=partial_x Theta at fixed u, where the derivation extends to R[[r,u]] plus xR[[r,u]], with x^2=r and Vx=xa. On even series partial_x F=2x partial_r F. Fixing u is equivalent to fixing physical y because u=y_*-y. Let Theta=(C/2)rZ(r,u)^10 be the normalized P331 factorization, with Z=qL, q=u-h(r), h(r)=kr/11+O(r^2), L(0,0)=1, and h invariant. Thus VZ=-(a/5)Z. Let Omega=xG(r,u), where the P321 axis coefficient G(0,u)=H_0 u^6+O(u^7) has H_0 nonzero.

There is a unique real formal unit Y(r,u), with Y(0,0)=1, such that

Omega=H_0 x Z^6 Y.

It obeys the exact formal equation

VY+(1-a/5)Y=(C/H_0)[Z^4+10r Z^3 partial_r Z].

In total (r,u)-degree, with r and u each of degree1, G has no term of degree below6, and its degree6 homogeneous part is

G_[6]=H_0 (u-kr/11)^6.

Consequently, the corresponding series in (x,u) has no monomial of ordinary degree below7, and its unique degree7 term is H_0 x u^6. The formal identity

x Omega Theta=(CH_0/2)r^2Z^16Y

holds. If k<0 and C>0, CH_0>0, but no pointwise sign or actual zero set is deduced from a merely formal identity.

## Complete proof
Transport on odd formal series gives V(xG)+xG=x[VG+(a+1)G]. Since Theta=(C/2)rZ^10 and partial_x=2x partial_r on even series, the vorticity equation after division by x becomes

VG+(a+1)G=S,
S=CZ^10+10CrZ^9 partial_r Z.

All statements are formal identities; division by x is valid because multiplication by x is injective. Make the invertible formal coordinate change q=u-h(r). The vector field is

V=2r alpha(r,q) partial_r+q delta(r,q) partial_q,

with alpha(0,0)=5 and delta(0,0)=-1. The transverse factor q follows from graph invariance. Write g(r,q)=G(r,q+h(r)). Since Z=q ell with ell a unit, the source S is divisible by q^9. Differentiating at fixed u changes partial_r Z to -h'(r)ell+q(ell_r-h'(r)ell_q), so only q^9, not q^10, is guaranteed.

For j<6, suppose g_0,...,g_{j-1} vanish as formal series in r, where g_j=[q^j]g. The q^j coefficient equation is

2r alpha(r,0) g_j'(r)+[alpha(r,0)+1+j delta(r,0)]g_j(r)=0.

The higher q coefficients of alpha, delta and the transported a multiply lower g_i or their r derivatives, which vanish. If g_j were nonzero, take its lowest r power p>=0. Its coefficient is multiplied by 10p+6-j, strictly positive. This contradicts the displayed identity. Induction gives g_j=0 for j=0,...,5. Therefore g=q^6K in R[[r,q]], with K(0,0)=H_0, from the given axis coefficient and h(0)=0. Dividing by the units H_0 and ell^6 defines a formal unit with constant1. Returning to (r,u), set Y=K(r,u-h(r))/(H_0 L(r,u)^6). This gives the claimed factorization. Multiplication by the nonzero element xZ^6 is injective, so Y is unique for the fixed Omega,Z.

Apply the derivation to Omega=H_0 xZ^6Y, use Vx=xa and VZ=-aZ/5, and divide by the nonzero formal product H_0 xZ^6. The left side is VY+(1-a/5)Y. The divided thermal source is precisely (C/H_0)[Z^4+10rZ^3 partial_r Z]. Thus the unit equation holds in the formal ring, with no negative powers. The constant coefficient on the left is zero because a(0,0)=5, consistent with the zero constant of the right.

Since Z has zero constant and degree1 part u-kr/11 while Y has constant1, Z^6Y has no terms below degree6 and degree6 part (u-kr/11)^6. This proves the total (r,u)-degree claim. A monomial r^i u^j of G with i+j>=6 yields x^(2i+1)u^j of ordinary degree2i+j+1>=7, equality only for i=0,j=6. Finally multiply the two formal factorizations to obtain the product identity. A formal unit with positive constant does not by itself assign values to the series at nonzero points; pointwise signs would require convergence or an independently constructed actual field. No such hypothesis is added.

## Dependencies, checks and scope
Only the stated local formal data are used in this implication: a(0,0)=5, the displayed linear field, the two transport equations, and G(0,u)=H_0u^6+O(u^7) with H_0 nonzero come from P321. Its particular B and Poisson relation are not otherwise used in this implication. P331 supplies h, its invariance and first coefficient, and the normalized Z=qL with L(0,0)=1. Uniqueness of Y is relative to this fixed normalized Z. The broader input formal solution is P321, including the all-order resonance tuning and the Poisson relation; P326 supplies one common complex disk for each separate axis coefficient but not convergence in x. P331 supplies the normalized formal thermal root and graph. Their full informal proofs and verification records remain available in their own folders. The above implication is proved independently here and does not require an analytic stable manifold theorem.

Independent exact finite checks will use this lane's nonlinear recurrence coefficients and a separate truncated bivariate ring evaluator. They will check lower transverse vanishing, leading weighted coefficients, division and the formal unit equation in an explicitly declared rectangle of known coefficients, using multiple truncations and negative perturbations. Any extended nonlinear recurrence run remains a finite calculation; it cannot certify infinite-order convergence. No lead or numerics source is imported or executed. No formal Lean verification is claimed or run. Restrictions: no JavaScript/TypeScript, no servers/listeners/tunnels, no RLScience cluster, no Lean/Lake builds; all writes in this verifier lane.
