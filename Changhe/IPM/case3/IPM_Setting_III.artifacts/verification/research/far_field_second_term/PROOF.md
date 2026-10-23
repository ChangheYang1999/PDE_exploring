# The second far-field coefficient of an exact smooth profile

Date: 2026-10-20. Status: CONFIRMED after independent proof, exact and manufactured checks, and actual lead Opus 5.5 review on 2026-10-20. The result is conditional on an exact profile, not on a sampled small residual.

## 1. Statement

Let ell>1 and let rho,psi,U be a smooth primary profile on the entire plane:

    (ell X+U).grad rho=rho, U=(-psi_y,psi_x), -Delta psi=rho_x,
    rho even in x and odd in y, psi odd in both variables,
    U=o(r), rho_y(0)!=0,
    |rho|+(1+r)|grad rho|<=C(1+r)^gamma, 0<gamma<1.

Put p=1/ell, D=ell-1, q=2p-1 and t=3p-2. Let Theta_0 be its already proved smooth angular limit. Define the unique smooth odd-odd angular stream factor Phi_0 by

    -Phi_0''-(p+1)^2 Phi_0
                  =p cos(theta)Theta_0-sin(theta)Theta_0'.       (1)

Here odd-odd means that Phi_0 is a sine series with positive even frequencies. Set

    u_0r=-Phi_0', u_0theta=(p+1)Phi_0,
    Theta_1=[p u_0r Theta_0+u_0theta Theta_0']/D.                (2)

Let Phi_1 solve the same equation with p,Theta_0 replaced by q,Theta_1, and put u_1r=-Phi_1', u_1theta=(q+1)Phi_1. Then, for every integer k>=0,

    |D_X^k[rho-r^p Theta_0-r^q Theta_1]|<=C_k r^(t-k),
    |D_X^k[U-r^p u_0-r^q u_1]|<=C_k r^(t-k), r>=R0.           (3)

The vector expressions use the polar frame at X. The homogeneous stream factors define canonical auxiliary velocities distributionally; the auxiliary densities may be singular at zero. They are not proposed smooth profiles. Since q is in (-1,1), the factors (m^2-(q+1)^2) at even frequencies m>=2 are nonzero. In particular ell=2, q=0, is not a resonance. No interior-topology or sign assumption is added.

## 2. A weighted inverse estimate, including negative exponents

We need the following elementary lemma. Suppose f is locally integrable, centrally odd, smooth off a fixed compact set, with

    |D^j f(X)|<=C_j r^(b-j), r>=1, -3<b<1,
    integral_(|Y|<1) |Y| |f(Y)| dY<infinity.

Use the canonical contact kernel at queries outside that compact set:

    T f(X)=-f(X)e2/2+PV integral K(X-Y)f(Y)dY,
    K(Z)=(-Z1 Z2/pi,(Z1^2-Z2^2)/(2pi))/|Z|^4.

At infinity interpret it with subtraction K(-Y) on centered exterior annuli. That subtraction integrates to zero by central oddness. Then

    |D^j Tf(X)|<=C_j' r^(b-j), r>=R1.                       (4)

The local singularity at the query is treated by subtracting f(X) in a centered disk of radius comparable to r. The gradient bound gives an absolute contribution at most C r^b. On the remaining annulus |Y| comparable to r the estimate follows by size after a smooth localization. In the inner disk |Y|<r/2, central oddness gives integral f=0. Subtract K(X) there to bound the contribution by

    C r^-3 integral_(|Y|<r/2) |Y| |f(Y)|dY
        <=C r^-3[1+integral_1^(r/2) s^(b+2)ds]<=C r^b.

This is the reason for b>-3. Bounding the same region without its odd cancellation would lose the available range of weights. The exterior estimate is

    C r integral_(2r)^infinity s^(b-2)ds<=C r^b,

which needs b<1. A fixed compact annular partition covers any overlap in these regions.

For derivatives, rescale a query annulus to unit size and localize its density with a fixed smooth cutoff. Commuting any fixed number j of derivatives through this localized order-zero kernel bounds the result using the C^(j+1) bounds of the scaled density; all cutoff derivatives are uniformly bounded. In the inner separated piece use D_X^j K(X-Y)-D_X^j K(X), bounded by C_j r^(-3-j)|Y|. In the exterior, derivatives of order j>=1 have bound C_j |Y|^(-2-j), so their integral is C_j r^(b-j), because b<1<=j. The j=0 exterior uses the preceding subtraction. These arguments also bound derivatives of partition cutoffs. This proves (4) for every j. The finite compact contribution to (4) has size r^(-3-j), which is no larger than r^(b-j).

## 3. Auxiliary homogeneous inverses

For a smooth angular density r^a Theta with -1<a<1 and the density parities, the query integral away from zero is well defined. The density is locally integrable at zero. Exterior cancellation is as above. The change of variables Y=lambda Z proves homogeneity of degree a of its canonical velocity: any annulus created by changing the reference exterior cutoff has zero integral by parity.

The right side of the angular stream equation has only sine modes m=2,4,... . Divide each Fourier coefficient by m^2-(a+1)^2 to obtain Phi. Smoothness follows from rapid Fourier-coefficient decay, and the denominator never vanishes for -1<a<1. The field J grad(r^(a+1)Phi) has the correct div-curl equations away from zero. They also hold distributionally across zero: its magnitude is O(r^a), so the small-circle boundary error against a fixed test function is O(r^(a+1)), tending to zero. The same estimate applies to the density derivative. Thus this field equals the kernel inverse. Indeed their difference is an entire harmonic distribution, hence a smooth harmonic vector field, sublinear at infinity; it is a constant, and parity removes it. This proves the assertions for a=p and a=q used in (1)-(3).

## 4. First error and the corresponding velocity error

The already verified ../local_ipm_continuation/PROOF.md gives every symbol estimate

    |D^j rho|+|D^j U|<=C_j r^(p-j),
    ||r^-p rho(r,.)-Theta_0||_Ck<=C_k r^(p-1).              (5)

Its input ../far_field_holder/PROOF.md supplies the noncircular density and velocity limits. Write s=log r, f=r^-p rho and u=r^-p U. Exact transport gives

    f_s=-r^(p-1)[p u_r f+u_theta f_theta]
                                      /[ell+r^(p-1)u_r].  (6)

All mixed derivatives in s and theta of f and u are bounded, by the symbol estimates. Differentiating (6) any finite number of times keeps a factor r^(p-1); the denominator is bounded below for sufficiently large r and all its differentiated reciprocals are bounded. Consequently every mixed derivative of f_s is O(r^(p-1)). Together with the angular estimate in (5), this proves

    |D^j[rho-r^p Theta_0]|<=C_j r^(q-j).                   (7)

For example any mixed derivative with at least one s derivative is controlled by the differentiated (6), while derivatives with no s derivative use (5). Cartesian derivatives are combinations of these divided by powers of r.

Put f_1=rho-r^p Theta_0 on the punctured plane. It is locally integrable at zero, centrally odd, and has a finite compact first absolute moment. Equation (7) and the weighted lemma with b=q show

    |D^j[U-r^p u_0]|<=C_j r^(q-j).                        (8)

Linearity of the canonical inverse justifies the subtraction. The assertion would not follow from boundedness of a singular integral on arbitrary continuous functions; the differentiated estimate (7) is used.

## 5. Determination of Theta_1 and the second remainder

Let F_0=p u_0r Theta_0+u_0theta Theta_0'. By (7)-(8), the numerator of (6) equals F_0+O_Ck(r^(p-1)), including all mixed derivatives. Expand its denominator to get

    f_s=-ell^-1 r^(p-1)F_0+O_Ck(r^(2p-2)).               (9)

Integrating from s to infinity gives

    f=Theta_0+[F_0/(ell(1-p))]r^(p-1)+O_Ck(r^(2p-2)).     (10)

The sign is positive because f(s)=Theta_0-integral_s^infinity f_s. Since ell(1-p)=D, (10) gives precisely (2). Mixed derivatives of the remainder with an s derivative follow by differentiating (9); pure angular derivatives follow by integration. Multiplication by r^p proves the density estimate in (3).

The difference f_2=rho-r^p Theta_0-r^q Theta_1 is locally integrable at zero, since q>-1. It is centrally odd, has finite compact first absolute moment, and has symbol growth b=t=3p-2 in (-2,1). The weighted lemma therefore gives its velocity bound with the same exponent, proving the second line of (3).

Equivalently, the coefficient of degree q in the transport residual is

    (ell q-1)Theta_1+F_0=-D Theta_1+F_0=0.

This checks both the sign and the normalization independently of the integration in (10).

## 6. Scaling, the axis and physical time

The genuine spatial scaling multiplies Theta_0 by lambda^(1-p) and Theta_1 by lambda^(1-q)=lambda^(2(1-p)). Formula (2) has exactly that covariance, since the inverse is linear and its right side is quadratic in Theta_0. Neither ell nor rho_y(0) is changed.

On the positive y-axis Phi_0(pi/2)=0, so u_0theta=0 and

    Theta_1(pi/2)=p u_0r(pi/2)K/D, K=Theta_0(pi/2)!=0.

This is a necessary far-axis correction, not an extra normalization. It may vanish if the corresponding radial velocity coefficient vanishes.

For tau=T-t_phys, alpha=1/D and beta=ell/D, the physical fields on compact annuli away from zero obey

    varrho=alpha[r^p Theta_0+tau r^q Theta_1+O(tau^2)],
    u_phys=alpha[r^p u_0+tau r^q u_1+O(tau^2)],

in every spatial Ck norm. Here r is the physical radius. The exponents use alpha-beta*p=0 and alpha-beta*q=1. The coefficient equation is also the terminal transport identity: -alpha*r^q Theta_1+alpha^2*r^q F_0=0. A spatial and value expansion does not by itself assert all time derivatives of u_phys at the terminal time.

## 7. Scope and dependencies

Dependencies are the canonical kernel and its parity cancellation, the confirmed local spatial regularity theorem, elementary angular Fourier inversion and exact transport. This proves two terms and a controlled remainder. It does not claim an all-order polyhomogeneous expansion: eventual powers encounter the r^-3 compact-source velocity tail, and resonances or logarithms must be treated separately. No arbitrary harmonic strain, exterior boundary condition or chosen angular tail has been introduced. The result imposes necessary compatibility on an exact profile and does not furnish a profile.

## 8. An independent finite-coefficient audit and normalization near angular zeros

For the smooth representation in ../smooth_representation/PROOF.md, with w=(1+r^2/L^2)^(-(1-p)/2), sigma=r^2/(L^2+r^2), t=1-2w and rho=y w sum sigma^k B_k(t) cos(2k theta), Taylor expansion at t=1 gives exactly

    Theta0=L^(1-p) sin(theta) sum B_k(1)cos(2k theta),
    Theta1=-2L^(2(1-p))sin(theta)sum B_k'(1)cos(2k theta).

The density remainder is O_symbol(r^(3p-2)); the corrections to w and sigma first occur at order r^(p-2), which is strictly lower. The inverse lemma applies to the difference from the first two homogeneous terms without assuming transport. Consequently the unforced residual of any finite coefficient array has

    R=r^(2p-1) E(theta)+O_symbol(r^(3p-2)),
    E=p u0r Theta0+u0theta Theta0'-(ell-1)Theta1,

provided ell=1/p. This is an exact asymptotic formula for the finite representation, not a claim that it solves transport. The first term uses the explicit angular inverse already derived above; no optimized velocity is involved. An external source decaying as r^-3 does not change this coefficient since 2p-1>-1.

For an angle where Theta0 is nonzero, both prompt normalization denominators have nonzero terms of order r^p, so the normalized residuals decay like O(r^(p-1)) even when E is nonzero. A small remote normalized residual therefore does not enforce the first correction. The audit records E separately.

At an interior angular zero theta* of Theta0, the cancellation in the prompt's Nv matters. If |Theta1(theta*)|+|F(theta*)|>0, where F=p u0r Theta0+u0theta Theta0', then

    |R|/Nv -> |F-(ell-1)Theta1| / [(1+|2p-1|)|Theta1|+|F|]

along the fixed ray theta=theta*. This follows by retaining the order r^(2p-1) terms in rho, X.grad rho and U.grad rho separately. No conclusion is asserted if the displayed denominator vanishes; higher terms are then required. At a simple interior zero away from both coordinate axes, Nf instead has the nonzero leading coefficient 2ell|cos(theta*)sin(theta*)Theta0'(theta*)| r^p. Thus Nf and Nv can show different far-field behavior. Exact x-axis points still have both denominators zero by symmetry and must be excluded only geometrically, as required by the prompt.

The script independent_code/audit_smooth_far_field.py reconstructs these finite angular coefficients through endpoint sums and an independent trigonometric convolution, and compares them with direct Cartesian singular-integral velocities and eighth-order centered differences at three large radii. Its numerical outputs do not certify a uniform residual bound.

## 9. The leading velocity is nonzero

For every exact primary profile, the angular vector u0 is not identically zero. In particular, with M=max_theta |u0(theta)|, one has M>0 and

    lim_(r->infinity) r^(-p) max_(|X|=r)|U(X)|=M.

To prove this, suppose that the velocity of the homogeneous density rho0=r^p Theta0 is identically zero. The curl identity gives partial_x rho0=0 on the punctured plane. Hence for each y>0, rho0(x,y) is constant in x, and homogeneity gives rho0(x,y)=K y^p, with K=Theta0(pi/2)!=0. Oddness gives rho0(x,y)=K sign(y)|y|^p below the axis. On the circle this requires Theta0(theta)=K sign(sin(theta))|sin(theta)|^p. Since 0<p<1 and K!=0, this function is not differentiable at theta=0. This contradicts the smooth angular trace proved from the exact primary assumptions in result32. Thus M>0. The uniform velocity limit U=r^p u0+O(r^(2p-1)) gives the displayed maximum limit. This establishes the exact supremum growth exponent of U, without claiming nonvanishing on each individual ray.
