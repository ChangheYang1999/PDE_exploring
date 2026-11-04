# Vorticity Liouville under vanishing strain and one subcritical integral

## Exact statement

Let c>0, omega be finite, U in C^2(R^3), and P in C^1(R^3) solve the full rotating profile equation with div U=0. Let S=(DU+DU^T)/2 and Omega=curl U. Assume S(y) tends to zero as |y| tends to infinity and Omega belongs to L^p(R^3) for one exponent 0<p<3c. Then U is constant. If U tends to zero, then U=0.

Tags: H0 with the stated pressure regularity, H3 (only the symmetric strain tends to zero), H4 (one vorticity exponent p<3c). No assumption on pressure at infinity, full derivative decay, or full sublinearity of U is used. This independently verifies LIT08 and the corresponding rotation extension of the Chae-Shvydkoy mechanism.

## 1. What vanishing strain implies about radial transport

For r=|y|, the fundamental theorem of calculus gives

\[
 y\cdot U(y)=y\cdot U(0)+\int_0^1 y\cdot S(ty)y\,dt.
\]

Let M=sup|S|, finite by continuity and its vanishing limit. Given epsilon>0 choose R_0 so |S|<=epsilon outside B_{R_0}. Split the integral at R_0/r. For r>=R_0,

\[
 |U(y)\cdot y/r|\le |U(0)|+MR_0+\epsilon r.
\]

Thus the radial component is o(r), uniformly in direction. Rotation has zero radial component, so B dot n=cr+U dot n is positive and at least cr/2 outside a large ball, and |B dot n|<=Cr there. Nothing about the tangential component of U is inferred or required.

## 2. Scalar vorticity transport, including exponents below one

The curl equation gives

\[
 B\cdot\nabla\Omega=(DU-\omega J-I)\Omega.
\]

Put sigma=Omega dot S Omega/|Omega|^2 at nonzero Omega and zero elsewhere. For every q>0,

\[
 \operatorname{div}(B|\Omega|^q)
       =(3c-q+q\sigma)|\Omega|^q                       \tag{1}
\]

holds in distributions. To justify the chain rule at zeros, first use

\[
 f_\delta=(|\Omega|^2+\delta)^{q/2}-\delta^{q/2}.
\]

Its classical transport derivative is q(sigma-1)|Omega|^2(|Omega|^2+delta)^{q/2-1}. For q<=2 the last amplitude is bounded by |Omega|^q. For q>2 it has a uniform bound on each compact set for 0<delta<=1. Both this term and 3c f_delta converge by dominated convergence on compact sets. This proves (1) without differentiating the nonsmooth power at a vorticity zero.

## 3. The exterior flux has the required sign

For q=p choose R_0 larger so

\[
 3c-p+p\sigma\ge(3c-p)/2=:\kappa>0\quad(r\ge R_0).
\]

Because integral_0^infinity integral_{S_r}|Omega|^p dS dr is finite, there is a sequence R_j tending to infinity such that R_j integral_{S_{R_j}}|Omega|^p tends to zero. If the liminf were positive, this radial integral would dominate a positive multiple of integral dr/r and diverge.

Integrate the regularized identity on R<r<R_j, with fixed R>=R_0, and then let delta tend to zero. This gives

\[
 \int_{R<r<R_j}(3c-p+p\sigma)|\Omega|^p
 =\int_{S_{R_j}}|\Omega|^p B\cdot n
    -\int_{S_R}|\Omega|^p B\cdot n.
\]

The outer integral tends to zero by the radial bound Cr. The inner integral is nonnegative. Dominated convergence on the left is valid because S is bounded and Omega is in L^p. Consequently

\[
 \kappa\int_{r>R}|\Omega|^p
 \le-\int_{S_R}|\Omega|^p B\cdot n\le0.
\]

Omega is zero outside B_R, first almost everywhere and then pointwise by continuity. The sign of the inner boundary is essential; it is the minus sign shown here.

## 4. A smaller power kills the compact support

The now compactly supported continuous Omega belongs to L^q for every q>0. Choose 0<q<3c/(1+M), where M=sup||S||_op. Integrating (1) over a ball beyond the support gives

\[
 0=\int(3c-q+q\sigma)|\Omega|^q
   \ge(3c-q-qM)\int|\Omega|^q.
\]

The coefficient is positive, so Omega=0 globally. The original p need not satisfy this stronger global smallness inequality; changing exponent is justified only after proving compact support.

## 5. Harmonic conclusion

Divergence and curl now vanish, so U is harmonic componentwise and hence smooth. Moreover DU is symmetric, so DU=S tends to zero. Every derivative of U is an entire harmonic function tending to zero; harmonic Liouville gives DU=0. Thus U is constant, and velocity decay forces zero.

## Scope

No complete-flow assertion is used: all steps are local identities followed by explicit flux limits. The strict p<3c condition cannot be replaced by equality in this proof. Under the additional pointwise estimate |Omega|<=C(1+r)^{-k} with k>1/c, one can choose 3/k<p<3c. Neither that rate nor vanishing strain is proved by mere velocity decay.
