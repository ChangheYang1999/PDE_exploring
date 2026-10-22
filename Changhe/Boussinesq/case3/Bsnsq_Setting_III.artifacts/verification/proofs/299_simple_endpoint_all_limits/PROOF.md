# Simple axis endpoints with any prescribed extended ratio limit

Status: complete informal argument, written before the independent symbolic controls. This is a theorem about four local axis relations only. It does not assert a full B2 profile or compatibility with the full-plane inverse.

## Statement and notation

Fix beta > 0, an endpoint y_*, a side epsilon in {-1,1}, and A != 0. Write s = epsilon (y_* - y), so s > 0 specifies the chosen side. Put

    L = 3 beta + 2, M = 2 beta + 1, N = 7 beta + 2.

There are real analytic functions b,T,eta,v,D on a neighborhood of y_* satisfying

    b T_y + (L - 2 b_y) T = 0,
    b eta_y + (M - b_y) eta = T,
    eta = -b_yy - 2 v,
    b D_y + (N - 4 b_y) D = 8 v_y T - 12 v T_y.       (1)

They have b(y_*) = 0, b_y(y_*) = -(3 beta + 2), and a zero of exactly order three for T at y_*. On a sufficiently short chosen side, A/T > 0. For every prescribed R in the extended real line, these functions can be chosen so that

    lim_{s downarrow 0} A D/T^2 = R.                  (2)

All extensions through s = 0 are analytic in the signed variable s; they are not extensions by zero. The positive slope magnitude of b is fixed here as c = 3 beta + 2. The theorem does not prescribe an arbitrary slope. The parameter A is only the sign and ratio factor; no B2 center jet at a distinct point is imposed.

For comparison, any smooth solution of the first relation in (1) with a simple zero of b, with T nonzero on a one-sided punctured neighborhood of y_* and T(y_*) = 0, has a finite positive integer vanishing order for T. Consequently D/T^2 has an extended real limit whenever D is smooth. Thus (2) realizes every possible limit type without creating an oscillatory exception to that conclusion.

## Reduction to an analytic singular system

Set c = L and a = 4 beta + 3. Choose q in {0,1}, C != 0, and ell real, and seek

    B = s(c+x),            b = epsilon B,
    T = s^3 g,             eta = s^3 h,
    v = s^(4-q) w,         D = ell s^(6-q) g^2.       (3)

The desired quotient is exactly D/T^2 = ell s^(-q) for s != 0. Introduce z so that B' = c+z, with primes in this proof denoting differentiation with respect to s. Consider

    s x' = z-x,
    s z' = -epsilon s^4 h - 2 epsilon s^(5-q) w,
    (c+x) s g' = (2z-3x) g,
    (c+x) s h' = (z-3x-a) h - g,
    s w' = delta w + (3/2) w(2z-3x)/(c+x)
            - epsilon ell g [beta-2+q(c+x)]/8,       (4)

where delta = (1+2q)/2. Initial values are

    x(0) = z(0) = 0,       g(0) = C,
    h(0) = -C/a,
    w(0) = epsilon ell C (beta-2+q c)/(4(1+2q)).      (5)

These initial values annul the right side of (4) at s = 0. In particular delta is either 1/2 or 3/2, and c,a are positive.

We check that (4) implies (1). Since d/dy = -epsilon d/ds, b_y = -B' and b_yy = epsilon B''. The first equation of (4) gives B' = c+z. The second then gives B'' = -epsilon s^3 h - 2 epsilon s^(4-q) w, so eta = -b_yy-2v. The T relation in (1) is B T' = (L+2B')T. After substituting T=s^3g and L=c, it is the third equation of (4). The eta relation becomes B eta' = (M+B')eta-T; since 2c-M=a, it is the fourth equation of (4).

For the final relation set J = ell s^(-q) and D=T^2 J. The first relation already checked gives

    b D_y + (N-4b_y)D
      = T^2 [(beta-2)J - B J']
      = ell s^(6-q) g^2 [beta-2+q(c+x)].            (6)

On the other hand direct differentiation gives

    8 v_y T - 12 v T_y
      = epsilon s^(6-q) g
          [4(1+2q)w - 8s w' + 12s w g'/g].         (7)

For small s, g is nonzero because g(0)=C. Substitution of the third and fifth equations of (4) into (7) gives (6). No division by ell is needed, so ell=0 is included.

## Convergent analytic solution of the singular system

The singular factor s in (4) requires an existence argument; a formal coefficient recursion alone would not suffice. Reorder the unknown deviations as

    X = (z, x, g-C, h+C/a, w-w(0)).

After dividing the third and fourth equations of (4) by c+x, write the system as s X' = f(s,X). The function f is real analytic near (0,0), with a holomorphic extension to complex variables there, since c>0. Let A_0 = D_X f(0,0). In this order A_0 is lower triangular: the z row is zero, the x row is z-x, the g row depends on z,x, the h row depends on z,x,g,h, and the w row depends on z,x,g,w. Its diagonal is

    0, -1, 0, -a/c, delta.                          (8)

Let R(s,X) = f(s,X)-A_0 X. The initial balances (5) imply

    R(s,0) = O(s^4),
    D_X R(s,X) = O(|s|+|X|).                        (9)

The second estimate follows from analyticity and D_X R(0,0)=0. The first follows because the only nonzero component of f(s,0) is the z component, -epsilon s^4 h(0)-2 epsilon s^(5-q) w(0), and 5-q is at least four. All constants in this proof may depend on the fixed beta,q,C,ell,epsilon.

For 0<r<=1 the matrix power r^(-A_0), defined by the matrix exponential, satisfies

    ||r^(-A_0)|| <= K_0 r^(-delta)(1+|log r|^m)      (10)

for example with m = 1. The two zero eigenvalues have a nontrivial Jordan block: in the zero-eigenvector equations the x row gives x=z, then the g row gives -C z/c=0, so x=z=0; the h and w rows determine those components from the free g component. The zero eigenspace is therefore one-dimensional. The other eigenvalues in (8) are simple and distinct for beta>0. The factor r^(-delta) can in fact absorb logarithmic growth from the zero block, so no claim that m>=1 is necessary is made. To prove the displayed bound directly, put A_0 in complex Jordan form. A block with eigenvalue lambda contributes r^(-lambda) times a polynomial in log r. All eigenvalues are real and at most delta by (8); changes of basis contribute a fixed constant.

On a closed complex disk |s|<=rho, use the Banach space of vector functions holomorphic in its interior and continuous on its boundary, vanishing to at least order two at zero, with norm

    ||X||_2 = sup_{0<|s|<=rho} |X(s)|/|s|^2.

Define

    F(X)(s) = integral_0^1 r^(-A_0) R(rs,X(rs)) dr/r. (11)

Take a fixed ball ||X||_2<=K. Shrink rho so that every argument in (11) remains in the analytic neighborhood. Equations (9)-(10) show that (11) converges uniformly on the disk, is holomorphic in its interior, and vanishes to at least order two. Explicitly, its value at X=0 has norm at most a constant times

    rho^2 integral_0^1 r^(3-delta)(1+|log r|^m) dr.

For X,Y in the ball, the mean-value estimate for R gives

    ||F(X)-F(Y)||_2
      <= K_1 [rho integral_0^1 r^(2-delta)(1+|log r|^m) dr
              + K rho^2 integral_0^1 r^(3-delta)(1+|log r|^m) dr]
           ||X-Y||_2.                              (12)

These integrals are finite since delta<=3/2. Choose rho small enough that the displayed Lipschitz constant is less than 1/2 and ||F(0)||_2<=K/2. Then F maps the closed ball to itself and is a contraction. Its successive iterates from zero converge in this norm to a unique fixed point X within this ball of functions vanishing to order at least two. Complex conjugation preserves (11) and the ball; uniqueness shows that X is real for real s.

For completeness, the fixed point solves the differential equation. If G(s)=R(s,X(s)), then G=O(s^2) and

    (s d/ds-A_0) integral_0^1 r^(-A_0)G(rs) dr/r
      = [r^(-A_0)G(rs)]_{r=0}^{r=1} = G(s).        (13)

The derivative under the integral is justified on smaller disks by holomorphy and the same bounds. The lower endpoint vanishes because 2-delta>0 in (10). Thus sX'=A_0X+R(s,X)=f(s,X). This proves convergent analytic existence for (4)-(5), with X=O(s^2), not merely existence of a formal series. The solution then satisfies the differential equations at s=0 by continuity as well.

## Limits and scope

The functions (3) are analytic in signed s because all their powers are nonnegative integers for q=0,1. We have B(0)=0, B'(0)=c, and g(0)=C, so b_y(y_*)=-c and T has exactly order three. Taking C of the sign of A makes A/T>0 for small s>0. Given finite R, take q=0 and ell=R/A. Given R=+infinity or -infinity, take q=1 and ell nonzero with the sign of A ell equal to the desired infinity. Formula (3) proves (2).

To justify the comparison statement, write xi=y-y_* and b=xi d(xi), with smooth d(0)=b_1!=0. The first equation of (1), wherever T!=0, gives

    T_y/T = alpha/xi + k(xi),
    alpha = 2-L/b_1,

where k is smooth. Hence on a fixed side T=C_1 |xi|^alpha exp(K(xi)) with C_1!=0 and smooth K. Smoothness, vanishing, and nonzero C_1 force alpha to be a positive integer: a noninteger positive power has a derivative that fails to extend smoothly, a nonpositive power does not vanish, and this formula cannot vanish to infinite order. Thus on the chosen side T=xi^n a_1(xi) with n>=1 and a_1(0)!=0, with a_1 extending smoothly from that side to the endpoint. If D has first nonzero Taylor coefficient of degree j, D/T^2 is a nonzero constant times xi^(j-2n)(1+o(1)), which has an extended real limit on the chosen side. If D is flat, D/xi^(2n)->0. This covers every smooth D.

The only equations imposed here are (1). No full x-Taylor hierarchy, no global transport domain, no center normalization, no far-field class, and no canonical full-plane inverse have been imposed or derived. Thus the result neither constructs nor excludes a full B2 profile. It shows that the four local relations at a simple attracting endpoint do not select a sign or value for A D/T^2, at any fixed beta>0. General B2 remains OPEN.

## Dependencies and verification

The proof above is self-contained apart from elementary complex analytic facts, finite-dimensional Jordan form, and the contraction argument proved by convergence of its iterates. Its four starting relations are explicitly displayed. Independent symbolic checks will be stored in verification/ and implemented under code_independent/ in the lane. No formalization or Lean build is claimed.
