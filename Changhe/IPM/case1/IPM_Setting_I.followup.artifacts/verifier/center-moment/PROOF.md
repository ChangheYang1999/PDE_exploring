# Exact full-plane center strain of the nodal representation

Date: 2026-10-20. Status: proof of a finite formula; candidate certificate computations are separate.

## Statement

Let L>0, 0<k<1 and |beta|<1. Let b be the finite tensor polynomial

    b(q,s)=sum_(n=0)^N sum_(m=0)^(M-1) a_nm T_n(2q-1) cos(2ms).

In each quadrant define theta=s+(beta/2)sin(2s), 0<=s<=pi/2, and extend by the required reflections. Put

    q=1-(1+r^2/L^2)^(-(1-k)/2),
    rho=r^3 cos(theta)^2 sin(theta) (1+r^2/L^2)^((k-3)/2) b(q,s).

Assume b(0,s)=1. For the canonical full-plane velocity, the center strain c=psi_xy(0) exists and equals

    c=L^2/(1-k) sum_(n even,m) [a_nm/(1-n^2)] Omega_m,                 (1)
    Omega_m=[I_(m,0)+I_(m,1)-I_(m,2)-I_(m,3)]/4,
    I_(m,0)=delta_(m,0)+(beta/2)delta_(m,1),
    I_(0,l)=0 for l>=1,
    I_(m,l)=m[J_(m-l)(l beta)-J_(-m-l)(l beta)]/(2l)
                for m>=1,l>=1.                                  (2)

Here J_j(z) is the ordinary integer-order Bessel function and Omega_m is the angular weight; in the implementation these are named bessel and angular_weight. Formula(1) integrates the entire plane, including both zero and infinity, with no radial cutoff or quadrature error. Interval evaluation still requires exact input pins, outward rounding, and a rigorous series remainder. It certifies the represented field, not the existence of a nearby solution.

## Canonical integral and separation

For the stated parity and vanishing linear center jet, the canonical inverse gives

    c=int_0^infinity rho_3(r)/r^2 dr,
    rho_3(r)=(1/pi)int_0^(2pi) rho(r,theta)sin(3theta)dtheta.

This identity follows by differentiating the canonical logarithmic inverse, as derived in ../inverse/PROOF.md. The local correction proportional to rho_y(0) vanishes here. The center density is O(r^3), while infinity has growth O(r^k), so the displayed strain integral is absolutely convergent. There are finitely many tensor terms, hence separation of their radial and angular integrals is valid. Define

    angular_weight_m=(4/pi)int_0^(pi/2)
               cos(theta)^2 sin(theta)sin(3theta)cos(2ms(theta)) dtheta.

The radial integral of the n-th tensor term is

    int_0^infinity r(1+r^2/L^2)^((k-3)/2)T_n(2q-1)dr
      =L^2/(1-k)int_0^1 T_n(1-2v)dv,

by v=(1+r^2/L^2)^(-(1-k)/2). The remaining integral is zero for odd n and 1/(1-n^2) for even n. To see this, substitute z=cos t into one half of the integral over[-1,1], use T_n(cos t)=cos(nt), and integrate sin(t)cos(nt) by its two-angle formula; for n=1 the integral is zero directly. This proves the radial coefficients in(1).

## Angular weights

The identity

    cos(theta)^2 sin(theta)sin(3theta)
      =[1+cos(2theta)-cos(4theta)-cos(6theta)]/8

and t=2s give angular_weight_m=(I_(m,0)+I_(m,1)-I_(m,2)-I_(m,3))/4, where

    I_(m,l)=(1/pi)int_0^pi cos(l(t+beta sin t))cos(mt)(1+beta cos t)dt.

The l=0 case follows by cosine orthogonality. For l>=1, integrate the derivative of sin(l(t+beta sin t)) against cos(mt). The boundary terms vanish because l and m are integers. This gives

    I_(m,l)=m/(pi l)int_0^pi sin(l(t+beta sin t))sin(mt)dt.

It is zero if m=0. For m>0 the absolutely convergent Fourier expansion

    exp(i l beta sin t)=sum_(j in Z) J_j(l beta)exp(i j t)

and sine orthogonality give(2). The Fourier expansion follows by multiplying the two absolutely convergent exponential power series in the generating function exp((z/2)(u-u^(-1))) on |u|=1. Collecting the coefficient of u^j gives, for j>=0,

    J_j(z)=sum_(a=0)^infinity (-1)^a (z/2)^(j+2a)/[a!(j+a)!],
    J_(-j)(z)=(-1)^j J_j(z).

The absolute double-series convergence on the unit circle justifies collecting coefficients and termwise integration. Thus no numerical angular integration is required for(1).

## Rigorous truncation and exact inputs

For n>=0 and |z|<3, let T_a=|z/2|^(n+2a)/[a!(n+a)!]. After summing a=0,...,K-1, the remainder has absolute value at most

    T_K/[1-9/(4(K+1)(n+K+1))],                              (3)

provided the denominator is positive. Indeed every successive absolute-term ratio after T_K is at most 9/[4(K+1)(n+K+1)]. The implementation evaluates the signed finite series using ball arithmetic, encloses T_K, and adds the symmetric error ball from(3). Negative orders use the exact integer parity identity. Values of K such as64and96 are independent truncation checks; overlap alone is not the proof of the enclosure.

The coefficient matrix of the ideal Chebyshev-Lobatto by angular-midpoint interpolant is computed by the finite cosine transforms described in ../inner-cutoff/PROOF.md. Every stored floating nodal value and parameter is first exported as an exact binary64 hexadecimal value in JSON and pinned to the source bytes. The shared exact-data input interface checks source hashes, shape, finite values and exact round-trip equality. Cosines and arithmetic in the coefficient transform are enclosed with Arb. The JSON inputs and every imported source are listed with hashes in the dependency manifest. Importing the table is not a proof: the displayed integral identity, transform orthogonality, ball operations and the explicit remainder(3) are the soundness argument.

The final self-consistency interval is 3c_l-1-c, using the exact binary c_l stored in the input and k=1/c_l exactly. A nonzero interval excludes an exact identity for that fixed represented field. A tiny interval does not certify a profile or the rest of the inverse. Additive harmonic strain is not available because the inverse in this statement is the canonical full-plane inverse. These certificates use Python/Arb; no Lean or FloatLib execution is performed under this run's no-build rule.

## Manufactured checks and limitations

At beta=0 the weights are1/4for m=0,1/8for m=1,-1/8for m=2and3, and0otherwise. For b=1, formula(1) reduces to c=L^2/[4(1-k)], which follows by direct radial integration. Finite polynomial transforms and these angular identities are checked before candidate results are reported. A separate floating quadrature comparison checks signs and conventions on nonzero beta; it is diagnostic, not part of the certificate.

This theorem does not certify sampled velocities away from0, elliptic residuals, source endpoints, B_j, smoothness, or a PDE solution. It addresses only the canonical center strain for the exact finite interpolant and its self-consistency identity.
