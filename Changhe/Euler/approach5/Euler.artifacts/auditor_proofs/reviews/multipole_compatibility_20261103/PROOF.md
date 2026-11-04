# Compatibility, uniqueness and vanishing of low pressure multipoles

Status: CONFIRMED at the exact scopes in A610, A611, A612, A613. Complete independent proof postread, including the corrected zero-g sign. The unrestricted campaign conjecture remains open.

## 1. Full hypotheses, exact moments and statements

Fix2/5<c<1/2 and any finite omega. Let U in C2(R3;R3), P in C1(R3) solve

    div U=0,
    [(1-c)I+omega J]U+DU(Ay+U)+grad P=0,
    A=cI-omega J, J(y1,y2,y3)=(-y2,y1,0).

Assume U tends uniformly to0, DU=O((1+r)^(1/2)), and U.curl U=0 everywhere. Equivalently for this proof, replace the first two asymptotic assumptions by the explicit natural estimates

    |U|<=C(1+r)^-p, |DU|<=C(1+r)^(-p-1),
    p=(1-c)/c in(1,3/2).

The implication from the displayed half-power condition to these natural estimates is the previously confirmed A498,A476,A492 and tail construction, not a consequence of velocity decay alone. Put a=1-2c, b0=2(1-c), Q_t=exp(omega tJ), T_t=exp(tA), B=Ay+U, Omega=curl U,

    H=P+|U|^2/2+(Ay).U, g=U.B.

Let Pinf be the actual pressure constant and V,P2 the actual canonical tails, W=curl V, k=(Ax).V, E=grad k and S=P2-|V|^2/2 on D=R3 minus{0}. Their regularities include V locally C1,alpha for every0<alpha<1 and P2 locally C2,alpha. Define

    K={n>=0:(n+5)c<3},
    r_n=(n+5)c-2,
    Mom_n=integral_R3 y^(tensor n) tensor
                     [U(y) tensor U(y)-V(y) tensor V(y)]dy,
    N(x)=-1/(4pi|x|),
    Theta_n=-((-1)^n/n!)D^(n+2)N:Mom_n.

The integrand is the difference as written, not two separately integrable terms. A550 proves absolute convergence, harmonicity and degree-(n+3) of Theta_n. Here K={0,1} if c>=3/7 and K={0,1,2} otherwise. Every r_n is strictly between0 and1. Write l=n+2, so l is2,3 or4, and the Kelvin numerator is a homogeneous harmonic polynomial h_n of degree l:

    Theta_n=r^(-2l-1)h_n.

Conclusions:

1. For every phase s and n in K, W.grad(Theta_n composed with Q_s^T)=0 on D, and E cross that gradient is0 wherever W!=0.
2. If omega!=0, at most one pair(n,|m|) in the finite rotational Fourier decomposition of all these multipoles can be nonzero. For each nonzero mode its squared modulus sigma satisfies k,sigma!=0 on {W!=0}; there k and S are constant multiples, on each component, of powers of sigma.
3. If omega=0, at most one Theta_n is nonzero. Each nonzero Theta_n has no zeros on {W!=0}, and the same componentwise formulas use |Theta_n|. No prescribed nodal geometry is needed.
4. Every vortical carrier equilibrium z, meaning B(z)=0 and Omega(z)!=0, has its distinguished eigenvalue rho in

       {-a,-2(1-c)} union (-infinity,-(3-2c)].

   If any low multipole is nonzero, every such equilibrium has rho=-a. In particular a selected vortical witness with rho<=-2a cannot exist in this case. Whenever such a witness does exist, rho=-2(1-c) or rho<=-(3-2c), and all low multipoles vanish.
5. If original vorticity is dense in one exterior, or equivalently actual tail vorticity is dense on D, ALL low multipoles vanish. Exterior real analyticity of U is a sufficient alternative. This assertion has no A2 assumption on the actual S.

The last two assertions are necessary constraints. The all-zero-multipole case remains open here. The equilibrium and selected-witness inputs are A496,A534,A551 and A571; their definitions and exact implications are recalled in Section7.

## 2. Rates and separation of the exact scaled identities

Set

    u_t=exp((1-c)t)Q_t U(T_t x),
    p_t=exp(b0 t)[P(T_t x)-Pinf],
    w_t=curl u_t=exp(t)Q_t Omega(T_t x),
    S_t=p_t-|u_t|^2/2,
    H_t=exp(at)[H(T_t x)-Pinf].

On every compact subset of D, A550 gives, for every gamma<1,

    S_t=S+sum_(n in K)exp(-r_n t)Theta_n(Q_t^T x)
                   +O_C1(exp(-gamma t)),
    w_t=W+O(exp(-gamma t)),
    grad H_t=E+O(exp(-gamma t)).

The derivative rate is substantive. It follows from the exact integral

    u_t-V=integral_t^infinity exp(-s)n_s ds,
    n_s=Du_s u_s+grad p_s,

and uniformly local C^alpha bounds for n_s, for every alpha<1. Mollifying at scale epsilon bounds the derivative error by C[epsilon^alpha+exp(-t)epsilon^(alpha-1)]. Taking epsilon=exp(-t) gives O(exp(-alpha t)). Thus naive interpolation, which would lose the needed exponent, is not being used. The exact expression for H_t is

    H_t=(Ax).u_t+exp(-t)(p_t+|u_t|^2/2).

Its gradient has the stated rate by the same estimates. The pressure expansion and these estimates have been reread in A550, including the absolute-moment and singular-kernel bounds.

Global zero helicity gives Omega.H=Omega.g=0. Therefore w_t.grad S_t=0 exactly. The full rank identity A413 gives grad H_t cross grad S_t=0 wherever w_t!=0. Fix x and choose max r_n<gamma<1. Replacing w_t and grad H_t by their limits in these equations gives the constant limiting identities W.grad S=0 and E cross grad S=0 on the respective domains, followed by

    sum_n exp(-r_n t)W.grad(Theta_n composed with Q_t^T)=O(exp(-gamma t))

and the analogous cross-product equation when W(x)!=0. Indeed then w_t(x)!=0 for every sufficiently large t.

The coefficients are constant in t if omega=0, and periodic with period T=2pi/|omega| otherwise. For the smallest remaining rate, multiply by exp(r_n t), set t=s+jT, and let j tend to infinity. Every later rate and the remainder vanish. This forces its coefficient to vanish at every phase s. Iterate finitely many times. In the constant case just let t tend to infinity. This proves conclusion1, with no assumption about the unknown phase at a limiting subsequence.

## 3. Mode geometry and the scalar theorem

When omega!=0, define

    Phi_nm(x)=T^-1 integral_0^T exp(im omega s)Theta_n(Q_s^T x)ds,
    sigma_nm=|Phi_nm|^2.

The polynomial h_n makes this a finite Fourier expansion: |m|<=l, and Phi_n,-m is the complex conjugate of Phi_nm. Changing variables in the periodic integral gives

    Phi_nm(Q_tau^T x)=exp(-im omega tau)Phi_nm(x).

For the stated J the angular factor is exp(im phi). Harmonicity and the degree-l spherical-harmonic equation give, up to a complex constant,

    Phi_nm=r^(-(l+1))P_l^j(z)exp(im phi),
    j=|m|, z=x3/r,
    P_l^j(z)=(1-z^2)^(j/2)P_l^(j)(z).

Here P_l^(j) is the ordinary jth derivative, with its possible conventional sign absorbed in the constant. The one-dimensional angular eigenspace exists only for |m|<=l; otherwise the mode is zero. Thus

    sigma_nm=C r^(-2(l+1))F_lj(z),
    F_lj=(1-z^2)^j[P_l^(j)(z)]^2, C>0

for a nonzero mode. Its degree under T_t is -nu, nu=2(l+1)c. The real scalar identities follow by first taking the linear Fourier coefficient in Section2, then using

    grad |Phi|^2=2 Re(conj(Phi)grad Phi).

Hence W.grad sigma=0 on D and E cross grad sigma=0 on {W!=0}. No averaging of a nonlinear equation without justification occurs.

The relevant Legendre polynomials are explicitly

    P2=(3z^2-1)/2,
    P3=(5z^3-3z)/2,
    P4=(35z^4-30z^2+3)/8.

They have respectively2,3,4 simple interior roots, directly from these formulas. Rolle's theorem gives all l-j simple interior roots of each derivative, whose endpoint values are nonzero. A nonzero sigma therefore has order2 on each interior nodal cone, and order2j on the axis when j>0. These sets are disjoint on D. The fixed-Holder chart theorem in the preceding proof applies since beta=a/[2(l+1)c] gives q beta=a/[(l+1)c]<1 on cones and q beta=ja/[(l+1)c]<a/c<1/2 on the axis.

There is also a proof without nodal charts: sigma=r^(-4l-2)|h_nm|^2 with a nonzero real polynomial |h_nm|^2 of degree2l. The polynomial A2 theorem applies because beta(2l)=al/[(l+1)c]<1. Either route gives k,sigma!=0 on every vortical component, E!=0 there, and E=0 implies V=0.

For omega=0 use sigma=Theta_n and nu=(l+1)c. Then beta=a/nu and beta l<1/2. The polynomial theorem gives local A2, including singular or crossing nodal sets, with bound at most97(r2/r1)^((2l+1)beta) on annular neighborhoods. The general scalar theorem proves the identical localization conclusions. Thus C40's extra hypothesis(G) is supplied by the already checked general-degree extension; the formerly conditional nodal restriction is unnecessary.

## 4. Component constants and existence of tail vorticity

For either choice of nonzero sigma, put b=|sigma|^beta. On a vortical component C the scalar theorem gives k=d_C b, d_C!=0, and sigma has a fixed sign. Thus

    grad k=d_C beta |sigma|^(beta-1)grad|sigma|!=0.

Rank with the actual S then gives grad S=lambda grad|sigma|. Dotting with Ax uses the exact degrees to obtain

    lambda=(b0/nu)S/|sigma|.

Integration on connected C yields

    k=d_C |sigma|^beta,
    S=s_C |sigma|^(b0/nu),

where s_C may be0. This does not divide by S or infer that the velocity, or the domain C itself, is axisymmetric.

If U!=0, then W is not identically0. One direct proof uses the exact scattering diffeomorphism A210 and the identity W(Xi y)=D Xi(y)Omega(y) on the escaping set. If W=0, Omega vanishes there; its complement is compact and null, and continuity forces Omega=0 everywhere. A bounded divergence-free, curl-free U on R3 has harmonic components and is constant, hence0 by decay. This argument does not require unique continuation of the original vorticity. Equivalently one may use global harmonic expansion of a curl-free homogeneous V and the tail-to-profile step. We retain the exact scattering hypotheses through the natural bounds.

## 5. At most one rotating pair

Suppose two nonzero pairs(n,j),(n',j') exist. Choose any vortical component C. The two nonzero constants for k give

    sigma'=K sigma^eta, K>0, eta=(l'+1)/(l+1).

The radial powers cancel, so on an open interval in z,

    F_l'j'(z)=K' F_lj(z)^eta, K'>0.

Analytic continuation extends the equality throughout the connected interval of {-1<z<1:F_lj(z)>0} containing it. If l>j this interval has an interior nodal endpoint. Both sides have the prescribed one-sided zero orders2 and2eta, so eta=1, hence l'=l. Equality of the polynomials then extends everywhere and their endpoint orders force j'=j.

If l=j the first polynomial is a positive constant times(1-z^2)^l on(-1,1). Letting z tend to an endpoint gives

    j'=eta l=l(l'+1)/(l+1).

Since l and l+1 are coprime, l+1 divides l'+1. Both l,l' belong to{2,3,4}; the only possible divisibility is equality. It then forces j'=j=l. Thus the pairs were the same. This proves conclusion2 for the finite low-moment index set; the arithmetic does not assert such a result for unrestricted multipole degrees.

## 6. At most one nonrotating degree, with singular nodes allowed

Suppose two distinct degrees l,l' in{2,3,4} survive. The component relation gives |Theta_n'|=K|Theta_n|^eta, eta=(l'+1)/(l+1). Since omega=0, a vortical component is a cone. On an open subset of S2,

    |Y'|=K|Y|^eta,

where Y,Y' are the degree-l and degree-l' spherical harmonics. The number eta is positive and not an integer. Let O be a connected nodal domain of Y containing an open part of this subset. The real analytic function Y'^2-K^2|Y|^(2eta) vanishes on that open part, hence on all O.

We justify that the boundary of O has a regular nodal point without using an unproved stratification assertion. In analytic conformal coordinates on S2, a spherical harmonic satisfies

    Delta_flat Y+q(z)Y=0

with analytic q. At any zero its first nonzero Taylor term H_m is a nonzero homogeneous harmonic polynomial in two variables: the lowest-order term of this equation gives Delta H_m=0. Finite order follows from analyticity and nonzero Y. Such a polynomial is r^m(A cos(m theta)+B sin(m theta)); its gradient has magnitude m sqrt(A^2+B^2)r^(m-1). The gradient of the higher Taylor terms is O(r^m), uniformly in angle. Therefore grad Y!=0 at every sufficiently small punctured point around a critical zero. Critical zeros are isolated, and their closed set on the compact sphere is finite.

If the entire boundary of O consisted of those finitely many points, O would be both open and closed in their connected complement in S2. It would equal that complement, making Y have one sign everywhere except possibly the finite set. This contradicts the zero spherical mean of a nonconstant spherical harmonic. Hence there is a boundary point with grad Y!=0.

Near that point Y is an analytic coordinate; a small rectangle has two connected sides Y>0 and Y<0. O contains the entire side of its own sign because it intersects that side and is a global connected nodal component. The analytic integral curve of grad Y/|grad Y|^2 through the point has Y=s. On its relevant half-interval the analytic function f(s)=Y'(curve(s)) obeys

    |f(s)|=K|s|^eta.

It is not identically0, so its order of vanishing is an integer j>=1. The one-sided equality forces j=eta, a contradiction. This proves conclusion3 with no smooth-nodal hypothesis. The argument uses only finite degrees for nonintegrality of eta; it does not classify arbitrary pairs with integer ratio.

## 7. Carrier rates, zero-g components and selected witnesses

A496 assigns a vortical carrier equilibrium the real eigenvalue rho<=-a with spectrum{rho,1+c,-a-rho}. At rho<-a put mu=-a-rho>0. The confirmed A534 escaping-sheet construction supplies a point x' in D with W(x')!=0 and k(x')=0. A551 gives

    mu in{1} union{1+r_n:n in K} union[2,infinity).

If1<mu<2, exactly one nonzero resonant Theta_n occurs; at x' every rotated Theta_n vanishes and every rotated gradient equals the same nonzero vector -mu V(x')/f for a nonzero sheet amplitude f. For omega!=0 its zero angular Fourier mode is therefore a nonzero function with value0 at a vortical point. Section3 excludes that. For omega=0 the real multipole itself has those properties and is excluded by the general A2 version. Thus mu=1 or mu>=2, which converts to conclusion4's rho values.

For any rho<-a, independently of resonance, the point x' with k=0,W!=0 contradicts Section3 whenever ANY low multipole is nonzero. Hence then every vortical carrier equilibrium must have rho=-a. A551 also says that when mu=1 or mu>=2 all the low multipoles vanish. These are compatible conclusions, not converse existence claims.

The same argument applies to the exact zero-g components of A536: connected components C of the vortical regular level {H=h}, with grad H!=0, g=0, and dg=lambda dH on C for a constant lambda>1. For such a component the established escaping construction uses mu=a(lambda-1), and gives the same k=0,W!=0 limiting points and A551 rate list. Thus its possible mu reduces to{1} union[2,infinity), and a nonzero low multipole excludes the component. This statement is restricted to the specified components, not arbitrary separating levels.

Theorem HF, A571, selects in a nonzero profile either a vortical equilibrium with rho<=-2a, an irrotational equilibrium, or a periodic irrotational witness, at its exact component hypotheses. Since -2a<-a, a selected vortical witness must have rho=-2(1-c) or rho<=-(3-2c), and its low multipoles all vanish. If a low multipole is nonzero, HF can only select one of its other two classes. This proves C40 Corollary35 for every omega after the preceding nonrotating audit, without excluding those other classes.

## 8. Exterior density forces every low moment scalar to vanish

Assume original vortical points are dense in {|y|>R}. The original gradients in A413 are continuous, so the full rank identity extends throughout that exterior before taking any limit. Thus for each fixed x in D,

    grad H_t(x) cross grad S_t(x)=0

for all sufficiently large t, without a W(x)!=0 restriction. The separation in Section2 now gives E cross every rotated multipole gradient=0 on ALL D. The scalar transport identities already hold on all D.

If a nonzero multipole exists, use sigma=Theta_n for omega0, or sigma=|Phi_nm|^2 for one nonzero mode when omega!=0. Section3 proves the local A2 property. Global rank and the general scalar theorem force V=0. The actual integrated spiral equation then improves U to O(r^(-2p-1)); the pressure bound is P-Pinf=O(r^-2p). The cutoff energy identity has nonzero bulk coefficient1-5c/2. Its linear, cubic and pressure boundary bounds are respectively O(R^(3-2q)), O(R^(2-3q)) and O(R^(2-2p-q)), q=2p+1>3; all tend to0. Hence U=0, and its actual low multipoles are0, contradicting the selected nonzero one.

This proves conclusion5. A603 supplies equivalence with actual tail density through the exact scattering diffeomorphism, so either density statement may be used. Exterior analytic U gives density unless its curl vanishes on the whole connected exterior; then compactly supported vorticity, complete flow and volume expansion force curl U=0 globally, hence U=0. No analyticity of the tail is inferred.

## 9. Scope and verification

The general scalar weight and nodal arguments are proved in the team records. The entire actual C40 Section5g, both existing the external referee (a second model) answers, and the complete LIT159 proof were read. The second referee's omega0 warning was correct for its stipulated input list, whose classification was rotating only; Sections3,6,7 supply the missing independent nonrotating argument. The proposed claim that LIT154 remained unaudited is stale: A596-A597 already confirm its exact hypotheses.

The moment constraints never assume symmetry of U or V, small omega, finite angular support of the velocity, or an A2 property of the actual S. They still require global zero helicity and the derivative premise, and conclusion5 additionally requires density or exterior analyticity. Every low multipole may vanish, so this does not resolve the full campaign. No computation was needed.
