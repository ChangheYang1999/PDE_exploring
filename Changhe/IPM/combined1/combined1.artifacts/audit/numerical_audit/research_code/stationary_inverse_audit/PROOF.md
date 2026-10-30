# Finite angular inverse and the order-eight small divisor

## Statement and hypotheses

Let c=4076476460239181/2251799813685248, gamma=1/c, delta=1-gamma, alpha_j=gamma-j delta, and s_j=alpha_j+3. For 0<=j<=16, let V_j be the span of cos(2m theta), 0<=m<=10(j+1)-1, and W_j the span of sin((2m+1)theta) with the same index range. The map

    C(theta) -> r^(-alpha_j)[-partial_y Delta(r^s_j C(theta))]

is an isomorphism V_j to W_j. The stationary homogeneous recurrence with fixed leading potential therefore has a unique solution in these finite angular spaces through order16.

For any real s different from0 and2, the pure homogeneous density G r^(s-3) sin(theta) has the unique radial potential chi=-G r^s/[s^2(s-2)]. With stream function psi=chi_xy and velocity U=(-psi_y,psi_x), its circle norm amplification is

    ||U(1,.)||_L2 / ||rho(1,.)||_L2
       = sqrt(1+(s-2)^2/4)/|s|.                         (1)

This is an algebraic statement on r>0. It does not identify a whole-plane Riesz transform of the singular density or prove convergence of an infinite expansion.

## Complete argument

The polar Laplacian maps r^s cos(n theta) to (s^2-n^2)r^(s-2)cos(n theta). Applying -partial_y, using partial_y=sin(theta)partial_r+cos(theta)partial_theta/r, gives coefficients

    -(s^2-n^2)(s-2-n)/2 at sin((n+1)theta),
     (s^2-n^2)(s-2+n)/2 at sin((n-1)theta)

for positive even n. For n=0 both signed-frequency terms combine into -s^2(s-2)sin(theta). In increasing frequency order the highest output frequency of each input is n+1. Descending elimination therefore solves the square system as soon as every displayed highest-frequency coefficient is nonzero. Their roots are even integers.

Writing p=4076476460239181 and d=1824676646553933 gives s_j=4-(j+1)d/p. Since gcd(p,d)=1 and 1<=j+1<=17<p, these s_j are nonintegral. All1530 diagonal coefficients are nonzero. The resulting map is invertible.

The stream from branch i has even angular frequencies at most20(i+1), while the density from branch k has odd frequencies at most20(k+1)-1. The velocity-density coupling equals

    U_i.grad rho_k=(psi_(i,r) rho_(k,theta)-psi_(i,theta) rho_(k,r))/r.

For i+k=j-1 its degree is alpha_j and its highest frequency is at most20(j+1)-1. It thus belongs to W_j. The linear coefficient is c alpha_j-1=-j(c-1), nonzero for j>=1. Induction determines the density forcing and then the potential uniquely at each stage.

For the pure first sine density, direct differentiation of chi gives

    psi=-G r^(s-2)sin(2theta)/(2s),
    U_r=G r^(s-3)cos(2theta)/s,
    U_theta=-(s-2)G r^(s-3)sin(2theta)/(2s).

The polar components are orthogonal in physical space and each trigonometric square integrates to pi. The density square also integrates to pi G^2, proving (1).

At order8, s_8=-116183978028673/4076476460239181. The small magnitude of this exact rational number causes the factor in (1) to be close to50. For a general potential with coefficients C_n at cos(n theta), only C_0 and C_2 contribute to the first density mode, and only C_0 and C_4 contribute to the second stream mode:

    G_1=-s^2(s-2)C_0+s(s^2-4)C_2/2,
    Psi_2=s(s-2)C_0/2-(s+4)(s+2)C_4/4.

These identities follow from the same differentiation formulas. The verification reads the independently computed N4 order-eight potential and applies the angular differential algebra, then compares with the frozen T4 values. It also tests each diagonal coefficient through all seventeen angular spaces. Neither the smallest diagonal entry nor (1) is asserted to be the full matrix condition number.

## Dependencies and scope

The potential and density coefficients are from the exact finite recurrence independently compared with N1 in N4-098. The arithmetic path uses the existing angular differentiation functions, then outward Arb square roots. The T4 proof, checker, selected data and output are frozen in source/. The new verification establishes the finite algebra and local homogeneous diagnostic only. It gives no remainder bound, no full-plane lower norm and no all-order growth estimate.
