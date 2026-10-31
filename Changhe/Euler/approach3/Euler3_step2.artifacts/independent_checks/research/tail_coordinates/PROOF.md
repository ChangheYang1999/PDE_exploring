# Derivatives in the reduced tail-constrained coordinates

Status: proved algebraic identity for the inviscid coefficient constraints. It does not assert an Euler solution.

## Statement

Fix main degree L=6, a radial coefficient count N>=2, a mode (ell,m) with ell>=1 and 0<=m<=ell, and 2/5<c<1/2, w>0. Set alpha=(1-c)/c, kappa=w/c. For a leading toroidal mode use sigma=0; for a leading poloidal mode use sigma=1. Put

P=(alpha+ell-sigma)/2 + i m kappa/2.

For m>0 combine cosine/sine radial coefficients into z_k=a_k+i b_k, k=0,...,N-1. For m=0 use real coefficients and the same equations with m=0. Hold z_0,...,z_(N-3) fixed and choose the final two coefficients so that

sum k² z_k=0,
sum [(8/3)k²(k²-1)-P]z_k=0.

There is a unique smooth choice of the final two coefficients throughout the stated parameter domain. If u=z_(N-2), v=z_(N-1), i0=N-2, j0=N-1 and K_k=(8/3)k²(k²-1), then

M [u,v]^T = [-sum_free k²z_k, -sum_free K_k z_k + P sum_free z_k]^T,

M=[[i0²,j0²],[K_i0-P,K_j0-P]].

For p=c or w, the derivative at fixed free coefficients is

M [u_p,v_p]^T = [0,P_p sum_all z_k]^T,

P_c=-1/(2c²)-i m w/(2c²), P_w=i m/(2c).

For B and D correction channels, the top-coefficient constraint sum k²z_k=0 has no c,w dependence, so its derivative at fixed free coordinates is zero. E coordinates are unchanged.

## Proof

The two complex equations are exactly the four real equations for a cosine/sine pair: the real part of (K-P)(a+ib) is (K-Re P)a+(Im P)b, and its imaginary part is (K-Re P)b-(Im P)a. Separating the last two terms gives the matrix equation.

Its determinant is

(j0²-i0²)[(8/3)i0²j0²+P].

The first factor is positive. The real part of the bracket is positive because alpha>1, ell>=1 and sigma in {0,1}; in particular Re P>0. Thus M is invertible, including N=2, and the solution depends smoothly on c,w.

Differentiate the first constraint: the free coefficients are constant, so i0²u_p+j0²v_p=0. Differentiate the second constraint: the new coefficient derivatives contribute (K_i0-P)u_p+(K_j0-P)v_p, and differentiating -P contributes -P_p sum_all z_k. Moving the latter term to the right proves the derivative equation. The formulas for P_p follow by differentiating alpha and kappa. The correction-channel statement follows because its constraint contains no parameter.

## Consequence for a represented field

Write C(a,c,w) for the expanded full coefficient arrays and let V(C,c,w,y) denote the full-coordinate velocity representation. At fixed reduced a,

U_p = (partial_p V)_C + V(C_p,c,w,y),

because the representation is linear in C. The same identity holds for DU, vorticity and its gradient. The momentum and pressure derivative identities in the neighboring proofs remain valid with this complete U_p. Testing only (partial_p V)_C is insufficient for a reduced-coordinate optimizer.

## Dependencies and scope

Only finite-dimensional linear algebra, complex arithmetic and the chain rule are used. The constraints are the inviscid constraints already present in the frozen representation. A viscosity-dependent or otherwise changed constraint would need a separate derivative and is not covered here.
