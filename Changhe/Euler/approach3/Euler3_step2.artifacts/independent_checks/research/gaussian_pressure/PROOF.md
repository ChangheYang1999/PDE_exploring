# An exact non-axisymmetric Gaussian pressure check

Status: proved identity for a manufactured family. This family is a pressure test, not an Euler profile and not a new optimization basis.

Let c>0 and w>0, let a=1+0.3c+0.2w, let lambda=1+0.1c+0.05w, and put k=2 lambda. Fix b=(1,2,3)/sqrt(14), B y=b cross y, F(y)=exp(-k|y|²), and U(y)=a exp(-lambda|y|²)B y on R³. All functions are smooth. U is divergence free because tr B=0 and y dot By=0. It is non-axisymmetric relative to the prescribed vertical rotation axis since b is not parallel to that axis.

The exact pressure source and its parameter derivatives are

f=tr((DU)²)=a² F Q, Q=-2|b|²+4lambda(|b|²|y|²-(b dot y)²),

fp=2a ap F Q+a² F lambdap[4(|b|²|y|²-(b dot y)²)-2|y|²Q].

Here (ac,aw)=(0.3,0.2) and (lambdac,lambdaw)=(0.1,0.05).

Define, for r>0,

G(r)=sqrt(pi) erf(sqrt(k)r)/(4 k^(3/2) r),

and extend G smoothly by G(0)=1/(2k). Then the unique decaying Newton pressure of U is

P(y)=-a²/(2k)[|b|² F(y)+(b dot grad)²G(|y|)].

In particular, P(0)=-a²|b|²/(3k) and grad P(0)=0. Differentiating this explicit formula in c or w gives the exact pressure derivative for comparison to integration of fp.

## Proof

The matrix derivative is DU=a exp(-lambda r²)[B-2lambda(By)y^T]. The identity B²=bb^T-|b|²I yields tr(B²)=-2|b|² and y^T B(By)=(b dot y)²-|b|²r². The square of (By)y^T has trace (y dot By)²=0. Taking the trace of the square gives the stated source. Its parameter derivative follows by the product rule.

Direct differentiation gives Delta F=(4k²r²-6k)F and (b dot grad)²F=[4k²(b dot y)²-2k|b|²]F. Hence

f=a²/(2k)[|b|² Delta F-(b dot grad)²F].

The radial Newton equation -(r²G')'=r² exp(-kr²), regularity at zero, and decay at infinity give the displayed expression for G by elementary Gaussian integration. Thus -Delta G=F. Applying -Delta to the displayed P and commuting the constant directional derivative with Delta yields exactly f. Its terms decay: F exponentially and the second derivative of G like r^-3. The companion Newton-pressure uniqueness argument therefore identifies P as the required full-space pressure.

For the origin, the convergent series

G(r)=(1/(2k)) sum over n>=0 of [(-k)^n r^(2n)/(n!(2n+1))]

gives G(r)=1/(2k)-r²/6+O(r⁴). Thus (b dot grad)²G(0)=-|b|²/3, giving the stated P(0). P is even, so grad P(0)=0. Parameter differentiation is justified either by this analytic formula or by the uniform Gaussian majorants in the companion pressure proof.

## Dependencies and scope

The proof uses the radial Laplacian, the derivative of erf, the cross-product matrix identity, and uniqueness of a decaying Newton potential. It supplies an exact pressure and pressure-derivative reference with non-axisymmetric velocity and nonzero exterior Green contributions. It does not establish that U satisfies the momentum equation.
