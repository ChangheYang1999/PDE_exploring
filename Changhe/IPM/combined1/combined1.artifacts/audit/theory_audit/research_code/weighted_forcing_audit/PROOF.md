# Independent weighted-forcing audit

## 1. Statement

Let c>1, gamma=1/c, delta=1-gamma, and let a finite real S1 potential be

chi=sum_(j,n) (1+r²)^p_j P_(j,n)(t) cos(n theta),
p_j=(3+gamma-j delta)/2, t=r²/(1+r²), u=1-t.

The indices j are nonnegative, the angular n are nonnegative even integers, and every P has rational coefficients. Assume that each branch is smooth at the origin. Define rho=-partial_y Delta chi, psi=partial_xy chi, U=(-partial_y psi,partial_x psi), and F=c r partial_r rho-rho+U.grad rho. Let w_R=(1+r²/R²)^(-a/2), a>0 and R>=1.

For 0<A<B, the exact full-circle unweighted annular integral I(A,B) gives

||w_R F||_2² >= (1+B²/R²)^(-a) I(A,B).                         (1)

For a finite sine representation F=r sum_(j,n) u^((j+1)delta/2) Q_(j,n)(u) sin(n theta), with positive odd n, suppose every individual diagonal term is integrable after multiplication by u^a. Then

||w_R F||_2² >= (R²/2)^a (pi/2) sum_n integral_0^U
 (1-u)u^(a-3) [sum_j u^((j+1)delta/2) Q_(j,n)(u)]² du,         (2)

where U=1/(1+R²). Both right sides have exact finite-power antiderivatives. These are lower bounds for the prescribed forcing norm, not for an inverse correction. A norm upper bound for an inverse cannot be reversed to infer that a large forcing requires a large correction.

## 2. Independent residual construction

Put a_j=(j+1)delta/2. On the potential radial factor the logarithmic derivative D=r partial_r acts on its polynomial by

A_j P=2p_j t P+2tu P'.

The Laplacian numerator is B=A_j²P-n²P. Applying -partial_y to the mode gives density numerators (A_j B-2B+nB)/2 at angular n-1 and -(A_j B-2B-nB)/2 at n+1. Fold a negative sine frequency with a minus sign and discard zero. After exact division of each combined numerator by t², this yields

rho=r sum_(j,n) u^a_j R_(j,n)(t) sin(n theta).

These are the same Laplacian identities proved independently in ../background_norm_reproduction/PROOF.md. The exact divisibility checks are part of the computation.

For the stream function, use L_plus=partial_x+i partial_y and L_minus=partial_x-i partial_y, so partial_xy=(L_plus²-L_minus²)/(4i). Acting on one cosine mode gives, before division by t², the sine numerators

(A_j-n-2)(A_j-n)P/4 at n+2,
-(A_j+n-2)(A_j+n)P/4 at n-2.

Consequently psi=r² sum_(j,m) u^a_j S_(j,m)(t) sin(m theta), with even nonzero m after folding. This construction avoids a Cartesian derivative tree.

Define T_b P=(1-2bt)P+2tu P' and B_a S=(2-2at)S+2tu S'. The polar fields are

U_r=-r u^a m S cos(m theta), U_theta=r u^a B_a S sin(m theta),
rho_r=u^b T_b P sin(n theta), r^-1 rho_theta=u^b nP cos(n theta).

Their product contributes to F/r, in branch h=j+k+1, the polynomials

[-m S T_bP+nP B_aS]/2 at n+m,
[-m S T_bP-nP B_aS]/2 at n-m.

Again fold negative sine indices. The linear term in branch k is cT_bP-P. Every operation here is rational polynomial arithmetic. This computes the same exact residual as the defining Cartesian formula, by the polar identities just proved.

## 3. Exact integrals and the weight inequalities

Changing from r to u gives r³ dr=-(1-u)du/(2u³). Full-circle sine orthogonality has integral pi on each positive frequency and zero between distinct frequencies. This proves

I(A,B)=(pi/2) sum_n integral_(1/(1+B²))^(1/(1+A²))
 (1-u)u^-3 [sum_j u^((j+1)delta/2) Q_(j,n)(u)]² du.             (3)

Multiply out the finite square exactly and collect equal exponents. A term q u^b integrates to q(V^(b+1)-U^(b+1))/(b+1), with the logarithmic formula q log(V/U) at b=-1. Endpoints are positive, so no integrability hypothesis is required for (3).

The weight decreases in r, proving (1). For r>=R,

w_R²=R^(2a)u^a/[1+(R²-1)u]^a >= (R²/2)^a u^a,

because 0<u<=1/(1+R²) and 1+(R²-1)u<=2. Apply this inequality before expanding the nonnegative square. This proves (2) and allows signed polynomial cross terms without discarding them.

If Q_(j,n) has exact order q at u=0, its diagonal exponent in (2) is a-3+(j+1)delta+2q. The assumed strict inequality greater than -1 proves its integrability. A cross exponent is the arithmetic mean of the two corresponding diagonal exponents and is also greater than -1. The finite-power primitive therefore has zero lower endpoint. If a separated diagonal check fails, this proof gives no exterior formula unless exact cancellations are first handled. It does not infer divergence from an inconclusive check.

## 4. Verification and scope

The implementation first performs the residual construction and all square expansions with exact rational polynomials, then encloses only the powers, pi and square roots using Arb. It compares every requested annular and exterior bound with the independently obtained N4 intervals. The data hash identifies the fixed state131 candidate and the parameters are exactly a=221/200, R=2^29. This norm is one specific proposed weighted low space. Neither a large value nor the lower bound in (2) rules out another norm, another reference profile, a sharper inverse analysis, or an exact stationary solution.
