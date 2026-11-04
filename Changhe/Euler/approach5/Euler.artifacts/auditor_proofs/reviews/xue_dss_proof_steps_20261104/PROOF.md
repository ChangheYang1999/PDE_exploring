# Independent audit of the Xue periodic-profile proof steps

Status: independent reconstruction and existing Theory Agent A  comparison reconciled. This document proves the stated kinematic obstruction and critical-energy lemma. It does not declare the pressure-normalized Euler theorem of Xue false.

## 1. Statement, source, and scope

The checked primary source is Liutang Xue, *Discretely self-similar singular solutions for the incompressible Euler equations*, arXiv:1408.6619v2, dated 2 March 2015. The retained source is in the team records, SHA256 `fcfa9f62acfe359006e5102a42ec245de7d6b42f27c56f6ba47e27f042f0b52d`. Its complete 27-page extracted text was read. Printed pages 3, 4, 5, 8, 9, 12, 16, 18 and 22 were also inspected as images retained in the team records. No later journal version, erratum, or new online retrieval is certified.

For an integer N >= 3, alpha > -1, put a = alpha/(1+alpha), b = 1/(1+alpha). The periodic profile equation is

    V_s + a V + b (y dot grad)V + (V dot grad)V + grad P = 0,
    div V = 0.                                                       (1)

The source's Theorem 1.1 explicitly assumes the standard whole-space pressure formula up to a time-only function. Theorem 1.2 explicitly assumes the stated renormalized pressure formula, including its qualification concerning the affine term. Neither pressure premise may be suppressed.

Three separate conclusions are reconstructed below. First, pointwise lower bounds on sup_s |V(y,s)| and smooth solenoidality do not imply the ball-energy lower bounds used in (5.2) and (5.16). Second, the proof of the pressure representation uses physical finite energy; an infinite-energy constant solution disproves an unrestricted removal of the affine term. Third, at alpha = N/2 the source's spacetime energy and pressure assumptions imply finite, constant energy at every time. The third conclusion repairs a specified fixed-time pressure estimate, not the whole remaining annular bootstrap.

## 2. A complete counterexample to the growth-only inference

For every 0 <= epsilon < 1 there is a real, smooth, period-one solenoidal field on R^N x R such that, writing angle brackets for (1+|.|^2)^(1/2),

    N^(-epsilon/2) <y>^epsilon <= sup_[0,1] |V(y,s)|
                              <= sqrt(N) <y>^epsilon,              (2)
    sup_[0,1] integral_{B_R} |V|^2 <= C R^(N-1), R >= 1.             (3)

The constant C is finite and may depend on N, epsilon, and the fixed smooth bump, but not R or s. Choose phi in C_c^infinity((-1/4,1/4)), 0 <= phi <= 1, phi(0)=1. Define

    h(x) = <x>^(-4),
    F(x,s) = <x>^epsilon sum_{n in Z} phi((s-x-n)/h(x)),
    V_j(y,s) = F(y_{j+1},s), with y_{N+1}=y_1.                       (4)

The sum is locally finite in (x,s), and at most one term is nonzero because its support interval in s has length at most 1/2. It is smooth, nonnegative, and period one. Component j is independent of y_j, proving div V = 0. The maximum of F(x,.) is exactly <x>^epsilon: it is reached at s=x modulo one. Some coordinate x of y has |x| >= |y|/sqrt(N), hence <x> >= <y>/sqrt(N). Its corresponding component gives the lower inequality in (2) at its own maximizing time. The upper bound follows for all components at every common time. No interchange of maximization and integration occurs here.

If the n-th term is nonzero at s in [0,1], then |x-(s-n)| < h(x)/4 <= 1/4. Thus <x> and <n> have uniform comparison constants. In particular this support lies in an interval centered at s-n of length at most C <n>^(-4), and F^2 there is at most C <n>^(2 epsilon). The supports are disjoint. Therefore

    sup_[0,1] integral_R F(x,s)^2 dx
        <= C sum_{n in Z} <n>^(2 epsilon-4) < infinity.              (5)

A slice of B_R perpendicular to any coordinate has (N-1)-dimensional measure at most |B_1^(N-1)| R^(N-1). Apply Fubini to each of the N components and (5) to obtain (3).

When epsilon=0, (2) satisfies the velocity bounds of (1.26) for every 0 < delta < 1/2. But (3) is o(R^N), contradicting the growth-only lower bound used in (5.16). When epsilon > 0 is small, choose epsilon_0=delta=epsilon in (1.24). Then (3) is o(R^(N+2 epsilon)), contradicting the growth-only lower bound in (5.2). The valid general inequality is

    sup_s integral_A |V(y,s)|^2 dy
        <= integral_A sup_s |V(y,s)|^2 dy.                          (6)

Thus those two printed inferences need a further Euler-specific argument if their conclusions are to hold for solutions. Smoothness, periodicity, the displayed velocity growth, and solenoidality alone are insufficient. This is the precise refutation, not a refutation of the full Euler conclusions of Theorem 1.2.

## 3. Verification that (4) fails full momentum and decay

Fix any alpha > -1. Put

    R(x,s) = F_s(x,s) + a F(x,s) + b x F_x(x,s).

For s near the support of phi around zero, R(0,s)=phi'(s)+a phi(s). This cannot vanish identically: the only compactly supported solution of phi'=-a phi is zero, whereas phi(0)=1. Choose s_* for which R(0,s_*) is nonzero. At the same time, open gaps between the supports of the x-pulses give R(x,s_*)=0. The mean value theorem supplies x_* with R_x(x_*,s_*) nonzero.

Set y_2=x_* and choose every other coordinate in an open zero interval of F(.,s_*). These zero intervals persist in a spacetime neighborhood. In that neighborhood (4) has the exact form (F(y_2,s),0,...,0), so (V dot grad)V=0. Its non-pressure residual has first component R(y_2,s) and all others zero. The antisymmetric derivative partial_2 R_1 - partial_1 R_2 equals R_x(x_*,s_*) and is nonzero. A gradient has zero such derivative, so no pressure can solve (1).

At any fixed s, a pulse is nonzero at some x=s-n. Hold the corresponding coordinate fixed and send a transverse coordinate to infinity. The relevant velocity component stays nonzero, which excludes spatial decay. Moreover it is positive on an interval in that coordinate and independent of N-1 transverse coordinates; its full spatial L^2 integral is infinite. Thus no field (4) is a counterexample to the campaign conjecture.

## 4. The finite-energy input in the pressure proof

On printed pages 8 and 9 the proof of Lemma 2.1 explicitly bounds the physical pressure in weak L^1 by the conserved physical L^2 velocity energy. It also uses that energy in the far part of the physical-pressure decomposition. Those are genuine inputs to that proof, not consequences of sublinear profile growth. A proof imported from those pages must retain them or independently replace them.

For a precise obstruction to the unrestricted affine-removal claim, take any nonzero v_0 in R^N and any alpha > 0. Then

    V(y,s)=v_0,             P(y,s)=-a v_0 dot y                     (7)

satisfies (1) at every y,s. It is smooth and periodic and satisfies 1 <= C sup_s |V| <= C' |y|^delta at large radii for any delta>0. Its affine pressure gradient is nonzero. The isotropically renormalized whole-space pressure expression for a constant tensor has zero spatial gradient: the kernel has zero mean on every spherical annulus; translating the outer truncation changes its integral by a term tending to zero; the local multiple of |v_0|^2 is constant. Consequently (7) cannot satisfy the asserted vanishing affine coefficient when alpha > -1/2 and delta < 1/2.

It follows that this coefficient cannot be removed for all smooth sublinear infinite-energy solutions. This does not contradict a theorem that requires the more restrictive pressure expression as an explicit premise. Nor is (7) decaying. In the rotating three-dimensional equation, U=v_0 is likewise solved by P=-([(1-c)I+omega J]v_0) dot y; for the target c it retains a nonzero constant far field for every omega.

## 5. Critical-energy lemma with every-time conclusion

Assume S_0>0, alpha=N/2, V in C_s^1 C_{y,loc}^3 is S_0-periodic, and P in C_s^0 C_{y,loc}^1 solves (1). Assume

    integral_0^S_0 integral_R^N |V|^2 < infinity,
    |V(y,s)| <= C(1+|y|)^delta for all y,s, 0 <= delta < 1,          (8)

and for almost every s, P modulo a time-only constant equals the standard whole-space Calderon-Zygmund pressure of V tensor V. Then

    E(s) = integral_R^N |V(y,s)|^2
         = S_0^(-1) integral_0^S_0 E(t) dt < infinity               (9)

for every s, not merely almost every s.

Choose a radial smooth nonincreasing chi, equal to 1 on B_1, zero off B_2, and between 0 and 1. Set chi_R(y)=chi(y/R), E_R(s)=integral chi_R |V|^2. Multiplication of (1) by 2 chi_R V and compactly supported integration by parts give

    E_R'(s) = integral grad chi_R dot
              [b y |V|^2 + V |V|^2 + 2 P V],                      (10)

because 2a-Nb=0. The pressure gauge contributes zero since integral grad chi_R dot V=0. Every compactly supported integral and time differentiation is justified by the stated local regularity.

For almost every s, E(s) is finite by (8). At such s split the normalized pressure into the operator on (V tensor V)1_{B_4R} and its complement. The L^(3/2) boundedness of that operator and Holder give, on A_R={R<|y|<2R},

    integral_A_R |P_near| |V|
       <= C ||V||_{L^3(B_4R)}^2 ||V||_{L^3(B_2R)}
       <= C R^delta E(s), R>=1.                                   (11)

Indeed integral_B_4R |V|^3 <= C R^delta E(s). For the far part the separation gives |K(y-z)| <= C |z|^(-N), hence |P_far(y,s)| <= C R^(-N) E(s) on A_R. Also integral_A_R |V| <= C R^(N+delta), so the far pressure product has the same bound as (11). The cubic term is bounded by C R^delta E(s). The b y term in (10), including |grad chi_R| <= C/R, is at most C integral_A_R |V|^2.

For any fixed s_1<s_2, integrate (10) and use these estimates almost everywhere in time:

    |E_R(s_2)-E_R(s_1)|
       <= C integral_s_1^s_2 integral_A_R |V|^2
          + C R^(delta-1) integral_s_1^s_2 E(s) ds -> 0.            (12)

Periodicity and (8) make the spacetime integrals finite on every bounded time interval. The first term tends to zero by integrability of the spatial tail, and the second by delta<1. No essential-supremum energy bound has been used.

Choose one good time s_1 with E(s_1)<infinity. Since chi_R increases to 1 as R increases, monotone convergence and (12) give E(s_2)=E(s_1) for every s_2>s_1; reversing the interval gives the same for earlier times. Average this constant over a period to obtain (9).

At the bottom of printed page 16 the source bounds a fixed-time inner pressure term by a spacetime energy norm. The direct kernel estimate is C R^(-N) E(s). Formula (9) makes this at most C R^(-N) S_0^(-1) ||V||_{L^2_{s,y}}^2 at every time, providing the missing justification. This lemma alone does not establish the remainder of the annular-decay iteration.

## 6. Weight check and campaign applicability

Before the K_3 estimate on printed page 12, the time weight is exp(s(2 alpha-N-1)/(1+alpha)). On its spatial support, exp(s/(1+alpha)) is comparable to |y|. Thus the weight is comparable to |y|^(2 alpha-N-1), not to 1/|y| for general alpha. The missing factor is |y|^(2 alpha-N). At alpha=N/2 it is one, exactly the case where Section 4.2 uses K_3. For alpha<=N/2 on exterior radii >=1, dropping it can give a weaker upper bound, but this does not justify a general all-alpha identity or the same upper estimate for alpha>N/2. The K_2 dyadic expression retains the exponent N+1-2 alpha. No general K_3 formula is used here outside criticality.

Theorem 1.2 concerns a lower bound that is already incompatible with the target's uniform decay. Its proof-step issue therefore yields no target counterexample and invalidates no campaign result that retained the source's actual hypotheses. In N=3, the target 2/5<c<1/2 corresponds to 1<alpha=1/c-1<3/2. For finite 3<=p<infinity, alpha>3/p, so Theorem 1.1(1), when its additional L_s^3 L_y^p and pressure hypotheses hold, is in the energy-growth alternative, not the alpha<=3/p vanishing alternative. Its energy power is 3-2 alpha=5-2/c. A ball-energy power does not imply a pointwise homogeneous velocity expansion; Remark 1.3 itself describes the proposed asymptotics as expectations.

A rotation change of variables preserves radial ball energies and spatial L^p norms. It cannot create missing integrability or justify pressure normalization. Lemma (9) concerns c=2/(N+2), which in three dimensions is the excluded endpoint c=2/5 of the open target interval. The full arbitrary-omega nonexistence conjecture stays open.

## 7. Verification boundary

Dependencies are the printed source for the identified statements, elementary smooth bump constructions and Fubini, the local energy identity derived above, and the standard whole-space Calderon-Zygmund L^p bound at p=3/2. There is no numerical evidence standing in for an estimate and no formal proof-assistant claim. The source submission and 41 manual obligations are retained alongside this proof. The complete existing Theory Agent A  comparison is reconciled in Section 9.


## 8. Additional pressure and time-integrability checks from the comparison

The constant example (7) extends to every alpha>-1: its affine coefficient is -a v_0 and vanishes exactly when alpha=0. Consequently, if the affine coefficient A(s) in Xue's pressure formula (1.23) were allowed to be arbitrary, this example would satisfy the regularity, periodicity, nondecaying lower bound and upper growth bound of Theorem 1.2(2) for every alpha>-1/2 and 0<delta<1/2. It would have E(R)=|B_1||v_0|^2 R^N. For alpha>0 or alpha<-delta the example contradicts the asserted range -delta<=alpha<=0. For -delta<=alpha<0 it contradicts the claimed two-sided energy scale R^(N-2alpha). At alpha=0 it is consistent. Thus the free-affine reading is false at every admissible nonzero alpha. The pressure-normalized reading, with A=0 explicitly required in this parameter range, excludes the example. Any use of Theorem 1.2(2) in this campaign must retain that requirement; this audit does not refute that reading of the theorem.

The implication from finite spacetime L2 to finite energy at every time is also false without an equation argument, even for smooth bounded solenoidal fields. To see this, choose a nonzero smooth divergence-free bump w of unit L2 norm supported in B(0,1/4). Such a bump is obtained by taking (partial_2 psi,-partial_1 psi,0,...,0) and normalizing. Let w_n(y)=w(y-3n e_1), n>=1, so the supports are disjoint and leave every compact set. Choose a smooth psi_time supported in(-1/2,1/2), with psi_time(0)=1, and set

    a_n(s)=sum_(j in Z) psi_time(n^2(s-j)),
    V(y,s)=sum_(n>=1) a_n(s)w_n(y).

The sum is locally finite in spacetime and hence smooth. The field is uniformly bounded, solenoidal and period one. Disjoint spatial supports give

    integral_0^1 integral |V|^2
       =sum_(n>=1) n^-2 integral_R psi_time(t)^2dt < infinity,
    integral |V(y,0)|^2dy=sum_(n>=1)1=infinity.

This is a counterexample to the generic norm implication only. The critical-energy theorem proved in Section 5 supplies the missing equation-specific argument for its own normalized Euler class.

Finally the standard pressure normalization, when present, is preserved by rotating coordinates. The whole-space kernel satisfies K(Qy)=QK(y)Q^T for every orthogonal Q, and the local multiple of |V|^2 is rotation invariant. Thus the simultaneous rotation V(y,s)=Q(s)U(Q(s)^T y), Q(s)=exp(omega sJ), carries a standard pressure to the standard pressure of V. It does not turn an arbitrary affine pressure into a normalized one. Direct differentiation yields the periodic equation from the complete rotating profile equation; radial energy and spatial Lp norms are preserved.

## 9. Reconciliation and exact limitations

All 197 lines of the existing A comparison, including twelve numbered checks and remarks R1-R4, were read. The exact pressure-free shear residual, uniform line L2 estimate and lower-growth quantifiers agree. The critical pressure-flux argument, every-time energy limit and factor 1/S_0 agree. The source locations were checked against the fully read primary manuscript, not merely its abstract. The K3 observation is limited exactly as in Section 6: at criticality the omitted factor is one, and below criticality on exterior radii it can be dropped for a weaker upper estimate.

R1 is resolved by the explicit pressure-reading distinction in Section 8. R2's generic time-integrability counterexample is proved there with uniformly bounded disjoint bumps. R3's Fatou variant is valid but unnecessary: the chosen radial nonincreasing cutoff already gives monotone convergence. R4's rotation covariance is verified explicitly above. The comparison's symbolic and sampled diagnostics are not used as proofs.

The A agent is configured as model; its actual provider execution is independently unattested. Collaboration used existing files only. No mathematical program, new model client, formal build or external retrieval was executed for this audit. The full annular bootstrap of Xue, any later journal version, and unrestricted rotating nonexistence are outside the conclusions proved here.
