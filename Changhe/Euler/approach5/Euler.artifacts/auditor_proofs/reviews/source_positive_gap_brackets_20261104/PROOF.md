# Bounds for optimal constants under a vanishing negative-source moment

## 1. Exact class and constants

Fix 0<beta<1 and L>0. Set t=(beta-3)/2, k=(beta+1)/2, D0=k^2+2 and H=t^2(k^2+4)/D0. Let C(beta,L) consist of all real C^1 divergence-free vector fields U on R^3 satisfying

    E(R)=integral_(|y|<R)|U(y)|^2dy, E(R)/(L R^beta) -> 1,
    liminf N_0(R)/log R = 0,
    N_a(R)=integral_(1<|y-a|<R) |y-a|^(2-beta)[-q(y)]_+dy,
    q=tr((DU)^2).

No Euler equation is imposed. Define extended-real quantities

    M(U)=limsup G_0(R)/(beta L log R),
    G_a(R)=integral_(1<|y-a|<R) |y-a|^(2-beta)|DU(y)|_F^2dy,
    A(U)=limsup_(|y|->infinity) |y|^((5-beta)/2)|DU(y)|_F.

Define the best universal constants by the infima

    zeta_opt=inf_(U in C(beta,L)) [M(U)-H],
    A_opt=inf_(U in C(beta,L)) 4pi A(U)^2/(beta L).

The class is nonempty and contains finite-M, finite-A fields, as shown below. Thus these are finite real infima, not formal infima of an empty class. Put

    C_n=2k t^2 sqrt(k/(k+3))/D0,
    e(zeta)=sqrt(10zeta/beta)(sqrt(H+zeta)+sqrt(H)),

and let zeta_beta be the unique root in (0,beta) of C_n(1-zeta/beta)=e(zeta), confirmed in A3161. Then

    zeta_beta <= zeta_opt <= 2beta k(2-k)/(D0(k+1)),
    H+zeta_beta <= A_opt <= 18t^2/(D0+3t^2).             (1)

In fact A_opt>=H+zeta_opt. These are brackets, not identifications of either infimum. The same assertions hold with the defining negative-moment condition at any fixed center. They also hold if the class is restricted to smooth fields with q>=0, or q>0, outside a compact set. No upper bound for the corresponding infimum over actual Euler profiles follows from these controls.

## 2. Universal lower bounds

A3161 applies to every member of C(beta,L), including M(U)=infinity, and gives M(U)>=H+zeta_beta. If A(U) is finite, for every epsilon>0 and sufficiently large r the pointwise estimate |DU|<=(A(U)+epsilon)r^((beta-5)/2) gives

    G_0(R)<=4pi(A(U)+epsilon)^2 log R+C_epsilon.

Hence M(U)<=4pi A(U)^2/(beta L). If A(U)=infinity that latter inequality holds in the extended-real sense. Taking infima proves both lower bounds in (1) and the stronger relation A_opt>=H+zeta_opt. No existence of a minimizer is needed.

A3162 proves that the extended-real M(U) is unchanged by the center. Ball inclusions give the same energy coefficient L at every fixed center. The above argument can therefore be applied at whichever center occurs in the negative-source hypothesis, with the same amplitude: the ratio |y-a|/|y| tends uniformly to 1 at infinity. This does not translate the Euler equation or assume translation invariance of that equation.

## 3. The two distinct upper-bound controls

A3166 supplies smooth completions of the parallel-axis degree-one tails

    U(rn)=r^t[k a-t(a.n)n+b cross n],
    (8pi/3)(D0|a|^2+|b|^2)=beta L,
    rho=D0|a|^2/(D0|a|^2+|b|^2).

They equal the displayed tail for r>=2, have E_0(R)=L R^beta there, and have q>=0 outside B_2 precisely for

    rho_minus=D0/(D0+3t^2) <= rho <= rho_plus=D0/[2(k+1)].

The source may be negative in the compact core. For any fixed center a0, its weighted negative integral N_a0 is nevertheless bounded, because q is continuous, its negative part has bounded support and the definition excludes |y-a0|<1. Thus every one of these controls belongs to the class used in Section 1 at every fixed center.

Let T denote the homogeneous formula extended to all r>0, separately from the completed U inside B_2. Then DU(rn)=r^(t-1)DT(n) for r>=2. Consequently

    r^(2-beta)|DU(rn)|^2=r^(-3)|DT(n)|^2,
    G_0(R)=beta L M log R+O(1),
    M=(beta L)^(-1) integral_(S^2)|DT(n)|_F^2,
    A(U)^2=max_(n in S^2)|DT(n)|_F^2.

There is no missing radial factor in the middle formula: spherical volume contributes r^2dr. The full spatial limsup defining A equals the maximum of this continuous angular function because every direction persists to arbitrarily large radius. The same amplitude holds at every fixed center by the weight ratio above. For these smooth homogeneous tails, the change of the gradient-square density under fixed translation is O(r^(2t-3)); after the radial weight r^(4-beta), it is O(r^-2), integrable. Thus G_a0-G_0=O_a0(1), proving the full limit M at all centers, although A3162 already suffices for the limsup.

At rho_plus the A3166 exact integrated minimum is

    M=H+2beta k(2-k)/(D0(k+1)).

This gives the upper bound for zeta_opt. At the different endpoint rho_minus the exact peak is

    A(U)^2=(beta L/(4pi))*18t^2/(D0+3t^2),

giving the upper bound for A_opt. These two controls are not a common optimizer. Approaching each endpoint from the open interval gives q>0 throughout the exterior, with the same limiting coefficients, so the brackets also hold for strict exterior positivity. Neither control is an Euler profile: its affine core has residual curl 2[z+omega(e3 cross z)] for a nonzero z, whose scalar product with z is 2|z|^2. This is nonzero for every real c and omega.

## 4. Source version and independent comparison

The complete coordinator Note 239 and C comparison of 10:35:59Z are retained in verification and read. The analytical part of C's item 2 agrees with Sections 2-3: center invariance of the limsup suffices, and homogeneity identifies the amplitude with the spherical maximum. No grid, root sample, numerical ratio or decimal in that comparison is certified or needed. In particular the fact that both intervals in (1) are nonempty follows analytically from applying the universal lower theorem to the explicit controls; it is not a numerical consistency claim.

The LIT387 source now has SHA256 dd15d31d33871f634f872125de08345697c72b4071489937e5acf43c207a56e3. Its complete difference from the reviewed 730957d0 changes only its status sentence, recording A3166-A3168. No hypothesis, formula or proof changes. The original A3166-A3168 scopes therefore persist.

The dependencies are the standalone proofs in the team records and in the team records. The argument establishes only brackets for larger kinematic classes. Full-mode optimal values, existence of their minimizers, the corresponding actual-profile infima and the primary nonexistence conjecture remain open.
