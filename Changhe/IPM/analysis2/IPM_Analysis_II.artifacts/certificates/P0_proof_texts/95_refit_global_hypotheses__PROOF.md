# Global reference hypotheses for exact algebraic refits

## 1. Exact objects and certificate scope

The references considered here are the exact potentials nb_d2_exact and nb_Mpen2_exact delivered by the numerical work and independently reconstructed in topics19 and91. They have the original rational exponent c=4076476460239181/2251799813685248. Every coefficient is rational. The coefficient arrays, original generator arrays and hashes are part of the certificate inputs. The density, canonical velocity and transport are

    rho=-partial_y Delta chi, u=(-chi_xyy,chi_xxy), V=cX+u.

The potential has the finite form

    chi=sum a_jmk r^(2k) cos(2m theta) (1+r^2)^(p_j-k),
    p_j=(3+gamma-j delta)/2, gamma=1/c, delta=1-gamma.

Each result below is conditional on a COMPLETE directed certificate for the specified reference and target. An incomplete subdivision is not a global bound. There is no claim here that the a posteriori residual threshold is met. Topics86 and90 prove that it is not met.

The target matrix inequalities are

    M=(2c+1)I+sym Du+A >=19I/5,
    M1=(1+c+V.D log omega1)I-sym DV+A >=I/2,
    M2=(1+c+V.D log omega2)I-2sym DV+A >=I/2,
    A=[[rho_y,-rho_x/2],[-rho_x/2,0]],
    omega1=(1+r^2)^(-1/10), omega2=(1+4r^2)^(2/5).

The additional target coefficient bounds are |Du|<=14/5 and |D rho|<=16, with the Euclidean norm of the ordered Cartesian tensor. Only targets whose complete certificate and independent recheck pass may be reported as proved. The remaining higher-derivative and decay hypotheses are separate.

## 2. Exact compactified fields

Set t=r^2/(1+r^2), z=cos(2theta), w=(1-t)^(delta/2). For q in {chi22,chi04,chi31,chi13} there are rational polynomials P_q,j(t,z) such that

    chi22=sum_j w^(j+1) P_22,j,
    chi04=sum_j w^(j+1) P_04,j,
    chi31=sqrt(1-z^2) sum_j w^(j+1) P_31,j,
    chi13=sqrt(1-z^2) sum_j w^(j+1) P_13,j.       (1)

Here chiab denotes partial_x^a partial_y^b chi. To obtain these polynomials, differentiate each term in polar coordinates by

    partial_x=cos(theta) partial_r-sin(theta) partial_theta/r,
    partial_y=sin(theta) partial_r+cos(theta) partial_theta/r.

At total derivative order d write a term as r^(-d)(1+r^2)^p t^k cos(n theta), or its sine version. Its radial Euler derivative is

    [2k-d+2(p-k)t] r^(-d)(1+r^2)^p t^k.

The angle products split into frequencies n+1 and n-1. At d=4 the radial prefactor becomes w^(j+1)t^(k-2). Smoothness cancels all negative powers of t exactly. Replace cos(2m theta) by the Chebyshev polynomial T_m(z) and sin(2m theta) by sqrt(1-z^2) U_(m-1)(z). This proves(1) by finite exact algebra, without interpolation.

The radial velocity quotient e=u.X/r^2 is also regular at t=0 as an angle-dependent function. Since psi=chi_xy and u=grad-perp psi,

    e=-partial_theta chi_xy/r^2.

The same recurrence stopped at d=2 followed by the angle derivative and division by r^2 yields

    e=sum_j w^(j+1) P_e,j(t,z).                 (2)

There are no negative t powers: chi_xy has no constant or linear Taylor term and is O(r^2). The possible angle dependence at r=0 is harmless because e always occurs multiplied by t below.

## 3. Matrices and norms

Direct substitution gives the exact formulas

    M=(2c+1)I+[[-2chi22-chi04,chi31],[chi31,chi22]],
    M1=[1-t(c+e)/5]I+[[-chi04,chi13],[chi13,-chi22]],
    M2=[1-c+(16/5)t(c+e)/(1+3t)]I
       +[[chi22-chi04,(-chi31+3chi13)/2],
          [(-chi31+3chi13)/2,-2chi22]].          (3)

The first-derivative norms satisfy

    |Du|^2=2chi22^2+chi13^2+chi31^2,
    |D rho|^2=(chi31+chi13)^2+(chi22+chi04)^2.  (4)

In(4), combinations can be formed before interval evaluation to preserve cancellation. The square and sum operations are then directed. Reflection changes the signs of chi31 and chi13 together and preserves all targets.

## 4. Complete interval proof

The compactified first quadrant is [0,1] times[-1,1]. On every rational rectangular cell express the polynomials in tensor Bernstein form. For the branch variable use its exact containing interval [(1-t_hi)^(delta/2),(1-t_lo)^(delta/2)] and the degree-six Bernstein representation of the sum of its six powers. Nonnegativity and partition of unity of all Bernstein bases enclose every field in(1)-(2). The factor sqrt(1-z^2) has its exact interval enclosure. At t=1 all fields vanish since delta>0; the formulas have their continuous limits there.

For a symmetric matrix with diagonal lower bounds a,b and off-diagonal absolute bound C, a lower eigenvalue bound is

    (a+b-sqrt((a-b)^2+4C^2))/2.

The alternative min(a,b)-C is also valid. The larger of these two directed bounds can be used. A cell is accepted for a target only if the entire directed bound meets that target. Binary64 may guide subdivision but cannot accept a cell.

Every rejected cell is bisected exactly along one coordinate. A successful certificate consists of finitely many accepted leaves covering the initial rectangle with disjoint interiors. The independent checker reconstructs the binary tree, checks the rational endpoints and reevaluates each leaf directly from the original power coefficients at a different precision. This proves the corresponding inequality for every point of the full plane. A finite point comparison checks implementation conventions but does not replace the complete partition.

## 5. What this would imply

Together with the independent remaining decay and derivative hypotheses, these matrix and first-derivative bounds can supply part of the reference contract in topics85,88,89. Adjustable higher-derivative caps in91 do not replace the remaining five fixed derivative bounds or the four decay bounds. Even a complete reference contract for a refit would leave the certified residual exclusions unchanged. No existence claim follows from this certificate alone.

For M2 one may first multiply M2-(I/2) by the strictly positive denominator1+3t. This gives a polynomial numerator plus the same six w powers. For M1 and M the denominator is1. The scalar parts and the t e term may be combined with each matrix entry before computing its Bernstein enclosure. This retains algebraic correlation and proves exactly the same matrix inequalities.

## Remaining fixed derivative and decay hypotheses

The same exact polar recurrence computes the third derivatives chi_xyy, chi_xxy and fifth derivatives chi_xxxxy, chi_xxxyy, chi_xxyyy, chi_xyyyy, chi_yyyyy. After cancellation of the zero coefficients at lower radial powers, third derivatives have the form r times sum_j w^(j+1) P_j(t,z), and fifth derivatives have the form sqrt(t(1-t)) times sum_j w^(j+1) P_j(t,z). Each P_j includes either cos(theta) or sin(theta); removing this factor leaves a rational polynomial in t,z, by the odd Chebyshev identities. These identities hold by continuity at r=0.

With full ordered Cartesian tensor norms,

    |Du|^2 = 2 chi22^2 + chi13^2 + chi31^2,
    |D rho|^2 = (chi31+chi13)^2 + (chi22+chi04)^2,
    |D2u|^2 = chi41^2 + 3 chi32^2 + 3 chi23^2 + chi14^2,
    |D2rho|^2 = (chi41+chi23)^2 + 2(chi32+chi14)^2 + (chi23+chi05)^2.

Thus the fixed bounds |Du|<=14/5, |D rho|<=16, <r>|D2u|<=3, |D2rho|<=3 and <r>|D2rho|<=8 are finite interval inequalities on the same compactified rectangle. The first two use fourth-derivative fields as above. The last three use the fifth-derivative polynomials, with the factors sqrt(t) or sqrt(t(1-t)) required by the displayed identities. Correlated sums such as chi41+chi23 must be formed before interval evaluation.

For d=4/9 set F_d(t)=t^(d/2)(1-t)^((delta-d)/2). The reference exponent has delta>d, so 0<=F_d<=1. Write S_m for the derivative-m field with its common w factor removed, keeping its angular factors. Then the decay quantities are

    r^(d-1)|u| = F_d |S_3|,
    r^d|Du| = F_d |S_4,u|,
    r^(d+1)|D2u| = F_d t |S_5,u|,
    r^d(|D rho|+r|D2rho|) = F_d (|S_4,rho|+t|S_5,rho|).

For each sum the remaining branches are 1,w,...,w^5. These identities reduce the four decay bounds to interval inequalities as well. Dropping F_d gives a valid upper bound, although direct interval evaluation may be sharper. A completed directed cover and independent recheck are required separately for every asserted cap. These formulas alone are not numerical certificates.

The weaker matrix target M>=5I/2 is also sufficient for the low hypothesis in85 and89. Indeed, on r<=R the required lower bound is at most2/5+(11/10)c; using c<=37/20, this is at most487/200<5/2. A certificate of this weaker target must be labeled with its actual target and does not assert M>=19I/5.

## Optional correlated radial enclosure

A second valid enclosure retains the relation between t and the branch powers. On a cell [a,b] with b<1, put s=(t-a)/(b-a). For q>=0 let T_N(s) be the degree-N Taylor polynomial of (1-t)^q about t=a. For N>=q, its uniform remainder is bounded by

    R_q = |q(q-1)...(q-N)| (b-a)^(N+1)
          (1-b)^(q-N-1)/(N+1)!.

For integral q<=N the remainder is zero. The coefficient of s^l is (-1)^l binom(q,l)(b-a)^l(1-a)^(q-l). This is the ordinary Taylor theorem with the maximum absolute (N+1)st derivative on the cell. All powers and coefficients may be enclosed by directed arithmetic.

If a branch polynomial has degree-n Bernstein coefficients p_i(z) in s, and T_N has degree-N Bernstein coefficients v_l, then the product has coefficients

    sum_(i+l=k) [binom(n,i)binom(N,l)/binom(n+N,k)] p_i(z)v_l.

This follows by multiplying the Bernstein basis functions exactly. Sum these product coefficients over branches before taking their convex hull. The error is at most sum_j R_(q_j) sup_cell |P_j|, with the latter supremum bounded by the original Bernstein coefficients. Use one such error for each matrix entry or scalar field. On cells touching t=1, the previous independent branch-variable enclosure remains available. Each is an enclosure of the same exact field, so their intersection or the better resulting lower bound is valid. This refinement changes no target or acceptance rule.
