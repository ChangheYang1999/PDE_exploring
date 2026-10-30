# Exact homogeneous negative norm of finite odd radial Fourier profiles

## Statement

Let F be real and S1-symmetric. Suppose it is a finite sum

F(r,theta) = sum_{n positive odd} f_n(r) sin(n theta),
f_n(r) = r sum_i u^(b_i) P_i(t),
t=r^2/(1+r^2), u=1-t,

where b_i are rational and P_i are rational polynomials. The indices i are local to each n. Put m=(n-1)/2. Assume P_i is divisible by t^m, as required by smoothness of that angular component at the origin. After extracting all factors (1-t)^q from P_i/t^m and adding q to b_i, assume b_i>3/2 for every nonzero term. Define rational polynomials

Q_i(u) = P_i(1-u)/(1-u)^m,
A_i(u) = (1-u)^n Q_i(u),
D_i(u) = sum_{l>=0} [u^l]Q_i(u) * u^l/(b_i+m-1+l).

Here the extracted endpoint factor is absent from Q_i and already incorporated in b_i. Then

||F||_Hdot^-1^2 = pi sum_n (1/(4n)) sum_{i,j} sum_{k>=0}
                    [u^k](A_i D_j)/(b_i+b_j-3+k).

All denominators displayed in D_i and the final sum are positive. In particular the squared norm divided by pi is exactly rational. The formula includes arbitrary rational coefficients and cancellations; it is not a quadrature rule.

## Radial Green function

For a fixed n>0 the decaying regular solution of -Delta phi=f_n(r) sin(n theta) is

phi_n(r) = [r^-n I_n(r) + r^n J_n(r)]/(2n),
I_n(r)=integral_0^r s^(n+1) f_n(s) ds,
J_n(r)=integral_r^infinity s^(1-n) f_n(s) ds.

This follows by variation of parameters from the two homogeneous solutions r^n and r^-n, whose radial Wronskian is -2n/r. Differentiation verifies the equation and the endpoint choices. The hypotheses give smoothness at zero and f_n=O(r^(1-2b_min)) with b_min>3/2 at infinity. They imply finiteness of the double Green integral: in the region 0<s<r<1 smoothness gives f_n(s)=O(s^n); in 1<s<r the outer integrand is bounded by r^(1-n)|f_n(r)| times integral_1^r s^(n+1)|f_n(s)| ds, which is integrable when every pair of b values has sum>3. The mixed region is also integrable. Thus F belongs to Hdot^-1 and all changes of order below are legitimate, including for signed terms.

Full-circle orthogonality gives

||F||_Hdot^-1^2 = pi sum_n integral_0^infinity f_n(r) phi_n(r) r dr.

The two Green-function contributions are equal by interchanging the inner and outer variables. Therefore the n-th contribution is

(pi/n) integral_0^infinity r^(1-n) f_n(r) I_n(r) dr.

This equality can also be obtained first on compact radial truncations and then by the absolute convergence just proved.

## Elementary antiderivative and exact integration

For a single inner term i, f_i=r t^m u^(b_i) Q_i(u). With u=1/(1+r^2),

s^(n+1) f_i(s) ds = -(1/2) (1-u)^n u^(b_i-m-3) Q_i(u) du.

If A_i(u)=sum_k a_ik u^k, then

I_i(r) = (1/2) sum_k a_ik (1-u^alpha_ik)/alpha_ik,
alpha_ik=b_i-m-2+k.

When alpha_ik=0, the quotient is interpreted as -log u. For an outer term j,

r^(1-n) f_j(r) dr = -(1/2) u^(b_j+m-2) Q_j(u) du.

For X=b_j+m-1+l>0 and X+alpha_ik=b_i+b_j-3+k+l>0,

integral_0^1 u^(X-1) (1-u^alpha)/alpha du = 1/[X(X+alpha)].

This identity is direct integration when alpha is nonzero, and the logarithmic integral when alpha=0. Substitution into the Green formula yields

(pi/(4n)) sum_{i,j,k,l} a_ik [u^l]Q_j /
                [(b_j+m-1+l)(b_i+b_j-3+k+l)].

Grouping by k+l gives the polynomial formula in the statement. It avoids cancellation between singular intermediate antiderivative terms and does not divide by alpha.

## Applicability to the potential family

The exact residual recurrence in ../whole_plane_norms/PROOF.md supplies f_n=r sum u^(ell delta/2) P[ell,n](t). Each n is positive odd. The algorithm checks the divisibility by t^m exactly and extracts the endpoint order of each resulting polynomial. For the admissible references, vanishing of every residual sector with exponent at least -2 gives b_i>3/2 after extraction. Distinct branch exponents are checked for nonresonance by the sector audit. For an input that fails these checks the algorithm does not assert a finite negative norm.

## Independent explicit checks

For n positive odd and phi=r^n(1+r^2)^(-n) sin(n theta), direct differentiation gives

-Delta phi = 4n(n+1) r^n (1+r^2)^(-n-2) sin(n theta).

Directly integrating F phi gives

||F||_Hdot^-1^2/pi = 2n(n+1) B(n+1,n+1)
                    = 2n(n+1)(n!)^2/(2n+1)!.

These examples test the Green prefactor, origin exponent, full-circle normalization, and high angular modes independently of the potential differentiation code. For F=r(1+r^2)^(-3) sin(theta), the exact value is pi/96, since the Poisson solution is r(1+r^2)^(-1) sin(theta)/8.

## Scope and dependencies

Dependencies are Fourier orthogonality, the elementary radial Poisson Green function, polynomial algebra, and integrals of powers and a logarithm. The formula concerns the actual Hdot^-1 norm with Fourier multiplier |xi|^-1 and the standard spatial L2 normalization. It is sharper than the harmonic Hardy proxy. It does not establish any inverse or nonlinear closure theorem. No formal proof-assistant build is performed.

## Signed cross-term check family

A second independent identity tests nonconstant radial polynomials, branch interactions, and near-threshold noninteger exponents. For n odd, a>n/2, and phi_a=r^n(1+r^2)^(-a)sin(n theta), direct differentiation gives

-Delta phi_a = 4a r^n(1+r^2)^(-a-2)[(n+1)+(n-a)r^2]sin(n theta).

Writing m=(n-1)/2 and b=a+1-m puts this in the required form, with radial factor t^m[(n+1)-(a+1)t] and b>3/2. For a second exponent c>n/2, direct integration gives

integral (-Delta phi_a) phi_c / pi
= 2a [(n+1) B(n+1,a+c+1-n) + (n-a) B(n+2,a+c-n)].

Both Beta functions have positive second argument and positive integer first argument, so they equal rational products when a,c are rational. Bilinearity supplies the exact energy of any signed finite sum of these potentials. The independent test uses three signed branches, the actual case4 delta, and n=1,3,7,21,59. This tests the full cross-term normalization rather than only a single monomial branch.

## Certified ball evaluation of the finite formula

The exact rational formula may create large intermediate common denominators. It can instead be evaluated by replacing every rational coefficient and every rational exponent denominator by an outward ball enclosure, then performing the finite polynomial products and sums in Arb. No quadrature or infinite truncation is introduced. Provided the resulting squared-energy ball has positive lower endpoint, its square root encloses the norm. The exact rational calculation for selected angular modes supplies a separate arithmetic comparison. Increasing precision changes only the width of the certificate, not the expression being evaluated.
