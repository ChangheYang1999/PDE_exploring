# What the vertex map-scale samples establish

## Statement and hypotheses

For the two stored native-source fields at beta=3.0952, lambda=0.989973 and map scales L=1 and L=1.5, distinguish the scalar printed during the solve from the center mismatch of the serialized coefficients. The latter is defined by the ordinary relative inverse center strain c, m=c-1-beta/2. Exact binary scalar parameters, raw binary coefficients, and the independently regenerated binary knot vector define the mathematical spline field used here. No claim is made about historical floating execution or a limiting continuum solution.

The mismatch difference of the stored fields is strictly greater than4e-7. Thus a4e-7 agreement assertion does not apply to these serialized field mismatches. The two printed solve mismatches differ by less than4e-7; this is a statement about those printed values only. A scalar at one prescribed beta and lambda does not determine the location or shape of the minimum-lambda curve, even if a pointwise lambda slope were known. No three-scale stability is established by an unconverged third run.

## Exact moment argument

Use exactly X=(r sin(phi),-r cos(phi)), with t increasing from0 to1 as r increases. Write the divided-vorticity angular expansion G=sum_k D_k(r)cos(k phi), Omega=r sin(phi)G. The center strain is c=(1/pi) integral xy Omega/|X|^4 dX. Here xy Omega/|X|^4 times the area element is -sin(phi)^2 cos(phi)G dr dphi. Since sin(phi)^2 cos(phi)=(cos(phi)-cos(3phi))/4, angular orthogonality gives weights -1/4 and +1/4 for k=1 and k=3. The minus sign comes from the angular coordinates, not from the radial orientation. The represented divided fields are bounded near0 and decay as O(r^(-1-1/beta_basis)) at infinity, so the radial moment integrals converge absolutely. In the recorded r2 map the odd-mode radial factor gives D_k(r)dr=beta_basis L S_k(t)dt. Thus

 c_self=-(beta_basis L/4) integral_0^1 [S_1(t)-S_3(t)]dt.

For a degree-p B-spline B_j on the clamped knot sequence kappa, integral B_j=(kappa_(j+p+1)-kappa_j)/(p+1). This follows from the usual derivative recursion for degree p+1 splines and telescoping over the complete clamped interval; equivalently it is the integral partition identity, already proved and independently controlled in packet160. Inactive leading coefficients are exactly zero as specified by the basis. Hence

 c_self=-(beta_basis L)/(4(p+1)) sum_j (g_(1,j)-g_(3,j))(kappa_(j+p+1)-kappa_j).

The native source has the same formula in its own unchanged beta_seed,L_seed,knot vector. Linearity gives c=c_self+lambda c_seed. Finite sums and products of binary rational inputs are exact rationals; the accompanying independent integer checker sums the two modes in a different order and verifies the source, knots, raw archive hash and decimal enclosures. No inverse matrix is imported.

## Why vertex accuracy does not follow

Even knowing m at this one(beta,lambda) and a nonzero slope in lambda, let m(beta,lambda)=s(lambda-lambda0)+v+A(beta-beta0)+B(beta-beta0)^2 with s nonzero. At the sampled point its value v and lambda derivative s are fixed independently of A and B. The zero curve has derivative lambda_beta=-A/s and second derivative-2B/s at beta0. Its stationary point, when B nonzero, is beta0-A/(2B). Thus neither vertex location nor existence follows from v and s alone. A difference divided by2.9 is only a linearized response under a shared-slope assumption, not a bound on a vertex or root displacement. This argument does not assert that the freely chosen polynomials are actual profile mismatch functions; it refutes inference from the listed scalar data alone.

## Scope

This audit proves statements about exact serialized center moments and logical limits of finite samples. It does not bound inner-solve errors, radial truncation, Jacobian invertibility or a forced branch. It makes no B2 existence or exclusion claim. Dependencies: center angular orthogonality, the r2 variable substitution, the B-spline integral identity and rational arithmetic. Packet190 gives additional independent examples separating sampled differences from point derivatives.
