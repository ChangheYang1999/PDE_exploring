# Exact irrotational profiles on an open spiral sector

## 1. Statement and scope

Fix 2/5<c<1/2 and any finite real omega. Put a=1-2c, p=(1-c)/c, sigma=omega/c, Jx=e3 cross x, A=cI-omega J and L=(1-c)I+omega J. There is a relatively open spherical disk O containing e1 whose compact closure avoids the vertical axis, such that on

    D_O={y!=0: q(y) in O},
    q(y)=exp(sigma log|y| J)y/|y|,

there are smooth real fields U,P satisfying the complete profile system

    div U=0, curl U=0, LU+DU(Ay+U)+grad P=0.

For constants v0,v1,v2,v3 positive and finite, depending on c,omega,O,

    v0|y|^(-p)<=|U(y)|<=v1|y|^(-p),
    |DU(y)|<=v2|y|^(-p-1), |P(y)|<=v3|y|^(-2p).

Set k=(Ay).U, E=|U|^2 and S=P-E/2. These fields have P=-E/2, S=-E, E/|S|=1, and grad k cross grad S nonzero everywhere on D_O. The domain is invariant under the complete linear flow F_t=exp(tA). Restricting to |y|>R gives an exact smooth solution on the unbounded fixed-aperture spiral sector of the form forced in LIT271. This is a domain-only result; D_O has angular boundaries and omits the origin.

## 2. A branch on the entire invariant domain

Choose O small enough that n1+i n2 has a smooth argument theta(n), with theta(e1)=0, on a neighborhood of its closure. For y in D_O put r=|y|, rho=sqrt(y1^2+y2^2), z=y1+i y2 and n=q(y). Define

    ell(y)=log rho+i(theta(n)-sigma log r).

The identity n1+i n2=exp(i sigma log r)z/r gives exp(ell)=z. This is an actual smooth single-valued logarithm on D_O, not an angle specified only modulo 2pi. Locally any two logarithms of z differ by a constant integer multiple of 2pi i. Thus ell has the local derivatives of the ordinary complex logarithm; in particular it is locally independent of y3. This local assertion does not require a single logarithm on the entire punctured horizontal plane.

The parametrization (r,n) to r exp(-sigma log r J)n is a smooth diffeomorphism (0,infinity) times O onto D_O. Along F_t the quotient n stays fixed, r and rho scale by exp(ct), and hence

    ell(F_t y)=ell(y)+(c-i omega)t

as an equality of complex numbers. Arbitrarily many rotations cause no ambiguity in this equality.

## 3. Harmonicity and the complete profile equation

Define

    lambda=-a/(c-i omega)=u+i v,
    u=-ac/(c^2+omega^2)<0, v=-a omega/(c^2+omega^2),
    f=Re(i exp(lambda ell)), U=-grad f/a, P=-|U|^2/2.

The function inside the real part is locally holomorphic in z and independent of y3. Thus f is harmonic in three dimensions, U is divergence free and irrotational, and all fields are smooth on D_O. The exact branch increment gives

    f(F_t y)=exp(-at)f(y), (Ay).grad f=-af.

Therefore (Ay).U=f: the contraction k is exactly this f. Differentiating the scalar transport equation with respect to y, keeping the transpose of A, gives

    D2f Ay=-(aI+A^T)grad f=-L grad f.

It follows that DU Ay=-LU. The symmetric matrix DU of an irrotational field satisfies DU U=grad(E/2), which cancels grad P. This proves every term of the full nonlinear profile equation. Diverging it, or differentiating P directly, also gives Delta P=-tr((DU)^2). The pressure here is explicit; no claim about a canonical pressure of a whole-space extension is needed or made.

## 4. Natural rates with a strict lower bound

The horizontal gradient of the real part of a holomorphic function has magnitude equal to the modulus of its complex derivative. Consequently

    E=(|lambda|^2/a^2)rho^(2(u-1))
                   exp(-2v(theta(q(y))-sigma log r))>0.

Differentiating the exact scalar flow identity yields

    U(F_t y)=exp(-(1-c)t)exp(-omega tJ)U(y),
    DU(F_t y)=exp(-t)exp(-omega tJ)DU(y)exp(omega tJ).

The second equality follows by multiplying the differentiated first equality by F_t inverse on the right; both rotations and the full scalar exponent are necessary. Since U,DU extend smoothly to a neighborhood of the compact closure of O, |U| has a positive minimum and finite maximum there and |DU| is bounded there. Taking t=(log r)/c proves the desired rates, with p+1=1/c. The pressure bound follows from P=-E/2. These constants need not remain uniform when omega varies.

## 5. Rank throughout the domain

At e1 one has ell=0, k=f=0 and

    grad k=(-v,-u,0), E0=|lambda|^2/a^2>0,
    grad E=(2(u-1)E0,-2vE0,0).

Indeed the complex derivative of i z^lambda at z=1 is i lambda, giving the first gradient, and the logarithmic derivatives of E are 2(u-1) and -2v in the first two coordinate directions. Since S=-E,

    (grad k cross grad S)(e1)
        =-2E0(v^2+u(u-1))e3
        =-2E0(|lambda|^2-u)e3.

This is nonzero for every omega because u<0. By continuity shrink O so that the cross product is nonzero on a neighborhood of its closure. The scalar flow degrees -a and -b, where b=2-2c, imply gradient degrees -(a+c) and -(b+c). The cross product therefore obeys

    (grad k cross grad S)(F_t y)
      =exp(-(3-2c)t)exp(-omega tJ)(grad k cross grad S)(y).

It is nonzero on all of D_O. There is no conflict with actual vortical rank: W=curl U is identically zero on this domain and there are no supported vortical points in it.

## 6. What the example establishes

The full profile equation, natural velocity and gradient decay, nonzero lower bound, zero helicity, pressure limit zero, comparison E/|S|=1 and open irrotational rank defect are compatible on this sector. Thus no argument restricted to these equations and bounds on the sector alone can exclude the LIT271 configuration. This is an exact analytic solution, not a numerical approximation or merely a solution of the leading linear equation.

Its formula is singular as r tends to zero inside D_O because p>0 and the lower bound is positive. No angular matching to a vortical exterior or canonical whole-space pressure is supplied. A smooth whole-space irrotational and divergence-free extension which decays would have bounded harmonic components and hence vanish by harmonic Liouville, contradicting the nonzero sector. An extension with vorticity outside the sector is neither constructed nor excluded. The LIT272 contact theorem concerns precisely such a global matching problem and is not contradicted.

All six submitted sections and all local branch and derivative calculations have been checked. No numerical computation or formal build was performed. The source copy and checksum are retained in verification. The mathematical construction needs no further literature input. Existing configured model collaborators remain available through working files only; actual runtime identity is not independently attested.
