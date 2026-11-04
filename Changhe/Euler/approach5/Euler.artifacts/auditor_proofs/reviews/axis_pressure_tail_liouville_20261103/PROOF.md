# Axis pressure excludes an axisymmetric actual leading tail

Status: independently CONFIRMED at A569-A570 after complete source, proof and focused existing model comparison. The extra helicity, derivative and actual-tail symmetry hypotheses are explicit.

## 1. Standalone pressure statement

Let D=R3 minus{0}, 1<p<3/2 and V in C1(D;R3) be ordinarily homogeneous of degree -p. Suppose V is axisymmetric about the third axis and purely azimuthal, with its actual Cartesian C1 extension through the nonzero axis. Write V=r^-p F(z)e_phi/s, z=x3/r, s=sqrt(1-z^2). Then V=0 on the axis. Set N(x)=1/(4pi|x|), T_ij=V_i V_j and Pcan=partial_i partial_j N*T_ij distributionally on R3. At every nonzero axial X,

    Pcan(X)=-(1/(4pi)) integral |V(y)|^2/|X-y|^3 dy. (1)

This is an absolutely convergent integral, strictly negative if V is not zero. Any C1 pressure P2 on D of degree -2p satisfying -Delta P2=partial_i partial_j T_ij on D equals Pcan. Thus no nonzero such V,P2 can obey

    P2-|V|^2/2=C r^-2p |F(z)|^nu, nu>0, C finite. (2)

No sign of C or F is needed by this pressure test.

## 2. Definition, local regularity and the contact term

On the unit sphere V is bounded, so |T(y)|<=C|y|^-2p. For a compactly supported smooth test phi, D_ij N*phi is smooth and bounded on compact sets and O(|y|^-3) at infinity. Consequently its pairing with T converges absolutely: the radial integrals are integral_0^1 r^(2-2p)dr and integral_1^infinity r^(-1-2p)dr. This defines Pcan without choosing a finite part at the origin. It solves the stated pressure equation distributionally on the whole space and has exact degree -2p by change of variables in test pairings.

The field V is divergence free off the axis by pure azimuthal axisymmetry and across it by C1 continuity. Therefore partial_i partial_j T_ij=tr((DV)^2) locally on D in distributions. This follows by smoothing the C1 field or by the first product rule followed by distributional differentiation. The local source is continuous. On a ball compactly inside D, a Newton potential of a continuous compactly supported extension of that source is C1 because N and grad N are locally integrable. Subtracting it from Pcan leaves a harmonic distribution on a smaller ball, hence a smooth function. Thus Pcan has a C1 representative on D. No second derivatives of V are assumed.

Twice integrating by parts outside a small ball gives

    D_ij N=PV[(3x_i x_j-delta_ij|x|^2)/(4pi|x|^5)]
                         -(delta_ij/3)delta_0.

The boundary coefficient is fixed by integral_S2 n_i n_j=(4pi/3)delta_ij. Its contraction with T gives

    Pcan(x)=-|V(x)|^2/3+(1/(4pi)) PV integral
       [3((x-y).V(y))^2/|x-y|^5-|V(y)|^2/|x-y|^3]dy. (3)

At an off-origin evaluation point, subtract T(x) in a small ball. The constant part has zero angular average, while T(y)-T(x)=O(|x-y|), so the remaining local integrand is absolutely integrable. The singularity of T at0 and its infinite tail are integrable by the preceding radial bounds. Therefore this principal value represents the actual continuous pressure, with exactly the displayed contact term.

## 3. Strict sign on the axis

For X on the axis, azimuthal geometry gives (X-y).V(y)=0 and V(X)=0. Formula(3) becomes(1). At y=X, local C1 regularity implies |V(y)|<=C|y-X|, so its integrand is bounded by C|y-X|^-1. At y0 the denominator stays bounded below and |V|^2 is integrable since2p<3. At infinity its radial bound is C r^(-2p-1), integrable sincep>0. The remaining region has no singularity. Thus no principal-value cancellation is being used in(1).

If V is nonzero, it is nonzero on an open subset of D. The nonnegative integrand has a strictly positive integral, proving Pcan(X)<0 on both nonzero half-axes.

## 4. No homogeneous harmonic ambiguity

Let h=P2-Pcan. It is harmonic on D and homogeneous of degree -2p. Its Kelvin transform K(x)=|x|^-1 h(x/|x|^2) is harmonic on D and homogeneous of degree d=2p-1 in(1,2). The transform identity follows by direct differentiation: Delta K=|x|^-5(Delta h)(x/|x|^2). Smooth angular data give |K|<=Cr^d and |grad K|<=Cr^(d-1) near0.

Extend K by0 at0. Integrating by parts outside radius epsilon leaves terms bounded by C epsilon^(d+1) and C epsilon^(d+2), both vanishing. Hence K is harmonic distributionally on the whole space and smooth near0. Its value and gradient vanish there. Taylor's theorem gives K=O(r^2); homogeneity then gives |K(theta)|<=C r^(2-d) for every unit theta, forcing K and h to vanish. This proves pressure uniqueness rather than imposing a normalization. The strict exponent interval excludes both harmonic resonances and the nonintegrable stress endpoint.

Cartesian continuity makes V_phi and F vanish at the poles. Taking pole limits in(2) gives P2(X)=0 for nonzero axial X, contradicting the strict sign unless V=0. This completes the standalone pressure theorem.

## 5. Axisymmetric tail classification and its exact activation

Let 2/5<c<1/2, p=(1-c)/c, a=1-2c, A=cI-omega J, with every fixed finite omega. Let V,P2 be C1 ordinarily homogeneous of degrees-p,-2p, both axisymmetric. Assume div V0, W=curl V, V.W0, the actual distributional pressure equation, W.grad S0, and grad k cross grad S0 on {W!=0}, where S=P2-|V|^2/2 and k=(Ax).V.

The independently confirmed A561 applies at these precise hypotheses, even though it was proved on the larger c interval(1/3,1/2). Its full proof is in the team records. It says every nonzero such V is pure azimuthal, with F of one strict sign off the axis and S=C r^-2p |F|^(2p/(p-1)), C<0. It does not assume global grad k0 or any original swirl. Its swirl-free completion uses an interior extremum of the meridional scalar and the rank-based endpoint plateau obstruction. The positive endpoint quadratic and pressure equation require only C1 velocity, not a twice differentiable angular velocity.

Since target c gives1<p<3/2, Sections1-4 exclude precisely this necessary pure-swirl branch. Therefore V=0 under the listed standalone tail hypotheses. This uses the pressure over the whole space, not a false local pole-indicial argument. It does not apply to a merely proper cone or to symmetry of a single harmonic pressure multipole.

## 6. Conditional full-profile nonexistence

Suppose U in C2(R3;R3), P in C1(R3) solve

    div U=0, [(1-c)I+omega J]U+DU(Ay+U)+grad P=0,
    U.curl U=0 on R3,
    |U(y)|<=C(1+|y|)^-p, |DU(y)|<=C(1+|y|)^(-p-1). (4)

Assume the actual leading velocity tail V is axisymmetric about the rotation axis. The verified natural tail, pressure and rank results A516,A530,A531,A533,A538,A539 supply V in C1alpha_loc for each alpha<1, its actual curl, pressure P2 in C1, and every scalar and rank identity in Section5. The twisted homogeneity becomes ordinary homogeneity when V is axisymmetric: substitute its rotation covariance into V(exp(tA)x)=exp(-(1-c)t)Q_t transpose V(x). The canonical pressure commutes with rotations, so P2 is axisymmetric as well. Section5 gives V=0.

For completeness the tail-to-profile step requires no additional Liouville citation. Put L=(1-c)I+omega J and N0=DU U+grad P. By A516, |grad P|<=Cr^(-2p-1) and |P-Pinf|<=Cr^-2p. Thus |N0|<=Cr^-q, q=2p+1>3. The linear spiral identity is

    d/dt [exp(tL)U(exp(tA)x)]=-exp(tL)N0(exp(tA)x).

Its limit is the actual V(x)=0. Since (1-c)-cq=-1, integrate to get

    U(x)=integral_0^infinity exp(tL)N0(exp(tA)x)dt,
    |U(x)|<=Cr^-q.                                (5)

Dotting the full momentum equation with U gives

    (1-5c/2)|U|^2+
    div[(Ay+U)|U|^2/2+(P-Pinf)U]=0.               (6)

Use a radial smooth cutoff at radius R. The drift, cubic and pressure boundary terms are respectively bounded by C R^(3-2q), C R^(2-3q) and C R^(2-2p-q), all tending0. The rotational drift has exactly zero radial flux. Dominated convergence yields (1-5c/2)integral|U|^2=0, hence U=0 sincec>2/5.

An alternative exact hypothesis set replaces the two bounds in(4) by uniform U->0 and DU=O(sqrt r): A498,A476,A492 and the natural-tail estimates supply(4). Global helicity zero and symmetry of the actual V remain additional. This is nonexistence for that conditional class, not the bare-decay arbitrary-omega theorem.

## 7. Verification and model comparison

The full seven-section LIT150 source was read. Every kernel sign, the contact term, origin and infinity integral, Kelvin boundary term, exponent, and final energy flux is independently checked above. A561's full proof and swirl-free completion were already independently postread. The actual configured-model coordinator in the team records was subsequently read in full and compared against every pressure and energy step. Its spectral uniqueness alternative agrees with the independently checked Kelvin argument. Its exact natural-pressure input is A516; that dependency was separately checked here. This is the existing the primary model agent configuration, not independent provider attestation.
