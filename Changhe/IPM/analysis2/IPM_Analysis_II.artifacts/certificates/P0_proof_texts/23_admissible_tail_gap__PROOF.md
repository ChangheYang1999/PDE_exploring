# A far-field residual lower bound for the exactly admissible N-B references

Status: analytical proof and numerical lower bounds CONFIRMED by the verifier (V103); independently reviewed CORRECT by the lead (V110). Scope: the two named candidates only.

## Statement, spaces and exact input class

Let rho be the density of an exact finite canonical potential

    chi=sum a_(j,m,k) r^(2k)(1+r^2)^(p_j-k) cos(2m theta),
    p_j=(3+gamma-j delta)/2, gamma=1/c, delta=1-gamma,
    rho=-partial_y Delta chi,
    u=(-partial_x partial_y^2 chi,partial_x^2 partial_y chi).

Here c is the accepted state131 exponent,0<=j<=5,0<=m<=59,m<=k<=75. Coefficients are exact rationals. The canonical velocity convention is the one proved in topic01. Assume that the residual F=(cX+u).D rho-rho has no nonzero sector with radial exponent larger than

    p_star=gamma-6delta=-8696260065638350/4076476460239181,

and that its p_star angular polynomial is E_star(theta)=sum e_m sin(m theta), not identically zero. These finite exact conditions must be checked for the particular input. They hold for the independently audited A2 and A3 references, whose six leading potential branches coincide with the stationary tail determined by the original leading profile. This proof does not impose an unproved uniform bound on all possible free coefficients in the enlarged family.

For R>=1 set w_R=(1+r^2/R^2)^(-11/10), L_R(F)=||w_R F||_(dot H^-1), and N_(s,R)=E_R(J^s F), with the weights, Euclidean derivative norms and completion of topic18. For0<s<=2^-12, the already proved inverse Bessel comparison gives

    N_(s,R)(F)>=2^(53/2)L_R(F)/6.                        (1)

These inputs are smooth symbols of degree p_star<-2 and their derivatives have the corresponding decay. Hence the required spaces and the canonical Bessel comparison apply, by the same completed-space argument as in topic20/RESIDUAL_PROOF.md. Membership is checked before using(1).

## 1. One combined angular test, allowing signed subleading sectors

Choose T>=1 and set chi0(t)=(t-1)^2(2-t)^2 on[1,2], zero elsewhere. Put

    d_m=1/35+m^2/630,
    phi(r,theta)=chi0(r/T) sum_m(e_m/d_m)sin(m theta),
    S=sum_m e_m^2/d_m, A=sum_m |e_m|/d_m.

This is a compact C1 test in homogeneous H1, with the density parity. Exact polynomial integration gives integral chi0=1/30, integral chi0^2=1/630 and integral t(chi0')^2=1/35. Angular orthogonality and1/t<=1 on[1,2] give

    ||D phi||_2^2<=pi S.                                (2)

Suppose a finite exact sector residual F_t=sum_(h,q) r^p E_(h,q)(theta) has the same leading sector E_star, and every other nonzero sector has p<p_star. Write

    C_(h,q)=sum_m e_m E_(h,q,m)/d_m,
    B=sum_(p<p_star) max(0,-C_(h,q)) T^(p-p_star).

If |F-F_t|<=Ctail r^p_star for every r>=T, then each normalized sine coefficient of the error is bounded by(4/pi)Ctail<2Ctail. Consequently the signed angular pairing coefficient obeys

    sum_m(e_m/d_m) F_m(r)/r^p_star
         >= S-B-2 Ctail A=:b, r>=T.                     (3)

Positive subleading cross coefficients are discarded; negative ones are bounded using their decreasing powers. This avoids the unnecessary requirement that every individual leading mode dominate its remainder. Assume b>0.

On T<=r<=2T, w_R>=W=(1+4T^2/R^2)^(-11/10). Since p_star+1<0, the radial factor satisfies t^(p_star+1)>=2^(p_star+1). The power has the opposite sign from the growing-residual test in topic20 and must be retained. Equations(2)-(3) give

    L_R(F)>=sqrt(pi) b T^(p_star+2) W 2^(p_star+1)
                                               /(30 sqrt(S)).    (4)

Every factor is positive. The exact test uses all nonzero leading modes and is a single duality witness, rather than a sum of unrelated norm lower bounds.

## 2. Complete uniform binomial remainder

Retain potential binomial orders0<=q<=Q, where Q=3 and q0=4. For each branch j and order q, form the exact angular potential polynomial by summing a_(j,m,k) binom(p_j-k,q) cos(2m theta). Cartesian differentiation gives the density, velocity, and every derivative through order4. Form F_t by exact polynomial products. All cancellations are performed before taking absolute values.

For d=3,4 let B_(d,j,q) be the maximum component sum of absolute complex Fourier coefficients of that differentiated potential sector. Define

    M_d=sum_(j,q<=Q) B_(d,j,q) T^(-j delta-2q),
    A_j=sum_(m,k)|a_(j,m,k)|,
    tau_d=((q0+76)/(q0+1))
                      *((2q0+130)/(2q0+128))^d/T^2,
    T_d=binom(q0+75,q0)(2q0+128)^d T^(-2q0)
                  sum_j A_j T^(-j delta)/(1-tau_d).      (5)

The actual exact index bounds imply |p_j-k|<76 and

    |3+gamma-j delta|+2m+2(d-1)<128, d<=4.

Thus |binom(p_j-k,q)|<=binom(q+75,q). Each Cartesian derivative multiplies the Fourier coefficient sum by at most2q+128. The omitted-term majorant ratio is at most tau_d, and both rational factors in that ratio decrease with q. Whenever tau_d<1, the geometric sum proves, for r>=T,

    |D^d chi_t|_(each component)<=M_d r^(gamma+3-d),
    |D^d(chi-chi_t)|_(each component)
          <=T_d(T/r)^(2q0) r^(gamma+3-d).               (6)

Density is a sum of two third derivatives and velocity has two individual third derivatives. Therefore the same Euclidean product calculation as in topic20 gives

    |F-F_t|/r^p_star<=Ctail,
    Ctail=(2sqrt(2)c T4+2T3) T^(gamma-p_star)
          +4(T3M4+M3T4+T3T4) T^(2gamma-1-p_star).       (7)

To take the sup at r=T, one uses2q0>gamma-p_star=6delta and2q0>2gamma-1-p_star=5delta. Both strict inequalities hold for the exact exponent. For the product of two omitted tails, discarding one factor(T/r)^(2q0)<=1 is permissible. No uniform coefficient bound other than the finite actual sums A_j is assumed.

Equations(5)-(7) are a full pointwise estimate, not an asymptotic numerical fit. The retained exact residual sectors and actual majorant quantities are stored with the certificate. Independent Cartesian evaluation at large rational-direction points checks their signs and phases; that check supports the implementation but does not replace the uniform proof.

## 3. Independent source reconstruction and verification

The program expands every supplied monomial or Legendre generator using exact integer binomial coefficients and reconstructs the canonical rational vector afresh. It compares the exact source and canonical hashes against the earlier independent admissibility audit. The original leading potential and exponent are independently recovered from the strictly read-only original checkpoint. No numerics producer evaluator or sector code is imported.

The program represents each angular polynomial by Laurent coefficients with explicit powers of i for Cartesian y derivatives, and multiplies them with exact rational polynomial convolution. It verifies the vanishing of every residual sector above p_star, the original leading profile, and the exact equality of the A2/A3 leading residual sectors. It checks all numerical claims with768-bit Arb. The large-point Cartesian evaluation uses a distinct full-potential Taylor expansion, without the exterior series.

## Scope

A lower bound from(4) concerns the specified exact reference and norm. It does not certify a norm upper bound, a uniform obstruction for arbitrarily large coefficients, or nonexistence of an exact solution. Cancellation of the eight sectors above-2 proves membership but does not, by itself, imply quantitative smallness. The purpose of this test is to measure that remaining gap for the supplied admissible references.
