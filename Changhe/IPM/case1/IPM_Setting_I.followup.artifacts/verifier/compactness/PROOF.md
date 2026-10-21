# What excludes zero and polynomial limits

Dated 2026-10-20. This note concerns compactness of normalized trial fields and of the canonical full-plane inverse. The manufactured fields below are not transport solutions. They show which conclusions cannot follow from parity, center normalization, a fixed strain identity, and separate growth bounds for each field alone.

## Definitions and dependencies

Use U=(-psi_y,psi_x), -Delta psi=rho_x, with the canonical kernel of ../inverse/PROOF.md. For an even-x, odd-y density of sublinear growth, the exterior can be paired at Y and -Y. For |X|<R its velocity is given by the convergent expansion proved in ../exterior-tail/PROOF.md. In particular a density supported outside radius R with only sine modes one and three induces exactly

    U(X)=(-c x,c y),  c=int_R^infinity rho_3(r) r^(-2) dr,  |X|<R.

There are no higher terms since they would require density modes five, seven and higher. For rho=x^2 y b(r), the third sine coefficient is r^3 b(r)/4. When b is smooth and compactly supported or rapidly decreasing, the center strain is therefore

    c=psi_xy(0)=(1/4) int_0^infinity r b(r) dr.

This formula also follows by taking the lower limit to zero in the exterior expansion: the inner density is O(r^3), so its contribution to a velocity derivative tends to zero. A nonzero rho_y(0) would require the contact term discussed in the inverse proof; it is zero here.

Fix c_*>2 and c_l=(1+c_*)/3>1. Choose a smooth nonnegative shell function b supported in 1<r<2 with int r b(r)dr=4. Put phi(X)=x^2 y b(|X|), so its canonical center strain is exactly one. Scaling the kernel gives

    U[M phi(X/R)](X)=M U[phi](X/R),

and hence the strain of R lambda phi(X/R) is lambda. These identities use the unique full-plane inverse and involve no freely added harmonic field.

## A normalized sequence that converges locally to zero

For 0<epsilon<1 and R>2 define

    rho_(epsilon,R)(X)
      = x^2 y exp(-|X|^2/epsilon^2)
        + R(c_*-epsilon^2/8) phi(X/R).

Each field is smooth, even in x, odd in y and factors as x^2 y a with

    a=exp(-|X|^2/epsilon^2)
       +(c_*-epsilon^2/8) R^(-2)b(|X|/R),  a(0)=1.

It is nonnegative as a factor. Each field and its first derivative meet the sublinear growth bounds for any fixed exponent 0<gamma<1, with a constant allowed to depend on epsilon and R. The Gaussian core has strain epsilon^2/8; the shell has the remaining strain. Thus every field has c=c_* and exactly the same c_l>1 and normalization identity.

Let epsilon tend to zero and R to infinity. On every compact set the shell density is eventually zero. The core is epsilon^3 F(X/epsilon), F(Z)=Z_x^2 Z_y exp(-|Z|^2), whose C^(2,alpha) norm is bounded by C_alpha epsilon^(1-alpha) for every alpha<1. The derivative suprema scale as epsilon^(3-j), j<=2, and the second-derivative Holder seminorm as epsilon^(1-alpha). Thus rho_(epsilon,R) tends to zero in C^(2,alpha) on every compact set.

On |X|<R the shell velocity is exactly

    (-(c_*-epsilon^2/8)x,(c_*-epsilon^2/8)y).

The core velocity and its first derivatives tend uniformly to zero on fixed compacts: the scaling is epsilon^3 U[F](X/epsilon), and U[F] and its first derivatives are bounded. This boundedness follows from the local smooth singular-integral subtraction and the decay of F. Therefore the canonical velocities converge locally in C^1 to (-c_*x,c_*y), whereas the canonical velocity of the limiting zero density is zero. Canonical inversion is not closed under this local convergence without tail control.

The third derivative rho_xxy(0)=2 persists for every member, but is not continuous under C^(2,alpha) convergence when alpha<1. Thus a(0)=1 alone does not exclude this zero limit.

The annular part has size comparable to R at radius comparable to R. Its growth constant for a fixed gamma<1 is at least a constant times R^(1-gamma), and therefore is not uniform. This is where the construction violates the uniform condition below.

## A normalized sequence that converges locally to a polynomial

Choose a smooth radial cutoff chi with chi=1 on [0,1], chi=0 on [2,infinity). Put C_chi=(1/4)int r chi(r)dr>0 and S=4R. Define

    rho_R(X)=x^2 y chi(|X|/R)
              +S(c_*-R^2 C_chi) phi(X/S).

The density is smooth, compactly supported, has the required parities and smooth factor a(0)=1, and its canonical strain is exactly c_*. Thus the same c_l identity holds. For every fixed compact set, rho_R=x^2y there once R is large enough, so it converges locally in every smooth norm to this nonzero polynomial. Each rho_R satisfies a separate sublinear growth bound, but no common bound is possible. The shell factor can be negative; no positivity is asserted for this second example.

On a fixed disk, the velocities of any two sufficiently large members agree exactly. Their density difference vanishes on that disk, has only modes one and three, and has zero strain. The exterior expansion therefore gives zero difference of the velocities there. This does not make the limiting polynomial an admissible whole-plane density.

Neither construction consists of profile solutions or claims small normalized residuals. Every member is bounded, tends to zero at spatial infinity and is nonzero, so its density has a nonzero extremum. At such a point grad rho=0 and (c_l X+U).grad rho-rho=-rho!=0. This elementary check prevents confusing these fields with a new branch or a counterexample to profile nonexistence.

## A sufficient uniform condition

Suppose rho_n have the parities, converge to rho in C^(1,alpha) on each compact set for some alpha>0, and obey one common bound

    |rho_n(X)|<=C(1+|X|)^gamma,  gamma<1.

Then their canonical velocities converge to U[rho] in C^1 on compact sets. To prove this, fix |X|<=M and split at |Y|=R>2M. By oddness under Y->-Y, the exterior contribution uses half the difference K(X-Y)-K(X+Y). Bounds on the homogeneous kernel give

    |K(X-Y)-K(X+Y)|<=C_M |Y|^(-3),
    |D_X K(X-Y)-D_X K(X+Y)|<=C |Y|^(-3).

The density bound and polar integration therefore bound both exterior contributions by C_M R^(gamma-1)/(1-gamma), uniformly in n. The limiting density has the same bound. On the fixed inner region the singular integral and its first derivatives converge by local C^(1,alpha) convergence: subtract the value of the density, or its derivative, at the pole and integrate |Z|^(alpha-2). The remaining smooth cutoff terms converge directly. First choose R large, then n large. This proves the claim.

In particular, if all c_l,n=(1+c_n)/3>1 and rho_n were to converge to zero in local C^(1,alpha), the uniform condition would force c_n->0 and c_l,n->1/3, a contradiction. It excludes zero collapse under those hypotheses. It also excludes a nonzero polynomial density limit, since the common sublinear bound passes pointwise to the limit, and an odd nonzero polynomial has degree at least one.

Uniform derivative tail bounds are not needed for this closure argument; uniform local C^(1,alpha) control and the stated density tail bound suffice. The separate first-derivative growth requirements of the admissible class can still be imposed on individual fields.

## Scope

For a proposed convergence sequence, uniform growth constants or equivalent uniform tail-integrability estimates must be measured or proved. Membership of each field in the same union of sublinear-growth classes is insufficient. Conversely, this compactness result supplies neither a converged sequence of transport solutions nor a closing estimate for the strong setting.
