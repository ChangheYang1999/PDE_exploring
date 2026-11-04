# Independent audit of the logarithmically enlarged vector threshold

This is a standalone reconstruction of LIT351, exact submitted source SHA256 93ea82c040e1c955fe6577f729afc8d4f7212f01d0faed3f62ac96c0e0b78964. All seven source sections and forty manual checks were read. The source and complete existing configured model comparison are retained in `verification`.

## 1. Statement and conventions

Fix Rstar>0 and a finite integer N>=1. Let D={z in C:|z|<Rstar/e}, and let u:D->C^N belong to L2_loc(D) and H1_loc(D minus {0}). The norm is Euclidean and dbar=(partial_x+i partial_y)/2 componentwise. Suppose almost everywhere off0 that

    |dbar u(z)| <= [1/4+1/(8 log^2(Rstar/|z|))] |u(z)|/|z|.

Assume infinite L2 integral order at0:

    integral_(|z|<r)|u(z)|^2 = o(r^L) for every real L>0.

Then u=0 almost everywhere on D. No distributional equation across0 or chosen point value at0 is required. A continuous representative is identically zero.

There is also a connected propagation statement. Let O be an open connected planar domain containing0, let u be locally L2 on O and H1 locally off0, and suppose |dbar u|<=b|u| there, with b locally essentially bounded away from0. If the displayed logarithmic bound holds on one such disc contained in O and u is integral-flat at0, then u=0 almost everywhere on O. Neither statement derives a coefficient bound from the Euler equations.

## 2. Cylinder equation and weighted integrability

Set r=Rstar exp(-t), t>1, and U(t,theta)=u(r exp(i theta)). Work in H=L2(S1;C^N) with the self-adjoint operator Dtheta=-i partial_theta on periodic H1. Its entire spectrum is the integers, with all vector components retained. Punctured H1 and change of variables on compact annuli give

    U in H1_loc((1,infinity);H) intersect L2_loc((1,infinity);Dom(Dtheta)).

In particular there is a common locally absolutely continuous H-valued representative. The polar identity for dbar gives, almost everywhere in t,

    U_t+Dtheta U=G,
    G=-2r exp(-i theta)dbar u,
    ||G||_H <= g(t)||U||_H,
    g(t)=1/2+1/(4t^2).

Indeed i partial_theta=-Dtheta, so the sign of both terms on the left is positive after multiplying by -2r exp(-i theta).

For every t0>1 and lambda>0, change of variables gives

    integral_(t0)^infinity exp(2lambda t)||U(t)||_H^2 dt
      =Rstar^(2lambda) integral_(|z|<Rstar exp(-t0))
                                    |z|^(-2lambda-2)|u(z)|^2 dA < infinity.

To justify finiteness, choose L>2lambda+2. Integral flatness bounds the mass on each sufficiently small disc of radius s by s^L. The dyadic annulus with outer radius s contributes at most 2^(2lambda+2)s^(L-2lambda-2). Summing the geometric series proves the assertion; the remaining compact annulus has finite L2 mass. No pointwise circle decay is asserted.

## 3. The two full spectral subspaces

For an integer m>=0 let A=P_(k<=m)U and B=P_(k>=m+1)U, with a=||A||_H and h=||B||_H. These projections are complementary on the whole H; the first includes every negative mode and the second includes the full positive tail. The vectors and their norms are locally absolutely continuous.

At almost every time where a,h>0, the equation and the spectral order give

    a' >= -m a + Re<A,P_low G>/a,
    h' <= -(m+1)h + Re<B,P_high G>/h.

The forms with Dtheta are well-defined at its almost-everywhere domain points: Cauchy-Schwarz bounds sum |k| |U_k|^2 by the product of the H norms of U and Dtheta U. The unbounded negative spectrum causes no reversal of <Dtheta A,A><=m a^2.

On an interval where a>0 set alpha=arctan(h/a). It is locally absolutely continuous. At positive h, multiplying the second inequality by a and the first by -h yields

    alpha' <= -a h/(a^2+h^2) + ||G||_H/sqrt(a^2+h^2)
            <= g(t)-sin(alpha)cos(alpha).

For the forcing estimate, the two orthogonal coefficients of G are -h A/a and a B/h, whose squared norms sum to h^2+a^2. This proves the displayed bound with no dimensional factor. On the set h=0, its nonnegative absolutely continuous norm has h'=0 almost everywhere, so alpha'=0 there. The right side is g>=0. Thus the angle inequality holds almost everywhere on every interval where a>0 without dividing by h at its zeros. The lower bound also gives

    a' >= -m a-g(t)sqrt(a^2+h^2).

## 4. The explicit moving cone

Define beta(t)=pi/4-1/(2t), so0<beta<pi/4 for t>1. Its derivative is 1/(2t^2), and

    g(t)-sin(beta)cos(beta)
      =sin^2(1/(2t))+1/(4t^2)
      <=1/(2t^2)=beta'(t).

The only estimate is |sin x|<=|x|. This checks the exact coefficient 1/8 in physical coordinates, including equality in the majorant.

Let F(t,x)=g(t)-sin x cos x. The identity F_x=-cos(2x) gives its Lipschitz constant1 in x. If alpha(t0)<=beta(t0) and a(t0)>0, then on every later interval where a>0 the positive part w=(alpha-beta)_+ is absolutely continuous and obeys w'<=w almost everywhere. Where w>0 this follows from F's Lipschitz bound and the two differential inequalities. Where w=0 the derivative of the nonnegative absolutely continuous w is0 almost everywhere. Multiplying by exp(-t) and integrating proves w=0. This handles a non-strict initial cone inequality and needs no first strict crossing assertion.

## 5. Positivity persists and forces an exponential lower bound

Inside the cone h/a<=tan beta<1 and g<=3/4. Hence

    a' >= -K_m a,    K_m=m+3sqrt(2)/4,
    a(t)>=a(t0) exp(-K_m(t-t0)).

Initially this holds on the connected interval of positivity of a that starts at t0. If its right endpoint T were finite, continuity and this positive lower bound would give a(T)>0, contradicting maximality. Therefore that interval continues to infinity. On each compact subinterval a is bounded below, justifying the angle calculation already used. The proof has not assumed that U or a cannot vanish at a later time; it has proved the required nonvanishing from the initial cone condition.

## 6. Flatness excludes every possible nonzero circle

If U(t0)!=0 at some t0>1, Parseval on the full H gives a(t0)->||U(t0)||_H>0 and h(t0)->0 as m->infinity. Since beta(t0)>0, one finite m has a(t0)>0 and alpha(t0)<=beta(t0). For this fixed m, Section5 applies forever. Taking lambda>K_m then gives

    integral_(t0)^infinity exp(2lambda t)||U(t)||_H^2 dt
      >=a(t0)^2 exp(2K_m t0)
            integral_(t0)^infinity exp(2(lambda-K_m)t)dt=infinity,

contradicting Section2. Thus the continuous H representative is zero at every t>1. Change of variables implies u=0 almost everywhere in D. Choosing a spectral split for a hypothetical nonzero vector is not a finite Fourier approximation; no mode of the equation is discarded.

## 7. Propagation from known zero points

Let Z be the set of points in O having an almost-everywhere zero neighborhood. It is open and contains0. Take x in its relative closure with x!=0. Choose B(x,2d) compactly contained in O and avoiding0, and choose a nonnegative essential bound K for |b| there. Take 0<rho<d with K rho<=1/4 and a in Z with |a-x|<rho/4. Then B(a,rho) lies in B(x,2d), and on it

    |dbar u|<=K|u|<=|u|/(4|z-a|)
                <=[1/4+1/(8 log^2(e rho/|z-a|))]|u|/|z-a|.

Because a is already in Z, u has infinite integral order there. Also u is H1 on this disc, which avoids the original0. Sections2-6, translated to a with Rstar=e rho, show it vanishes on B(a,rho). This includes a neighborhood of x. Thus Z is relatively closed, and connectedness gives Z=O. No regularity at an unknown boundary zero was assumed.

## 8. Comparison, diagnostic and scope

The entire existing Theory Agent C comparison dated2026-11-04T04:48:47Z was read and checked. Its nine mathematical items agree with the foregoing proof, including the zero set of h, first positivity interval and full spectral limit. Its observation that lambda>=K_m already gives a divergent integral is correct; the proof above uses the simpler strict choice. Its comparison with the earlier variable-width example is contextual and is not a dependency of this proof.

The complete ten-condition script and log were read, not run here. It has six symbolic identities, two numerical grids, one ODE test labelled FIN and one ODE negative control labelled EX, and it exits nonzero if a recorded condition fails. Both ODE tests are numerical evidence only. In particular FIN does not certify every time along the flow. The grid has a small negative rounding value about -1e-16, within its chosen tolerance; the exact sine inequality in Section4 proves the sign. The symbolic Lipschitz test checks the derivative identity, while |cos(2x)|<=1 is the hand justification for its global bound. No computation supplies a missing step of the argument.

This theorem is a sufficient criterion for finite complex vectors under a specific logarithmic majorant. It imports no endpoint continuation theorem. Its dependencies are Sobolev slicing, the circle Fourier basis, Hilbert-valued absolute continuity and elementary inequalities, with Gronwall proved above. It proves neither optimality of1/8 nor continuation for every integrable cylinder excess. A separate submitted LIT352 construction requires its own audit before any sharpness conclusion. There is no new scalar or Euler counterexample, and no bound on the Euler reduced coefficient. The unrestricted conjecture remains OPEN. Existing configured model collaboration uses the working files; actual provider execution is independently unattested. No new model client, mathematical computation or formalization was used.

## 9. Source confirmation revision

The submitted source93ea82c040e1c955fe6577f729afc8d4f7212f01d0faed3f62ac96c0e0b78964 has been compared with the current source50ccb08bf7de3d1b6b68cb08ff8bdc9c755cb532cb8c519ecae66a2ad98b3c4e. The complete difference changes only the opening status and adds a confirmation section. It correctly distinguishes A2942 from A2943, records that the source agent read the full existing comparison but not its diagnostics, and leaves LIT352 separate. No mathematical claim or proof changes. The exact bytes, difference and capture time are retained in verification.
