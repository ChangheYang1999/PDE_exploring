# The actual pressure is canonical under uniform velocity decay

Status: PROVED at the exact A500 CONFIRMED scope. The entire independent proof was read after writing. Only the canonical-pressure claim in the coordinator submission is included; no strain-tube, anisotropy or gradient-decay assertion is certified.

## 1. Exact statement

Let0<c<1,omega be any finite real number,J(y1,y2,y3)=(-y2,y1,0),A=cI-omega J. Let U in C2(R3;R3),P in C1(R3) solve

    div U=0, (1-c)U+DU(Ay+U)+omega JU+grad P=0,
    U(y)->0 uniformly as |y|->infinity.

Put F_ij=U_iU_j and Gamma(x)=1/(4pi|x|), so -Delta Gamma=delta0. Let p be the canonical distribution sum_ij partial_i partial_j Gamma*F_ij, defined modulo constants by the far-field subtraction below. Then

    P=p+C

for one real constant C. No global bound on DU, growth bound on pressure, helicity condition, integrability or decay of grad P is assumed. The literal scalar integral Gamma*tr(DU^2) need not converge. The result identifies the actual pressure as a renormalized distribution and does not by itself bound its pointwise derivatives.

## 2. Construction of p and its gradient

U is bounded, so F is bounded and locally C2. Write K_ij=partial_i partial_j Gamma as its standard distribution: a local delta term plus the principal-value degree-minus-three kernel. Around any fixed y, its local action on F can be defined by subtracting F(y) from the mean-zero principal-value part. Local C1 regularity makes the remaining integral absolutely convergent after radial integration; the delta term is finite.

At infinity subtract the kernel at the base point0: use K_ij(y-z)-K_ij(-z) for all sufficiently large |z|. For y in a fixed compact set this difference is O((1+|y|)|z|^-4), hence integrable against bounded F. A fixed smooth cutoff separating local and far regions gives a globally consistent distribution p modulo an additive constant. Different fixed subtraction conventions change only that constant. This definition, rather than an unrenormalized scalar Newtonian convolution, is meant by canonical pressure here.

Differentiation in y removes the subtraction. Thus

    partial_k p=sum_ij partial_k partial_i partial_j Gamma*F_ij. (1)

This is a distribution with integrable tail: outside0 its kernel is O(|z|^-4). Locally it is interpreted distributionally on the C2 data. It is enough to use(1) after mollification below; no pointwise bound is claimed.

Incompressibility gives q:=tr(DU^2)=partial_i partial_j F_ij locally and distributionally. Taking divergence of momentum cancels the two omega terms and gives -Delta P=q. The construction also gives -Delta p=q. For clarity, local regularity of p needs no global control: subtract the Newtonian potential of a compact cutoff of q. The difference is locally harmonic; q is C1, and subtracting its value in the degree-minus-three second-derivative kernel proves that this local potential is C2. Thus p is locally C2, and h=P-p is an entire harmonic distribution, represented by a smooth harmonic function. Momentum independently upgrades P to C2.

## 3. Large radial averages of the canonical gradient

Choose a smooth radial compactly supported phi with integral1 and put phi_R(x)=R^-3 phi(x/R). The smooth kernel

    T_kij=(partial_k partial_i partial_j Gamma)*phi

is bounded on compact sets and O(|x|^-4) at infinity, hence belongs to L1. This follows by convolving the distribution near its singularity with the smooth test function; outside a larger ball it is the ordinary third derivative kernel averaged against a compact function. Its homogeneity gives

    (partial_k partial_i partial_j Gamma)*phi_R(x)=R^-4 T_kij(x/R),
    ||T_kij,R||_L1=R^-1||T_kij||_L1.

Convolution can therefore be associated with bounded F; one may first cut off F and pass to the limit using this integrable kernel. Equation(1) gives

    ||grad p*phi_R||infinity<=C R^-1||F||infinity->0.          (2)

The constant depends only on the fixed mollifier and dimension.

## 4. Large averages of the actual momentum equation

With tensor convention (U tensor B)_ij=U_i B_j, div(U tensor B)=DU B+3cU because div B=3c. Hence the exact momentum equation is

    grad P=(4c-1)U-omega JU-div(U tensor Ay+U tensor U).       (3)

For every fixed x, U*phi_R(x)->0. To see this directly, split the averaging integral at a fixed radius L: the bounded inner contribution is O(R^-3), and the outer contribution is at most C sup_(|y|>L)|U(y)|. First let R grow, then L grow.

The nonlinear tensor term in(3), after moving its derivative to phi_R, has size at most C M^2/R, where M=sup|U|. The affine tensor term is bounded by

    C_A R^-4 integral_(|z-x|<=C_phi R) |z| |U(z)| dz.         (4)

On |z|<=L, this tends to0 for every fixed L. On the remainder, its limsup as R grows is at most C_A sup_(|z|>L)|U(z)|: for fixed x the integral of |z| over the sampled ball is at most C_x R^4 for all sufficiently large R, with a bounded limiting coefficient. Let L grow to infinity. The contribution(4) tends to0. Therefore

    (grad P*phi_R)(x)->0 for every fixed x.                   (5)

No derivative of U has been estimated here; all derivatives were transferred to the averaging kernel.

## 5. Harmonic ambiguity and scope

The gradient of the entire harmonic h=P-p satisfies its radial mean-value identity for every R:

    grad h*phi_R(x)=grad h(x).

This holds for any smooth radial phi of integral1 by expressing the convolution as weighted spherical averages. It does not require h to have polynomial growth or to be bounded. Equations(2) and(5) force grad h(x)=0 for every x. Since R3 is connected,h is constant. This proves the theorem.

The argument remains valid at every fixed finite omega; no smallness is used. It proves neither grad P->0 pointwise nor DU bounded. In particular it cannot replace the pressure feedback estimates used in A498. It only shows that the full profile equation and velocity decay leave no nonconstant harmonic pressure ambiguity. No absolute convergence claim is made for the unmodified scalar Newtonian pressure integral.

## 6. Verification record

The exact assumptions and the complete canonical-pressure argument in the coordinator source were read, together with the entire configured-model coordinator check. The source reports that its own separate model consultation failed; the coordinator then checked the canonical argument line by line. This reconstruction checks the distributional construction, all tensor signs, the L1 smoothed kernel, the large-radius velocity averaging and the harmonic mean-value step independently. Other claims in the source are outside this audit. Existing coordinator configuration is the primary model, not independent provider runtime attestation. No computation or new model client was used.
