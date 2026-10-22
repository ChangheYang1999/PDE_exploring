# A stable ordinary-moment formula for the constant of a serialized inverse

Written 2026-10-21T00:12:46.612769+00:00. Complete derivation before numerical checking. The formula is a property of a specified source and its canonical inverse. It is not a certificate for either transport equation.

## 1. Statement

Let2<b<3, L>0, s=1/b and t=1-z, z=(1+r^2/L^2)^(-1/(2b)). Consider a locally bounded, x-odd source of the finite representation from packet89,

    Omega(r,theta)=r cos(theta) z^(b+1)
          sum_(n=0)^(K-1) C_n(t) T_n(-sin(theta)) rho_n(r),
    rho_n(r)=1 for n even, rho_n(r)=r/sqrt(L^2+r^2) for n odd.

Assume each C_n is C^2 on[0,1], polynomial on finitely many subintervals, including the last. T_n denotes the Chebyshev polynomial of the first kind. The finite representation is continuous at the origin, with value zero, because its angular factors and coefficients are bounded and it has the factor r. This is enough for the ordinary and relative velocity integrals below. No claim of full Cartesian smoothness at the origin is made for arbitrary serialized higher angular modes. Put S(t)=C_0(t)-C_2(t)/2, with C_2=0 if absent. Let omega0 and omega1 be the first two actual homogeneous source terms of degrees-s and-2s in its exterior expansion, extended homogeneously on every r>0 without a cutoff. Their velocities u0,u1 use the same canonical relative inverse. Then eta=Omega-omega0-omega1 has an ordinary, absolutely convergent velocity U_eta at every point including0. Its centered full-plane inverse satisfies

    V=u0+u1+C+O(r^(1-3s)),    C=(0,C2),
    C2=-b L^2/[2(b-1)(b-2)]
          *[S'(0)-(b-2)S(0)+integral_0^1(1-t)^(2-b) S''(t)dt].   (1)

The integral in(1) is convergent, since2-b>-1. The source need not solve a PDE. For an exact B2 profile with basis equal to beta=b, packet90 further requires its first two actual tails to equal the transport-determined tails, and then the representation restriction forces this C to vanish. Measuring(1) for a nonprofile cannot replace checking those prerequisites or either PDE.

## 2. Reduction to a convergent first-mode radial integral

The source has exterior remainder O(r^-3s) after the first two terms, with differentiated bounds in the exterior only, and eta=O(r^-2s) near0. Thus U_eta and its value at0 converge absolutely, by2s<1<3s<3/2. The range1<3s<3/2 gives the value bound by the three-region absolute-kernel estimate without a logarithm. Also, the third stream degree2-3s lies strictly between1/2 and1, so no angular harmonic resonance occurs. The argument of packet90 gives V=u0+u1+U_eta-U_eta(0), U_eta=O(r^(1-3s)), and C=-U_eta(0). Parity makes C vertical.

Orthogonality gives the first cosine coefficient of Omega as

    q(r)=r z^(b+1) S(t).

Indeed (1/pi)int cos(theta)^2 T_n(-sin(theta))dtheta is1 for n=0,-1/2 for n=2, and0 for every other n. The odd rho_n are radial and do not affect the zero coefficients. The first cosine coefficients of omega0,omega1 are

    B0 r^-s, B1 r^-2s,
    B0=L^(1+s)S(1), B1=-L^(1+2s)S'(1).

Since K_2(-Y)=Y_1/(2pi|Y|^2), angular integration gives the absolutely convergent formula

    C2=-1/2 integral_0^infinity[q(r)-B0 r^-s-B1 r^-2s]dr.        (2)

When a nonzero homogeneous tail is present, the combined integral must not be evaluated by subtracting separately divergent improper integrals. If both B0 and B1 vanish, q is itself integrable, as in the j>=2 examples below.

## 3. Exact cancellation and two integrations by parts

Under the radial map, r dr=-b L^2 z^(-2b-1)dz, so the truncated integral of q is bL^2 int_(z_R)^1 z^-b S(1-z)dz. Put f(z)=S(1-z), f0=S(1), f1=-S'(1), and R_f(z)=f(z)-f0-f1 z. Since R_f=O(z^2), its weighted integral is finite. Subtract the two explicit homogeneous primitives from(2) at a finite upper radiusR and letR tend to infinity. For j=0,1,

    z_R^(j+1-b) - (R/L)^((b-j-1)/b) ->0,

because expansion of(1+L^2/R^2)^((b-j-1)/(2b)) makes the difference O(R^((b-j-1)/b-2)). Consequently the bracket integral in(2) divided by bL^2 is exactly

    J=int_0^1 z^-b R_f(z)dz+f0/(1-b)+f1/(2-b).               (3)

This is a derived finite-part expression for an already convergent combined integral, not a redefinition of the inverse.

Twice integrate by parts on R_f, which has zero value and first derivative at0. Its discarded endpoint terms at0 have orders z^(3-b), which tend to0. The boundary terms at1 and the explicit terms in(3) simplify to

    J=f(1)/(1-b)-f'(1)/[(1-b)(2-b)]
                       +int_0^1 z^(2-b)f''(z)dz/[(1-b)(2-b)].

There are no internal jump terms because f and f' are continuous. Substituting f(1)=S(0), f'(1)=-S'(0), and f''(z)=S''(1-z) proves(1). This form avoids subtraction of the two growing far-field moments at a large radius. It does not remove genuine conditioning as b approaches either endpoint2 or3.

## 4. Exact manufactured values and the role of a source sign

For S(t)=(1-t)^j with integer j>=0, the formula becomes

    C2=-b L^2/[2(j+1-b)].                                (4)

For j=0,1 this follows from(3) directly. For j>=2 the integral of q itself converges, and the map gives bL^2 int_0^1 z^(j-b)dz=bL^2/(j+1-b). Thus(4) is independently obtained in all cases used to test(1).

In particular the sources with all other modes zero and S(t)=1+d(1-t)^2, d>=0, are globally smooth and strictly positive on x>0. Their first homogeneous tail is fixed and nonzero, their second is zero, and

    C2=bL^2/[2(b-1)]-d bL^2/[2(3-b)].

Hence d=(3-b)/(b-1)>0 makes C2=0; d below or above it gives either sign. These are explicit smooth inverse sources, not profiles: their center strain is0, which fails the B2 center condition c=1+b/2: a pure first-cosine source has zero second-sine strain moment, and its stream has the form x times a smooth radial function, whose xy derivative vanishes at0. The example proves only that positivity of vorticity alone cannot force a nonzero C of one sign.

## 5. Numerical evaluation and scope

An independent implementation evaluates(1) with the serialized source coefficients and checks multiple quadrature orders. It uses Gaussian quadrature on ordinary spline cells and a Jacobi weight on the last cell, where the weight has its integrable power singularity. Exact formulas(4) give manufactured checks. Archived coefficients and source choices are recorded separately. Floating-point quadrature is supplementary numerical evidence, not an interval certificate. No Lean or Lake build is performed, and no full B2 endpoint follows.
