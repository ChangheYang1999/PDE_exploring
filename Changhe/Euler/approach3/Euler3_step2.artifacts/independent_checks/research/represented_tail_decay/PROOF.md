# Decay and source moments for the finite rotating basis

Status: proved statement about the exact finite representation defined below. It is not a statement that rounded field or derivative tables satisfy the same identities.

## Statement and notation

Fix positive real numbers R0 and R1, a nonnegative integer k, and a finite collection of real regular solid harmonics H_lm of degrees l>=1, with their real sine/cosine partners. The index m satisfies 0<=m<=l. The main collection may have l<=6; any finite higher degrees already present in the correction channels are allowed. Coefficients omitted from a channel are zero.

Let K be a compact subset of (2/5,1/2) times (0,infinity), and let every radial polynomial coefficient be a real C1 function of (c,w) on an open neighborhood of K. All polynomials have fixed finite degree. R0, R1, k and the harmonic index sets are independent of (c,w). Set

alpha(c)=(1-c)/c, kappa(c,w)=w/c,
alpha_* = min_K alpha(c), alpha^* = max_K alpha(c).

Then 1<alpha_*<=alpha^*<3/2. For x in R3, define

r=|x|, s=(r^2+R0^2)^(1/2), b=s/R0,
xi=2(s-R0)/(s+R0)-1, d=(r^2/(r^2+R1^2))^k,
psi=kappa log(b).

For k=0 define d=1, including at x=0. Let H_lm^psi(x) be the real harmonic H_lm evaluated at the rotation of x through psi about the third axis. Reversing the common sign of this rotation gives the same decay statement. For each harmonic index let A_lm, C_lm, B_lm, D_lm and E_lm be the fixed finite radial polynomials in xi, with their parameter-dependent coefficients. Define the scalar potentials

T(x)=sum_lm H_lm^psi(x) [b^(-alpha-l) A_lm(xi)
                              + d b^(-2alpha-1-l) B_lm(xi)],

S(x)=sum_lm H_lm^psi(x) [b^(1-alpha-l) C_lm(xi)
                              + d b^(-2alpha-l) D_lm(xi)]
       + sum_(l>=2,m) H_lm(x) d b^(-2l-1) E_lm(xi),

and U=curl(Tx)+curl curl(Sx). All derivatives in this statement are derivatives of these exact functions.

For every nonnegative integer j and every beta with 1<beta<alpha_*, there is a finite constant C_j,beta,K such that, for all (c,w) in K and x in R3,

|D^j U(x;c,w)| + |D^j partial_c U(x;c,w)|
                + |D^j partial_w U(x;c,w)|
 <= C_j,beta,K (1+|x|)^(-beta-j).

Here D^j is the full jth Cartesian derivative tensor with its Euclidean component norm. The constant may depend only on j, beta, K, R0, R1, k, the finite harmonic functions and polynomial degrees, and bounds on the coefficients and their first parameter derivatives on K. No uniformity is asserted as c approaches 1/2 or as w becomes unbounded.

The field U and each first parameter derivative are smooth in x and divergence free. Consequently, for f=tr((DU)^2) and f_p=2tr(DU D(partial_p U)), p=c,w, all of the following integrals are absolutely convergent and vanish:

integral_R3 f dx = integral_R3 x_i f dx = 0,
integral_R3 f_p dx = integral_R3 x_i f_p dx = 0, i=1,2,3.

## Proof of uniform derivative bounds

For r>=1, s is bounded above and below by positive constants times r. Its exact formula and repeated differentiation imply, for each j>=1,

|D^j log(b)| <= C_j r^(-j),
|D^j xi| <= C_j r^(-j),
|D^j d| <= C_j r^(-j).

The zeroth derivatives of xi and d are bounded. One way to see all the derivative estimates without a coordinate singularity is to write x=r n on annuli r<=|x|<=2r, rescale x=r z with 1<=|z|<=2, and differentiate the smooth functions of z, R0/r and R1/r. The latter two variables range over compact intervals; their denominators stay positive since |z|>=1. Each Cartesian derivative contributes a factor r^(-1). For log(b), separate the constant log(r/R0) before differentiating. For xi use xi=1-4R0/(s+R0). These observations also cover every finite derivative order that follows.

The quantities alpha, kappa and their first parameter derivatives are bounded on K. If a(c,w) is any of the exponents occurring in T or S, differentiation of b^a gives products of b^a, derivatives of log(b), and bounded polynomials in a. Hence

|D^j b^a| <= C_j r^(a-j),
|D^j partial_p(b^a)| <= C_j (1+log r) r^(a-j).

Constants are uniform on K because a has compact range and R0 is fixed. The same bounds apply when an exponent is parameter independent, with the parameter derivative then zero.

Homogeneity gives |D^j H_lm(x)|<=C_j r^(l-j). The rotation formula for a real harmonic is a sum of H_lm(x) cos(m psi) and its partner times sin(m psi). Spatial derivatives of psi of positive order are O(r^(-j)). Its parameter derivative is a bounded multiple of log(b), so it is O(1+log r); its positive spatial derivatives are O(r^(-j)). The product and chain rules therefore give

|D^j H_lm^psi(x)| <= C_j r^(l-j),
|D^j partial_p H_lm^psi(x)| <= C_j (1+log r) r^(l-j).

For l=0 or a missing partner the corresponding zero terms cause no problem, although this statement only requires l>=1. Finite radial polynomials in xi have uniformly bounded zeroth derivatives and D^j bounds O(r^(-j)); their first parameter derivatives obey the same bounds because the coefficient derivatives are bounded. Combining these estimates term by term, the potentials in each channel have the following bounds, where the exponent sigma describes |D^j potential|<=C_j r^(sigma-j):

| Channel | Potential | sigma |
| --- | --- | --- |
| A | T | -alpha |
| C | S | 1-alpha |
| B | T | -2alpha-1 |
| D | S | -2alpha |
| E, degree l>=2 | S | -l-1 |

Each first parameter derivative has the same bound with an additional factor 1+log r. This statement remains true when coefficients themselves vary, by the product rule.

For any smooth T and S, Cartesian differentiation gives

curl(Tx)=grad(T) cross x,
curl curl(Sx)=2 grad(S)+(D^2 S)x-x Delta(S).

Thus a T-channel with potential exponent sigma contributes a velocity with exponent sigma. An S-channel contributes exponent sigma-1. After j further derivatives, the velocity exponents are respectively

-alpha-j for A and C,
-2alpha-1-j for B and D,
-l-2-j for E.

Since alpha is between 1 and 3/2 and l>=2 in E, every correction channel decays faster than the main channels. Finite summation yields, uniformly on K and r>=1,

|D^j U| <= C_j r^(-alpha_*-j),
|D^j partial_p U| <= C_j (1+log r) r^(-alpha_*-j).

Put delta=alpha_*-beta>0. The elementary maximum

sup_(r>=1) (log r) r^(-delta)=1/(e delta)

implies (1+log r)r^(-alpha_*)<=(1+1/(e delta))r^(-beta). Also r^(-beta-j)<=2^(beta+j)(1+r)^(-beta-j) for r>=1.

On |x|<=1, all scalar factors are smooth in x: s and the denominators are positive, the powers are powers of positive functions, xi is smooth in r^2, and psi is smooth in r^2. The solid harmonics are polynomials. Since k is a nonnegative integer, d is smooth even at the origin. The coefficient functions are C1 in parameters. Compactness of the unit ball times K gives finite bounds on every spatial derivative and its first parameter derivative. Increasing C_j,beta,K to cover this compact region proves the global assertion. It also justifies commuting the required spatial and first parameter derivatives.

## Proof of the moment conclusion

A curl has zero divergence. Commuting spatial derivatives with the parameter derivative shows div(partial_p U)=0 as well. The preceding bounds with j=0 and1 give the hypotheses of the moment argument below, with the same beta>1.

For a C2 solenoidal field V and W with |V|+|W|=O((1+r)^(-beta)) and |DV|+|DW|=O((1+r)^(-beta-1)), define B_ij=V_i W_j+W_i V_j. Direct differentiation gives

sum_ij partial_i partial_j B_ij=2tr(DV DW).

Both this source and x_k times this source are integrable since they are O((1+r)^(-2beta-2)) and O((1+r)^(-2beta-1)). Integrating over the radius-R ball expresses its zeroth moment as a boundary integral of size O(R^(1-2beta)). Multiplying by x_k and integrating by parts again expresses its first moment as two boundary integrals, each O(R^(2-2beta)). All tend to zero. Taking V=W=U and dividing by two proves the moments of f. Taking V=U and W=partial_p U proves those of f_p. The detailed constants and integration-by-parts calculation are also given in ../pressure_moments/PROOF.md.

## Dependencies and scope

This proof uses only the explicitly displayed finite potential representation and elementary differentiation, compactness and the divergence theorem. The potential-to-velocity identities are derived independently in ../field_reconstruction/PROOF.md. The parameter-dependent reduced tail map is handled in ../tail_coordinates/PROOF.md: its coefficients meet the present C1 hypothesis on a neighborhood where the chosen elimination block is nonsingular. This result does not assert that an arbitrary singular elimination or changing mode list is differentiable.

The displayed formula matches the channel exponents in independent/src/primary_exchange.py at the time recorded in verification/source.json. It includes the untwisted E channel only for l>=2, and does not add a harmonic pressure term. The conclusion permits the exactly equivalent ell=0,1 exterior-moment formulas of ../pressure_moments/PROOF.md for the exact Newton pressure. It does not bound errors in a finite angular projection or numerical quadrature. Raw computed moments must still be reported as consistency diagnostics. No moment of order two or greater, rotating Euler solution, or numerical accuracy certificate is asserted.
