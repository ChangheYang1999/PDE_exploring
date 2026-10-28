# Pairing the residual separately at each radius

## Statement

Let 0<a<1 and let [f]_a=sup_{z!=w}|f(z)-f(w)|/|z-w|^a for real functions on R^2. The operators T_xx and T_xy are the circular principal-value operators with kernels cos(2theta)/(2 pi r^2) and sin(2theta)/(2 pi r^2), extended to the homogeneous Holder space modulo constants by convergent increments. Their common operator seminorm is C_a.

Use the accepted local-circle construction of ../existing_certificates/PROOF.md. Fix one radial row [u,v], with 0<u<v<=1/2, and one phase phi. Let m_l be its extracted signed integer angular masses, with mass unit U. Define

    S = sum_l m_l/U,
    tau = v_phi-sum_l |m_l|/U,
    q(r) = -r^2 cos(phi)-S.

Here v_phi is the certified upper bound for the original angular total variation, uniform in r in [u,v]. The extraction is a signed submeasure, also uniform in r, so the unextracted right measure per unit dr/r has variation at most tau and signed mass exactly q(r). Its left counterpart is its negative central reflection. In particular tau>=0 and |q(r)|<=tau.

Define g_a(r)=(1+2r)^a-(2r)^a. For 0<s<t set

    L(s,t) = log(t/s),
    H(s,t) = 1/2-s^2 L(s,t)/(t^2-s^2),
    J(s,t) = [L(s,t)-H(s,t)] |q(s)|+H(s,t)|q(t)|,
    E_a(s,t) = tau 2^a(t^a-s^a)/a
                 +g_a(s) min(tau L(s,t),J(s,t)).       (1)

For any finite partition u=s_0<...<s_N=v, the paired residual on this row costs at most

    sum_{i=0}^{N-1} E_a(s_i,s_{i+1}) [f]_a.           (2)

It may therefore replace the former residual upper bound in the accepted whole-operator construction. The minimum of (2) and the accepted aggregate residual bound is valid. No transport edge or extracted integer mass changes. No new numerical bound is asserted until outward evaluation and complete recombination.

## Proof

For each fixed r, apply ../PROOF.md to the right residual measure on the circle of radius r about x=(1/2,0) and its negative reflection about y=-x. Its support lies in B(x,r); its variation is at most tau; its signed mass is q(r). The pairing cost is at most

    tau(2r)^a+|q(r)|g_a(r).

The angular densities and their fixed cell extractions are measurable in r. The local interval lies away from the poles and all displayed bounds are finite. Fubini's theorem therefore allows this pointwise estimate to be integrated against dr/r. Equivalently, apply the estimate to each angular integral of f before integrating the nonnegative upper bound; no measurable choice of a coupling is required.

The first term integrates exactly to tau 2^a(t^a-s^a)/a. For the second, g_a is positive and decreasing because

    g_a'(r)=2a[(1+2r)^(a-1)-(2r)^(a-1)]<0.

The function q(r) is affine in r^2. Convexity of the absolute value gives, for s<=r<=t,

    |q(r)| <= [(t^2-r^2)|q(s)|+(r^2-s^2)|q(t)|]/(t^2-s^2).

Integrating against dr/r gives the upper bound J(s,t), since

    integral_s^t (r^2-s^2)/(t^2-s^2) dr/r
       =1/2-s^2 log(t/s)/(t^2-s^2)=H(s,t).

The integrand defining H lies strictly between zero and one in the interval interior, so 0<H<L. This also proves that both coefficients in J are nonnegative. The separate bound |q(r)|<=tau gives integral |q(r)| dr/r<=tau L. Multiplication by the positive number g_a(s) and addition of the exact first term proves (1). Summation proves (2).

Both the radius-by-radius bound and the older aggregate bound estimate the same residual functional. Taking their minimum is valid. The parent construction adds unchanged extracted transport, middle and exterior costs, and the uniform omitted-disk cost. Its finite phase interpolation and homogeneous-space completion remain applicable. This proves the stated replacement rule, including all principal-value and infinity limits through the accepted parent theorem.

## Numerical requirements and dependencies

A certificate must retain the original radial endpoints, signed integer masses, angular variation bound, and their source hashes. It must evaluate all positive powers, logarithms and cosines outward. For exact phi=pi/2, cos(phi)=0 may be used symbolically. Otherwise an interval for cos(phi) suffices. Form tau with an upper endpoint for v_phi and exact rational sum_l|m_l|/U. Form |q(s)| and |q(t)| with outward endpoints. Use only certified nonnegative coefficients L-H and H; if finite precision cannot establish this, increase precision or use the coarser accepted bound. Any finite rational partition is allowed, since no prescribed transcendental grid is being approximated.

The unchanged whole-operator construction and source-identity checks are in ../existing_certificates/PROOF.md and its numerical_values/PROOF.md. The measure lemma is ../PROOF.md, accepted as V150. The older aggregate numerical certificates were accepted as V152. This proof was written before the new computation; independent lead cross-read is pending.
