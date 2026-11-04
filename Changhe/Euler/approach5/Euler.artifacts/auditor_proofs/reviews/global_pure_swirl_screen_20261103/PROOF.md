# Full-sphere pure swirl: integer exponents and exactly two coefficient crossings

## 1. Exact scope

Let 0<c<1/2, omega be any finite real number, p=(1-c)/c>1, d=p-1, q=2p/d>2, lambda=2p(2p-1), kappa=2p(2p+1), Jx=(-x2,x1,0), A=cI-omega J. On a full spherical annulus r_-<|x|<r_+, with r_-<1<r_+, assume

    V(rn)=r^(-p)a(z)Jn, z=n3, a smooth on [-1,1],
    P2 smooth, P2(exp(tA)x)=exp(-2(1-c)t)P2(x),
    -Delta P2=tr((DV)²), W.grad S=0,
    W=curl V, S=P2-|V|²/2.

Smoothness of a means extendibility to an open interval about [-1,1]. No global original profile, momentum or rank equation is assumed. The annulus includes both full polar neighborhoods and excludes the origin. If V is nonzero, then a has one strict sign on the closed interval and q is an integer. Therefore c=(q-2)/(2(q-1)); the necessary integer screen in the target interval gives q>=7. The earlier canonical axis-pressure theorem A569 already excludes all of those target-range cases, as Section10 explains.

After changing the sign of V, set w=1-z², F=wa>0 on (-1,1), g=F²/w. The averaged reduced scalar has the form h=-K F^q for one K>0. Define B=Kq wF^(q-2). Besides the source's necessary mean and crossing identities, we prove that B crosses 1 at exactly two interior points and obeys the stronger height bound in Section9. These are necessary conditions on the broader 0<c<1/2 auxiliary class. They identify no new open candidate in the campaign interval.

## 2. Averaging and exact angular equations

Axial averaging preserves the pressure source because V is axisymmetric, and preserves W.grad S=0 by rotational pullback. A change of averaging angle converts twisted homogeneity to ordinary homogeneity. Write the averages as Pbar=r^(-2p)u(z), Sbar=r^(-2p)h(z), with u=g/2+h.

The exact spherical formulas are

    W=r^(-p-1)[-F' e_r+d F/sqrt(w) e_theta],
    2pF'h-dFh'=0,
    tr((r^(p+1)DV)²)=2pg+zg'.

For the last identity, write f=F/sqrt(w). The two off-diagonal derivative pairs contribute 2pf²+2zf f'=2pg+zg'. The pressure equation is

    (wu')'+lambda u=-2pg-zg',
    (wu'+zg)'=-lambda u-(2p-1)g.                 (1)

All primes here and below denote z derivatives. These equations retain every rotation rate because only the scalar pressure was averaged.

## 3. Endpoint uniqueness gives one scalar constant

On any connected nonzero-F interval, transport gives h=C_I|F|^q. At a hypothetical interior endpoint z0, F=0, g=g'=0 and, since q>2, h=h'=0. Thus u=u'=0 there. On this particular interval near z0, |h|/g=|C_I|w|F|^(q-2) tends to zero, so u>=g/4>=0.

Integrate the second equation in (1) from z0. Since w is bounded below and |zg|<=g<=4u, in the inward coordinate t one obtains

    |u_t|<=C[u(t)+integral_0^t u].

For Y=u+integral_0^t u, Y>=0, Y(0)=0 and Y'<=C1Y. Hence Y=0, contradicting nonzero F. Reversing orientation covers a right endpoint. No component has an interior endpoint, so a nonzero F has one sign everywhere in (-1,1), and h=C|F|^q for a single finite C. Changing the sign of V makes F positive and preserves all assumptions.

## 4. The sphere balance fixes C<0

Since F=wa and g=wa² with a smooth, g vanishes at both poles; u is smooth and wu' vanishes there as well. Integrating (1) gives

    integral u=-(1/(2p)) integral g,
    integral h=-(p+1)/(2p) integral g.

Thus C=-K<0 and

    K integral F^q=(p+1)/(2p) integral g.         (2)

The endpoint fluxes have been checked explicitly. This step requires the full sphere and is not available on a single cap.

## 5. Polar vorticity cannot vanish

Near either pole, |h|/g=K wF^(q-2) tends to zero, so Sbar>=-|V|²/8 in a sufficiently small full Euclidean ball. At either unit pole, V=0 and DV=a(pole)J, hence W=2a(pole)e3. In particular a(pole)=0 would give V=DV=0.

For completeness, let v,pi be a smooth divergence-free pressure pair in a ball with -Delta pi=partial_i partial_j(v_i v_j), v(0)=Dv(0)=0 and pi-pi(0)>=3|v|²/8. Let E and A0 be the spherical means of |v|² and (v.nu)², and Y=mean(pi-pi(0))+A0. Spherical integration yields Y'=(E-3A0)/r, Y(0)=0. Since E,A0=O(r^4), Y=O(r^4). Also Y>=3E/8+A0>=0, so Y'<=8Y/(3r). The nonnegative function r^(-8/3)Y is nonincreasing from its zero limit, hence vanishes. Therefore v=0 near the center.

Apply this to V,Pbar if a vanishes at a pole. The resulting open zero contradicts F>0 throughout the punctured sphere. Thus a(1),a(-1) are both positive, establishing the nonzero polar-vorticity assertion without assuming it.

## 6. Smoothness forces integer q

Near z=1, set y=1-z. Then F=yL(y) with L smooth and L(0)=2a(1)>0, so h=-K y^q L(y)^q. In local horizontal coordinates on the sphere, y is comparable to the squared distance from the pole. Thus h has magnitude comparable to distance^(2q) and is not infinitely flat.

Its lowest nonzero Taylor polynomial must be rotation invariant. A homogeneous polynomial on the plane that is constant on every circle is a multiple of (x1²+x2²)^m for an integer m. Hence the first order is even and equals 2q, forcing q to be an integer. Solving q=2p/(p-1), p=(1-c)/c gives c=(q-2)/(2(q-1)). The strict target lower endpoint c>2/5 is exactly q>6.

## 7. Highest-derivative coefficient and mean crossing constraint

Substitute u=g/2-KF^q into (1), using (wg')'+2zg'=wg''. This gives

    wg''+kappa g-2K[(w(F^q)')'+lambda F^q]=0.

Expanding g=F²/w and dividing by two yields

    F(1-B)F''+[1-(q-1)B](F')²
      +(4z/w+2KqzF^(q-2))FF'
      +[(kappa+2)/(2w)+4z²/w²-Klambda F^(q-2)]F²=0.    (3)

Thus F(1-B) is exactly the coefficient of F''. Since Bg=KqF^q, (2) gives

    integral Bg/integral g=(p+1)/(p-1)>1.       (4)

B is continuous, positive inside and zero at both poles. Its maximum is strictly greater than the average in (4): equality would force constant B on every interior point with g>0, contradicting the endpoint limits. There are at least two crossings of B=1.

## 8. Exact slope at every crossing

At B=1, the highest-derivative term in (3) is zero. With eta0=wF'/F, the remaining identity is

    -(2/d)eta0²+6z eta0+4pw+4z²=0.             (5)

The roots are

    eta0=(d/2)[3z +/- sqrt(z²+8p/d)].

This is equivalent to the source's radical because pw+z²=p-dz². They have opposite signs: z²+8p/d>9z², since p/d>1 and |z|<1. Further,

    wB'=z +/- sqrt(z²+8p/d)                   (6)

at B=1. Thus every crossing is transverse, with the plus sign for an increasing crossing and the minus sign for a decreasing crossing. At an increasing crossing F'>0; at a decreasing crossing F'<0. In particular a stationary F point cannot occur at B=1.

The B=1 set is finite. It lies in a compact subinterval because B tends to zero at the endpoints. An infinite set would have an accumulation point where B=1 and B'=0, contradicting (6). Its crossings alternate upward and downward.

## 9. Stronger consequence: exactly two crossings and a larger height bound

At a stationary point of F with B<1, equation (3) reduces to

    F(1-B)F''+C(z,B)F²=0,
    C(z,B)=[(kappa+2)/2-(lambda/q)B]/w+4z²/w².

Since (kappa+2)/2-lambda/q=4p, one has C(z,B)>0 for B<1. Therefore F''<0 at every such stationary point. In particular no local minimum of F can lie in the subcritical set {B<1}.

Suppose B had more than two crossings. Between a downward crossing and the next upward crossing, B<1. By Section8, F' is negative at the left endpoint and positive at the right endpoint. The positive smooth function F must have an interior minimum on that compact interval. This is impossible by the preceding paragraph. Hence B has exactly two crossings z_-<z_+, and {B>1}=(z_-,z_+). Also F is strictly increasing before z_- and strictly decreasing after z_+: F' has the stated signs at the poles and crossings, while any zero of F' in these subcritical intervals is a strict change from positive to negative and cannot be followed by the necessary reverse change.

Inside (z_-,z_+), F' starts positive and ends negative, so F has an interior maximum z_m with F''(z_m)<=0. Since 1-B<0 there, the first term in (3) is nonnegative at that point, forcing C(z_m,B(z_m))<=0. Therefore

    B(z_m)>=[2p²+p+1+4z_m²/(1-z_m²)]/[(2p-1)(p-1)],
    max B>=(2p²+p+1)/[(2p-1)(p-1)]
          =(p+1)/(p-1)+2/[(2p-1)(p-1)].       (7)

This is strictly stronger than the source's mean lower bound. It does not bound K independently of amplitude, and it supplies no contradiction. It is an additional exact necessary condition in the broader auxiliary range; no target-range candidate survives the earlier pressure theorem.

## 10. The earlier axis-pressure theorem already excludes the whole target range

A fresh source note points to LIT150 and A569. Their full seven-section source and independent proof were reread. Their scope includes the present annular necessary system after averaging. Extend the averaged fields by their ordinary radial homogeneity from the annulus to R3 minus {0}. This is an exact extension because the equations are homogeneous and their angular coefficients already satisfy them on the annulus. It introduces a singular origin, but the canonical-pressure argument below explicitly allows that singularity.

In the target interval, 1<p<3/2. The stress |V|²<=Cr^(-2p) is locally integrable at zero. Define the canonical distribution Pcan=partial_i partial_j Gamma*(V_iV_j), Gamma=1/(4pi|x|). Its test-function pairing converges at zero by integral_0^1 r^(2-2p)dr and at infinity by integral_1^infinity r^(-1-2p)dr. It is homogeneous of degree -2p and C1 off zero. The distributional Hessian gives

    Pcan(X)=-|V(X)|²/3+(1/(4pi)) PV integral
       [3((X-y).V(y))²/|X-y|^5-|V(y)|²/|X-y|^3]dy.

At a nonzero point X on the axis, V(X)=0 and (X-y).V(y)=0 by pure azimuthal geometry. Therefore

    Pcan(X)=-(1/(4pi)) integral |V(y)|²/|X-y|³dy<0

for every nonzero field. The integral is absolutely convergent: near X, C1 regularity gives |V(y)|=O(|y-X|); near zero use 2p<3; at infinity use p>0. Neither a contact term nor an omitted core flux changes this sign.

The difference Pbar-Pcan is harmonic off zero and homogeneous of degree -2p. Its Kelvin transform is harmonic off zero and homogeneous of degree 2p-1 in (1,2). Extending it by zero makes it distributionally harmonic, since its shrinking-sphere derivative and function fluxes are O(epsilon^(2p)) and O(epsilon^(2p+1)). It is then smooth at zero, with value and gradient zero. Taylor order two and homogeneity of degree strictly below two force it to vanish. Hence Pbar=Pcan.

On the other hand, Sections3-4 give Pbar=r^(-2p)(g/2-KF^q), which vanishes at every nonzero axial point. This contradicts the strict canonical sign. Thus V=0 throughout the strict target range. No rank or full momentum premise is needed for this pure-swirl conclusion.

The initial audit's statement that the target integers q>=7 remain open overlooked this already confirmed dependency. That wording is withdrawn. The initial proof is preserved under verification, and the correction is recorded separately in the chronological ledger. The crossing algebra stays valid, but supplies no new target-range existence problem or nonexistence theorem.

## 11. Corrected verdict and broader scope

All nine original source sections, the updated scope note, both seven-section A569 sources and all eleven current independent sections were read. LIT231's angular, endpoint, integer and crossing identities are confirmed; Section9 strengthens its crossing count. A569 already excludes its entire strict target range. The auxiliary integers q=3,4,5,6, corresponding to 0<c<=2/5 within the present q>2 screen, are not settled by the arguments audited here. No new claim of existence or of their status elsewhere in the literature is made.

Neither a general axisymmetric reduction nor an arbitrary-helicity conclusion follows from this ansatz. No computation or formal build was used. Comparison through the existing configured model agents is requested; actual provider runtime remains unattested.
