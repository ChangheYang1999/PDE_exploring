# Independent audit of the sharp quarter-ratio stress theorem

Status: CONFIRMED A2654-A2656 at the precise scope below; the erroneous proposed endpoint-example wording is REFUTED A2657, and unrestricted extensions remain OPEN A2658. This concerns a local divergence and Poisson system, not the full similarity equations.

## 1. Exact theorem and scope

Let V be C2 on B_R(x0) in R3, and let H be C1. Define E=|V|^2 and P=E/2-H. Suppose

    div V=0, -Delta P=tr((DV)^2) in distributions,
    V(x0)=DV(x0)=0,
    0<=H<=E/4 at every point of B_R(x0).              (1)

Then V=H=P=0 on that whole ball. The quarter constant is optimal within this C2 divergence-Poisson class. At the quarter constant, replacing C2 by C1,1 for V is false. The proof and exact examples below establish these separate claims. They do not establish optimality within the stronger Euler similarity or carrier equations.

The pointwise inequality is assumed on a whole neighborhood, including all velocity zeros. A mere limsup bound approaching one quarter does not supply that inequality and is not included.

## 2. Distributional center flux and the exact endpoint defect

Translate x0 to zero and put T=V tensor V+P I, a symmetric C1 tensor. Incompressibility and (1) imply div div T=0 in distributions. Write normalized sphere averages as

    e(r)=<E(rn)>, v(r)=<(V(rn).n)^2>, h(r)=<H(rn)>,
    A0(r)=<n.T(rn)n>=v+e/2-h.

The radial component of div T has average A0'+(2A0-B0)/r, where B0=<tr T-n.Tn>=2e-v-2h. Thus the continuous flux of div T across the sphere is

    4pi r^2[A0'-(e-3v)/r].                            (2)

To justify zero flux without differentiating H twice, test div(div T)=0 against smooth radial functions supported in annuli. The flux in (2) is constant in r as a distribution, hence everywhere by continuity. Since div T is bounded near zero and the sphere area tends to zero, that constant is zero. Consequently

    r A0'=e-3v.                                      (3)

The bounds in (1) give e/4<=A0<=3e/2. The C2 Taylor estimate gives e=O(r^4). Set k=e-4h>=0 and G=A0/r^4. Direct substitution into (3) gives the exact identity

    G'=-(7v+k)/r^5.                                  (4)

Hence G is nonnegative, bounded near zero and nonincreasing as r increases. Let L=lim_(r down to 0)G(r). For 0<R0<R,

    integral_0^R0 (7v+k)/r^5 dr=L-G(R0)<infinity.       (5)

If V is nonzero anywhere in the ball, continuity gives a sphere with e>0, hence G>0 and L>0. No sign of A0' is asserted.

## 3. The quadratic Taylor field is tangential and would be nonzero

Let Q(x)=(1/2)D2V(0)[x,x]. C2 regularity gives, on each compact set,

    V_epsilon(x)=epsilon^-2 V(epsilon x) -> Q(x)
    in C2 as epsilon decreases to zero.               (6)

Indeed D2V_epsilon=D2V(epsilon x) converges uniformly; the value and first derivative follow from Taylor expansion and the two zero center jets. Thus

    e(r)/r^4 -> e_Q=<|Q(n)|^2>,
    v(r)/r^4 -> v_Q=<(Q(n).n)^2>.

If v_Q>0, its contribution to (5) would dominate a positive multiple of integral dr/r and diverge. Therefore v_Q=0, and its nonnegative continuous integrand vanishes everywhere. Homogeneity gives x.Q(x)=0 for all x. Divergence freedom passes through (6) to Q.

If V were nonzero, the positive limit L and the upper bound A0<=3e/2 imply e_Q>=2L/3>0. Thus the remaining possibility is a nonzero tangential divergence-free homogeneous quadratic field Q.

## 4. The scalar limit follows from the nonnegative defect

Set E_epsilon=|V_epsilon|^2 and H_epsilon(x)=epsilon^-4 H(epsilon x). Since E-4H>=0 pointwise, for every fixed b>0 and sufficiently small epsilon,

    integral_(B_b) |E_epsilon-4H_epsilon| dx
      =4pi epsilon^-7 integral_0^(epsilon b) k(r)r^2 dr
      <=4pi b^7 integral_0^(epsilon b) k(r)/r^5 dr
      ->0.                                           (7)

The inequality uses r^7<=epsilon^7 b^7. The limit is the absolute continuity of the finite nonnegative integral in (5). Combining (7) with (6),

    H_epsilon -> |Q|^2/4 in L1 on compact sets.        (8)

This needs no fourth derivative of H, scalar Taylor expansion, compactness extraction or subsequence.

The rescaled Poisson equation is exactly

    Delta H_epsilon=Delta E_epsilon/2
                       +tr((DV_epsilon)^2).

Both sides have the same epsilon^-2 scaling. Pass to distributions using (8) on the left and the C2 convergence in (6) on the right. It gives

    Delta|Q|^2/4+tr((DQ)^2)=0.                        (9)

## 5. All tangential divergence-free quadratic fields fail the limit equation

From x.Q=0, differentiation gives (DQ)^T x=-Q. Euler's identity gives DQ x=2Q. The vector curl identity therefore yields

    x cross curl Q=-3Q.

Since curl Q is linear, Q=x cross (Mx) for a real constant matrix M. Taking the divergence gives div Q=-x.curl(Mx). Its vanishing for every x implies curl(Mx)=0, so M is symmetric. An oriented orthonormal eigenbasis preserves all the equations. In that basis

    Q=(A yz,B xz,C xy), A+B+C=0.

Direct differentiation gives

    Delta|Q|^2=2[(B^2+C^2)x^2+(A^2+C^2)y^2
                                 +(A^2+B^2)z^2],
    tr((DQ)^2)=2[BC x^2+AC y^2+AB z^2].

Equation (9) says B^2+C^2+4BC=0 and its cyclic versions. Since A+B+C=0 these are

    A^2+2BC=B^2+2AC=C^2+2AB=0.                       (10)

Multiplying the three identities A^2=-2BC and its cyclic versions yields (ABC)^2=-8(ABC)^2. Thus ABC=0. If A=0, the other two equations give B=C=0; the cyclic cases are identical. Hence Q=0, contradicting Section 3 if V were nonzero. It follows that V vanishes on the original ball. The pointwise bounds in (1) then force H=P=0.

## 6. Exact countertests of the hypotheses and the constant

Let rho=(x^2+y^2)^(1/2). For beta>1 define on R3

    V_beta=rho^(beta-1)(-y,x,0),
    E_beta=rho^(2beta), P_beta=rho^(2beta)/(2beta),
    H_beta=[(beta-1)/(2beta)]E_beta.                   (11)

Away from the axis the nonzero planar derivative block, in the radial and angular frame, is

    [[0,-rho^(beta-1)],[beta rho^(beta-1),0]].

Hence div V_beta=0, tr((DV_beta)^2)=-2beta rho^(2beta-2), and Delta P_beta=2beta rho^(2beta-2). At beta>=2 these expressions extend continuously to zero on the axis, and the identities hold there and distributionally. The acceleration is -rho^(2beta-1)e_r while grad P_beta=rho^(2beta-1)e_r, so these are also stationary Euler fields. They grow at infinity and are not campaign decaying similarity profiles.

For beta=2, the first derivatives of V_beta are homogeneous of degree one in (x,y), with bounded derivatives off the axis. Integrating on line segments, split at their possible intersection with the axis, proves those first derivatives are locally Lipschitz. On an axis-contained segment they vanish. Thus V_2 is C1,1 and V_2(0)=DV_2(0)=0. But its second component on y=z=0 is x|x|, which has unequal one-sided second derivatives at zero. Therefore V_2 is not C2. Its smooth scalars are H_2=P_2=rho^4/4, so H_2=E_2/4. This is the claimed endpoint regularity counterexample.

For beta>2, derivatives through order two off the axis obey |D^jV_beta|<=C_beta rho^(beta-j). Successive difference quotients give derivatives on the axis, with all derivatives through order two zero there; the displayed bounds make them continuous. Thus V_beta is C2. Given delta>1/4, set delta0=min(delta,1/3) and beta=1/(1-2delta0). Then 2<beta<=3 and H_beta/E_beta=delta0<=delta. This nonzero field satisfies the double-zero, divergence and Poisson hypotheses, but the larger upper ratio. It proves optimality over exactly the stated C2 class. A nonintegral beta is not claimed to give a smooth field of all orders.

Finally V=(-y,x,0), H=0 and P=(x^2+y^2)/2 satisfy the divergence and Poisson equations and the quarter bound, with V(0)=0. This smooth field is nonzero because DV(0) is not zero. It tests the necessity of the second center hypothesis.

## 7. Dependencies, verification and limitations

All seven source sections of LIT313 were read. The calculation above independently checks the distributional center flux with H only C1, the coefficient 7, the epsilon^-7 volume scaling, the C2 Taylor convergence, the forced scalar L1 limit, the full quadratic classification and each counterexample's regularity. No numerical computation or external uniqueness theorem is used.

The endpoint obstruction is stronger than the coarse positive-tensor estimate because it retains the special stress form. It remains a local divergence-Poisson theorem requiring a uniform quarter-ratio bound on the whole ball. Nothing here derives that bound for every actual Euler tail or profile. The existing configured model comparison is recorded below; actual provider execution is independently unattested. No new client, agent or formal build was started.

## 8. Complete coordinator comparison and one wording correction

All eleven items of in the team records and its complete supplied check log were read. Items 1-3 agree with the stress bounds, the C1 center-flux argument and the exact endpoint defect in Section 2. Items 4-5 agree with Sections 3-4, including C2 convergence on compact sets and the nonnegative L1 scalar limit without a fourth derivative. Item 6 agrees with the full algebraic classification in Section 5. Item 7 gives the same whole-ball conclusion. Items 8-10 agree with every power-swirl regularity and missing-derivative countertest in Section 6. Item 11 and wording points L2-L3 preserve the local kinematic scope, the distinction from the separate pressure-only theorem and the fact that existing completion applications already have H/E tending to zero.

The coordinator's wording point L1 contains a typographical mathematical error in its suggested report clause: the endpoint C1,1 example is

    V_2=rho^2 e_theta=rho(-y,x,0),

not `rho e_theta`. Here e_theta=(-y/rho,x/rho,0) off the axis. The latter field is the smooth linear rotation (-y,x,0), has nonzero DV at the center and is the distinct derivative-hypothesis countertest. The comparison's substantive item 9 and the source both use the correct beta=2 field. Thus the error affects the proposed report phrase, not the endpoint theorem or its proof.

The supplied log includes finite-dimensional numerical minimization and prints a positive observed minimum. This is only a sanity check and cannot establish global positivity or uniqueness. Neither the proof nor this verdict uses that optimization: the three exact identities (10) and their product prove the classification exhaustively. The log's display of beta's range as [2,3] is a closed enclosure; the theorem uses the precise range 2<beta<=3 when delta0>1/4.
