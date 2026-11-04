# Extended angular-frequency integrals at a flat negative-pressure zero

## 1. Statement and exact assumptions

Let v be C1 on B_R0 in R3, P continuous, div v=0 and div div(v tensor v+P I)=0 distributionally. Assume v has infinite value vanishing order at zero. With normalized sphere averages, set

    f(r,theta)=v(r theta).theta, w=v(r theta)-f theta,
    N=<f^2>, T=<|w|^2>, K=N+T,
    Aang=<|grad_S f|^2>, M=<P(0)-P(r theta)>.

Assume M>=beta K for a fixed beta>0 on 0<r<R0. Let ell>=1 be measurable, and suppose Aang<=ell(ell+1)N almost everywhere. If for some R1<R0 and finite C>=0,C0,

    integral_r^R1 (ell(t)-1)dt/t <= C log(R1/r)+C0          (1)

for all sufficiently small r, then v=0 on B_R1. Conversely, at a nonzero germ every R with M(R)>0 satisfies

    lim_(r->0) integral_r^R (ell(t)-1)dt/t / log(R/r)
       =infinity.                                       (2)

All integrals of ell-1 are nonnegative extended Lebesgue integrals. No separate local integrability premise is made. These are conditional statements about angular Rayleigh control. They permit infinitely many angular modes and make no assertion that the original Euler profile equation supplies (1).

## 2. Continuous pressure gives a flat mean

Set a=(v.grad)v. The distributional stress equation and incompressibility give Delta(P(0)-P)=div a. Radial testing gives -r^2 M'+r^2<a.theta> constant on (0,R0). Boundedness of a and continuity of P eliminate its possible 1/r singular primitive. Therefore

    M'(r)=<a(r theta).theta>, M(0)=0.                    (3)

This proves C1 regularity of M away from zero without differentiating P. On a smaller closed ball Dv is bounded. Infinite value flatness of v then gives infinite value flatness of a, and integration of (3) gives M(r)=O(r^j) for every j. No flatness of derivatives of v is needed.

## 3. The angular identity

Incompressibility reads r partial_r f+2f+div_S w=0. Multiply by f and average to obtain

    r N'=-4N+2<grad_S f.w>.                              (4)

For the acceleration, differentiate the radial unit vector to get

    a.theta=div(v f)-|w|^2/r.

The spherical mean of the divergence term is N'+2N/r because its tangential divergence integrates to zero. Hence <a.theta>=N'+(2N-T)/r. Combining (3) and (4) proves

    r M'=-2N-T+2<grad_S f.w>.                            (5)

All formulas hold for every r>0 at C1 regularity. They use neither Taylor expansion nor homogeneity nor truncation.

## 4. The exact quadratic constant

Cauchy-Schwarz bounds the last term by 2sqrt(ell(ell+1))sqrt(NT). For nonnegative N,T,

    (ell-1)(N+T)+2N+T-2sqrt(ell(ell+1))sqrt(NT)
       =[sqrt(ell+1)sqrt(N)-sqrt(ell)sqrt(T)]^2>=0.

Thus, almost everywhere,

    r M'<=(ell-1)K<=((ell-1)/beta)M.                    (6)

The second inequality uses ell>=1. At a radius with N=0, continuity makes f and grad_S f zero on the sphere, so (5) gives rM'=-T; nothing is divided by N.

For integer ell>=2, a harmonic homogeneous Q of degree ell gives stationary v=grad Q, P=-|v|^2/2. Here f has pure harmonic degree ell and T=(ell+1)N/ell, so equality holds in the first inequality of (6). This verifies the sharp coefficient within an exact stationary class. These models have finite-order zeros, grow at infinity, and do not meet the flatness premise.

## 5. The direction of the integrating-factor estimate

For 0<r<R<R0 with a finite integral of (ell-1)/t on [r,R], integrate (6) with its nonnegative coefficient. Multiplication by the negative exponential primitive gives

    M(R)<=M(r) exp[beta^(-1)integral_r^R (ell(t)-1)dt/t]. (7)

This holds even when M has zeros. It is used only on intervals where the coefficient has a finite integral. Under (1), every sufficiently small lower endpoint gives a finite integral up to R1, and hence up to any fixed R<R1.

For each R<R1, (1) and ell-1>=0 bound the right side by C_R M(r)r^(-C/beta) for sufficiently small r. Flatness makes this tend to zero. Hence M(R)=0, so K(R)=0 by the mean comparison. Continuity of v makes it zero on that sphere; varying R proves v=0 on B_R1.

For the converse choose R with M(R)>0. If some integral from r0 to R is infinite, every integral with lower endpoint r<=r0 is infinite, so (2) follows immediately. Otherwise all these integrals are finite. Formula (7) then forces M(r)>0 for all 0<r<R, and gives

    integral_r^R (ell(t)-1)dt/t >= beta log[M(R)/M(r)].

For every j, M(r)<=C_j r^j near zero. Division by log(R/r) and passage to the lower limit give a bound at least beta j for every j, proving (2). A nonzero germ supplies such R arbitrarily near zero: a nonzero value of continuous v makes K positive on its sphere, and hence M>0. No monotonicity of M itself was presumed.

## 6. A canonical measurable frequency and scope

For each radius define

    ell_min=max(1,(sqrt(1+4Aang/N)-1)/2) when N>0,
    ell_min=1 when N=0.

The functions N and Aang are continuous in r>0 because v is C1. Hence ell_min is finite valued and measurable. When N>0 its definition directly gives Aang<=ell_min(ell_min+1)N. When N=0, the continuous function f is identically zero on the sphere; its angular derivative is also zero, so Aang=0 and the inequality again holds. No continuity or local integrability of the ratio at its zero denominator is asserted.

Applying Section 5 to ell_min proves its divergent extended logarithmic mean at a nonzero flat germ with the stated pressure-deficit comparison. This establishes existence of a canonical frequency; it does not bound its logarithmic mean. All finite omega are compatible because no rotational parameter enters the local theorem. The actual Euler-tail estimate and the full target conjecture remain open.

The six-section earlier independent proof A1764-A1767 supplies the unchanged derivation, reproduced above. The complete new source diff and its current statements were checked. No numerical computation, model inference or formal build was run. Source hash and postread record are in verification; formal_sources records the absence of a formal build.
