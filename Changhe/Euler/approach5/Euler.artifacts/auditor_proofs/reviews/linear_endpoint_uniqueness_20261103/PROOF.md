# Uniqueness of the fixed-product linear endpoint weight

## 1. Exact statement and data

Let S be a real symmetric trace-free 3 by 3 matrix, W in R3, t=|W|^2, ell=6/5 and M=sqrt(103/100)>0, with Frobenius matrix norm. Put

    K={S: S=S^T, tr S=0, lambda_min(S)>=-ell},
    D_c[a,b,g](S,W)=a|S|^2+b tr S^3
       +(3b/4-2g'(t))W.SW+2g'(t)t-3c g(t)-a t/2.

The exact polynomial p9 and the rational polynomial representatives b*,gam*,x_a,x_c,rho are the coefficient lists in the team records. Coefficients are descending and each rational number is an exact numerator-denominator pair. Define c* to be the unique root of p9 in (447/1000,179/400), and evaluate those five representatives at c*. This is the same defining data as in the team records, A2341-A2344. Their copied inputs have SHA256 6b7c5a6bc68bd5157ee87b4d1baf4e1347d73eb63a402b5b22b6e70c8c4ea1b9. The exact data, not decimal approximations, are part of this statement.

Theorem. At c=c*, for real a>0,b,gamma,

    D_c*[a,b,gamma t]>=0 on K times {|W|<=M}
       if and only if (b,gamma)=a(b*,gam*).

This is uniqueness up to a positive factor in the fixed linear family. The endpoint density is nonnegative, not strictly positive away from the origin. Its uniqueness does not change the already proved strict threshold c<c* or any profile theorem.

## 2. Necessary double-zero equations

The density is linear in a,b,g, so divide by a and assume a=1. Write gamma for the normalized coefficient. Direct evaluation at

    S_a(x)=diag(x,-x/2,-x/2), W=M e1

gives

    f_a(x;b,gamma,c)=(3/2)x^2-M^2/2
       +(3b/4)(x^3+M^2 x)+gamma M^2(2-3c-2x).        (1)

For every 0<=x<=2ell the matrix lies in K, so a nonnegative full density implies f_a(x)>=0 throughout this interval. A second admissible matrix is

    S_c(x)=diag(x,ell-x,-ell), W=M e1,

when -ell<=x<=2ell. Its density is

    f_c(x)=2x^2+ell(x-ell)(3bx-2)
           +M^2[(3b/4-2gamma)x+(2-3c)gamma-1/2].       (2)

The previously verified exact certificate gives 0<x_a<2ell, -ell<x_c<2ell, rho>0 and the identity

    f_a(x_a;b,gamma,c*)+rho f_c(x_c;b,gamma,c*)=0       (3)

for every real b,gamma. This is the three-coefficient affine identity A2341, checked modulo p9 and against the original matrix density. It is a necessary test at actual points of the full product, not only a sufficient reduction of that product.

Nonnegativity at both points and (3) imply f_a(x_a)=f_c(x_c)=0. Since x_a is an interior point of the interval on which the real polynomial f_a is nonnegative, elementary differentiation gives f_a'(x_a)=0. Thus every admissible pair solves the two affine equations

    f_a(x_a;b,gamma,c*)=0, f_a'(x_a;b,gamma,c*)=0.       (4)

## 3. Nonsingularity and existence

The Jacobian of the affine map (b,gamma) to (f_a(x),f_a'(x)) has determinant

    -M^2[(3/2)(x^3+M^2 x)
         +(2-3c-2x)((9/4)x^2+(3/4)M^2)].             (5)

This follows directly from the coefficient of b in (1), (3/4)(x^3+M^2 x), and the coefficient of gamma, M^2(2-3c-2x), together with their derivatives. At x=x_a,c=c*, all terms in the bracket in (5) are positive. Indeed the existing exact enclosures, rechecked by rational inequalities, give

    0<x_a<1/4<2ell,
    2-3c*-2x_a>1743/10000>0.

A simpler sufficient bound would follow already from c*<179/400 and x_a<1/4, giving a lower bound 63/400. Hence the determinant is strictly negative. The two affine equations (4) have at most one solution.

The known pair (b*,gam*) is a solution: the exact endpoint factorization from A2341 is

    f_a(x;b*,gam*,c*)=(3b*/4)(x-x_a)^2(x-r),
    r=-2/b*-2x_a<0.

The new check also directly verifies both values in (4) as zero in Q[c]/(p9). It follows that (b,gamma)=(b*,gam*) is the unique normalized possible pair. Conversely A2342 proves D_c*[1,b*,gam*t]>=0 on the entire matrix-vector product. Multiplying this density by any a>0 proves sufficiency for (a,ab*,agam*). This completes both directions of the theorem.

## 4. Verification, dependencies and limits

The entire source Remark SF.14, its earlier C67 dependencies, the full new source checker and its complete log were read. The independent exact check imports the already verified JSON coefficient lists and rational root enclosure, reconstructs determinant (5), verifies its polynomial identity, proves the interior and positive-gap inequalities, verifies both double-zero equations modulo p9, and records an exact negative upper bound for the determinant. It passed in0.1194215496070683 actual seconds, from2026-11-03T21:24:02.899002+00:00 to2026-11-03T21:24:03.018422+00:00, on CPU55 at nice19 with OMP1. Its plan, code, dependency hashes, rational bounds and zero remainders are retained. No source resultant elimination, sampled optimizer or floating-point stage was run.

The algebraic dependencies are precisely A2341's endpoint definitions, root enclosure, affine identity and factorization, and A2342's nonnegative full-product density. Their full independent proof was reread. No pressure, integration by parts, characteristic completeness or profile regularity premise enters this uniqueness theorem.

This resolves only the endpoint-uniqueness item in A2346 for this pair and this linear multiplier family. Uniqueness or optimality for nonlinear g, other strain-vorticity products, deduction of either global bound from decay, and unrestricted smooth rotating-profile nonexistence remain open. The endpoint still fails the strict SF.3 condition, since its density vanishes at the two displayed nonzero product points.
