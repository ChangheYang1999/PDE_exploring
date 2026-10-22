# A transport graph norm does not control a transverse quadratic transport term

Date: 2026-10-20. Status: conditional analytic obstruction accepted by actual Claude Opus 5.5 with minor exposition repairs, now incorporated. Candidate-specific constrained application is separate. This is a statement about a Banach formulation, not nonexistence of an IPM profile.

## Exact statement

Let s>=0 and let V be a real smooth vector field in a neighborhood of a compact coordinate patch in R^2. Assume V(P)!=0 at an interior point P. Outside this patch V may be different, provided the operator below is defined on compactly supported smooth functions in the patch. Let B:H^s(R^2)->H^s(R^2) be bounded and put

L=V dot grad+B.

Let D be any linear subspace of the maximal distributional domain of L in H^s, containing the compactly supported smooth functions in the patch, equipped with a norm satisfying

||h||_D<=C_D(||h||_(H^s)+||Lh||_(H^s))

for those functions. The usual graph norm and its completion have this property. Assume f is a real smooth member of D. Let W be a real linear velocity assignment on D such that w=W[f] is smooth on the patch and w(P) is not parallel to V(P). Assume also that

h -> W[h] dot grad f

extends to a bounded map from H^s to H^s for compactly supported smooth h in the patch. Define on smooth functions the quadratic expression Q(h)=W[h] dot grad h, whenever it belongs to H^s.

Then the symmetrized cross term

C_f(h)=W[f] dot grad h+W[h] dot grad f

is unbounded from D to H^s. If Q is defined in H^s on every smooth f+h and f-h used below, Q has no continuous extension at0 from D to H^s. In particular there is no finite constant C with

||Q(h)||_(H^s)<=C||h||_D^2

on any neighborhood of0 containing these smooth perturbations.

The statement remains true if f is replaced by any fixed nonzero scalar multiple. Thus the obstruction persists arbitrarily close to0.

## Sobolev facts used, with their verification

We use the inhomogeneous Fourier norm

||g||_(H^s)^2=integral_(R^2)(1+|xi|^2)^s |g_hat(xi)|^2 dxi

with unitary Fourier normalization. Two local facts suffice.

First, for a nonzero smooth compactly supported amplitude A(u,v),

lambda^(-s)||A(u,v)exp(i lambda v)||_(H^s) -> ||A||_(L^2)

as lambda->infinity. Indeed multiplication by exp(i lambda v) translates the Fourier transform. The squared normalized norm is

integral [lambda^(-2)(1+xi_u^2+(xi_v+lambda)^2)]^s |A_hat(xi)|^2 dxi.

Its bracket tends pointwise to1 and, for lambda>=1, is bounded by a constant times(1+|xi|^2)^s. Since A is smooth and compactly supported, dominated convergence applies. The same estimates give uniform upper bounds with an arbitrary fixed smooth amplitude. For cosine and sine, the two oppositely translated Fourier packets have vanishing normalized cross term, so the corresponding limit is ||A||_2/sqrt(2). To see the vanishing rigorously, truncate each unshifted transform to |xi|<=R. Its normalized translated H^s tail is bounded uniformly for lambda>=1 by C times the H^s Fourier tail of A, using lambda^(-2s)(1+|xi +/- lambda e_v|^2)^s<=C_s(1+|xi|^2)^s. The two truncated translates have disjoint support when lambda>R, so their weighted inner product is zero. Cauchy-Schwarz bounds the remaining cross terms uniformly by a constant times this tail, which tends to zero as R tends to infinity. Taking lambda to infinity first proves the claim.

Second, on compactly contained supports, pullback by a smooth coordinate diffeomorphism and its inverse gives equivalent H^s norms. Here is a direct reduction for noninteger s. For0<sigma<1, the Fourier H^sigma norm is equivalent to

||g||_2^2+integral integral |g(x)-g(y)|^2/|x-y|^(2+2sigma) dx dy.

The Fourier identity follows by setting z=y-x and integrating |exp(i xi dot z)-1|^2/|z|^(2+2sigma); scaling and rotation give a finite positive constant times |xi|^(2sigma). A bi-Lipschitz change of coordinates on a slightly larger compact patch, with bounded positive Jacobian, bounds the double integral in both directions. Pairs with one point outside that larger patch contribute a bounded multiple of ||g||_2^2 because the support is separated from its boundary. Multiplication by a smooth coefficient is bounded: split the difference of ag into a(x)[g(x)-g(y)]+[a(x)-a(y)]g(y), and use the Lipschitz bound for small distances and boundedness for large distances. For s=m+sigma, use the equivalent norm summing the H^sigma norms of derivatives through order m and the ordinary chain rule. Every chain-rule term involving a derivative of order m_prime<=m is controlled by the same multiplier estimate and ||g||_(H^(m_prime+sigma))<=||g||_(H^s); the reverse coordinate map supplies the converse bound. Integer s follows directly from the chain rule and Jacobian bounds. This proves the coordinate equivalence needed below without assuming a global coordinate chart.

## Construction of the bounded graph sequence

The local flow-box construction gives smooth coordinates(u,v) on a sufficiently small patch, with V dot grad=partial_u. One can obtain them by flowing a small transverse curve through P: the derivative of the resulting map at P has independent flow and transverse columns, so the inverse function theorem gives a local diffeomorphism. Shrink the patch so the hypotheses above and all coordinate bounds hold.

In these coordinates write w dot grad=alpha(u,v)partial_u+beta(u,v)partial_v. Nonparallelism at P is exactly beta(P)!=0. Choose a real smooth compactly supported amplitude A, supported where beta does not vanish, with A not identically zero. For lambda>=1 put

h_lambda=lambda^(-s)A(u,v)cos(lambda v),

pulled back to the physical patch and extended by0. It is a smooth compactly supported physical function. The modulation estimate and coordinate equivalence imply

||h_lambda||_(H^s)<=C_0.

Since V dot grad=partial_u and v is a first integral of V,

V dot grad h_lambda=lambda^(-s)(partial_u A)cos(lambda v),

so its H^s norm is bounded independently of lambda. The boundedness of B implies ||Lh_lambda||_(H^s)<=C_1. Therefore ||h_lambda||_D<=C_2.

## The transverse derivative is unbounded

Direct differentiation gives

w dot grad h_lambda
 =-lambda^(1-s)beta A sin(lambda v)
  +lambda^(-s)(alpha partial_u A+beta partial_v A)cos(lambda v).

The first amplitude beta A is nonzero. The lower modulation estimate and the inverse coordinate bound imply that the H^s norm of its first term is at least c lambda for all sufficiently large lambda, with c>0. The second term has H^s norm bounded independently of lambda. Thus

||W[f] dot grad h_lambda||_(H^s)>=c lambda-C_3.

By hypothesis, ||W[h_lambda] dot grad f||_(H^s)<=C_4||h_lambda||_(H^s)<=C_5. The reverse triangle inequality now gives

||C_f(h_lambda)||_(H^s)>=c lambda-C_6.

This proves unboundedness on a bounded D sequence. The argument does not replace a nonlocal velocity by a compact term: its bounded action in the second cross term is an explicit assumption, while its fixed transverse velocity drives the unbounded first term.

## Failure of a continuous quadratic extension

Linearity of W gives the exact polarization identity

Q(f+h)-Q(f-h)=2C_f(h).

Suppose Q had a continuous extension at0 from D to H^s, agreeing with this expression on smooth inputs. Then Q(0)=0, so some D ball of radius delta>0 would satisfy ||Q(g)||_(H^s)<=1. Choose a fixed a>0 so that a(||f||_D+C_2)<delta. Both a(f+h_lambda) and a(f-h_lambda) lie in that ball, and homogeneity gives

Q(a(f+h_lambda))-Q(a(f-h_lambda))=2a^2 C_f(h_lambda).

The left side has norm at most2, whereas the right side is unbounded. This contradiction proves the claim. The same argument immediately rules out a uniform quadratic bound. If Q fails to belong to H^s for one of these smooth inputs, the proposed mapping into H^s already fails before continuity is considered.

## Relation to IPM and scope

For the fixed-scaling IPM linearization, B includes h -> U[h] dot grad rho_bar-h. The canonical full-plane velocity is an order-zero Fourier multiplier; multiplication by a sufficiently smooth bounded background gradient is bounded on H^s. For a compactly supported smooth f, h -> U[h] dot grad f has the same boundedness. An eliminated scaling term adds c[h]X; the cross term c[h]X dot grad f is bounded whenever c is a bounded functional in the chosen norm. For the full linear scaling contribution c[h]X dot grad rho_bar, boundedness additionally requires X dot grad rho_bar to belong to the target H^s, or another separately proved mapping estimate. The compact-f cross term does not establish this background condition. The present theorem assumes the stated boundedness instead of invoking it in a weighted or finite-regularity space.

To apply this obstruction to a particular IPM formulation, one must exhibit an admissible f with W[f](P) not parallel to V(P), verify the background and velocity hypotheses on the patch, and check that the proposed D norm has only the stated graph control on the oscillating sequence. Symmetry may require combining reflected disjoint patches. A center normalization does not automatically remove a perturbation supported away from the center, but a scaling or canonical constraint must still be checked. No such candidate-specific application is asserted here yet.

Stronger norms controlling transverse derivatives, formulations with derivative loss, estimates on a scale of spaces, or nonlinear changes of coordinates are outside this obstruction. A bounded linear inverse in a graph norm is therefore insufficient by itself for a quadratic closing inequality into that same H^s target under these hypotheses. A weaker target, a stronger domain or a scale of spaces is not ruled out. Transfer to a weighted space requires local norm equivalence and all the boundedness and domain hypotheses to be verified separately. This theorem neither proves a global inverse impossible nor excludes an exact IPM profile.
