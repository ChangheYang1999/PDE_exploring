# Independent selected-mode Laplacian audit for candidate 007

## Statement, notation and hypotheses

The reference is the exact rational potential of
C1-N1-007-d2w-j7-e2bal. Its independently reconstructed canonical file has
SHA-256 153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316.
Let c=4076476460239181/2251799813685248, delta=1-1/c and A=1+1/c.
Put rho=-partial_y Delta chi, u=(-chi_xyy,chi_xxy), and
F=(cX+u).grad rho-rho on the whole plane. Let Pi_n be orthogonal
projection onto sin(n theta), with full-circle angular measure dtheta.

For 0<a<2 and 0<s<1, q=2+s, w=(1+r²)^(-a/2), use exactly the
dyadic space Y of the frozen T4_Y_PROOF.md. Explicitly, for the canonical
velocity U[h]=(-R1R2 h,R1² h),

    Y(h)² = ||wh||2² + ||chi0 h||Hq² + ||chi0 U[h]||Hq²
      + sum_(j>=1) 2^(2(1-a)j)
        (||chi(.)h(2^j .)||Hq² + ||chi(.)U[h](2^j .)||Hq²).

The Hq norm uses the unitary Fourier transform. The fixed smooth radial
cutoffs take values in [0,1]; chi0 is one on r<=2 and zero on r>=4;
chi is one on 1<=r<=2 and zero outside 1/2<r<4. No choice of their
transition shapes enters the lower bound below.

Define J_n(a)=||(1+r²)^((2-a)/2) Delta Pi_n F||2 and
J_S(a)=(J_1(a)²+J_3(a)²)^(1/2). Then

    Y(F) >= 5^((a-2)/2) J_S(a).                         (1)

Under the independently reviewed inverse-floor and contraction-radius
hypotheses of the registered FW-T-DYADIC-Y-v1 scheme, closure requires

    Y(F) < B(a)=sqrt(8 pi)(1+c-ca)²/(1+a), 0<a<A.        (2)

The accompanying computation reproduces J_1 and J_3 at a=k/4,
k=0,...,7. Four strict interval comparisons imply failure of (2) for
4/5<=a<A. The positive low rate required by that scheme already fails
for A<=a<2. No conclusion for 0<a<4/5 is asserted here.

## Proof of the continuous and cell bounds

On each cutoff plateau, its derivatives vanish. Since q>2,
||g||Hq>=||Delta g||2. Rescaling the jth shell gives

    Y(F)² >= ||Delta F||²_(r<2)
       + sum_(j>=1) 2^(2(2-a)j)
                    ||Delta F||²_(2^j<r<2^(j+1)).

The core and shells partition the plane up to null circles. On the
core 1+r²<=5; on shell j, 1+r²<=5*2^(2j). Since a<2,
the last display dominates 5^(a-2) J_full(a)². Angular orthogonality
commutes with Delta and with radial weights, so J_full>=J_S. This
proves (1), even if the full norm is infinite.

For the scheme in (2), its established high inverse floor is
M>=1/(1+c-ca), and its radius ceiling is
R<sqrt(8 pi)(1+c-ca)/(1+a). Thus M Y(F)<=R implies (2).
All analytic hypotheses of those theorems are retained; the present
calculation supplies no replacement high inverse estimate.

J_S(a) is decreasing by pointwise monotonicity of its squared
integrand. The factor 5^((a-2)/2) increases. B(a) decreases on [0,A].
For a cell [l,h] it suffices to check

    5^((l-2)/2) J_S(h) > B(l).

Use [4/5,1], [1,5/4], [5/4,3/2], [3/2,A]. In the last cell use the
smaller J_S(7/4), since A<7/4. These are interval certificates, not
an interpolation claim from a grid.

## Independent exact reconstruction and integration

Write t=r²/(1+r²), v=1-t. The existing independent Cartesian
potential derivative engine constructs rho, rho_x, rho_y, u1 and u2.
For a cosine factor cos(n theta) and a sine factor sin(m theta), the
coefficient of sin(k theta) in their product is

    (1_(m+n=k)+1_(m-n=k)-1_(m-n=-k))/2.

Using this identity in u1*rho_x+u2*rho_y retains every background
frequency pair contributing to k=1 or k=3, without assembling the
other residual frequencies. The linear part is differentiated from
the same exact potential. Exact origin divisibility is checked.
This gives

    Pi_k F = r sum_ell v^(ell delta/2) P_(ell,k)(t) sin(k theta).

Differentiate the resulting finite Fourier expression twice in
Cartesian coordinates and add the traces. Independently check the
polar identity, coefficient by coefficient,

    t L_(ell,k) = T_d(T_d P_(ell,k))-k² P_(ell,k),
    T_d P=(1-2dt)P+2t(1-t)P', d=ell delta/2.

Thus Delta Pi_k F = r sum_ell v^(1+ell delta/2)L_(ell,k)(t) sin(k theta).
The exact mixed Cartesian derivatives are checked equal. Angular
orthogonality and r dr=dt/(2v²) give

    J_k(a)²=(pi/2) sum_(ell,b)
      integral_0^1 v^(a+(ell+b)delta/2-3)(1-v)
                    L_(ell,k)(1-v)L_(b,k)(1-v) dv.

Every diagonal endpoint order is tested for integrability. Combine
each polynomial product exactly before evaluating all finite power
integrals. Off-diagonal branch products have multiplicity two; none
is dropped. For each surviving monomial v^e, check e>-1 and use its
exact integral 1/(e+1). Outward ball arithmetic encloses the rational
sum and the final square root with pi. This uses no quadrature.

## Dependencies and verification scope

Dependencies are the independent exact potential derivative engine,
Cartesian residual derivative engine and the previously reviewed
plateau, inverse-floor and radius theorems. Their source identities,
all frozen peer records, and exact candidate identity are registered
in the output. A peer comparison checks the separately generated
T4 mode moments and its four-cell cover. Mode sums from 5 through15
are unnecessary and are not audited here. This is a scheme-specific
necessary-test failure, not nonexistence of a stationary profile.
