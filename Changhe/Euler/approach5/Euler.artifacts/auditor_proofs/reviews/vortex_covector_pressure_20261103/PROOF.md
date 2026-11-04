# Vortex covectors, canonical pressure and escaping half-lines

Status: CONFIRMED A673-A675 after complete source and independent proof postreads. Prepared 2026-11-03T10:01:20.634027+00:00.

## 1. Exact hypotheses and statements

Let U in C2(R3;R3), P in C1(R3), 0<c<1/2 and omega real. Put A=cI-omega J, where Jx=e3 cross x, B=Ax+U, Omega=curl U, a=1-2c, kappa=1+c, G=DU, S=(G+G^T)/2. Assume

    div U=0,
    (1-c)U+(B.grad)U+omega JU+grad P=0.

For the geometric assertions assume uniform sublinearity U=o(r) and global zero helicity U.Omega=0. Put H=P+|U|2/2+(Ax).U and g=U.B. Let p satisfy B(p)=0 and Omega(p)!=0. The previously confirmed carrier algebra gives U(p)!=0 and

    DB(p)^T U(p)=rho U(p), rho real.

Let L be the complete vortex line through p and M the connected component containing p of {H=H(p), grad H!=0, Omega!=0}. Then U!=0 on L, L is contained in M, g=0 on M, and on L

    grad H=-aU, grad g=rho U,
    (B.grad)U=rho U-DB^T U,                         (1)
    (B.grad)log|U|=rho-c-n.Sn, n=U/|U|,
    grad P=G^T U-(a+rho)U,
    G Ax=(rho-c)U-omega JU-2SU.                    (2)

On M, P=H(p)+|U|2/2 and U is normal to M, with the zero vector allowed away from L. These assertions do not need decay or a derivative bound. They are asserted only in the displayed parameter interval, where the global rank theorem is established.

Separately, assume 1<k<2 and the natural bounds

    |U(x)|<=C(1+r)^(-k), |DU(x)|<=C(1+r)^(-k-1).  (3)

No helicity assumption is needed for the pressure assertion. The actual pressure obeys

    |grad P|<=C r^(-2k-1),             1<k<3/2;
    |grad P|<=C r^-4 log(2+r),         k=3/2;
    |grad P|<=C r^-4,                 3/2<k<2.    (4)

Constants depend on the fixed parameters and bounds; uniformity at endpoints is not claimed. For k>3/2, with M_ij=integral U_i U_j and N(x)=1/(4pi|x|),

    grad P=M_ij partial_i partial_j grad N+O(r^(-2k-1)). (5)

Finally impose the geometric assumptions, (3), and k=(1-c)/c, hence 1/3<c<1/2. If either half of L is unbounded, its forward B-orbit y(t) escapes and

    r(t) asymp exp(ct),
    |U(y(t))| asymp exp((rho-c)t),
    |Omega(y(t))| asymp r(t)^(-1/c),                (6)
    H(p)=H_infinity.

If |grad P(y(t))|<=C r(t)^(-gamma), then

    rho=-a or rho<=c(1-gamma).                      (7)

For 2/5<c<1/2 this gives rho=-a or rho<=-2(1-c). A lower-window witness rho<=-2a therefore has rho<=-2(1-c) and lambda_min(S(p))<=c-2. No escape assertion or universal lower bound for rho follows.

## 2. Rank, the vortex line and completeness

The confirmed global helicity-free rank theorem A413 gives dH wedge dg=0 on {Omega!=0}. Its regular-level consequence A496 gives g=0 on M and

    grad g=-(rho/a)grad H,
    Phi_t^*dH=exp(rho t)dH on M.                  (8)

Here is the local argument specifying that consequence. At a regular point the rank and submersion coordinates imply g=F(H) for a local C1 function F. On overlapping neighborhoods along the connected regular level both F(H(p)) and F'(H(p)) agree. At p these are 0 and -rho/a. Since B.grad H=-ag, the level is invariant; differentiating this identity gives (8). Finite-time invariance of its regularity follows from the nonsingular derivative of the flow and (8), and nonvanishing of Omega follows from its Cauchy formula.

Uniform sublinearity makes B grow at most linearly, so its C1 flow is complete in both directions by the usual norm differential inequality. The exact bracket [B,Omega]=-kappa Omega gives on the vortex line gamma(tau), gamma(0)=p,

    B(gamma(tau))=kappa tau Omega(gamma(tau)).     (9)

Locally this follows by differentiating B along gamma and comparing with the bracket. Equivalently it is the confirmed A106 identity. Each nonzero half is a B-orbit with tau(t)=tau0 exp(kappa t). Completeness of B and uniqueness extend the identity to every finite nonzero tau. Near tau=0 the original local vortex solution extends it across p. Thus the full vortex parameter is real; there is no unproved completeness assumption for an arbitrary unbounded vorticity field. The Cauchy formula makes Omega nonzero at every finite point of the two half-orbits.

On L, helicity gives g=0 and grad H=B cross Omega-aU=-aU. Near p the latter is nonzero. On the component of L where U!=0 containing p, (8) gives grad g=rho U and (1). The linear covector equation (1) has bounded coefficients on each finite carrier-time interval; a nonzero solution cannot reach zero there. Every hypothetical endpoint on a half-line occurs at finite carrier time, since its tau is finite and nonzero. The neighborhood of p handles tau=0. Hence U!=0 on all of L and L is contained in M. This also removes any circular use of regularity of the whole line.

## 3. Covector and pressure identities

H is C2, since grad H=B cross Omega-aU is C1. Differentiating B.grad H=-ag on M and using (8) yields

    (B.grad)grad H=rho grad H-DB^T grad H.

Restrict to L and divide by -a to get (1). Since DB^T=cI+omega J+G^T, dotting with U proves its logarithmic norm formula. Equating (1) with momentum proves the first identity in (2); replacing B by Ax+U proves the second. No term in omega has been discarded except the exact identity U.JU=0.

On M, H=P-|U|2/2+g gives the asserted pressure value. Both B and Omega are tangent to M and orthogonal to U. Where they are independent they span its tangent plane. Where they are dependent, grad H=-aU. This proves normality everywhere, including points where U might vanish.

## 4. Poisson source, two moments and harmonic ambiguity

Momentum makes grad P C1. Taking its divergence, the two rotation traces cancel exactly and

    -Delta P=f=partial_i U_j partial_j U_i
              =partial_i partial_j(U_i U_j),
    |f(x)|<=C(1+r)^(-2k-2).                      (10)

Thus f and |x|f are absolutely integrable for k>1. For a smooth cutoff chi_R supported in B_(2R), equal to1 on B_R, integration by parts gives

    integral f chi_R=integral U_i U_j partial_ij chi_R=O(R^(1-2k)),
    integral x_l f chi_R=integral U_i U_j partial_ij(x_l chi_R)=O(R^(2-2k)).

Both tend to0. Absolute convergence therefore gives integral f=0 and integral x_l f=0. There are no omitted boundary terms.

The convolutions V=N*f and grad V=K*f, K=grad N, are absolutely convergent. Their distributional identities follow by local integrability of N,K and (10). Splitting into |z|<r/2, |x-z|<r/2 and their complement gives K*f=O(r^-2). On the second region f=O(r^(-2k-2)) and integral_(|w|<r/2)|K(w)|dw=O(r); the other regions use f in L1. Momentum and (3) give grad P=O(r^-k). Hence P-V is a harmonic distribution with gradient tending to0. Weyl regularity and the maximum principle for each entire harmonic gradient component give grad(P-V)=0. An additive pressure constant is the only remaining freedom. This argument identifies the actual pressure, without imposing a canonical normalization in advance.

## 5. Pressure bounds and the optional quadrupole

The two moment cancellations give

    grad P(x)=integral [K(x-z)-K(x)+DK(x)z] f(z)dz. (11)

For |z|<=r/2 the bracket is bounded by C r^-4 |z|2. The resulting radial integral is bounded by

    C r^-4 integral_0^(r/2) s4(1+s)^(-2k-2)ds.

It has exactly the three rates in (4). For |z|>r/2 the subtracted constant and linear terms cost, respectively,

    C r^-2 integral_(|z|>r/2)|f| <=C r^(-2k-1),
    C r^-3 integral_(|z|>r/2)|z f|<=C r^(-2k-1).

The K(x-z) term on |x-z|<=r/2 has the same bound by the local integral above; outside that ball bound K by Cr^-2 and use the tail mass of f. This proves (4) without a modulus for DU or a bound for D2U.

For k>3/2, |z|2 f is absolutely integrable. A second cutoff integration by parts gives

    integral z_i z_j f=2 integral U_i U_j=2M_ij.

All extra shell terms are O(R^(3-2k)) and vanish. Subtract the quadratic Taylor term from (11). In |z|<=r/2 its remainder is bounded by Cr^-5|z|3; the integral is O(r^(4-2k)), since k<2. Outside that region the second-moment tail is O(r^(3-2k)), and all other outer terms were already bounded. This proves (5). Nonzero trace-free M is possible for a smooth compactly supported helicity-free divergence-free field, for example U=h(z)(psi_y,-psi_x,0) with nonconstant radial compactly supported psi in the plane and compactly supported nonzero h. Then M=diag(m,m,0), m>0. This verifies sharpness in the static class only; such a field is not asserted to solve profile momentum.

## 6. Escape and the exact norm rates

For large r,

    r'=cr+(y/r).U>cr/2.

Once a forward orbit exits a sufficiently large ball it cannot return; unboundedness therefore implies eventual monotone escape. Since r grows at least exponentially, (3) makes

    (log r)'-c=O(r^(-k-1))

integrable, proving r exp(-ct) tends to a positive finite constant. The logarithmic norm equation in (1) and integrability of |S(y(t))| similarly show |U(y(t))|exp(-(rho-c)t) tends to a positive finite constant. No convergence of the direction of U is required.

Equation (9), |Ax+U| asymp r (because c>0), and tau=tau0 exp(kappa t) give |Omega| asymp exp((c-kappa)t)=exp(-t). This is (6). In particular it is the full vorticity norm along this trajectory that has the natural rate. Its projected angular field may nevertheless vanish at its scattering direction, as A602 separately proves.

The identity grad H=B cross Omega-aU and (3) give grad H=O(r^-k). Integrating radially shows a limit in each direction with uniform error O(r^(1-k)). The oscillation on a sphere is also O(r^(1-k)), so these limits coincide: H=H_infinity+O(r^(1-k)) uniformly. Constancy of H along L proves H(p)=H_infinity. Since B(p)=0, U(p)=-Ap and H(p)=P(p)-|Ap|2/2; thus P(p)-H_infinity=|Ap|2/2. This is invariant under adding a pressure constant.

## 7. Pinning the rate and its limits

From (2), at a point on L,

    |a+rho|<=|S|+|grad P|/|U|
            <=C r^(-k-1)+C r^(-gamma-(rho-c)/c).

If rho!=-a, the right side cannot tend to0. Therefore -gamma-(rho-c)/c>=0, proving (7). In the target interval (4) supplies gamma=2k+1, giving c(1-gamma)=-2(1-c). For k>3/2 it supplies gamma=4, giving rho<=-3c apart from the exceptional value. At k=3/2, if rho>-3c the same quotient tends to0 despite the logarithm, so rho<=-3c again. Comparison with the global velocity bound alone only gives rho<=-a.

At p, dot DB(p)^TU(p)=rho U(p) with its unit direction to get rho=c+n.S(p)n. Thus a lower-window escaping witness has n.S(p)n<=c-2 and lambda_min(S(p))<=c-2. This is an upper bound on rho, not an exclusion of every negative rate. Both halves may be bounded, and those are handled by A657-A659, not by this argument.

## 8. Dependencies and audit scope

This proves all four parts of B31 Proposition1 and Lemma PG, including its stated endpoint and quadrupole remarks, and Proposition2(a)-(c). The global rank and carrier data are the explicitly confirmed A413, A428, A478 and A496 inputs; the line identity is A106 and was rechecked above. The natural bounds (3) can be supplied by uniform decay plus bounded DU through A476-A477/A492, or by the precise alternatives A601. They do not follow here from decay alone. The geometric result assumes uniform sublinearity and global zero helicity; the pressure estimate does not need zero helicity.

B31 Remark(iv)'s phrase that no range beyond a!=0 is used is not part of this verdict: the global rank input here has 0<c<1/2. Its ordinary statement in Section1 is correct with that range retained. Proposition3's norm argument is already implied by the same covector calculation, but its unqualified parenthetical reference to a curve through w_+ presupposes an escaping L+ and is not asserted for bounded L+. Proposition2(d) remains A602 with its projected-field qualification. There is no nonexistence theorem in this file. No computation, formalization or external literature claim was needed.
