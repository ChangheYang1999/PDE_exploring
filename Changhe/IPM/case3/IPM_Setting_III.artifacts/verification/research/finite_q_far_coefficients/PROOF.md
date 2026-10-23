# The second far coefficient of a finite smooth Q representation

Date: 2026-10-20. Status: independently derived exact asymptotic diagnostic. An expansion of a finite interpolant is not a profile existence proof.

## 1. Statement and notation

Let kappa>1, eta=1/kappa, p=1-eta, L>0, and finitely many real polynomials B_k, 0<=k<M. Define t in[-1,1), sigma=(1+t)/2, z=1-t, and

    r=L sqrt(sigma)/z^kappa,
    rho(r,theta)=r z/2 sin(theta) sum_k sigma^k B_k(t)cos(2k theta).

The Cartesian extension is smooth at the origin: sigma is a smooth function of r² there and sigma^k cos(2k theta) has a polynomial Cartesian numerator of degree2k times a smooth radial factor. Take the unique full-plane canonical velocity U=(-psi_y,psi_x), -Delta psi=rho_x, U=o(r), with the required parities. Fix ell>1 and suppose ell*p=1 exactly. Put D=ell-1 and define

    F0(theta)=sum_k B_k(1)cos(2k theta),
    F1(theta)=sum_k [B_k'(1)+k B_k(1)/2]cos(2k theta),
    Theta0=L^eta sin(theta)F0/2,
    Theta1=L^(2eta) sin(theta)[-eta F0/4-F1]/2.             (1)

Then, with all fixed-order derivatives in the corresponding symbol estimates,

    rho=r^p Theta0+r^(2p-1)Theta1+O(r^(3p-2)).              (2)

If Theta0=sum_(n positive odd) q_n sin(n theta), set for positive even m

    f_m=[(p-(m-1))q_(m-1)+(p+(m+1))q_(m+1)]/2,
    Phi=sum_(m positive even) f_m sin(m theta)/[m²-(p+1)²],
    u0r=-Phi', u0theta=(p+1)Phi.                           (3)

An absent q coefficient means zero. The unforced transport residual has the expansion

    R=r^(2p-1) C2(theta)+O(r^(3p-2)),
    C2=-D Theta1+p u0r Theta0+u0theta Theta0'.             (4)

Thus C2 identically zero is a necessary second far-field condition for this finite interpolant to be an exact profile. A small sampled normalized residual at moderate radii does not replace this condition. A nonzero C2 is decisive nonexactness for this interpolant, not for its potential infinite-resolution limit or for the primary class.

## 2. Expanding the map without an endpoint loss

Let h=(L/r)^eta. The defining map gives

    h=z(1-z/2)^(-eta/2)=z+eta z²/4+O(z³),
    z=h-eta h²/4+O(h³).

Taylor expansion of (1-z/2)^k B_k(1-z) gives B_k(1)-z[B_k'(1)+k B_k(1)/2]+O(z²). Insert these expansions into rho. Since r h=L^eta r^p and r h²=L^(2eta)r^(2p-1), equations(1)-(2) follow. Analytic expansion near z=0 gives symbol remainders after any fixed number of radial and angular derivatives. Coefficients can be large; the radius at which the remainder is small is a separate quantitative issue.

For Chebyshev coefficients B_k(t)=sum_j c_(kj) T_j(t),

    B_k(1)=sum_j c_(kj), B_k'(1)=sum_j j² c_(kj).

These finite sums are evaluated directly at higher precision when cancellation makes double precision unreliable. High precision does not repair uncertainty in the originally published coefficients; it defines and evaluates their binary-data interpolant accurately.

## 3. Canonical inversion of the leading term

Differentiation in polar coordinates gives

    partial_x(r^p Theta)=r^(p-1)[p cos(theta)Theta-sin(theta)Theta'].

For Theta=sin(n theta), the bracket is [(p-n)sin((n+1)theta)+(p+n)sin((n-1)theta)]/2. This gives f_m in(3). Since 0<p<1, the denominator m²-(p+1)² is nonzero for each positive even m. The homogeneous stream r^(p+1)Phi solves the Poisson equation for the leading homogeneous density, and its velocity is r^p(u0r,u0theta).

To compare with the actual smooth density, insert a smooth radial cutoff outside a fixed disk in this homogeneous expression. The remainder has symbol degree2p-1, which lies in(-1,1). The canonical inverse on the prescribed parity class preserves this degree: its smooth-kernel contribution from a fixed disk decays at least as r^-3, and splitting the cancellation-subtracted kernel into radii below, comparable to and above r bounds the rest by Cr^(2p-1). The far integral converges because 2p-1<1. The inner integral converges with this bound because 2p-1>-3 and the first nonzero density/velocity multipole in these parities gives the threshold -3. Applying the differentiated kernel after local Taylor subtraction gives the derivative bounds. A full independent proof of this weighted inverse estimate is in ../far_field_second_term/PROOF.md; the present application uses only degree2p-1 in(-1,1).

Consequently U=r^p u0+O(r^(2p-1)), with derivative symbol bounds. No harmonic linear strain or fitted far velocity is added.

## 4. Residual, ratios and scope

Since ell*p=1, the dilation part annihilates the leading density. On the next term its factor is ell(2p-1)-1=-D. The leading nonlinear term is r^(2p-1)[p u0r Theta0+u0theta Theta0'], which proves(4). The remaining products have degree at most3p-2; differentiating the error in(2) and multiplying by the dilation or velocity yields the same bound.

On the positive vertical axis suppose K=Theta0(pi/2)!=0. The horizontal terms vanish by symmetry. Then, as r tends toinfinity,

    N_f~2|K|r^p, N_v~(1+p)|K|r^p.

If C2(pi/2)!=0, the respective residual ratios are asymptotic to |C2|/(2|K|)r^-eta and |C2|/((1+p)|K|)r^-eta. For ell close to1 this decay can be extremely slow. When p>1/2 the absolute residual instead grows like r^(2p-1). Thus a ratio tending tozero at infinity does not prove the transport equation.

For arbitrary ell*p, put delta=ell*p-1. The exact two-term residual expansion is

    R=delta r^p Theta0+r^(2p-1)[C2+2delta Theta1]+O(r^(3p-2)),

where C2 in(4) uses D=ell-1. A nonzero delta gives the previously proved nonzero leading normalized floor. Rounded binary ell and kappa may have a tiny nonzero delta even when double multiplication prints zero. The data audit reports it and the corrected second coefficient explicitly. In the present finite radius range it can be quantitatively negligible without being set tozero as an identity.

The necessary condition C2=0 does not require a positive Theta0. It can be checked at a single angle to refute exactness of an explicit finite interpolant. Passing it is only a necessary condition and supplies no existence, uniqueness, regularity-convergence or full-class nonexistence theorem.
