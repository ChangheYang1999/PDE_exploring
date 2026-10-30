# Candidate 020 exact origin normalization: independent acceptance

## Statement and hypotheses

Fix c=4076476460239181/2251799813685248 and the exact rational potential
of C1-N1-020-legqs25p50-quot013, raw SHA256
bddbd3120852a815cfe850635564cb09ab52a98ec596a4cce3b72c98cf04f7cf.
Set gamma=1/c, delta=1-gamma, rho=-partial_y Delta chi and
u=(-partial_xyy chi,partial_xxy chi). The existing canonical-potential
identification is assumed; this local calculation does not reprove it.
The exact claim is c+partial_y u2(0)=1 and partial_y rho(0)>0.
Its exact slope and an outward decimal interval are stored in the result.
It asserts no stationary solution, global bound or inverse.

## Complete local argument

Write z=x^2+y^2, H_m=Re((x+iy)^(2m)) and
p_j=(3+gamma-j delta)/2. A generator is
H_m (1+z)^(p_j-m) t_R^w u_R^Q P_N(2t_R-1),
where t_R=z/(R^2+z), u_R=R^2/(R^2+z), R>0 and w,Q,N>=0.
The mono case has N=Q=0 and R=1; the ordinary Legendre case has Q=0,R=1.
Let A_N(Z)=(1+Z)^N P_N((1-Z)/(1+Z)). The Legendre recurrence constructs
this finite polynomial exactly. The radial coefficient after H_m is

 (-1)^N R^(-2w) z^w (1+z)^(p_j-m)
 A_N(z/R^2) (1+z/R^2)^(-w-Q-N).

This identity follows by P_N(-x)=(-1)^N P_N(x). All factors are analytic
at zero, so finite Taylor convolution gives exact coefficients. Only
the coefficient of z^(2-m) can affect fourth derivatives. Terms with
m+w>2 vanish to order at least six. Sum the remaining exact coefficients
into B_m for m=0,1,2. Since H_0=1, H_1=x^2-y^2 and
H_2=x^4-6x^2y^2+y^4, the homogeneous quartic part is

 (B0+B1+B2)x^4+(2B0-6B2)x^2y^2+(B0-B1+B2)y^4.

If its coefficients are A40,A22,A04, direct differentiation gives
partial_y u2(0)=4A22 and partial_y rho(0)=-4A22-24A04.
Every higher Taylor term has zero fourth derivative at zero; lower terms
also have zero fourth derivative. These exact finite identities prove
the normalization and slope claim once the rational checks pass.

## Independent path and verification

N4 reconstructs the local coefficients by the homogenized Legendre
recurrence above. T4-361 instead expands the shifted Legendre polynomial
as sum_k (-1)^(N+k) binom(N,k) binom(N+k,k) t_R^k, then convolves its
two binomial series. Both derivations are exact, with no differentiation
step size or quadrature. Read and freeze T4's full proof, code and input
hashes without executing its code. Recompute the own origin coefficients
and all three quartic coefficients, compare all four exact fields with
both independent records, count every contributing raw generator and
summand, and check the strict slope interval with outward Arb arithmetic.
The input is exact JSON; no numeral table is manually transcribed.
The local generator proof is ../generator_sector_audit/PROOF.md. Every
executed local dependency and frozen peer source is bound by SHA256.
