# A second rigorous full-plane center moment by periodic quadrature

Date: 2026-10-20. Status: complete informal proof and numerical protocol, independent review pending. This proof precedes the implementation and execution.

## Statement and exact data

Use the density representation and canonical velocity convention of ../center-moment/PROOF.md, with L>0, 0<k<1, |beta|<1 and b(0,s)=1. The density is

    rho=x^2 y (1+r^2/L^2)^((k-3)/2) b(q,s),
    q=1-(1+r^2/L^2)^(-(1-k)/2),
    theta=s+(beta/2)sin(2s).

The finite polynomial b has degree at most N in 2q-1 and at most M-1 in cos(2s). Its supplied table is at q_j=(1-cos(pi j/N))/2, j=0,...,N, and phi_a=2s_a=pi(2a+1)/(2M), a=0,...,M-1. All table entries and parameters are exact binary values imported through the shared exact JSON interface. No stored approximation to a node is substituted for its ideal trigonometric definition.

Let alpha_j=1/2 at j=0,N and alpha_j=1 otherwise. Define

    lambda_j=(2 alpha_j/N)
              * sum_(0<=n<=N, n even)
                   alpha_n cos(pi n j/N)/(1-n^2),
    d_a=sum_(j=0)^N lambda_j b_(N-j,a),
    c_m=(gamma_m/M)sum_(a=0)^(M-1)d_a cos(m phi_a),
    gamma_0=1,  gamma_m=2 for m>0,
    C(phi)=sum_(m=0)^(M-1)c_m cos(m phi).

Then C(phi)=integral_0^1 b(q,phi/2)dq exactly. Put

    T(phi)=phi+beta sin(phi),
    f(phi)=C(phi)(1+beta cos(phi))
            *[1+cos(T(phi))-cos(2T(phi))-cos(3T(phi))]/4.

For any positive integer J and a>0, write

    S_J=(1/J)sum_(j=0)^(J-1) f(2pi j/J),
    D(a)=sum_m |c_m| exp(m a),
    t(a)=a+|beta|sinh(a),
    M(a)=D(a)(1+|beta|cosh(a))
                 *[1+exp(t(a))+exp(2t(a))+exp(3t(a))]/4.

The exact canonical center strain satisfies

    |c - L^2 S_J/(1-k)|
       <= L^2/(1-k) * 2 M(a)/(exp(Ja)-1).               (1)

This bounds all angular discretization error. The radial integration is exact, including both zero and infinity. Evaluating the finite expressions with outward-rounded intervals then gives a certificate independent of the Bessel series used in the first center-moment implementation.

## Radial interpolation and integration

For z_j=cos(pi j/N), the cardinal polynomial at the Chebyshev-Lobatto node z_j is

    ell_j(z)=(2 alpha_j/N)sum_(n=0)^N alpha_n cos(pi n j/N)T_n(z).

To verify the cardinal formula, evaluate at another node and apply finite cosine orthogonality, which follows by summing geometric series in exp(i pi j/N). Thus a polynomial of degree at most N is the sum of its nodal values times these cardinal polynomials. The supplied q nodes run in the reverse order from z=2q-1, explaining b_(N-j,a).

The elementary integral of T_n(2q-1) over 0<=q<=1 is zero for odd n and 1/(1-n^2) for even n. This follows on substituting 2q-1=cos t and using sin t cos(nt). Integrating the cardinal formula gives lambda_j and hence d_a. Finite cosine orthogonality on the angular midpoint nodes gives c_m and reconstructs C. No two-dimensional coefficient transform is required by this algorithm.

## Reduction of the canonical strain to one periodic mean

The canonical integral identity is

    c=integral_0^infinity rho_3(r)/r^2 dr,
    rho_3(r)=(1/pi)integral_0^(2pi)rho(r,theta)sin(3theta)dtheta.

It follows from differentiating the paired logarithmic inverse; its sign and vanishing local linear-jet correction are established in ../inverse/PROOF.md and ../center-moment/PROOF.md. Here rho=O(r^3) at zero and O(r^k) at infinity, so this moment is absolutely convergent.

Let v=1-q. Direct differentiation gives

    r(1+r^2/L^2)^((k-3)/2)dr=-L^2 dv/(1-k).

The radial integral is therefore exactly L^2 C(2s)/(1-k). Use quadrant parity and

    cos^2(theta) sin(theta) sin(3theta)
      =[1+cos(2theta)-cos(4theta)-cos(6theta)]/8.

On changing variable phi=2s, we have 2theta=T(phi) and dtheta=(1+beta cos(phi))dphi/2. It follows that

    c=L^2/(1-k) * (1/pi)integral_0^pi f(phi)dphi.

The function f is even and 2pi-periodic, so this is L^2/(1-k) times its full periodic mean. It is entire as a function of complex phi. All changes of variables are legitimate since 1+beta cos(phi)>0 on the real line.

## Error bound for the periodic mean

For complex phi with |Im phi|<=a, elementary exponential formulas give

    |cos(m phi)|<=exp(m a),
    |Im(phi+beta sin(phi))|<=a+|beta|sinh(a),
    |1+beta cos(phi)|<=1+|beta|cosh(a).

These imply |f(phi)|<=M(a) on the closed strip. Let f_n denote its Fourier coefficients. Shift the integration contour to Im phi=-a for n>0 and +a for n<0. The vertical sides cancel by periodicity, and analyticity justifies the shift. Hence |f_n|<=M(a)exp(-a|n|). This exponential bound makes the Fourier series absolutely convergent on the real line.

Averaging the Fourier series at the J equispaced nodes retains exactly the coefficients whose indices are multiples of J. Thus

    |S_J-f_0| <= sum_(ell != 0)|f_(ell J)|
               <=2M(a)/(exp(Ja)-1).

Multiplying by L^2/(1-k) proves (1). This derivation makes no use of Bessel functions, a difference of two quadrature values, or an empirical spectral tail.

## Implementation and verification scope

Use Arb interval trigonometry for the cardinal weights, angular coefficients, quadrature and strip bound, with a=1/4 and J=512 at 256-bit precision. Absolute coefficient upper bounds in M(a) are taken outward. Every finite exact value is enclosed in the computed interval; add the symmetric error interval from (1) before forming 3c_l-1-c. The input table is read through the shared exact JSON interface and pinned to its source bytes. The output manifest records all code, proof and input hashes.

Manufactured checks include constant b, a radial T_2 perturbation that preserves b(0,s)=1 after its constant correction, and an angular perturbation multiplied by q so that the first radial row stays one. At beta=0 the angular means are known by cosine orthogonality. The candidate computations compare their certified enclosures with the first method's saved Bessel certificates. Overlap is a consistency check; each enclosure is justified separately by its own error proof.

This certifies only the exact represented field's canonical center moment. It does not bound off-center velocity, interior principal-value quadrature, transport residuals, a smooth center obstruction, or distance to a genuine profile. No harmonic strain is added. It uses Python/Arb and does not run Lean, Lake, JavaScript, a server, or a cluster computation.
