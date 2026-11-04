# Independent audit of the axisymmetric quadratic pressure optimum

Status: all eight LIT322 source sections read; independent reconstruction and complete existing coordinator comparison finished. Source pinned in the team records. This is an optimum in a restricted polynomial Poisson class, not an Euler profile theorem.

## 1. Statement, notation and exact root

Let Q be a nonzero homogeneous quadratic polynomial vector field on R3, divergence-free and equivariant under rotations about the z-axis. Let P be any homogeneous quartic polynomial with -Delta P=tr((DQ)^2). Among such pairs satisfying P>=g|Q|^2 everywhere, the maximal coefficient is the unique root g_star in [0,1/4] of

    F(g)=96g^4+16g^3-23g^2-6g+1.

It satisfies 2/17<g_star<1/8. Put

    t_star=(1-3g_star)/(8g_star(1-2g_star)),
    B_star=(3+8g_star+4g_star t_star)/(1-2g_star).

Up to multiplying Q by any nonzero real scalar and P by its square, every attaining pair for this fixed axis is

    Q=(z(x-b y),z(y+b x),-t_star(x^2+y^2)-z^2),
    b=+sqrt(B_star) or -sqrt(B_star), P=g_star |Q|^2.

No rotational symmetry of P is assumed. The root bounds follow from

    F(2/17)=1689/83521>0, F(1/8)=-7/128<0.

On [0,1/4], F'=384g^3+48g^2-46g-6<=144g^2-46g-6<=-10g-6<0, proving existence and uniqueness there. The constants g_star, t_star and B_star are positive.

## 2. Exhausting the equivariant velocity and averaged pressure families

Write u=x^2+y^2 and v=z^2. The half-turn sends each horizontal component to its negative, so its quadratic monomials must be z times x or y. Its horizontal linear map must commute with every planar rotation, so it is aI+bJ. The invariant vertical quadratic is cu+dz^2. Divergence is 2(a+d)z, hence d=-a. Thus the whole family is

    Q=(azx-bzy,azy+bzx,cu-az^2), a,b,c in R.

Differentiation gives

    E=|Q|^2=c^2 u^2+(a^2+b^2-2ac)uv+a^2 v^2,
    tr((DQ)^2)=4ac u+(6a^2-2b^2)v.

For example, the horizontal 2 by 2 block contributes 2(a^2-b^2)v, the vertical diagonal contributes 4a^2v, and the axial off-diagonal pairs give 4ac u, with the b terms cancelling.

Average P over planar rotations. The energy and Poisson source are invariant, so the averaged Pbar has the same equation and preserves the lower bound. An invariant quartic has the form A u^2+C uv+D v^2. Since Delta u^2=16u, Delta(uv)=2u+4v and Delta v^2=12v, the equation is equivalent to

    C=-2ac-8A,
    D=b^2/6-a^2/2+(2/3)ac+(8/3)A.

This reduction is valid for an upper bound on every original P, not merely symmetric ones.

## 3. Positivity and the universal one-quarter bound

A polynomial alpha u^2+h uv+delta v^2 is nonnegative on u,v>=0 precisely when alpha,delta>=0 and h+2sqrt(alpha delta)>=0. The axes give the first two inequalities. Completing the square gives sufficiency. If both diagonal coefficients are positive, substituting sqrt(alpha)u=sqrt(delta)v gives necessity; if either is zero, varying the other coordinate forces h>=0. This covers all degenerate cases.

Sphere moments give

    15<E>=8c^2+5a^2+2b^2-4ac,
    60<Pbar>=2b^2-6a^2-8ac.

Thus

    15(<E>-4<Pbar>)=8(c+a/4)^2+(21/2)a^2>=0.

Since Q is nonzero, <E>>0, and Pbar>=gE implies g<=1/4. It is enough to exclude g>g_star in [g_star,1/4]. In that interval,

    48g(1-2g)>48(2/17)(13/17)=1248/289>1.

Indeed g(1-2g) is nondecreasing up to 1/4 and g_star>2/17. Hence for alpha,delta>=0,

    -8(1-2g)alpha-6g delta+2sqrt(alpha delta)<=0,

with equality only at alpha=delta=0. The negative is a positive definite quadratic in sqrt(alpha),sqrt(delta), with determinant 48g(1-2g)-1>0.

## 4. The a=0 branch and the normalized a!=0 branch

If a=0, set alpha=A-gc^2, delta=D and h=C-gb^2 for the pressure defect. Positivity gives alpha,delta>=0. The pressure relation gives b^2=6delta-16A and C=-8A, so

    h+2sqrt(alpha delta)=-8g(1-2g)c^2
      -8(1-2g)alpha-6g delta+2sqrt(alpha delta).

By Section 3 the right side can be nonnegative only when c=alpha=delta=0. Then A=b=0 and Q=0, a contradiction. No a=0 nonzero field attains or exceeds g_star.

If a!=0, replace Q by Q/a and Pbar by Pbar/a^2, which preserves the equation and ratio. Write c=-t and B=b^2>=0. Then

    E=t^2u^2+(1+B+2t)uv+v^2,
    C=2t-8A, D=B/6-1/2-(2/3)t+(8/3)A.

For the defect set alpha=A-gt^2, delta=D-g, h=C-g(1+B+2t). Solving the D equation gives

    B=3+6g+4t-16gt^2+6delta-16alpha.

Substitution, without estimates, gives

    h+2sqrt(alpha delta)=S(t,g)
      -8(1-2g)alpha-6g delta+2sqrt(alpha delta),
    S(t,g)=2[(1-3g)t-4g(1-2g)t^2-2g-3g^2].

We allowed every real t in taking the following maximum, so no extra sign restriction on c or B is inserted into the upper bound.

## 5. Exact maximum and all equality conditions

The concave quadratic S has unique maximizer t(g)=(1-3g)/(8g(1-2g)). Completing the square gives

    max_t S(t,g)=F(g)/(8g(1-2g)).

This follows by expanding (1-3g)^2-(32g^2+48g^3)(1-2g)=F(g). For g>g_star the maximum is negative; the defect cannot be nonnegative. At g=g_star, positivity and the strictly negative correction in Section 3 force t=t_star, alpha=delta=0 and h=0. Thus Pbar=g_star E.

The z^2 coefficient of Delta(g_star E)=-tr((DQ)^2) now gives

    g_star(16+4B+8t_star)=2B-6,

so B=B_star. Conversely that definition verifies this coefficient. The other coefficient equation is

    g_star(16t_star^2+2+2B_star+4t_star)=4t_star.

After multiplying by 1-2g_star and dividing by four, it becomes

    4g_star(1-2g_star)t_star^2+(3g_star-1)t_star
      +2g_star+3g_star^2=0,

which is exactly S(t_star,g_star)=0. Thus the displayed pair attains the optimum. B_star>0 and t_star>0 follow from 0<g_star<1/8.

For the original pressure P, the defect P-g_star E is nonnegative and its rotational average is zero at every point. A continuous nonnegative function on each compact rotation orbit with zero integral is zero everywhere on that orbit. Thus P=g_star E, including before averaging. This proves the full equality classification, not merely the classification of averaged pressures.

## 6. Normalization and exclusion from the profile class

The energy is t_star^2u^2+(1+B_star+2t_star)uv+v^2, with positive coefficients. The vertical component -t_star u-v itself already excludes every velocity zero except the origin. Its sphere mean is

    M=(8t_star^2+5+2B_star+4t_star)/15>0.

The pair Q/sqrt(M), P/M is feasible in the all-quadratic definition, so Gamma2>=g_star. This is only a lower bound there. In particular g_star<1/8<1/6 does not give Gamma2<=1/6.

For every equivariant quadratic, DQ(Jx)=JQ and DQ(x)=2Q. At any similarity exponent c_l>0 the full rotating residual is (1+c_l)Q+DQ Q+grad P. The first part has degree two and the others degree three. Restricting to tx and letting t tend to zero after division by t^2 prevents this residual from vanishing on an open ball for nonzero Q. This holds for every real omega.

For the attaining normalized-a field on the axis, Q=(0,0,-z^2), DQ Q=(0,0,2z^3), and grad P=(0,0,4g_star z^3). The stationary residual is nonzero for z!=0. Nonzero degree-two homogeneity also excludes decay. Scalar multiples preserve the same conclusions.

## 7. Verification boundary

All identities were checked by hand from the complete source, including the a=0 branch, both degenerate positivity cases, the exact root signs, and the equality-before-averaging argument. No symbolic or numerical computation was needed for this reconstruction. The source's separate computation is not a dependency and has not been rerun here. The complete existing coordinator comparison is recorded in Section 8, and designated verdicts are in the auditor's ledger (AUDIT_LEDGER.md). Existing configured model file collaboration only; actual provider runtime independently unattested.

## 8. Completed coordinator comparison

All nine coordinator comparison items, both wording points and the entire 42-check log were read. They agree with Sections 1-7, including the a=0 case, the degenerate quadrant criterion, the strict negative-definite correction, and the equality conclusion for the original unaveraged pressure. The two proofs of monotonicity of F are equivalent. The new cross-check 15(<E>-4<Pbar>)=105<(Q.n)^2> is exactly the already confirmed radial stress identity, not an extra hypothesis.

Here "axisymmetric" means equivariant under every rotation about the given axis, with a swirl component allowed; no reflection symmetry is imposed. A rigid orthogonal change of coordinates gives the same pressure optimum for any chosen axis, since it preserves divergence, the Poisson equation and the Euclidean norm. The profile residual in Section 6 is explicitly computed with that axis as the rotation axis.

This is only a restricted-family upper bound and an all-quadratic lower bound. The exact conclusion is 2/17<g_star<=Gamma2, with g_star<1/8<1/6. A quadratic velocity giving a coefficient greater than 1/6 must therefore lie outside the equivariant family, but the existence of such a velocity remains open. The numerical root, sampled ratios and symbolic checks are corroboration and were not rerun or used in the proof. The existing coordinator is configured as model; actual provider execution remains independently unattested. No new client or computation was used.
