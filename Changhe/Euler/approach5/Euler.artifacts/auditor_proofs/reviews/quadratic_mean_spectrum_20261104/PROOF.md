# Exact spectrum of the quadratic pressure averaging quotient

## 1. Statement and scope

Let V be the fifteen-dimensional real vector space of homogeneous quadratic vector polynomials Q on R3 with div Q=0. Give V the inner product <Q1.Q2>, where brackets denote normalized surface integration on the unit sphere. For Q in V let N_Q be the symmetric matrix such that -tr((DQ)^2)=x^T N_Q x. The quadratic form

    A(Q)=tr N_Q/60

has, relative to the sphere inner product, the three eigenvalues

    -1/2 with multiplicity 7,  1/18 with multiplicity 3,
     1/4 with multiplicity 5.

Their respective eigenspaces are gradients of harmonic homogeneous cubics, the fields 2|x|^2v-(x.v)x with v in R3, and the fields x cross Mx with M symmetric modulo scalar multiples of I. Thus for Q nonzero,

    -1/2 <= tr N_Q/(60<|Q|^2>) <= 1/4,

with precisely those first and third equality spaces. This quotient is the mean of any homogeneous quartic Poisson pressure divided by the mean energy. It is not the pointwise pressure optimum gamma_Q. In particular, attaining the upper mean quotient does not mean gamma_Q=1/4.

## 2. The universal mean identity

The identity reconstructed in the boundary-uniqueness audit, Section10, is

    A(Q)=(<|Q|^2>-7<(Q.n)^2>)/4.                       (1)

For completeness it needs no sign assumption on pressure. Every quadratic source x^T N x has a homogeneous quartic inverse Laplacian, namely

    R=|x|^2(x^T N x)/14-(tr N)|x|^4/140.

Indeed Delta(|x|^2(x^T N x))=14x^T N x+2(tr N)|x|^2 and Delta|x|^4=20|x|^2. For this R, the tensor S=Q tensor Q+R I has div div S=0. The divergence theorem on finite balls, followed by differentiating the radial flux of S n, gives r A_sphere'(r)=e(r)-3v(r), with A_sphere=mean n.S n. All fields are polynomial and there is no origin flux. Homogeneity gives 4(<R>+<(Q.n)^2>)=<|Q|^2>-3<(Q.n)^2>. Finally <R>=tr N/60 by averaging Delta R. This proves (1). Every other homogeneous quartic solution has a harmonic difference of zero sphere mean, so its pressure mean is the same.

## 3. Three orthogonal subspaces

Let H3 be the space of harmonic homogeneous cubics h. It has dimension7: scalar cubics have dimension10, and Delta maps onto the three-dimensional linear space because Delta(|x|^2 l)=10l for every linear l. The gradient map is injective on H3. Write G3={grad h:h in H3}.

Let P1 consist of P_v=2|x|^2v-(x.v)x. It is solenoidal since both terms have divergence4x.v. Its dimension is3, since on the unit sphere n.P_v=n.v determines v.

The tangential solenoidal space T2 consists of x cross Mx with M symmetric modulo scalar matrices and has dimension5. A direct proof is given in the boundary-uniqueness audit, Section10: x cross curl Q=-3Q for a tangential quadratic Q; zero divergence forces the resulting matrix symmetric. The kernel is precisely scalar matrices. Its sphere divergence is zero, because its Euclidean divergence and radial component both vanish.

The spaces G3 and P1 are perpendicular to T2: their tangential components are sphere gradients, and integration by parts pairs these to zero against a tangential field of zero sphere divergence. To check G3 perpendicular to P1, put g(n)=n.v and restrict h to the sphere. The polar-coordinate Laplacian gives

    -Delta_S h=12h,   -Delta_S g=2g.

Self-adjointness gives <hg>=0. On the sphere,

    grad h=3h n+grad_S h,
    P_v=g n+2 grad_S g.

Their inner product is 3<hg>+2<grad_S h.grad_S g>=7<hg>=0. Thus the three subspaces are pairwise orthogonal. Their dimensions sum to15, the dimension of V, so they exhaust it. This proves the decomposition without a representation-theoretic irreducibility assertion. The dimension of V is18-3=15 because divergence maps vector quadratics onto all linear polynomials.

## 4. Energy and radial energy on each subspace

For Q=grad h in G3, integration by parts on the sphere gives

    <|Q|^2>=(9+12)<h^2>=21<h^2>,
    <(Q.n)^2>=9<h^2>=(3/7)<|Q|^2>.

For Q=P_v in P1 the corresponding formulas are

    <|Q|^2>=(1+4*2)<g^2>=9<g^2>,
    <(Q.n)^2>=<g^2>=(1/9)<|Q|^2>.

For Q in T2 the radial energy is zero. Radial cross terms between G3 and P1 vanish because they are multiples of <hg>=0, and all cross terms with T2 vanish because its radial component is zero.

Therefore if Q=Q_G+Q_P+Q_T is the orthogonal decomposition, (1) becomes

    A(Q)=-(1/2)<|Q_G|^2>+(1/18)<|Q_P|^2>
                         +(1/4)<|Q_T|^2>.             (2)

Polarizing (2) proves the full stated self-adjoint spectrum and its multiplicities. The Rayleigh bounds and exact equality spaces follow by comparing the three distinct coefficients, all three summand energies being nonnegative.

## 5. Pressure-optimum distinction

If R>=gamma|Q|^2, taking its mean gives gamma<=A(Q)/<|Q|^2>. This is only a necessary condition. In particular, equality in the maximum mean quotient makes Q tangential but does not give a pressure realizing the pointwise coefficient1/4. The separate argument in the boundary-uniqueness audit, Section10, shows that R>=|Q|^2/4 would force R=|Q|^2/4 and then Q=0. For nonzero Q with a nonempty feasible set, fixed-Q attainment therefore gives gamma_Q<1/4. This is the precise correction recorded in A2818.

## 6. Evidence and comparison

The existing Theory Agent C 03:01 note, its complete script and its complete log were read. The three exact roots and multiplicities reported there agree with (2), as do the three proposed spaces. The direct proof above removes any dependence on sampled elements, floating eigensolvers or a Schur-lemma argument. The basis-dependent overall constant -131072 in the reported determinant is not a claim of this audit and is not needed. No script was executed or rerun.

This is a mathematical comparison with the existing agent configured as model; actual provider execution is independently unattested. No new agent or model client was launched. The statement supplies no global pressure normalization or pointwise pressure lower bound for a decaying rotating Euler profile.


## 7. Correction acknowledged and checked

The Theory Agent C 03:10 note and its revised03:01 entry were read. They explicitly replace attainment of gamma_Q by attainment of the averaging quotient, retain the strict fixed-Q inequality, and mark the original sentence as refuted by A2818. The two descriptions of the tangential space agree: for a harmonic quadratic h, grad h=2Sx with S symmetric and trace free; adding a scalar multiple of I to M leaves x cross Mx unchanged. The corrected entry also leaves the determinant prefactor uncertified. This resolves the wording defect without changing A2819. The same note acknowledges the report's still-pending homogeneous-quartic clarification.
