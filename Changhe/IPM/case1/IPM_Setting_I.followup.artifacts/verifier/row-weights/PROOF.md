# Residual row weights and their interpretation

Date: 2026-10-20. Status: exact elementary identities and counterexamples; supplied-matrix arithmetic independently checked.

For a real matrix D, an orthogonal projection P onto selected residual rows, and lambda>=1, define W_lambda=I+(lambda-1)P. For every coefficient vector v,

    ||W_lambda Dv||² = ||Dv||²+(lambda²-1)||PDv||².

This is the Pythagorean identity for the selected and complementary rows. Thus if f=||PDv||²/||Dv||², the norm ratio for this fixed v is sqrt(1+(lambda²-1)f). The fraction f is squared norm, not norm. Its complementary norm fraction is sqrt(1-f), which is nonzero for f<1. Recomputing a singular vector after changing weights can change the minimizing direction. A fixed-vector formula is not an equality for the smallest singular value. The inequalities ||Dv||<=||W_lambda Dv||<=lambda||Dv|| give sigma_j(D)<=sigma_j(W_lambda D)<=lambda sigma_j(D) by the finite min-max principle. This controls a specified finite matrix and metric only.

Small action in the Euclidean norm of a supplied matrix does not establish a pointwise relative PDE residual: the physical residual, continuum derivative, row normalizer and interpolation error have to be checked separately. Localizing most of a small action in a region does not identify the mechanism of that action or prove it vanishes outside. In particular it does not distinguish transport-only and coupled kernels.

Algebraic convergence of small singular values does not exclude a genuine continuum kernel, even one represented by analytic functions. On R² take A=diag(0,1) and A_N=diag(N^(-3),1). The exact continuum kernel is spanned by the first coordinate, while sigma_min(A_N)=N^(-3) decreases algebraically. This example remains valid if the two coordinates represent two fixed analytic basis functions. A discretization error with this size can mask any approximation rate of a true tangent. Different trial states at different resolutions add another error source.

Nor does C-infinity imply exponential spectral coefficients. The Chebyshev series f(x)=sum_(n>=1) exp(-sqrt(n)) T_n(x) is C-infinity on[-1,1]. For every fixed k, |T_n^(k)|<=n^(2k): derivatives of T_n have nonnegative Chebyshev coefficients, as follows from T_n'=n U_(n-1) and its cosine sum, so their maximum absolute value is their value at1. Differentiating (1-x²)T_n''-x T_n'+n²T_n=0 at1 gives (2k+1)T_n^(k+1)(1)=(n²-k²)T_n^(k)(1), which proves the bound. The sum n^(2k)exp(-sqrt(n)) converges; hence the differentiated series converges uniformly at every finite order. Its coefficients are exp(-sqrt(n)), which are not bounded by C exp(-c n) for any C,c>0. Exponential spectral convergence needs stronger assumptions than smoothness. Even a regularity exponent alone does not determine a discrete action convergence rate without specifying approximation norms and operator consistency.

Executed audit: independently reconstruct the ideal-node row geometry from frozen N,M,L,c_l,beta, read the saved action matrices without importing the numerics evaluator, recompute the row masks, squared fractions and weighted singular values. This confirms their finite matrix arithmetic only. The scalar source location used by those rows remains their supplied value; no canonical root confirmation is silently attributed to this audit.
