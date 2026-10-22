# Exact center-strain shells and their scale dependence

Date:2026-10-20. Status: proved for the stated fields and separately for the represented spline functions. No PDE assumption is needed.

## Statement and hypotheses

Let Omega be smooth, odd in x, Omega=O(r) at zero and O(r^-nu) uniformly in angle at infinity, nu>0. Use Omega=-Delta Psi and V=(-Psi_y,Psi_x). The centered canonical inverse means

    V(X)=integral [B(X-Y)+B(Y)]Omega(Y)dY,
    B(Z)=(Z2,-Z1)/(2pi|Z|^2).

This integral is absolutely convergent: the centered kernel is O(|Y|^-2) at infinity, and its local singularities are integrable against the smooth source. It is sublinear and vanishes at0. A sublinear inverse with these conditions is unique, since its difference from V is an entire harmonic sublinear vector field, hence constant and then zero. In particular no harmonic quadratic stream term is allowed. Put c=partial_x Psi_y(0). Use X=(r sin phi,-r cos phi) and the sine coefficients

    H_n(r)=(1/pi) integral_0^(2pi) Omega(r sin phi,-r cos phi) sin(n phi) dphi.

Then the signed strain outside radius R and its total variation are

    C_>(R)=-(1/2) integral_R^infinity H_2(r) dr/r,
    c=C_>(0), C_abs=(1/2) integral_0^infinity |H_2(r)| dr/r.

They converge absolutely and C_abs>=|c|. For c nonzero define cancellation ratio C_abs/|c|. If H_2(r)=a_2 r^-nu+O(r^-2nu), then

    C_>(R)=-(a_2/(2nu)) R^-nu+O(R^-2nu).

Thus a mandatory nonzero vorticity tail does not imply tail-dominated strain, nor even that its n2 coefficient is nonzero. The signed shell contribution can be negative even when c is positive.

For the verifier's r2 spline basis let b>0 be its beta_basis, L>0, t=1-(1+(r/L)^2)^(-1/(2b)), z=1-t, and let S_k(t) be the masked spline coefficients of G=Omega/x. The radial factor is z^(b+1), with an additional r/sqrt(r^2+L^2) for odd angular k, and the angular factors cos(k phi). Put D(t)=S_1(t)-S_3(t), with S_3=0 if absent. Then EXACTLY for this represented field,

    c=-(bL/4) integral_0^1 D(t) dt,
    C_>(R)=-(bL/4) integral_t(R)^1 D(t) dt,
    C_abs=(bL/4) integral_0^1 |D(t)| dt,
    a_2=(L^(1+1/b)/2) D(1).

The endpoint tail coefficient formula holds for every b>0. Its general remainder is O(r^(-nu-min(nu,2))), nu=1/b. Thus the earlier conditional O(r^-2nu) remainder applies to the spline case when b>=1/2, including every basis used here. All exact spline integrals and the final-cell polynomial identity hold for every b>0.

The mask is S_k coefficient indices0 through floor(k/2)-1 set to zero. With clamped knots it gives S_k=O(t^floor(k/2)) near0, or identically0 near0 when that index lies beyond the first cell. This cancels the apparent polar singularity: r^k cos(k phi) is a homogeneous polynomial, and the remaining factors are analytic functions of r^2 near0. Consequently the represented fields are smooth at the origin. At nonzero spline knots they have the finite differentiability of the splines, not generally global C-infinity. The shell formulas require only the displayed size bounds and integrability.

The integral of |D| can be evaluated by splitting each polynomial cell at its real zeros. Floating-point root finding is numerical evidence, not a rigorous root certificate.

## Proof

For the centered full-plane inverse the exact strain moment is c=(1/pi) integral xy Omega/r^4 dX. Since xy=-(r^2/2)sin(2phi), angular orthogonality gives the displayed one-dimensional formula. Absolute convergence follows near zero from |H_2|=O(r) and at infinity from O(r^-nu). The same computation with radial cutoffs defines C_>. Triangle inequality gives C_abs>=|c|. Integrating the stated tail term and its uniform remainder gives the asymptotic formula, including the factor1/(2nu).

For the spline field, the identity sin phi cos(k phi)=[sin((k+1)phi)-sin((k-1)phi)]/2 shows that only k1 and k3 contribute to H2. Therefore

    H_2(r)= [r^2/(2sqrt(r^2+L^2))] z^(b+1) D(t).

Direct differentiation of r=L sqrt(z^(-2b)-1) gives

    (H_2(r)/r) dr=(bL/2)D(t)dt.

All exact integral formulas follow by substitution, and the positive Jacobian gives the absolute integral formula. Finally z~(L/r)^(1/b), giving the value of a2. On the final polynomial cell, an optional exact finite expansion is

    C_>(R)=-(bL/4) sum_(j=0)^degree [(-1)^j D^(j)(1)/(j+1)!] [1-t(R)]^(j+1).

This last identity holds whenever t(R) lies in that final cell. It is a polynomial identity in1-t, not merely an asymptotic series.

## Scaling and comparison scope

For positive spatial scale l, Omega_l(X)=Omega(X/l) and c_l=c. Substitution gives C_l,>(R)=C_>(R/l), while C_abs and its cancellation ratio are invariant. Negative signed scale adds a pi angular shift, which also leaves sin2phi unchanged; replace l by|l|. Thus a tail fraction at one fixed numerical radius depends on spatial normalization. A cancellation ratio does not. Comparing several a0 values under a fixed external forcing compares different normalized fields; it does not prove a scale-invariant concentration theorem.

The tail coefficient scales as a2_l=|l|^nu a2. For an explicit positive-total/negative-tail example, take

    Omega=xy[A exp(-r^2)-(1+r^2)^(-(nu+2)/2)], A>2/nu.

Direct integration gives C_>(R)=(A/8)exp(-R^2)-(1/(4nu))(1+R^2)^(-nu/2). Thus c=A/8-1/(4nu)>0 and C_>(R)<0 at large R. Separately, Omega=x(1+r^2)^(-(nu+1)/2) has a nonzero leading tail but H2 identically0. These are vorticity examples only, not profiles.

All statements concern the inverse and vorticity alone. They neither bound a profile residual nor establish a continuum branch or nonexistence. The PDE can impose further relations that are not used here.
