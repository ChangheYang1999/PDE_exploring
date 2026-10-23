# The negative-sign leading inner problem

Result 224. Written independently on 2026-10-21 before the accompanying verifier calculations. This is a theorem about a linear ordinary differential equation arising in a formal hydrostatic expansion. It is not a nonexistence theorem for the hydrostatic profile problem or for full-plane IPM.

## Statement and relation to the profile problem

Fix $0<p<1$ and $\lambda>0$, and put $\mu=(p+1)/2$, $r=p-1/\mu$ and $\theta=z\,d/dz$. Suppose $h\in C^3((0,\infty))$ satisfies

    (theta-p)(theta-r)(theta-p-2)h = -2 lambda h'',          (1)

has $h(z)=O(z^p)$ as $z\to\infty$, and extends evenly to a $C^1$ function at zero. Then $h=0$.

For the negative signed hydrostatic equation, $-\Phi_{yy}=-g_x$, with $g_y(0)=1$, let a proposed smooth homogeneous outer trace have positive axis value $K$. Set $c=1/p$, $D=c-1$, $A=c(1-\mu)$, $n=\mu p$, $q=n+p-1$ and $\lambda=pK/(2\mu^2 A)$. Write a leading density correction as $y^q h(x/y^\mu)$ and its contribution together with the outer velocity cusp as $y^n w(x/y^\mu)$. The leading system is

    A(theta-p-2)h + p K w = 0,
    h'' - mu^2(theta-p)(theta-r)w = 0.                    (2)

The second sign follows from $V_{2,yy}=g_{xx}$ for this signed operator. Eliminating $w$ gives (1). If $C_p$ denotes the cusp coefficient of the positive-sign canonical inverse of the leading outer density, the physical negative-sign velocity has cusp $-C_p|x|^p$. Matching (2) therefore requires the $z^p$ coefficient of $h$ to be $-pKC_p/D$. Under this specific leading ansatz, the theorem forces $C_p=0$ and $h=w=0$. This does not show that every hydrostatic solution admits the ansatz, has the differentiated outer expansion, or has a smooth angular trace. Other scales and full nonlocal matching are not addressed.

The proof below establishes the ODE statement directly. It does not assume the absence of an exponentially small free mode, and does not infer completeness from a sampled special-function computation.

## Reduction and the two admissible modes at infinity

Define

    X=lambda/z^2, a=-p/2, b=(1-p)/2,
    d=1/(p+1), B=1-d=p/(p+1), kappa=a+b-B-2.

Thus $-1/2<a<0$, $0<b<1/2$, $1/2<d<1$, $b-a=1/2$, $a+d>0$ and $b+d>0$. Writing $h=z^p u(X)$ transforms (1) into

    [T(T+B-1)(T+1)-X(T+a)(T+b)]u=0,  T=X d/dX.            (3)

The power series with coefficient ratio $(j+a)(j+b)/[(j+B)(j+2)(j+1)]$ gives

    f1(X) = 2F2(a,b;B,2;X),
    f2(X) = X^d 2F2(a+d,b+d;1+d,2+d;X).                 (4)

At $X=0$, the indicial roots are $0,d,-1$. The first two solutions are independent. The third has nonzero leading term $X^{-1}$, with a possible logarithmic correction at exponent zero. One can see the last fact without assuming a nonresonant formula: the Frobenius recurrence starting at exponent $-1$ has one resonance at zero, resolved by adding a multiple of $f_1\log X$; the leading $X^{-1}$ coefficient remains arbitrary and nonzero for the third independent solution. There are no other resonances since $d\notin\mathbb Z$. The ordinary Frobenius construction for a regular singular third-order equation then gives a complete local basis. Its logarithm contributes only lower order terms. Consequently every solution with $h=O(z^p)$, equivalently bounded $u$ as $X\downarrow0$, has $u=c_1f_1+c_2f_2$. The third mode would give $h$ of order $z^{p+2}$.

This regular singular classification is also the resonant limiting interpretation of NIST DLMF 16.8, especially the equation and fundamental solutions in 16.8.3 and 16.8.6. Here only the two nonresonant functions in (4) are used explicitly.

## A necessary condition for boundedness at the axis

The elementary gamma-ratio asymptotic gives, for fixed real parameters without forbidden denominator poles,

    (a)_j(b)_j/[(B)_j(2)_j]
       = E1*j^kappa*(1+O(1/j)),
    E1=Gamma(B)Gamma(2)/[Gamma(a)Gamma(b)] != 0.

This remains valid for $a<0$: the coefficients for $j\ge1$ have one fixed negative sign. Dividing the entire series by $e^X$ expresses it as an expectation under a Poisson random variable of mean $X$. Splitting at $j=X/2$ and $j=2X$, exponential Poisson tail estimates make the outside contribution negligible compared with any fixed power of $X$. On the middle interval, concentration of $j/X$ at one and the polynomial coefficient bound give the limit by dominated convergence. The finitely many small indices are exponentially negligible. Thus

    f1(X)/(e^X X^kappa) -> E1.

Applying the same argument to the second series and retaining the factor $X^d$ gives

    f2(X)/(e^X X^kappa) -> E2,
    E2=Gamma(1+d)Gamma(2+d)/[Gamma(a+d)Gamma(b+d)] > 0.     (5)

The gamma-ratio input is DLMF 5.11.12; the displayed argument derives the needed positive-axis hypergeometric limit from it. If $h$ is bounded at zero, then $u(X)=O(X^{p/2})$ as $X\to\infty$. Equations (4)-(5) force $c_1E_1+c_2E_2=0$. Hence the subspace permitted by both the infinity condition and axis boundedness has dimension at most one. This is only a necessary exponential cancellation so far; we next construct that line and determine its axis derivative.

## A convergent contour representation of that line

Set

    M(s)=Gamma(-s)Gamma(d-s)Gamma(a+s)Gamma(b+s)/Gamma(2+s),
    C_even=Gamma(a)Gamma(d+a)Gamma(b-a)/Gamma(2-a),
    C_odd =Gamma(b)Gamma(d+b)Gamma(a-b)/Gamma(2-b).         (6)

Choose any vertical line with $-b<\eta<0$. Define for real $X>0$

    G(X)=C_even X^(-a)
           +(1/(2 pi i)) integral_(eta-i infinity)^(eta+i infinity)
                 M(s) X^s ds.                           (7)

The separate term in (7) is essential. The pole $s=-a=p/2$ lies to the right of this line but must belong to the left pole family. Formula (7) is the continued contour with that pole restored explicitly, not an incorrectly separated straight Barnes contour. Stirling's estimate gives exponential decay $e^{-3\pi|\operatorname{Im}s|/2}$ times a power on every fixed vertical line away from poles. Thus the integral and its derivatives under $X\,d/dX$ converge absolutely and locally uniformly for $X>0$.

This is the continued integral definition of

    G^(2,2)_(2,3)(X | 1-a,1-b ; 0,d | -1),

in the convention of DLMF 16.17.1. Its identification can also be checked directly by contour shifts. Closing to the right for small $X$, the poles $s=j$ and $s=d+j$ give

    G(X)=A1 f1(X)+A2 f2(X),
    A1=Gamma(d)Gamma(a)Gamma(b),
    A2=Gamma(-d)Gamma(a+d)Gamma(b+d)/Gamma(2+d).            (8)

The extra term in (7) cancels the extraneous contribution of the pole $-a$ in this closure. Residue signs in (8) use the clockwise right closure. For example the residue of $\Gamma(-s)$ at zero is $-1$, so the resulting leading coefficient is positive $\Gamma(d)\Gamma(a)\Gamma(b)$ before the sign of its gamma factors is evaluated. The general residues give exactly the coefficient ratios in (4); both series converge for all $X$. This is the usual residue derivation of DLMF 16.17.2, with no coinciding right pole families because $d\notin\mathbb Z$.

The reflection identities show

    A1 E1 = Gamma(d)Gamma(1-d),
    A2 E2 = Gamma(-d)Gamma(1+d) = -Gamma(d)Gamma(1-d).      (9)

Both coefficients are nonzero. Thus (8) spans the only possible exponential cancellation line. Independently of cancellation of the asymptotic series, the absolutely convergent contour (7) controls the resulting function at large $X$.

Move the line in (7) left past the simple pole $s=-b$, to any $\eta'$ with $-a-1<\eta'<-b$. The other restored pole is $-a$. The residue at $-b$ is exactly $C_\mathrm{odd}$. The integral on the new line is $O(X^{\eta'})$; derivatives under $T$ obey the same bound because their extra polynomial factors in $s$ are absorbed by the exponential gamma decay. Therefore

    G(X)=C_even X^(-a)+C_odd X^(-b)+O(X^eta'),
    (X d/dX)^j remainder=O(X^eta')                       (10)

for every fixed nonnegative integer $j$. Repeated left shifts give higher terms if desired. In particular the two first powers and their differentiated error are rigorously separated without an asymptotic fit.

Now let $h_G(z)=z^pG(\lambda/z^2)$. Equation (10) yields

    h_G(z)=C_even lambda^(-a)
              +C_odd lambda^(-b) z + O(z^(p-2 eta')).    (11)

The error exponent is greater than one because $\eta'<-b$, and the first derivative of the error tends to zero. All factors of $C_\mathrm{odd}$ in (6) are positive except $\Gamma(a-b)=\Gamma(-1/2)<0$: indeed $b>0$, $d+b>0$, and $2-b>0$. Thus $C_\mathrm{odd}<0$ for every $0<p<1$. The derivative $h_G'(0+)=C_\mathrm{odd}\lambda^{-b}$ is nonzero. Any nonzero multiple of $h_G$ has an even extension with a derivative jump at zero. The only member of the allowed line with a $C^1$ even extension is zero, which proves the statement.

## Canonical inverse and matching scope

For an even smooth trial $h$ with $h''=O(z^{p-2})$ at infinity define

    I[h](z)=(1/mu)[z^p int_z^infinity t^(-p-1)h''(t)dt
                         +z^r int_0^z t^(-r-1)h''(t)dt]. (12)

The proof in result215 derives this from the complete positive-sign vertical integral, with both endpoints convergent. Since $r<0$, (12) is bounded at zero and has no $z^p$ term at infinity. For the negative signed operator the physical velocity coefficient is

    w=-C_p z^p-I[h](z).                                 (13)

It solves the second equation in (2). Any difference from (13) solves the homogeneous inverse equation and is a combination of $z^p$ and $z^r$; boundedness at zero removes $z^r$, and the specified cusp at infinity removes $z^p$. This excludes a hidden homogeneous velocity in the formal model. The theorem already excludes every nonzero $h$ before imposing (13), so this inverse check cannot create an exceptional admissible solution. The only smooth solution has $h=0$; its transport equation then gives $w=0$, and (13) forces $C_p=0$.

The statement applies for each fixed $p$ and $\lambda$, with no claimed uniform conditioning as $p$ approaches an endpoint. At $p=0$ or $p=1$ the root configuration or coefficients degenerate; both values are excluded. In particular the positive-sign exceptional value $p=\sqrt2-1$ does not make (6)'s negative-sign odd coefficient vanish. A one-sided bounded function with a cusp is not a smooth layer; changing the admissible regularity would be a different question. Neither the full nonlinear outer expansion, its next orders, core matching, nor an unconditional negative-slope bound follows from this calculation.

## Verification and provenance

The lead's diagnostic source `code/chk_neg1.py` was read statically as a claim source. It is not imported, executed, or copied into the verifier implementation. The verifier will use its own coefficient recurrence and explicit vertical contour integral, rather than the lead's Meijer-G evaluator and numerical differentiation. Exact algebra and sign calculations are checked separately. Primary NIST documents 5.11, 16.8 and 16.17 were retrieved read-only with Python and are frozen with hashes in `verification/sources/MANIFEST.json`. The lead lane's MODEL file identifies `us.anthropic.claude-opus-5-5`; the numerics lane reports Fable5.1. The ongoing exchange with the lead is the Opus collaboration, and these model identities are not conflated.
