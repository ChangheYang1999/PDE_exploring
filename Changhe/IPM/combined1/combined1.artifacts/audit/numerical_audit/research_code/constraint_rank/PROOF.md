# Exact rank of the tail and origin constraints at candidate 007

## Statement and scope

Let c=4076476460239181/2251799813685248, gamma=1/c,
delta=1-gamma and p_j=(3+gamma-j delta)/2. Let V be the exact
1922-dimensional potential span of candidate C1-N1-007-d2w-j7-e2bal,
with its 2982 generators and 1060-dimensional coefficient kernel as
confirmed in N4-163. Its generators are

    H_m (1+r^2)^(p_j-m) P(t),
    H_m=Re(x+iy)^(2m), t=r^2/(1+r^2).

The frozen optimizer imposes one leading potential moment in each of
360 (j,m) blocks, a first descendant moment in each of the 60 blocks
with j in {0,1,2}, and the center strain chi_xxyy(0)=1-c. It also
linearizes the five coefficients x^2,y^2,x^4,x^2 y^2,y^4 of R_f=F/y,
where

    rho=-partial_y Delta chi,
    U=(-chi_xyy,chi_xxy),
    F=(c(x,y)+U) dot grad rho-rho.

At the exact candidate, write a0=rho_y(0). If the retained rational
checks establish a0 != 4c-2 and a0 != 8c-4, these 426 constraint
functionals have linearly independent differentials on V. The 421
linear constraints alone have rank421. Thus the homogeneous linearized
constraint space has potential dimension1496, and its preimage in the
2982 generator coordinates has dimension2556, including the1060 zero
potentials. These dimensions concern the constraint differential, not
the PDE residual Jacobian or its norm conditioning.

If the exact candidate also satisfies all five Taylor equations and
the prescribed linear right sides, the finite-dimensional implicit
function theorem gives a local1496-dimensional constraint manifold
in V. This extra conclusion is conditional on those exact feasibility
checks; constraint rank does not itself establish feasibility.

## 1. Independent tail rows

In a fixed block, put z=r^-2. After removing r^(2p_j), the radial
factor equals

    (1+z)^(p_j-m) P((1+z)^-1).

Its first two coefficients are

    L0(P)=P(1), L1(P)=(p_j-m)P(1)-P'(1).

Every generator polynomial has P(1)=1, so L0 is nonzero in every
block. In the60 blocks with j in {0,1,2}, the checker verifies an
explicit pair with a nonzero L0,L1 determinant. Consecutive monomials
t^w,t^(w+1) have determinant -1, and leg(w,0),leg(w,1) span such a
pair. This two-row condition is required only where both rows are
imposed. Several higher-branch blocks have only one generator and
one imposed leading row. Thus L0,L1 are independent wherever both
are imposed.
Different blocks are independent potential subspaces by the exact
nonresonance and angular argument in ../basis_redundancy/PROOF.md.
The360 leading rows and60 descendant rows therefore have rank420.
This proof uses exact polynomial coordinates, with no floating rank
tolerance and no normal matrix.

## 2. Six explicit directions in the tail kernel

For nonnegative integers a,b, l=a+b, define

    eta_(a,b)=x^(2a)y^(2b) (1+r^2)^(p_0-l-2).

Every such function with l<=4 belongs to V. Indeed the homogeneous
polynomial x^(2a)y^(2b) is a rational combination of
H_m r^(2(l-m)), 0<=m<=l. After the common radial factor of block(0,m)
is removed, the remaining polynomial is a rational multiple of

    t^(l-m)(1-t)^2.

Its degree is l-m+2<=6-m, within the full polynomial span of each
relevant j=0 block. The checker verifies each finite decomposition
and polynomial membership exactly. Both L0 and L1 vanish because
of the double zero at t=1. No other branch is present, so every
prescribed tail row vanishes on these directions.

Use the six directions

    eta_(1,1), eta_(2,1), eta_(0,3),
    eta_(3,1), eta_(1,3), eta_(0,4).

The first has chi_xxyy(0)=4. The other five have total order at least6
at the origin, hence zero strain. This already proves that the
center row raises the linear rank from420 to421.

## 3. Taylor differential at the normalized origin

Parity and the strain relation give

    rho=a0 y+O(r^3),
    U=((c-1)x,(1-c)y)+O(r^3),
    c(x,y)+U=((2c-1)x,y)+O(r^3).

For a perturbation whose leading homogeneous potential is a
polynomial M of even degree2l>=6, its leading density and velocity
are -partial_y Delta M and (-M_xyy,M_xxy). Linearizing F, the leading
term is

    DF[M]=((2c-1)x partial_x+y partial_y-1)
             (-partial_y Delta M)+a0 M_xxy.

Terms involving higher background Taylor coefficients or higher
terms of eta have degree at least2l-1 in F. Therefore the leading
R_f differential has degree2l-4 and depends only on M and a0.
This is a polynomial identity and is checked independently by
symbolic differentiation of these monomials.

For the two degree6 directions, on the ordered rows x^2,y^2 this
gives the diagonal matrix

    diag(24(a0-4c+2), -240).

For the three degree8 directions, on rows x^4,x^2 y^2,y^4 it gives

    [60(a0-8c+4)       0             0   ]
    [     0         -480c           0   ]
    [     0       12(a0-4)       -1344  ].

In the full six by six strain/Taylor matrix, entries above these
blocks vanish by order at the origin. Its determinant is therefore

    4 * 24(a0-4c+2) * (-240)
      * 60(a0-8c+4) * (-480c) * (-1344).

Because c>0 and both displayed differences are nonzero, the
matrix is invertible. The six rows restricted to the kernel of
the420 tail rows are independent. This proves total rank426.
It does not require the Taylor right sides to vanish.

## 4. Arithmetic and interpretation

The verification uses the exact canonical coefficients and frozen
source hashes. Reconstruct chi through total degree8 with rational
binomial coefficients; derive rho,U,F by polynomial differentiation
and multiplication; obtain a0 and strain independently of the stored
metadata. Verify the two nonzero factors with outward bounds as
readable witnesses and also as exact rational inequalities. Check
the six direction matrix against the displayed determinant and an
independent copied origin-jet implementation. Record the exact
Taylor residual coefficients as feasibility data, not as assumed
zeros. Large exact rationals stay in JSON and are never transcribed
into a generated proof-assistant source.

If any claimed block support or determinant check fails, no dimension
claim is accepted. Successful rank arithmetic remains OPEN until a
separate lane reproduces it and reviews the argument. Even after
confirmation, a coefficient-space eigenvalue does not become a
function-space inverse estimate. The finite sampled residual map,
its errors, its constraint projection and its infinite-dimensional
complement require separate analysis.

Dependencies: N4-163's exact potential rank and branch decomposition,
elementary finite-dimensional linear algebra, Taylor differentiation,
and, only for the conditional manifold statement, the implicit
function theorem. No optimizer, server, remote computation or
proof-assistant build is used.
