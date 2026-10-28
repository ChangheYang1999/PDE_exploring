# A weighted fixed-exponent inverse admitting the growing checkpoint residual

## Theorem

Let rho_bar be either exact checkpoint88 or131, reconstructed from the read-only source as in ../source_audit/PROOF.md. Let c be its exact exponent and Ubar its canonical velocity. Put

    R=2^200, w_R=(1+r²/R²)^(-11/10),
    ||h||_(L,R)=||w_R h||_(homogeneous H^-1).

Let X_(L,R) be the completion of the smooth compact parity core in this norm. The fixed-exponent operator

    L_fix h=(cX+Ubar).grad h-h+U[h].grad rho_bar

has a bijective transport-generator realization on X_(L,R), and

    ||L_fix^-1 f||_(L,R)<=5||f||_(L,R).                       (1)

The two checkpoints' unnormalized residuals belong to X_(L,R), because their leading powers2/c-1 are less than1/5. Their leading angular perturbations, scaling direction and exponent-logarithm directions do not belong. The huge radius makes (1) a rigorous existence-of-an-inverse result; it does not give a useful nonlinear residual bound.

## Coefficient hypotheses

The proof uses 9/5<c<37/20, global M>=19/5 I, and the following bounds, with delta=2/5:

    C_rho=sup r^delta(|grad rho_bar|+r|D²rho_bar|)<=2^16,
    C_U=sup r^(delta-1)|Ubar|<=2^5,
    C_DU=sup r^delta|DUbar|<=2^5,
    C_D2U=sup r^(1+delta)|D²Ubar|<=2^15.                      (2)

The matrix and unweighted derivative certificates are already established. The independent script verification/weighted_background_bounds.py checks (2) by combining those bounds on r<=100 with exact Fourier sectors and a rigorous binomial tail on r>=100. Its JSON files contain the input hashes and all intermediate bounds. The certification argument is detailed below.

## Exact energy and radial transport weight

For g=w_R h, phi=(-Delta)^-1 g, q=grad phi, set

    b=V.grad log w_R=b0+b1,
    b0=-(11/5)c t, t=r²/(R²+r²),
    b1=-(11/5) Ubar.X/(R²+r²).

The exact identity is

    -<w_R L_fix h,phi>
      =integral q^T(M+bI)q -(1/2)integral Delta b phi²
        -<D_R g,phi>,                                      (3)

where D_R is the commutator in COMMUTATOR_PROOF.md. This includes every weight term.

The radial angular-Poincare inequality is especially useful here: for every nonnegative radial a(r),

    integral a(r) phi² <= integral r² a(r)|q|².               (4)

It follows from the circle Poincare inequality at each radius. It is stronger than applying the global Hardy inequality and then taking unrelated extrema.

For r<=R, Delta b0<=0, b0>=-(11/10)c, so the M+b0 part of (3), including Delta b0, is bounded below by19/5-(11/10)c>2/5.

For r>=R, M>=(2c+1-(C_DU+C_rho)R^-delta)I. Also

    (1/2)r² Delta b0=2(11/5)c t(1-t)(2t-1)>=0.

Using (4), the net scalar cost is at most(11/5)c times

    t+2t(1-t)(2t-1)=-4t³+6t²-t
       <=1/2+2sqrt(6)/9<21/20.

Consequently this region contributes at least

    1-(31/100)c-(C_DU+C_rho)R^-delta
       >=2/5-(C_DU+C_rho)R^-delta.                           (5)

The pointwise M lower bound is radial here, so applying (4) does not require comparing phi/r and q pointwise.

## The velocity part of the weight

Write P=Ubar.X and D=R²+r². The definitions in (2) imply

    |P|<=C_U r^(2-delta),
    |grad P|<=(C_U+C_DU)r^(1-delta),
    |Delta P|<=sqrt(2) C_D2U r^-delta.

The last identity uses Delta P=X.Delta Ubar+2 div Ubar and div Ubar=0. Expanding Delta(P/D) gives

    Delta(P/D)=(Delta P)/D-4X.grad P/D²
                  +P(-4/D²+8r²/D³).

For m=1,2,3, r^(2m-delta)/(R²+r²)^m<=R^-delta. It follows that the total energy loss from b1 and Delta b1 is at most

    (11/5)(9C_U+2C_DU+C_D2U/sqrt(2))R^-delta ||q||².          (6)

Here the ordinary parity Hardy inequality controls the nonradial Delta b1 term.

The commutator theorem gives an additional loss2^53 C_rho R^-delta||q||². Combining (3)-(6) proves coercivity at least

    2/5-R^-delta [C_DU+C_rho
       +(11/5)(9C_U+2C_DU+C_D2U/sqrt(2))+2^53 C_rho].         (7)

For R=2^200 and (2), the subtracted quantity is less than1/5. Thus the final margin is at least1/5, giving the constant5 in (1).

## Existence of the generator and surjectivity

The smooth complete Lipschitz flow Phi_t of V preserves parity, fixes the origin and has two-sided finite exponential distortion of distances. On the compact core the transport semigroup is

    T_t h=e^-t h(Phi_t X).

After multiplication by w_R its action on g is multiplication by w_R(X)/w_R(Phi_t X), followed by composition with Phi_t. For each finite time this ratio and r times its gradient are bounded, by the flow distortion bounds and the logarithmic derivative of w_R. The parity Hardy inequality therefore proves boundedness on H^-1. Approximation from the compact core gives strong continuity. The usual resolvent-integral approximation by finite Riemann sums of transported compact core functions proves that this core is a graph core.

The weighted coupling w_R B w_R^-1 is bounded on H^-1 by the final paragraph of COMMUTATOR_PROOF.md. Bounded perturbation therefore supplies a C0 semigroup with generator w_R L_fix w_R^-1. The exact core inequality (7) extends to its generator domain. Differentiating the squared norm along generator-domain solutions gives decay at least exp(-t/5). By density the same bound holds on the whole space.

The operator -integral_0^infinity exp(t L_fix)dt consequently converges in operator norm, has bound5, and is both a right and a left inverse on the strong generator domain. This proves surjectivity as well as injectivity. The unweighted inverse and this weighted inverse are not asserted to agree on every common forcing unless their solutions belong to a common uniqueness class.

## Certification of (2)

On r<=100 use |grad rho_bar|<=11sqrt(2), |D²rho_bar|<=77, |DUbar|<=14/5, |D²Ubar|<=35, and Ubar(0)=0. The last two bounds imply |Ubar(X)|<=(14/5)r. Multiplication by the relevant powers of100 gives the local bounds in the JSON.

For r>=100 expand each exact potential generator in r^-2 through q=6 and differentiate the resulting angular Fourier polynomials exactly. For an order d=3,4,5 derivative, every omitted coefficient is bounded by

    binom(q+25,q)(2q+32)^d

 times the absolute input coefficient and r^(-2q). The bound26 on |p_j-k| and the angular frequency bound18 justify this majorant. Starting at q=7, its successive ratio is at most

    ((q+26)/(q+1))*((2q+34)/(2q+32))^d /100² <1,

and decreases with q. A geometric tail is therefore valid uniformly outside100. Exact angular coefficient sums bound each differentiated sector; Euclidean sums give the vector and tensor bounds. Finally multiply by100^(2/5-(1-gamma)), which is valid because1-gamma>2/5. All arithmetic entering (2) and (7) is enclosed with384-bit Arb. The computation reads our exact source reconstruction and never imports the numerical work's evaluator.

## Limitations

The admitted correction exponent is1/5. The center and nonlinear high regularity are not supplied by this low inverse. A change of the weight radius preserves the underlying weighted space but changes equivalence constants substantially. In particular the norm of the growing residual for R=2^200 can be enormous. No a posteriori smallness condition or nonlinear existence theorem follows from (1).

## Small Lipschitz velocity perturbations

The same low realization has a uniform estimate under a divergence-free parity-preserving perturbation W of the transport field, provided W(0)=0 and ||DW||_infinity<=1/120. No third derivative of W is required for the energy estimate. Write b_W=W.grad log w_R. The extra transport contribution is

    integral q^T sym(DW)q + integral b_W|q|²
       -(1/2) integral Delta b_W phi².

Interpret the last term weakly as integral phi grad b_W.q. Since |W|<=r||DW||_infinity,

    ||b_W||_infinity<=s||DW||_infinity,
    ||r grad b_W||_infinity<=4s||DW||_infinity, s=11/5.

The total absolute loss is at most(1+5s)||DW||_infinity ||q||²=12||DW||_infinity||q||². Starting with the certified margin1/5 therefore leaves at least1/10. The perturbed complete Lipschitz transport flow and the same bounded coupling give an inverse with norm at most10. Smooth W can first be used on the core; C1 Lipschitz W follows by the same weak energy identity and flow construction. This is a low-norm result only. A high solvability theorem for W=U[k] is not supplied.
