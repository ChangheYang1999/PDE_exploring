# Scalar inverse-radius continuation and its carrier consequence

Status: scalar continuation and local carrier consequence CONFIRMED A2506, after the complete five-item coordinator comparison. This is the B=0 special case of A2501-A2504. No global Euler nonexistence is asserted.

## 1. Exact statements

Let D_R={z in C:|z|<R}, let C>=0 be finite, and suppose f:D_R->C is smooth and flat at zero, meaning every derivative at zero, including the value, vanishes. Assume

    |partial_zbar f(z)| <= C |f(z)|/|z| almost everywhere,
    partial_zbar=(partial_1+i partial_2)/2.                    (1)

Then f vanishes on a neighbourhood of zero. It consequently vanishes on all of D_R by local continuation away from zero, although the carrier application needs only the neighbourhood conclusion. No smallness of C is required.

Fix 0<c<1/2 and omega real, and define Jx=e3 cross x, A=cI-omega J, X=Ax and L=(1-c)I+omega J. Suppose V is smooth on an open U in R3 avoiding zero and

    div V=0, X.V=0, DV X=-LV, W=curl V.                       (C)

Let sigma:D_R->U be a smooth transverse section through x1=sigma(0), with det(sigma_1,sigma_2,X(sigma)) nonzero. If V is flat at x1 and

    |(W.X)(sigma(y))| <= C |V(sigma(y))|/|y|

almost everywhere on the punctured disc, then V vanishes on a neighbourhood of x1. The constant can be arbitrarily large. A bounded additive term in the coefficient is absorbed by increasing C on a bounded disc.

Finally, in the complete common-flat setting (F) specified in Section 4, each of the three ratios listed there has

    ess sup_(0<|y|<r) |y| B(y)=infinity                       (2)

on every transverse section disc about Gamma and every admissible r>0. This excludes an inverse-radius upper bound, not merely L2 integrability. It supplies no particular quantitative lower asymptotic rate.

The analytic argument uses the Cauchy fundamental solution, elementary integral bounds, local Sobolev calculus for bounded potentials, and elementary holomorphy. The carrier reduction is the exact quotient system A2463. This is a scalar assertion; no vector-valued extension is claimed.

## 2. A logarithmically bounded Cauchy factor

Define alpha=(partial_zbar f)/f where f!=0 and alpha=0 elsewhere. The inequality gives |alpha(z)|<=C/|z| and partial_zbar f=alpha f almost everywhere. Extend alpha by zero outside D_R and put

    s(z)=(1/pi) integral_(D_R) alpha(zeta)/(z-zeta) dA(zeta).

For every z!=0 this integral converges absolutely. For 0<r=|z|<R/2, split it into |zeta|<2r and 2r<=|zeta|<R. On the first part rescale zeta=r eta and write e=z/r. Its absolute value before the factor C/pi is bounded by

    integral_(|eta|<2) 1/(|eta||e-eta|) dA(eta) <=20 pi.

To verify this uniform bound, on |eta|<1/2 use |e-eta|>=1/2, on |eta-e|<1/2 use |eta|>=1/2, and on the remainder bound both denominators below by 1/2. The two small discs contribute at most 2 pi each and the remainder at most 16 pi. On the outer part |z-zeta|>=|zeta|/2, giving an upper bound 4 pi log(R/(2r)) before multiplication by C/pi. Thus

    |s(z)| <=20C+4C log(R/r), 0<|z|<R/2.                     (3)

This rough constant is sufficient. There is no assertion that s is bounded at zero.

The fundamental-solution identity gives partial_zbar s=alpha in distributions. On every annulus compactly contained in D_R minus {0}, s is locally W1p for every finite 1<p<infinity and has a continuous bounded representative on smaller annuli. Here is a direct localization justification. Split alpha into a part supported near the observation annulus, which is bounded and compactly supported, and a part supported a positive distance away. The Cauchy transform of the latter is holomorphic there by dominated differentiation: alpha is globally L1, and the kernel and its derivatives are bounded on the separated supports. For the first part the standard Cauchy-transform derivative is an Lp singular integral, or one can take any fixed p>2 and use its usual local regularity. Only this away-from-zero bounded-coefficient input is used. The classical Cauchy-transform Lp property is the same one used in the already checked p>2 similarity principle A2464 and A2467.

Consequently F=exp(-s)f is W1p on each compact annulus and satisfies partial_zbar F=0 there by the ordinary bounded Sobolev chain and product rules. It has a holomorphic representative on the punctured disc. Bound (3), with the pointwise continuous representative away from zero, gives

    |F(z)|<=exp(20C)(R/|z|)^(4C)|f(z)|, 0<|z|<R/2.           (4)

## 3. Removal of the puncture and continuation

Flatness of f gives |f(z)|<=C_N |z|^N for every positive integer N near zero. Equation (4) therefore gives |F(z)|<=C'_N |z|^(N-4C). Choose N>4C to see that F tends to zero and is bounded near the puncture. The removable-singularity theorem extends it holomorphically with F(0)=0. Since N was arbitrary, the extension vanishes to every finite order. A nonzero holomorphic function has a finite first nonzero Taylor coefficient, so the extension is identically zero near zero. As exp(-s) is nowhere zero on the punctured disc, f is zero there and at zero.

In fact F is holomorphic on the connected punctured disc D_R minus {0}, and it has just been shown to vanish on a nonempty open subset. The identity theorem gives F=0 on the entire punctured disc; hence f=0 on D_R. This avoids any additional boundary continuation theorem.

For the carrier, recall the exact quotient equations. On a smaller relatively compact section let

    m=|X(sigma)|, beta_i=X(sigma).sigma_i/m^2,
    g_ij=sigma_i.sigma_j-m^2 beta_i beta_j,
    j=|det(sigma_1,sigma_2,X(sigma))|=m sqrt(det g).

Writing V(sigma)=sigma_i v_i-(beta.v)X(sigma) and theta=sigma^*(V.dx)=u_i dy_i, one has u=gv and

    div(jv)=(3c-1)j beta.v,
    d theta=[epsilon j(W.X)/m^2+q2(v)]dy1 wedge dy2,

where epsilon is the orientation sign and q2 is a smooth linear expression in v. In smooth isothermal coordinates z centred at zero, theta=alpha1 dz1+alpha2 dz2 and f=alpha1-i alpha2 satisfy

    |partial_zbar f| <= (C1+C2 B0(y(z)))|f|.

This is the already derived div-curl reduction A2463-A2464. The two smooth coordinate changes are locally bi-Lipschitz, so |y(z)|>=k|z| for some k>0 after shrinking. The assumed B0(y)<=C/|y| therefore gives (1), with an enlarged finite constant. Flatness transfers to f. The scalar result makes f, theta and V zero on a smaller section. The exact transport

    V(exp(tA)x)=exp(-tL)V(x)

and a finite local flowbox extend the zero set to a neighbourhood of x1. No infinite-time flow completeness, boundary term, pressure normalization or integrability at infinity is used.

## 4. Full common-flat consequence, attribution and limits

Here (F) means the complete setting used in C66-C68: G is an X-flowbox avoiding zero, Gamma its central orbit segment, and V,S are smooth on G, satisfy (C) and

    X.grad S=-bS, W.grad S=0, b=2(1-c),
    P=S+|V|^2/2, -Delta P=tr((DV)^2),
    S=0 on Gamma, S<0 on G minus Gamma,

with V and S flat at one point of Gamma. Put H=-S, eta=(1-2c)/b and n=(V cross X)/(|V||X|) where defined. The confirmed C66 conclusions say that V is flat precisely on Gamma, V and W have the same zeros, and off-Gamma zeros form locally isolated X-orbit segments. Thus V cannot vanish on a nonempty open subset of G. They also give, off the zero set,

    |W.X|/|V|=eta |X| |n.grad log H|.

On any section through Gamma define

    B1=|W.X|/|V|, B2=|W|/|V|, B3=eta |X||n.grad log H|,

with zero values assigned at the exceptional points. The section intersections with Gamma and with off-Gamma zero orbits are countable, hence null, as proved explicitly in the endpoint audit Section 6. If ess sup |y|B1 were finite on a disc, the carrier assertion would force V to vanish on an open set, a contradiction. If the same held for B2, shrink to a disc on which |X(sigma)| is bounded and use B1<=|X|B2. Since B3=B1 almost everywhere, (2) follows for all three ratios. None of these conclusions supplies an upper bound of any kind from (F).

The actual Pan-Zhang manuscript, New York Journal of Mathematics 29 (2023), 402-416, was obtained and read in the adjacent endpoint review. Its Theorem 4.3 contains a scalar C/|z| continuation result, whose one-variable proof cites Pan1992 Lemma7. That earlier primary lemma has not been obtained here. Sections 2-3 instead supply a separate scalar proof sufficient for the stated smooth-flat case. This is not a novelty claim or a certification that Pan1992 was read. The primary journal PDF and its hash are retained in the endpoint review's verification directory.

The result is compatible with a ratio growing like log log(1/r)/r, such as the proposed carrier construction in the sharpness review. It does not contradict failure of all L2 bounds in the complete common-flat setting. It excludes no full-(F) solution without an additional inverse-radius upper estimate, and it settles neither the common-flat obstruction nor the unrestricted decaying rotating Euler conjecture.

All four independent sections and the complete five-item coordinator comparison were read. The comparison is pinned in verification; its generic phrase every p<infinity is used only in the valid range 1<p<infinity. No unverified numerical or model output is an argument input.
