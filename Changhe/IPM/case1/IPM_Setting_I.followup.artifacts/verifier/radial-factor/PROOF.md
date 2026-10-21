# Radial density factors and finite warped angular bases

Date: 2026-10-20. Status: proved restricted nonexistence and proved representation rigidity. These statements do not exclude a general smooth-center IPM profile or a convergent sequence of approximate profiles.

## Radial-factor statement

Let rho(x,y)=x^2 y b(r), r=sqrt(x^2+y^2), with b radial, b(0)=1, smooth as a function of r^2 near zero, and sufficiently regular away from zero for rho to belong to C^(2,alpha)_loc. Suppose rho and its gradient obey the admissible sublinear bounds with some gamma<1. Give rho its canonical full-plane velocity U=(-psi_y,psi_x), -Delta psi=rho_x, with no freely added harmonic strain. Then no constant c_l>1 makes (c_l X+U).grad rho=rho on a neighborhood of zero.

Only the radial-factor restriction is extra. The statement is not a theorem for factors with general angular dependence. The proof uses the full-plane law, including decay of b at infinity.

## Canonical angular inverse

Write

    rho=h(r)(sin theta+sin 3theta), h=r^3 b/4.

Differentiation gives

    rho_x=(r^2 b+r^3 b'/4)sin 2theta+(r^3 b'/8)sin 4theta.

Thus psi=S(r)sin 2theta+T(r)sin 4theta. For source mode f_n, the regular-at-zero and canonical-at-infinity radial solution is

    psi_n(r)=(1/(2n))[r^(-n) int_0^r f_n(s)s^(n+1)ds
                          +r^n int_r^infinity f_n(s)s^(1-n)ds].

Direct differentiation verifies -psi_n''-psi_n'/r+n^2 psi_n/r^2=f_n. The sublinear density and gradient assumptions imply b=O(r^(gamma-3)), b'=O(r^(gamma-4)) at infinity, by evaluating rho and its radial derivative on a fixed nonaxis ray. The integrals above converge and admit the integrations by parts used next. Their difference from another regular solution would consist of harmonic r^n terms; the full-plane velocity growth excludes those for n>=2.

For n=4 the formula simplifies exactly to

    T(r)=-(1/8) r^(-4) int_0^r s^7 b(s)ds.

Indeed the exterior integral is (b(infinity)-b(r))/8=-b(r)/8 before the overall factor 1/8; integration by parts in the interior cancels its endpoint b(r). In particular T=-r^4/64+O(r^6).

For n=2, the coefficient of r^2 is (1/8) int_0^infinity s b(s)ds. Define c=(1/4) int_0^infinity s b(s)ds, so U_linear=(-cx,cy). Since the leading mode-2 forcing is r^2, its particular solution is -r^4/12. Hence

    S=(c/2)r^2-r^4/12+O(r^6).

These signs and constants are checked below both algebraically and by the independent real-space inverse on a Gaussian field.

## Highest angular transport equation

In polar coordinates U_r=-psi_theta/r and U_theta=psi_r. In the transport residual, the coefficient of sin 7theta comes only from interaction of the third density mode with the fourth streamfunction mode. It is

    (3 h T'-4 T h')/(2r).

The dilation term and the second streamfunction mode have no seventh harmonic. Consequently an exact transport solution must satisfy 3hT'-4Th'=0 for all sufficiently small positive r. Since b(0)=1, h is positive there. The equation says that T/h^(4/3) is constant. Its limit at zero fixes the constant, yielding

    T=-r^4 b^(4/3)/64.

On the other hand differentiation of the canonical integral gives

    T'=-4T/r-r^3 b/8.

Combining the last two identities gives r b'/b=6(b^(-1/3)-1). For u=b^(1/3), this becomes r u'=2(1-u). Every solution has u=1+C/r^2. Boundedness and b(0)=1 force C=0. Thus b is identically one near zero.

## Contradiction at degree five

If b=1 on that neighborhood, its canonical streamfunction there is exactly

    psi=c xy-xy(11x^2+5y^2)/48.

The quartic polynomial follows from -r^4 sin2theta/12-r^4 sin4theta/64. Therefore

    U=(-cx,cy)+((11x^3+15xy^2)/48,(-33x^2y-5y^3)/48).

The degree-three transport coefficient is 3c_l-c-1. If it vanishes, the remaining residual is still

    -11 x^4 y/48+25 x^2 y^3/48,

which is not identically zero. If it does not vanish, transport already fails at degree three. This proves the radial-factor theorem.

As an independent jet check, write b=1+b_1 r^2+O(r^4) and impose c=3c_l-1. With A=2c_l-1 the linear field at this center is diag(-A,2A+1), not the source matrix diag(A,1). The two degree-five residual coefficients are

    -2A b_1-11/48,   (4A+2)b_1+25/48.

Together they allow only A=11/3, b_1=-1/32. However the seventh angular coefficient at degree seven is b_1/160, so it cannot vanish. This supplies a second finite-jet contradiction consistent with the exact harmonic argument.

## Rigidity of a finite warped tensor representation

Fix 0<|beta|<1 and theta=s+(beta/2)sin2s on [0,pi/2]. Let

    B(q,s)=sum_(j=0)^N q^j sum_(m=0)^M B_jm cos(2ms).
    a(r,theta)=P(r^2) B(q(r^2),s(theta)),

where P and q are real analytic near zero, P(0) is nonzero, q(0)=0 and q'(0) is nonzero. If a extends to an even-in-x, even-in-y C^infinity function near (0,0), then every coefficient B_jm with m>=1 vanishes. Thus this finite representation is radial wherever its formula is used. In fact C^(2N) regularity together with continuity suffices for the argument.

First prove an angular intersection fact. A finite cosine polynomial in s cannot also be a nonconstant finite cosine polynomial in theta. Put z=exp(2is). A cosine polynomial in s is a Laurent polynomial in z. On the other hand,

    exp(2i theta)=z exp((beta/2)(z-z^(-1))).

A nonconstant finite cosine polynomial in theta contains a highest term indexed by J>=1. As a holomorphic function on C excluding zero, it is a finite sum of

    z^j exp(j beta(z-z^(-1))/2)
    and z^(-j) exp(-j beta(z-z^(-1))/2).

Equality on an arc of the unit circle implies equality throughout this connected domain by the identity theorem. On the positive real axis at infinity, the highest J term of the growing sign dominates every lower exponential and every Laurent polynomial. Its coefficient is nonzero, a contradiction. This works for either sign of beta, choosing the growing sign. Thus the intersection consists of constants.

Now expand a in r^2. Its coefficient at each order l is a finite cosine polynomial in s. Smoothness and the two Cartesian parities make the corresponding homogeneous Taylor polynomial a linear combination of x^(2i)y^(2l-2i), so its angular part is a finite cosine polynomial in theta. The intersection fact makes this angular part constant. At l=0, continuity gives the same conclusion. Since P(0) and q'(0) are nonzero, the relation between the first N+1 radial coefficients of a and B_0(s),...,B_N(s) is triangular with nonzero diagonal. Induction makes every B_j constant. This proves the representation statement.

For the nodal candidates, P=(1+r^2/L^2)^((k-3)/2) and q=1-(1+r^2/L^2)^(-(1-k)/2), with k=1/c_l in (0,1), meet these hypotheses. Their finite radial interpolant and finite warped cosine interpolant have exactly the form above. Consequently an individual field in this fixed warped basis could be smooth at the center only if its factor were radial; the preceding radial-factor theorem then excludes an exact canonical transport solution in that smooth subclass.

## Scope and dependencies

The finite-basis conclusion is about an individual finite representation with nonzero beta. It does not say that smooth functions cannot be approximated in it, or that smooth limits are radial. The required Cartesian compatibility may be approached as the angular degree increases. At beta=0 the intersection lemma fails, and the usual nonradial polynomial Taylor jets are available. A different representation that incorporates physical Cartesian angular factors is outside the theorem.

The radial theorem uses the canonical full-plane inverse, the supplied sublinear growth assumptions, elementary angular orthogonality and ordinary differentiation. It is a restricted ansatz exclusion, not NO_inf for the full admissible class. No proof assistant verification or general nonlinear existence claim is made.
