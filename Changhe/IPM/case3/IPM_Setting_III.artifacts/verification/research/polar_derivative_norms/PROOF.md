# Positive polar formulas for derivative residual norms

Independent derivation, 2026-10-21. This is an evaluation identity, not an existence or regularity theorem. It is written before its implementation.

## Statement and scope

Let f be a real C^k function on a closed annulus 0<a<=r<=b<infinity, with a finite sine expansion f(r,theta)=r sum_{n>=1} d_n(log r) sin(n theta), where the coefficients are C^k. Put E=d/dt, t=log r. Define the squared full ordered Cartesian derivative norm by

    |D^k f|^2 = sum_{j=0}^k binom(k,j) |partial_x^j partial_y^(k-j) f|^2.

For 0<=j<=k and integer n, let

    P_(k,j,n)(z) = product_{i=0}^{j-1}(z+1-n-2i)
                  product_{h=0}^{k-j-1}(z+1+n-2h).

Empty products equal 1. Then the exact identity on every annulus is

    integral_{a<r<b} |D^k f|^2 dxdy
      = (pi/2^k) integral_{log a}^{log b} exp((4-2k)t)
          sum_{n>=1} sum_{j=0}^k binom(k,j)
              [P_(k,j,n)(E) d_n(t)]^2 dt.                    (1)

There are no integrations by parts, omitted boundary terms, signed cancellation among angular integrals, or assumptions of square integrability of f. If f is smooth on the whole plane and D^k f is square integrable, monotone convergence as a decreases to zero and b increases to infinity gives the full-plane identity. The same formula holds for an infinite sine expansion provided its Cartesian derivatives converge in L2 on each annulus; this extension is not needed for finite numerical input.

For a smooth finite-angular density rho, its independently computed canonical stream, and a fixed ell, apply (1) to rho and to R=(ell X+U).grad rho-rho. The ratio eta_k=||D^k R||_2/||D^k rho||_2 is defined when the denominator is positive and finite and the numerator is finite. Its calculation needs the actual canonical inverse. Small sampled transport residuals alone supply none of these norm values.

## Proof of (1)

Complexify the symmetric k-linear derivative tensor using the Hermitian orthonormal vectors (e_x+i e_y)/sqrt(2) and (e_x-i e_y)/sqrt(2). Unitary invariance of the tensor norm, with the binomial count of the positions of the first vector, gives the pointwise equality

    |D^k f|^2 = 2^(-k) sum_{j=0}^k binom(k,j)
        |D_+^j D_-^(k-j) f|^2,
    D_+ = partial_x+i partial_y,
    D_- = partial_x-i partial_y.                           (2)

This is a pointwise algebra identity. In particular using only D_+^k would not give (2) pointwise. For example f=xy has |D^2 f|^2=2 but |D_+^2 f|^2=4.

The polar forms are D_+=exp(i theta)(partial_r+i r^(-1)partial_theta) and D_-=exp(-i theta)(partial_r-i r^(-1)partial_theta). For an individual complex mode F(r) exp(i n theta), repeated use of these formulas gives

    D_+^j D_-^(k-j)[F(r) exp(i n theta)]
       = r^(-k) exp(i(n+2j-k)theta)
         product_{i=0}^{j-1}(r partial_r-n-2i)
         product_{h=0}^{k-j-1}(r partial_r+n-2h) F(r).       (3)

For example applying D_- once contributes r^(-1)(r partial_r+n); a subsequent D_- shifts n to n-1 and differentiates r^(-1), giving the next factor r partial_r+n-2. Applying a subsequent D_+ cancels the previously accumulated minus shifts, giving r partial_r-n. This proves (3) by induction, and also agrees with commutation of the two constant Cartesian operators. Substitution F=r d_n(t) replaces each r partial_r by E+1.

For a fixed j, the output frequencies n+2j-k are distinct for distinct input frequencies n. Parseval therefore applies without cross terms, including the negative input frequencies. Each sine coefficient gives complex amplitudes r d_n/(2i) and -r d_n/(2i) at frequencies n and -n. Since P_(k,j,-n)=P_(k,k-j,n), summing over j with binomial weights makes the positive and negative contributions equal. Thus the angular integral of (2) is exactly pi 2^(-k) r^(2-2k) times the sum in (1). Finally r dr=r^2 dt yields (1). Every step is valid at finite radii and needs only the stated derivatives.

## Independent radial differentiation and the full-plane inverse

The numerical Q family has a compact variable s in (0,1), w=1-s and

    r = L sqrt(s) [2(1-s)]^(-kappa),  kappa>1.

The stored Chebyshev coefficients determine polynomials B_j(2s-1). Direct multiplication of sin(theta) cos(2j theta) yields

    d_1=w[B_0-s B_1/2],
    d_(2j+1)=w s^j[B_j-s B_(j+1)]/2,  j>=1,              (4)

with omitted coefficients equal to zero. In this subsection d_n is always the coefficient of rho/r. Differentiating the map gives

    E s = 2s(1-s)/[1+(2kappa-1)s].                        (5)

Equations (4)-(5) generate logarithmic radial derivatives by finite Taylor arithmetic. They use neither the producer's radial differentiation matrix nor numerical differences of nearby coefficient values. The initial s is obtained by the independently implemented complementary map inversion. The density coefficients in (4) are evaluated by Chebyshev recurrence, without converting a large polynomial to floating monomials.

Write the canonical stream as psi=r^2 sum_{m even>=2} p_m(t) sin(m theta). Its two initial logarithmic data p_m and E p_m come from the separately implemented full-plane inverse, including both the regular interior and the infinite exterior. This is a necessary input, not a free homogeneous constant. The derivative source modes are

    h_m=(1/2)[(E+2-m)d_(m-1)+(E+m+2)d_(m+1)].             (6)

Applying the polar Laplacian to r^2 p_m sin(m theta) gives

    E^2 p_m = -4 E p_m+(m^2-4)p_m-h_m.                  (7)

This recurrence computes every further logarithmic derivative from the two independent initial inverse data and the density derivatives. It preserves the source and does not select a new gauge. For computing E^k(R/r), density derivatives through k+1 and stream derivatives through k+1 suffice. No local Poisson recurrence by itself determines p_m or its canonical exterior moment.

To construct R/r, set q_m=-m p_m, v_m=(E+2)p_m. Polar velocity gives U_r/r=sum q_m cos(m theta), U_theta/r=sum v_m sin(m theta). Therefore

    R/r = sum_n [(ell-1)d_n+ell E d_n] sin(n theta)
         +sum_(m,n) q_m(d_n+E d_n) cos(m theta)sin(n theta)
         +sum_(m,n) v_m n d_n sin(m theta)cos(n theta).    (8)

The identities 2cos(m theta)sin(n theta)=sin(n+m)theta+sin(n-m)theta and 2sin(m theta)cos(n theta)=sin(m+n)theta+sin(m-n)theta determine the residual sine coefficients with the sign of negative frequencies retained. There is no angular collocation or aliasing in this finite convolution. Derivatives of these products use the exact finite Leibniz rule.

## Endpoint conditions and numerical limitations

For an actual finite Q field the implicit function theorem applied to (5) in r^2 shows smoothness at zero, and s^j gives precisely the required r^(2j+1) factor of mode 2j+1. The canonical Green inverse is smooth there. At infinity let p=1-1/kappa in (0,1). Equations (4)-(7), or the convergent exterior inverse formulas, give D^h rho=O(r^(p-h)) and D^h U=O(r^(p-h)) at every fixed derivative order. To justify the latter directly, the interior Green moment is a finite integral of polynomial functions times an explicit power of 1-s; its power or logarithmic endpoint expansion has leading degree at most p and its decaying homogeneous terms have smaller degree. The exterior moment has the same leading bound. Logarithmic exceptional terms, if present in a lower degree, still obey the leading symbol bound. Differentiating the finite sums preserves these bounds. Consequently D^h R=O(r^(p-h))+O(r^(2p-1-h)). For k>=2, 2(p-k)+1<-1, so both D^k rho and D^k R are square integrable at infinity. Smoothness gives integrability at zero. Also ||D^k rho||_2 cannot vanish for a nonzero finite Q density of sublinear growth: vanishing kth derivatives would make it a polynomial of degree below k, and sublinear growth would make that polynomial constant, hence zero by odd-y parity.

Formula (1) remains an identity when numerical quadrature is used, but finite quadrature is not its proof. Reports must give the radial interval, nodes and precision, compare at least two independent quadrature levels, show endpoint shell contributions or tails, retain absolute norms, and distinguish numerical stability from a certified error enclosure. Positive integrands prevent signed angular cancellation; they do not prevent radial underresolution or loss of digits inside a differential polynomial.

Under rho_lambda(X)=lambda rho(X/lambda), the canonical velocity and residual have the same scaling. A change of variables gives ||D^k rho_lambda||_2=lambda^(2-k)||D^k rho||_2, and the same for R. Thus every eta_k is invariant. Comparing eta_k across states does not identify a limiting regularity class without compactness and control of the separate numerator and denominator. Ratios can mask divergent denominators. Smoothness alone gives no geometric Fourier convergence claim; analyticity requires separate evidence.

Dependencies: polar differentiation, finite-dimensional tensor algebra, angular Parseval on finite sums, the finite full-plane inverse formulas proved in research/q_full_inverse_primitives/PROOF.md, and elementary compact-map endpoint expansions. This result changes neither the primary admissible class nor the endpoint evidence standard.
