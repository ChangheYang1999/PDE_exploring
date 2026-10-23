# Higher stream endpoint conditions and logarithmic derivative defects

Independent verifier supplement to result107, written 2026-10-21 before the exact checker. This concerns a separate stream interpolant, not the exact canonical inverse of the saved smooth density.

## Statement

Let s be the compact variable r=L sqrt(s)[2(1-s)]^(-kappa), L>0, kappa>1, and let a stream interpolant have an even angular mode

    psi_n=r^2(1-s)P_n(2s-1) sin(n theta), n=2m,

where P_n is analytic at -1. Cartesian smoothness requires

    P_n^(j)(-1)=0 for 0<=j<=m-2.                         (1)

These conditions are also sufficient for this mode to be smooth at zero. They are conditions on each derivative, not merely the first derivative. In particular P_8''(-1) is not harmless: after P_8(-1)=P_8'(-1)=0, a nonzero second derivative gives a nonpolynomial r^6 sin(8theta) stream term.

For a density with rho=ay+O(r^3), a!=0, suppose the interpolated stream differs from a smooth canonical stream by

    delta psi=tau r^6 sin(8theta)+O_symbol(r^8), tau!=0,

where the remainder is smooth on punctured neighborhoods and obeys the differentiated radial bounds through sufficiently many orders. Then

    delta R=a tau r^5[7sin(7theta)-sin(9theta)]+O_symbol(r^7).

Consequently this residual difference is not C^5 at zero, and

    int_(epsilon<r<r0) |D^6(delta R)|^2 dxdy
       =208089907200 pi a^2 tau^2 log(r0/epsilon)+O(1).     (2)

Here the norm is the full ordered Cartesian derivative tensor. Adding any smooth residual does not change the leading logarithmic divergence. It follows that checking only first stream endpoint derivatives does not establish finiteness of the sixth residual derivative norm, even if those first derivatives vanish exactly.

The general logarithmic formula is as follows. For a finite sine sum

    F=r^q sum_n s_n sin(n theta), q>=0 integer,

smooth away from zero, set k=q+1 and

    J_(q,n)=product_(h=0)^q (n+q-2h).

Then on an annulus

    int |D^(q+1)F|^2 dxdy
        =pi sum_n J_(q,n)^2 s_n^2 log(r0/epsilon).         (3)

Distinct frequencies do not cross in this integrated tensor norm. In the odd parity relevant here q,n are odd. Then J_(q,n) vanishes exactly at the nonnegative frequencies n<=q that represent degree-q Cartesian homogeneous polynomials. Every nonzero higher angular frequency contributes a strictly positive logarithmic coefficient.

## Proof

The implicit compact map has s=(2^(2kappa)/L^2)r^2+O(r^4), analytic in r^2 near zero, with nonzero first derivative. The factor 1-s is nonzero at zero. If P_n has first nonzero Taylor order j, the stream mode has first nonzero radial degree 2j+2. A homogeneous angular mode r^d sin(n theta) extends smoothly to the origin only when n<=d and d-n is a nonnegative even integer; then it is Im(x+iy)^n times (x^2+y^2)^((d-n)/2). Necessity follows by comparing its degree-d Taylor polynomial along rays. No homogeneous Taylor polynomial of degree d has angular frequency above d. For n=2m, the first permitted j is m-1. This proves both directions of (1), since all later analytic radial powers are also allowed.

With P_8=P_8'=0, Taylor expansion gives P_8(2s-1)=2P_8''(-1)s^2+O(s^3), so

    tau=2^(4kappa+1) P_8''(-1)/L^4.                       (4)

The identity

    partial_x[r^d sin(n theta)]
      =r^(d-1)[(d+n)sin((n-1)theta)
                         +(d-n)sin((n+1)theta)]/2

follows by polar differentiation. Since U_2=psi_x, the leading residual change is a partial_x(delta psi); the higher density gradient terms are O(r^2), and the higher stream terms contribute only O_symbol(r^7). Putting d=6,n=8 gives the stated residual difference. Its degree5 angular frequencies7,9 preclude a C5 Taylor polynomial by the same ray argument.

For (3), use the positive polar derivative identity in result102 with F=r d_n(log r)sin(n theta) and d_n=s_n r^(q-1). At derivative order k=q+1 its differential polynomial becomes

    P_(k,j,n)(q-1)=
        product_(i=0)^(j-1)(q-n-2i)
         product_(h=0)^(k-j-1)(q+n-2h).

The first product can be rewritten as (-1)^j times the last j factors of product_(h=0)^q(q+n-2h), in reverse order. Thus P_(k,j,n)(q-1)=(-1)^j J_(q,n). The sum of the binomial coefficients is 2^k, canceling the prefactor in the tensor identity. The radial power is exactly dr/r. This proves (3). It also proves positivity without an integration by parts or an assumption that F itself is square integrable.

For q=5,

    J_(5,n)=(n^2-25)(n^2-9)(n^2-1),
    J_(5,7)=46080, J_(5,9)=322560.

The coefficient is pi a^2 tau^2[49*46080^2+322560^2], which is (2). The sixth derivative of the O_symbol(r^7) remainder is O(r); its cross term with the leading O(r^-1) derivative is bounded in area, and its own square is integrable. A smooth added residual has bounded sixth derivatives, whose cross term is also integrable. This proves the O(1) remainder and the persistence of the divergence.

For an explicit manufactured example, take rho=ay exp(-r^2) with its exact canonical stream, and add tau chi(r)r^6 sin(8theta) to that stream, where chi is smooth, radial and one near zero. The density is unchanged and smooth; the added stream is C5 but not C6, violates the canonical Poisson equation, and creates exactly the above logarithmic defect. The example is not a profile. It isolates the interpolation issue without saying that the corresponding exact canonical residual is singular.

## Scope for the producer data

The producer's rounded endpoint summary gives only numerical values, not independently verified coefficients. The statement in NUM_REPORT(c18) that both mode6 and mode8 second endpoint derivatives are harmless is refuted by (1). A mode6 second derivative first gives r^6 sin6theta, which is permitted. A mode8 second derivative first gives r^6 sin8theta, which is not permitted. For still higher modes more endpoint derivatives must vanish. Tiny numerical values may support approximate cancellation at a measured order; they cannot establish exact Cartesian smoothness or all higher cancellations. Actual interpolant coefficients, source hashes and endpoint cleaning remain necessary for the numerical audit.

Dependencies: result107's stream convention, result102's full ordered polar tensor identity, analytic inversion of the compact map, and finite homogeneous Taylor/Fourier calculus.
