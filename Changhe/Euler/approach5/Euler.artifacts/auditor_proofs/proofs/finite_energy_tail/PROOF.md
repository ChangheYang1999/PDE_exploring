# Finite energy of the difference from the Dini scattering tail

## Statement and scope

Let J(y1,y2,y3)=(-y2,y1,0), A=cI-omega J, and B(y)=Ay+U(y). Suppose

    U in C^2(R^3;R^3), P in C^1(R^3), div U=0,
    (1-c)U+(B.grad)U+omega JU+grad P=0,
    U is bounded and U(R .) tends to 0 in distributions as R tends to infinity,
    integral_1^infinity [sup_{|y|>=r}|DU(y)|] dr/r < infinity.

Assume 2/5<c<3/5 and any finite real omega. Put k=(1-c)/c, alpha=3-2k=5-2/c, and q=|U|^2/2. Thus 2/3<k<3/2 and alpha>0. Let V be the scattering tail constructed in the already checked Theorem T (A210), and F its restriction to the unit sphere. Define W=U-V away from the origin, assigning any value at the origin.

Then W and (U.grad)U belong to L^2(R^3), and

    (5c-2) ||W||_2^2 = 2 N,
    N = integral U_i U_j partial_j V_i
      = integral W . (U.grad)U.

Both displayed integrals are absolutely convergent. In particular

    ||W||_2 <= 2 ||(U.grad)U||_2/(5c-2).

If E(R)=integral_{B_R}|U|^2 and A_F=integral_{S^2}|F|^2, then

    E(R) - (A_F/alpha) R^alpha tends to 0,
    integral_{B_R} V.W tends to -||W||_2^2/2.

For nonzero U, N>0 and W is nonzero. For every rho>0,

    ||W||_{L^2(B_rho)} >= (A_F rho^alpha/alpha)^(1/2)
                          - ||U||_infinity (4 pi rho^3/3)^(1/2).

This confirms Theory Agent A Proposition T.7 with its extra Dini hypothesis. It is a necessary identity for a hypothetical profile, not a nonexistence result. Constants in the estimates below may depend on the profile, c, omega and its Dini bound. No uniform bound in those data is asserted.

## Dependencies, with their exact content

A210, in the team records, supplies a continuous V off zero and a continuous curl V there, with

    V(e^{sA}y)=e^{-(1-c)s} Q_s^T V(y), Q_s=exp(omega sJ),
    curl V(e^{sA}y)=e^{-s} Q_s^T curl V(y),
    div V=0 and curl V=Omega_tilde in distributions on all R^3,
    LV=0 away from zero, L=(1-c)+(Ay.grad)+omega J,
    U-V=o(|y|^{-k}) uniformly at infinity,
    |Omega(y)| <= C |y|^{-k-1} at infinity.

It also proves F is nonzero whenever U is nonzero. These are the only scattering inputs. The canonical-pressure and energy estimates A031, A040, A052 and A229 give, under the resulting natural bound |U(y)|<=C(1+|y|)^{-k}, constants p_R with

    ||P-p_R||_{L^2({R<|y|<2R})} <= C R^{3/2-2k}, R>=1,
    (R^{-alpha} E(R))' = -(2/c) R^{-1-alpha} F_E(R),
    F_E(R)=integral_{|y|=R} (q+P-p) U.n,
    |R^{-alpha}E(R)-L_energy| <= C R^{-1/c}.

The last estimate uses the natural decay in the uniform-decay refinement of Theorem A, rather than merely its O(1/R) version. Pressure itself has no decay or normalization hypothesis. Constants may be subtracted on individual annuli because div U=0.

## Local regularity and the singular origin

The polar map y=e^{sA}w, |w|=1, rotates each sphere and changes its radius by e^{cs}. Consequently

    |V(y)| <= ||F||_infinity |y|^{-k},
    integral_{B_R}|V|^2 = (A_F/alpha) R^alpha.                 (1)

In particular V is locally square integrable at zero. To justify differentiating V, split Omega_tilde into its parts inside and outside the unit ball. They belong respectively to L^{p1} and L^{p2}, where

    1<p1<3c<p2<3.

This is possible throughout the asserted range. Biot-Savart and the L^p boundedness of its gradient give DV in L^{p1}+L^{p2}, hence in L^1 locally. Differentiation of the distributional homogeneity gives, almost everywhere,

    DV(e^{sA}y)=e^{-s} Q_s^T DV(y) Q_s,
    integral_{R<|y|<2R}|DV|=R^{2-k} integral_{1<|y|<2}|DV|. (2)

Thus every product rule used below is valid on a compact annulus. Inner boundary terms will be estimated separately. No unproved differentiability of the angular function F is used.

## Cross identity and absolute convergence

Using the two linear equations, cancellation of the skew matrix J, and both divergence identities gives

    div[B(U.V)+(P-p)V]=(5c-2)U.V+U_i U_j partial_j V_i.       (3)

The vector on the left is continuous away from zero. It is O(|y|^{-k}) near zero for each fixed p, while its divergence is locally integrable. Its inner spherical flux is O(epsilon^{2-k}), hence tends to zero. With

    X(R)=integral_{B_R}U.V,
    N(R)=integral_{B_R}U_i U_j partial_j V_i,
    b(R)=integral_{|y|=R} [(U.n)(U.V)+(P-p)V.n],

integration of (3) gives

    c R X'(R)-(5c-2)X(R)=N(R)-b(R).                         (4)

One may first integrate with smooth radial cutoffs and obtain the identity almost everywhere in R. The continuous surface integrals and the continuous cumulative volume integral then extend it to every positive R. The flux of V through every sphere is zero, because div V=0 on all of R^3 and V is continuous off zero. Thus b is independent of p.

Near zero the integrand defining N is bounded in absolute value by ||U||_infinity^2 |DV|, which is integrable. On a dyadic annulus of radius R>=1, (2) gives

    integral |U|^2 |DV| <= C R^{2-3k}.                      (5)

Since k>2/3, these bounds are summable. Therefore N(R) tends to the absolutely convergent integral N.

## The radial remainder equation, without assuming finite energy

Set G(R)=integral_{B_R}|W|^2, finite for each R by (1). Combining (1), (4) and the energy identity gives

    (R^{-alpha}G(R))'
      =-(2/c)R^{-1-alpha}[F_E(R)+N(R)-b(R)].                (6)

The uniform little-o tail implies R^{-alpha}G(R) tends to zero. Indeed, for any fixed large r,

    G(R)<=G(r)+sup_{|y|>=r}(|y|^k|W(y)|)^2
                   (4 pi/alpha) R^alpha, R>=r.

Take R to infinity and then r to infinity. This uses no global integrability of W.

On [R,2R] choose the same p_R in both surface fluxes. The pressure estimate, Cauchy-Schwarz on the annulus, and |U|+|V|<=C R^{-k} there give

    integral_R^{2R} (|F_E(r)|+|b(r)|) dr <= C R^{3-3k}.     (7)

It follows by dyadic summation that

    R^alpha integral_R^infinity r^{-1-alpha} (|F_E|+|b|)dr
      <= C R^{2-3k} tends to zero.                         (8)

Here 2-3k-alpha=-1-k<0 ensures convergence of the weighted series. The N term is integrable because N(R) is bounded and alpha>0. Integrating (6) from R to infinity is therefore legitimate and yields

    G(R)=(2/c)R^alpha integral_R^infinity
                       r^{-1-alpha}[F_E(r)+N(r)-b(r)]dr.

The N contribution tends to 2N/(c alpha), and (8) disposes of both boundary contributions. Since G is nondecreasing, this proves W in L^2 and

    (5c-2)||W||_2^2=2N.                                   (9)

The proof has not assumed the conclusion at any step.

## The nonlinear term and integration by parts

For a smooth cutoff chi supported in {R/2<|y|<4R}, equal to one on the radius-R annulus, the compactly supported div-curl identity implies

    ||DU||_{L^2({R<|y|<2R})}
      <= C [||Omega||_{L^2({R/2<|y|<4R})}
              +R^{-1}||U||_{L^2({R/2<|y|<4R})}]
      <= C R^{1/2-k}.

Thus

    ||(U.grad)U||_{L^2({R<|y|<2R})}^2 <= C R^{1-4k}.

The dyadic series converges already for k>1/4, so it converges here. On the unit ball the nonlinear term is bounded. Hence it belongs to L^2 globally.

Integrate U_i U_j partial_j V_i by parts on B_R minus B_epsilon, substituting V=U-W. The pure U derivative has outer flux integral q U.n=O(R^{2-3k}). The W boundary term is also O(R^{2-3k}) at infinity and O(epsilon^{2-k}) at zero. All tend to zero. W.(U.grad)U is absolutely integrable by the newly proved L^2 properties. Therefore

    N=integral W.(U.grad)U.

Cauchy-Schwarz in (9) proves the asserted norm bound, with the zero-W case interpreted directly.

For comparison, the second proof in T7.5 can also be made without circularity. Before knowing W in L^2, its natural pointwise bound gives ||W||_{L^2(A_R)}<=C R^{3/2-k}. Paired with the preceding nonlinear bound, it gives an annular absolute integral O(R^{2-3k}) for W.(U.grad)U. The remainder-energy identity then replaces (6). This independent summability is the step that must precede any use of global L^2. The revision at 22:51Z includes the separately necessary proof of absolute convergence of N.

## Renormalized energy and nonzero remainder

From (1) and W in L^2,

    E(R)=(A_F/alpha)R^alpha+2 integral_{B_R}V.W+G(R),
    |integral_{B_R}V.W|<=C R^{alpha/2}||W||_2.

Hence L_energy=A_F/alpha. The refined energy estimate from the dependencies gives

    E(R)-L_energy R^alpha=O(R^{alpha-1/c})
                          =O(R^{5-3/c})=o(1),

because c<3/5. Substitution into the preceding exact expansion proves the limit of integral V.W.

For nonzero U the checked scattering theorem gives A_F>0. The triangle inequality in L^2(B_rho) proves the quantitative lower bound. Its right side is positive for sufficiently small rho because alpha<3. Therefore W is nonzero and N>0 by (9). The argument uses an integral bound near the singular origin, not a pointwise singularity on a set of measure zero.

## Verification and limitations

All powers, both inner and outer fluxes, pressure-constant independence, and the alternative proof's order of dependencies have been checked. No computation was needed. The upper endpoint c=3/5 is excluded for absolute convergence of N and vanishing of the unweighted energy correction; the lower endpoint c=2/5 is excluded for local square integrability of a nonzero V. The Dini hypothesis is additional to the campaign's decay assumption. Positivity of N in (9) supplies no contradiction without a separate sign estimate.
